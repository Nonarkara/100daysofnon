# FloodDash Work Order 02 — LINE OA message throttling rules (economical alerting under free-tier constraint)

**Filed:** 2026-07-17 by Claude/Cowork (Orchestrator, SPADA) per Non's request.
**Trigger:** Non 2026-07-17 — *"Line messaging is back for the FloodDash project again. Unlike Telegram where we relay every warning to, set rules as we need to be more economical since Line only allows 300 free messages per month."*
**Priority:** **HIGH** — LINE quota exhaustion mid-monsoon is a life-safety operational risk; rules must ship before quota is consumed.

## The constraint, quantified

**LINE OA Communication Plan (free tier):** **300 messages/month** — where *"messages"* = **individual send-events** to each recipient.

- 1 broadcast × 100 subscribers = **100 messages** consumed
- 1 broadcast × 1,000 subscribers = **1,000 messages** consumed — already 3.3× over budget in one broadcast

**Implication:** at any meaningful subscriber count, **the broadcast model is architecturally incompatible with the free tier.** The throttling rules below reduce burn per broadcast; the phase-3 per-user subscription model from [[wo-01-sensor-level-granularity-and-source-taxonomy]] eliminates the burn-per-broadcast problem structurally.

**Snapshot of current burn rate** — the Line screenshot Non filed earlier 2026-07-17 showed 3 broadcasts in 90 minutes (1:20 / 1:50 / 2:20 PM). At 100 subscribers, that's 300 messages in one afternoon — full monthly quota gone.

## The throttling rules — six layers

### Rule 1: Severity-tiered delivery

Every alert gets classified into one of four tiers based on score:

| Tier | Score threshold | Line broadcast? | Telegram broadcast? | Notes |
|---|---|---|---|---|
| **CRITICAL** | ≥ 70 | ✅ Immediate, no consolidation, no silent-hours suppression | ✅ Immediate | Life-safety priority; must not throttle |
| **HIGH** | 45–69 | ✅ Consolidated (see Rule 2) | ✅ Immediate | Current default alert level per the screenshot |
| **MODERATE** | 30–44 | ❌ Not broadcast to Line | ✅ Immediate | Telegram fire-hose only |
| **LOW** | < 30 | ❌ | Optionally logged only | Ambient state |

**Rationale:** the current system broadcasts every HIGH-tier event to Line, which is unnecessary. HIGH does not require the same real-time-per-event cadence CRITICAL does.

### Rule 2: Consolidation window for HIGH tier

Bundle multiple simultaneous province changes into a **single broadcast per rolling window**:

- **Window size:** 3 hours (tunable per season)
- **Window content:** consolidated summary of all provinces that entered HIGH or changed score within the window
- **Format example:** *"FloodDash แจ้งเตือน (13:00-16:00) · จ.สตูล 48, ฉะเชิงเทรา 46, นครศรีธรรมราช 45, สุพรรณบุรี 46 → เสี่ยงสูง · ดูรายละเอียด: flood.nonarkara.org"*

**Effect:** the current 3-broadcast afternoon in the screenshot collapses to **1 broadcast**. Immediate 3× reduction in burn.

### Rule 3: Deduplication for same province within same tier

If a province is already at HIGH and its score updates from 46 → 48 (still HIGH), **do not broadcast again**. Broadcast only on:
- Tier transitions (MODERATE → HIGH, HIGH → CRITICAL)
- Threshold crossings within CRITICAL (e.g., 70 → 85 in same tier could warrant re-broadcast per severity policy — TBD)
- Explicit resolution notice (HIGH → MODERATE clears; broadcast a **one-line consolidated "all-clear" digest** at end of window)

### Rule 4: Silent hours (22:00–06:00 ICT)

- **CRITICAL alerts** — always sent immediately, override silent hours (life-safety)
- **HIGH alerts** — held for the 06:00 morning digest
- **MODERATE + LOW** — Telegram-only regardless

**Rationale:** most non-critical LINE notifications received at 03:00 will be seen at 06:00 anyway; the intervening broadcast is quota-burn without informational value.

### Rule 5: Budget-accounting + escalation

Persist a monthly message counter (Postgres/Timescale time-series, resets on 1st of month at 00:00 ICT).

**Escalation thresholds:**

| Consumed | Action |
|---|---|
| 0-70% (0-210) | Normal operation |
| 70-85% (210-255) | Log warning; internal metric on dashboard |
| 85-95% (255-285) | Non receives a **per-day summary email** with remaining budget + current-day usage |
| 95-100% (285-300) | Switch HIGH-tier broadcasts to **Telegram-only + morning email digest**; CRITICAL still broadcasts to LINE |
| Over 100% | Hard block on non-CRITICAL LINE broadcasts; log every skipped alert with reason |

**Non-approval needed** on the *over-100%* fallback: either (a) hard-block non-critical (recommended, default), (b) upgrade to Light Plan (5,000 msg/mo @ ฿1,200), or (c) case-by-case Non manual approval. **Default proposed: (a) hard-block, with the *"we can upgrade to Light Plan for ฿1,200/mo"* offer surfaced in the near-quota email.**

### Rule 6: Telegram remains the fire-hose

Every alert of every tier continues to broadcast on Telegram unchanged (Telegram bots have effectively no cost or throttle for legitimate use). Telegram is the **complete-record channel**; LINE is the **must-see-immediately channel**.

Language on both platforms should acknowledge the difference: LINE messages carry the phrase *"เฉพาะเหตุเสี่ยงสูงหรือวิกฤต"* / *"HIGH or CRITICAL alerts only"* so subscribers understand they are receiving the filtered subset.

