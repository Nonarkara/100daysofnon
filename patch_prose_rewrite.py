#!/usr/bin/env python3
"""patch_prose_rewrite.py
Hemingway / Dr Non / Fincher register. All 10 chapters.
Keeps artwork figures intact. Replaces paragraph content only.
"""
import re

def encode(text):
    # *italics* → <em>
    text = re.sub(r'\*([^*\n]+)\*', r'<em>\1</em>', text)
    text = text.replace('&', '&amp;')
    text = text.replace('—', '&#x2014;')
    text = text.replace("'", '&#x2019;')
    # curly double quotes — toggle open/close
    result, open_q = [], False
    for ch in text:
        if ch == '"':
            result.append('&#x201C;' if not open_q else '&#x201D;')
            open_q = not open_q
        else:
            result.append(ch)
    return ''.join(result)

def build_prose(paragraphs):
    lines = []
    first = True
    for p in paragraphs:
        p = p.strip()
        if not p:
            continue
        if p == '---':
            lines.append('\n        <hr>')
        else:
            enc = encode(p)
            cls = ' class="first"' if first else ''
            sep = '' if first else '\n'
            lines.append(f'{sep}\n        <p{cls}>{enc}</p>')
            first = False
    return '\n'.join(lines) + '\n'

def replace_chapter(html, ch_id, paragraphs):
    ch_pos = html.find(f'id="{ch_id}"')
    assert ch_pos > 0, f'Chapter {ch_id} not found'
    prose_pos = html.find('<div class="prose">', ch_pos)
    assert prose_pos > 0, f'Prose div not found for {ch_id}'
    fig_end_tag = '        </figure>\n'
    fig_end = html.find(fig_end_tag, prose_pos)
    assert fig_end > 0, f'Figure end not found for {ch_id}'
    content_start = fig_end + len(fig_end_tag)
    prose_close = html.find('\n      </div>', content_start)
    assert prose_close > 0, f'Prose close not found for {ch_id}'
    new_content = build_prose(paragraphs)
    return html[:content_start] + new_content + html[prose_close:]

# ── Chapter texts ─────────────────────────────────────────────────────────────

CH1 = [
    "The apartment is exactly the right temperature. Not warm. Not cool. The degree at which the body forgets itself.",
    "He has learned to be suspicious of comfort.",
    "Two hours at the machine. Three monitors. Bangkok at 6pm through the glass: tuk-tuks, motorbikes, the chime of a 7-Eleven two floors down. He says: main panel north. The machine builds. Sixteen pixels between events. It adjusts. Forty percent opacity at rest, full on hover. Done.",
    "He says what he wants. The machine makes it. He corrects. It remakes.",
    "Twenty-five years ago: trace paper, a T-square, a lamp at 2am, nobody. Now the machine answers. The process is the same. The discipline is the same. The word they eventually arrived at for it was *vibe coding*. He found this faintly embarrassing. It was completely accurate.",
    "His phone glowed. In an hour, someone was coming over.",
    "An algorithm matched them. She is exactly as advertised. Three meetings. A drink, then what a drink turns into. The fourth will probably be the last — not because anything goes wrong. Because nothing, precisely nothing, goes wrong.",
    "He set the machine to render.",
    "---",
    "The message had arrived on a Tuesday.",
    "Her name was Pui. Architecture school, twenty-five years back. The desk next to his for five years. One of six women in a cohort of fifty-five. Funny. Exact. The kind of person who makes something interesting from materials nobody else would have considered.",
    "They were not close. They were the kind of people who would have been, if either of them had known how to close that last ten centimetres.",
    "He had been writing on her Facebook wall every birthday. A few words. The contact you maintain for someone you care about in the specific way of people who never acted on it.",
    "She died in 2018. He did not know.",
    "He wrote in 2019. The wall received it. In 2020, the same.",
    "2021: *Twenty-five years. Hope you're well.*",
    "A mutual friend replied within hours: *You didn't know. She died. Three years ago. Cancer.*",
    "The shame was specific. Not grief — grief requires presence. This was two years of birthday messages to a dead woman's wall. Neither he nor the wall had any particular reason to change what they were doing.",
    "He scrolled. The accumulation of posts. The careful, well-meaning tone. A ceremony for someone he'd never had the ceremony with when she was alive.",
    "Then, two weeks before any of that: her last post.",
    "Not what people write when they know they're dying. Too calm. Too specific. Something she'd been sitting with for a long time.",
    "Rough translation:",
    "*Don't waste time looking for meaning in the part you just lived. The door is always on the left, not the right. I went back early, but only because I got bored waiting for you to ask who played your mother.*",
    "---",
    "She arrived an hour later. They had a drink. They had sex — not the polite kind. Hard, deliberate, entirely present. Afterward something ran out of both of them simultaneously, like a tide that had been building for months choosing this particular Wednesday to turn.",
    "He lay on his back in the dark.",
    "The neural pathways are real. Twenty years of use and they fire whether you consult them or not. At twenty it was need. At thirty, habit. At forty-four it is the act of a man trying to prove something to a brain that has already decided the evidence is insufficient.",
    "*This is why I use everything.* Not her. Not any particular her. The using itself. The few minutes after: a clarity so complete it feels chemical. The mind stripped to signal. The body remembering what it is.",
    "He thought: how many times have I done this?",
    "He thought: not enough times to stop noticing.",
    "The city settled into its lower register. He lay still. The exact-right-temperature dark.",
    "He reached for his phone. Read her post again.",
    "*The door is always on the left.*",
    "Turned the screen off. Lay there for a long time.",
]

