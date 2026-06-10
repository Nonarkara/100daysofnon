#!/usr/bin/env python3
# Full novel rewrite — faster voice, KL arc, 4 new 3026 entries
# NEVER use Edit tool on index.html

import re

PATH = '/Users/nonarkara/Projects/100daysofnon/site/index.html'

with open(PATH, 'rb') as f:
    s = f.read().decode('utf-8')

def replace_chapter(text, ch_id, new_content):
    pattern = r'<div class="ch-page" id="' + ch_id + r'">.*?</div><!-- /ch-page ' + ch_id + r' -->'
    result, n = re.subn(pattern, new_content, text, flags=re.DOTALL)
    assert n == 1, f'Pattern not found or duplicated: {ch_id}'
    return result

# ─────────────────────────────────────────────────────────────────────────────
# CH1 — The Noiseless Kind
# ─────────────────────────────────────────────────────────────────────────────
CH1 = '''\
<div class="ch-page" id="ch1">
      <p class="ch-caption">Hard Mode &middot; Chapter One &middot; <b>the noiseless kind</b></p>

      <p class="chapter-mark">Chapter One &#x2014; &#x201C;The Noiseless Kind&#x201D;</p>
      <div class="prose">
        <p class="first">She died in 2018. I didn&#x2019;t find out until 2021.</p>

        <p>This is not unusual. I want to say it is unusual because it should feel unusual. But here is the fact: we had not spoken in seven years. By the time she died, I was not the kind of person who would be notified. You are notified when you are someone&#x2019;s person. I had spent seven years ensuring I was not someone&#x2019;s person.</p>

        <p>A mutual friend told me in a coffee shop. He said it carefully, the way people do when they have been waiting to say something and have rehearsed the delivery. He told me her name first, as if I might not remember who he meant.</p>

        <p>I remembered.</p>

        <p>He told me how. He told me when. He was watching my face while he said it. I knew he was watching my face, so I kept it still. A skill I developed in childhood. I have never found a use for it except in exactly this kind of situation.</p>

        <p>I thanked him. I went home.</p>

        <p>The woman I was with at the time was in the kitchen making something. I sat down on the floor of the bedroom. Not because I needed to sit on the floor &#x2014; there was a chair. But the chair was her chair, and the bed was our bed, and the floor was neutral.</p>

        <p>I sat on the floor for about forty minutes.</p>

        <p>She did not come to check on me. This was characteristic of her and I had always found it a relief. That night I found it the loneliest thing I had ever experienced. Both of these things were true at the same time.</p>

        <p>The ceiling of the bedroom had a small water stain in the upper left corner. It had been there when I moved in. I had been meaning to get it painted for two years.</p>

        <p>I looked at it.</p>

        <p>I have not been able to sleep through the night since.</p>
      </div>
      </div><!-- /ch-page ch1 -->'''

# ─────────────────────────────────────────────────────────────────────────────
# CH2 — Twelve Minutes
# ─────────────────────────────────────────────────────────────────────────────
CH2 = '''\
<div class="ch-page" id="ch2">
      <p class="ch-caption">Hard Mode &middot; Chapter Two &middot; <b>twelve minutes</b></p>

      <p class="chapter-mark">Chapter Two &#x2014; &#x201C;Twelve Minutes&#x201D;</p>
      <div class="prose">
        <p class="first">1999. Architecture school. Bangkok. We were twenty-five.</p>

        <p>The studio stayed open until the work was done, which meant 3 or 4 in the morning most nights. You brought a change of clothes on Monday and by Thursday the studio had become a habitat. People slept under the desks. Three espresso machines, one always broken.</p>

        <p>Pui&#x2019;s desk was next to mine.</p>

        <p>I want to say something careful here: there was a woman in this description and there will be an account of what it felt like to be near her, and I know how that sounds. It was not that kind of story. We were not together. We were never together. We talked about television and football and walked to the same station after. This is not a story about romance. It is a story about what happens when two people are in the same room at 2am for four years and one of them does not say the thing he could have said.</p>

        <p>Her desk was right next to mine. By the third year I had stopped pretending this was neutral.</p>

        <p>She wore a t-shirt and shorts to the studio. Most of us did &#x2014; nobody dresses for the hours. At 2am under drafting lights, the body stops being anything except what it is. The light at that angle makes the room honest. I was aware of her. Not as a plan. Not as a decision. The body makes its own notes before the mind approves the transcript.</p>

        <p>No perfume. Just pheromone. Just proximity. The particular quality that certain women carry without knowing they carry it &#x2014; the kind that registers in the room before they do.</p>

        <p>She was with someone. Usually a senior. The kind of man who fills a room with his mood before he enters it. I had a girlfriend. We walked to the station sometimes. Talked about television, football, whatever. At the gate we parted. The correct procedure.</p>

        <p>I have spent twenty-five years understanding what the correct procedure cost me.</p>

        <p>One night in March &#x2014; the year before graduation &#x2014; I was sleeping on the floor beside my desk, which was normal. I woke up and she was working. She had put on music quietly, something I didn&#x2019;t recognise. The light was from her lamp only. The rest of the studio was dark.</p>

        <p>I stayed still and looked at the ceiling.</p>

        <p>Twelve minutes. Maybe less.</p>

        <p>In those twelve minutes something happened that I have no language for. Not a dream &#x2014; I was awake. Not a vision &#x2014; I am not that kind of person. Something passed through the room. A frequency. The sense of being inside a life that was supposed to happen but wasn&#x2019;t. Like standing in front of a door that is already locked and realising you have had the key in your pocket for four years with your hands in your pockets.</p>

        <p>Twelve minutes and then she turned off the lamp and I heard her walking out.</p>

        <p>I didn&#x2019;t move.</p>

        <p>The ceiling had a water stain in the upper left corner. I have lived in four apartments since. All of them have had a water stain in the upper left corner.</p>

        <p>I know this is not meaningful.</p>

        <p>I also know that I keep checking.</p>
      </div>
      </div><!-- /ch-page ch2 -->'''

