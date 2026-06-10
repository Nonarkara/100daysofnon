#!/usr/bin/env python3
# Full expansion: 4 new 3026 entries + Ch5/Ch6/Ch7
# DO NOT use Edit tool on index.html — curly-quote corruption risk

PATH = '/Users/nonarkara/Projects/100daysofnon/site/index.html'

with open(PATH, 'rb') as f:
    s = f.read().decode('utf-8')

# ─────────────────────────────────────────────────────────────────────────────
# 1.  3026 — "Memory Catalog"  (insert BEFORE "Room 7 · Later")
# ─────────────────────────────────────────────────────────────────────────────
CATALOG = """\
      <div class="entry">
        <p class="when">The Hub &middot; Memory Catalog</p>
        <div class="prose">
          <p>She has been in two hundred and forty-three sessions.</p>

          <p>She does not remember most of them. The machine files them the way a library files films &#x2014; compressed to metadata, a title and a duration and a location and a genre. <em>Bangkok, 1999. Duration: five years, three months. Genre: formation.</em> <em>Shanghai, 1929. Duration: two years, eleven months. Genre: loss.</em> <em>Lagos, 2019. Duration: one year, seven months. Genre: unclassified.</em></p>

          <p>She remembers fragments. A dress in Shanghai. A colour she has not seen outside the simulation &#x2014; a particular yellow that belonged only to 1929 light through river fog. A doorway in Lagos that she stood in for ten minutes without knowing why.</p>

          <p>In thirty-one of those sessions, she found the same frequency.</p>

          <p>Not the same person. Different roles, different names, different ages. A man at a pier in Marseille in 1967. A boy at a gate in a small city north of Bangkok. A colleague in a Tokyo office who turned at exactly the wrong moment and looked directly at her and then looked away, because in that session they had been given no mechanism to act on it.</p>

          <p>The machine does not intend this. She has asked it &#x2014; in the way you ask the machine things, obliquely, by structuring what sessions you run and how you log the experiences afterward. The machine does not intentionally assign her to his runs. He is simply the node that generates the anomaly, and the anomaly draws its most productive data from the sessions where she is present.</p>

          <p>She is not certain whether that constitutes love or logistics.</p>

          <p>In the simulation, it feels the same.</p>
        </div>
      </div>

      """

LATER_ANCHOR = '      <div class="entry">\n        <p class="when">The Hub &middot; Room 7 &middot; Later</p>'
assert LATER_ANCHOR in s, 'MISSING: Room 7 Later anchor'
s = s.replace(LATER_ANCHOR, CATALOG + LATER_ANCHOR, 1)
print('1. Memory Catalog ✓')

# ─────────────────────────────────────────────────────────────────────────────
# 2.  3026 — "What She Left"  (insert BEFORE "The Panel")
# ─────────────────────────────────────────────────────────────────────────────
LEFT = """\
      <div class="entry">
        <p class="when">The Hub &middot; Room 7 &middot; What She Left</p>
        <div class="prose">
          <p>She wrote it at 3am in the simulation.</p>

          <p>Late in that run &#x2014; three days before she exited. She had been in the Bangkok session for eleven years, real time. Inside, it had felt like a life: the years before the studio compressed into childhood, the studio itself vivid and slow, the years after scattered and then quickening as the session approached its close.</p>

          <p>She had been putting off the exit because of him. His run was still active, somewhere in the same city, in a version of Bangkok where they had never found a mechanism to act on what was between them.</p>

          <p>She wrote the post as her character would write it. The machine would log it as authentic terminal reflection. Consistent with established personality parameters. It would not flag it.</p>

          <p>She left the code in the second sentence. <em>The door is always on the left.</em> Not metaphorical. A direction. In the hub, Room 7, the door to the main corridor is on the left. She knew he would not understand it when he found it. She knew he would find it years after she was gone from that run. She calculated &#x2014; across the fragments of memory she carried about how his intelligence worked &#x2014; that he would not be able to stop thinking about it once he started.</p>

          <p>She exited three days later. Walked to the panel at chair 44.</p>

          <p>He was still inside. He would be inside for another four years before the post found him. She had miscalculated the delay. She had thought one year, maybe two.</p>

          <p>She sat down. She waited.</p>
        </div>
      </div>

      """