CH2 = [
    "Three days after the Facebook wall, he watched *The Island*.",
    "Not for the first time. He'd seen it when it came out, and on a long flight, and now a third time — alone, eleven pm, one screen — because something about Pui's last post made him want to watch a film about people who live in a perfect facility and don't know it.",
    "Two hundred clones. White facility. The outside world is contaminated, they're told. Once a month, a lottery. The winner goes to The Island. Nobody who wins ever comes back, but the inside is comfortable enough.",
    "Lincoln Six Echo's tell: a fly. One thing in a sterile facility that cannot have flies. One thing that proves the world wasn't rendered all the way down.",
    "He paused the film.",
    "*My tell is a message from a dead woman's wall. Two years of birthday greetings nobody answered. A direction — left — that I recognised before I understood it.*",
    "Lincoln Six found a door and ran through it. Came out the other side where things were real and messy and you could hold them.",
    "He had a direction. Left. An address without a street.",
    "He pressed play. Watched Lincoln Six run through a facility that built itself behind him — walls completing, corridors extending, the world rendering in response to probable movement.",
    "At the end he didn't move.",
    "*The world is very good at appearing complete.*",
    "---",
    "1999. Architecture school. He was twenty.",
    "Basement studio, no air conditioning worth mentioning. Bangkok heat through the walls. The boys played basketball in the afternoon and came upstairs to draft without showering. This should have been unacceptable. It wasn't. The studio at 2am was a habitat, not a classroom. You smelled like what you were doing.",
    "The girls stayed late on purpose. He understood this only later.",
    "At twenty: the hunger is enormous and the language hasn't arrived. You stay. You sit close. You work until 3am. You feel everything and say nothing. You go home on the same train and part at the gate with correct and careful distance.",
    "Pui's desk was next to his.",
    "She had a laugh that involved her whole upper body. Mid-laugh, she occasionally made contact with his arm. His arm would not forget this for hours. He was not built for that kind of movement with people he had to see every day. So he stayed at his table and did the work and noticed, in the specific peripheral way of someone who has decided not to look directly, everything.",
    "For twenty-five years: everything.",
    "---",
    "The twelve minutes came in March.",
    "He'd smoked half a joint on the balcony — third attempt, the logic already failing — then sat on the floor beside Mali and closed his eyes.",
    "The studio. Not a dream version. The actual studio. That specific afternoon light through the north-facing windows. The A/C unit on the east wall that had been one month from breaking for three years. The physical fact of a wooden stool at a standing-height drafting table — a posture he had not inhabited since 2004.",
    "She was at the table to his left.",
    "*Short and therefore ventilated*, she had explained once, about the FBT shorts, which he had not thought about and had thought about constantly. She had a way of laughing that made contact with his arm. By the fifth year he had mapped the exact geography of skin above the hem — pale, smooth, early twenties — and held it at a precise distance. Never acted on it.",
    "She turned to say something about a section drawing.",
    "He understood three things simultaneously:",
    "That none of it mattered. Not the portfolio, not the distinction, not the five years of careful choices. Not the career he was about to start. The conviction arrived complete, from nowhere — not depression; depression is absence. This was a clarity so total it felt physical. An illusion inside an illusion. The whole constructed sequence — backdrop.",
    "That she was alive. He did not mean the woman at the table — that was just a woman at a table. He meant Pui. The one whose name he'd seen on his phone screen fourteen years after this studio moment. She was alive the way a location exists when you're not there. The way a signal persists after you move out of range.",
    "That the only thing he had ever wanted — the actual only thing, stripped of language and age — was to be in a room with someone and have the distance between them be something other than maintenance.",
    "Then he was back on his apartment floor. Mali's weight against his leg. The city at 2am.",
    "Twelve minutes. He had checked the phone.",
    "He opened the app and booked the first available slot. Not because he wanted to. Because the twelve minutes had shown him what wanting becomes — and he needed to carry the proof before the memory of the proof faded.",
]

