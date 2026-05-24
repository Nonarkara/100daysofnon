# Method

How the daily loop runs. Read this before touching the pipeline scripts.

---

## Daily loop

1. Non opens Dispatch and asks for today's question.
2. Dispatch reads `docs/ARC.md` for the day-number's question and (when wired) pushes via OpenClaw's Biographer persona to Telegram at 21:00 Asia/Bangkok.
3. Non answers — in chat, as long as he wants. Long-form prose is the default; bullet lists are allowed; pure refusal is allowed and logged as the answer.
4. `telemetry.py` captures timestamps and writes `diary/day-XXX/telemetry.json`.
5. `intake.py` orchestrates: fact-check → narrate → analyze (cross-day) → deploy.
6. Day's page is published to the e-portal.

---

## Telemetry

Per-day file `diary/day-XXX/telemetry.json`:

| Field | Meaning |
|---|---|
| `T0` | Question pushed to Telegram (UTC + Bangkok local) |
| `T1` | Read receipt — omitted if Telegram bot API doesn't expose it |
| `T2` | Typing-action received (Telegram bot API exposes `sendChatAction` events) |
| `T3` | First response message timestamp |
| `T4` | Last response message timestamp within 60 minutes of T3 with no intervening bot push |
| `latency_ms` | T3 − T0 |
| `composition_ms` | T4 − T3 |
| `open_to_type_ms` | T2 − T0 if available |

The dashboard surfaces these obsessively. Per-day stat block, accumulated trend, day-of-week analysis. If Non's median latency drifts past 24 hours, that's data too.

---

## Fact-check rules

For every answer:

1. Extract verifiable claims — dates, places, names, numbers, public events, credentials, employers, exact quotes attributed to others.
2. Web-verify each. Targeted sources first (Wikipedia, university registries, news archives, public records, GitHub commits with timestamps when relevant); search engines second.
3. Tag each claim:
   - **`✓` verified** — record agrees with claim
   - **`✗` contradicted** — record disagrees with claim; record's version shown
   - **`?` unverified** — couldn't find evidence either way
   - **`∅` un-verifiable** — private, non-public, no plausible source (e.g., "my mother said X to me in 1989")
4. Display all four states publicly on the day's page. Contradicted cells get the chartreuse accent. No color softening anywhere else.

**Tone is cold.** When confirmed, state confirmed + citation. No celebration. When contradicted, state contradiction + citation + the recorded reality. No editorial cushion.

**When a strong claim verifies, state it plainly without diminishment.** The system isn't out to undermine; it's out to test. Confirmed credentials (Harvard PhD, MIT master's, Oxford master's, IDEO, Sydney University, Golden Panda Design Award) read as confirmed, full stop. No "Non claims and indeed it appears" — just "✓ confirmed via [source]."

---

## Cross-day contradiction detection

`analyze.py` runs nightly. Builds a claims index across all `diary/day-*/fact-check.md`. When a Day-N claim contradicts a Day-M claim (M < N), surfaces:

- A flag on Day N's page ("contradicts your Day-M answer: …")
- An entry in the day's `patterns.md`
- A persistent row in the top-level patterns dashboard

Example: Day 1 says "born at Bumrungrad Hospital," Day 47 says "born at Siriraj." Both can't be true. The flag shows both, with the citation for whichever (if either) the public record supports.

This is the project's most artistically interesting mechanic. The unreliable narrator made structural.

---

## Pattern discovery

`analyze.py` also runs nightly across all accumulated days:

- Latency trend — median, drift, day-of-week effect, are answers getting faster or slower
- Word-count distribution per phase
- Fact-check pass/fail/contradict ratio over time
- Named-entity recurrence heat-map (which people, places, years recur across days)
- Theme drift — which categories of question get long vs. short answers
- Refusal pattern — which days got "I'd rather not answer this" and what they had in common

Output: top-level `patterns.md` (markdown, append-only — old entries stay, new patterns added as discovered) plus a dashboard widget on the e-portal `/patterns`.

---

## Narration

For each day after fact-check, `narrate.py` writes `diary/day-XXX/narration.md` — a biographer's voice summary in Non's own register: direct, literary, slightly rhythmic. Not a summary of what Non said — a *third-person rendering* of what the day revealed, including what the fact-check contradicted or confirmed. Cold but generous.

When the voice-clone work lands (separate effort), the narration also gets pushed as audio to Non's Telegram via the cloned voice. Until then: text only.

---

## Theme system

The site has a base shell (see `docs/DESIGN.md`). A theme overlay (universe, Chinese cosmology, animal kingdoms, whatever) gets selected around Day 25, informed by what the first phase revealed. Don't pre-pick. The theme is the lens the project chooses, not the lens applied to it.

`themes/` holds candidate lenses as stub files. When the theme is chosen, the chosen file gets a full design treatment and the e-portal swaps to use it.

---

## Phase 4 consent gate

Before Day 36, the project pauses. Non confirms the redaction policy for the romantic-life phase:

- **Pseudonym** — names replaced with consistent pseudonyms in the public surface; archive holds the real names privately.
- **First name only** — first names in the public surface, full names in the archive.
- **Withhold** — public surface shows only the structural shape (year, country, length); names withheld entirely.
- **Full naming with consent** — real names in public, but only after each named person has given verbatim consent.

The choice is logged in `docs/DEVLOG.md` and shown on the e-portal as part of the project's structural honesty. The public surface displays which policy is active. No surprises.

---

## Refusal

A refusal — "I'd rather not answer this today" — is a valid answer. It gets:

- Logged as `answer.md` content
- Fact-check section reads "∅ — no claims to verify"
- Narration acknowledges the refusal in the third person
- Pattern analyzer tracks refusal frequency and topic

Refusal isn't failure. It's data.

---

## Versioning

- v0.1.0 — scaffolding (this state)
- Each day shipped = patch bump (v0.1.1, v0.1.2, …)
- Each phase boundary = minor bump (v0.2.0 at Day 16, v0.3.0 at Day 26, etc.)
- v1.0.0 ships at Day 100

Version surfaces in the e-portal header, in `/health` (when the pipeline service is built), and in every commit's message.
