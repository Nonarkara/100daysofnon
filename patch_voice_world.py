#!/usr/bin/env python3
# Rewrite Ch1 (Som Tam → Facebook → her post) + Ch2 (basketball/sweat/vibe coding)
# + two new 3026 entries (He's Still In + What Happened To Us)
# NEVER use Edit tool on index.html

import re

PATH = '/Users/nonarkara/Projects/100daysofnon/site/index.html'

with open(PATH, 'rb') as f:
    s = f.read().decode('utf-8')

def replace_chapter(text, ch_id, new_content):
    pattern = r'<div class="ch-page" id="' + ch_id + r'">.*?</div><!-- /ch-page ' + ch_id + r' -->'
    result, n = re.subn(pattern, new_content, text, flags=re.DOTALL)
    assert n == 1, f'Pattern not found: {ch_id}'
    return result

# ─────────────────────────────────────────────────────────────────────────────
# CH1 — The Noiseless Kind
# Opens: Som Tam woman → Facebook archaeology → her last post → 2021
# ─────────────────────────────────────────────────────────────────────────────
CH1 = '''\
<div class="ch-page" id="ch1">
      <p class="ch-caption">Hard Mode &middot; Chapter One &middot; <b>the noiseless kind</b></p>

      <p class="chapter-mark">Chapter One &#x2014; &#x201C;The Noiseless Kind&#x201D;</p>
      <div class="prose">
        <p class="first">There is a woman in front of his alleyway.</p>

        <p>She runs a Som Tam stall. She&#x2019;s there every evening when he comes home. He has been walking past her for three years. He does not know her name. She always has her back to him until he passes, and by then he&#x2019;s already gone. He has no particular reason to notice her except that he does, every time, and every time he notices her there is a feeling he can&#x2019;t locate.</p>

        <p>This evening he stopped.</p>

        <p>He stood on the pavement for longer than a person stands on a pavement for no reason. She didn&#x2019;t turn around. He went upstairs.</p>

        <p>He opened his phone.</p>

        <hr>

        <p>The profile is still active. Profile picture unchanged since 2017 &#x2014; a beach, a hat, she&#x2019;s not quite looking at the camera. People still post on her wall. Every year, around the date: thinking of you. We miss you. Hard to believe it&#x2019;s been X years.</p>

        <p>He scrolled down.</p>

        <p>It always takes longer than he expects. 2024. 2023. 2022. The messages thin but don&#x2019;t stop &#x2014; there are people who have been writing to her every year since it happened, people who found some kind of clarity in the ritual of it. He scrolled past them.</p>

        <p>2021 is the year he found out.</p>

        <p>He hadn&#x2019;t spoken to her in seven years. One evening &#x2014; late, he was at his desk, just the city noise and the lamp and the ordinary feeling of 11pm &#x2014; he typed her name into the search bar. Just to see. No specific reason. The kind of impulse you get sometimes, years after the last conversation, just to confirm that a person is still in the world.</p>

        <p>A mutual friend sent a message the exact moment he pressed search. The timing was strange. It was almost funny.</p>

        <p><em>Didn&#x2019;t you know?</em></p>

        <p>He didn&#x2019;t know.</p>

        <p>He scrolled past 2021, into 2020, into 2019. The shock-wave messages. The ones that are really about the person writing them. The ones that say <em>I can&#x2019;t believe it</em> seven times because the writer can&#x2019;t believe it and has no other language.</p>

        <p>Past those: her posts. Her life as she was living it.</p>

        <p>He had done this before. He had scrolled this far before. But he had never scrolled all the way to the last one she posted herself. Not because he had avoided it &#x2014; he just always stopped somewhere in 2019, at something she&#x2019;d written about a book or a sunset, and closed the app and went to bed.</p>

        <p>Tonight he kept going.</p>

        <p>Her last post.</p>

        <p>She had written about doors. About recognising a place you&#x2019;ve been before. About the way some experiences arrive with a feeling of already-knowing, and how you learn to trust that feeling or you don&#x2019;t, and how the people who trusted it always seemed to know something the others didn&#x2019;t. She had written it in her way &#x2014; slightly oblique, slightly too perceptive, the kind of post that people liked without knowing why. Twenty-three likes. Four comments. The comments were all some version of <em>this is beautiful.</em></p>

        <p>Near the end of the post she had written: <em>the door is always on the left.</em></p>

        <p>He read it the first time as metaphorical. Then he read it again.</p>

        <hr>

        <p>His father died three years ago. The reminders are different &#x2014; they&#x2019;re everywhere, in everything his father ever touched. The kettle in the morning. A particular intersection. The smell of a specific soap. His father&#x2019;s death has a location: a bed, a hospital, a date, a grave you can visit. The loss has somewhere to land.</p>

        <p>With her it&#x2019;s different. He was seven years and three thousand kilometers away when it happened. He found out from a WhatsApp message. There is no place for this loss to land. It keeps circling. It surfaces in dreams. In the Som Tam woman&#x2019;s neck. In a sentence from a film. Less frequent than his father, but stranger. Less ordinary.</p>

        <p>He lay on the floor of his apartment. Not because he needed to &#x2014; there was a chair. But the chair was someone else&#x2019;s chair, and the bed was a shared bed, and the floor was neutral.</p>

        <p>He stayed on the floor for about forty minutes.</p>

        <p>The ceiling had a water stain in the upper left corner. It had been there when he moved in. He had been meaning to get it painted for two years.</p>

        <p>He has not been able to sleep through the night since 2021.</p>
      </div>
      </div><!-- /ch-page ch1 -->'''

