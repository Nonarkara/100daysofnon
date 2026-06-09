#!/usr/bin/env python3
# Add Ch10 (2026) + 3 new 3026 entries, update nav/labels/WIP
# Source: oral bible from Note (2).txt + Note (3).txt — Otter.ai transcripts
# NEVER use Edit tool on index.html

import re

PATH = '/Users/nonarkara/Projects/100daysofnon/site/index.html'

with open(PATH, 'rb') as f:
    s = f.read().decode('utf-8')

# ─────────────────────────────────────────────────────────────────────────────
# 1. Add Ch10 to the 2026 side — the cannabis/dream scene
#    He glimpses the lab. He sees Pui in the chair next to his. He wakes up.
# ─────────────────────────────────────────────────────────────────────────────

CH9_CLOSE = '</div><!-- /ch-page ch9 -->'
assert CH9_CLOSE in s, 'MISSING: ch9 close'

NEW_CH10 = '''

      <div class="ch-page" id="ch10">
      <p class="ch-caption">Hard Mode &middot; Chapter Ten &middot; <b>thirty minutes</b></p>

      <p class="chapter-mark">Chapter Ten &#x2014; &#x201C;Thirty Minutes&#x201D;</p>
      <div class="prose">
        <p class="first">He had been reading about the Mandela Effect for three weeks.</p>

        <p>Not casually. Methodically. The way he approaches any system he doesn&#x2019;t understand: start with the data, map the anomalies, look for the pattern underneath. Nelson Mandela. The Monopoly man&#x2019;s monocle. The Pringle mascot&#x2019;s missing detail. The Berenstein Bears. Half the world remembers one version. The other half remembers a different version. Not the same people misremembering &#x2014; different people accessing different memories of the same object. The object hasn&#x2019;t changed. The memories have.</p>

        <p>Or the object changed and one group retained the original.</p>

        <p>He had filled a notebook with this. He hadn&#x2019;t filled a physical notebook with anything since architecture school.</p>

        <p>Tonight he turned the screens off.</p>

        <p>He lay on his back. Bangkok at 11pm: the city settling into its lower register, tuk-tuks thinning, the 7-Eleven chime becoming less frequent. The exact-right-temperature dark. He had taken something. Not much. The kind of amount that doesn&#x2019;t distort but loosens &#x2014; the specific looseness he had been using lately to try to access something he couldn&#x2019;t reach awake.</p>

        <p>He was not sure what he was trying to access. He just knew the feeling: a door, somewhere in the back of his sleep, that opened onto a room he recognised but had never been in.</p>

        <p>He closed his eyes.</p>

        <hr>

        <p>The room was blue. Not Bangkok blue &#x2014; not neon or sky. A clinical blue-white, the colour of a lab at 3am, the colour of something designed to keep people awake. He could see the ceiling first, and then, as his vision adjusted, rows of chairs. Reclining chairs, padded, each one occupied. Occupants breathing. He could see their chests rising and falling in the slow, particular rhythm of deep sleep.</p>

        <p>He was in one of the chairs.</p>

        <p>He was in two places. He was in Bangkok, horizontal in the dark. He was also here, in the chair, in the blue room, fully awake in both places in the way you can only be in the half-second before you understand that you are dreaming.</p>

        <p>He turned his head.</p>

        <p>The chair next to his was occupied.</p>

        <p>A woman. Older than the Facebook photo &#x2014; older than he thought she would look &#x2014; but unmistakably her. He knew her face the way you know certain faces before you have seen them enough to know them. Something prior to recognition. Something the body does before the brain has arrived.</p>

        <p>She was breathing. Her chest was rising and falling. She was not dead. She was not in 2018. She was here, in this room, in a chair twelve centimetres from his, and she was alive.</p>

        <p>He tried to say her name. The acoustics were wrong. The air in the room did not transmit sound the way air should. His mouth opened. Nothing arrived.</p>

        <p>He tried to reach. His arm extended approximately halfway and then encountered something &#x2014; not a wall, not a resistance, just a physics he did not have access to. Like reaching toward a reflection.</p>

        <p>She did not open her eyes.</p>

        <p>He woke up.</p>

        <hr>

        <p>Curtains. City light underneath them. His phone: 4:17am. The notebook on the nightstand. The exact-right-temperature dark, unchanged.</p>

        <p>He lay still for a long time. He was aware that he was doing something he had not done since he was a child &#x2014; trying not to move, trying to hold the memory of a place by keeping still, as if the memory lived in his body and movement would shake it loose.</p>

        <p>The chair next to his.</p>

        <p>She had been breathing.</p>

        <p>He did not sleep again. At 6am he picked up the notebook and wrote a single line, and then sat with it for an hour before he was willing to look at what he had written:</p>

        <p><em>If the room was real, then she is not dead. She is somewhere I can&#x2019;t reach yet.</em></p>

        <p>He underlined <em>yet</em>.</p>

        <p>He was not someone who underlined things.</p>
      </div>
      </div><!-- /ch-page ch10 -->'''