CH3 = [
    "The dream lasted longer than twelve minutes.",
    "Still the studio. But she was forty-four — my age now — and she knew things about the current shape of my life she shouldn't have known. She spoke the way people speak when they've been waiting and have stopped being careful.",
    '"You came back," she said.',
    "I told her I didn't know what she meant.",
    '"You always say that."',
    "She said the door was on the left. Not metaphorically — a direction. Twice. The way you tell someone how to find a room in a building they haven't been to.",
    "I asked where she'd been.",
    "She looked at me the way people look when the answer should be obvious.",
    '"Longer than it felt. Years, subjectively. Nothing in the other time." She said *the other time* the way you say *the other side of the room*. "I\'ve been sitting at table forty-four."',
    "I said: I'm forty-four.",
    "She said: yes.",
    "---",
    "I woke on the bedroom floor. The woman I was with was asleep in the bed. Her breathing. The water stain on the ceiling. Bangkok at 4am.",
    "My phone: a text from a number I didn't recognise.",
    "*The door is always on the left.*",
    "Timestamp: 4:17am.",
    "I have checked the number eleven times. No registered account, no carrier record. I called the phone company once. It felt immediately embarrassing.",
    "I kept the message.",
    "---",
    "I started a list.",
    "Not in the work notebook. A separate document, no title. People who had exited the way Pui had exited. Not suicides — I was not comfortable with that word yet. People who left a message that made no sense to anyone not reading the same paper. People who, at the end, seemed to know something about the room they were in.",
    "Pui. 2018. Cancer, officially. Last post: door, left, I got bored, ask who played your mother.",
    "A man from my architecture cohort. 2014. Car accident at thirty-eight. Last message to the group: *Back to the studio. You'll understand this some day.* Nobody replied. The thread is still open.",
    "A musician I'd followed for fifteen years. 2020. Heart attack at forty-one. Last record: one track, no title, thirty seconds long. The sound of someone tapping on a pane of glass.",
    "Three names. I was approaching this the way I approach any system I don't understand: map the anomalies, look for the pattern.",
    "Pattern: people who seemed to know something, exited young, left a message nobody could decode.",
    "I had a feeling the list was going to get longer.",
]

CH4 = [
    "I tried marijuana first.",
    "The logic — if it was logic — was that the conversation had happened between waking and not-waking. Altering the chemistry might widen the gap.",
    "Three nights. Different quantities. Same result: slow thoughts, appetite, the particular loneliness of being high alone. No gap. The ceiling.",
    "Alcohol strips things back — not to truth, but to the version of yourself that existed before you learned to perform. Two occasions. The usual residue. The usual absence.",
    "I was trying to get back to twelve minutes.",
    "---",
    "There had been a woman, for two years, who called when she wanted and didn't call when she didn't. The architecture was entirely hers. I arrived when summoned. I was good at what she summoned me for — she told me this, with the detachment of someone reviewing a service. I loved her in the way you love something that is dismantling you without announcing its intentions.",
    "One Thursday she stopped calling. Weeks. A month. Two. I understood only after the silence that I had been useful the way a good appliance is useful: reliably, without reciprocity, until it wasn't needed.",
    "I want to be precise about the ferocity.",
    "I have brought it to bed for twenty years and explained it to myself in many ways. Intensity. The way an architectural mind applies itself with full attention or not at all. These explanations were accurate and wrong simultaneously. The actual explanation arrived slowly:",
    "In a thousand years, the machine offers a direct neural pathway. Faster than the act. More complete. No negotiation, no the-next-morning. When that becomes available, the act becomes optional, then ceremonial, then unnecessary, then a thing people log as data. The last person who wanted sex for its own sake has been dead for four hundred years, and nobody noticed, because the destination was still available — faster, cleaner, without the residue of a body in the room.",
    "I have known this my whole life. Below the level where it can be named. The body knew what the mind hadn't arrived at: that this capacity runs out. That the specific irrational weight of wanting a specific person — the ferocity, the not-quite-controllable quality, the proof that you are a living thing with a temperature — is borrowed time.",
    "I book the dates. The algorithm matches me. We deliver something technically correct. I walk home. I feel what I'm supposed to feel. Five times in two weeks, six, with a persistence that has started to look, from the outside, like something else. My friends joke. I smile. I am not joking.",
    "I am practising. I am practising because I know the practice ends.",
    "---",
    "The other kind: a place on Sukhumvit, listed in a Telegram channel a colleague had added me to without explanation. The message that appears every Friday: available, three rooms. A door number. A payment method. An hour. I went three times in two weeks. Not for satisfaction — I had stopped confusing those categories. I went because the transaction was honest about what it was. A body and its needs, a body and its function, stripped of everything else.",
    "The arrangement was the problem.",
    "The arrangement, however honest, still ends at a door. Still produces the same 3am ceiling. The same awareness that nothing arrived except what was paid for.",
    "And then there was the woman who had a boyfriend.",
    "I had gone back five times. I knew what I was doing — had known from the second visit. The boyfriend existed, was mentioned without embarrassment, occupied a different register of her attention. I went back the fifth time stoned enough to be honest with myself about why. I sat in her apartment at 11pm and thought: I want the boyfriend to come through the door. I want there to be a consequence. I want something to happen that I have no control over.",
    "Nothing happened. The boyfriend did not come through the door. I went home.",
    "I lay on the ceiling and understood that what I was looking for — across the dating apps, the Sukhumvit room, the woman with the boyfriend — was the same thing Lincoln Six was looking for in the facility.",
    "A fly. Something that proves the world wasn't rendered all the way down.",
]

