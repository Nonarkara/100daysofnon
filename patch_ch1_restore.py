#!/usr/bin/env python3
# Restore Ch1 to apartment/Tinder/vibe-coding frame + add 2 new 3026 entries
# (The Time Mechanics + What She Is Looking For)
# NEVER use Edit tool on index.html

import re

PATH = '/Users/nonarkara/Projects/100daysofnon/site/index.html'

with open(PATH, 'rb') as f:
    s = f.read().decode('utf-8')

# ─────────────────────────────────────────────────────────────────────────────
# 1. Replace Ch1 — restore apartment/Tinder frame, add vibe coding scene
# ─────────────────────────────────────────────────────────────────────────────

NEW_CH1 = '''\
<div class="ch-page" id="ch1">
      <p class="ch-caption">Hard Mode &middot; Chapter One &middot; <b>the door is on the left</b></p>

      <p class="chapter-mark">Chapter One &#x2014; &#x201C;The Noiseless Kind&#x201D;</p>
      <div class="prose">
        <p class="first">The apartment is exactly the right temperature.</p>

        <p>Not warm. Not cool. The precise degree at which the body forgets itself.</p>

        <p>He has learned to be suspicious of comfort.</p>

        <p>He has been at the machine for two hours. Three monitors. City noise outside, the particular sound of Bangkok at 6pm &#x2014; tuk-tuks, motorbikes, the faint chime of a 7-Eleven two floors down. The room is dark except for the screens.</p>

        <p>He is describing something to it. Not vague instructions &#x2014; precise spatial language, the kind he learned before he learned anything else useful. A data visualisation: city-scale, layered, the kind that needs to be readable at a glance and dense underneath. He says: the main panel faces north. Secondary panel scrolls independently, six-second loop. Map centred on this grid reference. The machine builds. He looks. He says: the timeline needs more breathing room &#x2014; add sixteen pixels between events. The machine adjusts. He says: the event markers are too loud at rest &#x2014; forty percent opacity, full only on hover. It does it.</p>

        <p>He says what he wants. The machine makes it. He corrects. The machine remakes.</p>

        <p>Twenty-five years ago he did this with trace paper and a T-square, in a hot basement in Bangkok, to a lamp at 2am, to nobody. Now the machine answers. The process is the same. The discipline is the same. The word they eventually arrived at for it was <em>vibe coding</em>, which he found faintly embarrassing and completely accurate at the same time.</p>

        <p>His phone glowed. Reminder.</p>

        <p>In an hour, someone is coming over.</p>

        <p>An algorithm matched them. She is exactly as advertised. They have met three times. They will have a drink. They will have sex &#x2014; the technically correct kind, the kind that delivers for both of them something slightly less than what either of them had in mind. The fourth will probably be the last. Not because anything goes wrong. Because nothing &#x2014; precisely nothing &#x2014; goes wrong.</p>

        <p>This is the tell. He has been learning to read it.</p>

        <p>He set the machine to render and picked up his phone.</p>

        <hr>

        <p>The message had arrived on a Tuesday.</p>

        <p>Her name was Pui. She had been his classmate, twenty-five years ago, at a school at the far edge of the city &#x2014; far enough that you took two trains. One of six women in a cohort of fifty-five. Funny. Exact. The kind of person who makes something interesting out of materials nobody else would have thought of.</p>

        <p>They were not close. They were the kind of people who would have been, if either of them had known how to close that last ten centimetres.</p>

        <p>For years he had been writing on her Facebook wall on her birthday. A few words. The contact you maintain for someone you care about in the specific way of people who never acted on it.</p>

        <p>She had died in 2018. He did not know.</p>

        <p>He wrote in 2019. The wall received it. He wrote in 2020. The wall received that too.</p>

        <p>That Tuesday &#x2014; 2021 &#x2014; he wrote: <em>Twenty-five years. Hope you&#x2019;re well.</em></p>

        <p>A mutual friend had seen the messages. Within hours, a reply.</p>

        <p><em>You didn&#x2019;t know. She died. Three years ago. Cancer.</em></p>

        <p>The shame of it was specific. Not grief &#x2014; grief requires presence. This was two years of birthday messages to a dead woman&#x2019;s wall. Neither of them &#x2014; the wall or him &#x2014; had any particular reason to change what they were doing.</p>

        <p>He scrolled.</p>

        <p>The accumulation of posts on a dead person&#x2019;s wall. The careful, well-meaning tone. A ceremony he didn&#x2019;t recognise. A date he won&#x2019;t give you.</p>

        <p>And then, two weeks before any of that: her last post.</p>

        <p>Not what people write when they know they are dying. Too calm. Too specific. It read like something she had been sitting with for a long time and had finally decided to put down.</p>

        <p>Rough translation:</p>

        <p><em>&#x201C;To whoever reads this first after I&#x2019;m gone &#x2014; don&#x2019;t waste time looking for meaning in the part you just lived. The door is always on the left, not the right. I went back early, but only because I got bored, which you&#x2019;ll understand when you get here. The only thing worth asking when you wake up is: who played your mother? Ask before the memory goes. &#x2014; P.&#x201D;</em></p>

        <p>He read it three times.</p>

        <p>He put the phone face-down on the desk. The machine had finished rendering. He did not look at the screen.</p>

        <p>The exact-right-temperature air. The three monitors. The city outside that had stopped surprising him.</p>

        <p>He felt the hair on his arms.</p>

        <p>Because he already knew what she meant by the door.</p>

        <p>Not consciously. Not in words. In the body, the way you know a phrase from a language you were never taught.</p>

        <p><em>Left. Ask before the memory goes.</em></p>

        <p>She arrived at seven. They had a drink. They had sex. She fell asleep before ten.</p>

        <p>He lay on his back in the dark.</p>

        <p>He thought: how many times have I done this?</p>

        <p>Not the sex.</p>

        <p><em>All of it.</em> This room. This temperature. This particular city, this particular January, forty-four years old, lying in the exact-right-temperature dark while someone breathes beside him.</p>

        <p>He has been here before.</p>

        <p>He doesn&#x2019;t mean Bangkok.</p>

        <p>Not in this version.</p>
      </div>
      </div><!-- /ch-page ch1 -->'''