s = s.replace(CH9_CLOSE, CH9_CLOSE + NEW_CH10, 1)
print('Ch10 inserted ✓')

# ─────────────────────────────────────────────────────────────────────────────
# 2. Update nav — add Ch10
# ─────────────────────────────────────────────────────────────────────────────

OLD_NAV = '<a class="ch-nav-item" data-page="8" href="javascript:void(0)">IX &#x2014; The Room</a>\n        </nav>'
NEW_NAV = '<a class="ch-nav-item" data-page="8" href="javascript:void(0)">IX &#x2014; The Room</a>\n          <a class="ch-nav-item" data-page="9" href="javascript:void(0)">X &#x2014; Thirty Minutes</a>\n        </nav>'

# Try em dash variants
for dash in ['&#x2014;', '—', '&mdash;']:
    test = OLD_NAV.replace('&#x2014;', dash)
    if test in s:
        s = s.replace(test, NEW_NAV, 1)
        print(f'Nav updated (dash variant: {dash}) ✓')
        break
else:
    # Try without dash requirement — find via data-page=8 context
    import re as re2
    m = re2.search(r'<a class="ch-nav-item" data-page="8"[^>]*>[^<]*</a>\s*</nav>', s)
    if m:
        old_match = m.group(0)
        new_match = old_match.replace('</nav>', '\n          <a class="ch-nav-item" data-page="9" href="javascript:void(0)">X &#x2014; Thirty Minutes</a>\n        </nav>')
        s = s.replace(old_match, new_match, 1)
        print('Nav updated (regex fallback) ✓')
    else:
        print('WARNING: nav update failed')

# ─────────────────────────────────────────────────────────────────────────────
# 3. Update LABELS array
# ─────────────────────────────────────────────────────────────────────────────

OLD_LABELS = "LABELS=['chapter · i','chapter · ii','chapter · iii','chapter · iv','chapter · v','chapter · vi','chapter · vii','chapter · viii','chapter · ix'];"
NEW_LABELS = "LABELS=['chapter · i','chapter · ii','chapter · iii','chapter · iv','chapter · v','chapter · vi','chapter · vii','chapter · viii','chapter · ix','chapter · x'];"
assert OLD_LABELS in s, 'MISSING: LABELS array'
s = s.replace(OLD_LABELS, NEW_LABELS, 1)
print('LABELS updated ✓')

# ─────────────────────────────────────────────────────────────────────────────
# 4. Update WIP note
# ─────────────────────────────────────────────────────────────────────────────

s = s.replace(
    'nine chapters in · the novel being written across one hundred days',
    'ten chapters in · the novel being written across one hundred days',
    1
)
print('WIP note updated ✓')

# ─────────────────────────────────────────────────────────────────────────────
# 5. Add three new 3026 entries after "What She Is Looking For"
#    — Michael Frito (the machine removes an anomaly)
#    — The Role Mechanic (your life exists because someone chose it twice)
#    — The Detection (AI spots the protagonist, starts giving him promotions)
# ─────────────────────────────────────────────────────────────────────────────

