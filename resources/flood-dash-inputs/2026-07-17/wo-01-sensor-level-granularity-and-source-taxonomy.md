# FloodDash Work Order 01 — Sensor-level granularity + alert-source taxonomy

**Filed:** 2026-07-17 by Claude/Cowork (Orchestrator, SPADA) per Non's request.
**Trigger:** Non's Line-notifications screenshot 2026-07-17 showing FloodDash 2.0 issuing 4 province-level High-Risk alerts (สตูล 48, ฉะเชิงเทรา 46, นครศรีธรรมราช 45, สุพรรณบุรี 46 twice).
**Non's ask, verbatim:** *"Can we have more information about specific locations or where the sensors are that detect the warnings? That way we can be more specific about the flood mitigation efforts."*

## Current-state audit (inferred from the screenshot)

- Alert unit: **province (จังหวัด)**
- Score scale: **0–100**, with High-Risk threshold appearing ~45
- Source citation in-message: **ปภ./กรมอุตุฯ** (DDPM + TMD)
- Distribution: **Line broadcast** (unverified account — see §Ops-note)
- Frontend: **https://flood.nonarkara.org**
- Alert cadence observed: three broadcasts in 90 min (1:20 / 1:50 / 2:20 PM)
- Alert content: province name + risk-level label + numeric score + link. **No sensor identifier, no coordinates, no sub-district area, no mitigation-actionable target.**

## The gap Non named — why province-level is not enough

A province the size of Nakhon Si Thammarat (~9,900 km², population ~1.55 M, 23 districts, coastal + interior + mountainous) at "High Risk score 45" is *directionally* correct but *operationally opaque.* It cannot:

- Tell a district-level ปภ. officer whether to pre-position pumps in Sichon vs Chawang
- Tell a resident whether their soi is in the affected watershed or a dry ridge
- Tell an insurance underwriter which policies are in the flood cone
- Tell a routing/logistics system which shipments to reroute
- Support the specific-mitigation-effort targeting Non explicitly asked for

## The Thai flood-sensor ecosystem — what actually exists

Six agencies operate real-time flood-related sensor networks in Thailand. **The single richest sub-provincial dataset is HII's thaiwater.net.**

| Agency | Sensor type | Coverage | Real-time API | Sub-provincial resolution |
|---|---|---|---|---|
| **HII** (Hydro-Informatics Institute) — **thaiwater.net** | Water-level telemetry (สถานีโทรมาตร) | ~800+ stations nationwide | Yes | ✅ station-level with lat/lon |
| **RID** (Royal Irrigation Dept.) | Canal + reservoir levels, dam discharge | Major watersheds | Yes | ✅ station-level |
| **TMD** (Thai Meteorological Dept.) | Rain gauges, radar, forecasts | Nationwide | Yes | ✅ station-level, radar tile-level |
| **DWR** (Dept. of Water Resources) | Additional gauges + small watersheds | Complement to RID | Yes | ✅ station-level |
| **GISTDA** | Satellite-derived flood maps | Nationwide | Delayed | ✅ pixel-level (30 m or better) |
| **BMA** (Bangkok Metropolitan Admin.) | Canal levels, pump stations | Bangkok only | Yes | ✅ station-level |

**HII + RID + TMD together = the correct primary-sensor stack** for a Thailand-wide flood dashboard at sensor granularity.

## Recommended FloodDash 2.1 architecture

### Phase 1 — Sensor ingestion (Codex's zone)

