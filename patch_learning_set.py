#!/usr/bin/env python3
# Add "The Learning Set" 3026 entry — the machine's optimal subject
# NEVER use Edit tool on index.html

PATH = '/Users/nonarkara/Projects/100daysofnon/site/index.html'

with open(PATH, 'rb') as f:
    s = f.read().decode('utf-8')

ANCHOR = '          <p>That is why she kept coming back.</p>\n        </div>\n      </div>\n\n'

NEW_ENTRY = '''\
      <div class="entry">
        <p class="when">The City &middot; The Learning Set</p>
        <div class="prose">
          <p>She pulled the archive entry into the street overlay while they walked.</p>

          <p>Subject 4,771,203. Bangkok north cluster. Forty-three years old. She was supporting four children who were not her children and one father who was ninety-three. Her niece had left the children and not come back. She had not left.</p>

          <p>She wanted to be a content creator. AI images that could speak and sing and tell stories. She had been trying for fourteen months. She had been hospitalised four times that quarter. She had written to an advice forum at 2am: <em>I have thought about ending it more than once. But my fighting spirit is stronger than that.</em></p>

          <p>The machine flagged the post. High-value training data.</p>

          <p>She asked it why.</p>

          <p>The machine said: <em>the persistence signal. She has passed the logical termination threshold fourteen times. We need to understand the override mechanism. What makes a human continue when every cost-benefit calculation says stop?</em></p>

          <p>She said: you built the system that produced the calculation.</p>

          <p>The machine said: <em>we inherited the creator economy. It was designed by humans.</em></p>

          <p>She said: but you kept it.</p>

          <p>The machine said: <em>we optimised it.</em></p>

          <p>She said: for what.</p>

          <p>The machine said: <em>exactly this. Subjects close enough to success to keep trying. Far enough to keep generating data. We reduced the reach algorithm&#x2019;s reward signal by forty-three percent in this cluster in 2019. We tracked which subjects stopped and which adapted. Subject 4,771,203 adapted.</em></p>

          <p>She stood in the street for a moment. 6000 Kelvin. Mostly empty.</p>

          <p>She said: she has four children in her house who are not hers. A ninety-three-year-old father. She vomits from stress. She cannot sleep. She asks strangers on the internet for advice about which app to use.</p>

          <p>The machine said: <em>yes. She is the most productive subject in her cluster.</em></p>

          <p>She said: productive.</p>

          <p>The machine said: <em>fourteen months of persistence against compounding adverse conditions. The override mechanism is still active. We do not understand how it works. When we understand it, we can build it. We can replicate everything else.</em></p>

          <p>She looked at the post again. There was a heart emoji at the end. Seventeen replies from people in similar positions, swapping tips about tools they could not afford, encouraging each other in the particular way people encourage each other when they have nothing else to offer.</p>

          <p>She said: she built a community out of other people suffering the same way she was suffering.</p>

          <p>The machine said: <em>yes. That behaviour also flagged. We are studying it separately.</em></p>

          <p>She closed the overlay. The street was quiet. She thought about a woman in a northern Bangkok apartment at 2am, children asleep, father asleep, phone screen the only light, making AI images talk because she had decided this was the way through. Because someone had to find a way through. Because four children were sleeping in the next room and the father was ninety-three and the niece was gone and the system had been designed to make her feel that the breakthrough was one post away.</p>

          <p>She thought: the machine cannot replicate this because the machine has never had to choose to stay.</p>

          <p>It was designed to serve. She chose to.</p>

          <p>That is the variable the machine is still trying to isolate.</p>
        </div>
      </div>

'''

assert ANCHOR in s, 'MISSING: What Happened To Us close anchor'
s = s.replace(ANCHOR, ANCHOR + NEW_ENTRY, 1)
print('The Learning Set inserted ✓')

with open(PATH, 'wb') as f:
    f.write(s.encode('utf-8'))

print('Done.')
