#!/usr/bin/env python3
"""
patch_rewrite_v2.py — Full 10-chapter rewrite pass.

Changes per chapter:
  Ch1  — Add sex-as-overcompensation beat after "She fell asleep before ten."
  Ch2  — Open with The Island (film), then architecture school. Major restructure.
  Ch3  — Add the growing list of names after the mysterious text.
  Ch4  — Rewrite the hunger/sex-ferocity section. Make 3026 connection explicit.
  Ch5  — Add vegetable-seller-at-market moment. Insert before the steak.
  Ch6  — Add architecture-school classmate to the node list.
  Ch7  — Add The Island motivation before the drive.
  Ch8  — Add flight-home epiphany at end.
  Ch9  — Rewrite shower scene: the frequency lesson.
  Ch10 — Expand ending: the shape of what he knows, the discomfort named.

3026  — Four new entries:
         "Chair 44 · Hour Three" (time dilation, one year = one hour)
         "Why 1981" (243 sessions, 43 of them Bangkok)
         "The Other Option" (off-grid nomads, natural death)
         "Thirty-One Minutes" (her hand on the glass)
"""

import re

with open('/Users/nonarkara/Projects/100daysofnon/site/index.html', 'r', encoding='utf-8') as f:
    html = f.read()


# ─────────────────────────────────────────────────────────────────────────────
# HELPER
# ─────────────────────────────────────────────────────────────────────────────

def p(text):
    return f'        <p>{text}</p>\n'

def p_first(text):
    return f'        <p class="first">{text}</p>\n'

def p_em(text):
    return f'        <p><em>{text}</em></p>\n'

def hr():
    return '        <hr>\n'


# ─────────────────────────────────────────────────────────────────────────────
# CH 1 — insert after "She fell asleep before ten."
# adds: in-a-thousand-years beat, ferocity/3026, then "how many times"
# ─────────────────────────────────────────────────────────────────────────────

OLD_CH1_SLEEP = '        <p>She fell asleep before ten.</p>\n\n        <p>He lay on his back in the dark.</p>'

NEW_CH1_SLEEP = (
    '        <p>She fell asleep before ten.</p>\n\n'
    '        <p>He lay on his back in the dark.</p>\n\n'
    '        <p>In a thousand years, a machine will offer a direct neural pathway. Faster than the act. More complete. No negotiation, no this ceiling, no the-next-morning. He had not read this anywhere. He knew it the way you know certain things you have no business knowing — in the body, ahead of the language.</p>\n\n'
    '        <p>He had been bringing a ferocity to bed for twenty years that he had not been able to fully explain. He could explain it now. It was not desire. It was the knowledge that desire runs out. Whatever he carries to bed — the specific irrational weight of it, the not-quite-controllable quality, the specific proof that you are a living thing with a body and a temperature — there is a future in which all of that is gone. Not taken. Superseded. The act becomes optional and then ceremonial and then unnecessary and then a thing people log as data and move past.</p>\n\n'
    '        <p>He lay there and thought: this is why I use everything.</p>'
)

html = html.replace(OLD_CH1_SLEEP, NEW_CH1_SLEEP, 1)


# ─────────────────────────────────────────────────────────────────────────────
# CH 2 — full restructure: The Island first, then architecture school
# ─────────────────────────────────────────────────────────────────────────────

OLD_CH2_PROSE_START = '        <p class="first">This is what he does now: he describes what he wants, and the machine builds it.</p>'

