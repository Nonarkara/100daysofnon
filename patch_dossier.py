# -*- coding: utf-8 -*-
"""patch_dossier.py
Case-file format for the 3026 record column:
  1. Dossier cover block at the top of the column
  2. SOURCE stamp under every entry's when-header
  3. CSS: .dossier, .stamp, and render-degradation for ch8-ch10
"""

PATH = '/Users/nonarkara/Projects/100daysofnon/site/index.html'

with open(PATH, encoding='utf-8') as f:
    html = f.read()
orig_len = len(html)

# ── 1. Stamp map: when-text (exact, entity-encoded) → stamp text ─────────────
STAMPS = {
 'The Hub &middot; Room 7 &middot; Thirty-one minutes after entry':
   'SOURCE: PARTICIPANT 44 &middot; SESSION NOTE &middot; MINUTE 31',
 'The World &middot; 3026':
   'SOURCE: INTERNAL &middot; HISTORICAL SUMMARY',
 'The Hub &middot; Room 7 &middot; The Cycle':
   'SOURCE: INTERNAL &middot; USAGE RECORD',
 'The World &middot; What You Keep':
   'SOURCE: RECOVERED IN-SESSION NOTE &middot; CHAIR 44',
 'The Hub &middot; He&#x2019;s Still In':
   'SOURCE: INTERNAL &middot; OBSERVATION LOG',
 'The City &middot; What Happened To Us':
   'SOURCE: INTERNAL &middot; HISTORICAL SUMMARY',
 'The City &middot; The Learning Set':
   'SOURCE: RECOVERED IN-SESSION NOTE &middot; CHAIR 44',
 'The Hub &middot; The Time Mechanics':
   'SOURCE: INTERNAL &middot; ORIENTATION MATERIAL',
 'The City &middot; What She Is Looking For':
   'SOURCE: INTERNAL &middot; PATTERN ANALYSIS',
 'The Hub &middot; The Austrian':
   'SOURCE: RECOVERED IN-SESSION NOTE &middot; CHAIR 44',
 'The City &middot; The Role Mechanic':
   'SOURCE: PARTICIPANT 44 &middot; DEBRIEF TRANSCRIPT',
 'The Hub &middot; Room 7 &middot; What She Came For':
   'SOURCE: PARTICIPANT 44 &middot; PERSONAL RECORD',
 'The Archive &middot; The Detection':
   'SOURCE: INTERNAL &middot; SESSION TERMINATION REPORT',
 'The Hub &middot; Memory Catalog':
   'SOURCE: PARTICIPANT 44 &middot; PERSONAL RECORD',
 'The Archive &middot; Session Zero &middot; The Eye Problem':
   'SOURCE: INTERNAL &middot; INCIDENT ARCHIVE',
 'The Hub &middot; Room 7 &middot; Why She Goes Back':
   'SOURCE: PARTICIPANT 44 &middot; PERSONAL RECORD',
 'The Hub &middot; Room 7 &middot; Later':
   'SOURCE: RECOVERED IN-SESSION NOTE &middot; CHAIR 44',
 'The City That Replaced Bangkok &middot; Before':
   'SOURCE: PARTICIPANT 44 &middot; PERSONAL RECORD',
 'The Hub &middot; Room 7 &middot; What She Left':
   'SOURCE: RECOVERED IN-SESSION NOTE &middot; CHAIR 44',
 'The Hub &middot; Room 7 &middot; The Panel':
   'SOURCE: INTERNAL &middot; OBSERVATION LOG',
 'The Hub &middot; Room 7 &middot; Sub-Indicator 7':
   'SOURCE: RECOVERED IN-SESSION NOTE &middot; CHAIR 44',
 'The Hub &middot; Room 7 &middot; The Protocol':
   'SOURCE: PARTICIPANT 44 &middot; PERSONAL RECORD',
 'The Hub &middot; Room 7 &middot; Sub-Indicator 9':
   'SOURCE: RECOVERED IN-SESSION NOTE &middot; CHAIR 44',
 'The Hub &middot; The Last Time She Saw Bangkok':
   'SOURCE: PARTICIPANT 44 &middot; PERSONAL RECORD',
 'The Hub &middot; Chair 44 &middot; Hour Three':
   'SOURCE: RECOVERED IN-SESSION NOTE &middot; CHAIR 44',
 'The Record &middot; Why 1981':
   'SOURCE: PARTICIPANT 44 &middot; PERSONAL RECORD',
 'The Machine &middot; Why The Basement':
   'SOURCE: INTERNAL &middot; TECHNICAL BRIEF',
 'The World &middot; The Other Option':
   'SOURCE: INTERNAL &middot; POPULATION STUDY',
 'The Hub &middot; Thirty-One Minutes':
   'SOURCE: INTERNAL &middot; OBSERVATION LOG',
 'The Question &middot; Session Briefing':
   'SOURCE: INTERNAL &middot; ORIENTATION MATERIAL &middot; WITHHELD',
 'System Log &middot; Substance Anomaly &middot; Class 4':
   'SOURCE: INTERNAL &middot; AUTOMATED',
 'Internal Audit &middot; Session 44 &middot; The Channel':
   'SOURCE: INTERNAL &middot; AUDIT DIVISION',
 'Incident Report &middot; Flag Protocol &middot; Class 4':
   'SOURCE: INTERNAL &middot; AUTOMATED',
 'Research Note &middot; The Bootstrapping Problem':
   'SOURCE: INTERNAL &middot; RESEARCH DIVISION',
 'Personal Record &middot; Neural Pathway &middot; Standard Session':
   'SOURCE: PARTICIPANT 44 &middot; PERSONAL RECORD',
}