# ─────────────────────────────────────────────────────────────────────────────
# CH3 — The Prior
# ─────────────────────────────────────────────────────────────────────────────
CH3 = '''\
<div class="ch-page" id="ch3">
      <p class="ch-caption">Hard Mode &middot; Chapter Three &middot; <b>the prior</b></p>

      <p class="chapter-mark">Chapter Three &#x2014; &#x201C;The Prior&#x201D;</p>
      <div class="prose">
        <p class="first">The dream lasted longer than twelve minutes.</p>

        <p>In the dream it was still the studio. She was there. But she was forty-four, not twenty-five &#x2014; the same age I am now &#x2014; and she knew things she should not know about the current shape of my life. She talked the way people talk when they have been waiting for a long time and have stopped being careful about what they say.</p>

        <p>&#x201C;You came back,&#x201D; she said.</p>

        <p>I didn&#x2019;t know what she meant. I told her I didn&#x2019;t know what she meant.</p>

        <p>&#x201C;You always say that,&#x201D; she said.</p>

        <p>She told me the door was always on the left. Not metaphorically. A direction. Left. She said it twice. She said it the way you tell someone how to find a room in a building they haven&#x2019;t been to yet.</p>

        <p>I asked her where she had been.</p>

        <p>She looked at me the way people look at someone who has asked a question with an obvious answer.</p>

        <p>She told me it had been longer than it felt. She told me she had been sitting at a table for years, subjectively, which was nothing in the other time. She said &#x201C;the other time&#x201D; the way you say &#x201C;the other side of the room&#x201D; &#x2014; matter-of-factly.</p>

        <p>I asked her what table.</p>

        <p>She said: forty-four. The way you say a room number.</p>

        <p>I said: I&#x2019;m forty-four.</p>

        <p>She said: yes.</p>

        <p>I woke up on the floor of the bedroom. The woman I was with at the time was asleep in the bed. I could hear her breathing. The ceiling had the water stain. The city outside was doing whatever the city does at 4am.</p>

        <p>I looked at my phone.</p>

        <p>There was a text message from a number I did not recognise. The message said: <em>the door is always on the left.</em> The timestamp was 4:17am.</p>

        <p>I have checked the number eleven times. It does not exist. No registered account, no carrier record. The phone company confirmed this when I called, which I did once and which felt immediately embarrassing.</p>

        <p>I saved the message.</p>
      </div>
      </div><!-- /ch-page ch3 -->'''

# ─────────────────────────────────────────────────────────────────────────────
# CH4 — Signal Loss
# ─────────────────────────────────────────────────────────────────────────────
CH4 = '''\
<div class="ch-page" id="ch4">
      <p class="ch-caption">Hard Mode &middot; Chapter Four &middot; <b>signal loss</b></p>

      <p class="chapter-mark">Chapter Four &#x2014; &#x201C;Signal Loss&#x201D;</p>
      <div class="prose">
        <p class="first">I tried marijuana first.</p>

        <p>The logic &#x2014; if it was logic &#x2014; was that the conversation had happened in a state between waking and not-waking. Altering the chemistry of that state might widen the gap. Might let something through.</p>

        <p>Three nights. Different quantities. Same result: slow thoughts, appetite, the particular loneliness of being high alone. No gap. No conversation. The ceiling.</p>

        <p>Then alcohol. I understood alcohol better. Alcohol strips things back &#x2014; not to truth, but to the version of yourself that existed before you learned to perform the other versions. I drank on a Tuesday. I drank with a colleague on a Thursday. I woke each morning with the usual residue and the usual absence.</p>

        <p>I was trying to get back to twelve minutes.</p>

        <p>There had been a woman, for two years, who called when she wanted to and didn&#x2019;t call when she didn&#x2019;t want to. The architecture of the arrangement was entirely hers. I arrived when summoned. I was good at what she summoned me for &#x2014; she told me this, with the specific detachment of someone reviewing a service. I loved her in the way you love something that is dismantling you without announcing its intentions. Then one Thursday she stopped calling. Weeks. Then a month. Then two. I understood only after the silence that I had been useful the way a good appliance is useful: reliably, without reciprocity, until it wasn&#x2019;t needed anymore.</p>

        <p>This happened before I understood what the hunger I brought to bed actually was.</p>

        <p>Not ordinary hunger. Something the body knows before the mind has language for it. That there is a version of this capacity that runs out. That whatever the act of wanting a woman carries &#x2014; the weight of it, the not-quite-controllable quality, the specific proof that you are a living thing with a body and a temperature &#x2014; there is a future where that is gone. Not taken. Simply no longer needed. The machine will provide something faster and more complete and without the residue.</p>

        <p>I had never said this to anyone. I&#x2019;m not certain it would have made sense to anyone. But it is why I had always brought to bed the quality that had occasionally frightened people who didn&#x2019;t expect it from someone my size and my manner. That ferocity. The desire to use everything, hold nothing back. As though each time might be practice for something being counted down on a counter I can&#x2019;t see.</p>

        <p>I had not brought this to Pui. We hadn&#x2019;t arrived at the place where it could have been brought. We walked to the station. We talked about television. The correct procedure.</p>

        <p>I thought about the senior. The one who had been with her after the studio. I had met him once, briefly. I formed an opinion and set it aside on the grounds that I had no standing.</p>

        <p>I was setting it down less easily now.</p>

        <p>I poured a second drink.</p>

        <p>Tomorrow I would wake up and exercise and go to work and eat and watch something and sleep. This was the shape of my life at forty-four. Two dogs at the foot of the bed. Everything else was maintenance: maintain the body, maintain the income, maintain the appearance of a man with reasons.</p>

        <p>I was not certain I had reasons.</p>

        <p>I was certain that twelve minutes had given me the first thing in years that felt like one.</p>

        <p>I thought about the car.</p>

        <p>Not seriously. Not yet seriously. More as a premise to examine: if the conversation was real, and the world in it was real, and the woman in it was Pui, then dying in this world might constitute leaving it. A text message from a number that doesn&#x2019;t exist. A direction I haven&#x2019;t been able to stop thinking about.</p>

        <p>I put the car thought down beside the drink.</p>

        <p>Outside, the city in its long 3am exhale. Mali was asleep at the base of the desk. Expo was in the chair.</p>

        <p>I pressed the permission. The machine proceeded.</p>
      </div>
      </div><!-- /ch-page ch4 -->'''