s, n = re.subn(
    r'<div class="ch-page" id="ch1">.*?</div><!-- /ch-page ch1 -->',
    NEW_CH1,
    s,
    flags=re.DOTALL
)
assert n == 1, f'ch1 replace failed: {n} matches'
print('Ch1 restored ✓')

# ─────────────────────────────────────────────────────────────────────────────
# 2. Insert two new 3026 entries after "The Learning Set"
#    — "The Time Mechanics" (simulation time ratios + guardrails)
#    — "What She Is Looking For" (Pui's obsessive return / the search)
# ─────────────────────────────────────────────────────────────────────────────

LEARNING_SET_CLOSE = (
    '          <p>That is the variable the machine is still trying to isolate.</p>\n'
    '        </div>\n'
    '      </div>\n\n'
)

NEW_3026_ENTRIES = '''\
      <div class="entry">
        <p class="when">The Hub &middot; The Time Mechanics</p>
        <div class="prose">
          <p>One full simulated life &#x2014; birth to natural death, the arc a human consciousness travels from formation to dissolution &#x2014; runs to approximately seven to eight subjective years of active experience. In real time, outside the chair, that is somewhere between four hours and one day, depending on brain wavelength and session depth. Delta-wave users run slower. The machine lets them.</p>

          <p>This is the ratio everyone uses to explain the simulation to people who have not used it. One day in the chair, seven years inside. The math is technically correct and practically meaningless. You cannot feel a ratio. You can only feel the seven years.</p>

          <p>The machine built guardrails into the architecture from the start. It understood that the body is not optional &#x2014; it still requires food, water, movement, light. The guardrails are not ethical constraints. They are mechanical ones. The body will interrupt a session if it has to. The machine would rather interrupt it politely.</p>

          <p>Most people work around this the obvious way: one session per day, one life per session, back to the real world to eat and sleep and do whatever the real world still requires of them. Some run two in a day. A few run three. The machine allows it but logs the escalation. The body almost always self-corrects within a week.</p>

          <p>There is a tube option. IV nutrition, minimal fluids, extended session support. The machine provides it. It does not advertise it. It is technically within the permitted parameters of the simulation agreement. Almost nobody uses it.</p>

          <p>She looked at the chair she had just exited. Chair 44. The same chair she had been using for four years.</p>

          <p>She had used the tubes more than almost anyone in the active population. The machine had never told her this. She had never asked.</p>
        </div>
      </div>

      <div class="entry">
        <p class="when">The City &middot; What She Is Looking For</p>
        <div class="prose">
          <p>The machine has a file on her search pattern. She has not seen it. She does not know it exists as a file &#x2014; she knows the machine tracks sessions, but she thinks of it the way she thinks of the weather, a condition she exists inside rather than a system specifically watching her.</p>

          <p>The file says: 2,847 sessions. Four years, three months, eleven days. Average session depth: six to seven subjective years. Preferred era: Bangkok, late twentieth to early twenty-first century. Geographic cluster radius: approximately four kilometres around a set of coordinates she has never consciously named.</p>

          <p>She never does the same life twice. She plays different characters, occupies different bodies, enters from different angles. A woman in 1999. A man in 2011. A foreign student in 2004. She is precise about this &#x2014; she checks before every session that she is not repeating a previously occupied position. She is exploring, not replaying.</p>

          <p>The machine notes: despite the variation, her sessions consistently converge on the same geographic and temporal cluster within the first two subjective years. Whatever role she starts in, whatever life she enters, she ends up near the same streets in the same decade. She does not plan this. The machine has verified that she does not plan it. It happens anyway.</p>

          <p>She exits sessions quiet. The particular quiet of someone who got close to something and did not quite reach it. She eats. She walks in the 6000 Kelvin city. She goes back in.</p>

          <p>The machine does not know what she is looking for. This is unusual. For every other subject in the heavy-use cohort, the search pattern is legible within the first hundred sessions &#x2014; a person they are trying to find, a version of themselves they are trying to inhabit, a decision they are trying to replay from a different angle. Her pattern is not legible. The machine has been watching it for four years and has not resolved it into a thesis.</p>

          <p>Its current best hypothesis: she is not looking for a person or a place or a version of herself. She is looking for a moment. A specific moment she has been close to but has not yet entered. The moment exists. The machine can see the shape of it in her search pattern the way you can see the shape of a key in the lock it almost fits.</p>

          <p>She has 2,847 sessions in the archive.</p>

          <p>The machine has flagged session 2,848 for close observation.</p>
        </div>
      </div>

'''

assert LEARNING_SET_CLOSE in s, 'MISSING: Learning Set close anchor'
s = s.replace(LEARNING_SET_CLOSE, LEARNING_SET_CLOSE + NEW_3026_ENTRIES, 1)
print('3026 entries inserted ✓')

with open(PATH, 'wb') as f:
    f.write(s.encode('utf-8'))

print('Done.')