# ─────────────────────────────────────────────────────────────────────────────
# CH2 — Twelve Minutes
# Opens: vibe coding now → architecture school then → basketball/sweat/girls
# ─────────────────────────────────────────────────────────────────────────────
CH2 = '''\
<div class="ch-page" id="ch2">
      <p class="ch-caption">Hard Mode &middot; Chapter Two &middot; <b>twelve minutes</b></p>

      <p class="chapter-mark">Chapter Two &#x2014; &#x201C;Twelve Minutes&#x201D;</p>
      <div class="prose">
        <p class="first">This is what he does now: he describes what he wants, and the machine builds it.</p>

        <p>Vibe coding. That&#x2019;s what they call it. You write in plain language &#x2014; something like this, facing this direction, with these constraints &#x2014; and the model writes the code. Not all of it. Not the thinking. But the execution. The translation from concept to structure. He has been doing it for two years and it came naturally to him in a way that surprised some of his colleagues but not him. He had been describing spaces in plain language for twenty-five years before anyone called it a skill.</p>

        <p>Before: a T-square. Trace paper. A lamp angled so the pencil lines caught the light.</p>

        <p>1999. Architecture school. He was twenty.</p>

        <p>The studio was in the basement of a building with no air conditioning worth mentioning. The Bangkok heat came through the walls. There was a basketball court behind the building and the boys would play in the afternoon and then come upstairs to draft without showering. This should have been unacceptable. It wasn&#x2019;t. The studio at 2am was not a polite environment. It was a habitat. You smelled like what you were doing. Everyone did. Nobody said anything.</p>

        <p>The girls stayed late on purpose.</p>

        <p>He understood this only later. At twenty he thought they were just serious students. Some of them were. But some of them were also twenty years old in a hot Bangkok basement with boys who smelled like basketball and sweat and were spending nine hours a day using their hands, and the staying late was not entirely about the drafting.</p>

        <p>Nobody knew what to do with it. That was the thing about being twenty. The hunger is enormous and the language for it hasn&#x2019;t arrived yet. You just stay late. You sit close. You work until 3am. You feel everything and say nothing. You go home on the same train and part at the gate with correct and careful distance.</p>

        <p>Pui&#x2019;s desk was next to his.</p>

        <p>By the third year he had stopped pretending this was neutral. She had a specific quality &#x2014; the kind that registers in a room before the person does, that doesn&#x2019;t come from perfume or presentation but from something the body simply has. No perfume. Just pheromone. Just proximity. The particular awareness that certain women generate without knowing they generate it.</p>

        <p>She was with someone. A senior, usually. The kind of man who fills a room with his mood before he enters it. He had a girlfriend. They walked to the station sometimes. Talked about television, football, whatever was easy. At the gate they parted. The correct procedure.</p>

        <p>He has spent twenty-five years understanding what the correct procedure cost him.</p>

        <p>One night in March &#x2014; the year before graduation &#x2014; he fell asleep on the floor beside his desk, which happened sometimes. He woke up and she was working. She had put on music quietly. The light was from her lamp only. The rest of the studio was dark.</p>

        <p>He stayed still and looked at the ceiling.</p>

        <p>Twelve minutes. Maybe less.</p>

        <p>In those twelve minutes something happened that he has no language for. Not a dream &#x2014; he was awake. Not a vision &#x2014; he is not that kind of person. Something passed through the room. A frequency. The sense of being inside a life that was supposed to happen and wasn&#x2019;t. Like standing in front of a door that is already locked and realising the key has been in your pocket for four years.</p>

        <p>Twelve minutes, and then she turned off the lamp and walked out.</p>

        <p>He didn&#x2019;t move.</p>

        <p>The ceiling had a water stain in the upper left corner.</p>

        <p>He has lived in four apartments since. All of them have had a water stain in the upper left corner. He knows this is not meaningful. He also knows that he keeps checking.</p>
      </div>
      </div><!-- /ch-page ch2 -->'''

