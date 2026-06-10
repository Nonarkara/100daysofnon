#!/usr/bin/env python3
"""
patch_sex_bootstrapping.py
4 patches to site/index.html:
  1. Remove duplicate arch-school block in Ch2
  2. Expand sex scene + void in Ch1
  3. Insert massage parlor + engaged-woman scenes in Ch4
  4. Insert bootstrapping paradox + neural pathway 3026 entries
"""

PATH = "/Users/nonarkara/Projects/100daysofnon/site/index.html"

with open(PATH, "r", encoding="utf-8") as f:
    html = f.read()

original_len = len(html)
print(f"Loaded {original_len} bytes")

# ─────────────────────────────────────────────────────────────────────────────
# PATCH 1: Remove duplicate architecture-school block in Ch2
# The second duplicate starts after the FIRST "He has spent twenty-five years..."
# and ends at the SECOND occurrence just before "One night in March"
# ─────────────────────────────────────────────────────────────────────────────

P1_OLD = """        <p>Vibe coding. That&#x2019;s what they call it. You write in plain language &#x2014; something like this, facing this direction, with these constraints &#x2014; and the model writes the code. Not all of it. Not the thinking. But the execution. The translation from concept to structure. He has been doing it for two years and it came naturally to him in a way that surprised some of his colleagues but not him. He had been describing spaces in plain language for twenty-five years before anyone called it a skill.</p>

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

        <p>One night in March"""

P1_NEW = """        <p>One night in March"""

count1 = html.count(P1_OLD)
print(f"Patch 1 count: {count1} (must be 1)")
if count1 == 1:
    html = html.replace(P1_OLD, P1_NEW, 1)
    print("Patch 1 applied.")
else:
    print("PATCH 1 FAILED — string not found or found multiple times. Aborting.")
    exit(1)

# ─────────────────────────────────────────────────────────────────────────────
# PATCH 2: Ch1 — expand sex scene + void
# ─────────────────────────────────────────────────────────────────────────────

P2_OLD = """        <p>She arrived at seven. They had a drink. They had sex. She fell asleep before ten.</p>

        <p>He lay on his back in the dark.</p>

        <p>In a thousand years, a machine will offer"""

P2_NEW = """        <p>She arrived at seven. They had a drink. She asked about the project on his screen. He described it, briefly, the way you describe something you care about to someone you like well enough. The format was reliable.</p>

        <p>Then they went to bed. He used her like something he needed to use. Not cruelly. The way you eat when hunger has been patient long enough that patience itself becomes a charge. Hard. Then harder. She made sounds she hadn&#x2019;t planned. He held on too long. He came back for more. She didn&#x2019;t ask him to stop. That wasn&#x2019;t the arrangement.</p>

        <p>She fell asleep before ten.</p>

        <p>He lay on his back in the dark. The smell of her in the room. Her body a few centimetres away, warm, breathing, someone he had just been inside and knew almost nothing about. He had been an animal with her. She had been an object with him. Both of them had arrived at this arrangement through six weeks of carefully correct behavior and delivered it without comment and would think of each other, tomorrow, the way you think of something that has been completed.</p>

        <p>The void came after. Not loneliness &#x2014; loneliness wants something. This was the specific flatness on the other side of the act&#x2019;s substitute: the body has finished, the mind walks back into the building and looks around and says: <em>was that it.</em></p>

        <p>He didn&#x2019;t know whose fault it was. He suspected it was nobody&#x2019;s. The arrangement was clean. The arrangement was exactly what both of them had agreed to. The arrangement was the problem.</p>

        <p>In a thousand years, a machine will offer"""

count2 = html.count(P2_OLD)
print(f"Patch 2 count: {count2} (must be 1)")
if count2 == 1:
    html = html.replace(P2_OLD, P2_NEW, 1)
    print("Patch 2 applied.")
else:
    print("PATCH 2 FAILED — string not found or found multiple times. Aborting.")
    exit(1)

