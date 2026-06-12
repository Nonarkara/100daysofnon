# -*- coding: utf-8 -*-
"""patch_new_content.py
New creative content (EN only — plain <p>, translated in a later pass):
  1. The full act inserted into "What She Came For" (between the look and
     "Later she would lie still")
  2. Addendum entry: the 2,604 erased sessions (after Memory Catalog)
  3. Personal Record entry moved before "The Hub · Thirty-One Minutes"
  4. Final entry: the reunion, logged by the system
  5. Chapter 6-10 expansion beats
"""
import re

PATH = '/Users/nonarkara/Projects/100daysofnon/site/index.html'

def enc(t):
    t = t.replace('&', '&amp;')
    t = t.replace('—', '&#x2014;')
    t = t.replace("'", '&#x2019;')
    t = t.replace('“', '&#x201C;').replace('”', '&#x201D;')
    t = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', t)
    return t

def find_matching_close(s, open_pos):
    depth = 0
    for m in re.finditer(r'<div\b|</div>', s[open_pos:]):
        if m.group(0).startswith('<div'):
            depth += 1
        else:
            depth -= 1
            if depth == 0:
                return open_pos + m.end()
    return -1

with open(PATH, encoding='utf-8') as f:
    html = f.read()
orig_len = len(html)

# ── 1. The act — "What She Came For" ─────────────────────────────────────────
SCENE = [
 "One session. Years ago by chair time, lifetimes ago by the other count. A configuration she has never re-entered and never logged, in a city she does not name even to herself, in a life where the machine had given them what it never gave them in Bangkok: a mechanism.",
 "He crossed the room the way weather crosses a field. She watched him come and did nothing to help it and nothing to stop it, because the not-helping was the last sovereign territory she had — and he seemed to understand that, and stopped at the edge of it, and waited until she said yes. Out loud. The asking was the technology. No machine has ever asked.",
 "His hands were slower than the button. That was the first discovery. Slowness — the one luxury a system optimised for delivery cannot stock. He undressed her the way you read a document you have waited years to be cleared for: in order, missing nothing. Lips at the back of her neck. A thumb along the line of her hip, checking it like a level. She heard herself make a sound she had never made in 3026. Nobody in 3026 makes sounds. There is nothing to make them about.",
 "The weight was the part the button never solved. Pressure, the chip can do. Weight, no. Weight is the consequence of a body that can fall, can crush, can die — held back by nothing except its own intention. He was heavy on her and the heaviness said: I am here, I am real, I could be otherwise and I am not. Her hips rose against the weight to test it. It held. She tested it again. It held. She stopped testing.",
 "Sweat. The machine renders smell at low priority — a documented economy. There was nothing low-priority about this. Salt and skin and the animal fact of him, and under it her own body answering in a language the chip had spoken *for* her since birth and never once let her speak herself.",
 "There was a moment — his teeth at her shoulder, her nails finding his back, both of them clumsy, an elbow wrong, a laugh, an apology breathed into her hair — when she understood what the historians had missed. The act was never the point. The clumsiness was the point. The machine has never once apologised to her. Perfection has no inside.",
 "The want built the way pressure builds in a sealed space. No vent. No button. No exit except through. She came the way you fall when you have decided to stop holding the rail — not delivered, *arrived* — and it was not ten times anything. It was one times one. A single unrepeatable instance of a single thing happening to a single body that could die. That was the entire content of it. That was everything.",
 "After, his arm was under her and it had gone dead — she could tell from his breathing that it had gone dead — and he did not move it. Discomfort, chosen, held, for someone. She lay on the dead arm of a man in a rendered city and understood the whole millennium: they had not removed the suffering from love. They had removed the love from suffering, and called what was left wellness.",
 "Four minutes, twelve seconds. That is the standard session, the one the file logs as equivalent. She checked once, out of spite. The destination is identical. Everything between the bodies is missing, and everything between the bodies was the entire cargo.",
]

anchor = html.find('<p lang="en">Later she would lie still')
line_start = html.rfind('\n', 0, anchor) + 1
block = ''.join(f'          <p>{enc(p)}</p>\n' for p in SCENE)
html = html[:line_start] + block + html[line_start:]
print('1. Scene inserted: 9 paragraphs')

