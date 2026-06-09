#!/usr/bin/env python3
"""patch_text_fix.py — three fixes:
   1. 3026 text colour: CSS custom props don't re-inherit computed values —
      must declare color:var(--ink) on the container so children inherit
      the locally-scoped light value, not body's dark brown.
   2. Prose too small — bump both columns up.
   3. Record artwork frame: make border visible on dark bg.
"""

with open('/Users/nonarkara/Projects/100daysofnon/site/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

changes = 0

# ── inject CSS before </style> ────────────────────────────────────────────────
CSS_FIX = """
    /* ── FIX: dark-column color inheritance ──────────────────────────────────
       CSS custom props don't auto-inherit computed values. Declaring
       color:var(--ink) on the container forces re-resolution with the
       locally-scoped --ink (#c9d1d9), which then cascades to every child.  */
    .col.record{ color:var(--ink); }
    #ch10{ color:var(--ink); }

    /* ── LARGER PROSE ─────────────────────────────────────────────────────── */
    .prose p{
      font-size:1.3125rem;
      line-height:1.84;
    }
    .col.record .prose p{
      font-size:1.125rem;
      line-height:1.80;
    }

    /* ── 3026 ARTWORK: visible frame + tighter entry spacing ──────────────── */
    .col.record .ch-art{
      border-color:#2e3d50;
      margin-bottom:2rem;
    }
    .col.record .ch-art figcaption{
      color:#5a6e80;
      border-top-color:#2e3d50;
    }

"""

OLD_END = '  </style>'
NEW_END = CSS_FIX + '  </style>'

c = html.count(OLD_END)
print(f'</style> anchor: {c}')
if c == 1:
    html = html.replace(OLD_END, NEW_END, 1)
    changes += 1

print(f'\nTotal changes: {changes}/1')
with open('/Users/nonarkara/Projects/100daysofnon/site/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print(f'Written. {len(html):,} chars')
