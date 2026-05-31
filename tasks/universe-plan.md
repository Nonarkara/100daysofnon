# Plan — "The Universe, made one" (the completeness capstone)

*2026-06-01. The one important thing: turn five scattered surfaces into one coherent, navigable, finished work — cleanly, working with existing code, without disturbing the book.*

## Current state (surveyed)
- `/` biography (main.css) · `/workshop/` (workshop.css, dark) · `/portrait/`, `/atlas/`, `/questions/` (each with **duplicated inline warm CSS**).
- Cross-links inconsistent; book → workshop only; no map of the whole.

## The mess to clean
1. Three inline copies of the same warm-surface system (portrait/atlas/questions) → **drift risk**.
2. Ad-hoc, inconsistent cross-navigation.
3. No single place that presents the whole universe.

## Deliverables (one objective, executed cleanly)
1. **`assets/css/surface.css`** — extract the shared warm-surface system (palette, type, eyebrow/title/toprule/method, movement, colophon) into one stylesheet. Add a canonical **`.universe-nav`** component.
2. **Refactor** portrait / atlas / questions → link `surface.css`; keep ONLY page-specific rules inline. Verify pixel-identical render (no regression).
3. **`/universe/index.html`** — a Vignelli map of the project: the biography as the trunk, the four companions as stations on one amber line, each with a one-line and a live stat. The capstone index.
4. **Consistent `.universe-nav`** on all warm surfaces + universe (current entry marked `aria-current`), replacing ad-hoc `.back` lists.
5. **Book + workshop**: a single quiet link into the universe map (book stays sacred — minimal touch; repoint the existing cover/footer link).

## Guardrails
- Book (`/`) is anti-regression sacred: only repoint existing links; no structural change.
- Doctrine held: one amber accent, no rounding/gradient/shadow, Literata/JetBrains Mono, phone-first, real data.
- Verify every surface (desktop + mobile) renders unchanged except the intended additions.
- Document: README, vault project note, this plan, clean commits.

## Verify
- curl each surface live; confirm surface.css loads; confirm nav present + current-marked; confirm portrait still recomputes, atlas rail intact, questions intact; mobile no-overflow.