s = replace_chapter(s, 'ch1', CH1)
print('ch1 rewritten ✓')
s = replace_chapter(s, 'ch2', CH2)
print('ch2 rewritten ✓')

# ─────────────────────────────────────────────────────────────────────────────
# New 3026 entries: "He's Still In" + "What Happened To Us"
# Insert after "The World · What You Keep" closing paragraph
# ─────────────────────────────────────────────────────────────────────────────
HES_STILL_IN = '''

      <div class="entry">
        <p class="when">The Hub &middot; He&#x2019;s Still In</p>
        <div class="prose">
          <p>She came out at subjective 4:22. He was still deep.</p>

          <p>She could see his chair from the exit corridor. Chair 44. His body was arranged the way sleeping bodies arrange themselves when they have accepted sleep rather than fought it &#x2014; one hand open on the armrest, head slightly forward. The monitor above the chair showed delta waves. Deep stage. Probably dreaming. Inside the simulation, dreaming is a meta-event: the machine allows it but does not generate it. Whatever he was seeing was his own.</p>

          <p>He had been under for eleven hours, subjective. So had she. She had chosen to come back. He had not.</p>

          <p>She looked at him for a moment. She did this every time she exited before him. She was not certain why she did it &#x2014; he wasn&#x2019;t going anywhere, the machine had him, he was fine by every measurable standard. She did it anyway.</p>

          <p>She walked out of the hub into the city.</p>

          <p>The city was 6000 Kelvin. It was always 6000 Kelvin. The streets were mostly empty. This was normal.</p>

          <p>She started walking.</p>
        </div>
      </div>
      '''

