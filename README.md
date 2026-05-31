# 100 Days of Non

A biography of Non Arkaraprasertkul, recorded over one hundred days and kept as precise as memory and the record allow. One question a day; the answers assembled into a readable life — and, around it, a living "agent swamp" that computes the life into prose in public. In progress.

## The universe

The point is the **biography**. Everything else is the *making* of it, kept honest: every companion surface is computed verbatim from the record and the 99-post nonharvard blog. Nothing is invented.

| Surface | Path | What it is |
|---|---|---|
| **The Biography** | `/` | The record. Twelve chapters, first-person, book typography (Literata, warm paper, no accent). The single source of truth. |
| **The Workshop** | `/workshop/` | Split screen — the machine (live compute console + eight workers) beside the biography (embedded). Click a worker; it lights the passage it produced. Analytics ledger toggle. |
| **The Self-Portrait** | `/portrait/` | A portrait assembled from his own verbatim sentences — 38-line source-verified pool, 20 drawn fresh on every visit. |
| **The Atlas** | `/atlas/` | The life as a single Vignelli transit line — 13 stops, Bangkok→world→Bangkok, returns marked as interchanges. |
| **Open Questions** | `/questions/` | The 18 questions he asked across the essays and never closed, each with a dashed line where the answer is not. |
| **The Universe** | `/universe/` | The map of the whole — the biography as trunk, the four companions as stations. The navigable index. |

Every companion surface carries the same `.universe-nav`, so the whole work is traversable from anywhere.

## Structure

```
site/
  index.html              # the biography  (main.css)
  workshop/index.html     # the machine    (workshop.css — dark)
  portrait/index.html     # the self-portrait
  atlas/index.html        # the life as a transit line
  questions/index.html    # the open questions
  universe/index.html     # the map of the whole
  assets/css/
    main.css              # book typography (Literata; warm; no accent)
    surface.css           # SHARED warm-surface system for the companions
    workshop.css          # the dark machine
```

The four companion surfaces share **`surface.css`** (palette, type, masthead, movements, colophon, the universe-nav). Each page sets only its own `--measure` and a few page-specific rules. One design system; no drift.

## Design doctrine

Minimalistic, detailed, *it rhymes*. **Walter Gropius** (Bauhaus grid) · **New York subway map** (Vignelli — the diagram is the model) · **Monocle** (editorial ledgers, section markers, marginalia). One amber accent only; zero rounded corners, gradients, shadows. Machine layer = JetBrains Mono; book layer = Literata. Phone-first. Real data only.

## Source & data

- Biography drawn from `diary/day-XXX/` — Non's own answers, edited for reading, never invented.
- The agent surfaces compute from `archive/old-site/data/corpus.json` (99 posts, 239,110 words) and `tasks/timeline.md` (14 life-phases, gaps mapped to day numbers). Every portrait line, atlas date, and analytic count is source-verified against the corpus.

## Deploy

`site/` → GitHub Actions → `100.nonarkara.org`.

## Earlier attempts (archived, not deleted)

- `archive/old-site/` — the first biography build (and the blog corpus).
- `archive/frames-attempt/` — the "Frames" analytical-lens direction. Set aside; the biography is the foundation.

## License

Dr. Non. Public domain.