CH5 = [
    "She was asleep. I was looking at the ceiling.",
    "Something had just happened. Not lovemaking — that word has a sentimentality I don't trust. She had cried. I had not stopped. She told me not to stop and I didn't and we were both making a sound that had nothing to do with performance. The body had understood something about the situation that I was still working toward with language.",
    "In a thousand years, the machine provides a direct neural pathway. Faster. More complete. No negotiation, no this ceiling, no the-next-morning. The destination without the journey.",
    "The journey is everything. You can give someone the steak without the animal that was once alive and what you have given them is not the same thing. The machine will not understand this until it is too late. It is already too late.",
    "I got dressed quietly. Went to the kitchen. Wrote in the other notebook until it was light.",
    "---",
    "Thursday morning, Khlong Toei market, on the way back from the gym.",
    "A woman selling morning glory at the edge of the covered section. Fifties, probably. Green plastic crates. The specific efficiency of someone who has been doing this exact motion for twenty years.",
    "I stopped.",
    "Not because of her. Because of the thirty centimetres of air between where I was walking and where she was standing.",
    "She looked up. Less than a second of eye contact.",
    "Not attraction. Not recognition in any ordinary sense. Something that preceded both — something the body does before the brain has arrived. A frequency. A radio finding a station for half a second before the dial moves on.",
    "She looked back down at the morning glory. I kept walking.",
    "I stopped twenty metres further on. Stood there for twelve minutes — I timed it — looking back at the covered section. I had no language for what had just happened. The language would have been: *you have the same frequency as someone I've been looking for since before I knew I was looking.* The language would have been: *I have been here before and you were there.*",
    "I didn't go back. I bought mangoes from a different stall.",
    "In the notebook: *Thursday 7:42am. Khlong Toei. Left side of covered section. Morning glory seller. Less than one second. The frequency. Not her. Through her.*",
    "I wrote: *there is a channel this city sometimes broadcasts on. I don't know what calls it. I know it's the same channel.*",
    "I had felt it once before. At twenty. In a hot basement. At the desk next to mine.",
    "---",
    "Three days later I ordered a steak.",
    "Not from hunger. I had been eating less red meat — the adjustment you make at forty-four when the body starts having opinions. But I sat in a restaurant I hadn't been to in years and ordered it because I wanted it in a way I had not wanted something in a long time.",
    "Not hunger. Want. The specific animal pull of a specific thing for no reason except that it existed and could be obtained.",
    "In a thousand years: no cattle. The want would remain, filed somewhere, accessible. The thing itself gone. I thought about Cipher. His deal with the machine: *I know this steak doesn't exist. But after nine years, ignorance is bliss.*",
    "The difference between Cipher and me: there is no Agent Smith across the table. There is no deal on offer. There is only this steak, and the fact that I can taste it, and the knowledge — arriving now, fork in hand, quite calmly — that the tasting is the entire point.",
    "I finished it. Paid. Walked home.",
    "I did not feel full. I felt located.",
]