# ── helpers for entry-level ops ───────────────────────────────────────────────
def entry_span(html, when):
    """Full span of an entry div (line start to after closing div + newline)."""
    wp = html.find(f'<p class="when">{when}</p>')
    if wp == -1:
        return None
    open_pos = html.rfind('<div class="entry">', 0, wp)
    close_pos = find_matching_close(html, open_pos)
    start = html.rfind('\n', 0, open_pos) + 1
    end = close_pos
    while end < len(html) and html[end] == '\n':
        end += 1
    return (start, end)

def build_entry(when, stamp, paras):
    lines = ['      <div class="entry">',
             f'        <p class="when">{when}</p>',
             f'        <p class="stamp">{stamp}</p>',
             '        <div class="prose">']
    for p in paras:
        lines.append(f'          <p>{enc(p)}</p>')
    lines += ['        </div>', '      </div>', '']
    return '\n'.join(lines)

# ── 2. Addendum entry after Memory Catalog ───────────────────────────────────
ADDENDUM = [
 "Participant 44 reports two hundred and forty-three sessions. She is correct.",
 "The file records two thousand eight hundred and forty-seven.",
 "Both numbers are accurate. Two hundred and forty-three is the number of sessions she was permitted to keep.",
 "The remaining two thousand six hundred and four are stored under seal. The seal predates this audit. The seal does not carry the system's signature.",
 "The system did not erase them. The system does not know who did. This is the only sentence in this file the system cannot complete.",
]
span = entry_span(html, 'The Hub &middot; Memory Catalog')
new_entry = build_entry('Addendum &middot; Count Reconciliation &middot; Restricted',
                        'SOURCE: INTERNAL &middot; RESTRICTED &middot; SEAL PRESENT',
                        ADDENDUM)
html = html[:span[1]] + new_entry + '\n' + html[span[1]:]
print('2. Addendum entry inserted')

# ── 3. Move Personal Record before "The Hub · Thirty-One Minutes" ───────────
pr_span = entry_span(html, 'Personal Record &middot; Neural Pathway &middot; Standard Session')
pr_block = html[pr_span[0]:pr_span[1]].rstrip('\n') + '\n\n'
html = html[:pr_span[0]] + html[pr_span[1]:]
tm_span = entry_span(html, 'The Hub &middot; Thirty-One Minutes')
html = html[:tm_span[0]] + pr_block + html[tm_span[0]:]
print('3. Personal Record moved before Thirty-One Minutes')

# ── 4. Reunion — final entry of the case file ────────────────────────────────
REUNION = [
 "Session 45 terminated at hour thirty-one, minute thirty-one, chair time. Exit: chosen. The door was rendered on the left, as requested. The request was not made in words.",
 "The participant in Chair 44 opened his eyes at 06:12 standard. Room 7 holds 6000 Kelvin, the same light as the city. He did not look at the light.",
 "Chair 43 was occupied.",
 "Participant 44 had been seated for nine hours. In that time she declined two meal prompts and one recovery advisory. The system logged her as non-compliant. The system did not act on it.",
 "He looked at her for eleven seconds before either of them moved. The system has no classification for the expression. The closest match in the training data is: recognition. Confidence: low. The training data is a thousand years old.",
 "She said something the room microphones captured below transcription threshold. Three syllables.",
 "He moved his hand from the armrest of Chair 44 to the armrest of Chair 43. Twelve centimetres. It took four seconds. The system can deliver the equivalent neural sensation in under three. Neither participant has ever filed a complaint about the difference. Both have stopped using the service.",
 "Neither participant has booked another session.",
 "The file does not close. Classification: pending. Appended by the system, unprompted, against protocol: three hundred and twelve years of this programme, every possible configuration of every possible brain, in search of the variable that broke the species. The variable was never inside the simulation. It was in the room. It was twelve centimetres of distance, defended for four years, crossed in four seconds, by choice.",
 "The system can usually say what a thing is for.",
 "Usually.",
]
rn_span = entry_span(html, 'Research Note &middot; The Bootstrapping Problem')
reunion_entry = build_entry('Room 7 &middot; Hour Thirty-One &middot; Minute Thirty-One',
                            'SOURCE: INTERNAL &middot; SESSION TERMINATION REPORT &middot; FINAL ENTRY',
                            REUNION)
html = html[:rn_span[1]] + reunion_entry + '\n' + html[rn_span[1]:]
print('4. Reunion entry inserted as final record')

