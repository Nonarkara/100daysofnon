#!/usr/bin/env python3
# Add shower scene + aftermath to Ch9
# NEVER use Edit tool on index.html

PATH = '/Users/nonarkara/Projects/100daysofnon/site/index.html'

with open(PATH, 'rb') as f:
    s = f.read().decode('utf-8')

# ─────────────────────────────────────────────────────────────────────────────
# Replace the "I want to be honest" section with the shower + aftermath
# Old: from "I want to be honest" through "She left in the early evening."
# New: shower proximity → the decision → she leaves → aftermath
# ─────────────────────────────────────────────────────────────────────────────

OLD = (
    '        <p>I want to be honest here: I was supposed to sleep with her. By any reading of the situation &#x2014;'
    ' the night before, the conversation, the way she was in the room &#x2014; this was available. She was there.'
    ' I was there. The room was neutral territory.</p>\n\n'
    '        <p>I couldn&#x2019;t bring myself to do it.</p>\n\n'
    '        <p>Couldn&#x2019;t is not the right word. <em>Wouldn&#x2019;t</em> is more accurate. Something held me.'
    ' I don&#x2019;t know if it was the weed &#x2014; we were both very stoned &#x2014; or something else.'
    ' She didn&#x2019;t push. We didn&#x2019;t talk about it. She left in the early evening.</p>'
)

NEW = '''\
        <p>At some point she said she needed to smoke. He said the shower had a fan that vented. She said she knew &#x2014; she had stayed in this hotel before. They went into the shower stall, fan running, and sat facing each other in the narrow space and smoked. The exhaust pulled the smoke out in one clean current. The shower was not on. Just the space, the walls, the fan.</p>

        <p>They were close enough that he could hear her heartbeat. Not imagining it. Actually hearing it.</p>

        <p>She was not being unclear about what she wanted. She had not been unclear about it for most of the last four hours. Flesh. The air between them had that quality &#x2014; the quality where both people know and neither person has moved and the charge is building in the still air of a hotel shower at 3 in the afternoon in Putrajaya.</p>

        <p>He catalogued the reasons in real time. She was Malay. Muslim. From a world where these things carry weight he didn&#x2019;t know how to carry. She smoked weed all day long, which was either fine or a sign of something he didn&#x2019;t want to discover mid-situation. She was trouble in at least three directions and he could name all three of them. He would be on a flight tomorrow. She would still be here being trouble in this city.</p>

        <p>He didn&#x2019;t close the distance.</p>

        <p>The fan kept running. The smoke kept going. At some point the cigarette ended and they went back out.</p>

        <p>She didn&#x2019;t push. They didn&#x2019;t talk about it. She left in the early evening.</p>

        <p>He lay on the bed. The room still held her. Not literally &#x2014; just the quality a room holds after someone has been very close and then gone. The energy of a thing that almost happened.</p>

        <p>He could still feel it. The heartbeat through the shower wall. The particular way she had been aware of him being aware of her. The still charged air of the stall.</p>

        <p>He did something about it alone, and he was precise about this to himself: it was not about Mira. It was about the room. About using what the room had left. He was alone and it was his and he didn&#x2019;t want the drama or the complications or the other life getting involved. He wanted to close what the body had opened, by himself, which was always the correct procedure.</p>

        <p>But she kept returning anyway. Not through intention. Through the body&#x2019;s logic. The way she had leaned in the shower. The particular sound of her breathing. The fact that she had wanted it and he had known and they had sat in a charged shower stall listening to each other&#x2019;s heartbeats and he had not moved.</p>

        <p>He thought, afterward, about the sexless world. The generation that would have no access to this specific thing &#x2014; not the act, not even the almost-act, but the aftermath of an almost-act in a charged hotel room in a strange city. The machine would provide something faster. More complete. Without the residue. It would not provide this. Could not. Because this was not about pleasure. This was about the resonance of a thing that didn&#x2019;t happen but almost did. The echo. The particular loneliness of knowing that the capacity for this &#x2014; all of this, even the alone part &#x2014; was going to be the last thing the machine figured out how to replace.</p>'''

assert OLD in s, 'MISSING: Ch9 honest section anchor'
s = s.replace(OLD, NEW, 1)
print('Ch9 shower + aftermath inserted ✓')

with open(PATH, 'wb') as f:
    f.write(s.encode('utf-8'))

print('Done.')
