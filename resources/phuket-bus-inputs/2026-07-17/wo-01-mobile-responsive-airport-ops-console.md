# Phuket SMART Bus Work Order 01 — Mobile-responsive redesign of `/ops` (Airport Ops Console)

**Filed:** 2026-07-17 by Claude/Cowork (Orchestrator, SPADA) per Non's request.
**Trigger:** Non's screenshot 2026-07-17 of `bus.nonarkara.org/ops` on mobile with the comment *"The Phuket SMART Bus project looks cramp on the phone."*
**Live URL:** https://bus.nonarkara.org/ops (production)
**Priority:** **HIGH** — this is a live public-facing operational dashboard on Non's personal domain; broken mobile view is a credibility hit.

## Diagnosis — nine specific defects visible in the screenshot

Reading the screenshot in reading order, mobile-viewport width ~360–420 px:

| # | Defect | Location | Severity |
|---|---|---|---|
| 1 | **Title breaking vertically** — "AIRPORT / OPS / CONSOLE" wraps into 3 lines squeezed against day tabs | Header | High — sets a broken first impression |
| 2 | **KPI-row values shattered mid-word** — "arriving / pax / this…" with visible truncation "…"; "255 · seats / 25 ·"; "SHORTFALL / 415 pax @ 12:00" not readable as a coherent line | KPI strip below header | High — the *primary decision-support numbers* are illegible |
| 3 | **Card overlap / z-index bug** — the "DEMAND QUEUE 220 / SUPPLY ROLLING 25" card is *layered on top of* both the ARRIVALS BY REGION column (left) and the SUPPLY & IMPACT column (right); left-column region rows are hidden behind it | Mid-page | Critical — content is invisible, not merely cramped |
| 4 | **Column headers wrap uglily** — "SUPPLY & / IMPACT" and "FLEET / CAPACITY" wrap to two lines with mid-word breaks | Mid-page column headers | Medium |
| 5 | **Sidebar labels without data** — "ARRIVALS BY REGION" column shows labels (SE Asia, Other, China, East Asia, Russia/CIS, India) but no visible bar values | Left column | High — the region breakdown is functionally missing |
| 6 | **Map squeezed to ~40% of available width** — the map has room to be full-width but is constrained by the surrounding grid | Center-lower | Medium — a map at this size loses geographic legibility |
| 7 | **Body prose wraps 3–4 words per line** — "Schedule- / derived / fleet size / across 3 / routes. / Headway / varies by / demand…" | Right column | Medium — text becomes staircase-shaped |
| 8 | **Bottom KPI strip clipped right-side** — "120 PAX DELIVERED" visible; "฿" starts to appear then cut off; the strip continues off-screen with no horizontal-scroll affordance | Bottom KPIs | High — data lost off-screen without hint |
| 9 | **"FLIGHT SCHEDUL…" label truncated left** | Left column, lower | Low |

## Root cause — desktop-first grid with no mobile breakpoints

This is a classic desktop-first CSS grid / flex layout being forced into a ~400 px viewport without responsive breakpoints or a mobile-specific layout. The alert banner at top (yellow ⚠ card with "220 pax in the airport queue now · 1,214 already walked away today (฿121,400 lost). Next departure absorbs 25. Dispatching 5 standby buses clears the current queue.") **works correctly on mobile** — it's the one component that reflows properly. Everything below it treats the mobile viewport as a scaled-down desktop.

## The one thing that works exactly right — preserve this

**The alert banner.** It's high-signal, high-priority, action-oriented, uses appropriate warm-alert color, has a clear recommended action ("Dispatching 5 standby buses clears the current queue"), and reflows cleanly. This is the *pattern* the rest of the ops console should imitate for mobile: **priority information first, in single-column vertical rhythm, with recommended actions attached.**

## Proposed mobile layout (single-column vertical rhythm)

Following Non's design discipline ([[CLAUDE.md]] — Rams + Vignelli, Template Poison list — no rounded corners >4 px, no gradients, no cramped padding, no decorative shadows, no icon bloat, minimum 16 px internal padding preferred 24 px):