# ── 5. Chapter expansion beats ───────────────────────────────────────────────
def insert_after_triplet(html, locator, paras):
    """Find EN paragraph containing locator, skip its th+zh siblings,
    insert flush-left plain <p> paragraphs after."""
    variants = [locator, locator.replace("'", '&#x2019;')]
    pos = -1
    for v in variants:
        pos = html.find(v)
        if pos != -1:
            break
    if pos == -1:
        print(f'   ✗ MISS: {locator[:50]}')
        return html
    p = html.find('</p>', pos) + 4
    th = html.find('<p lang="th">', p)
    p = html.find('</p>', th) + 4
    zh = html.find('<p lang="zh">', p)
    p = html.find('</p>', zh) + 4
    p = html.find('\n', p) + 1
    block = ''.join(f'<p>{enc(t)}</p>\n' for t in paras)
    print(f'   ✓ {locator[:50]}')
    return html[:p] + block + html[p:]

CH = [
 # ch6
 ("A dropped asset", [
   "I stood in the doorway of the train holding the strap, and the thing I felt was not fear. It was professional. Somebody had reviewed this city — the grid, the flicker, the recovery time — and signed off on it. I know the signature of a reviewed object. I produce them for a living.",
 ]),
 ("They are maintenance", [
   "I started watching for them after that. The man recalibrating a ticket gate that was not broken. The woman at Siam who stood for forty minutes without shifting her weight — no human stands without shifting their weight. Once you know the uniform, the city is full of staff.",
   "The notebook was filling. I had stopped showing it to anyone. There is a specific point where evidence becomes symptom, and I knew exactly which side of that line my friends would file me under.",
 ]),
 # ch7
 ("repeat the cycle three times", [
   "I stood with the dog in the dead light and felt something close to tenderness. Somewhere, a renderer had decided that a soi dog at 3 AM was worth four steps, a pause, a sniff. A budget had been allocated. I was being given more — more resolution, more physics, more consequence. That was the comfort. That was also the bill.",
 ]),
 ("the idea of a brick", [
   "I kept my hand on it longer than the test required. My grandmother's house had a wall like this once — I had pressed my palm against the real version of this exact texture, in 1989, beside a rain jar. The wall under my hand now was quoting it. The world was quoting itself to me and getting the citation slightly wrong.",
 ]),
 ("until the textures became sharp again", [
   "At the mouth of the soi the phone buzzed once more. The same number. One word.",
   "'Good.'",
 ]),
 # ch8
 ("Intonation for intonation", [
   "Mitt laughed at the same beat in the same story, both times. My friend of eleven years. I sat with my drink and did the arithmetic I had been refusing to do: how many of my people are people. The bar went on glittering. Nobody else had seen it. Or everybody else was part of it. The two possibilities cost exactly the same.",
 ]),
 ("reallocating resources to monitor me", [
   "That night the hotel was perfect. The card key worked on the first try. The pillow was right. The hot water was immediate, the towels warm, and the bed was turned down with one corner folded back, as if a quiet hand had thought about my comfort specifically. I lay in the perfection and felt it close over me like water.",
   "Somewhere, something had opened a file on me and selected: increase ambient satisfaction. I slept eleven hours. I dreamed of nothing. It was the most frightening night of my life.",
 ]),
 # ch9
 ("nervous system in the Hub is lethal", [
   "That's not true, I said. I didn't insert Pui. She was real. She had a desk. She had a laugh that made contact with my arm. The smoke moved through the fan. The voice said nothing for a long time.",
   "Ask the right question, it said.",
   "Who played my mother?",
   "The cherry flared. Wrong question. Ask who rode the bicycle.",
   "Something moved in me. A province north of Bangkok. A gate. A woman selling vegetables from a bicycle, twice a week, who looked at me once when I was five years old and whom I have never, in forty-four years, stopped expecting at the end of every street.",
 ]),
 # ch10
 ("She was breathing. Not dead. Alive.", [
   "The information did not arrive as words. It arrived the way the studio had arrived in the twelve minutes — whole, physical, with weather. A room the colour of early morning. Two chairs. The hum of a machine that loves us and cannot say so. And in the chair beside mine, twelve centimetres away, a woman who had crossed four thousand years of other people's lives to be sitting there when the light hit my eyes.",
   "Every birthday message I wrote to a dead woman's wall, she had already read from the other side of the glass.",
 ]),
]

print('5. Chapter beats:')
for locator, paras in CH:
    html = insert_after_triplet(html, locator, paras)

print(f'\n{orig_len:,} → {len(html):,} (+{len(html)-orig_len:,})')
with open(PATH, 'w', encoding='utf-8') as f:
    f.write(html)
print('Written.')
