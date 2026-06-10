#!/usr/bin/env python3
# Add Ch4 "Signal Loss" + enrich Ch2 + update 3026 world + nav/labels
# NEVER use Edit tool on index.html — it corrupts ASCII quotes to curly quotes

PATH = '/Users/nonarkara/Projects/100daysofnon/site/index.html'

with open(PATH, 'rb') as f:
    s = f.read().decode('utf-8')

changes = 0

# ─────────────────────────────────────────────────────────────────────────────
# 1. Ch2 — insert proximity / pheromone / correct-procedure paragraphs
#    8-space indent for prose <p> tags inside .novel column
# ─────────────────────────────────────────────────────────────────────────────
CH2_ANCHOR = (
    '<p>By the fifth she was beautiful in the way particular to women who were not beautiful early. '
    'Earned. Without vanity. Like something grown into rather than applied.</p>\n\n'
    '        <p>I closed my eyes on the floor beside the desk.</p>'
)

CH2_NEW = (
    '<p>By the fifth she was beautiful in the way particular to women who were not beautiful early. '
    'Earned. Without vanity. Like something grown into rather than applied.</p>\n\n'
    '        <p>Her desk was right next to mine. By the third year I had stopped pretending this was neutral. '
    'She wore a t-shirt and shorts to the studio like most of us did &#x2014; nobody was dressing for the hours. '
    'At 2am under the drafting light, working, a body stops being anything except what it is. '
    'The light at that angle made the room honest. I was aware of her. '
    'Not as a plan, not as a decision. '
    'The body makes its own notes before the mind approves the transcript.</p>\n\n'
    '        <p>No perfume. Just pheromone. Just proximity. Just that particular sensibility that certain '
    'women have without knowing they have it &#x2014; the quality that registers in the room before they do.</p>\n\n'
    '        <p>She was always with someone &#x2014; usually a senior, the kind of man who fills a room '
    'with his mood before he enters it. I had a girlfriend. We walked to the station sometimes. '
    'Talked about television, football, whatever. At the station gate we parted. The correct procedure.</p>\n\n'
    '        <p>I have spent twenty-five years understanding what the correct procedure cost me.</p>\n\n'
    '        <p>I closed my eyes on the floor beside the desk.</p>'
)

assert CH2_ANCHOR in s, 'NOT FOUND: Ch2 anchor'
s = s.replace(CH2_ANCHOR, CH2_NEW, 1)
changes += 1
print('1. Ch2 proximity/pheromone paragraphs ✓')

# ─────────────────────────────────────────────────────────────────────────────
# 2. 3026 "The World" — add neural-orgasm paragraph after "hub for the suffering"
#    10-space indent for prose <p> tags inside .record column
# ─────────────────────────────────────────────────────────────────────────────
WORLD_ANCHOR = (
    '          <p>People go to the hub for the suffering.</p>\n'
    '        </div>\n'
    '      </div>'
)

WORLD_NEW = (
    '          <p>People go to the hub for the suffering.</p>\n\n'
    '          <p>The last thing to disappear was sex. It persisted, mechanically, for two more centuries '
    'after children became rare. But once the machine offered a direct neural pathway &#x2014; faster than '
    'the act, more complete, no negotiation, no the-next-morning &#x2014; the ritual began to hollow out '
    'the way all rituals hollow out when the meaning migrates. By 3026 people technically can. '
    'Most simply stopped seeing the reason.</p>\n\n'
    '          <p>Some of them remember that they used to want it. They log this as data.</p>\n'
    '        </div>\n'
    '      </div>'
)

assert WORLD_ANCHOR in s, 'NOT FOUND: World anchor'
s = s.replace(WORLD_ANCHOR, WORLD_NEW, 1)
changes += 1
print('2. 3026 World — neural orgasm paragraph ✓')