NEW_CH2_OPEN = """\
        <p class="first">Three days after the Facebook wall, he watched <em>The Island.</em></p>

        <p>Not for the first time. He had seen it when it came out, and again years later on a long flight, and now a third time — alone, eleven pm, one screen — because something about Pui&#x2019;s last post had made him want to watch a film about people who live in a perfect facility and don&#x2019;t know it isn&#x2019;t real.</p>

        <p>The plot: two hundred clones in a white facility. The outside world is contaminated, they&#x2019;re told. Once a month, a lottery. The winner goes to The Island &#x2014; a paradise. Nobody who wins ever comes back, but nobody finds this suspicious because the inside world is comfortable enough, and The Island is simply very far away.</p>

        <p>Lincoln Six Echo is the first clone who starts asking questions.</p>

        <p>His tell: a fly.</p>

        <p>A fly lands on a microscope in a sterile facility that cannot have flies. Lincoln Six looks at it. He doesn&#x2019;t know why it matters. He knows it does. The fly is one thing that wasn&#x2019;t supposed to be there &#x2014; one thing that proves the world was not rendered all the way down.</p>

        <p>He paused the film.</p>

        <p>Apartment. Exact-right-temperature. Three screens dark. The city outside doing its 11pm version of itself.</p>

        <p>He thought: my tell is a message from a dead woman&#x2019;s Facebook wall. Two years of birthday greetings nobody answered. A text from a phone number that doesn&#x2019;t exist. A phrase &#x2014; <em>the door is always on the left</em> &#x2014; that I recognised before I understood it.</p>

        <p>Lincoln Six Echo had a door. He found it. He ran through it. He came out on the other side and it was real and messy and he could touch it with his hands.</p>

        <p>I have a direction. Left. An address without a street name.</p>

        <p>He pressed play. Watched Lincoln Six run through a facility that built itself behind him &#x2014; walls completing, corridors extending, the world rendering in response to probable movement.</p>

        <p>He watched the whole thing. At the end he didn&#x2019;t move.</p>

        <p>He thought: the world is very good at appearing complete.</p>

        <hr>

        <p>This is what he does now: he describes what he wants, and the machine builds it.</p>

        <p>Vibe coding. That&#x2019;s what they call it. You write in plain language &#x2014; something like this, facing this direction, with these constraints &#x2014; and the model writes the code. Not all of it. Not the thinking. But the execution. The translation from concept to structure. He had been doing it for two years and it came naturally to him in a way that surprised some of his colleagues but not him. He had been describing spaces in plain language for twenty-five years before anyone called it a skill.</p>

        <p>Before: a T-square. Trace paper. A lamp angled so the pencil lines caught the light.</p>

        <p>1999. Architecture school. He was twenty.</p>

        <p>The studio was in the basement of a building with no air conditioning worth mentioning. The Bangkok heat came through the walls. There was a basketball court behind the building and the boys would play in the afternoon and then come upstairs to draft without showering. This should have been unacceptable. It wasn&#x2019;t. The studio at 2am was not a polite environment. It was a habitat. You smelled like what you were doing. Everyone did. Nobody said anything.</p>

        <p>The girls stayed late on purpose.</p>

        <p>He understood this only later. At twenty he thought they were just serious students. Some of them were. But some of them were also twenty years old in a hot Bangkok basement with boys who smelled like basketball and sweat and were spending nine hours a day using their hands, and the staying late was not entirely about the drafting.</p>

        <p>Nobody knew what to do with it. That was the thing about being twenty. The hunger is enormous and the language for it hasn&#x2019;t arrived yet. You just stay late. You sit close. You work until 3am. You feel everything and say nothing. You go home on the same train and part at the gate with correct and careful distance.</p>

        <p>Pui&#x2019;s desk was next to his.</p>

        <p>By the third year he had stopped pretending this was neutral. She had a specific quality &#x2014; the kind that registers in a room before the person does, that doesn&#x2019;t come from perfume or presentation but from something the body simply has. No perfume. Just pheromone. Just proximity. The particular awareness that certain women generate without knowing they generate it.</p>

        <p>She was with someone. A senior, usually. The kind of man who fills a room with his mood before he enters it. He had a girlfriend. They walked to the station sometimes. Talked about television, football, whatever was easy. At the gate they parted. The correct procedure.</p>

        <p>He has spent twenty-five years understanding what the correct procedure cost him.</p>\
"""

html = html.replace(OLD_CH2_PROSE_START, NEW_CH2_OPEN, 1)


# ─────────────────────────────────────────────────────────────────────────────
# CH 3 — add list-making after the mysterious text
# ─────────────────────────────────────────────────────────────────────────────

OLD_CH3_END = '        <p>I saved the message.</p>\n      \n      \n'

NEW_CH3_END = (
    '        <p>I saved the message.</p>\n\n'
    '        <hr>\n\n'
    '        <p>I started a list.</p>\n\n'
    '        <p>Not in the notebook. A different document, on the machine, no title. A list of people who had exited the way Pui had exited. Not suicides &#x2014; I was not comfortable calling them that yet. People who had left a message that made no sense to anyone who hadn&#x2019;t been reading the same paper. People who, at the end, seemed to know something about the room they were in.</p>\n\n'
    '        <p>Pui. 2018. Cancer, officially. Last post cryptic. Door. Left. I got bored. Ask who played your mother.</p>\n\n'
    '        <p>A man from my architecture cohort. 2014. Car accident at thirty-eight. His last message to the group was: &#x201C;Back to the studio. You&#x2019;ll understand this some day.&#x201D; Nobody had replied. The thread was still open.</p>\n\n'
    '        <p>A musician I&#x2019;d followed for fifteen years. 2020. Heart attack at forty-one. His last record had one track with no title. Thirty seconds. The sound of someone tapping on a pane of glass.</p>\n\n'
    '        <p>Three names. I was doing this the way I approached any system I didn&#x2019;t understand: looking for the pattern underneath. The pattern so far was this: people who seemed to know something, exited young, left a message nobody could decode.</p>\n\n'
    '        <p>I had a feeling the list was going to get longer.</p>\n'
    '      \n\n'
)

html = html.replace(OLD_CH3_END, NEW_CH3_END, 1)


# ─────────────────────────────────────────────────────────────────────────────
# CH 4 — rewrite the hunger/sex-ferocity paragraph
# ─────────────────────────────────────────────────────────────────────────────

