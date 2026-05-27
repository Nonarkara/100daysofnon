# 100 Days of Non — Public Surface Refresh (2026-05-27)

**Brief:** render diary day-001/002/003 as visual day-pages reflecting each day's mood. Build as a generator (Markdown → HTML), not hand-coded per day. Ship live via existing GitHub Actions → 100.nonarkara.org.

---

## Plan

- [x] Read repo (README, DESIGN.md, METHOD.md, existing day pages, build_day.py, diary content)
- [x] Diagnose: site/day/003/index.html is rendering stale TKC-ninja content; current diary/day-003/answer.md is the FATHER arc (245 lines, 10 messages, 16 artifacts). Day 2 diary expanded from 4 → 9 messages (Msgs 5–9 added).
- [ ] Write `build.py` — generator: reads `diary/day-XXX/{question, answer, fact-check, narration, telemetry, artifacts}` → emits `site/day/XXX/index.html` with a per-day mood overlay
- [ ] Define three mood registers in `site/data/day-moods.json`:
  - **001 registration** — vintage commerce-certificate aesthetic; 發祥 Chinese characters as motif; cool restraint
  - **002 elegy** — funeral-booklet weight; "I MADE IT" pull; chronological deaths timeline; Paolo + ashes as quiet plates
  - **003 catharsis** — punk loudest; canonical father portrait full-bleed; "PEOPLE WERE WRONG" as six anaphoric lines at max scale
- [ ] Copy artifacts: `diary/day-XXX/artifacts/*.png` → `site/assets/artifacts/day-XXX/`
- [ ] Generate the three day pages
- [ ] Update master `site/index.html` lobby — version stamp v0.1.3, three days active
- [ ] Verification taxonomy (✓ ✗ ? ∅ ⤬ ◆ ⚐) legend on each day page
- [ ] Commit + push → GitHub Actions deploys → verify live at 100.nonarkara.org

---

## Mood-register design notes

Each day inherits scaffolding (nav, 100-day strip, day-counter, 1px vertical rule, telemetry, taxonomy legend). Register varies:

- **Anchor artifact** — Day 3 gets the canonical father portrait full-bleed; Day 1 gets the shop registration as duotone plate; Day 2 puts photos lower (death sequence is more text than image)
- **Type-as-image** — one per day, single line, hard-cropped:
  - Day 1: `發祥 / FA-XIANG / SUWAN PANIT`
  - Day 2: `I MADE IT.`
  - Day 3: stacked anaphora `PEOPLE WERE WRONG` × 6

---

## Files touched

- NEW `build.py` (replaces stub `build_day.py`)
- NEW `site/data/day-moods.json`
- NEW `site/assets/artifacts/day-002/*.png`, `site/assets/artifacts/day-003/*.png`
- REWRITE `site/day/001/index.html`, `site/day/002/index.html`, `site/day/003/index.html`
- EDIT `site/index.html` — version stamp + day-3 status
