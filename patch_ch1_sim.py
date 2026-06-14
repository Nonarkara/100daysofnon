#!/usr/bin/env python3
"""Rewrite Chapter 1 simulation prose with the full brief:
Neo question opening → mechanized life → substances → glimpse of 3026 →
animal return → paranoia seeds (Michael, Lek, the sedan).
"""
import json

with open('data/two-layers.json', encoding='utf-8') as f:
    data = json.load(f)

CH1_SIM_EN = [
    "Have you ever felt like none of this is real?",

    "Not in the philosophical way. Not depression. Just the feeling — certain mornings, certain angles of light through Bangkok smog — that everything around you is running slightly too smoothly. That the repetitions have been designed. That someone is getting something out of them.",

    "I noticed it first in my coffee. Same brand. Same temperature. Same twenty seconds I waited before the first sip. I thought I was building discipline. Maybe I was. Maybe discipline is what the machine looks like from the inside.",

    "I am an architect. I do not draft anymore. I talk to an AI and the AI builds. I sit in a glass box forty floors above Sukhumvit and describe what I see in my head and the machine turns description into structure. It is never wrong. It is never late. It is never anything except exactly what I asked for. Which is, I have learned, the problem.",

    "I eat once a day. One meal. I wear the same four shirts in rotation. I take fourteen vitamins in the morning, in order, with water at room temperature. I walk at least eleven thousand steps. The body requires maintenance the way a car does and I accept this. The dentist. I go to the dentist. I have always hated the sound the instruments make. I have thought about why nobody has fixed this. The sound keeps people afraid. Afraid people come back. It is good for the business of dentistry to leave the sound exactly as it is.",

    "I have more money than I can use. This is not a complaint. It is a data point.",

    "I still buy sneakers. I know this is inconsistent with everything I just said about uniforms. But some shoes are not born equal. Some shoes will take you places and some shoes will leave you exactly where you are. I walk this city. I walk it in the morning before the heat arrives and in the evening when it almost breaks and I need to know that the shoes I am wearing understand where I am trying to go.",

    "The body gets less energetic. I notice this more each year. What I could do at twenty-eight requires twice the maintenance at thirty-seven. The vitamins, the steps, the water, the sleep — these are not improvements. They are holding actions. The machine is slowing.",

    "I started smoking weed somewhere around 2022 when it became easy to get good weed in Bangkok. Legal, then less legal, then gray, then just available. I smoked because it stopped the part of my brain that would not stop. The thoughts come in loops. The loops get tighter. Weed made them expand. Opened space between the repetitions. Sometimes I added nicotine — small pouches under the lip, twenty-eight milligrams, which is more than most people can handle, and I could handle it, or I told myself I could. Sometimes alcohol. Never at the same time. Then always at the same time.",

    "There were nights I pushed it to the edge of what felt safe. Heart pounding. The ceiling of the room becoming something else. And in those moments — not every time, not reliably, but enough times that I started chasing it — I saw something.",

    "A room. White. Cold. Not the cold of air conditioning. The cold of something kept at a temperature I had no word for. Rows of chairs. People in the chairs, not moving, eyes closed, faces slack, breathing but only barely. Something attached to the back of each skull. The air in that room — I can still feel it — the air had no smell. Not clean. Absent. Like the concept of air had been achieved and all the accident had been removed from it.",

    "I came back from that room wanting to touch everything. To hold someone and feel the heat of them and know by that heat that they were still an animal. That we were still animals. The body understands what the brain will not admit. I am not proud of everything I did to confirm this. But I confirmed it.",

    "Lek got married in March. New house in Chiang Rai. New life. He sent photographs of the garden. Two months later he was gone. Not a long illness. Not an accident anyone could explain clearly. Just: gone. The kind of gone that closes quickly, like water over a stone.",

    "Michael — I will not use his real name — Michael came to Bangkok from Vienna. He knew everyone. He went to every party. He understood this city the way foreigners sometimes understand a city better than the people who were born in it, because they are still paying attention. He left on the third of May. Not the city. Existence. Fifty-four years old. The announcement came and then almost immediately the traces of him started to thin. The photographs. The articles. The LinkedIn page. Thinning, not deleted. The way a sound fades before you notice it has stopped.",

    "I drive myself now. No driver. I take different routes. Last Tuesday someone in a gray sedan pulled beside me at the lights on Rama IV, rolled down the window, and looked at me the way you look at something you have already decided to do something about. Then the light changed.",

    "There is a dent on the passenger side of my car I do not remember making.",
]

data['chapters'][0]['simulation']['paragraphs']['en'] = CH1_SIM_EN

with open('data/two-layers.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Done. {len(CH1_SIM_EN)} paragraphs written to chapter 1 simulation (EN).")