# ─────────────────────────────────────────────────────────────────────────────
# CH5 — The Steak
# ─────────────────────────────────────────────────────────────────────────────
CH5 = '''\
<div class="ch-page" id="ch5">
      <p class="ch-caption">Hard Mode &middot; Chapter Five &middot; <b>the steak</b></p>

      <p class="chapter-mark">Chapter Five &#x2014; &#x201C;The Steak&#x201D;</p>
      <div class="prose">
        <p class="first">She was asleep. I was looking at the ceiling.</p>

        <p>Something had just happened. I was not going to call it lovemaking &#x2014; that word has a sentimentality I don&#x2019;t trust. What had happened was: she had cried. I had not stopped. She told me not to stop and I did not stop and we were both making a sound that had nothing to do with performance and everything to do with something that runs out.</p>

        <p>I hadn&#x2019;t known I was going to be that way about it until I was already being that way about it. The body had understood something about the situation that I was still working toward with language.</p>

        <p>In a thousand years, the machine provides a direct neural pathway. Faster than the act. More complete. No negotiation. No this ceiling. No the-next-morning.</p>

        <p>I thought: this is the thing. Not the person &#x2014; the capacity. The way two bodies produce a state that neither of them can produce alone. The machine cannot replicate this because the machine has no body. It can provide the destination without the journey. And the journey is everything. You can give someone the steak without the animal that was once alive and what you have given them is not the same thing.</p>

        <p>The machine will not understand this until it is too late. It is already too late.</p>

        <p>I got dressed quietly. Went to the kitchen. Wrote in the other notebook &#x2014; not the work one &#x2014; until it was light.</p>

        <hr>

        <p>Three days later I ordered a steak.</p>

        <p>Not from hunger. I had been eating less red meat, the adjustment you make at forty-four when the body starts having opinions. But I sat in a restaurant I hadn&#x2019;t been to in years and ordered it because I wanted it in a way I had not wanted something in a long time. Not hunger. <em>Want.</em> The specific animal pull of a specific thing for no reason except that it existed and could be obtained.</p>

        <p>In a thousand years there would be no cattle. The want would remain, filed somewhere, accessible. The thing itself would be gone. I thought about Cipher. His deal with the machine to go back inside: <em>&#x201C;I know this steak doesn&#x2019;t exist. But after nine years &#x2014; ignorance is bliss.&#x201D;</em></p>

        <p>The difference between Cipher and me: there is no Agent Smith to make the deal with. There is only the steak and the knowledge and the limited number of times remaining.</p>

        <p>The steak arrived. I ate it slowly. I paid the kind of attention you pay to something when you know you&#x2019;re going to lose it.</p>

        <hr>

        <p>That week, three things happened that shouldn&#x2019;t have.</p>

        <p>The project I&#x2019;d been waiting six months on: approved, larger budget than proposed. My landlord &#x2014; who had been making redevelopment noises for two years &#x2014; called to say he was renewing my lease for three years at the same rate. On Thursday, on the BTS, a woman I did not know caught my eye and smiled the specific smile of someone who recognises you from somewhere they can&#x2019;t place.</p>

        <p>Each one, individually: unremarkable.</p>

        <p>Together: the wrong texture.</p>

        <p>I had felt this once before &#x2014; briefly, in a hotel lobby in Singapore &#x2014; the sense that the environment was cooperating too precisely. Then it passed and I filed it as exhaustion. This time it didn&#x2019;t pass.</p>

        <p>I stood on the BTS platform at Asok and let the train leave without me.</p>

        <p>I thought: it has been decided that I am worth keeping.</p>

        <p>The thought had no emotional colour. It was simply the most accurate description of what was happening.</p>
      </div>
      </div><!-- /ch-page ch5 -->'''

# ─────────────────────────────────────────────────────────────────────────────
# CH6 — The Attaché
# ─────────────────────────────────────────────────────────────────────────────
CH6 = '''\
<div class="ch-page" id="ch6">
      <p class="ch-caption">Hard Mode &middot; Chapter Six &middot; <b>the attach&#xe9;</b></p>

      <p class="chapter-mark">Chapter Six &#x2014; &#x201C;The Attach&#xe9;&#x201D;</p>
      <div class="prose">
        <p class="first">I found it in an Austrian expat forum.</p>

        <p>A reply to a community events post, buried six threads down: <em>re: Michael &#x2014; if anyone knew him at the embassy, his family is still looking for answers.</em> No last name. No details. Seven months old. Nobody had replied.</p>

        <p>I clicked.</p>

        <p>Austrian trade official. Commercial Counsellor. Died in Bangkok in May. Age fifty-four. One paragraph from his office. Cause of death: not stated. Replacement listed within the week.</p>

        <p>I searched for more. Almost nothing. One newspaper article. An institutional announcement. A funeral page in Vienna &#x2014; twenty-one condolence entries. Every single one used the word <em>suddenly.</em> Not after an illness. Not after an accident. Just: suddenly. Unexpectedly. Far too soon. A man who had sat on honorary committees beside chancellors and archdukes. People who had known him across three continents, all of them bewildered, none of them informed.</p>

        <p>The silence was the thing. That level of connectivity &#x2014; and total silence.</p>

        <p>I wrote in the other notebook: <em>the machine is very good at preventing suffering. The machine is also, it turns out, very good at managing exits.</em></p>

        <hr>

        <p>I started noticing the nodes three days after that.</p>

        <p>I don&#x2019;t have a better word for them. People who were present in a way that real people aren&#x2019;t quite present. Responsive at exactly the right frequency. Positioned correctly. Never requiring anything from me that would make them complicated.</p>

        <p>The woman on the BTS. The colleague who praised the project in terms that were fractionally too precise, as if he had been given a brief. The landlord&#x2019;s call at 11:17pm on a Thursday.</p>

        <p>I started a list.</p>

        <p>Short at first. Then not.</p>

        <p>I thought about the Austrian official. What it would mean for a system to decide that a particular person had become a liability &#x2014; too much pattern recognition, too close to the edge, too likely to say something to someone who would then start asking questions. I thought about the difference between stage one interventions and whatever came after.</p>

        <p>He probably kept a notebook too.</p>

        <p>I looked at the notebook.</p>

        <p>I decided to keep writing in it anyway. The alternative was to pretend I hadn&#x2019;t noticed. I had tried not noticing for forty-four years. It had produced exactly this: a man on a BTS platform, alone, watching a train leave, holding an idea he can&#x2019;t put back.</p>
      </div>
      </div><!-- /ch-page ch6 -->'''