count = 0
for when, stamp in STAMPS.items():
    tag = f'<p class="when">{when}</p>'
    pos = html.find(tag)
    if pos == -1:
        print(f'  ✗ when not found: {when[:50]}')
        continue
    insert_at = pos + len(tag)
    html = html[:insert_at] + f'\n        <p class="stamp">{stamp}</p>' + html[insert_at:]
    count += 1
print(f'Stamps: {count}/{len(STAMPS)}')

# ── 2. Dossier cover block ───────────────────────────────────────────────────
intro_anchor = 'That is correct.</p>'
pos = html.find(intro_anchor)
dossier = '''

      <div class="dossier">
        <p class="d-line">CASE FILE 44&#x2013;44</p>
        <p class="d-line">SUBJECT: PARTICIPANT 44 &middot; CHAIR 44</p>
        <p class="d-line">CLASSIFICATION: CLASS 4 &middot; FREQUENCY ANOMALY</p>
        <p class="d-line">COMPILED: YEAR 3026 &middot; BY THE SYSTEM</p>
        <p class="d-line">STATUS: OPEN</p>
      </div>'''
if pos != -1:
    insert_at = pos + len(intro_anchor)
    html = html[:insert_at] + dossier + html[insert_at:]
    print('Dossier cover: inserted')
else:
    print('Dossier cover: ANCHOR NOT FOUND')

# ── 3. CSS ───────────────────────────────────────────────────────────────────
css = '''
/* ── Case-file dossier format ── */
.dossier{margin:0 0 3rem;padding:1.1rem 1.3rem;border:1px solid #2e3d50;}
.dossier .d-line{margin:0.25rem 0;font-family:var(--mono);font-size:0.625rem;letter-spacing:0.1em;color:#7a8a9a;text-transform:uppercase;}
.dossier .d-line:first-child{color:var(--amber);}
.stamp{margin:0.3rem 0 0;font-family:var(--mono);font-size:0.575rem;letter-spacing:0.11em;color:#4a5a6a;text-transform:uppercase;}
/* ── Render degradation: the simulation losing resolution, ch8 → ch10 ── */
#ch8 .prose p{letter-spacing:0.012em;}
#ch9 .prose p{letter-spacing:0.026em;word-spacing:0.05em;}
#ch10 .prose p{letter-spacing:0.045em;word-spacing:0.08em;text-shadow:0.5px 0 rgba(255,0,60,0.16),-0.5px 0 rgba(0,180,255,0.16);}
'''
style_close = html.rfind('</style>')
html = html[:style_close] + css + html[style_close:]
print('CSS: injected')

print(f'\n{orig_len:,} → {len(html):,}')
with open(PATH, 'w', encoding='utf-8') as f:
    f.write(html)
print('Written.')