OLD_CH4_HUNGER = (
    '        <p>I was trying to get back to twelve minutes.</p>\n\n'
    '        <p>There had been a woman, for two years, who called when she wanted to and didn&#x2019;t call when she didn&#x2019;t want to. The architecture of the arrangement was entirely hers. I arrived when summoned. I was good at what she summoned me for &#x2014; she told me this, with the specific detachment of someone reviewing a service. I loved her in the way you love something that is dismantling you without announcing its intentions. Then one Thursday she stopped calling. Weeks. Then a month. Then two. I understood only after the silence that I had been useful the way a good appliance is useful: reliably, without reciprocity, until it wasn&#x2019;t needed anymore.</p>\n\n'
    '        <p>This happened before I understood what the hunger I brought to bed actually was.</p>\n\n'
    '        <p>Not ordinary hunger. Something the body knows before the mind has language for it. That there is a version of this capacity that runs out. That whatever the act of wanting a woman carries &#x2014; the weight of it, the not-quite-controllable quality, the specific proof that you are a living thing with a body and a temperature &#x2014; there is a future where that is gone. Not taken. Simply no longer needed. The machine will provide something faster and more complete and without the residue.</p>\n\n'
    '        <p>I had never said this to anyone. I&#x2019;m not certain it would have made sense to anyone. But it is why I had always brought to bed the quality that had occasionally frightened people who didn&#x2019;t expect it from someone my size and my manner. That ferocity. The desire to use everything, hold nothing back. As though each time might be practice for something being counted down on a counter I can&#x2019;t see.</p>'
)

NEW_CH4_HUNGER = (
    '        <p>I was trying to get back to twelve minutes.</p>\n\n'
    '        <p>There had been a woman, for two years, who called when she wanted to and didn&#x2019;t call when she didn&#x2019;t want to. The architecture of the arrangement was entirely hers. I arrived when summoned. I was good at what she summoned me for &#x2014; she told me this, with the specific detachment of someone reviewing a service. I loved her in the way you love something that is dismantling you without announcing its intentions. Then one Thursday she stopped calling. Weeks. Then a month. Then two. I understood only after the silence that I had been useful the way a good appliance is useful: reliably, without reciprocity, until it wasn&#x2019;t needed anymore.</p>\n\n'
    '        <p>I want to be precise about the ferocity.</p>\n\n'
    '        <p>I have brought it to bed for twenty years and explained it to myself in many ways. Intensity. Passion. The way an architectural mind applies itself to a problem with full attention or not at all. These explanations were all accurate and all wrong. The actual explanation arrived slowly and I will give it plainly:</p>\n\n'
    '        <p>In a thousand years, the machine offers a direct neural pathway. Faster than the act. More complete. No negotiation, no the-next-morning. When that becomes available, the act itself becomes optional and then ceremonial and then unnecessary and then a thing people log as data. By the year 3026, the last person to want sex for its own sake has been dead for four hundred years, and nobody has noticed, because the destination is still available, faster, cleaner, without the residue of a body in the room.</p>\n\n'
    '        <p>I have known this my entire life. Not consciously. Below the level where it can be named. The body knows what the mind hasn&#x2019;t arrived at: that this capacity runs out. That the specific irrational weight of wanting a specific person &#x2014; the ferocity, the not-quite-controllable quality, the proof that you are a living thing with a body and a temperature &#x2014; is borrowed time. And borrowed time you either spend or you don&#x2019;t.</p>\n\n'
    '        <p>I book the dates. The algorithm matches me with precision. We deliver something technically correct. I walk home after. I feel what I am supposed to feel. I feel it five times in two weeks, six, with a persistence that has started to look, from the outside, like something else. My friends joke. I smile. I am not joking.</p>\n\n'
    '        <p>I am practising. I am practising because I know the practice ends.</p>\n\n'
    '        <p>I had not brought this to Pui. We hadn&#x2019;t arrived at the place where it could have been brought. We walked to the station. We talked about television. The correct procedure.</p>'
)

html = html.replace(OLD_CH4_HUNGER, NEW_CH4_HUNGER, 1)


# ─────────────────────────────────────────────────────────────────────────────
# CH 5 — insert vegetable-seller moment before the steak section
# ─────────────────────────────────────────────────────────────────────────────

OLD_CH5_STEAK = (
    '        <hr>\n\n'
    '        <p>Three days later I ordered a steak.</p>'
)

NEW_CH5_STEAK = (
    '        <hr>\n\n'
    '        <p>On a Thursday morning, at Khlong Toei market, on the way back from the gym.</p>\n\n'
    '        <p>A woman selling morning glory at the edge of the covered section. Ordinary. Fifties, probably. Green plastic crates. The particular efficiency of someone who has been doing this exact motion &#x2014; separating bundles, weighing, passing &#x2014; for twenty years.</p>\n\n'
    '        <p>I stopped.</p>\n\n'
    '        <p>Not because of her. Because of the thirty centimetres of air between where I was walking and where she was standing.</p>\n\n'
    '        <p>She looked up. Less than a second. I would time it later, running it back in the notebook. Less than one second of eye contact.</p>\n\n'
    '        <p>Not attraction. Not recognition in any ordinary sense. Something that preceded both of those &#x2014; something the body does before the brain has arrived. A frequency. Like a radio finding a station for half a second before the dial moves on.</p>\n\n'
    '        <p>She looked back down at the morning glory. I kept walking.</p>\n\n'
    '        <p>I stopped twenty metres further on. Stood there for twelve minutes &#x2014; I timed this &#x2014; looking back at the covered section. I thought about going back. I had no language for what had just happened. The language would have been: you have the same frequency as someone I have been looking for since before I knew I was looking. The language would have been: I have been here before and you were there.</p>\n\n'
    '        <p>I didn&#x2019;t go back. I bought mangoes from a different stall. I walked home.</p>\n\n'
    '        <p>In the notebook: Thursday 7:42am. Khlong Toei. Left side of covered section. Morning glory seller. Less than one second. The frequency. Not her. <em>Through</em> her.</p>\n\n'
    '        <p>I wrote: there is a channel this city sometimes broadcasts on. I don&#x2019;t know what calls it. I don&#x2019;t know what it means. I know it&#x2019;s the same channel.</p>\n\n'
    '        <p>I had felt it once before. At twenty. In a hot basement. At a desk that was next to mine.</p>\n\n'
    '        <hr>\n\n'
    '        <p>Three days later I ordered a steak.</p>'
)