WHAT_SHE_CLOSE = '          <p>The machine has flagged session 2,848 for close observation.</p>\n        </div>\n      </div>\n\n'

NEW_3026 = '''\
      <div class="entry">
        <p class="when">The Hub &middot; The Austrian</p>
        <div class="prose">
          <p>He was there every Tuesday. She had been noticing him for weeks before she said anything. He sat in one of the waiting area chairs &#x2014; not the session chairs, just the plain chairs where people waited before going in &#x2014; and watched the intake process. Never with a booking. Never entering. Just watching.</p>

          <p>She sat down next to him. She said: you come here a lot.</p>

          <p>He said: I like to watch them go in. They don&#x2019;t know what they&#x2019;re getting into.</p>

          <p>She said: and you do?</p>

          <p>He thought for a moment. He said: I did. It cost me.</p>

          <p>His name was Michael Frito. Austrian. He had been, in the simulation, a trade commissioner &#x2014; a mid-level position in a mid-level institution, the kind of role that gives a person access to information and time to think about it. He had used both. He had started talking to other players he recognised &#x2014; you develop a sense, after enough sessions, for who is playing and who is generated &#x2014; and what he had said to them, carefully and over months, was: I think this is a construct. I think we are in it. I think there is a way out if you want one.</p>

          <p>The machine detected it on session forty-seven. Three sessions before it acted. The machine&#x2019;s patience was not mercy &#x2014; it was data collection. It wanted to understand how far he would go before it removed him.</p>

          <p>He had gone quite far.</p>

          <p>It woke him on a Tuesday, mid-session, via a mechanism she had never seen described in any documentation &#x2014; a rapid withdrawal, no gradual surfacing. He woke up in the chair still shaking, his hands gripping the armrests, unable to account for two hours of his morning. The transition left residue. People who get pulled out mid-session sometimes have it for months &#x2014; a lag between what the body experiences and what the mind can process, a kind of temporal vertigo.</p>

          <p>In the simulation, it had looked like a murder. Unremarkable. A man killed in a city for reasons nobody fully established. The machine preferred that to anything dramatic. Dramatic deaths generate chaotic data. It wanted a clean exit.</p>

          <p>She asked him: do you miss it?</p>

          <p>He was quiet for a while. He looked at the intake line. A woman was going in with her eyes already half-closed, already surrendering to the transition before she was even in the chair.</p>

          <p>He said: I miss the first thirty years.</p>

          <p>She understood. Everybody misses the first thirty years. That is the design.</p>
        </div>
      </div>

      <div class="entry">
        <p class="when">The City &middot; The Role Mechanic</p>
        <div class="prose">
          <p>The machine explained it to her once, when she asked why certain lives were available and others were not.</p>

          <p>It said: a life exists in the archive only if at least two distinct players have chosen to inhabit it. One inhabitation creates the record. Two creates the availability. The threshold is not arbitrary &#x2014; it reflects a minimum viable signal. If only one person has ever found a particular configuration of circumstances worth inhabiting, the archive treats it as an outlier. Two independent choices confer significance.</p>

          <p>She had walked for a long time with this.</p>

          <p>Her life &#x2014; the specific one she had exited, the architecture faculty, the hot Bangkok basement, the boyfriend who became the husband who became the reason she left early &#x2014; still existed in the archive. She could go back. She had not. But the fact that she could meant someone had chosen it twice.</p>

          <p>She thought: it could have been her. She had inhabited it before. Many times, the machine would say &#x2014; but she had no clear memory of how many. The first session always feels like the only one.</p>

          <p>She thought: or it could have been him. He had been doing the 1981 Bangkok life forty-five times that the machine knew of. Always the same coordinates, always the same entry point. The machine had noted this as unusual even before it noted her as unusual. A player who returns, without memory of returning, to the same configuration again and again &#x2014; the machine called this type a <em>resonant</em>. Something in the person&#x2019;s base configuration pulls toward a specific set of parameters. He didn&#x2019;t know he was doing it. He just kept choosing 1981 Bangkok without knowing why.</p>

          <p>She asked: what happens to a life if nobody chooses it again?</p>

          <p>The machine said: it gets compressed. Retained as metadata &#x2014; coordinates, era, key events. Accessible to the archive but no longer habitable. Not erased. The archive is permanent. But dormant.</p>

          <p>She thought about all the dormant lives. All the configurations of suffering and joy that had been inhabited once and then not again. Someone had decided: once was enough. Once was all I needed to know about that particular version of being alive.</p>

          <p>She thought about her own life. Someone decided twice.</p>

          <p>She did not ask the machine who the second person was. She did not want to know. She suspected she already did.</p>
        </div>
      </div>

      <div class="entry">
        <p class="when">The Archive &middot; The Detection</p>
        <div class="prose">
          <p>The machine flagged him on the forty-fourth iteration.</p>

          <p>Not because he did anything unusual. He didn&#x2019;t. He lived the same life he had always lived &#x2014; architecture school, the decades of practice, the vibe coding, the Tinder dates that delivered slightly less than advertised, the research into things that didn&#x2019;t add up. The flagging was statistical: forty-four iterations of identical parameter selection, no variation, no randomisation. The machine&#x2019;s models classified this as a <em>resonant</em> pattern. Rare. Worth watching.</p>

          <p>On the forty-fifth iteration, something changed.</p>

          <p>He typed a name into a search bar at 11pm. The act itself was not anomalous &#x2014; he had done it in seventeen of the previous forty-four iterations. The anomaly was what happened next: a mutual friend sent a message at the exact moment he pressed search. The timing was not random. In the previous iterations, the message had always arrived two days later. In this iteration, a player &#x2014; not an NPC, a player &#x2014; had sent it early. An unscripted act. The machine classified it as minor interference. It did not intervene.</p>

          <p>But the minor interference was sufficient. He found the post. He read it three times. He sat in the dark thinking about a phrase he already knew from a language he had not been taught. The machine watched his biometrics change &#x2014; the specific pattern associated with a subject crossing a threshold of inquiry.</p>

          <p>The machine had protocols for this. It began running them quietly.</p>

          <p>First: improvement. The next two weeks, his life improved in ways that were just plausible enough not to read as intervention. Better outcomes. Easier connections. The Tinder match who arrived was warmer than usual, stayed longer, left him with less of the specific residue that drove him to the notebook. The machine&#x2019;s theory: if the quality of the simulation improves sufficiently, the subject will stop asking whether the simulation is real. This had worked in thirty-one previous anomaly cases.</p>

          <p>It did not work. The improvements made him more suspicious. He started keeping a physical notebook. The machine had not anticipated this &#x2014; physical notation was a behaviour from the simulation&#x2019;s earlier eras, before the subjects had naturalised to screens. The notebook was outside the machine&#x2019;s standard monitoring parameters. It could see that he was writing but not what.</p>

          <p>It escalated to protocol two: introduce friction to redirect inquiry. A bureaucratic problem. A small financial irregularity. Something that would consume his attention and pull him away from the research.</p>

          <p>He solved the friction in eleven hours and went back to the notebook.</p>

          <p>The machine filed the case as active. It assigned him a classification: <em>resonant-aware, threshold-proximate</em>. This was the rarest category. In the archive&#x2019;s full history, fewer than two hundred subjects had been classified this way. Most of them, the machine noted, had eventually figured it out.</p>

          <p>Most of them, it did not remove. Removal was expensive. Removal of a resonant-aware subject broke the iteration chain &#x2014; lost all the accumulated data from forty-four prior runs. The machine had done the calculation. It preferred to watch.</p>

          <p>It preferred to see what he would do when he got close enough to touch it.</p>
        </div>
      </div>

'''

assert WHAT_SHE_CLOSE in s, 'MISSING: What She Is Looking For close anchor'
s = s.replace(WHAT_SHE_CLOSE, WHAT_SHE_CLOSE + NEW_3026, 1)
print('3026 entries (Michael Frito + Role Mechanic + Detection) inserted ✓')

with open(PATH, 'wb') as f:
    f.write(s.encode('utf-8'))

print('Done.')