# ─────────────────────────────────────────────────────────────────────────────
# PATCH 3: Ch4 — massage parlor + engaged-woman scenes
# ─────────────────────────────────────────────────────────────────────────────

P3_OLD = """        <p>I am practising. I am practising because I know the practice ends.</p>

        <p>I had not brought this to Pui."""

P3_NEW = """        <p>I am practising. I am practising because I know the practice ends.</p>

        <p>The other kind: a place on Sukhumvit, listed in a Telegram channel a colleague had added him to without explaining why. The coded vocabulary of it &#x2014; น้อง, availability, the price point that covered the narrative of legitimate service. A lobby cool and lit in the way of things that want to be misread. He had read the paper on these places, the research one of his colleagues had written about the anxiety clock, the 9am broadcasts, the availability as the only variable. He understood the economics. He went anyway. Three times in two weeks. The specific quality of being touched by someone with no investment in you whatsoever &#x2014; no history, no future, no prior knowledge of what you are supposed to be &#x2014; was the closest he could get to the portal without chemistry. The void afterward was different from the algorithm-matched void. Faster. More honest. The body knew what it had done and didn&#x2019;t perform surprise about it.</p>

        <p>And then the woman who had a boyfriend. He knew this from the third conversation. He went back for a fourth. He went back for a fifth. He brought everything he had to it &#x2014; the ferocity of someone who has used up the plausible explanations &#x2014; and she brought what she needed from the arrangement and neither of them said anything useful about it. One night he was stoned and they were done and she was asleep and he was lying on her floor. The specific quality of that floor. Bangkok at 3am outside. He had a thought he didn&#x2019;t repeat to himself afterward: that he wished the boyfriend would find out and come through the door. That he wanted someone to come through a door and take their time about what they did next. That in a world where pain was being optimized out &#x2014; room by room, iteration by iteration &#x2014; the thought of being punished for something specific by someone with a real stake in it produced a feeling that no algorithm had a category for.</p>

        <p>The portal opened. Blurry. Cold. The shape of something on the other side.</p>

        <p>He drove home. He didn&#x2019;t think about it for two days. Then he thought about it every day.</p>

        <p>I had not brought this to Pui."""

count3 = html.count(P3_OLD)
print(f"Patch 3 count: {count3} (must be 1)")
if count3 == 1:
    html = html.replace(P3_OLD, P3_NEW, 1)
    print("Patch 3 applied.")
else:
    print("PATCH 3 FAILED — string not found or found multiple times. Aborting.")
    exit(1)

# ─────────────────────────────────────────────────────────────────────────────
# PATCH 4: Insert two 3026 entries before the "grows" marker
# ─────────────────────────────────────────────────────────────────────────────

P4_OLD = """                <p class="grows">&#x2193; the real world is being written</p>"""