```
┌──────────────────────────────────┐
│ ⚠ ALERT BANNER  (unchanged)      │
│   220 pax queued · 1,214 walked  │
│   ฿121,400 lost                  │
│   → Dispatch 5 standby buses     │
├──────────────────────────────────┤
│ AIRPORT OPS CONSOLE              │
│ Mon · Jul 20                     │
├──────────────────────────────────┤
│ ← Mon Tue Wed Thu Fri Sat Sun → │  (horizontal scroll if needed)
├──────────────────────────────────┤
│ NOW                              │
│ Arriving pax this hour:  255     │
│ Seats:                    25     │
│ Shortfall @ 12:00:       415 pax │
├──────────────────────────────────┤
│ DEMAND / SUPPLY                  │
│ 220 waiting at airport curb      │
│ 25  buses moving now             │
├──────────────────────────────────┤
│ FLEET CAPACITY                   │
│ 34 buses required                │
│ 19 in service                    │
│ (Schedule-derived across 3       │
│  routes. Headway varies by       │
│  demand.)                        │
├──────────────────────────────────┤
│ MAP  (full-width, 60vh tall)     │
│ ┌────────────────────────────┐   │
│ │       Phuket route map     │   │
│ └────────────────────────────┘   │
├──────────────────────────────────┤
│ ARRIVALS BY REGION               │
│ SE Asia       ████████ 85        │
│ China         █████    52        │
│ East Asia     ███      38        │
│ India         ██       21        │
│ Russia/CIS    █        12        │
│ Other         █        47        │
├──────────────────────────────────┤
│ FLIGHT SCHEDULE                  │
│ (grouped by hour)                │
├──────────────────────────────────┤
│ TODAY SUMMARY                    │
│ 19 buses now · 3 trips today     │
│ 139 km · 120 pax · ฿[revenue]    │
└──────────────────────────────────┘
```

**Design principles applied:**
- Single column ≥ 320 px wide
- Every card gets 16–24 px internal padding
- Section headers use consistent weight + spacing
- KPI numbers get their own line, unit spelled out
- Map is full-width and generous height (60 vh minimum) — this is the geographic decision-support tool, not a decoration
- Region bars use horizontal bar chart, not sparklines
- No horizontal-scroll surprises — if content needs scroll, use an *explicit* horizontal-scroll strip with fade-edge affordance
- No rounded corners >4 px, no gradients, no shadows, no icon-only labels

## Recommended breakpoints

- **≤ 480 px** — mobile single-column layout above
- **481–768 px** — 2-column: KPIs left, map+regions right
- **769–1199 px** — 3-column current desktop layout with tighter gutters
- **≥ 1200 px** — current desktop layout as-is

## Routing per SPADA

- **Me (Claude/Cowork, orchestrator):** wrote this design review + Work Order (docs/architecture/specs zone). Can also draft the *design-tokens spec* (breakpoint values, spacing scale, font sizes) as a follow-up in my zone.
- **Antigravity (frontend, browser-verified):** primary implementer for this Work Order. Zone is shared-frontend with Work Claim discipline. Full mobile-responsive rewrite of `/ops` view, browser-verified against real iPhone Safari + Chrome Android at 360, 390, 414, 428 px viewports.
- **Codex (services):** likely no service-layer changes required for this Work Order; the data is the same, only the presentation changes. Codex may need to be looped in if any API-shape change is discovered during frontend work.
- **Non (Lead Architect):** approve the design direction above (or return with corrections) before I file the AGENT_NOTES.md D-E-R routing this to Antigravity. This is the irreversible-action gate — once shipped to production, the mobile experience is what users see.

## Ops-note — three things Non can approve today

1. **Design direction greenlight** — approve the mobile layout sketch above (or return corrections) so I can file the Antigravity Work Claim
2. **Optional intermediate ship:** while Antigravity does the full rewrite (est. 4–8 hours), we could ship a **one-line CSS emergency patch** that sets `overflow: hidden` on the offending overlapping card and adds `max-width: 100vw; overflow-x: auto` on the outer container. This wouldn't fix the design but would eliminate the *visible defect* (item #3 above — the card overlap) in ~10 minutes of Codex work. **Not recommended** — better to do the mobile layout right — but available as an escape valve if the current view is embarrassing you in front of stakeholders today.
3. **Analytics greenlight** — install a lightweight anonymous analytics tag (Plausible or Umami, both self-hostable on the Coolify VPS from [[Input 60]]) to measure actual mobile-vs-desktop split on `/ops` traffic. Without this we're guessing at how important mobile is. **Recommended: yes, ship this before the rewrite starts** so we have a baseline to measure the fix against.

## Cross-references

- [[FloodDash Work Order 01]] filed today — same day, same SPADA routing pattern, same *"Non owns approvals, I write specs, Codex/Antigravity implement"* choreography
- [[Input 60 — Ultraboost Integration Map]] — the Tier-A **Taste Skill** + **Designer Skills** installs directly serve this Work Order; if those are installed before Antigravity starts, output quality goes up meaningfully
- [[Input 60]] — the Coolify VPS is the natural host for Plausible/Umami analytics
- [[Non's CLAUDE.md]] — Template Poison list; the mobile redesign must not introduce rounded corners >4 px, gradients, decorative shadows, template typefaces, etc.
- [[reference_spada_team_architecture_and_my_role]] — the routing above
- [[feedback_no_localhost_ship_principle]] — this project is already correctly hosted at a public URL; the fix ships to the same URL
- [[feedback_always_mvp_make_it_exist_first]] — the current version *exists*, which is right; now it needs to be *good* per your "make it work now, make it good later" philosophy
