# Phuket SMART Bus Work Order 02 — Install privacy-first analytics on `bus.nonarkara.org`

**Filed:** 2026-07-17 by Claude/Cowork (Orchestrator, SPADA).
**Trigger:** Non greenlit 2026-07-17 ("sure") in response to the recommended-item list on [[WO-01]].
**Priority:** **Ship BEFORE the mobile rewrite begins**, so we have baseline mobile-vs-desktop split to measure the fix against.

## The pick — Plausible or Umami

Both are privacy-first, cookieless, GDPR-compliant, self-hostable, open-source. Both give the same essential data (pageviews, unique visitors, referrers, top pages, country, device class, browser).

| | **Plausible** | **Umami** |
|---|---|---|
| License | AGPL-3.0 self-hosted (or hosted paid) | MIT self-hosted (or hosted paid) |
| Stack | Elixir + Postgres + Clickhouse | Node.js + Postgres/MySQL |
| Coolify one-click install | ✅ yes | ✅ yes |
| Resource footprint on small VPS | Moderate (Clickhouse) | Light (Node + Postgres) |
| UI polish | Higher | Very good |
| Real-time dashboard | ✅ | ✅ |
| Custom events / goals | ✅ | ✅ |

**Recommendation: Umami** for this deployment. Lighter footprint on the shared Coolify VPS ([[Input 60]]), MIT license means fewer downstream questions, UI is fine for what Non needs. Plausible would be a defensible choice too — either works.

## Scope

1. **Install** Umami on the Coolify VPS via one-click template
2. **Create sites** for `flood.nonarkara.org` + `bus.nonarkara.org` (both projects benefit from analytics ahead of the FloodDash phase-1 work + Phuket bus mobile rewrite)
3. **Add tracking snippets** to both sites' HTML `<head>` (one line each, no build changes)
4. **Verify** hits appearing in Umami dashboard within ~5 minutes of first pageview
5. **Set device/viewport goals** so mobile-vs-desktop split is explicit in the top-level dashboard (not just buried in a segment)

## Non-side approvals

- **Coolify hosting cost** — Umami self-hosted adds ~$0 to the existing Coolify VPS from [[Input 60]] (already provisioned or provisionable). No new cost line.
- **Privacy notice on bus.nonarkara.org + flood.nonarkara.org** — Umami is cookieless and privacy-first, so no GDPR-consent banner is required, but a one-line footer *"Analytics via Umami (cookieless, privacy-first, self-hosted)"* is honest hygiene and matches the Honesty-Layer discipline. **Not a blocker; just a polish item.**

## Routing per SPADA

- **Me (Claude/Cowork, orchestrator):** wrote this WO. Available to draft the "About the data" footer text (my zone).
- **Codex (services):** Umami installation on Coolify + tracking-snippet insertion into both sites. Straightforward — this is the routine services-layer work Codex is optimized for.
- **Antigravity (frontend):** no direct action needed; tracking snippet is a `<script>` tag insertion. If Antigravity is already doing the mobile rewrite, they can drop the snippet in as part of that work.
- **Non (Lead Architect):** approve Coolify VPS spin (if not already up) + approve the privacy-footer text before it ships.

## What we should see after 2 weeks of data

- **Mobile-vs-desktop split** on `/ops` — currently guessing; this will tell us how important the mobile rewrite actually was
- **Peak-hour usage pattern** — do users hit `/ops` at flight-arrival peaks, or is it continuous ambient monitoring? This informs whether real-time updates or scheduled digests matter more.
- **Referrer sources** — is `/ops` reached directly (bookmarks by airport staff) or via Google / social / DDPM/TMD backlinks? Different referrer profiles imply different audience assumptions.
- **Same for `flood.nonarkara.org`** — device split, peak hours, referrers; will inform [[FloodDash WO-01]] phase-1 subscription-tier design (province rollup vs sensor-specific subscriptions).

## Cross-references

- [[Phuket Bus WO-01]] — the mobile rewrite this analytics install baselines against
- [[FloodDash WO-01]] — same benefit for the FloodDash project
- [[Input 60 Ultraboost Integration Map]] — the Coolify VPS this Umami install rides on
- [[reference_spada_team_architecture_and_my_role]] — routing above
- [[feedback_no_localhost_ship_principle]] — Umami self-hosted on Coolify is the on-brand implementation