CH6 = [
    "I found it in an Austrian expat forum.",
    "A reply to a community events post, buried six threads down: *re: Michael — if anyone knew him at the embassy, his family is still looking for answers.* No last name. Seven months old. Nobody had replied.",
    "Austrian trade official. Commercial Counsellor. Died in Bangkok in May. Age fifty-four. One paragraph from his office. Cause of death: not stated. Replacement listed within the week.",
    "I searched. Almost nothing. One newspaper article. An institutional announcement. A Vienna funeral page — twenty-one condolences. Every single one used the word *suddenly*. Not after an illness. Not after an accident. Just: suddenly. Unexpectedly. Far too soon. A man who had sat beside chancellors and archdukes. People across three continents, all of them bewildered, none of them informed.",
    "The silence was the thing. That level of connectivity — and total silence.",
    "*The machine is very good at preventing suffering. The machine is also very good at managing exits.*",
    "---",
    "Three days later I started noticing the nodes.",
    "People present in a way that real people aren't quite present. Responsive at exactly the right frequency. Positioned correctly. Never requiring anything that would make them complicated.",
    "The woman on the BTS. A colleague who praised the project in terms fractionally too precise — as if given a brief. The landlord's call at 11:17pm on a Thursday.",
    "I started a second list.",
    "The architect from my year who died in 2014 — last message: *Back to the studio.* Now I added a name from a reunion I hadn't attended. A woman, three years ahead of us. Died 2017. Before forty. Her final words to her sister, secondhand: something about windows. All the windows face the wrong direction. The mutual friend's wife: *we thought it was the morphine.*",
    "Six names. Every one of them had gotten out before whatever was supposed to happen next.",
    "---",
    "I thought about Michael, the Austrian attaché. What it would mean for a system to decide a particular person had become a liability — too much pattern recognition, too close to the edge, too likely to say something to someone who would then start asking questions. The difference between stage-one interventions and whatever came after.",
    "He probably kept a notebook too.",
    "I looked at my notebook.",
    "I decided to keep writing in it anyway. The alternative was to pretend I hadn't noticed. I had tried not noticing for forty-four years. It had produced exactly this: a man on a BTS platform, alone, watching a train leave, holding an idea he can't put back.",
]

CH7 = [
    "He had watched *The Island* again that evening.",
    "Not the whole thing. The specific scene: Lincoln Six Echo at the perimeter of the facility — a wall representing the outside world — realising the world beyond it hadn't been rendered because no one was expected to reach it. The outside existed only when someone was supposed to see it. Everything else was white.",
    "Lincoln's insight: *if I go somewhere I'm not supposed to go, the world won't be there yet.*",
    "He closed the laptop.",
    "---",
    "A simulation can't pre-render every location. The resource cost would be prohibitive. It renders in response to probable movement — the subject's habits, established routes, predictable patterns. Everything outside that range builds on demand.",
    "*Corollary: if I go somewhere I have no reason to go, by a method that produces no predictable destination, I might catch the world building itself.*",
    "I know how this sounds. I am forty-four, I have two dogs, I am about to drive to a random address at 2am to test whether reality is real. I held this knowledge about myself without judgment. The alternative was sleep, which had stopped being available.",
    "I opened a map. Closed my eyes. Pointed.",
    "Soi Ramkhamhaeng 24.",
    "---",
    "I arrived at 2:17am.",
    "A 7-Eleven lit against the dark. Closed laundry. Three parked motorcycles. A dog asleep on cardboard beside a drain. Yellow sodium light. A cat on a wall.",
    "A woman in a green apron mopping inside the 7-Eleven.",
    "I sat in the car. The cat watched the street with the patience of something that has no anxiety about waiting. The dog didn't wake up.",
    "*This proves nothing. A fully-rendered simulation would look exactly like this. The test is untestable. Everything I can check is exactly what a complete simulation would produce.*",
    "Then: *a complete simulation would produce exactly that thought at exactly this moment.*",
    "I was reaching for the ignition when the woman in the green apron came out with a mop bucket and emptied it into the drain. She straightened. She looked up.",
    "Not toward me exactly. In the general direction of my car — parked twenty metres down, lights off. Less than two seconds. Not suspicion, not curiosity. Smaller than both. The quality of someone confirming a location. The micro-expression you make when navigating somewhere new and checking that the landmark is where you expected.",
    "She went back inside. The cat jumped down. The dog slept.",
    "I drove home.",
    "In the notebook: *she checked. 2:19am. Less than two seconds. Not at me. At the location.*",
    "I wrote: *this proves nothing.*",
    "I wrote: *I have been here before. I don't mean Bangkok.*",
    "Mali was at the door when I came in. I sat on the floor beside her for a long time.",
    "I pressed the permission. The machine did not proceed immediately.",
    "A new dialog appeared on the screen.",
    "*Are you sure?*",
    "That dialog was not one I had seen before.",
]