# ─────────────────────────────────────────────────────────────────────────────
# 3. Add Ch4 "Signal Loss" before closing of ch-track
#    6-space indent for structural elements, 8-space for prose <p>
# ─────────────────────────────────────────────────────────────────────────────
CH4_CONTENT = (
    '\n\n      <div class="ch-page" id="ch4">\n'
    '      <!-- ch4 image: /assets/artifacts/hard-mode-ch4.jpg &#x2014; to be added -->\n'
    '      <p class="ch-caption">Hard Mode &middot; Chapter Four &middot; <b>signal loss</b></p>\n\n'
    '      <p class="chapter-mark">Chapter Four &#x2014; "Signal Loss"</p>\n'
    '      <div class="prose">\n'
    '        <p class="first">I tried marijuana first.</p>\n\n'
    '        <p>The logic &#x2014; if it was logic &#x2014; was that the conversation had happened in a state '
    'between waking and not-waking, and that altering the chemistry of the state might widen the gap through '
    'which something had come. Three nights, different quantities, same result: slow thoughts, appetite, the '
    'particular loneliness of being high alone. No gap. No conversation. The ceiling.</p>\n\n'
    '        <p>Then alcohol, which I understood better. Alcohol had always had the quality of stripping '
    'things back &#x2014; not to truth, but to the version of yourself that was present before you learned '
    'to perform the other versions. I drank on a Tuesday. I drank with a colleague on a Thursday. I drank '
    'with intention and without it. I woke each morning with the usual residue and the usual absence.</p>\n\n'
    '        <p>I was trying to get back to twelve minutes.</p>\n\n'
    '        <p>During those twelve minutes something had spoken to me. Or something in me had spoken. Or '
    'I had assembled &#x2014; from grief and exhaustion and the specific quality of 4am &#x2014; a hallucination '
    'so internally consistent that it had reorganized the way I looked at the ceiling. I was not certain which. '
    'The uncertainty was itself a kind of signal: if it was pure hallucination, it was the most structured one '
    'I had ever had, and I have had structure enough to know the difference.</p>\n\n'
    '        <p>There had been a woman, for two years, who called when she wanted to and did not call when '
    'she did not want to. The architecture of the arrangement was entirely hers. I arrived when summoned. '
    'I was good at what she summoned me for &#x2014; she told me this, with the specific detachment of someone '
    'reviewing a service. I loved her in the way you love something that is dismantling you slowly without '
    'announcing its intentions. I understood only after the silence of a Thursday evening when she stopped '
    'calling &#x2014; weeks passing, then a month, then two &#x2014; that I had been useful to her the way '
    'a good appliance is useful: reliably, without reciprocity, until it wasn&#x2019;t needed anymore.</p>\n\n'
    '        <p>This had happened before I understood that the hunger I brought to bed was not ordinary '
    'hunger. It was something else &#x2014; something the body knows before the mind has language for it. '
    'That there is a version of this that runs out. That whatever the act of wanting a woman carries &#x2014; '
    'the specific weight of skin on skin, the not-quite-controllable quality of it, the particular proof that '
    'you are a living thing with a body and a temperature &#x2014; there is a version of the future where '
    'that is gone. Not taken. Simply not needed anymore. The machine would provide something faster and more '
    'complete and without the residue.</p>\n\n'
    '        <p>I had never said this to anyone. I am not certain it would have made sense to anyone. But '
    'it is why I had always brought to bed the quality that had confused and occasionally frightened people '
    'who did not expect it from someone my size and my manner &#x2014; that particular ferocity, the desire '
    'to use everything, to hold nothing back, as though each time might be practice for something being '
    'counted down on a counter I couldn&#x2019;t see.</p>\n\n'
    '        <p>I had not brought this quality to Pui. We had not arrived at a place where it could have '
    'been brought. We walked to the station. We talked about television. The correct procedure.</p>\n\n'
    '        <p>I thought about the senior &#x2014; the one with the bad temper who had been with her in '
    'the years after the studio. I had met him once, briefly. I had formed an opinion and then set it aside '
    'on the grounds that I had no standing. I was setting it down less easily now.</p>\n\n'
    '        <p>I poured a second drink.</p>\n\n'
    '        <p>Tomorrow I would wake up and exercise and go to work and eat and watch something and sleep. '
    'This was the shape of my life at forty-four. I had two dogs who slept at the foot of the bed and who '
    'were, I suspected, the primary reason the shape remained tolerable. Everything else was maintenance: '
    'maintain the body, maintain the income, maintain the appearance of a man with reasons.</p>\n\n'
    '        <p>I was not certain I had reasons.</p>\n\n'
    '        <p>I was certain that twelve minutes had given me the first thing in years that felt like one.</p>\n\n'
    '        <p>I thought about the car.</p>\n\n'
    '        <p>Not seriously. Or not yet seriously. More as a premise to examine: if the conversation was '
    'real, and if the world inside it was real, and if the woman in it was Pui, then dying in this world '
    'might constitute leaving it. The hypothesis had no evidence beyond the twelve minutes and a text message '
    'from an unknown number sent at 04:30 saying: <em>the door is always on the left.</em></p>\n\n'
    '        <p>I put the car thought down beside the drink.</p>\n\n'
    '        <p>Outside: the city in its long 3am exhale. Mali had moved from the floor to the base of the '
    'desk. Expo was still in the chair.</p>\n\n'
    '        <p>I pressed the permission. The machine proceeded.</p>\n'
    '      </div>\n'
    '      </div><!-- /ch-page ch4 -->'
)