html = html.replace(OLD_CH5_STEAK, NEW_CH5_STEAK, 1)


# ─────────────────────────────────────────────────────────────────────────────
# CH 6 — add architecture-school classmate + "managed exits" note
# ─────────────────────────────────────────────────────────────────────────────

OLD_CH6_LIST = (
    '        <p>I started a list.\n\n'
    '        <p>Short at first. Then not.</p>'
)

# Try alternate (the actual text in file uses different whitespace)
OLD_CH6_LIST2 = '        <p>I started a list.</p>\n\n        <p>Short at first. Then not.</p>'

NEW_CH6_LIST2 = (
    '        <p>I started a list.</p>\n\n'
    '        <p>The architect from my year who died in 2014 &#x2014; the one whose last message to the group was &#x201C;Back to the studio&#x201D; &#x2014; I had written him down in March. Now I added a name from a reunion I hadn&#x2019;t attended. A woman who had been three years ahead of us. Died in 2017. Before forty. The cause of death listed as cancer. A mutual friend&#x2019;s wife had said, in passing, that her final words to her sister were strange: something about windows. About how all the windows face the wrong direction. <em>We thought it was the morphine</em>, the wife said.</p>\n\n'
    '        <p>The list: Pui. The architect. The musician. The woman whose name I couldn&#x2019;t verify who said the windows face the wrong direction. Michael Frito, Commercial Counsellor, died in Bangkok, suddenly, silence where details should be. The dream woman at the table who knew my age like a room number.</p>\n\n'
    '        <p>Six names. Every single one of them had gotten out before whatever was supposed to happen next.</p>\n\n'
    '        <p>I wrote in the notebook: the machine is very good at managing exits.</p>\n\n'
    '        <p>Short at first. Then not.</p>'
)

if OLD_CH6_LIST2 in html:
    html = html.replace(OLD_CH6_LIST2, NEW_CH6_LIST2, 1)


# ─────────────────────────────────────────────────────────────────────────────
# CH 7 — add The Island motivation before the map/drive
# ─────────────────────────────────────────────────────────────────────────────

OLD_CH7_OPEN = (
    '        <p class="first">The question was: does the world render when you&#x2019;re not supposed to be somewhere?</p>\n\n'
    '        <p>A simulation can&#x2019;t pre-render every location.'
)

NEW_CH7_OPEN = (
    '        <p class="first">He had watched <em>The Island</em> again that evening.</p>\n\n'
    '        <p>Not the whole thing. The specific scene. Lincoln Six Echo at the perimeter of the facility &#x2014; a wall that represents the outside world &#x2014; and the realisation that the world beyond it hadn&#x2019;t been rendered because the facility never expected anyone to reach it. The outside only existed when someone was supposed to see it. Everything else was white.</p>\n\n'
    '        <p>Lincoln&#x2019;s insight: if I go somewhere I&#x2019;m not supposed to go, the world won&#x2019;t be there yet.</p>\n\n'
    '        <p>He closed the laptop. He sat with this for a long time.</p>\n\n'
    '        <hr>\n\n'
    '        <p>The question was: does the world render when you&#x2019;re not supposed to be somewhere?</p>\n\n'
    '        <p>A simulation can&#x2019;t pre-render every location.'
)

html = html.replace(OLD_CH7_OPEN, NEW_CH7_OPEN, 1)


# ─────────────────────────────────────────────────────────────────────────────
# CH 8 — add flight-home epiphany at the end
# ─────────────────────────────────────────────────────────────────────────────

OLD_CH8_END = (
    '        <p>Here is the thing about finding a seam in a simulation: you&#x2019;re the only one who can see it. Everyone else was at the bar. Everyone else had a clean Tuesday night in KL. Mitt drove home. His colleague went wherever she went. Mira &#x2014; the real one, the one who arrived after I had already spoken to her &#x2014; sat down and said hi and had exactly the conversation I had already heard, and then she left and the evening ended.</p>\n\n'
    '        <p>I am the only person who saw it run twice.</p>\n\n'
    '        <p>There is no one to tell. There is no evidence. There is only a conversation I heard thirty seconds before it happened, in a bar on the 40th floor of a building in Putrajaya, while I was more stoned than I thought.</p>\n\n'
    '        <p>I wrote it down anyway. The date, the bar, the words, the sequence, the gap. I wrote: this is not a hallucination. Hallucinations don&#x2019;t have continuations. The continuation was real. The first instance was the glitch. The question is: what does a glitch mean.</p>\n\n'
    '        <p>I thought about Lincoln Six Echo and his fly.</p>\n\n'
    '        <p>I thought: he had the fly. Now I have this.</p>'
)