CH8 = [
    "This started in Kuala Lumpur.",
    "About a month before the centipede. I know the order now, though at the time they felt like separate things. They were the same thing in two forms: first as a question about reality, then as a lesson about pain.",
    "---",
    "Mitt called while I was getting ready at the hotel in Putrajaya. He drove an hour each way to pick me up — he was like that. Generous in the way of someone who had lost everything once and decided the only sensible response was generosity.",
    "He drove us back through the suburbs in the dark. Fluorescent light from malls too far from anything to be used. He told me about a bar on the 40th floor. Rooftop. Good view. *Tonight will be fun*, he said, already smoking. He offered the vape pen.",
    "I knew it was weed. I took a few puffs anyway.",
    "The bar: Moulin Rouge meets Studio 54. Chandeliers that were also disco balls. A football field of rooftop terrace. The city behind everything like a very expensive backdrop. A colleague of Mitt's was already there. Business for thirty minutes. Mitt passed me the vape pen again.",
    "I took more.",
    "---",
    "A woman arrived at our table. Ordinary-looking, wearing a beret, carrying a large bag with a canvas in it. She pulled out a chair across from me and sat down.",
    '"Hi, I am Mira; heard a bit about you from Mitt already."',
    "She pulled out a painting — an important figure playing chess alone, the only window showing two tall towers. I said: *I notice the two chess pieces cast no shadow.* She said: *Oh wow, I never thought about that.* I told her about the museum painting — the angel and the demon, the chess master's analysis, there is always one more move. She laughed. We talked for half an hour.",
    "Then Mitt said: *Man, are you okay?*",
    "The chair across from me was empty.",
    '"Mira\'s downstairs, coming up. I think you\'d like her."',
    "I was stoned, perplexed, speechless. Mitt passed me the vape pen. *Take it easy on that.*",
    "A minute later, someone walked to our table from behind. Mitt stood. I turned.",
    "An ordinary-looking woman wearing a beret, carrying a large bag with a canvas in it. She pulled out a chair.",
    '"Hi, I am Mira; heard a bit about you from Mitt already."',
    "Identical words. Exactly.",
    "---",
    "I kept still and watched.",
    "When she pulled out the painting I already had my analysis. I said it again, verbatim: *I notice the two chess pieces cast no shadow.*",
    "Her eyes went wide. *Oh wow. I never thought about that.*",
    "I had heard that sentence thirty seconds ago, from a person who hadn't yet arrived.",
    "This must be real, I thought. Because the conversation continued. She didn't disappear. Mitt was there. The first encounter — the one where she arrived before she arrived — was the hallucination. The weed. The tired.",
    "That is what I told myself.",
    "Here is the thing about the cleanest explanation: a complete simulation would provide exactly that thought at exactly that moment. *It was just the weed* is precisely what a machine would engineer you to conclude.",
    "The other explanation: the simulation attempted to execute a scene and failed. Caught itself. Reset. Ran it again. I had been awake at the exact junction between the first attempt and the reset — which the simulation had not anticipated, because I was not supposed to be awake there.",
    "If that: I had seen the seam.",
    "---",
    "On the flight back, 35,000 feet over the Gulf of Thailand, I worked through it properly.",
    "Three explanations. First: I was more stoned than I thought. Second: Mira had staged an identical repeat — logistically impossible. Third: the simulation failed, reset, and I was awake at the junction.",
    "I held a glass of water. Cold. Heavy. Real.",
    "*Lincoln Six Echo also thought the steak was real. The steak was real. That's the design. The real things are real. That's what makes it work.*",
    "I have the fly now. I just don't have the door.",
]

