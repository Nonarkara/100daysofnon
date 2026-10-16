# AGENT_NOTES.md entry — mobile-responsive rewrite of `/ops`

**Copy this D-E-R block to the top of `AGENT_NOTES.md` in the `bus.nonarkara.org` repo (newest-first). If no `AGENT_NOTES.md` exists yet, create one and paste this as the first entry. Also add the ACTIVE CLAIM at the bottom.**

---

## 2026-07-17 · Claude/Cowork (Orchestrator) → Antigravity

**D — Describe.** Mobile view of `/ops` on `bus.nonarkara.org` is broken at ~400 px viewport. Nine specific defects diagnosed (title breaks vertically, KPI values shatter mid-word, `DEMAND QUEUE / SUPPLY ROLLING` card z-index bug hides `ARRIVALS BY REGION` column entirely, bottom KPI strip clips off-screen without scroll affordance, map squeezed to ~40% width, etc.). Full diagnostic + proposed single-column mobile layout + design-token guidance + breakpoints (480 / 768 / 1200 px) in the spec at `resources/phuket-bus-inputs/2026-07-17/wo-01-mobile-responsive-airport-ops-console.md` in the 100daysofnon repo.

**E — Evaluate.** Non greenlit the design direction 2026-07-17 ("sure"). The current live view is credibility-damaging on mobile — it's a production URL on Non's personal domain. Alert banner at top already reflows correctly; that is the pattern the rest of the console should imitate. Design must respect Non's CLAUDE.md Template Poison list (no `border-radius` > 4 px, no gradients, no decorative shadows, no template typefaces, minimum 16 px internal padding preferred 24 px). Data-shape is unchanged — presentation only.

**R — Recommend.** Antigravity implements the mobile-responsive rewrite of `/ops` per the WO-01 spec. Browser-verify against iPhone Safari + Chrome Android at 360, 390, 414, 428 px viewports. No API/service changes expected; loop in Codex if any data-shape change surfaces. Preserve the working alert-banner component as reference for the new mobile rhythm. **Estimated: 4–8 hours.** Ship to production behind whatever preview/staging convention `bus.nonarkara.org` uses; Non gates the production merge.

## ACTIVE CLAIMS

| Agent | Zone | Files/routes | Started | ETA |
|---|---|---|---|---|
| **Antigravity** | frontend | `/ops` view + shared responsive utilities | 2026-07-17 | 2026-07-18 or per Antigravity's queue |

---

**Sourced from:** [[Non's screenshot 2026-07-17]] · [[WO-01 spec]] · [[Non's CLAUDE.md Template Poison list]] · [[reference_spada_team_architecture_and_my_role]]
