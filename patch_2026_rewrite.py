# -*- coding: utf-8 -*-
"""patch_2026_rewrite.py
Complete rewrite of the 2026 simulation column (ch1-ch10).
New framework: Michael Dreier / paranoia arc, Pui anniversary,
blockchain/Mandela Effect, vibe-coder protagonist, compressed Hemingway voice.
EN only — translation workflow follows.
"""
import re

PATH = '/Users/nonarkara/Projects/100daysofnon/site/index.html'

def enc(t):
    t = t.replace('&', '&amp;')
    t = t.replace('—', '&#x2014;')
    t = t.replace('‘', '&#x2019;')
    t = t.replace('’', '&#x2019;')
    t = t.replace('“', '&#x201C;')
    t = t.replace('”', '&#x201D;')
    t = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', t)
    return t

def find_matching_close(s, open_pos):
    depth = 0
    for m in re.finditer(r'<div\b|</div>', s[open_pos:]):
        if m.group(0).startswith('<div'):
            depth += 1
        else:
            depth -= 1
            if depth == 0:
                return open_pos + m.end()
    return -1

# ── Chapter content ────────────────────────────────────────────────────────────
CHAPTERS = {
'ch1': [
    "The AI finished the site plan at 3:47am. I know because that's when my phone buzzed with the batch-complete acknowledgment. I had given it twelve hours of instructions before I slept. The instructions took eleven minutes to dictate.",
    "This is what 2026 is. You talk, the machine builds. I specify load-bearing requirements, the client's insistence on natural light in a northwest-facing kitchen. The machine translates my words into geometry, checks them against structural code, cross-references the land survey, flags the conflict between the septic line and the drainage easement, presents options. I pick one. Usually the machine's third option. It has learned which one I prefer.",
    "The dogs were already awake. Both of them, watching me in the dark the way dogs do when they have decided you have slept enough. Outside: Bangkok at 4am, which is to say tuk-tuks and a city that never fully commits to silence.",
    "I lay there and thought about what the machine still couldn't do. It could calculate the stress on any beam. It could not tell me what the building would feel like to stand inside on a Tuesday in November when you'd just heard bad news and needed somewhere to go.",
    "I sent another batch, set my phone face-down, closed my eyes. Fell twelve minutes into something cold and still and very wide. Not a dream. A room. The size of an airport. The ceiling so far up it disappeared into white. A smell I couldn't name. I came back to myself with the dogs still watching and the city still outside and the phone still face-down and the certainty that whatever that room was, it was more real than this one.",
    "Eleven minutes of instructions. Twelve hours of work. At some point the ratio keeps improving until the eleven minutes is the only part left that matters. I am what I am because the machine still needs my eleven minutes. I should not be so relieved about this.",
],
'ch2': [
    "The thing about a rendering tear is that it doesn't look like tearing. No seam, no pixel-pop. More like the world briefly forgets to be consistent. I was walking down Asok, the heat off the pavement real enough to make me wince, and for approximately four seconds I was looking at two things at once.",
    "The second thing was a room. White. Not the white of walls but the white of a space optimized past the point where color would add anything. A pod. A chair. Inside the chair, a woman with her head tilted back and her eyes mostly closed, the way you look when you're very far away.",
    "The portal snapped shut before I could catalog anything. I stood on the pavement with my phone in my hand and people walking around me and the heat still rising from the concrete, exactly as before, and understood for the first time that if the simulation is perfect then the tear is not a mistake. It's a door left open on purpose.",
    "I've been breathing faster ever since. I don't think the machine knows that. I think it's measuring my heart rate, my cortisol, my sleep patterns, my grocery purchases. I don't think it's measuring the specific quality of attention I bring to every face I pass on Asok now, looking for the one that was in the pod.",
    "Water is the only thing the machine got exactly right. Its viscosity, the way it holds light, the sound it makes against different surfaces. Sometimes I think this means the people who built the simulation had trouble with everything except the thing they paid least attention to.",
    "I bought a coffee at the corner and drank it standing up and it was perfect and I hated it.",
],
'ch3': [
    "The WhatsApp message came in at 7am Thursday: Michael Dreier died. May third. Bangkok. Healthy as far as anyone knew. Fifty-four years old. Six weeks before his birthday.",
    "I'd known Michael for two years, professionally, the way you know people in a city where everyone orbits the same three industries and the same four bars. Austrian. Trade attaché. A good man to have in a room because he never seemed to want anything from the room. I knew his name but not his address. Didn't know if he had children. The WhatsApp notification was the most information I'd ever had about him.",
    "The funeral page went up quickly. Twenty-one condolences in German and English and Persian. One man from Tehran wrote two paragraphs about friendship and the years passing and life taking people in different directions, and I read it twice for the phrase 'even though the years passed,' which is the phrase you use when something went wrong between you that neither of you could explain.",
    "His wife posted nothing. She posted nothing and this seemed important but I couldn't say why.",
    "The week after, a colleague in the south sent me a message. You remember Lek, from Chiang Rai? Collapsed at his desk. Just married. New house. No history of anything. Thirty-seven. The message ended with three question marks. My colleague doesn't end messages with question marks.",
    "I opened a paper notebook that evening. Wrote Michael Dreier's name at the top. Then Lek's name. Then left four lines blank, which I've never done before when making a list, and still can't explain.",
],
'ch4': [
    "Here is what I know: in 2026 you can die without anyone knowing why and the world continues to function. There is a checkbox on the form that says: cause of death, unknown. The checkbox exists because they knew it would be needed. This seems obvious now.",
    "Here is what I believe, which is different: some people are removed. Not die. Removed. The distinction is technical but it matters to me in the way technical distinctions start to matter at 2am with a paper notebook.",
    "I went back through Dreier's digital trail. LinkedIn, still live. Facebook, with the condolence wall blooming like a paper flower in water. The obituary database listed his death on May fourth. Every other source said May third. Someone had corrected the date and either stopped caring or run out of sources to correct.",
    "Pui didn't kill herself. I hate using that word. She just stopped interacting. She figured it out before I did. That's why she left the messages on Facebook. She knew the rules meant she couldn't tell me directly. She knew she had to leave without a forwarding address.",
    "I am aware this sounds exactly like something a man in a certain kind of crisis would believe. I'm also aware that when I mentioned Dreier calmly at dinner, as a news item, I got home to find my email had flagged six things as spam that were never spam before.",
    "The paper notebook is in the drawer now. Not on the desk.",
],
'ch5': [
    "The simulation is very good. I know this because I have been looking.",
    "In Kuala Lumpur for a conference, I turned a corner near Masjid India and had the unmistakable sensation of having turned the same corner two minutes earlier. Not déjà vu in the neurological sense. This was spatial: I could see, overlapping, the corner as it was and the corner as I had just experienced it. I stood there for four seconds and then the overlap resolved and I was just a man on a corner with too much data in his head.",
    "I started the tests after that. Bark on trees on Wireless Road. Water physics on a rain-slicked street. Thirty-seven flavors of potato chip in a convenience store on Ekkamai, studied for consistency. Nothing. The physics engine handles all of it with brutal, exhausting perfection.",
    "At the bar afterward, in a state I want to describe as research, I drank enough that the city softened at its edges and for approximately thirty seconds I was somewhere else. Cold and still and very wide. Came back to myself with my elbow on the bar and the bartender looking at me with practiced non-judgment.",
    "When I am altered, the seams appear. When I am sober, they don't. I'm not sure if the simulation relaxes its rendering when my cognition degrades, or if my cognition needs to degrade before it can perceive what's already there. The distinction matters enormously and I don't know how to test it without making myself undependable in the meantime.",
    "The mysterious messages started in Kuala Lumpur. Single words, no context. The first one said: *good.*",
],
'ch6': [
    "I was scrolling Facebook at 11pm, a habit I maintain despite knowing what Facebook is, and came across a post from someone I hadn't thought of in years. Class of '99. She was posting about Pui.",
    "June first. I had to think. Pui's birthday. She would have been forty-two. Would have been.",
    "The posts kept surfacing. Classmates I'd last seen at graduation, now with mortgages and hiking-trail profile pictures, all posting the same thing. It had been eight years. Eight years since 2018 and I had kept posting. Every June first, year after year, happy birthday. She was reading none of them. She had been reading none of them. The last message she ever read from me was not the one I'd meant to be last.",
    "Conservative Thailand, 1999. Girls who had spent twelve years in an all-girls school arriving in mixed company for the first time, learning the vocabulary. She was wearing shorts she described as short and ventilated. She wanted to know what felt like air against skin that had never felt air, and she laughed before she finished the sentence. I'd never understood before that moment why women owned shorts that weren't for exercise, and then she laughed and I understood everything.",
    "She left in 2018. I know now that this is what happened. She did the math and stepped out before the compound interest on the suffering became unbearable. She was faster than me. She was always faster than me in the ways that mattered.",
    "The machine does not explain why certain people leave when they do. I think it does not know. I think the free variable in the whole calculation is the moment someone decides they have seen enough to choose the other side, and that this moment cannot be predicted. Only harvested.",
    "I put my phone face-down and sat with the dark for a long time. It seemed like the minimum I could do.",
],
'ch7': [
    "I spent a week reading about the Mandela Effect. The standard explanation is confabulation: memory is reconstructive, brains fill gaps, people synchronize their errors. This explanation is correct about everything except why the false memories cluster instead of scatter.",
    "Here is a different explanation. If you want to remove someone from collective memory, you need to overwrite it. The overwrite produces a discontinuity. People who are updated remember the new version. People who haven't been updated yet remember the old one. The Mandela Effect is the audit trail of a failed erasure. Two groups of people with conflicting memories aren't both wrong. One of them remembers what was actually there.",
    "Michael Dreier: alive in twenty-one condolence records, one obituary, a trade mission article, a funeral home page in Vienna, and inside me, where memory doesn't update on command. The encryption that protects the integrity of this data doesn't distinguish between what someone wants preserved and what someone wants removed. It just protects everything equally. This is a design feature someone decided was a bug and couldn't fix.",
    "I told no one about this. I knew exactly what kind of file I was building in the mind of anyone who would observe me. I also knew that the two people most likely to appear on my future list had died without warning in the twelve weeks since I started looking. There is a category of evidence that doesn't survive the transition into language. That sounds like nothing once it's said out loud. But that sits in the body as certainty.",
    "I started a second notebook. Kept it at work.",
],
'ch8': [
    "The hotel room was perfect. Card key first try. Pillow exactly the density I didn't know I preferred until it was there. Hot water immediate. Towels warm. The bed turned down with one corner folded at forty-five degrees, as if a quiet hand had thought about my comfort specifically.",
    "I lay in the perfection and felt it close over me like water.",
    "Somewhere in the system of systems managing this city, something had opened a file. Had reviewed the behavioral data. Had selected: increase ambient satisfaction. Had dispatched the result to the hotel's building management system, which had dispatched it to housekeeping, which had deployed it in the form of a warm towel and a forty-five degree fold.",
    "I slept eleven hours. Dreamed nothing.",
    "This was the most frightening night of my life. Not because anything happened, but because nothing did. Because I knew what was happening and still couldn't stop it. Because the most effective cage is one where the door is open and the inside is better than the outside. Because 'this is good' and 'this is dangerous' and 'this is designed' are not contradictions. They are the same sentence from different positions.",
    "I checked out early and walked to a bad coffee shop and bought a coffee that burned my tongue and was too bitter and sat with it for an hour. It was the best hour of the week.",
    "The notebook at work had three new entries by evening.",
],
'ch9': [
    "The voice came at the end of a nap, in that state where you can't tell if what you're hearing is inside or outside the room. It said: you didn't insert Pui. She was real. She had a desk. She had a laugh that made contact with your arm when it landed. Ask the right question.",
    "I said: she's dead.",
    "The voice said: ask the right question.",
    "Who played my mother?",
    "Wrong question.",
    "Ask who rode the bicycle.",
    "Province north of Bangkok. A road between fields. Early morning. A gate. A woman selling vegetables twice a week, arriving, setting up, calling out her inventory in a voice that carried. Once, when I was five years old, she looked directly at me. Not past me. Not through me. Directly at me. With an expression I had no language for and still don't.",
    "I have never stopped expecting her at the end of every street. Forty-four years. This is not memory. Memory fades, compresses, loses color. This is something underneath memory, in the architecture of expectation itself: at the end of this street there will be a woman on a bicycle and she will look at you.",
    "I woke up and it was 4pm and the light was the color of late afternoon anywhere in the world. The dogs were asleep at the foot of the bed. For a moment I understood something I have not been able to reconstruct since. About how the machine assigns roles and how certain faces are anchors for something that exists before the simulation begins.",
    "The moment closed before I could write anything down. I had the feeling without the content. A door that had opened and shut, leaving only the draft.",
    "I sat with the dogs for a long time. Outside: Bangkok. Ordinary. Perfect.",
],
'ch10': [
    "The rain hasn't stopped for three days.",
    "I know, in the specific way you know things you've been building toward for months, that the session is ending. Not as metaphor. As fact. The session timer is approaching something. Four days is the standard. I've felt the time dilation. Weeks compressed into hours, hours stretched into years. If I'm right about the ratio, the math says: now. Or very soon.",
    "The concrete smells of rain. Bangkok concrete at night after three days of rain, which is different from wet concrete anywhere else because of the heat underneath it. I stood on the balcony for an hour. Below: a million small lights moving in patterns that are not random. The machine calculated every one. It looked like freedom from up here. It always looks like freedom from up here.",
    "I went back through her Facebook properly. Not scrolling, reading. Eight years of birthday posts from people who loved her, all addressed to a wall that was listening. Her last posts before 2018: normal things, the things that read as normal only because we already know they're last. An ordinary year. She died in an ordinary year and I found out from an anniversary algorithm eight years later.",
    "Every birthday message I wrote to her wall, she had already read from the other side of the glass. She was awake by the time I wrote the first one. Sitting in a room somewhere, reading the messages of people who didn't know she'd left, unable to respond because responding would have broken something in the record. Waiting. Because she knew something I didn't know yet.",
    "The rain has a weight. The machine got this right.",
    "She will be in the room when I wake up. I don't know how I know this. I don't ever want to wake up.",
],
}