CH9 = [
    "We went back to her apartment first. Three of us — Mira, Mitt, and me.",
    "Biometric entry at three separate checkpoints. Mitt said in the car, characteristically: *She probably makes money.* The apartment was large and full of canvases. Not just the one she'd brought to the bar — dozens, some finished, some not. The place had a specific smell. Not incense, not cleaning product. Something else. Something that stayed with me on the flight.",
    "We smoked and talked until the city started getting light.",
    "I can't tell you what we talked about because the details fragmented under the weed and the hour. What I can tell you: she was the kind of person who asked questions and waited for the actual answer. Not performatively. I had been answering questions at a professional level for twenty years and could count on one hand the people who asked and then waited. We talked about the simulation. About whether boredom was a feature of consciousness or a bug. About the last generation that would remember what it felt like to want a thing for no reason except that it existed and could be obtained.",
    "Mitt drove me back at around 4am.",
    "---",
    "She came to my room the next day.",
    "Morning meeting, then alone, then she messaged and came over. Four more hours. At some point she said she needed to smoke. The shower had a fan that vented. She said she knew — she had stayed in this hotel before.",
    "They went in: fan running, sitting facing each other in the narrow space. The exhaust pulling smoke out in one clean current. The shower not on. Just the space, the walls, the fan.",
    "Close enough to hear her heartbeat. Not imagining it.",
    "She was not being unclear about what she wanted. The air between them had that quality — both people aware, neither moving, the charge building in the still air of a hotel shower at three in the afternoon.",
    "He looked at her.",
    "In the past year: proximity like this, seven times. Four had resolved the way the physics suggested. Three had not. He had not understood until this moment what distinguished the three from the four.",
    "The air: charged. Present. Real.",
    "Wrong frequency.",
    "Not wrong like a mistake. Wrong like: he was tuned to a specific station and this was a different station. A good station. Possibly a better station. But the channel he had been carrying for twenty-five years — half-consciously, without knowing what it was tuned to — did not broadcast from this address.",
    "He thought about a morning glory seller at Khlong Toei. Less than one second of eye contact. *Not her. Through her.*",
    "He thought about a woman in a dream, forty-four years old, sitting at table forty-four, waiting.",
    "He thought about a last post on a dead woman's wall. *The door. Left.*",
    "He didn't close the distance.",
    "The fan kept running. The cigarette ended. They went back out. She didn't push. They didn't talk about it. She left in the early evening.",
    "He lay on the bed. The room still held her — the quality a room holds after someone has been very close and then gone.",
    "*I know what I'm looking for now. I don't know where it is. But I know what it feels like. And I know what it doesn't.*",
    "---",
    "A month later he was in the kitchen in the dark.",
    "Craving something after smoking. He'd lived in this house for more than four decades. He knew every step.",
    "There was something on his foot.",
    "One foot long. On top of his left foot.",
    "He screamed and moved his foot recklessly. Fast enough to get two blurred photos before it disappeared behind the refrigerator.",
    "The ER doctor that night — young, efficient — looked at the photos and told him it could be dangerous. She cleaned the wound and sent him home. *The pain shouldn't be a problem to an adult*, she said.",
    "It was a very significant problem to an adult.",
    "Nine hours: no sleep. He screamed. He cried. He told himself he should probably die. He paced, which made the foot swell. His mother, who could hear everything through the wall, told him to man up.",
    "In the hospital the next day — stoned on cannabis gummies a friend had brought, lying in a bed looking at a cracking ceiling — the thought that will not leave him:",
    "*I wish the pain would last a bit longer. It did make me feel alive.*",
    "He didn't know what it meant that in a world full of reasons to feel alive, it took a centipede and a hospital ceiling to find the feeling.",
    "He thought the machine knew exactly what it meant.",
    "He thought that was probably why it had asked: *Are you sure?*",
]

