# Devlog

One entry per meaningful work session. Dated. What shipped + what's next + open questions.

---

## 2026-05-24 — Scaffold landed (v0.1.0)

**Shipped:**
- `README.md` — premise, daily loop, status
- `docs/ARC.md` — all 100 questions framed; Days 1–15 precisely worded, later phases framed-and-sharpened-night-of
- `docs/METHOD.md` — daily loop, telemetry spec, fact-check rules, cross-day contradiction logic, narration, theme system, Phase 4 consent gate, refusal handling, versioning
- `docs/DESIGN.md` — visual register locked: black / white / chartreuse `#CCFF00`, Akzidenz-Grotesk + JetBrains Mono, broken grid, hard bans on rounded corners / gradients / shadows / templates
- `docs/DEVLOG.md` — this file
- `diary/day-001/question.md` — already-asked Day 1 question

**Open and queued:**
- Code task `100 Days of Non — scaffold v1` was spawned twice, both timed out (workspace approval prompt unanswered). The full code-task scaffold (pipeline scripts, e-portal Next.js skeleton, biographer persona, cron config) is still pending. The user created the folder manually so Dispatch could scaffold the docs side via direct file tools; the pipeline + e-portal side waits on the code task spawn landing.
- Biographer persona on @DrNonOpenClaw_bot: not wired. Daily push channel is currently Dispatch chat itself; Telegram push activates when the OpenClaw Biographer persona is configured.
- Voice-clone narration: depends on the separate OmniVoice/XTTS work.
- Theme overlay: deferred to ~Day 25, picked from what Phase 1 reveals.

**Decisions logged:**
- Project name: `100daysofnon` (lowercase, no hyphen) — created by user, accepted.
- Accent color: chartreuse `#CCFF00`.
- Daily push time: 21:00 Asia/Bangkok.
- Phase 4 (romantic life) consent policy: to be locked before Day 36. Default if Non doesn't specify by Day 30: pseudonym in public surface, real names in archive.
- Isaacson framing: dropped from the public premise. The project is what it is; no biographer comparison anchor.
- Refusal is a valid answer and gets logged structurally.

**What's next:**
- Day 1 — Non answers the birth question. Telemetry captured (T3 from the moment he sends the first message in this chat). Fact-check runs against birth-year claim and any further verifiable details he includes.
- Once the code task spawns, the e-portal goes up at a TBD subdomain. Day 1 page renders.
- Day 2 question fires tomorrow at 21:00 Bangkok via Dispatch (Biographer persona activates when wired).

---

## 2026-05-25 — Day 1 answered

**Answer received** via Dispatch chat (Biographer persona not yet wired so precise telemetry deferred — word count and message count captured exactly; latency approximated as "same-evening").

**Fact-check result:** 3 ✓ confirmed, 1 ✗ contradicted, 3 ? unverified, 3 ∅ un-verifiable, across 10 extracted claims.

- ✓ Birth date November 1, 1981 — calendar matches Sunday
- ✓ Hospital: Phyathai (Payatai) — Phyathai Hospital Group, address in Ratchathewi consistent with stated proximity to the family's location
- ✓ Day of week: Sunday — confirmed via calendar arithmetic
- ✗ "Near Siam Paragon" — Siam Paragon opened December 2005; family could not have lived "near Siam Paragon" in 1981. Logged as a present-day-landmark slippage, not a memory error, but the literal claim is false.
- ? Age at move to current house; ? "42 years in current house" (within stated precision); ? father built the house — all resolvable with the photo albums Non offered
- ∅ Brother six years older; ∅ mall-loss incident; ∅ comparative self-assessment

**Narration written.** Tone landed cold but generous, as `docs/METHOD.md` specifies. The Siam Paragon flag is framed as grammar, not gotcha.

**Open thread:** Non offered the photo albums his father took of the house construction. If shared as artifacts, they resolve the three `?` claims and may add new verifiable claims (move date, address, family composition). Filed as standing invitation, not pressure.

**Day 2** fires next day at 21:00 Asia/Bangkok via Dispatch (Biographer Telegram persona still not wired — daily push remains chat-based until then). Day 2 question pulled from `docs/ARC.md`: mother's full name, birth year, city, occupation when Non was five, and the one story she tells about him most often.

---

## 2026-05-25 — Day 1 expansion (Message 2) + updated fact-check

Non answered the fact-check by going *back in time* with much more texture. Total Day 1 answer is now 999 words across 2 messages. Updated fact-check has **27 extracted claims**: 9 ✓, 2 ✗, 7 ?, 6 ∅.

**The mechanic worked as designed.** The first ✗ (Siam Paragon) made Non self-correct and produce a much richer historical-architectural reconstruction: Siam Intercontinental Hotel (1966–2002, demolished for Siam Paragon), the hat-shaped roof, the FLW-tradition American architect, the surrounding park, the wedding receptions, the 2002 Australian student-affairs expo. He then mapped the family's daily walking geography: row house → elephant-headed bridge → Khlong Saen Saep → Sra Pathum Palace → beer garden → science center → Siam Square. Mother's commute to Krung Thai Bank HQ on Sukhumvit. Maternal grandmother's eminent-domain story as the origin of the current house. Pantip Plaza for the mall-loss incident, with later-life architectural reading of the columns (Doric / Ionic).

**One additional contradiction surfaced in the expansion**: "Paris style of Frank Lloyd Wright." Wright had no Paris style — Prairie, Usonian, Organic only; he was famously anti-Beaux-Arts. Logged as ✗. Non is reaching for a nearby anchor at the level of specificity he naturally thinks at; this is the recurring drift mode the project will keep surfacing.

**New artifact invitations opened**: row-house photos, family land records / eminent-domain documentation, period photos of Pantip Plaza interior (to resolve the Doric/Ionic claim), Siam Intercontinental wedding-or-expo photos.

**Methodological observation:** Day 1 demonstrates that the public fact-check is *generative*, not just adversarial. The first slip → a 4x richer answer. This pattern is likely to recur. The project's central artistic mechanic — the unreliable-narrator-made-structural — is producing material as designed.

**Day 2** holds at 21:00 Asia/Bangkok unless Non wants to keep going on Day 1 first (he was offered the choice).