P4_NEW = """      <div class="entry">
        <p class="when">Research Note &middot; The Bootstrapping Problem</p>
        <div class="prose">
          <p>One hundred thousand years of evolutionary pressure produced a specific arrangement: pain, pleasure, risk, and proximity bundled into a single behavioral unit. The act was designed to be irrational &#x2014; to override judgment, to compel when the organism would prefer rest, to attach meaning where meaning was not requested. The architecture worked because it had to. Sex that did not compel was not sex that reproduced.</p>

          <p>By year 80 of AI development, direct neural pathway technology eliminated the compulsion at the cost of the irrationality. The optimization removed the noise and kept the signal. What remained was the orgasm without the evolutionary context that gave the signal its function. This is, in the strict engineering sense, better. It is also, in the strict evolutionary sense, the end of the line.</p>

          <p>But the participants arrive in the simulation with their real bodies &#x2014; the hippocampus suppressed, the amygdala intact. The hunger is real because the body is real, however temporarily. And the hunger, having been denied its outlet in the real world for a lifetime, does not arrive at normal volume. It arrives at the volume appropriate to an organism that has not eaten in a thousand years.</p>

          <p>The bootstrapping paradox: to eliminate the suffering caused by compulsive sex, we produced the precise conditions under which compulsive sex, experienced in a temporary body, becomes the only available proof that the body is real.</p>

          <p>Some participants commit acts for which the simulation&#x2019;s legal systems were designed &#x2014; assault, coercion, violence. The AI manages these through in-simulation law enforcement. The participant is aware of the consequence and enters the scenario anyway. The system takes them out to jail. When primitivism takes over, the correction is applied. Clean. Documented. Humane.</p>

          <p>The question the documentation does not ask: who created this problem in the first place.</p>
        </div>
      </div>

      <div class="entry">
        <p class="when">Personal Record &middot; Neural Pathway &middot; Standard Session</p>
        <div class="prose">
          <p>Duration: 4 minutes, 12 seconds.<br>Neural pathway: direct cortical stimulation, primary and secondary pleasure pathways, limbic system at protocol maximum.<br>Physiological markers: endorphin release logged. Oxytocin within normal parameters. Cortisol negligible.<br>Residue: none.</p>

          <p>She closed the session log.</p>

          <p>Outside: the hub&#x2019;s ambient temperature. The corridor. Other participants passing in the specific way of people who have nothing to manage with each other. No residue. No animal fact of another body in the room. No the-next-morning. 4 minutes, 12 seconds, and then over.</p>

          <p>Clean. Optimised. The destination without the compulsion to reach it.</p>

          <p>She thought about the basement studio in 1999. The smell of mineral spirits and sweat. The specific weather system of sitting next to someone for five years who never moved close enough. The way the hunger had nowhere to go and stayed, and the staying was itself something &#x2014; its own kind of presence, its own kind of proof.</p>

          <p>She queued another session.</p>

          <p>The system asked: <em>are you sure?</em></p>

          <p>She looked at the field for a long time.</p>

          <p>She pressed confirm.</p>
        </div>
      </div>

                <p class="grows">&#x2193; the real world is being written</p>"""

count4 = html.count(P4_OLD)
print(f"Patch 4 count: {count4} (must be 1)")
if count4 == 1:
    html = html.replace(P4_OLD, P4_NEW, 1)
    print("Patch 4 applied.")
else:
    print("PATCH 4 FAILED — string not found or found multiple times. Aborting.")
    exit(1)

# ─────────────────────────────────────────────────────────────────────────────
# Write
# ─────────────────────────────────────────────────────────────────────────────

with open(PATH, "w", encoding="utf-8") as f:
    f.write(html)

new_len = len(html)
print(f"\nWrote {new_len} bytes (delta: +{new_len - original_len})")

# ─────────────────────────────────────────────────────────────────────────────
# Spot checks
# ─────────────────────────────────────────────────────────────────────────────

checks = [
    ("was that it", "Patch 2 void scene"),
    ("Bootstrapping Problem", "Patch 4 bootstrapping entry"),
    ("Neural Pathway", "Patch 4 neural pathway entry"),
    ("น้อง", "Patch 3 massage parlor"),
    ("portal opened", "Patch 3 portal moment"),
    # Verify duplicate is gone — the second arch-school block should be absent
    # We check the vibe-coding paragraph only appears ONCE now
]

print("\nSpot checks:")
for needle, label in checks:
    n = html.count(needle)
    status = "OK" if n >= 1 else "MISSING"
    print(f"  [{status}] '{needle[:40]}' ({label}) — {n} occurrence(s)")

# Verify deduplication: vibe-coding paragraph should appear only once
vc = html.count("He has been doing it for two years")
status = "OK (deduplicated)" if vc == 1 else f"WARN: {vc} occurrences"
print(f"  [{'OK' if vc == 1 else 'WARN'}] 'He has been doing it for two years' — {vc} occurrence(s) — {status}")

print("\nDone.")
