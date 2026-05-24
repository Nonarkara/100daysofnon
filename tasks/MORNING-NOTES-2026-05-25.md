# Morning Notes — 2026-05-25

Built overnight while you slept. Six new museum rooms, 50-answer bot, 100 blog posts indexed, OG metadata everywhere. Three commits pushed. One thing needs your hand for 30 seconds.

---

## The 30-second thing first

The Cloudflare Pages project **`100-days-of-solitude`** has `100days.nonarkara.org` registered as a custom domain. It's intercepting every request to that URL and serving the old "100 Days of Solitude" prototype — not GitHub Pages. The new museum is fully built and pushed to gh-pages but cannot be seen at the canonical URL until you unhook this.

**Do this:**

1. Cloudflare dashboard → Workers & Pages → `100-days-of-solitude` → Custom domains
2. Remove `100days.nonarkara.org` (leave `solitude.nonarkara.org` and `100-days-of-solitude.pages.dev` — those keep the old site live where it should be)
3. Save

Then within ~30 seconds, https://100days.nonarkara.org/ should serve the new museum from GitHub Pages.

If you'd rather I do it: reply "yes, unhook" and I'll run the CLI command in one go.

**Alternative for impatient testing right now:** open https://nonarkara.github.io/100daysofnon/ — the new museum is live there immediately, just at the wrong URL. Most internal links use absolute paths (`/map/`) so navigation may feel slightly off until the custom domain works.

---

## What got built

### Three commits, in order

1. **`add 6 new museum rooms`** — corpus, chronos, lexicon, voices, method, bot. Plus all the data files (JSON corpus, voice anchor, lexicon, chronos, voices, bot demos).
2. **`reframe lobby as museum`** — index.html became the lobby with 11-room directory. Every existing page got the new 11-room nav and the Talk-to-Non widget.
3. **`polish`** — Open Graph metadata on all 12 pages, museum-style 404, bot demos doubled from 25 → 50, Random Read button in CORPUS.

### The eleven rooms

| # | Room | URL | What it is |
|---|------|-----|-----------|
| 01 | Record | `/day/001/` | Day 001 — the existing biographical entry. Now sits inside the museum frame. |
| 02 | Map | `/map/` | City of ideas. 8 districts, 32 landmarks. Existing. |
| 03 | **Corpus** | `/corpus/` | **NEW.** Full nonharvard blog. 100 posts, ~240k words. Two-pane browser with theme/location filters + Random Read button. |
| 04 | **Chronos** | `/chronos/` | **NEW.** Vertical timeline 1981 → 2026. One station per year. |
| 05 | **Lexicon** | `/lexicon/` | **NEW.** 35 Nonism terms with aphoristic definitions. Searchable. |
| 06 | Archive | `/archive/` | Ten uncomfortable facts. Existing. |
| 07 | **Voices** | `/voices/` | **NEW.** Six speech-acts as posters. Including the structural-guess signature. |
| 08 | **Method** | `/method/` | **NEW.** The trust page. Four claim types, bot promises, what this museum is not. |
| 09 | Game | `/game/` | Claim Check. Existing. |
| 10 | Subject | `/subject/` | Portrait + bio data. Existing. |
| 11 | **Bot** | `/bot/` | **NEW.** Frontend-complete chat UI. 50 demo answers. Honest fallback for misses. |

### The bot (the centerpiece)

**Current state:** Frontend-complete. 50 demo Q&A pairs covering blog topics, your biography, the Smart City work, philosophy, refusals, and the structural-guess pattern. Free-text input uses word-overlap matching against the demo set. When no good match exists, the bot honestly says "I don't have a direct answer in the record. The structural guess is the move I would make."

**The four answer kinds (shown as tags on every answer):**
- `DIRECT` (from the record) — cited Day N
- `DEDUCTION` (deduced from the record) — hedged
- `STRUCTURAL` (structural guess) — refuses literal Q, answers shape Q
- `NOT_KNOWN` (not in scope) — refuses entirely, suggests an alternative

