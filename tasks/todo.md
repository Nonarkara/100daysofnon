# 100 Days of Non — Museum Build

**Started:** 2026-05-25 (Bangkok) overnight session
**Brief:** Reframe the portal as a museum of Dr Non's mind. Add 6 new rooms. Build a frontend-complete chatbot ready to be wired to Claude API later. The structural-guess pattern is the signature.

---

## Phase 0: Foundation

- [ ] Write this plan
- [ ] Extract nonharvard PDF → `site/data/corpus.json` (101 posts, structured: id, date, title, excerpt, full_text, themes, locations, claims, references)
- [ ] Extract voice anchor → `site/data/voice.json` (forbidden phrases, signature patterns, system prompt scaffold)
- [ ] Extract lexicon entries → `site/data/lexicon.json` (~30 Nonism terms with definitions)
- [ ] Extract timeline events → `site/data/chronos.json` (~25 stations 1981–2026)
- [ ] Extract bot Q&A pairs → `site/data/bot-demos.json` (~20-25 prompts with voice-faithful answers)

## Phase 1: New Rooms

- [ ] `site/corpus/index.html` — Full blog browser. Vitrines per post. Filter by year, theme, location. Click to expand.
- [ ] `site/chronos/index.html` — Vertical timeline. Year as station. Click for detail.
- [ ] `site/lexicon/index.html` — Aphoristic glossary. Two-column on desktop.
- [ ] `site/voices/index.html` — Six speech-acts as posters. Massive type. Each one quotable.
- [ ] `site/method/index.html` — How the project works. Fact-check protocol, four claim types, latency commitment.
- [ ] `site/bot/index.html` — Chat UI. Demo prompts pre-loaded. Structural-guess pattern. Persistent across pages via widget.

## Phase 2: Lobby Reframe

- [ ] Rewrite `site/index.html` from "5-panel portal" to "museum lobby with 11 rooms." Add the museum metaphor copy. Update nav.
- [ ] Update global nav on every page to reflect 11 rooms (organized into clusters: Record / Mind / Apparatus / Subject / Bot)
- [ ] Update `site/day/001/index.html` nav to match

## Phase 3: The Bot

- [ ] Frontend-complete chat UI in `site/bot/index.html`
- [ ] Persistent "TALK TO NON" pulse widget bottom-right of every page (collapsible, single button → opens BOT room)
- [ ] Pre-loaded demo answers (~20) showing the voice
- [ ] Type-your-own input → naive keyword match against demos OR fallback to "Not yet known. The structural guess: ..."
- [ ] Backend stub: `/api/ask` endpoint description in METHOD room. Clearly labeled "BOT NOT YET WIRED" until Dr Non wires it.

## Phase 4: Polish

- [ ] Mobile QA every page (phone-first per §11.8)
- [ ] Visual coherence pass (every room feels like one museum)
- [ ] Update SUBJECT page tally numbers if corpus extraction changes them
- [ ] Add "you are in room X of 11" breadcrumb on each room
- [ ] Hover/focus state on every interactive element
- [ ] Color contrast check on every text block

## Phase 5: Deploy

- [ ] `git add site/ tasks/ && git commit && git push`
- [ ] Verify GitHub Actions deploy success
- [ ] Verify gh-pages branch has all new files
- [ ] Note for Dr Non in morning: 30-second Cloudflare unhook to free 100days.nonarkara.org from the 100-days-of-solitude Pages project

---

## Voice rules (do not violate)

- §12.4 forbidden phrases. No motivational fluff. No business-school clichés. No "unlock your potential."
- Aphoristic mode for definitions (Day 70 template).
- The structural-guess pattern: not "who killed" but "who in what position would want this victim killed."
- Long unbroken paragraphs are fine for voice surfaces.
- Open from the mundane. End on the open question. No conclusion.
- Address the reader as co-investigator.
- Dry self-deprecating humour permitted, announced openly.

## Visual rules (do not violate)

- Black bg, white fg, chartreuse accent (#CCFF00). One amber/accent only.
- Space Grotesk + JetBrains Mono. No Roboto/Inter/Poppins (§11.11).
- Zero rounded corners. Zero gradients. Zero shadows. Hairline borders.
- Three text sizes per page (§11.7).
- Phone-perfect (§11.8). 44px min touch targets.
- No AI images. No stock photos. Real assets only.

## The structural-guess pattern (the signature)

Direct from blog → cited answer in his voice.
Easy deduction → hedged answer.
Cannot know → does NOT pretend. Instead: "I don't know. But the structural guess: [the shape of the answer, in his voice]."

This is the anthropologist's move. Not the fact, but the shape.