TRACK_CLOSE = '      </div><!-- /ch-page ch3 -->\n      </div></div><!-- /ch-track /ch-viewport -->'
TRACK_NEW   = '      </div><!-- /ch-page ch3 -->' + CH4_CONTENT + '\n      </div></div><!-- /ch-track /ch-viewport -->'

assert TRACK_CLOSE in s, 'NOT FOUND: ch-track close anchor'
s = s.replace(TRACK_CLOSE, TRACK_NEW, 1)
changes += 1
print('3. Ch4 "Signal Loss" inserted ✓')

# ─────────────────────────────────────────────────────────────────────────────
# 4. Nav — add Ch4 link (handles both entity and literal em dash variants)
# ─────────────────────────────────────────────────────────────────────────────
added_nav = False
for dash in ['&#x2014;', '—', '—']:
    nav_anchor = (
        f'          <a class="ch-nav-item" data-page="2" href="javascript:void(0)">III {dash} The Prior</a>\n'
        '        </nav>'
    )
    if nav_anchor in s:
        nav_new = (
            f'          <a class="ch-nav-item" data-page="2" href="javascript:void(0)">III {dash} The Prior</a>\n'
            f'          <a class="ch-nav-item" data-page="3" href="javascript:void(0)">IV {dash} Signal Loss</a>\n'
            '        </nav>'
        )
        s = s.replace(nav_anchor, nav_new, 1)
        added_nav = True
        break
assert added_nav, 'NOT FOUND: nav anchor'
changes += 1
print('4. Nav Ch4 link ✓')

# ─────────────────────────────────────────────────────────────────────────────
# 5. JS LABELS — add 'chapter · iv'
# ─────────────────────────────────────────────────────────────────────────────
OLD_LABELS = "var LABELS=['chapter · i','chapter · ii','chapter · iii'];"
NEW_LABELS = "var LABELS=['chapter · i','chapter · ii','chapter · iii','chapter · iv'];"
assert OLD_LABELS in s, f'NOT FOUND LABELS (checking literal ·)'
s = s.replace(OLD_LABELS, NEW_LABELS, 1)
changes += 1
print('5. LABELS updated ✓')

# ─────────────────────────────────────────────────────────────────────────────
# 6. WIP note — three → four (try multiple dash/dot variants)
# ─────────────────────────────────────────────────────────────────────────────
updated_wip = False
for variant in [
    ('&#x2014; Hard Mode &middot; three chapters in &middot;', '&#x2014; Hard Mode &middot; four chapters in &middot;'),
    ('— Hard Mode · three chapters in ·',        '— Hard Mode · four chapters in ·'),
    ('— Hard Mode · three chapters in ·',                       '— Hard Mode · four chapters in ·'),
]:
    if variant[0] in s:
        s = s.replace(variant[0], variant[1], 1)
        updated_wip = True
        break
assert updated_wip, 'NOT FOUND: WIP note anchor'
changes += 1
print('6. WIP note updated ✓')

with open(PATH, 'wb') as f:
    f.write(s.encode('utf-8'))

print(f'\nAll {changes} changes applied.')