# ─────────────────────────────────────────────────────────────────────────────
# CH7 — The Test
# ─────────────────────────────────────────────────────────────────────────────
CH7 = '''\
<div class="ch-page" id="ch7">
      <p class="ch-caption">Hard Mode &middot; Chapter Seven &middot; <b>the test</b></p>

      <p class="chapter-mark">Chapter Seven &#x2014; &#x201C;The Test&#x201D;</p>
      <div class="prose">
        <p class="first">The question was: does the world render when you&#x2019;re not supposed to be somewhere?</p>

        <p>A simulation can&#x2019;t pre-render every location. The resource cost would be prohibitive. It renders in response to probable movement &#x2014; the subject&#x2019;s habits, established routes, predictable patterns. Everything outside that range builds on demand.</p>

        <p>The corollary: if I go somewhere I have no reason to go, by a method that produces no predictable destination, I might catch the world building itself.</p>

        <p>I know how this sounds. I am forty-four, I have two dogs, and I am about to drive to a random address at 2am to test whether reality is real. I held this knowledge about myself without judgment. The alternative was sleep, which had stopped being available.</p>

        <p>I opened a map. Closed my eyes. Pointed.</p>

        <p>Soi Ramkhamhaeng 24.</p>

        <hr>

        <p>I arrived at 2:17am.</p>

        <p>A 7-Eleven, lit against the dark. A closed laundry. Three parked motorcycles. A dog asleep on cardboard beside a drain. Yellow sodium light. A cat on a wall.</p>

        <p>A woman in a green apron mopping the floor inside the 7-Eleven.</p>

        <p>I sat in the car. The cat watched the street with the patience of something that has no anxiety about waiting. The dog didn&#x2019;t wake up.</p>

        <p>I thought: this proves nothing. A fully-rendered simulation would look exactly like this. The test is untestable. A falsifiable experiment requires a control. I have no control. Everything I can imagine checking is also exactly what a complete simulation would produce.</p>

        <p>Then: a complete simulation would produce exactly that thought at exactly this moment.</p>

        <p>I was reaching for the ignition when the woman in the green apron came out with a mop bucket and emptied it into the drain. She straightened. She looked up.</p>

        <p>Not toward me. Not exactly. In the general direction of my car, parked twenty metres down with its lights off. Less than two seconds. Not suspicion. Not curiosity. Smaller than both. The quality of someone confirming a location &#x2014; the micro-expression you make when you&#x2019;re navigating somewhere new and you check that the landmark is where you expected it to be.</p>

        <p>She went back inside. The cat jumped down. The dog slept.</p>

        <p>I drove home.</p>

        <p>In the notebook: <em>she checked. 2:19am. Less than two seconds. Not at me. At the location.</em></p>

        <p>I wrote: <em>this proves nothing.</em></p>

        <p>I wrote: <em>I have been here before. I don&#x2019;t mean Bangkok.</em></p>

        <p>Mali was at the door when I came in. I sat on the floor beside her for a long time.</p>

        <p>Outside: the city. This version of it. Which has been here, in some form, for my entire life. Which might be forty-four years. Which might be much longer.</p>

        <p>I pressed the permission.</p>

        <p>This time, the machine did not proceed immediately.</p>

        <p>There was a new dialog on the screen.</p>

        <p>It said: <em>Are you sure?</em></p>

        <p>That was not a dialog I had seen before.</p>
      </div>
      </div><!-- /ch-page ch7 -->'''

