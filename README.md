# 100 Days of Non

A 100-day biographical installation. One question per day, answered by Dr. Non. The answers are fact-checked publicly. Memory and record are displayed side-by-side. Where they disagree is the most interesting cell on the page.

The final deliverable is a biography. The site is the artifact while it builds.

---

## The daily loop

1. Non opens Dispatch and asks for today's question.
2. Dispatch sends the question (planned arc in `docs/ARC.md`).
3. Non answers — in chat, as long as he wants.
4. The system captures telemetry (T0 / T2 / T3 / T4), extracts verifiable claims, web-verifies each (`✓` confirmed / `✗` contradicted / `?` unverified / `∅` un-verifiable), narrates the day in a biographer's voice, deploys to the e-portal, and (eventually) pushes voice narration via Telegram in Non's cloned voice.
5. Patterns accumulate. Cross-day contradictions surface automatically.

## Premise

Most biographies are sanitized. This one isn't. The fact-check is brutal but accepts strong claims plainly when verification holds. The mirror is honest in both directions.

## Status

- **Current day:** 1 of 100
- **First question:** filed at `diary/day-001/question.md`
- **Bot push channel:** OpenClaw `@DrNonOpenClaw_bot` (Biographer persona, planned), 21:00 Asia/Bangkok daily
- **E-portal:** to be deployed at a subdomain TBD
- **Visual register:** see `docs/DESIGN.md` — black, white, chartreuse `#CCFF00`. Punk-chaotic-minimalism.

## Versioning

v0.1.0 — scaffolding landed. Each day shipped is a patch bump. Each phase boundary is a minor bump.