**Persistent widget:** Bottom-right of every page (except BOT itself). Bright chartreuse "Talk to Non" button. One click opens the BOT room.

**When you want to wire it to Claude:**
- Voice anchor is at `/site/data/voice-anchor.json` — already structured as a system-prompt scaffold.
- Corpus is at `/site/data/corpus.json` (1.4MB, lazy-loaded) and `/site/data/corpus-index.json` (64KB metadata).
- Demo answers at `/site/data/bot-demos.json` — use as few-shot examples.
- Suggested backend: a `/api/ask` endpoint (Cloudflare Worker fits, given the rest of the stack). System prompt = voice-anchor + the 50 demo answers + ~10 relevant corpus excerpts retrieved by keyword.

### Data files (the RAG layer)

```
site/data/
├── corpus.json          1.4 MB    100 posts, full body, themes, locations
├── corpus-index.json     64 KB    Lightweight index (no body) for fast list
├── lexicon.json         9.5 KB    35 Nonism term definitions
├── chronos.json         4.9 KB    Timeline stations 1981–2026
├── voices.json          2.6 KB    Six speech-act posters
├── bot-demos.json        18 KB    50 demo Q&A pairs for the chat
└── voice-anchor.json    3.5 KB    System-prompt scaffold for the future bot
```

### Visual + Behavioural notes

- Black bg, white text, chartreuse `#CCFF00` accent. One amber, always, only. (§14 Rule 1.)
- Space Grotesk + JetBrains Mono. Zero rounded corners, zero gradients, zero shadows. Hairline borders.
- Three text sizes per page (§11.7).
- Mobile: 11-item nav scrolls horizontally; every interactive target ≥44px; phone-perfect (§11.8).
- Open Graph: WhatsApp/LINE link previews on all 12 pages now carry your portrait + room-specific copy.

---

## What's not done (for later)

- **Bot ↔ Claude wiring.** Frontend ready. Needs `/api/ask` endpoint with anthropic API key. See above.
- **Day 002+ records.** Day strip already shows future days as dim/unclickable, which is the right UX for now. When you write Day 002, just clone `site/day/001/` to `site/day/002/`, update content, set the day-strip active class. The 100-day strip will light up automatically as you ship each.
- **Cross-links between rooms.** Lexicon entries cite "Day N, blog" but don't link to `/corpus/#day-N`. Easy follow-up; rendering tweak in lexicon's render function. (~15 min.)
- **More lexicon entries.** 35 today. The plan was 50. Cut for time — quality-driven.
- **Cloudflare custom domain.** Blocked on you (§1 above).

---

## Verification checklist when you wake up

After the Cloudflare unhook:

1. https://100days.nonarkara.org/ → see the museum lobby with hero "100 DAYS"
2. /map/ → 8-district SVG, click landmarks
3. /corpus/ → 100 posts in left pane, click one → reads in right pane. Hit Random Read.
4. /lexicon/ → search "harvard" → finds the Harvard definition
5. /voices/ → scroll through six posters; the structural-guess one is the chartreuse panel
6. /chronos/ → vertical timeline, 1981 → 2026
7. /method/ → four claim types, bot promises, "this museum is not a portfolio"
8. /game/ → Claim Check still works
9. /subject/ → portrait + data, "BORN 1 NOV 1981" pull quote
10. /bot/ → click any demo question on the left → answer appears tagged DIRECT/DEDUCTION/STRUCTURAL. Type "who killed kennedy" → see the structural-guess fallback.
11. /404 → museum-style not-found page (just type a random URL like /xyz/)
12. iPhone check at 390px viewport — every room collapses cleanly

If anything looks broken, the gh-pages branch has the source; `git log gh-pages` shows what was deployed when.

---

The journal is a journey. Day 002 is yours to write.