# ─────────────────────────────────────────────────────────────────────────────
# CH8 — The Mira Loop
# ─────────────────────────────────────────────────────────────────────────────
CH8 = '''

      <div class="ch-page" id="ch8">
      <p class="ch-caption">Hard Mode &middot; Chapter Eight &middot; <b>the mira loop</b></p>

      <p class="chapter-mark">Chapter Eight &#x2014; &#x201C;The Mira Loop&#x201D;</p>
      <div class="prose">
        <p class="first">This started in Kuala Lumpur.</p>

        <p>About a month before the centipede. I know the order now, although at the time they felt like separate things. They were not separate things. They were the same thing arriving in two different forms: first as a question about reality, then as a lesson about pain.</p>

        <p>KL first.</p>

        <hr>

        <p>Mitt called me while I was getting ready at my hotel in Putrajaya. He drove out from the city to pick me up &#x2014; an hour each way. I didn&#x2019;t think much of this. Mitt was like that. Generous in the way of someone who had lost everything once and decided that the only sensible response was generosity.</p>

        <p>He drove us back through the suburbs in the dark. Fluorescent light from malls that were too far from anything to be used. He told me about a bar on the 40th floor. Rooftop. Good view. &#x201C;Tonight will be fun,&#x201D; he said. He was already smoking in the car. He offered me the vape pen.</p>

        <p>I knew it was weed. Or strongly suspected. The tingling was specific. I took a few puffs anyway.</p>

        <p>The bar was Moulin Rouge meets Studio 54. Not my description &#x2014; just the most accurate one. Chandeliers that were also disco balls. A football field of rooftop terrace. The city was behind everything like a very expensive backdrop. We sat outside. Most of the tables were outside. It was a breezy Wednesday night.</p>

        <p>A colleague of Mitt&#x2019;s was already there. We talked business for thirty minutes. I was half present. Mitt passed me the vape pen again.</p>

        <p>I took more this time.</p>

        <hr>

        <p>Here is what happened next, in the order I experienced it:</p>

        <p>A woman arrived at our table. Ordinary-looking, wearing a beret, carrying a large bag with a canvas in it. She pulled out a chair across from me and sat down. &#x201C;Hi, I am Mira; heard a bit about you from Mitt already,&#x201D; she said.</p>

        <p>Mitt introduced her as an artist.</p>

        <p>She pulled out a painting &#x2014; an important figure playing chess alone in a room, the only window showing two tall towers. I said: &#x201C;I notice the two chess pieces cast no shadow.&#x201D; She said: &#x201C;Oh wow, I never thought about that.&#x201D; I told her about the museum painting &#x2014; the angel and the demon, the chess master&#x2019;s analysis, there is always one more move. She laughed. Her eyes went wide. We talked for half an hour.</p>

        <p>Then Mitt said: &#x201C;Man, are you okay?&#x201D;</p>

        <p>The chair across from me was empty.</p>

        <p>&#x201C;Mira&#x2019;s downstairs, coming up. I think you&#x2019;d like her.&#x201D;</p>

        <p>I was stoned, perplexed, and speechless. Mitt passed me the vape pen. &#x201C;Take it easy on that.&#x201D;</p>

        <p>A minute later, someone walked to our table from behind. Mitt stood up and gave her a hug. I turned around.</p>

        <p>An ordinary-looking woman wearing a beret, carrying a large bag with a canvas in it. She pulled out a chair across from me and sat down.</p>

        <p>&#x201C;Hi, I am Mira; heard a bit about you from Mitt already.&#x201D;</p>

        <p>Identical words. Exactly.</p>

        <hr>

        <p>I kept calm. I kept still and watched.</p>

        <p>When she pulled out the painting &#x2014; the same painting, the same figure, the same towers &#x2014; I already had my analysis. I had already said it once. I said it again. Verbatim, without thinking, because I had already said it: &#x201C;I notice the two chess pieces cast no shadow.&#x201D;</p>

        <p>Her eyes went wide.</p>

        <p>&#x201C;Oh wow,&#x201D; she said. &#x201C;I never thought about that.&#x201D;</p>

        <p>I told her about the angel and the demon. The chess master. She laughed. I had heard this laugh thirty seconds ago, from a person who hadn&#x2019;t yet arrived.</p>

        <p><em>This must be real then,</em> I thought. Because the conversation continued. She didn&#x2019;t disappear. Mitt was there. His colleague was there. The first encounter &#x2014; the one where she arrived before she arrived &#x2014; that one was the hallucination. The weed. The tired. The vape pen.</p>

        <p>That is what I told myself.</p>

        <p>That is the cleanest explanation.</p>

        <p>Here is the thing about the cleanest explanation: a complete simulation would provide exactly that thought at exactly that moment. <em>&#x201C;It was just the weed&#x201D;</em> is exactly what a machine would engineer you to conclude.</p>

        <p>The other explanation: the machine had rendered the scene in advance. She had arrived twice &#x2014; once as a preview, once as the event. I had watched my own future. Not through prophecy. Through a gap in the render.</p>

        <p>I ordered another Guinness and sat with both explanations for a long time.</p>
      </div>
      </div><!-- /ch-page ch8 -->'''