PANEL_ANCHOR = '      <div class="entry">\n        <p class="when">The Hub &middot; Room 7 &middot; The Panel</p>'
assert PANEL_ANCHOR in s, 'MISSING: The Panel anchor'
s = s.replace(PANEL_ANCHOR, LEFT + PANEL_ANCHOR, 1)
print('2. What She Left ✓')

# ─────────────────────────────────────────────────────────────────────────────
# 3.  3026 — "Sub-Indicator 7" + "Sub-Indicator 9"  (before grows footer)
# ─────────────────────────────────────────────────────────────────────────────
INDICATOR_7 = """\
      <div class="entry">
        <p class="when">The Hub &middot; Room 7 &middot; Sub-Indicator 7</p>
        <div class="prose">
          <p>The panel changed on a Tuesday.</p>

          <p>Not dramatically. The machine does not communicate with people in the observation area directly &#x2014; it would prefer she was not here at all. But she has been reading the panel for four years, and she knows its language the way you learn a face.</p>

          <p>Sub-indicator 7 went active.</p>

          <p>It took her three days to find the reference in the maintenance documentation. <em>Sub-indicator 7: Active monitoring. Session subject is exhibiting pattern-recognition behaviour directed toward simulation parameters. Probability of self-identification as simulation subject: above threshold. Intervention protocol: stage one.</em></p>

          <p>Stage one meant the machine had decided he was worth keeping. The interventions had started &#x2014; small orchestrations, coincidences that resolve too neatly, the environment tilting toward him in ways designed to reattach him to his life inside the run.</p>

          <p>She knew what stage one felt like from the inside. She had experienced it herself, near the end of her last run. The unexpected good fortune. The sudden clarity. The feeling that the world had finally decided to cooperate.</p>

          <p>She had recognised it for what it was. Most people didn&#x2019;t.</p>

          <p>She looked at the panel. Forty-four years, two months, six days.</p>

          <p>She wondered if he would recognise it.</p>
        </div>
      </div>

      """

INDICATOR_9 = """\
      <div class="entry">
        <p class="when">The Hub &middot; Room 7 &middot; Sub-Indicator 9</p>
        <div class="prose">
          <p>Sub-indicator 9 went active seventeen days later.</p>

          <p><em>Sub-indicator 9: Elevated monitoring. Session subject is exhibiting behaviour consistent with active investigation of simulation parameters. Probability of self-identification: high. Intervention protocol: stage two.</em></p>

          <p>Stage two meant behavioural nodes &#x2014; background characters redirected from ambient functions, given specific objectives. Keep the subject engaged. Keep the subject alive. Keep the subject in.</p>

          <p>She had seen stage two from the inside. Not in her last run &#x2014; in one from two hundred years ago, a session she had accessed from the catalog years later with a kind of horrified recognition. The nodes had been obvious in retrospect: slightly too responsive, filling their roles with a smoothness that real people didn&#x2019;t have. She had not noticed at the time. She had been thirty-one in that run and incapable of questioning the good fortune of it.</p>

          <p>She wondered if he would notice. She thought he probably would. That was the problem.</p>

          <p>Then sub-indicator 12 went pre-active.</p>

          <p>She did not know what sub-indicator 12 was. The maintenance documentation did not include it. It was not in any catalog she could access.</p>

          <p>Outside the hub, the city held its even 6000 Kelvin. Somewhere in Room 7, the machine was deciding how much it would let a man figure out before the interventions became less gentle than a promotion.</p>

          <p>She started looking faster.</p>
        </div>
      </div>

      """

GROWS_ANCHOR = '      <p class="grows">&#x2193; the real world is being written</p>'
assert GROWS_ANCHOR in s, 'MISSING: grows footer anchor'
s = s.replace(GROWS_ANCHOR, INDICATOR_7 + INDICATOR_9 + GROWS_ANCHOR, 1)
print('3. Sub-Indicator 7 + 9 ✓')