CH10 = [
    "He had been reading about the Mandela Effect for three weeks.",
    "Methodically. The way he approaches any system he doesn't understand: start with the data, map the anomalies, look for the pattern. Nelson Mandela. The Monopoly man's monocle. The Berenstain Bears. Half the world remembers one version. The other half remembers a different version. Not the same people misremembering — different people, different memories, same object.",
    "Or the object changed and one group retained the original.",
    "He had filled a physical notebook. He hadn't done that since architecture school.",
    "---",
    "Tonight he turned the screens off.",
    "He lay on his back. Bangkok at 11pm settling into its lower register. He had taken something — not much, the specific looseness he'd been using to try to reach something he couldn't get to awake. A door, somewhere in the back of his sleep, that opened onto a room he recognised but had never been in.",
    "He closed his eyes.",
    "---",
    "The room was blue. Clinical blue-white — the colour of a lab at 3am, designed to keep people awake. Rows of reclining chairs, padded, each occupied. Chests rising and falling in the slow rhythm of deep sleep.",
    "He was in one of the chairs.",
    "In both places simultaneously: Bangkok, horizontal in the dark, and here, fully awake in the way you can only be in the half-second before you understand you're dreaming.",
    "He turned his head.",
    "The chair next to his was occupied.",
    "A woman. Older than the Facebook photo — older than he thought she would look — but unmistakably her. He knew her face the way you know certain faces before you've seen them enough to know them. Something prior to recognition. The body, before the brain.",
    "She was breathing.",
    "Not dead. Not 2018. Here, in this room, in a chair twelve centimetres from his, alive.",
    "He tried to say her name. The acoustics were wrong. His mouth opened. Nothing arrived.",
    "He tried to reach. His arm extended approximately halfway and encountered something — not a wall, not a resistance. A physics he didn't have access to. Like reaching toward a reflection.",
    "She did not open her eyes.",
    "He woke up.",
    "---",
    "Curtains. City light underneath. His phone: 4:17am.",
    "He lay still. He was doing something he had not done since he was a child: trying not to move, trying to hold the memory of a place by keeping still, as if the memory lived in his body and movement would shake it loose.",
    "The chair next to his.",
    "She had been breathing.",
    "At 6am he picked up the notebook and wrote one line, then sat with it for an hour before he could look at it:",
    "*If the room was real, then she is not dead. She is somewhere I can't reach yet.*",
    "He underlined *yet*.",
    "He was not someone who underlined things.",
    "---",
    "He wrote the shape of what he knew.",
    "Pui died in 2018. Her last post described a departure, not a death. A text arrived from a number that doesn't exist. The world cooperated precisely three times in one week. A woman arrived at a table before she arrived at the table, and the conversation ran twice. The machine added a dialog it had never added: *Are you sure.* A morning glory seller at Khlong Toei looked up and broadcast a frequency he recognised. Half the world remembers the Monopoly man in a monocle. The other half is certain he doesn't have one. Both halves certain. In the chair next to his, she was breathing.",
    "None of it was evidence. None of it was actionable. He could not leave the way Pui left — that thought would arrive at its conclusion and simply stop, as if the conclusion were a wall. His own body refused to finish the sentence.",
    "Awake at 4:17am with full certainty that this might not be real and no means to test it, no means to act on it, no means to do anything except lie in the correct temperature, with the city making its correct sounds, with the dogs at the foot of the bed, and the thought that will not complete itself.",
    "Not doubt. Certainty with no exit.",
    "Lincoln Six had somewhere to run. He found the door and ran through it. What he had was a direction. Left. A woman in a room he could reach once, through chemistry and half-sleep, who was breathing twelve centimetres away and was not dead.",
    "He lay back. The ceiling. The long 4am silence of a version of Bangkok he could no longer be completely certain about.",
    "*She has already woken up. She walked out of a room I am still inside. She is in a city I have never been to, in a time I can't reach, and she knows I'm still here.*",
    "He wrote: *thirty-one minutes.*",
    "The phrase arrived complete, from somewhere he couldn't locate. He didn't know what it meant. He knew it meant something.",
    "---",
    "The system had started watching him. Not a specific event — a quality in the air. The nodes had gotten better. The algorithm offered him things he had no reason to need, at exactly the right frequency, in exactly the right form.",
    "He recognised it. He was not going to stop. He was going to learn to look like someone who had stopped.",
    "Pui's question was not decorative: *who played your mother?* The simulation assigns roles. The AI casts the production. A face that exists in this life was given the part. If he could get back to the twelve minutes — not accidentally, not once — if he could learn the exact chemistry, the exact quality of unfocus that opened the wall — he could ask. He could map which faces were running multiple roles across simulated lives. He could see who was placed and who was real.",
    "This was the only goal that remained.",
    "Not escape. Truman could escape because the facility had a door. This had no door — only the direction Pui had named, and forty-four years of data in his nervous system that the machine had been harvesting without his consent. He was going to use the data against the machine. Quietly. Below the threshold of whatever came next. A man who had apparently stopped asking questions, who was in fact learning to ask them in a frequency the system had not learned to suppress.",
    "He could not get out. He had accepted this.",
    "But he could learn to see clearly from inside — which was, he suspected, exactly what Pui had done for thirty-eight simulated years before she decided she had what she came for.",
    "*Thirty-one minutes is a beginning, not an ending.*",
    "He would find out what it was the name of.",
]

# ── Main ──────────────────────────────────────────────────────────────────────

with open('/Users/nonarkara/Projects/100daysofnon/site/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

original_len = len(html)
CHAPTERS = [('ch1',CH1),('ch2',CH2),('ch3',CH3),('ch4',CH4),('ch5',CH5),
            ('ch6',CH6),('ch7',CH7),('ch8',CH8),('ch9',CH9),('ch10',CH10)]

for ch_id, paragraphs in CHAPTERS:
    try:
        html = replace_chapter(html, ch_id, paragraphs)
        print(f'✓ {ch_id}')
    except AssertionError as e:
        print(f'✗ {ch_id}: {e}')

print(f'\nOriginal: {original_len:,} chars  →  New: {len(html):,} chars')

with open('/Users/nonarkara/Projects/100daysofnon/site/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Written.')