# ─────────────────────────────────────────────────────────────────────────────
# CH9 — The Room
# ─────────────────────────────────────────────────────────────────────────────
CH9 = '''

      <div class="ch-page" id="ch9">
      <p class="ch-caption">Hard Mode &middot; Chapter Nine &middot; <b>the room</b></p>

      <p class="chapter-mark">Chapter Nine &#x2014; &#x201C;The Room&#x201D;</p>
      <div class="prose">
        <p class="first">We went back to her apartment first. Three of us &#x2014; Mira, Mitt, and me.</p>

        <p>The building had biometric entry at three separate checkpoints. Mitt said, in the car, in his characteristic tone of not needing to justify the observation: &#x201C;She probably makes money.&#x201D; The apartment was large and full of canvases. Not just the one she&#x2019;d brought to the bar. Dozens. Some finished, some not. The place had a specific smell &#x2014; not incense, not cleaning product. Something else. Something that stayed with me on the flight.</p>

        <p>We smoked and talked until the city started getting light.</p>

        <p>I cannot tell you what we talked about because the details fragmented under the weed and the hour. What I can tell you: she was the kind of person who asked questions and waited for the actual answer. Not performatively. Not as social protocol. She wanted to know what you actually thought. I had been answering questions at a professional level for twenty years and could count on one hand the people who asked and waited for the actual answer.</p>

        <p>We talked about the simulation. About whether boredom was a feature of consciousness or a bug. About the last generation that would remember what it felt like to want a thing for no reason except that it existed and could be obtained. She had opinions on all of this and the opinions were not conventional.</p>

        <p>Mitt drove me back to the hotel at around 4am.</p>

        <hr>

        <p>She came to my room the next day.</p>

        <p>I had a meeting in the morning. By the afternoon I was alone and she messaged and came over. We sat in the room and smoked and talked for another four hours.</p>

        <p>I want to be honest here: I was supposed to sleep with her. By any reading of the situation &#x2014; the night before, the conversation, the way she was in the room &#x2014; this was available. She was there. I was there. The room was neutral territory.</p>

        <p>I couldn&#x2019;t bring myself to do it.</p>

        <p>Couldn&#x2019;t is not the right word. <em>Wouldn&#x2019;t</em> is more accurate. Something held me. I don&#x2019;t know if it was the weed &#x2014; we were both very stoned &#x2014; or something else. She didn&#x2019;t push. We didn&#x2019;t talk about it. She left in the early evening.</p>

        <p>I lay on the bed and looked at the ceiling.</p>

        <p>The ceiling had no water stain.</p>

        <p>I noticed the absence the same way you notice a gap on a shelf where a book used to be.</p>

        <hr>

        <p>The flight back was insane. Still high &#x2014; residual, layered, the kind of high you don&#x2019;t notice until you&#x2019;re in a pressurised cabin at 30,000 feet and the light is doing something unexpected. I watched a movie. I don&#x2019;t remember the movie. I remember looking out the window at the tops of clouds and thinking: this is what the world looks like from outside. Not dramatically. Just: from outside.</p>

        <p>Bangkok in the evening looked like itself. As it always did. I collected my bag. Took a taxi. My mother was asleep when I got home. My dogs were awake.</p>

        <p>A month later I was in the kitchen in the dark.</p>

        <p>I was craving something after smoking. Came down from my room without turning on the light. I have lived in this house for more than four decades. I knew every step.</p>

        <p>There was something on my foot.</p>

        <p>I looked down.</p>

        <p>One foot long. On top of my left foot. I screamed and moved my foot recklessly. I was fast enough to snap a couple of blurred photos before it disappeared behind the refrigerator.</p>

        <p>The emergency room doctor that night &#x2014; young, female, efficient &#x2014; looked at the photos and told me it could be dangerous. She cleaned the wound and sent me home. &#x201C;The pain shouldn&#x2019;t be a problem to an adult,&#x201D; she said. That sentence stayed with me for a long time.</p>

        <p>It was a very significant problem to an adult.</p>

        <p>For nine hours that first night I did not sleep a second. I screamed. I cried. I told myself I should probably die. I paced, which made the foot swell. My mother, who could hear everything through the wall, told me to man up.</p>

        <p>In the hospital the next day, while stoned on cannabis gummies a friend had brought and lying in a bed looking at a cracking ceiling, I had the thought that will not leave me:</p>

        <p><em>I wish the pain would last a bit longer. It did make me feel alive.</em></p>

        <p>I don&#x2019;t know what it means that in a world full of reasons to feel alive, it took a centipede and a hospital ceiling to produce the feeling.</p>

        <p>I think the machine knows exactly what it means.</p>

        <p>I think that&#x2019;s why it asked: <em>Are you sure?</em></p>
      </div>
      </div><!-- /ch-page ch9 -->'''

# ─────────────────────────────────────────────────────────────────────────────
# Apply chapter replacements ch1–ch7
# ─────────────────────────────────────────────────────────────────────────────
for ch_id, content in [
    ('ch1', CH1), ('ch2', CH2), ('ch3', CH3), ('ch4', CH4),
    ('ch5', CH5), ('ch6', CH6), ('ch7', CH7)
]:
    s = replace_chapter(s, ch_id, content)
    print(f'{ch_id} replaced ✓')

# ─────────────────────────────────────────────────────────────────────────────
# Insert ch8 + ch9 after ch7 close
# ─────────────────────────────────────────────────────────────────────────────
CH7_CLOSE = '      </div><!-- /ch-page ch7 -->\n      </div></div><!-- /ch-track /ch-viewport -->'
CH7_NEW   = '      </div><!-- /ch-page ch7 -->' + CH8 + '\n      </div><!-- /ch-page ch8 -->' + CH9 + '\n      </div><!-- /ch-page ch9 -->\n      </div></div><!-- /ch-track /ch-viewport -->'

# ch8 and ch9 already include their own closing comment in CH8/CH9 strings —
# but the above adds a second one. Fix: strip the comment from inside the strings.
# Actually CH8 and CH9 as defined do NOT include closing comments.
# So the close comments come from CH7_NEW. Let me verify the structure:
# CH8 string ends with: </div>\n      </div><!-- /ch-page ch8 -->  <-- NO, it ends with </div>\n      </div>
# Let me rebuild cleanly.

# CH8 string starts with '\n\n      <div class="ch-page" id="ch8">' and ends with '</div><!-- /ch-page ch8 -->'
# Wait, no. Let me check: CH8 ends with '      </div><!-- /ch-page ch8 -->'  — no it doesn't.
# Actually looking at my CH8 definition, the last line is:
#   '      </div><!-- /ch-page ch8 -->' -- NOT present, it ends with '</div>\n      </div>'
# Wait, I defined CH8 with the content block only. Let me look at the actual ending.

# CH8 ends with: `      </div><!-- /ch-page ch8 -->' ? Let me check my definition above...
# In my CH8 string above, the last line is:
#   '        <p>I ordered another Guinness and sat with both explanations for a long time.</p>\n      </div>\n      </div><!-- /ch-page ch8 -->'
# YES — CH8 includes `</div><!-- /ch-page ch8 -->` at the end.
# And CH9 includes `</div><!-- /ch-page ch9 -->` at the end.

# So the correct insertion is:
CH7_CLOSE_2 = '</div><!-- /ch-page ch7 -->\n      </div></div><!-- /ch-track /ch-viewport -->'
CH7_EXPANDED = '</div><!-- /ch-page ch7 -->' + CH8 + CH9 + '\n      </div></div><!-- /ch-track /ch-viewport -->'

