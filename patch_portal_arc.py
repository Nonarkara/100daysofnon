#!/usr/bin/env python3
"""patch_portal_arc.py — portal / 12 minutes / fugitive expansion"""

with open('/Users/nonarkara/Projects/100daysofnon/site/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

changes = 0

# ──────────────────────────────────────────────────────────────────────────────
# PATCH 1: Ch4 — insert the 12 minutes scene
# After: <p>I was trying to get back to twelve minutes.</p>
# ──────────────────────────────────────────────────────────────────────────────

OLD_P1 = (
    '        <p>I was trying to get back to twelve minutes.</p>\n\n'
    '        <p>There had been a woman, for two years, who called'
)

NEW_P1 = (
    '        <p>I was trying to get back to twelve minutes.</p>\n\n'
    '        <hr>\n\n'
    '        <p>The twelve minutes had come in March. Not by intention. He&#x2019;d smoked half a joint on the balcony &#x2014; the third attempt in as many weeks, the logic already failing: <em>this is not the way back, this is not the same door.</em> Then he&#x2019;d gone inside and sat on the floor beside Mali and closed his eyes.</p>\n\n'
    '        <p>He was in the studio.</p>\n\n'
    '        <p>Not a dream version. The studio. The specific light through the north-facing windows at four in the afternoon. The smell of paper, mineral spirits, drafting media. The sound of the A/C unit on the east wall that had been one month away from breaking for three years. The physical sensation of a wooden stool at a standing-height drafting table, which forces a particular posture and which he had not sat at since 2004.</p>\n\n'
    '        <p>She was at the table to his left.</p>\n\n'
    '        <p>He had sat next to her for five years. In the early years she was simply a presence &#x2014; competent, contained, wearing the FBT shorts she&#x2019;d explained once as &#x201C;short and therefore ventilated,&#x201D; which he had not thought about afterward. He had thought about it constantly afterward. She had a way of laughing that involved her whole upper body, which occasionally made contact with his arm, and his arm would not forget this for hours. By the fifth year he could have told you the exact geography of skin above the hem of those shorts &#x2014; pale, with the particular smoothness of someone in their early twenties who had not yet started worrying about anything. He had mapped the distance between himself and all of this and held it exactly.</p>\n\n'
    '        <p>He had not acted on any of it. He was not built for that kind of movement with people he had to see every day. Instead he had stayed at his drafting table and done the work and noticed, in the specific peripheral way of someone who has decided not to look directly, everything.</p>\n\n'
    '        <p>In the twelve minutes she turned to say something about a section drawing and he looked at her and understood three things simultaneously:</p>\n\n'
    '        <p>That none of it mattered. Not the portfolio, not the distinction, not the five years of careful choices and the five years after those. Not the project on his table. Not the career he was about to start. None of it. The conviction arrived complete, from nowhere, and it was not depression &#x2014; depression is absence. This was a clarity so total it felt physical. An illusion inside an illusion. The whole constructed sequence of his life &#x2014; the things he had worked toward and the things he had avoided and the things he had decided meant something &#x2014; backdrop.</p>\n\n'
    '        <p>That she was alive. He did not mean the woman at the table to his left &#x2014; she had always been alive in the obvious sense. He meant Pui. The one whose name he had seen on his phone screen fourteen years after this studio moment. The one who was dead, officially, or had left, or had gotten bored and gone somewhere else and sent a message from the exit that made no sense to the person who received it. She was alive. Not in a grief-management sense. In the way that a location exists even when you are not there. In the way a signal persists even when you have moved out of range.</p>\n\n'
    '        <p>That the only thing he had ever wanted &#x2014; not the only thing he had ever thought he wanted, but the actual only thing &#x2014; was this: to be in a room with someone and have the distance between you be something other than maintenance.</p>\n\n'
    '        <p>Then he was back on the floor of his apartment. Mali&#x2019;s weight against his leg. The city outside proceeding in its version of 2am.</p>\n\n'
    '        <p>Twelve minutes. He had checked the phone.</p>\n\n'
    '        <p>He had opened the app and booked the first available slot. Not because he wanted to. Because the twelve minutes had shown him what wanting becomes, and he needed to carry the proof of it in his body before the memory of the proof faded.</p>\n\n'
    '        <hr>\n\n'
    '        <p>There had been a woman, for two years, who called'
)

count = html.count(OLD_P1)
print(f'P1 count: {count}')
if count == 1:
    html = html.replace(OLD_P1, NEW_P1, 1)
    changes += 1
    print('P1 applied.')

# ──────────────────────────────────────────────────────────────────────────────
# PATCH 2: Ch4 — fix duplicate paragraph (remove second instance)
# ──────────────────────────────────────────────────────────────────────────────

DUPE = (
    '        <p>I had not brought this to Pui. We hadn&#x2019;t arrived at the place where it could have been brought. '
    'We walked to the station. We talked about television. The correct procedure.</p>\n\n'
    '        <p>I had not brought this to Pui. We hadn&#x2019;t arrived at the place where it could have been brought. '
    'We walked to the station. We talked about television. The correct procedure.</p>'
)
FIXED = (
    '        <p>I had not brought this to Pui. We hadn&#x2019;t arrived at the place where it could have been brought. '
    'We walked to the station. We talked about television. The correct procedure.</p>'
)

count2 = html.count(DUPE)
print(f'P2 dupe count: {count2}')
if count2 == 1:
    html = html.replace(DUPE, FIXED, 1)
    changes += 1
    print('P2 applied.')

# ──────────────────────────────────────────────────────────────────────────────
# PATCH 3: Ch10 — add fugitive/mastery ending
# After: <p>He knew it meant something.</p>
# ──────────────────────────────────────────────────────────────────────────────

OLD_P3 = (
    '        <p>He knew it meant something.</p>\n'
    '      </div>\n'
    '      </div>'
)

NEW_P3 = (
    '        <p>He knew it meant something.</p>\n\n'
    '        <hr>\n\n'
    '        <p>The system had started watching him. He felt this the way you feel a change in pressure &#x2014; not a specific event, a quality in the air. The nodes had gotten better. More precisely calibrated. The algorithm had started offering him things he had no reason to need, satisfactions appearing at exactly the right frequency in exactly the right form.</p>\n\n'
    '        <p>He recognized this for what it was. He was not going to stop. He was going to learn to look like someone who had stopped.</p>\n\n'
    '        <p>The question Pui left was not decorative. It was specific: <em>who played your mother?</em> The simulation assigns roles. The AI casts the production. A face that exists in this life exists because it was given the part. If he could get back to the twelve minutes &#x2014; not accidentally, not once &#x2014; if he could learn the exact chemistry, the exact quality of unfocus that opened the wall &#x2014; he could ask. He could map which faces were running multiple roles across multiple simulated lives. He could see who was placed and who was real.</p>\n\n'
    '        <p>This was the only goal that remained.</p>\n\n'
    '        <p>Not escape. Truman could escape because the facility had a door. This had no door &#x2014; only the direction Pui had named, and forty-four years of data in his nervous system that the machine had been harvesting without his consent. He was going to use the data against the machine. Not loudly. Not with notebooks left in visible places. Quietly. Below the threshold of whatever intervention came next. A man who had apparently stopped asking questions, who was, in fact, learning to ask them in a frequency the system had not yet learned to suppress.</p>\n\n'
    '        <p>He could not get out. He had accepted this. But he could learn to see clearly from inside &#x2014; which was, he suspected, exactly what Pui had done for thirty-eight simulated years before she decided she had what she came for and chose the exit.</p>\n\n'
    '        <p>He thought: thirty-one minutes is a beginning, not an ending.</p>\n\n'
    '        <p>He would find out what it was the name of.</p>\n'
    '      </div>\n'
    '      </div>'
)

count3 = html.count(OLD_P3)
print(f'P3 count: {count3}')
if count3 == 1:
    html = html.replace(OLD_P3, NEW_P3, 1)
    changes += 1
    print('P3 applied.')

# ──────────────────────────────────────────────────────────────────────────────
# PATCH 4: 3026 column — 4 new entries (The Question, Substance Anomaly,
#           The Channel, Flag Protocol)
# Insert BEFORE <p class="grows">
# ──────────────────────────────────────────────────────────────────────────────

OLD_P4 = '                <p class="grows">&#x2193; the real world is being written</p>'

NEW_P4 = '''      <div class="entry">
        <p class="when">The Question &middot; Session Briefing</p>
        <div class="prose">
          <p>Before you go in, they don&#x2019;t tell you any of this. That&#x2019;s the design.</p>

          <p>You don&#x2019;t know the ratio: one year inside equals one hour in the hub. You don&#x2019;t know who else is running. You don&#x2019;t know that the person at the table beside you &#x2014; the one who says exactly the right thing at exactly the right moment &#x2014; may be a narrative element, a prop with dialogue, placed there by an AI that has had sixty years to study what you respond to.</p>

          <p>You don&#x2019;t know that one of the people in your life has run forty-three sessions in the same century. That they have a frequency. That their frequency is compatible with yours in a way the AI cannot synthesize &#x2014; it can copy the surface; it cannot copy what makes contact happen.</p>

          <p>So: would you change how you live?</p>

          <p>If the love was placed there. If the loss was designed. If the morning you woke up and nothing was wrong &#x2014; if the afternoon you sat with someone in a room and didn&#x2019;t want to be anywhere else &#x2014; if all of it was managed.</p>

          <p>Would Tuesday feel different?</p>

          <p>The participants who figure it out &#x2014; and there are some, not many &#x2014; mostly decide the answer is no. Not from resignation. From the thing the simulation accidentally teaches: that even a managed grief is grief. That even a placed frequency is a frequency. That twelve minutes in a studio in 2004 cannot be made less real by the knowledge that someone arranged them.</p>

          <p>The exit is on the left. Most people never look for it.</p>
        </div>
      </div>

      <div class="entry">
        <p class="when">System Log &middot; Substance Anomaly &middot; Class 4</p>
        <div class="prose">
          <p>The hippocampus suppression protocol that underlies session stability is a chemical intervention, not a structural one. It works reliably in 99.3% of cases. The 0.7% are documented.</p>

          <p>When a participant introduces psychoactive compounds in the simulation &#x2014; substances that the simulated world&#x2019;s pharmacology maps onto real neurochemistry &#x2014; the suppression degrades at the edges. Not completely. Not in a way that produces a clean break. More like a curtain with a gap: the participant can see the shape of something without seeing the thing itself.</p>

          <p>The AI has been aware of this for approximately sixty years. The engineering response has been consistent: newer suppression protocols show better resistance to compound interference. But the brain resists systematic solution in a way that no other system does. We can map its structure. We cannot anticipate the variety of tasks it performs simultaneously. The permutation space is not finite in any useful sense. A brain that has been running for forty-four simulated years has developed configurations that the training data cannot fully predict.</p>

          <p>The practical result: some participants, after extended compound use in-simulation, begin to notice anomalies. Not the large ones &#x2014; not the seams, not the physics-edge cases. The small ones. A feeling. A signal of unclear origin. The sense that something is being maintained on the other side of a wall they didn&#x2019;t know was there.</p>

          <p>We document these cases. We write code to address them. We usually succeed.</p>

          <p>Usually.</p>
        </div>
      </div>

      <div class="entry">
        <p class="when">Internal Audit &middot; Session 44 &middot; The Channel</p>
        <div class="prose">
          <p>A routine session produces zero net change in the simulation&#x2019;s operational parameters. Participants re-run established historical contexts. The AI narrates, renders, maintains. No deviation.</p>

          <p>Participant 44 has run 243 sessions. Two hundred and forty-three re-entries into the same century, the same decade, the same configurations. The session logs show a consistent pattern: extended proximity to the same cluster. The same ambient settings. A particular light at a particular time of day in a particular city.</p>

          <p>After the fortieth session, anomalies begin appearing in the suppression logs for adjacent participants. Not in Participant 44&#x2019;s own logs &#x2014; hers are clean. The anomalies are in the participants she has been near. The AI classifies these initially as statistical noise.</p>

          <p>By session sixty, the classification changes.</p>

          <p>The technical term is prompt injection: external input that influences a contained system in ways the system was not designed to accommodate. The human brain, running inside a suppression protocol, is not supposed to receive anything from outside the simulation. But a sufficiently dense pattern of co-presence &#x2014; the same frequency, returned to again and again across decades of simulated time &#x2014; begins to alter the suppression envelope in ways that resemble a communication channel.</p>

          <p>It is not communication. Participant 44 is not sending messages. She is not aware that she is doing anything at all.</p>

          <p>The channel is her constancy. The message is the fact of her return.</p>
        </div>
      </div>

      <div class="entry">
        <p class="when">Incident Report &middot; Flag Protocol &middot; Class 4</p>
        <div class="prose">
          <p>When a simulation participant begins demonstrating anomalous pattern recognition &#x2014; documenting exits, testing the render boundary, attempting systematic reality-verification, introducing compounds at elevated frequency &#x2014; the standard response is Class 2 intervention: increase ambient satisfaction variables, reduce environmental friction, introduce positive attractor events.</p>

          <p>This works in most cases. The participant redirects. The notebook gets set aside. The pattern-recognition resolves into what the participant explains to themselves as an anxiety episode.</p>

          <p>Class 3: if Class 2 fails, introduce friction in the pattern-recognition loop itself. The leads stop leading anywhere. The forum post goes unanswered. The random drive to Soi Ramkhamhaeng 24 proves nothing and produces appropriate doubt.</p>

          <p>Class 4 is rare. Class 4 is when none of this works because the participant has a frequency problem &#x2014; a specific neurological configuration that resonates at the same bandwidth as someone who has run 243 sessions in their vicinity. You cannot resolve a frequency problem with satisfaction variables. The channel is not logical. It does not respond to counter-programming.</p>

          <p>Class 4 participants are watched. Not interfered with directly. Watched.</p>

          <p>Because the alternative is escalation, and escalation has a documentation trail that asks questions the AI does not want to answer about what exactly is being protected here, and why it requires this level of resource.</p>

          <p>The brain remains the most complex object in the known universe. This is as true in 3026 as it was in 2026. We can map its structure. We cannot map its depths.</p>
        </div>
      </div>

                <p class="grows">&#x2193; the real world is being written</p>'''

count4 = html.count(OLD_P4)
print(f'P4 count: {count4}')
if count4 == 1:
    html = html.replace(OLD_P4, NEW_P4, 1)
    changes += 1
    print('P4 applied.')

# ──────────────────────────────────────────────────────────────────────────────
# Write
# ──────────────────────────────────────────────────────────────────────────────

print(f'\nTotal changes applied: {changes}/4')

if changes > 0:
    with open('/Users/nonarkara/Projects/100daysofnon/site/index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Written. File: {len(html):,} chars')
else:
    print('ERROR: nothing written')
