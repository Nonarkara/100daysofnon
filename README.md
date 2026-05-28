# Frames

A field manual for thinking — lenses for situations that resist a simple answer.

Each frame is a way of seeing structure where other people see noise. The frames are drawn from architecture, anthropology, Daoist strategy, history, and twenty years of building things that had to stand up. Not theories. Tools.

The site is built the way an architect draws: a warm-paper drawing sheet, ink, and one mark of colour — 朱 cinnabar, the colour of the correction pencil and the family name-seal — used once, where it means something. Every sheet carries a titleblock; the worked examples are read from the record, not invented.

## Status — v0.3.0

- **The Survey** · live · the frames turned on the subject. Five recurring structures assembled from things said across different days and never connected. The payoff surface — it tells the subject something he did not already know.
- **Sheet 01 — The Spatial Frame** · live · adjacency, boundary, flow, centre.
- **Sheet 02 — The Cultural Frame** · live · stated code, desire paths, reward & exile, the disavowed.
- Sheets 03–04 (Strategic / Temporal) — planned, not yet drawn.
- **Form:** written + an architectural diagram + a local-only worksheet (nothing leaves your device).
- **Energy:** rigorous and warm. Precise is not the same as cold.

The Survey re-runs as the record grows; a pattern that looks solid now may break against a later day, and that break is the most interesting cell on the page. Every fragment it cites is real, drawn from `diary/day-XXX/`.

## Structure

```
site/
  index.html              # the drawing set — titleblock + register
  404.html                 # re-filed sheet — routes orphaned links back to the set
  assets/css/main.css      # the design system (IBM Plex; one cinnabar accent; no rounded corners)
  frames/
    spatial.html           # Sheet 01 — adjacency, boundary, flow, centre
    cultural.html          # Sheet 02 — stated code, desire paths, reward & exile, the disavowed
```

## Design rules

- One accent only (cinnabar 朱). Ink on warm paper otherwise.
- IBM Plex Serif (body) / Sans (structure) / Mono (drawing labels). No Inter, no template fonts.
- Zero rounded corners, zero gradients, zero shadows. Hairline rules only.
- Three text sizes. Phone-first.

## Previous work

The 100-day biographical installation is archived in `archive/old-site/` and `archive/old-scripts/`. Its memories now appear inside the frames as worked examples — the life is the proof, not the subject.

## Deploy

`site/` → GitHub Actions → `100.nonarkara.org`.

## License

Dr. Non. Public domain.