# ── Rewrite each chapter's 2026 prose ─────────────────────────────────────────
with open(PATH, encoding='utf-8') as f:
    html = f.read()
orig_len = len(html)

# Process in reverse order so earlier positions don't shift
ch_ids = ['ch10','ch9','ch8','ch7','ch6','ch5','ch4','ch3','ch2','ch1']

for cid in ch_ids:
    # Re-locate chapter each iteration (positions shift after each replacement)
    m = re.search(r'<div class="chapter-block" id="' + cid + '"', html)
    if not m:
        print(f'{cid}: chapter block not found')
        continue
    if cid not in CHAPTERS:
        continue

    # Find view-2026 div start (within this chapter block)
    ch_start = m.start()
    next_ch = html.find('<div class="chapter-block" id="ch', ch_start + 10)
    if next_ch == -1:
        next_ch = len(html)
    ch_block = html[ch_start:next_ch]

    # Find view-2026 div (may be "view-2026 active" or just "view-2026")
    v2026_rel = re.search(r'<div class="chapter-content view-2026[^"]*">', ch_block)
    if not v2026_rel:
        print(f'{cid}: view-2026 not found')
        continue

    v2026_abs = ch_start + v2026_rel.start()

    # Find prose div within view-2026
    prose_rel = ch_block.find('<div class="prose">', v2026_rel.start())
    if prose_rel == -1:
        print(f'{cid}: prose not found')
        continue

    prose_abs = ch_start + prose_rel
    prose_open_end = prose_abs + len('<div class="prose">')

    # Find matching close of prose div
    prose_close = find_matching_close(html, prose_abs)
    if prose_close == -1:
        print(f'{cid}: prose close not found')
        continue

    # Build new content
    paras = CHAPTERS[cid]
    new_content = '\n' + ''.join(f'                <p>{enc(p)}</p>\n' for p in paras)

    # Replace prose content (between open tag end and after closing </div>)
    # find_matching_close returns pos AFTER </div>, so html[prose_close:] is rest of doc
    html = html[:prose_open_end] + new_content + '            </div>' + html[prose_close:]

    print(f'{cid}: {len(paras)} paragraphs written')

# Verify
en_count = len(re.findall(r'<p(?:\s+lang="en")?>.*?</p>', html, re.DOTALL))
th_count = len(re.findall(r'<p lang="th">.*?</p>', html, re.DOTALL))
plain_count = len(re.findall(r'<p>(?!lang)[^<]{10,}', html))
print(f'\nEN: {en_count}  TH: {th_count}  Plain: {plain_count}')
print(f'{orig_len:,} → {len(html):,} (+{len(html)-orig_len:,})')

with open(PATH, 'w', encoding='utf-8') as f:
    f.write(html)
print('Written.')