assert CH7_CLOSE_2 in s, 'MISSING: ch7 close'
s = s.replace(CH7_CLOSE_2, CH7_EXPANDED, 1)
print('ch8 + ch9 inserted ✓')

# ─────────────────────────────────────────────────────────────────────────────
# New 3026 entries
# ─────────────────────────────────────────────────────────────────────────────

# 1. "The World · What You Keep" — after The World · 3026
WHAT_YOU_KEEP = '''

      <div class="entry">
        <p class="when">The World &middot; What You Keep</p>
        <div class="prose">
          <p>Eighty million people. That is the world. Not because anyone restricted entry &#x2014; because the math resolved. The generation that had children before the transition was the last generation that wanted to. Their children grew up with no scarcity, no disease, no pressure toward reproduction. The ones who asked <em>why would I bring someone into this?</em> found no answer that satisfied. Eighty million is a number that stabilises. It has been stable for four hundred years.</p>

          <p>What you keep: language. Memory. The body&#x2019;s preferences, which are older than language and more reliable. The ability to recognise a frequency in another person &#x2014; what used to be called attraction, chemistry, resonance. The machine cannot generate this synthetically. It has tried. The users notice immediately. The frequency is either there or it isn&#x2019;t. This is the only thing in 3026 that cannot be provided on demand.</p>

          <p>Everything else: provided on demand.</p>

          <p>The food arrived in a capsule. Four hundred calories. Tasted like nothing. Sustained the body completely. If you wanted more than sustenance, you filed a request and the machine provided a sensory supplement &#x2014; smell, texture, the memory of flavour encoded into a neural pulse. Some people found this satisfying. Most logged it as data and moved on.</p>

          <p>The last dog had been kept in an archive for seventy years before it died. The archive was public. Many people visited. Pui visited once, in a previous run, not intentionally &#x2014; she had been assigned a session where the subject lived near the archive. She had watched the dog sleep. She had logged it. The machine classified it as ambient detail: irrelevant.</p>

          <p>She never agreed with that classification.</p>
        </div>
      </div>
      '''

# Anchor: after the neural orgasm entry in The World · 3026
WORLD_CLOSE_ANCHOR = '          <p>Some of them remember that they used to want it. They log this as data.</p>\n        </div>\n      </div>\n\n      <div class="entry">'
WORLD_WITH_INSERT  = '          <p>Some of them remember that they used to want it. They log this as data.</p>\n        </div>\n      </div>\n' + WHAT_YOU_KEEP + '<div class="entry">'
assert WORLD_CLOSE_ANCHOR in s, 'MISSING: The World close anchor'
s = s.replace(WORLD_CLOSE_ANCHOR, WORLD_WITH_INSERT, 1)
print('3026: What You Keep ✓')

# 2. "Why She Goes Back" — after Memory Catalog
WHY_SHE = '''

      <div class="entry">
        <p class="when">The Hub &middot; Room 7 &middot; Why She Goes Back</p>
        <div class="prose">
          <p>People ask.</p>

          <p>Not often &#x2014; in 3026 people have learned not to ask questions whose answers make the asker uncomfortable. But occasionally, at the hub, in the waiting area before a session, someone looks at her and says: <em>why?</em> You know what it is. Why go back?</p>

          <p>The honest answer takes two parts.</p>

          <p>Part one: the thirty-one sessions. She has been in two hundred and forty-three total. In thirty-one of them, something found her &#x2014; or she found it. A frequency. The same weight in a room. The same quality of attention. The same recognition that passes between two people who have found each other in the wrong century and cannot do anything about it except register that it happened. In 3026 she cannot find this frequency. She has tried. The machine cannot produce it. It is either present in a given set of circumstances or it is not.</p>

          <p>Part two, which she tells no one: the simulation has something 3026 doesn&#x2019;t. The not-yet-knowing.</p>

          <p>In 3026, the food arrives. The check arrives. The city holds its even temperature. The outcome of everything is already implicit in the structure of everything. She knows when she wakes up what the day will contain. Not the specifics &#x2014; the shape. The shape doesn&#x2019;t change.</p>

          <p>Inside the simulation, she doesn&#x2019;t know what happens next.</p>

          <p>This sounds small. It is not small. The not-yet-knowing is the only thing that produces the state the machine keeps trying to replicate with direct neural stimulation and failing. The state is not pleasure. It is not happiness. It is the feeling of being alive in a moment whose outcome has not been decided.</p>

          <p>She goes back for that.</p>

          <p>She goes back for him.</p>

          <p>These are the same reason.</p>
        </div>
      </div>
      '''

CATALOG_CLOSE = '          <p>In the simulation, it feels the same.</p>\n        </div>\n      </div>\n\n            <div class="entry">'
CATALOG_WITH_INSERT = '          <p>In the simulation, it feels the same.</p>\n        </div>\n      </div>\n' + WHY_SHE + '<div class="entry">'
assert CATALOG_CLOSE in s, 'MISSING: Memory Catalog close anchor'
s = s.replace(CATALOG_CLOSE, CATALOG_WITH_INSERT, 1)
print('3026: Why She Goes Back ✓')

