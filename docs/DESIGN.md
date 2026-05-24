# Design

**Super punk with deep chaotic minimalism.** Jamie Reid + Wolfgang Weingart + Designers Republic + David Carson Ray Gun era + Vaughan Oliver 4AD. Aggression from structural rigor. Chaos placed precisely. The site looks like the truth it's reporting.

---

## The thesis

The site looks like the truth it's reporting. Aggressive because brutal honesty is aggressive. Minimal because every element is load-bearing. Chaotic because memory is.

---

## Color

| Token | Hex | Use |
|---|---|---|
| `--bg` | `#000000` | Background. Pure black. |
| `--fg` | `#FFFFFF` | Type. Pure white. |
| `--accent` | `#CCFF00` | Chartreuse. ONE accent. Contradiction cells, latency stats, glitch markers, hover states. |

Nothing else. No tints. No greys except as `rgba(255,255,255, x)` when type needs to recede. No gradients ever.

---

## Type

| Token | Family | Use |
|---|---|---|
| `--sans` | Akzidenz-Grotesk (or Inter as fallback) | Body, headlines, navigation |
| `--mono` | JetBrains Mono | Telemetry, dates, claim tags, numerals where they should read as data |

No other typefaces. Contrast comes from scale, not from font collection.

Allowed scales (don't use anything in between):

- 11px — micro caption / metadata
- 14px — body
- 18px — emphasis body
- 32px — section
- 64px — pull
- 144px — pull-as-image / day-counter
- 240px+ — full-bleed pull

---

## Layout

Broken grid by design.

- Day-number column is 1px wide, runs floor-to-ceiling, lives at column 0. Pure architecture.
- Answer column overflows the right edge by design where the body demands it. Don't reflow. Cut.
- Stacking elements need not align. Adjacency without alignment is the language.
- Negative space is compositional weight, not decoration. Use it like Weingart used it — to load tension.

---

## Type-as-image

Pull a fragment from the day's answer, render it at 144px+ in a single line, intentionally crop mid-word at the viewport edge. The text fragment IS the image. Reid's ransom-note logic. No background image, no soft fade. Hard crop.

One per day. Not three. The day has a single visual anchor.

---

## Artifacts

Photos and documents Non sends get processed:

- Convert to harsh duotone (`#000000` + `#CCFF00`)
- No soft edges, no shadows, no rounded crops
- Posterize OR 1-bit dither — pick per artifact, don't mix on the same page
- No "polish." No film grain, no vignette, no border. Raw.

---

## Fact-check column

```
✓  VERIFIED       [source]
✗  CONTRADICTED   [recorded: …]   [source]
?  UNVERIFIED
∅  UN-VERIFIABLE
```

Monospace. Glyph + tag + source. Contradicted rows: `--accent` chartreuse on the glyph. Nothing else colored.

---

## Telemetry block

The response-latency stat is rendered as a single architectural number per day:

```
00:14:32
2026-05-24 21:14 Asia/Bangkok
```

144px on the latency. 11px mono date underneath. No icon, no label, no "Response time:". The number is the title.

---

## Motion

No transitions. No fades. No slide-ins.

If anything moves: data scrubbing. The latency stat counts up live during composition. The fact-check tags flip from `?` to `✓` / `✗` when verification lands. Pattern dashboard numbers jump as new data arrives. No easing curves. No "delightful" animations. Glitch register only.

---

## Mobile

Same brutalism, rescaled. No softening on small screens. The 1px day-column stays 1px. The 144px pull becomes 96px but stays huge. Don't add padding to "make it feel less intense" on mobile. The intensity is the point.

---

## Hard bans

This is the punk floor. The CLAUDE.md anti-pattern list is the design ceiling; punk goes harder.

- **No rounded corners.** Zero. `border-radius: 0` everywhere.
- **No gradients.** Anywhere. Background, text, button, icon. None.
- **No box-shadow.** Including the "subtle" kind. Elevation is communicated by position and stacking, not by shadow.
- **No decorative SVG** — no waves, blobs, wavy lines, abstract shapes used for atmosphere.
- **No Poppins, Nunito, Raleway, Quicksand, Lato, Playfair Display.** Period.
- **No pill buttons.** Buttons are rectangles. They contain a label. They invert on hover (white→black or chartreuse→black).
- **No card-grid feature layouts.** No "three columns with icon and tagline."
- **No emoji as UI.** Status glyphs (`✓ ✗ ? ∅`) are the only allowed semi-iconographic marks and they're monospace characters, not emoji.
- **No hero sections with imagery washes.** Pages open with text.
- **No icon bloat.** Icons appear only when they encode information unavailable in text.
- **No glass-morphism, no neumorphism, no skeuomorphism.** Flat. Always flat.
- **No "template" feature presentation.** If a layout could appear on a Webflow / Bootstrap / Figma Community template, it's banned.

---

## The test

Before shipping any visual element, ask:

> Does this look like it came from a Figma Community template or a Bootstrap theme?

If yes — redesign from scratch using Reid / Weingart / Designers Republic logic.

> Does this look like a "designer made it cool"?

If yes — too decorated. The aesthetic is structural, not surface. Strip until only the load-bearing parts remain.

> Does this feel hostile?

If yes — you're on the right track. The site is honest. Honest looks hostile when most other sites are flattering.
