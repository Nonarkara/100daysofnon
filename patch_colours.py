#!/usr/bin/env python3
"""patch_colours.py — two-column visual identity split

  LEFT  (3026 record)  : dark institutional #0d1117 + IBM Plex Serif prose
  RIGHT (2026 novel)   : per-chapter mood backgrounds; Ch10 converges to dark
"""

with open('/Users/nonarkara/Projects/100daysofnon/site/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

changes = 0

# ── 1. Google Fonts — add IBM Plex Serif ─────────────────────────────────────
OLD_FONT = (
    'href="https://fonts.googleapis.com/css2?'
    'family=JetBrains+Mono:wght@400;500;700'
    '&family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,500;1,7..72,400'
    '&display=swap"'
)
NEW_FONT = (
    'href="https://fonts.googleapis.com/css2?'
    'family=IBM+Plex+Serif:ital,wght@0,400;0,500;1,400'
    '&family=JetBrains+Mono:wght@400;500;700'
    '&family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,500;1,7..72,400'
    '&display=swap"'
)
c = html.count(OLD_FONT)
print(f'Font link: {c}')
if c == 1:
    html = html.replace(OLD_FONT, NEW_FONT, 1)
    changes += 1

# ── 2. CSS additions — insert before </style> ────────────────────────────────
CSS_BLOCK = """
    /* ── 3026: DARK INSTITUTIONAL RECORD ─────────────────────────────────── */
    .col.record{
      background:#0d1117;
      --ink:#c9d1d9; --soft:#8b949e; --faint:#606b78;
      --rule:#21262d; --paper:#0d1117; --amber:#f0a030;
    }
    /* IBM Plex Serif: cooler, more systematic than Literata */
    .col.record .prose p{
      font-family:'IBM Plex Serif',Georgia,serif;
      font-size:1rem;
      line-height:1.75;
      letter-spacing:0.012em;
    }
    /* inherit dark vars for record UI elements */
    .col.record .col-head{color:var(--ink);}
    .col.record .col-intro{color:var(--soft);}
    .col.record .ch-art figcaption{color:var(--faint);border-top-color:var(--rule);}
    .col.record .ch-art{border-color:var(--rule);}

    /* ── CHAPTER PAGE MOODS (2026 NOVEL) ─────────────────────────────────── */
    #ch1 {background:#faf7f2;}  /* warm parchment — domestic stillness */
    #ch2 {background:#eff4fb;}  /* muted blue — cool memory, Vermeer */
    #ch3 {background:#f3f0f9;}  /* lavender — dream state, skull */
    #ch4 {background:#fdf5e6;}  /* amber-warm — altered consciousness */
    #ch5 {background:#f1f7f2;}  /* sage — domestic unease, flowers */
    #ch6 {background:#f2f3f6;}  /* cool grey — the attaché, clinical */
    #ch7 {background:#ecf0f6;}  /* blue-grey — Friedrich, two men, moon */
    #ch8 {background:#faf0ee;}  /* terracotta — KL heat, Mira loop */
    #ch9 {background:#f4f0f3;}  /* muted rose — dissolution, Courbet */
    /* Ch10: converges with the record column — he has decided to stay inside */
    #ch10{
      background:#0d1117;
      --ink:#c9d1d9; --soft:#8b949e; --faint:#606b78;
      --rule:#21262d;
    }

"""

OLD_STYLE_END = '  </style>'
NEW_STYLE_END = CSS_BLOCK + '  </style>'

c = html.count(OLD_STYLE_END)
print(f'Style end: {c}')
if c == 1:
    html = html.replace(OLD_STYLE_END, NEW_STYLE_END, 1)
    changes += 1

# ── write ─────────────────────────────────────────────────────────────────────
print(f'\nTotal changes: {changes}/2')
with open('/Users/nonarkara/Projects/100daysofnon/site/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print(f'Written. {len(html):,} chars')