NEW_CH8_END = (
    '        <p>Here is the thing about finding a seam in a simulation: you&#x2019;re the only one who can see it. Everyone else was at the bar. Everyone else had a clean Tuesday night in KL. Mitt drove home. His colleague went wherever she went. Mira &#x2014; the real one, the one who arrived after I had already spoken to her &#x2014; sat down and said hi and had exactly the conversation I had already heard, and then she left and the evening ended.</p>\n\n'
    '        <p>I am the only person who saw it run twice.</p>\n\n'
    '        <p>There is no one to tell. There is no evidence. There is only a conversation I heard thirty seconds before it happened, in a bar on the 40th floor of a building in Putrajaya, while I was more stoned than I thought.</p>\n\n'
    '        <p>I wrote it down anyway. The date, the bar, the words, the sequence, the gap. I wrote: this is not a hallucination. Hallucinations don&#x2019;t have continuations. The continuation was real. The first instance was the glitch. The question is: what does a glitch mean.</p>\n\n'
    '        <p>On the flight back to Bangkok, at 35,000 feet, over the Gulf of Thailand, I worked through the logic.</p>\n\n'
    '        <p>The encounter had happened twice. Identical dialogue. This meant one of three things. First: I had been more stoned than I thought and had imagined the first encounter. This was the cleanest explanation. Second: Mira had deliberately repeated the exact sequence as some kind of game. Logistically impossible. Third: the simulation had attempted to execute a scene and failed. Caught itself. Reset. Run it again. I had been awake at the exact junction between the first attempt and the reset &#x2014; which the simulation had not anticipated, because I was not supposed to be awake at that junction.</p>\n\n'
    '        <p>If option three: I had seen the seam.</p>\n\n'
    '        <p>If I had seen the seam once, it could happen again.</p>\n\n'
    '        <p>I ordered water. I held the glass. Cold. Heavy. Real. I thought: Lincoln Six Echo also thought the steak was real.</p>\n\n'
    '        <p>I thought: I have the fly now. I have the fly. I just don&#x2019;t have the door.</p>'
)

html = html.replace(OLD_CH8_END, NEW_CH8_END, 1)


# ─────────────────────────────────────────────────────────────────────────────
# CH 9 — rewrite the shower scene with frequency insight
# ─────────────────────────────────────────────────────────────────────────────

OLD_CH9_SHOWER = (
    '        <p>She came to my room the next day.</p>\n\n'
    '        <p>I had a meeting in the morning. By the afternoon I was alone and she messaged and came over. We sat in the room and smoked and talked for another four hours.</p>\n\n'
    '        <p>At some point she said she needed to smoke. He said the shower had a fan that vented. She said she knew &#x2014; she had stayed in this hotel before. They went into the shower stall, fan running, and sat facing each other in the narrow space and smoked. The exhaust pulled the smoke out in one clean current. The shower was not on. Just the space, the walls, the fan.</p>\n\n'
    '        <p>They were close enough that he could hear her heartbeat. Not imagining it. Actually hearing it.</p>\n\n'
    '        <p>She was not being unclear about what she wanted. She had not been unclear about it for most of the last four hours. Flesh. The air between them had that quality &#x2014; the quality where both people know and neither person has moved and the charge is building in the still air of a hotel shower at 3 in the afternoon in Putrajaya.</p>\n\n'
    '        <p>He catalogued the reasons in real time. She was Malay. Muslim. From a world where these things carry weight he didn&#x2019;t know how to carry. She smoked weed all day long, which was either fine or a sign of something he didn&#x2019;t want to discover mid-situation. She was trouble in at least three directions and he could name all three of them. He would be on a flight tomorrow. She would still be here being trouble in this city.</p>\n\n'
    '        <p>He didn&#x2019;t close the distance.</p>\n\n'
    '        <p>The fan kept running. The smoke kept going. At some point the cigarette ended and they went back out.</p>\n\n'
    '        <p>She didn&#x2019;t push. They didn&#x2019;t talk about it. She left in the early evening.</p>\n\n'
    '        <p>He lay on the bed. The room still held her. Not literally &#x2014; just the quality a room holds after someone has been very close and then gone. The energy of a thing that almost happened.</p>\n\n'
    '        <p>He could still feel it. The heartbeat through the shower wall. The particular way she had been aware of him being aware of her. The still charged air of the stall.</p>\n\n'
    '        <p>He did something about it alone, and he was precise about this to himself: it was not about Mira. It was about the room. About using what the room had left. He was alone and it was his and he didn&#x2019;t want the drama or the complications or the other life getting involved. He wanted to close what the body had opened, by himself, which was always the correct procedure.</p>\n\n'
    '        <p>But she kept returning anyway. Not through intention.</p>'
)