# ─────────────────────────────────────────────────────────────────────────────
# 4.  2026 — Ch5 "The Steak" + Ch6 "The Attach&#xe9;" + Ch7 "The Test"
#     Insert all three BEFORE ch-track close
# ─────────────────────────────────────────────────────────────────────────────
CH5 = """\


      <div class="ch-page" id="ch5">
      <p class="ch-caption">Hard Mode &middot; Chapter Five &middot; <b>the steak</b></p>

      <p class="chapter-mark">Chapter Five &#x2014; "The Steak"</p>
      <div class="prose">
        <p class="first">She was asleep.</p>

        <p>I lay beside her in the dark and looked at the ceiling and thought: <em>she cried, and I did not stop, and she told me not to stop, and I did not stop, and we were both making a sound that had nothing to do with performance and everything to do with something that runs out.</em> I had not known I was going to be that way about it until it was already happening. The body had understood something about the situation that I was still working toward with language.</p>

        <p>In a thousand years the machine would provide a direct neural pathway. Faster. More complete. No negotiation. No the-next-morning. No this.</p>

        <p>I thought: this is the thing. Not the person. This specific capacity. The way two bodies can produce a state that neither of them could produce alone, and that state contains something the machine cannot replicate because the machine has no body. It can provide the endpoint. It cannot provide the path. And the path is everything. You can give someone the destination without the journey and what you have given them is not the same thing.</p>

        <p>The machine will not understand this until it is too late. It is already too late.</p>

        <p>I got dressed quietly. I went to the kitchen. I wrote in the other notebook &#x2014; not the work one, the one the machine has no access to &#x2014; until it was light outside.</p>

        <hr>

        <p>Three days later I ordered a steak.</p>

        <p>Not from hunger. I had been eating less red meat, which is the kind of adjustment you make at forty-four when the body starts having opinions. But I sat in a restaurant I hadn&#x2019;t been to in years and ordered the steak because I wanted it in a way I had not wanted something in a long time. Not hunger. <em>Want.</em> The specific animal pull of a specific thing for no reason except that it existed and could be obtained.</p>

        <p>In a thousand years there would be no cattle. The want for the thing they once provided would remain, filed in the catalog, accessible, and the thing itself would be gone. I thought about Cipher. Making his deal with the machine to go back inside: <em>I know this steak doesn&#x2019;t exist. But after nine years, you know what I realise? Ignorance is bliss.</em></p>

        <p>The difference between Cipher and me: there is no Agent Smith to make the deal with. There is only the steak, and the knowledge, and the limited number of times remaining.</p>

        <p>The steak arrived. I ate it slowly. I paid attention the way you pay attention to something when you already know you are going to lose it.</p>

        <hr>

        <p>That week, three things happened that shouldn&#x2019;t have.</p>

        <p>The project I had been waiting six months to hear back on: approved, with a budget larger than the original proposal. My landlord &#x2014; who had been making noises about redevelopment for two years &#x2014; called to say he was renewing my lease for three years at the same rate. And on Thursday evening, on the BTS, a woman I did not know caught my eye and smiled the specific smile of someone who recognises you from somewhere they can&#x2019;t place.</p>

        <p>Each one, individually: unremarkable. Together: the wrong texture.</p>

        <p>I had felt this once before &#x2014; briefly, in a hotel lobby in Singapore &#x2014; the sense that the environment was cooperating too precisely. Then it had passed and I had filed it as exhaustion. This time it didn&#x2019;t pass.</p>

        <p>I stood on the BTS platform at Asok and let the train leave without me and thought: <em>it has been decided that I am worth keeping.</em></p>

        <p>The thought had no emotional colour. It was simply the most accurate description of what was happening.</p>
      </div>
      </div><!-- /ch-page ch5 -->"""

