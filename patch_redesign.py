#!/usr/bin/env python3
"""patch_redesign.py — full visual redesign

  1. Full-width layout: remove max-width cap from .split
  2. Font swap:
       2026 (novel)  → Lora — warm, literary, contemporary paperback feel
       3026 (record) → IBM Plex Serif (stays) — IBM's institutional typeface,
                       the company that thought it could organise all human
                       knowledge into machine-readable systems. Perfect Kafka.
  3. Artwork: gallery scale — 420px tall, caption that teaches
"""

with open('/Users/nonarkara/Projects/100daysofnon/site/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

changes = 0

# ── 1. Add Lora to Google Fonts ──────────────────────────────────────────────
OLD_FONT = (
    'href="https://fonts.googleapis.com/css2?'
    'family=IBM+Plex+Serif:ital,wght@0,400;0,500;1,400'
    '&family=JetBrains+Mono:wght@400;500;700'
    '&family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,500;1,7..72,400'
    '&display=swap"'
)
NEW_FONT = (
    'href="https://fonts.googleapis.com/css2?'
    'family=IBM+Plex+Serif:ital,wght@0,400;0,500;1,400'
    '&family=JetBrains+Mono:wght@400;500;700'
    '&family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,500;1,7..72,400'
    '&family=Lora:ital,wght@0,400;0,500;0,600;1,400;1,500'
    '&display=swap"'
)
c = html.count(OLD_FONT)
print(f'Font link: {c}')
if c == 1:
    html = html.replace(OLD_FONT, NEW_FONT, 1)
    changes += 1

# ── 2. CSS: full redesign block ───────────────────────────────────────────────
CSS_REDESIGN = """
    /* ═══════════════════════════════════════════════════════════════════════
       REDESIGN — full-width · font swap · gallery artwork
       ═══════════════════════════════════════════════════════════════════════ */

    /* Full-width: remove the 74rem cap so columns fill the browser */
    .split{ max-width:none; }

    /* Breathe: wider column padding now that we have the full width */
    .col{ padding:2rem clamp(2rem,5vw,4.5rem) 5rem; }

    /* ── 2026 NOVEL: LORA ──────────────────────────────────────────────────
       Lora is the definitive literary-contemporary serif of this decade —
       warm, slightly melancholic, exactly what a Murakami/Camus hybrid
       should feel like in your hands.                                       */
    .col.novel .prose p{
      font-family:'Lora',Georgia,serif;
      font-size:1.25rem;
      line-height:1.88;
      max-width:64ch;
    }

    /* ── 3026 RECORD: IBM PLEX SERIF ───────────────────────────────────────
       IBM Plex Serif is literally IBM's institutional typeface — the company
       that believed it could reduce all human knowledge to machine-readable
       logic. Nothing says Utopianist Dystopia more precisely.               */
    .col.record .prose p{
      font-family:'IBM Plex Serif',Georgia,serif;
      font-size:1.125rem;
      line-height:1.82;
      max-width:62ch;
      letter-spacing:0.01em;
    }

    /* ── ARTWORK: GALLERY SCALE ────────────────────────────────────────────
       These are real paintings. Treat them like paintings.
       Full column width, 420px tall, caption that names the work clearly.  */
    .ch-art{
      margin:0 0 3rem;
      border:none;
      border-top:2px solid var(--rule);
    }
    .ch-art img{
      display:block;
      width:100%;
      height:420px;
      object-fit:cover;
    }
    .ch-art figcaption{
      padding:0.7rem 0 0;
      font-family:var(--mono);
      font-size:0.6875rem;
      letter-spacing:0.07em;
      color:var(--soft);
      border-top:none;
      line-height:1.6;
    }

    /* Entry artworks on dark background */
    .ch-art--entry{
      border-top-color:#2e3d50;
    }
    .ch-art--entry img{
      height:300px;
    }
    .col.record .ch-art figcaption{
      color:#7a8fa0;
      font-size:0.6875rem;
    }

"""

OLD_END = '  </style>'
NEW_END = CSS_REDESIGN + '  </style>'

c = html.count(OLD_END)
print(f'</style> anchor: {c}')
if c == 1:
    html = html.replace(OLD_END, NEW_END, 1)
    changes += 1

print(f'\nTotal changes: {changes}/2')
with open('/Users/nonarkara/Projects/100daysofnon/site/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print(f'Written. {len(html):,} chars')