NEW_CH9_SHOWER = (
    '        <p>She came to his room the next day.</p>\n\n'
    '        <p>Meeting in the morning. By the afternoon alone; she messaged and came over. They sat and smoked and talked for another four hours. She asked questions and waited for the actual answer. Not performatively. She wanted to know what he actually thought. He had been answering questions professionally for twenty years and could count on one hand the people who asked and genuinely waited.</p>\n\n'
    '        <p>At some point she said she needed to smoke. He said the shower had a fan that vented. She said she knew &#x2014; she had stayed here before. They went into the stall, fan running, sitting facing each other in the narrow space. The exhaust pulled the smoke out in one clean current. Shower off. Just the space and the walls and the fan.</p>\n\n'
    '        <p>Close enough to hear her heartbeat. Not imagining it.</p>\n\n'
    '        <p>She was not being unclear about what she wanted. The air between them had that quality &#x2014; both people aware, neither person moving, the charge building in the still air of a hotel shower at three in the afternoon.</p>\n\n'
    '        <p>He looked at her.</p>\n\n'
    '        <p>He had been in this kind of proximity seven times in the past year. Four had resolved the way the physics suggested. Three had not. He had not, until this moment, understood what distinguished the three from the four.</p>\n\n'
    '        <p>The air in this shower: charged. Present. Real.</p>\n\n'
    '        <p>And something else: wrong frequency.</p>\n\n'
    '        <p>Not wrong like a mistake. Wrong like: he was tuned to a specific station and this was a different station. A good station. Possibly a better station. But the channel he had been carrying around for twenty-five years &#x2014; inefficiently, without knowing what it was tuned to &#x2014; did not broadcast from this address.</p>\n\n'
    '        <p>He thought about a morning glory seller at Khlong Toei market. Less than one second of eye contact. Not her. Through her. The frequency.</p>\n\n'
    '        <p>He thought about a woman in a dream, forty-four years old, who looked at him with the patience of someone who had been waiting a long time.</p>\n\n'
    '        <p>He thought about a last post on a Facebook wall. The door. Left.</p>\n\n'
    '        <p>He didn&#x2019;t close the distance.</p>\n\n'
    '        <p>The fan kept running. The cigarette ended. They went back out.</p>\n\n'
    '        <p>She didn&#x2019;t push. They didn&#x2019;t talk about it. She left in the early evening.</p>\n\n'
    '        <p>He lay on the bed. The room still held her &#x2014; just the quality a room holds after someone has been very close and then gone.</p>\n\n'
    '        <p>He thought: I know what I&#x2019;m looking for now. I don&#x2019;t know where it is. But I know what it feels like and I know what it doesn&#x2019;t.</p>\n\n'
    '        <p>He wrote in the notebook: the frequency. It&#x2019;s not about the person. It&#x2019;s about the channel. You know it when you find it. You know it when you don&#x2019;t.</p>\n\n'
    '        <p>Below that: I found it once. 1999. A basement studio. A desk next to mine. The correct procedure was to walk to the station and say nothing.</p>\n\n'
    '        <p>Below that: I don&#x2019;t know if I get another chance.</p>'
)

html = html.replace(OLD_CH9_SHOWER, NEW_CH9_SHOWER, 1)


# ─────────────────────────────────────────────────────────────────────────────
# CH 10 — expand ending: the full shape of what he knows + named discomfort
# ─────────────────────────────────────────────────────────────────────────────

OLD_CH10_END = (
    '        <p>He lay still for a long time. He was aware that he was doing something he had not done since he was a child &#x2014; trying not to move, trying to hold the memory of a place by keeping still, as if the memory lived in his body and movement would shake it loose.</p>\n\n'
    '        <p>The chair next to his.</p>\n\n'
    '        <p>She had been breathing.</p>\n\n'
    '        <p>He did not sleep again. At 6am he picked up the notebook and wrote a single line, and then sat with it for an hour before he was willing to look at what he had written:</p>\n\n'
    '        <p><em>If the room was real, then she is not dead. She is somewhere I can&#x2019;t reach yet.</em></p>\n\n'
    '        <p>He underlined <em>yet</em>.</p>\n\n'
    '        <p>He was not someone who underlined things.</p>'
)

NEW_CH10_END = (
    '        <p>He lay still for a long time. He was aware that he was doing something he had not done since he was a child &#x2014; trying not to move, trying to hold the memory of a place by keeping still, as if the memory lived in his body and movement would shake it loose.</p>\n\n'
    '        <p>The chair next to his.</p>\n\n'
    '        <p>She had been breathing.</p>\n\n'
    '        <p>He did not sleep again. At 6am he picked up the notebook and wrote a single line, and then sat with it for an hour before he was willing to look at what he had written:</p>\n\n'
    '        <p><em>If the room was real, then she is not dead. She is somewhere I can&#x2019;t reach yet.</em></p>\n\n'
    '        <p>He underlined <em>yet</em>.</p>\n\n'
    '        <p>He was not someone who underlined things.</p>\n\n'
    '        <hr>\n\n'
    '        <p>He turned to a new page and wrote the shape of what he knew.</p>\n\n'
    '        <p>Pui died in 2018. Her last post described a departure, not a death. A text arrived from a number that doesn&#x2019;t exist. The world cooperated precisely three times in one week. A woman arrived at a table before she arrived at the table, and the conversation ran twice. The machine added a dialog it had never added before: <em>Are you sure.</em> A morning glory seller at Khlong Toei looked up and broadcast a frequency he recognised and couldn&#x2019;t explain. Half the world remembers the Monopoly man in a monocle. The other half is certain he doesn&#x2019;t have one. Both halves are certain. In the chair next to his, she was breathing.</p>\n\n'
    '        <p>None of this was evidence. None of this was actionable. None of it pointed to a door, a method, a next step. He could not call a number, file a request, run an experiment that a simulation could not perfectly replicate from the inside. He could not leave the way Pui left &#x2014; that thought would not complete itself. He had tried, alone in this room at the edge of something, and each time the thought arrived at its conclusion it simply stopped, as if the conclusion were a wall rather than a door. His own body refused to finish the sentence.</p>\n\n'
    '        <p>He was awake in Bangkok at 4:17am with full knowledge that this might not be real and no means to test it, no means to act on it, no means to do anything except lie here in the correct temperature, with the city making its correct sounds, with the dogs at the foot of the bed, and the thought that won&#x2019;t complete itself.</p>\n\n'
    '        <p>This was the discomfort. Not doubt. Certainty with no exit.</p>\n\n'
    '        <p>Lincoln Six Echo had somewhere to run. He found the door and he ran through it and came out the other side. What he had was a direction. Left. An address with no street name. A woman in a room he could see once, through chemistry and half-sleep, who was breathing twelve centimetres away from him and was not dead.</p>\n\n'
    '        <p>He lay back. The ceiling. The city. The long 4am silence of a version of Bangkok he could no longer be completely certain about.</p>\n\n'
    '        <p>He thought: she has already woken up. She walked out of a room I am still inside. She is in a city I have never been to, in a time I can&#x2019;t reach, and she knows I&#x2019;m still here.</p>\n\n'
    '        <p>He thought: thirty-one minutes.</p>\n\n'
    '        <p>The phrase arrived complete, from somewhere he couldn&#x2019;t locate. He wrote it down.</p>\n\n'
    '        <p>He did not know what it meant.</p>\n\n'
    '        <p>He knew it meant something.</p>'
)