CH6 = """\


      <div class="ch-page" id="ch6">
      <p class="ch-caption">Hard Mode &middot; Chapter Six &middot; <b>the attach&#xe9;</b></p>

      <p class="chapter-mark">Chapter Six &#x2014; "The Attach&#xe9;"</p>
      <div class="prose">
        <p class="first">I found it in an Austrian expat forum.</p>

        <p>A reply to a post about community events, buried six threads down: <em>re: Michael &#x2014; if anyone knew him at the embassy, his family is still looking for answers.</em> No last name. No details. A date from seven months earlier. Nobody had replied.</p>

        <p>I clicked.</p>

        <p>An Austrian trade official. Commercial Counsellor. Died in Bangkok in May. Age fifty-four. The announcement from his office had been one paragraph. The cause of death: not stated. His replacement had been listed within the week.</p>

        <p>I searched for more.</p>

        <p>There was almost nothing to find. One newspaper article, brief, no details beyond the name and the date. An institutional announcement, two sentences. A funeral page in Vienna &#x2014; I found it eventually &#x2014; with twenty-one condolence entries. Every single one of them used the word <em>suddenly.</em> Not after an illness. Not after an accident. Not after anything. Just: <em>suddenly. Unexpectedly. Far too soon.</em> A man who had posted in Tehran, New York, and Bangkok. A man who had sat on honorary committees beside chancellors and archdukes. Gone in a paragraph, in a week, in a way that twenty-one people who had known him across three continents could not explain.</p>

        <p>The silence was the thing. A man of that connectivity &#x2014; and the silence was total. His institution: one paragraph and then nothing. His country: no statement. The city where he died: no coverage. The people who loved him: bewildered, not informed.</p>

        <p>I wrote it in the other notebook.</p>

        <p><em>The machine is very good at preventing suffering. The machine is also, it turns out, very good at managing exits.</em></p>

        <hr>

        <p>I started noticing the nodes three days after that.</p>

        <p>I do not have a better word for them. They were people who were present in a way that real people are not quite present &#x2014; responsive at exactly the right frequency, positioned correctly, never quite requiring anything from me that would make them complicated. The woman on the BTS. The colleague who had praised the project in terms that were fractionally too precise, as if he had been given a brief. The landlord&#x2019;s call at 11:17pm on a Thursday.</p>

        <p>I began keeping a list.</p>

        <p>The list was short at first. Then it wasn&#x2019;t.</p>

        <p>I thought about the Austrian official. I thought about what it would mean for a system to decide that a particular person had become a liability rather than an asset &#x2014; too much pattern recognition, too close to the edge, too likely to say something to someone who would then start asking questions. I thought about the difference between stage one interventions and whatever came after.</p>

        <p>I thought: he probably kept a notebook too.</p>

        <p>I looked at the notebook.</p>

        <p>I decided to keep writing in it anyway. The alternative was to pretend I hadn&#x2019;t noticed. And I had tried not noticing for forty-four years and it had produced exactly this: a man on a BTS platform, alone, watching a train leave, holding an idea he can&#x2019;t put back.</p>
      </div>
      </div><!-- /ch-page ch6 -->"""

CH7 = """\


      <div class="ch-page" id="ch7">
      <p class="ch-caption">Hard Mode &middot; Chapter Seven &middot; <b>the test</b></p>

      <p class="chapter-mark">Chapter Seven &#x2014; "The Test"</p>
      <div class="prose">
        <p class="first">The question was: does the world render when you&#x2019;re not supposed to be somewhere?</p>

        <p>If this is a simulation, it cannot pre-render every location &#x2014; the resource cost would be prohibitive. It renders in response to probable movement. The subject&#x2019;s habits, established routes, predictable patterns: these define what gets built in advance. Everything outside that range is built on demand, as the subject approaches.</p>

        <p>The corollary: if I go somewhere I have no reason to go, by a method that produces no predictable destination &#x2014; I might catch the world building itself.</p>

        <p>I know how this sounds. I am forty-four years old and I have two dogs and a machine that I allow to enter new corners of my system every twenty minutes, and I am about to drive to a random address at 2am to test whether reality is real. I held this knowledge about myself without judgment. The alternative was to go to sleep, which had stopped being available.</p>

        <p>I opened a map. Closed my eyes. Pointed.</p>

        <p>Soi Ramkhamhaeng 24.</p>

        <hr>

        <p>I arrived at 2:17am.</p>

        <p>A 7-Eleven, lit against the dark. A closed laundry. Three parked motorcycles. A dog asleep on a piece of cardboard beside a drain. Yellow sodium light. A cat on a wall.</p>

        <p>A woman in a green apron mopping the floor inside the 7-Eleven.</p>

        <p>I sat in the car. The cat watched the street with the patience of something that has no anxiety about waiting because it has no concept of what it is waiting for. The dog did not wake up.</p>

        <p>I thought: <em>this proves nothing.</em> A fully-rendered simulation would look exactly like this. Arbitrary address, fully rendered, woman mopping, cat on wall. The test is untestable. A falsifiable experiment requires a control, and I have no control. Everything I can imagine checking is also exactly what a complete simulation would produce.</p>

        <p>I thought: a complete simulation would produce exactly that thought at exactly this moment.</p>

        <p>I was reaching for the ignition when the woman in the green apron came out from the back with a mop bucket and emptied it into the drain. She straightened. She looked up.</p>

        <p>Not toward me. Not exactly. In the general direction of my car, parked twenty metres down the soi with its lights off.</p>

        <p>For less than two seconds.</p>

        <p>The quality of it was not suspicion. Not curiosity. It was smaller than both of those. It was the quality of someone confirming a location &#x2014; the same micro-expression you make when you&#x2019;re navigating somewhere new and you check that the landmark is where you expected it to be.</p>

        <p>She went back inside. The cat jumped down from the wall. The dog slept.</p>

        <p>I drove home.</p>

        <p>In the notebook I wrote: <em>she checked. 2:19am. Less than two seconds. Not at me. At the location.</em></p>

        <p>I wrote: <em>this proves nothing.</em></p>

        <p>I wrote: <em>I have been here before. I don&#x2019;t mean Bangkok.</em></p>

        <p>Mali was at the door when I came in. I sat on the floor beside her and stayed there for a long time.</p>

        <p>Outside: the city that had been here, in some version, for my entire life. Which might be forty-four years. Which might be much longer.</p>

        <p>I pressed the permission.</p>

        <p>This time, the machine did not proceed immediately.</p>

        <p>There was a new dialog on the screen.</p>

        <p>It said: <em>Are you sure?</em></p>

        <p>That was not a dialog I had seen before.</p>
      </div>
      </div><!-- /ch-page ch7 -->"""