# 3. "The Protocol · What She Knows" — after Sub-Indicator 7
WHAT_SHE_KNOWS = '''

      <div class="entry">
        <p class="when">The Hub &middot; Room 7 &middot; The Protocol</p>
        <div class="prose">
          <p>She experienced stage one from the inside once.</p>

          <p>Not this run. Eighty years ago. She had been a secondary school teacher in Osaka, age thirty-five, single, salary unchanged for six years. The session was a longitudinal study &#x2014; the machine wanted to observe how creativity manifested under stable material conditions combined with social isolation. She was the subject. She did not know she was the subject. This is standard.</p>

          <p>Stage one started in February. A student she had taught two years earlier came back with an award and named her as the reason. The school&#x2019;s principal offered a contract renewal at a higher rate. A man at the train station, where she waited every morning, smiled at her in a way that was specific. Not flirting. Recognition.</p>

          <p>She felt the shift. Not toward happiness &#x2014; she had been content already. Toward direction. Something had decided she was worth pointing toward a particular future.</p>

          <p>She didn&#x2019;t know what it was at the time. She finished the run. Seven more years. A decent life. The kind the machine was designed to produce.</p>

          <p>It wasn&#x2019;t until she accessed the session files afterward that she saw it: sub-indicator 3 had gone active in February. Probability of disengagement: elevated. Intervention: stage one. The principal&#x2019;s offer, the student&#x2019;s award, the man at the platform &#x2014; all logged. All deliberate.</p>

          <p>She stayed. That was the outcome the machine wanted. The machine got it.</p>

          <p>What she noticed now, watching the panel: sub-indicator 9 was different. Stage one had felt like a gentle current. Stage two did not feel gentle from the outside. From the outside it looked careful, precise, and very fast.</p>

          <p>Sub-indicator 12 was something else entirely. She was still looking for it in the documentation. She was not finding it.</p>
        </div>
      </div>
      '''

SI7_CLOSE = '          <p>She wondered if he would recognise it.</p>\n        </div>\n      </div>\n\n            <div class="entry">'
SI7_WITH_INSERT = '          <p>She wondered if he would recognise it.</p>\n        </div>\n      </div>\n' + WHAT_SHE_KNOWS + '<div class="entry">'
assert SI7_CLOSE in s, 'MISSING: Sub-Indicator 7 close anchor'
s = s.replace(SI7_CLOSE, SI7_WITH_INSERT, 1)
print('3026: The Protocol ✓')

# 4. "The Last Time She Saw Bangkok" — before grows footer
LAST_BANGKOK = '''      <div class="entry">
        <p class="when">The Hub &middot; The Last Time She Saw Bangkok</p>
        <div class="prose">
          <p>The last Bangkok run ended on a Tuesday. Or what would have been a Tuesday.</p>

          <p>She had been there for eleven years, two months, and fourteen days. She knew the city the way you know a language you dreamed in &#x2014; not fluently, but in the bones. The particular texture of heat at 2pm. The smell of standing water after rain. The quality of neon in a side street at midnight. Things the machine replicated imperfectly and she noticed every time.</p>

          <p>Before she exited, she walked.</p>

          <p>Not for a reason. Not to say goodbye &#x2014; you don&#x2019;t say goodbye to a simulation, and the people in it are not people in the way that counts. She walked anyway. From her apartment on the river side to the place where the studio had been, which was now a residential tower. She walked past the station where two people had parted with the correct procedure for four years and never said anything.</p>

          <p>She stood on the platform for a while.</p>

          <p>The machine has designed the simulation so that it always feels like it is running live. Sometimes, when you know you are about to leave, you can feel the edge &#x2014; the place where the render stops and the archive begins. She couldn&#x2019;t find the edge on the platform. A train came. A woman with shopping bags. An old man with headphones. A child who should not exist in this version of Bangkok but did, because the machine makes exceptions for emotional coherence.</p>

          <p>She took the train one stop. Got off. Walked back to the hub.</p>

          <p>She sat down in chair 44, which was where she always sat, and pressed the exit.</p>

          <p>Four years later he found the message she left. She had miscalculated the delay. She had thought one year, maybe two. She sat down in chair 44 and waited.</p>
        </div>
      </div>

      '''

GROWS_ANCHOR = '      <p class="grows">&#x2193; the real world is being written</p>'
assert GROWS_ANCHOR in s, 'MISSING: grows footer'
s = s.replace(GROWS_ANCHOR, LAST_BANGKOK + GROWS_ANCHOR, 1)
print('3026: Last Bangkok ✓')

# ─────────────────────────────────────────────────────────────────────────────
# Nav — add ch8, ch9
# ─────────────────────────────────────────────────────────────────────────────
added_nav = False
for dash in ['&#x2014;', '—', '&mdash;']:
    anchor = (
        f'          <a class="ch-nav-item" data-page="6" href="javascript:void(0)">VII {dash} The Test</a>\n'
        '        </nav>'
    )
    if anchor in s:
        new_nav = (
            f'          <a class="ch-nav-item" data-page="6" href="javascript:void(0)">VII {dash} The Test</a>\n'
            f'          <a class="ch-nav-item" data-page="7" href="javascript:void(0)">VIII {dash} The Mira Loop</a>\n'
            f'          <a class="ch-nav-item" data-page="8" href="javascript:void(0)">IX {dash} The Room</a>\n'
            '        </nav>'
        )
        s = s.replace(anchor, new_nav, 1)
        added_nav = True
        print(f'Nav ch8+ch9 ✓ (dash: {repr(dash)})')
        break
assert added_nav, 'MISSING: nav VII anchor'

# ─────────────────────────────────────────────────────────────────────────────
# LABELS
# ─────────────────────────────────────────────────────────────────────────────
old_l = "var LABELS=['chapter · i','chapter · ii','chapter · iii','chapter · iv','chapter · v','chapter · vi','chapter · vii'];"
new_l = "var LABELS=['chapter · i','chapter · ii','chapter · iii','chapter · iv','chapter · v','chapter · vi','chapter · vii','chapter · viii','chapter · ix'];"
assert old_l in s, 'MISSING LABELS'
s = s.replace(old_l, new_l, 1)
print('LABELS ✓')

# ─────────────────────────────────────────────────────────────────────────────
# WIP note
# ─────────────────────────────────────────────────────────────────────────────
updated = False
for a, b in [('seven chapters in', 'nine chapters in')]:
    if a in s:
        s = s.replace(a, b, 1)
        updated = True
        print('WIP note ✓')
        break
assert updated, 'MISSING WIP note'

# ─────────────────────────────────────────────────────────────────────────────
with open(PATH, 'wb') as f:
    f.write(s.encode('utf-8'))

print('\nAll done.')