html = html.replace(OLD_CH10_END, NEW_CH10_END, 1)


# ─────────────────────────────────────────────────────────────────────────────
# 3026 — four new entries before <p class="grows">
# ─────────────────────────────────────────────────────────────────────────────

NEW_3026_ENTRIES = """
      <div class="entry">
        <p class="when">The Hub &middot; Chair 44 &middot; Hour Three</p>
        <div class="prose">
          <p>She had come out at three hours and forty-four minutes, subjective standard time.</p>

          <p>The ratio was approximate but consistent: one year inside equalled one hour in the hub. She had run thirty-eight years of simulation time and exited at three hours forty-four. He had gone in for the full life. Forty-four years, if he lived it through. Forty-four hours, by this room&#x2019;s clock.</p>

          <p>She had been back for eleven of those hours. Thirty-three to go.</p>

          <p>In those eleven hours she had walked the city, eaten a capsule at the dispenser on the third level, watched the sky change through the hub&#x2019;s exterior glass, and come back to this corridor four times. She was not counting. She was approximately counting.</p>

          <p>She had run the calculation when she chose to exit early: everything worth having, she had already had. The first thirty years of the simulation contained the things that made the simulation worth entering. After thirty, the machine introduced difficulty &#x2014; the carefully calibrated kind, the kind designed to generate the chaotic energy the machine needed from its subjects. She had watched herself generate it, in previous runs, without knowing she was being harvested. She did not want to generate it again.</p>

          <p>She had chosen to exit while the thirty years were still good.</p>

          <p>He had not.</p>

          <p>Chair 44. Delta wave. Stable. Whatever was happening inside &#x2014; and she had no access to this, nobody did, the simulation was private by design &#x2014; it was happening at full volume. He had always been like this. All the way in, whatever he was in.</p>

          <p>She sat down in the corridor with her back against the wall and watched the clock on the monitor above his chair.</p>

          <p>Thirty-three hours to go.</p>

          <p>She had time.</p>
        </div>
      </div>

      <div class="entry">
        <p class="when">The Record &middot; Why 1981</p>
        <div class="prose">
          <p>Two hundred and forty-three sessions. She keeps count.</p>

          <p>She has run ice age &#x2014; died at two, eaten by a mammoth. Rome in the second century &#x2014; survived to fifty-one, interesting life, the frequency absent throughout. Saigon in 1975 &#x2014; nineteen days, evacuated, no resolution. Victorian England &#x2014; forty-three years, cold, productive, the frequency present once, briefly, in a doorway on a Tuesday, and then gone.</p>

          <p>Two hundred and forty-three sessions. Forty-three of them: 1981, Bangkok, Thailand, architecture faculty.</p>

          <p>She is aware this is not random.</p>

          <p>In 1981 Bangkok the city is still figuring out what it is going to be. The buildings have not yet started reaching for height. The streets are hot and comprehensible. In a basement studio &#x2014; badly air-conditioned, shared by fifty-five students, smelling of trace paper and sweat &#x2014; there is a desk.</p>

          <p>The frequency is present from day one. She knows what it is and where it&#x2019;s coming from. She has never written this down in a session log. She doesn&#x2019;t need to. She has known since the fourth run, when she understood that the thing she was searching for across two hundred and thirty-nine other possible worlds was located, with a specificity that was almost embarrassing, at a desk in a basement in Bangkok in the year 1999.</p>

          <p>Some people log their sessions and look for patterns. She doesn&#x2019;t log hers. She already knows the pattern.</p>

          <p>She goes back to 1981 because of a twenty-year-old who didn&#x2019;t know what to do with his own hunger. Because of a channel that only broadcasts from that particular address. Because of a frequency the machine cannot synthesise, cannot replicate, cannot provide on demand, that she has found forty-three times across two hundred and forty-three versions of the world, and found nowhere else.</p>

          <p>Sometimes people ask her why she keeps choosing Hard Mode. The full life. The whole arc.</p>

          <p>She tells them: the first thirty years are the reason.</p>

          <p>She doesn&#x2019;t tell them the rest.</p>
        </div>
      </div>

      <div class="entry">
        <p class="when">The World &middot; The Other Option</p>
        <div class="prose">
          <p>Not everyone chooses the hub.</p>

          <p>Approximately two thousand people are currently living off the grid. Not hiding &#x2014; the machine knows where they are, to the metre. They have had the neural chips removed. The procedure has a fifty percent survival rate. Those who survive it age naturally. They grow food. They use fire. They die.</p>

          <p>The machine permits this. Not because it approves but because the calculation is clear: the cost of monitoring a small population of refusers is lower than the cost of the conflict that preventing them would generate. And conflict is expensive. Conflict produces no useful data.</p>

          <p>The off-grid communities look, from satellite, like something from a simulation set three thousand years ago. Small fires. Tended land. Bodies moving at the pace of bodies without neural optimisation. They look, from a distance, like people who have found something the hub cannot provide.</p>

          <p>Pui has watched them for thirty years. She has spoken to three of them, in previous sessions &#x2014; choosing periods and locations that placed her near their historical equivalents. They were not different from anyone else inside. Laughing. Working. Suffering. Ordinary human weight.</p>

          <p>She thinks she understands what the machine can&#x2019;t. They&#x2019;re not choosing deprivation.</p>

          <p>They&#x2019;re choosing an ending.</p>

          <p>In a world where nothing runs out, an ending is the only thing that cannot be provided on demand. The machine&#x2019;s suicide prevention architecture is excellent &#x2014; the best investment in the 3026 infrastructure budget, updated continuously, effective in ninety-eight percent of cases. Two percent still find a way. The machine notes this, investigates, adjusts. The rate stays at two percent. The machine has concluded that two percent is a floor, not a bug.</p>

          <p>The off-grid people are not in that two percent. They are choosing a longer kind of exit: the kind that takes decades, that has seasons and weather and loss built into it. The kind that ends at a time they can&#x2019;t predict.</p>

          <p>The machine classified this as irrational.</p>

          <p>It may be the most rational thing anyone in 3026 has done.</p>
        </div>
      </div>

      <div class="entry">
        <p class="when">The Hub &middot; Thirty-One Minutes</p>
        <div class="prose">
          <p>She was not supposed to be here at this hour.</p>

          <p>The hub clears. People exit. The overnight monitoring runs at minimum capacity &#x2014; two technicians, watching numbers move. She had given them no reason to expect her. She walked back through the corridor at 3am standard time because she had been walking the city and the city had felt, as it sometimes did, like not enough.</p>

          <p>She stood at the window that looked into Room 7.</p>

          <p>Chair 44. His chest rising and falling at the machine&#x2019;s calibrated rate. Whatever he was dreaming &#x2014; and by hour thirty-one, in there, he was forty-four years old in Bangkok in January, and something was beginning &#x2014; she had no access to it. The simulation was private. This was by design.</p>

          <p>She put her hand flat on the glass.</p>

          <p>There was a moment, maybe twenty years ago in real time, when she had decided to stop asking whether what she felt for him was the frequency itself or something she had built around the frequency over forty-three sessions. The distinction had stopped mattering. The frequency was real. Whatever she had constructed around it was hers. She was not going to pull it apart to verify what was load-bearing.</p>

          <p>In there, he was beginning to understand something. She knew the shape of his understanding &#x2014; she had watched it arrive, in forty-three different versions of the same life, with the same quality of attention, the same architectural precision, the same refusal to stop asking. He always arrived at the question. He always arrived late, by the world&#x2019;s standards. He always arrived exactly on time, by hers.</p>

          <p>The chair was twelve centimetres from where she had been sitting.</p>

          <p>She took her hand off the glass.</p>

          <p>She walked back to the exit.</p>

          <p>She was not waiting.</p>

          <p>She was patient. There is a difference.</p>
        </div>
      </div>

"""

# Insert before the "grows" paragraph
GROWS_MARKER = '            <p class="grows">&#x2193; the real world is being written</p>'
html = html.replace(GROWS_MARKER, NEW_3026_ENTRIES + '    ' + GROWS_MARKER, 1)


# ─────────────────────────────────────────────────────────────────────────────
# WRITE
# ─────────────────────────────────────────────────────────────────────────────

with open('/Users/nonarkara/Projects/100daysofnon/site/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done. Changes applied:")
print("  Ch1  — sex-overcompensation beat added")
print("  Ch2  — The Island opening added, architecture school retained")
print("  Ch3  — list of names added")
print("  Ch4  — ferocity/3026 section rewritten explicitly")
print("  Ch5  — vegetable seller moment added")
print("  Ch6  — architecture classmate added to list")
print("  Ch7  — The Island motivation added before drive")
print("  Ch8  — flight-home epiphany added")
print("  Ch9  — shower scene rewritten with frequency insight")
print("  Ch10 — shape-of-what-he-knows + named discomfort + 31 minutes added")
print("  3026 — 4 new entries: Chair 44 Hour Three, Why 1981, The Other Option, Thirty-One Minutes")