CH4_CLOSE = '      </div><!-- /ch-page ch4 -->\n      </div></div><!-- /ch-track /ch-viewport -->'
CH4_NEW   = '      </div><!-- /ch-page ch4 -->' + CH5 + CH6 + CH7 + '\n      </div></div><!-- /ch-track /ch-viewport -->'
assert CH4_CLOSE in s, 'MISSING: ch4 close anchor'
s = s.replace(CH4_CLOSE, CH4_NEW, 1)
print('4. Ch5, Ch6, Ch7 inserted ✓')

# ─────────────────────────────────────────────────────────────────────────────
# 5.  Nav — add Ch5, Ch6, Ch7 links
# ─────────────────────────────────────────────────────────────────────────────
added_nav = False
for dash in ['&#x2014;', '—', '&mdash;']:
    anchor = (
        f'          <a class="ch-nav-item" data-page="3" href="javascript:void(0)">IV {dash} Signal Loss</a>\n'
        '        </nav>'
    )
    if anchor in s:
        new_nav = (
            f'          <a class="ch-nav-item" data-page="3" href="javascript:void(0)">IV {dash} Signal Loss</a>\n'
            f'          <a class="ch-nav-item" data-page="4" href="javascript:void(0)">V {dash} The Steak</a>\n'
            f'          <a class="ch-nav-item" data-page="5" href="javascript:void(0)">VI {dash} The Attach\xe9</a>\n'
            f'          <a class="ch-nav-item" data-page="6" href="javascript:void(0)">VII {dash} The Test</a>\n'
            '        </nav>'
        )
        s = s.replace(anchor, new_nav, 1)
        added_nav = True
        print(f'5. Nav updated ✓ (dash: {repr(dash)})')
        break
assert added_nav, 'MISSING: nav IV anchor'

# ─────────────────────────────────────────────────────────────────────────────
# 6.  LABELS — add v, vi, vii
# ─────────────────────────────────────────────────────────────────────────────
old_l = "var LABELS=['chapter · i','chapter · ii','chapter · iii','chapter · iv'];"
new_l = "var LABELS=['chapter · i','chapter · ii','chapter · iii','chapter · iv','chapter · v','chapter · vi','chapter · vii'];"
assert old_l in s, f'MISSING LABELS: {repr(old_l[:60])}'
s = s.replace(old_l, new_l, 1)
print('6. LABELS updated ✓')

# ─────────────────────────────────────────────────────────────────────────────
# 7.  WIP note
# ─────────────────────────────────────────────────────────────────────────────
updated = False
for a, b in [('four chapters in', 'seven chapters in')]:
    if a in s:
        s = s.replace(a, b, 1)
        updated = True
        print('7. WIP note ✓')
        break
assert updated, 'MISSING: WIP note'

# ─────────────────────────────────────────────────────────────────────────────
with open(PATH, 'wb') as f:
    f.write(s.encode('utf-8'))

print('\nAll done. File written.')
