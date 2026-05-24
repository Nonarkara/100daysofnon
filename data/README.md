# `site/data/` — The RAG layer

This directory holds all structured knowledge that powers the museum and that will, when wired, power the bot.

## File map

| File | Size | Purpose |
|---|---|---|
| `corpus.json` | 1.4 MB | All 99 nonharvard blog posts. Per post: `n`, `id`, `date`, `weekday`, `title`, `words`, `excerpt`, `paragraphs[]`, `themes[]`, `locations[]`. |
| `corpus-index.json` | 63 KB | Same fields *minus* `paragraphs`. Loads first; the full corpus loads lazily when a post is opened. |
| `lexicon.json` | 12 KB | 52 Nonism term definitions, aphoristic, each with a `source`. |
| `chronos.json` | 5 KB | 15 timeline stations 1981–2026, with 21 events. |
| `voices.json` | 3 KB | Six speech-act posters. `tag`, `headline`, `footnote`, `source`. |
| `bot-demos.json` | 18 KB | 49 Q&A pairs across four `kind`s: `DIRECT`, `DEDUCTION`, `STRUCTURAL`, `NOT_KNOWN`. |
| `voice-anchor.json` | 4 KB | System-prompt scaffold for the future bot. Identity, voice rules, forbidden phrases, answer logic, the chain, the central tension. |

## When you wire the bot to Claude

The minimum viable wiring:

1. **System prompt** = `voice-anchor.json.identity` + `voice_rules` (joined) + `forbidden_phrases` (joined as "never say") + `answer_logic` (joined as four labeled blocks) + `the_chain` + `central_tension`.
2. **Few-shot examples** = the 49 pairs in `bot-demos.json`. Format each as `User: {q}\nNon ({kind}): {a}\nCitation: {cite}\n---`. Sample 8–12 per request, biased toward the question's matched theme.
3. **Retrieval (optional but recommended)** = keyword-match the user's question against `corpus-index.json` (title + excerpt + themes + locations), pull the top 2–3 posts, then for each pull 2 nearby paragraphs from `corpus.json`. Insert as `Context from the blog:` block before the user's message.
4. **Response constraint** = "Reply in one of the four kinds (DIRECT, DEDUCTION, STRUCTURAL, NOT_KNOWN). Tag the kind. Cite the post if relevant. Refuse to invent — the structural guess is the answer when you cannot answer literally."

## The structural-guess pattern (the bot's signature)

```
User: Who killed X?
Bot (STRUCTURAL):
  I don't know. The structural guess:
  the question is not who pulled the trigger; it is who could absorb
  the aftermath without their institution buckling. The intersection
  of motive, access, and post-event resilience is a small set. That
  is where I would look. I am not investigating it.
```

The bot must NEVER fabricate a literal answer. If the record is silent,
either give a structural guess (refusing the literal question, answering
the shape) or admit `NOT_KNOWN` and suggest a related question the record could answer.

## Numbering quirk

The corpus uses sequential `day-NNN` IDs in *date order*. The original
nonharvard blog had non-sequential `DAY N` labels (skipped numbers — `DAY 5`,
then `DAY 7`, then `DAY 12`...). Citations in `lexicon.json`, `voices.json`,
and `bot-demos.json` use the original `DAY N` labels for fidelity to the
source. If you want clickable cross-links between citations and corpus IDs,
build an `originalDay → corpusId` mapping from the PDF first.

## Updating the corpus

The corpus was extracted from `/Users/nonarkara/Projects/_personal/blog/nonharvard-100-days.pdf`
using `pdftotext -layout` plus a Python parser (`/tmp/parse_blog.py` and the
later refinement). If you re-run extraction, regenerate `corpus-index.json`
by stripping the `paragraphs` field from each post.

The blog ended at 99 effective posts in date-sequential order (one duplicate
caused by an inline date marker was filtered out). The PDF cover claims
"101 posts" — the discrepancy is the difference between *blog posts published*
and *posts as parsed*; if every original DAY N entry must be preserved as a
distinct record, a manual reconciliation pass is needed.