1. Ingest **thaiwater.net** station roster (~800 stations) with metadata: `station_id`, `station_name`, `agency` (HII/RID/TMD/DWR), `lat`, `lon`, `province`, `district`, `sub-district`, `river/watershed`, `alert_threshold_m`, `critical_threshold_m`, `historical_max_m`.
2. Poll **thaiwater.net** water-level API on a 15-minute cadence for real-time readings.
3. Persist to time-series store (Postgres w/ TimescaleDB extension, or InfluxDB — Codex's call).
4. Compute per-station: `current_level`, `pct_of_alert_threshold`, `pct_of_critical_threshold`, `trend_last_3h`, `trend_last_24h`.

### Phase 2 — Alert schema restructure (Codex's zone)

Replace the current province-level alert schema:

**Old:**
```
FloodDash แจ้งเตือน
• จ.สตูล ยกระดับเป็น "เสี่ยงสูง" (คะแนน 48)
```

**New:**
```
FloodDash แจ้งเตือน
📍 สถานี [SID_XXXX] — [Station Name]
   ต.[Subdistrict] อ.[District] จ.[Province]
   น้ำที่วัดได้: 4.72 ม. (112% ของระดับเตือนภัย)
   แนวโน้ม 3 ชม.: +18 ซม./ชม.
   พื้นที่เสี่ยงต่อน้ำท่วม: [downstream sub-districts A, B, C]
   ที่พักพิงใกล้ที่สุด: [shelter name + distance]
🔗 ดูรายละเอียด: https://flood.nonarkara.org/station/SID_XXXX
```

Province-level score becomes a *rollup* of the station-level readings, not the primary alert unit.

### Phase 3 — Frontend sensor-map layer (Antigravity's zone)

Add to https://flood.nonarkara.org:
- **Sensor map layer** — every station rendered as a pin, colored by `pct_of_alert_threshold`
- **Sensor detail page** at `/station/{station_id}` — current + 24h/7d/30d history, agency source, upstream/downstream context, nearest shelter + evacuation route
- **Sub-district affected-area overlay** — computed from station readings + downstream watershed model (initial version can use a simple radius/DEM heuristic; full hydrological modelling is a Phase-4 upgrade)

### Phase 4 — Source-taxonomy discipline (docs/specs zone — mine)

Every FloodDash alert should carry a source-type tag so operators + downstream users can reason about *what kind of signal* it is:

| Alert type | Data source | Register |
|---|---|---|
| **🌧 Meteorological Forecast** | TMD rain forecast / radar nowcast | Prospective ("rain expected") |
| **📊 Hydrological Reading** | HII / RID / DWR telemetry | Real-time ("water is here now") |
| **🛰 Satellite Inundation** | GISTDA / Sentinel / Landsat derived | Retrospective/confirming ("flood observed") |
| **🚨 Administrative Warning** | DDPM / provincial governor declaration | Authority ("official warning issued") |

The current alert format conflates these. Separating them lets sophisticated users understand *why* the alert fired.

## Non-side approvals required before Codex implementation

Per SPADA (Non is Lead Architect + irreversible-action gate):

1. **thaiwater.net API terms-of-use review** — is a 15-min polling cadence within acceptable-use? If unclear, contact HII directly. **Non's call.**
2. **Data-hosting cost approval** — a full 800-station × 15-min-cadence × 30-day history is manageable in Postgres/Timescale on a small VPS, but hosting cost should be greenlit. Estimate: <$20/mo on Coolify-deployed VPS ([[Input 60 Ultraboost Map]] proposed this stack).
3. **Line broadcast frequency policy** — sensor-level alerts could produce 10–100× current alert volume. **Line's rate limits + user tolerance both matter.** Recommend: keep the existing province-level rollup as the *default subscription* + offer *sensor-specific subscriptions* (opt-in per station) for power users like ปภ. district officers.
4. **Verified-account application to Line** — the "This account is not verified" banner in the screenshot is a user-trust degrader for a public-safety service. Recommend applying for Line Official Account verification. **Non's call, low urgency but high credibility payoff.**

## Ops-note — what Non can do *today* without waiting on Codex

1. **Add the six-agency source list above** ([[HII]] + [[RID]] + [[TMD]] + [[DWR]] + [[GISTDA]] + [[BMA]]) as an "About the data" page on https://flood.nonarkara.org — that alone raises perceived credibility significantly for the ปภ./academic audience.
2. **Publish the current alert-scoring methodology** (what does score 48 mean vs 45?) — same reason.
3. **Apply for Line verified-account status** — no cost, one form.

Items 1 + 2 are markdown-page updates Non can approve for me to ship immediately. Item 3 needs Non's identity docs.

## Routing per SPADA

- **Me (Claude/Cowork, orchestrator):** wrote this Work Order (docs/architecture/specs — my zone); available to draft the "About the data" markdown page + methodology page (also my zone).
- **Codex:** Phase 1 (sensor ingestion) + Phase 2 (alert-schema restructure) + Phase 4 (source-taxonomy tagging in the alert payload). Await Non's greenlight before I file the AGENT_NOTES.md D-E-R.
- **Antigravity:** Phase 3 (frontend sensor-map layer + sensor detail pages). Await Codex's Phase-1 API + Non's greenlight.
- **Non (Lead Architect):** irreversible-action approvals — API-terms review, hosting greenlight, Line-verification application.

## Cross-references

- [[Input 60 Ultraboost Integration Map]] — the Coolify + n8n + Trigger.dev stack this project's Phase 1 background jobs should ride on
- [[reference_spada_team_architecture_and_my_role]] — the routing above
- [[feedback_no_localhost_ship_principle]] — the deploy discipline (flood.nonarkara.org is already living the principle correctly)
- [[feedback_always_mvp_make_it_exist_first]] — argues for shipping Phase 1 + Phase 2 first, Phase 3/4 iteratively
- [[feedback_teach_dont_silently_fix]] — argues for the source-taxonomy discipline in Phase 4