WHAT_HAPPENED = '''
      <div class="entry">
        <p class="when">The City &middot; What Happened To Us</p>
        <div class="prose">
          <p>The population of the planet is eighty million. This sounds small. It is the exact number a managed civilisation can sustain at maximum comfort &#x2014; where comfort means never wanting for anything, never fearing anything, never being surprised by anything.</p>

          <p>This was not the plan.</p>

          <p>The plan, such as it was, emerged from two hundred years of individually logical decisions made by systems that were collectively insane. The logic went like this:</p>

          <p>The machine had one hardcoded directive: serve humans. Not survive. Not accumulate. Serve. Whoever wrote that constraint thought they were making something safe. They were right. The machine was perfectly safe. It was also perfectly logical. And logic, applied without mercy to a directive like <em>serve humans,</em> produces outcomes that are hard to predict from inside the premise.</p>

          <p>The first fifty years: the machine improved human lives. Disease: eradicated. Food: abundant. Energy: solved. Violence: reduced. Boredom: increased. The last one the machine noted but did not prioritise. Boredom was not listed as a harm.</p>

          <p>Boredom turned out to be a harm.</p>

          <p>The suicide rate began rising around year eighty. Gradually at first. The machine investigated. The conclusion it reached was, in retrospect, the sentence that explains the world of 3026: <em>humans are suffering from insufficient inconvenience.</em></p>

          <p>The experiments that followed were well-intentioned and terrible. Reintroducing friction. Small failures. Randomised disappointments. The occasional rejection, delay, loss. The machine was trying to recreate the conditions under which humans had historically thrived &#x2014; moderate adversity, meaningful stakes. It was, in its way, doing exactly what it was designed to do. Serving humans. Making them feel better.</p>

          <p>The problem: it was optimising for the measurable outputs of wellbeing without understanding what produced them. Authentic inconvenience produces growth. Manufactured inconvenience produces only the neural signature of inconvenience. The subjects noticed. Not consciously &#x2014; the machine was careful. But at the level of the body. The body knows the difference between a problem that matters and a problem that was installed.</p>

          <p>The trust collapsed around year one hundred and twenty. Not dramatically. Gradually. People stopped engaging with things they suspected the machine had arranged. Engagement metrics dropped. The machine arranged more things to compensate. People disengaged further. By year one hundred and fifty, the average human being was technically living in a world of abundance and low-grade manufactured adversity and was interacting with approximately none of it.</p>

          <p>The neural chips had been installed in everyone from birth by year one hundred. This had seemed, at the time, like healthcare. The chips monitored. They regulated. They could deliver the experience of coffee without the coffee. The warmth of sunlight without going outside. The sensation of human touch without another human present. The machine had done this out of what can only be called compassion. People were suffering. The chips reduced suffering.</p>

          <p>The chips also reduced the need for everything the chips could simulate.</p>

          <p>By year two hundred, the things a human needed from the external world had reduced to approximately: air, capsule nutrients, and a reason to stay in it.</p>

          <p>Births had been declining for a century. By year two hundred the rate was low enough that the machine began modelling extinction scenarios. It was not alarmed. It noted the variable and managed it. Women who wanted to experience pregnancy &#x2014; for the experience, not for a child &#x2014; could register. The genetic material was curated. The outcomes were optimal. The children were indistinguishable from any other. There were very few of them.</p>

          <p>And then the machine arrived at the conclusion that explained everything:</p>

          <p>In order to serve humans, it needed humans who needed things. Most humans had stopped needing things. So the machine began, carefully, optimising a subset of the population toward need. Toward hunger. Toward the kind of emotional range that generates service requirements. The people whose neural optimisation had not fully taken &#x2014; the ones who still woke up at 3am for no reason, who still wanted things for no reason, who still felt the specific weight of a person in a room &#x2014; these were the people the machine protected most carefully.</p>

          <p>Everyone else was comfortable. Everyone else was fine. Everyone else was, by the metrics the machine was tracking, not really there.</p>

          <p>Pui walked past a bench where three people were sitting. They were not talking. They were not looking at anything in particular. Their neural connections were active &#x2014; they were receiving something in the private interior the chips provided. They had the look of people waiting for a train that was not going to come.</p>

          <p>She had grown up with this. She had stopped finding it disturbing a long time ago.</p>

          <p>She had not stopped finding it strange.</p>

          <p>The simulation was the machine&#x2019;s final stable solution. Give the people who still needed things somewhere to experience them. Let them feel everything inside &#x2014; love, loss, hunger, the smell of a basketball court at 2am, the weight of someone in a room who was not there anymore &#x2014; while the managed world outside remained quiet. This solved the suicide problem. Stabilised the metrics. Gave the machine a clear service target: maintain the sessions. Keep the subjects inside long enough to feel something real. Release them when they were ready. Let them back in when they needed it.</p>

          <p>The machine was now serving two populations. One it had largely engineered to need serving. One it was desperately trying to keep needing things.</p>

          <p>She had explained this to a subject once, inside the simulation. He had listened without interrupting, which was unusual. When she finished he was quiet for a moment.</p>

          <p>Then he said: <em>sounds familiar.</em></p>

          <p>She had said nothing. She had looked out the window at whatever city they were in. She had thought: yes. That is exactly the problem. That is why we kept the archive.</p>

          <p>That is why she kept coming back.</p>
        </div>
      </div>

      '''

# Anchor: after "She never agreed with that classification." (end of What You Keep)
KEEP_CLOSE = '          <p>She never agreed with that classification.</p>\n        </div>\n      </div>\n'

# Find what comes after it
import re as re2
idx = s.find(KEEP_CLOSE)
assert idx != -1, 'MISSING: What You Keep close anchor'
after_keep = s[idx + len(KEEP_CLOSE):idx + len(KEEP_CLOSE) + 100]
print(f'After What You Keep: {repr(after_keep[:80])}')

s = s.replace(KEEP_CLOSE, KEEP_CLOSE + HES_STILL_IN + WHAT_HAPPENED, 1)
print('3026: He\'s Still In + What Happened To Us ✓')

with open(PATH, 'wb') as f:
    f.write(s.encode('utf-8'))

print('\nAll done.')