## Why this is a stopgap — the architectural answer is phase 3 of [[wo-01]]

The rules above will keep FloodDash inside the LINE free tier at the *current* ~100-subscriber scale. **They will not scale.** At 1,000 subscribers, even one CRITICAL broadcast consumes 1,000 messages — more than 3× the free-tier monthly budget.

**The structural answer is [[wo-01 phase 3]]: sensor-specific per-user subscriptions.**

Under per-user subscriptions:
- Each user opts into specific stations relevant to their area (home / office / farm / commute)
- Alerts are sent as **1:1 push notifications**, not broadcasts (LINE OA counts these differently — 1:1 messages via the LINE Login/OAuth channel have different quota rules than OA broadcasts)
- 1,000 subscribers with 3 stations each = 3,000 subscriptions; a single station's HIGH alert reaches only the ~few subscribers watching that station = ~5-50 messages instead of 1,000

**Recommendation for the roadmap:** ship WO-02 throttling this month (fast, small-Codex effort), and prioritize WO-01 phase 3 subscription work as the Q4 2026 architectural milestone.

## Concrete Codex implementation tasks

Suggested order (each item small, individually shippable):

1. **Add tier classifier** to the alert-emission code path (CRITICAL / HIGH / MODERATE / LOW based on score thresholds). Emit tier in the alert-event data structure.
2. **Add consolidation buffer** — a 3-hour rolling window per tier that batches HIGH-tier events, flushes as a single broadcast.
3. **Add deduplication cache** — per-province tier state; skip broadcast if same province + same tier is already the last-broadcast state.
4. **Add silent-hours schedule** — configurable 22:00-06:00 ICT hold-and-defer for non-CRITICAL.
5. **Add monthly message counter** — Postgres/Timescale table `line_message_ledger`; increment on every successful send; expose `/api/line-budget` for internal dashboard.
6. **Add escalation triggers** — cron/scheduled job checks counter at 06:00 ICT daily; emits warning-email / hard-block based on thresholds.
7. **Add "filtered subset" copy** in LINE broadcast template — one-line reminder that Telegram carries the fire-hose.
8. **Add integration tests** — synthetic alert stream reproducing the 2026-07-17 screenshot scenario; assert 1 broadcast emitted instead of 3.

**Estimate:** 1-2 days of Codex work total; each item individually testable.

## Non-side approvals required

Per SPADA (Non holds irreversible-action gate + configuration decisions):

1. **Severity thresholds (45 / 70 / 30 boundaries)** — approve, adjust, or ask for research on how DDPM / TMD / RID define severity. **Proposed defaults are educated guesses; Non should validate against actual Thai flood-authority conventions.**
2. **Consolidation window size** — 3 hours is a starting number; peak monsoon may want 1 hour, dry season 6 hours. Default 3h; make it a config value.
3. **Silent hours 22:00–06:00 ICT** — approve or adjust.
4. **Over-budget fallback policy** — (a) hard-block / (b) upgrade to Light Plan ฿1,200/mo / (c) case-by-case. **Recommended: (a) with (b) surfaced as an opt-in escalation.**
5. **Confirm current LINE OA free-tier is 300** — LINE has adjusted plans multiple times; **worth 5 minutes verifying at the LINE for Business Thailand page before committing rules based on 300 as the exact number.** Rules scale to whatever the correct number is; the *architecture* doesn't change.

## What NOT to do

- ⚠️ **Do not throttle CRITICAL-tier alerts** for any budget reason. Life-safety.
- ⚠️ **Do not present the LINE-throttling as a *reduction in service*** on public materials. Frame it as *"LINE gets high-priority alerts; full alert stream on Telegram."* Same information available; different channel.
- ⚠️ **Do not ship without an escape valve.** If the throttling rules bug-out and start blocking critical alerts, there must be a manual override. Recommend a Non-owned kill-switch in the config (`line_throttling_enabled = true|false`).
- ⚠️ **Do not treat this WO as a substitute for [[wo-01 phase 3]]** — the subscription-model architectural fix is still required for the next scale-order.

## Routing per SPADA

- **Me (Claude/Cowork, orchestrator):** wrote this WO (docs/architecture/specs zone). Available to draft the LINE / Telegram user-visible language changes (my zone) once you greenlight the direction.
- **Codex (services):** all 8 implementation tasks above. Await Non greenlight + I file the D-E-R in AGENT_NOTES.md.
- **Antigravity (frontend):** no direct action for this WO; possible follow-up work if `/api/line-budget` gets a dashboard-visible surface.
- **Non (Lead Architect):** the 5 approvals in the section above.

## Cross-references

- [[wo-01-sensor-level-granularity-and-source-taxonomy]] — the sensor-granularity WO this rides adjacent to; phase 3 is the architectural fix that makes throttling largely unnecessary at scale
- [[reference_spada_team_architecture_and_my_role]] — routing pattern
- [[feedback_no_localhost_ship_principle]] — flood.nonarkara.org is on-brand; the throttling changes are backend-only
- [[feedback_always_mvp_make_it_exist_first]] — throttling ships now; subscription architecture ships when Codex + you have bandwidth
- [[Horizon Input 61 — LINE OA MCP]] — the emerging LINE-native automation stack; a future FloodDash could use MCP for subscription management via natural-language
- LINE for Business Thailand: https://linebiz.com/th/ (verify current free-tier limit before committing rules)
