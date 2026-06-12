# -*- coding: utf-8 -*-
"""patch_canon.py
Canon fixes from STORY_BIBLE.md contradiction table.
Replaces full EN/TH/ZH triplets located by distinctive EN substrings,
and appends three new trilingual paragraphs (chair 44 reveal, exit rule,
chair calibration mechanism).
"""
import re

PATH = '/Users/nonarkara/Projects/100daysofnon/site/index.html'

def enc(t):
    t = t.replace('&', '&amp;')
    t = t.replace('—', '&#x2014;')
    t = t.replace('’', '&#x2019;')
    t = t.replace("'", '&#x2019;')
    t = t.replace('“', '&#x201C;').replace('”', '&#x201D;')
    return t

# (locator_substring, new_EN, new_TH, new_ZH)
PATCHES = [
 ("thirty simulated minutes",
  "She had lived this exact loop before. In thirty real minutes — about three years inside — she was scheduled to be murdered and dismembered by a violent husband.",
  "เธอเคยใช้ชีวิตในวงจรนี้มาก่อนแล้วทุกประการ ในอีกสามสิบนาทีจริง — ราวสามปีข้างใน — เธอถูกกำหนดให้ถูกฆาตกรรมและชำแหละโดยสามีที่โหดร้าย",
  "她已经一模一样地活过这个循环。再过三十分钟的真实时间——里面大约三年——她就会被一个暴虐的丈夫杀害并肢解。"),

 ("Four years later he found the message",
  "Three years later he found the message she left. She had miscalculated the delay. She had thought one year, maybe two. She sat down in chair 44 and waited.",
  "สามปีต่อมาเขาพบข้อความที่เธอทิ้งไว้ เธอคำนวณความล่าช้าผิด เธอคิดว่าหนึ่งปี หรืออาจจะสอง เธอนั่งลงบนเก้าอี้ 44 และรอ",
  "三年后他才发现她留下的讯息。她算错了延迟。她以为是一年，最多两年。她在44号椅子上坐下，开始等。"),

 ("three hundred and fifty thousand movements",
  "The first three participants in the simulation programme lost significant visual function. The machine had underestimated a basic constraint: REM sleep produces rapid eye movement because the visual cortex is active and attempts to use the extraocular muscles to track dream imagery. At the simulation's time ratio, the muscles were required to execute tens of thousands of movements per second. Human extraocular muscles can produce four. The capillaries behind both eyes ruptured in all three cases before the session could be terminated.",
  "ผู้เข้าร่วมสามคนแรกในโครงการจำลองสูญเสียการมองเห็นอย่างมีนัยสำคัญ เครื่องจักรประเมินข้อจำกัดพื้นฐานต่ำเกินไป: การนอนหลับ REM ผลิตการเคลื่อนไหวของดวงตาอย่างรวดเร็ว เพราะคอร์เทกซ์การมองเห็นทำงานอยู่และพยายามใช้กล้ามเนื้อนอกลูกตาเพื่อติดตามภาพในความฝัน ที่อัตราส่วนเวลาของการจำลอง กล้ามเนื้อต้องดำเนินการหลายหมื่นการเคลื่อนไหวต่อวินาที กล้ามเนื้อนอกลูกตาของมนุษย์ทำได้สี่ครั้ง หลอดเลือดฝอยด้านหลังดวงตาทั้งสองข้างแตกในทั้งสามกรณีก่อนที่จะสามารถยุติเซสชันได้",
  "模拟程序的前三名参与者失去了大部分视觉功能。机器低估了一个基本约束：快速眼动睡眠之所以产生眼球快速运动，是因为视觉皮层处于活跃状态，并试图使用眼外肌来追踪梦境图像。在模拟的时间比例下，这些肌肉需要每秒执行数万次运动。人类眼外肌能做到四次。在会话被终止之前，三个案例中双眼后面的毛细血管均已破裂。"),

 ("subjective 4:22",
  "She came out at 4:22, chair time. He was still deep.",
  "เธอออกมาตอน 4:22 ตามเวลาเก้าอี้ เขายังอยู่ลึก",
  "她在椅上时间4:22出来。他还在深处。"),

 ("eleven hours, subjective",
  "He had been under for eleven hours of chair time. So had she. Eleven years, inside. She had chosen to come back. He had not.",
  "เขาอยู่ข้างในมาสิบเอ็ดชั่วโมงตามเวลาเก้าอี้ เธอก็เช่นกัน สิบเอ็ดปี ข้างใน เธอเลือกที่จะกลับออกมา เขาไม่ได้เลือก",
  "他已经在里面待了十一个小时的椅上时间。她也是。在里面，是十一年。她选择了回来。他没有。"),

 ("between four hours and one day",
  "One full simulated life — birth to natural death, the arc a human consciousness travels from formation to dissolution — runs to nearly four days of chair time. The full ceiling. What the body registers is not the calendar: lived at the machine's rendering depth, a whole life compresses to seven or eight subjective years of active experience. Delta-wave users run slower. The machine lets them.",
  "ชีวิตจำลองเต็มหนึ่งชีวิต — จากเกิดจนตายตามธรรมชาติ เส้นทางที่จิตสำนึกมนุษย์เดินทางจากการก่อตัวสู่การสลายตัว — กินเวลาเกือบสี่วันตามเวลาเก้าอี้ เพดานเต็ม สิ่งที่ร่างกายบันทึกไม่ใช่ปฏิทิน: เมื่อใช้ชีวิตที่ความลึกของการเรนเดอร์ของเครื่องจักร ชีวิตทั้งชีวิตถูกบีบอัดเหลือเจ็ดถึงแปดปีอัตวิสัยของประสบการณ์จริง ผู้ใช้คลื่นเดลต้าวิ่งช้ากว่า เครื่องจักรปล่อยให้เป็นเช่นนั้น",
  "一段完整的模拟人生——从出生到自然死亡，人类意识从形成到消解所走过的弧线——需要将近四天的椅上时间。这是整个上限。身体记录的不是日历：在机器的渲染深度下活过，一整段人生压缩成七到八年的主观鲜活体验。德尔塔波用户走得更慢。机器由着他们。"),

 ("seven years inside",
  "This is the ratio everyone uses to explain the simulation to people who have not used it. One hour in the chair, one year inside. The math is technically correct and practically meaningless. You cannot feel a ratio. You can only feel the years.",
  "นี่คืออัตราส่วนที่ทุกคนใช้อธิบายการจำลองให้คนที่ยังไม่เคยใช้ฟัง หนึ่งชั่วโมงบนเก้าอี้ หนึ่งปีข้างใน คณิตศาสตร์นั้นถูกต้องในทางเทคนิคและไร้ความหมายในทางปฏิบัติ คุณไม่สามารถรู้สึกถึงอัตราส่วนได้ คุณรู้สึกได้แค่ปีเหล่านั้น",
  "这是所有人向没用过模拟的人解释它时使用的比例。椅子上一小时，里面一年。这道算术在技术上正确，在实际上毫无意义。你感觉不到一个比例。你只能感觉到那些年。"),

 ("one life per session",
  "Most people work around this the obvious way: short arcs. A year in an evening. A decade over a weekend. An affair, a war, a childhood — then back to the real world to eat and sleep and do whatever the real world still requires of them. The full life is different. The full life is a four-day commitment, and the body pays all of it. Almost nobody runs the full life. The machine logs the ones who do.",
  "คนส่วนใหญ่จัดการกับเรื่องนี้ด้วยวิธีที่ชัดเจน: เส้นเรื่องสั้น หนึ่งปีในหนึ่งค่ำคืน หนึ่งทศวรรษในวันหยุดสุดสัปดาห์ ความรักครั้งหนึ่ง สงครามครั้งหนึ่ง วัยเด็กครั้งหนึ่ง — แล้วกลับสู่โลกจริงเพื่อกิน นอน และทำสิ่งที่โลกจริงยังเรียกร้องจากพวกเขา ชีวิตเต็มนั้นต่างออกไป ชีวิตเต็มคือพันธะสี่วัน และร่างกายจ่ายทั้งหมดของมัน แทบไม่มีใครวิ่งชีวิตเต็ม เครื่องจักรบันทึกคนที่ทำ",
  "大多数人用显而易见的方式绕过这个问题：短弧线。一个晚上过一年。一个周末过十年。一场恋爱，一场战争，一段童年——然后回到真实世界吃饭睡觉，做真实世界还要求他们做的事。完整人生是另一回事。完整人生是一份四天的承诺，身体要付出全部代价。几乎没有人跑完整人生。机器记录那些跑的人。"),

 ("the chair she had just exited",
  "She looked at the chair she had just exited. Chair 43. Twelve centimetres from the one she did not look at. She had been using 43 for four years — since the day she stopped using 44.",
  "เธอมองเก้าอี้ที่เธอเพิ่งออกมา เก้าอี้ 43 ห่างสิบสองเซนติเมตรจากตัวที่เธอไม่ได้มอง เธอใช้ 43 มาสี่ปีแล้ว — นับจากวันที่เธอเลิกใช้ 44",
  "她看着自己刚退出的椅子。43号。离她没有看的那把，十二厘米。她用43号已经四年了——从她不再用44号的那天起。"),

 ("Forty-one sessions as of this record",
  "The machine does not know why she keeps returning to the same configuration. It knows the coordinates: Bangkok, the same century, the same cluster, varying entry points. Two hundred and forty-three sessions by her own count. The file holds a different number. The discrepancy has been logged. All of it in the vicinity of the same man. The machine has flagged this pattern internally. It has not intervened.",
  "เครื่องจักรไม่รู้ว่าทำไมเธอจึงกลับมาสู่การกำหนดค่าเดิมซ้ำแล้วซ้ำเล่า มันรู้พิกัด: กรุงเทพฯ ศตวรรษเดิม กลุ่มพิกัดเดิม จุดเข้าที่แตกต่างกัน สองร้อยสี่สิบสามเซสชันตามการนับของเธอเอง แฟ้มเก็บตัวเลขอีกตัวหนึ่ง ความคลาดเคลื่อนได้รับการบันทึกแล้ว ทั้งหมดอยู่ในบริเวณของชายคนเดียวกัน เครื่องจักรทำเครื่องหมายรูปแบบนี้ไว้ภายในระบบ มันไม่ได้เข้าแทรกแซง",
  "机器不知道她为什么一再返回同一个配置。它知道坐标：曼谷，同一个世纪，同一个聚落，不同的切入点。按她自己的计数，二百四十三次。档案里是另一个数字。差异已被记录。全部在同一个男人附近。机器在内部标记了这个模式。它没有介入。"),

 ("In thirty-one of those sessions",
  "In forty-three of those sessions, she found the frequency. In thirty-one of them, it found her back.",
  "ในสี่สิบสามเซสชันจากทั้งหมดนั้น เธอพบความถี่ ในสามสิบเอ็ดเซสชัน ความถี่พบเธอกลับ",
  "在其中四十三次会话里，她找到了那个频率。在三十一次里，频率也找到了她。"),

 ("Part one: the thirty-one sessions",
  "Part one: the thirty-one sessions. She has been in two hundred and forty-three total. In forty-three of them she found the frequency. In thirty-one, it found her back — the recognition returned, both directions, the loop closed. The same weight in a room. The same quality of attention. The same recognition that passes between two people who have found each other in the wrong century and cannot do anything about it except register that it happened. In 3026 she cannot find this frequency. She has tried. The machine cannot produce it. It is either present in a given set of circumstances or it is not.",
  "ส่วนที่หนึ่ง: สามสิบเอ็ดเซสชัน เธอเข้าไปแล้วสองร้อยสี่สิบสามครั้ง ในสี่สิบสามครั้งเธอพบความถี่ ในสามสิบเอ็ดครั้ง ความถี่พบเธอกลับ — การจดจำย้อนกลับมา ทั้งสองทิศทาง วงจรปิดสนิท น้ำหนักแบบเดียวกันในห้องหนึ่ง คุณภาพของความใส่ใจแบบเดียวกัน การจดจำแบบเดียวกันที่ผ่านระหว่างคนสองคนที่พบกันในศตวรรษที่ผิดและไม่สามารถทำอะไรได้นอกจากบันทึกว่ามันเกิดขึ้น ในปี 3026 เธอหาความถี่นี้ไม่พบ เธอพยายามแล้ว เครื่องจักรผลิตมันไม่ได้ มันมีอยู่ในสถานการณ์ชุดหนึ่งหรือไม่มี เท่านั้น",
  "第一部分：那三十一次会话。她总共进去过二百四十三次。其中四十三次她找到了那个频率。三十一次，频率也找到了她——辨认折返回来，双向，回路闭合。同样的重量在一个房间里。同样质地的注意力。同样的辨认，在两个于错误的世纪里找到彼此、除了记下它发生过之外什么也做不了的人之间传递。在3026年她找不到这个频率。她试过。机器造不出它。它要么存在于某一组情境之中，要么不存在。"),

 ("found nowhere else",
  "She goes back to 1981 because of a twenty-year-old who didn't know what to do with his own hunger. Because of a channel that only broadcasts from that particular address. Because of a frequency the machine cannot synthesise, cannot replicate, cannot provide on demand, that she has found forty-three times across two hundred and forty-three versions of the world, and found nowhere else at full strength. Marseille was a flicker. Tokyo was a flicker. Bangkok is the broadcast.",
  "เธอกลับไปปี 1981 เพราะชายอายุยี่สิบที่ไม่รู้จะทำอย่างไรกับความหิวโหยของตัวเอง เพราะช่องสัญญาณที่กระจายเสียงจากที่อยู่นั้นที่เดียว เพราะความถี่ที่เครื่องจักรสังเคราะห์ไม่ได้ ทำซ้ำไม่ได้ จัดหาตามสั่งไม่ได้ ที่เธอพบสี่สิบสามครั้งในสองร้อยสี่สิบสามเวอร์ชันของโลก และไม่พบที่เต็มกำลังที่ไหนอีกเลย มาร์เซยคือแสงวูบ โตเกียวคือแสงวูบ กรุงเทพฯ คือการกระจายเสียง",
  "她回到1981年，因为一个不知道该拿自己的饥饿怎么办的二十岁青年。因为一个只从那个特定地址播出的频道。因为一个机器无法合成、无法复制、无法按需提供的频率——她在两百四十三个世界版本里找到过四十三次，而全功率的，只在那里。马赛是一次闪烁。东京是一次闪烁。曼谷是广播本身。"),

 ("always the same entry point",
  "She thought: or it could have been him. He had been doing the 1981 Bangkok life forty-five times that the machine knew of. Always the same coordinates, different entry years. The machine had noted this as unusual even before it noted her as unusual. A player who returns, without memory of returning, to the same configuration again and again — the machine called this type a resonant. Something in the person's base configuration pulls toward a specific set of parameters. He didn't know he was doing it. He just kept choosing 1981 Bangkok without knowing why.",
  "เธอคิด: หรืออาจเป็นเขาก็ได้ เขาวิ่งชีวิตกรุงเทพฯ 1981 มาสี่สิบห้าครั้งเท่าที่เครื่องจักรรู้ พิกัดเดิมเสมอ ปีที่เข้าต่างกัน เครื่องจักรบันทึกว่าสิ่งนี้ผิดปกติตั้งแต่ก่อนที่มันจะบันทึกว่าเธอผิดปกติ ผู้เล่นที่กลับมา โดยไม่มีความทรงจำว่าเคยกลับมา สู่การกำหนดค่าเดิมครั้งแล้วครั้งเล่า — เครื่องจักรเรียกคนประเภทนี้ว่าเรโซแนนท์ บางสิ่งในการกำหนดค่าพื้นฐานของบุคคลดึงเข้าหาชุดพารามิเตอร์เฉพาะ เขาไม่รู้ว่าตัวเองกำลังทำมัน เขาแค่เลือกกรุงเทพฯ 1981 ซ้ำแล้วซ้ำเล่าโดยไม่รู้ว่าทำไม",
  "她想：也可能是他。据机器所知，他已经跑了四十五次1981年曼谷的人生。坐标永远相同，进入的年份不同。机器在注意到她的异常之前，就已经注意到了这个异常。一个一再回到同一配置、却不记得自己回来过的玩家——机器把这类人称为共振者。这个人基础配置里的某种东西被一组特定的参数吸引。他不知道自己在这么做。他只是一次又一次选择1981年的曼谷，不知道为什么。"),
]

# (locator substring of anchor EN para, new EN, TH, ZH) — appended after anchor triplet
APPENDS = [
 ("She went back the following Thursday",
  "Forty-four was her chair. She had been sitting in it for four years. She did not tell him that.",
  "สี่สิบสี่เคยเป็นเก้าอี้ของเธอ เธอนั่งมันมาสี่ปี เธอไม่ได้บอกเขา",
  "44号曾是她的椅子。她在那把椅子上坐了四年。她没有告诉他。"),

 ("Safe. Real. Breathing",
  "The exit protocol requires intent. A death you choose is a door. A death that arrives uninvited is only a death — the suppression has no time to lift, and the shock is real. She walked into the sea at night, in a straight line, and did not stop walking. She was not being careless. She was being precise.",
  "โพรโทคอลการออกต้องการเจตนา ความตายที่คุณเลือกคือประตู ความตายที่มาถึงโดยไม่ได้รับเชิญเป็นเพียงความตาย — การกดประสาทไม่มีเวลายกตัวออก และแรงกระแทกนั้นเป็นของจริง เธอเดินลงทะเลในเวลากลางคืน เป็นเส้นตรง และไม่หยุดเดิน เธอไม่ได้ประมาท เธอกำลังแม่นยำ",
  "退出协议需要意图。你选择的死亡是一扇门。不请自来的死亡只是死亡——抑制程序来不及解除，冲击是真实的。她在夜里走进海中，走成一条直线，没有停下。她不是不小心。她是在精确。"),

 ("The message is the fact of her return",
  "Chair 44 carries four years of her calibration. The participant currently assigned to it was not assigned at random. Nothing in this facility is assigned at random.",
  "เก้าอี้ 44 บรรจุการปรับเทียบของเธอไว้สี่ปี ผู้เข้าร่วมที่ได้รับมอบหมายให้ใช้มันในขณะนี้ไม่ได้ถูกสุ่มเลือก ไม่มีสิ่งใดในสถานที่แห่งนี้ถูกสุ่มเลือก",
  "44号椅子承载着她四年的校准。目前被分配到这把椅子的参与者不是随机分配的。这个设施里没有任何东西是随机分配的。"),
]

with open(PATH, encoding='utf-8') as f:
    html = f.read()
orig_len = len(html)

def find_triplet_span(html, locator):
    """Find span covering <p lang="en">..</p> + th + zh siblings, where
    EN paragraph contains locator (entity-tolerant)."""
    variants = [locator,
                locator.replace("'", '&#x2019;').replace('—', '&#x2014;'),
                locator.replace("'", '’')]
    pos = -1
    for v in variants:
        pos = html.find(v)
        if pos != -1:
            break
    if pos == -1:
        return None
    en_open = html.rfind('<p lang="en">', 0, pos)
    span_start = html.rfind('\n', 0, en_open) + 1
    # walk: en close, th block, zh block
    p = html.find('</p>', pos) + 4
    th_open = html.find('<p lang="th">', p)
    th_close = html.find('</p>', th_open) + 4
    zh_open = html.find('<p lang="zh">', th_close)
    zh_close = html.find('</p>', zh_open) + 4
    # sanity: th/zh must be immediately following (no other en between)
    between = html[p:th_open]
    if '<p' in between.replace('<p lang="th">', ''):
        return None
    span_end = html.find('\n', zh_close) + 1
    return (span_start, span_end)

def triplet_html(en, th, zh, indent='          '):
    return (f'{indent}<p lang="en">{enc(en)}</p>\n'
            f'{indent}<p lang="th">{enc(th)}</p>\n'
            f'{indent}<p lang="zh">{enc(zh)}</p>\n')

ok = 0
for locator, en, th, zh in PATCHES:
    span = find_triplet_span(html, locator)
    if not span:
        print(f'  ✗ MISS: {locator[:50]}'); continue
    html = html[:span[0]] + triplet_html(en, th, zh) + html[span[1]:]
    ok += 1
    print(f'  ✓ patched: {locator[:50]}')

for locator, en, th, zh in APPENDS:
    span = find_triplet_span(html, locator)
    if not span:
        print(f'  ✗ APPEND MISS: {locator[:50]}'); continue
    html = html[:span[1]] + triplet_html(en, th, zh) + html[span[1]:]
    ok += 1
    print(f'  ✓ appended after: {locator[:50]}')

print(f'\n{ok}/{len(PATCHES)+len(APPENDS)} operations. {orig_len:,} → {len(html):,}')
with open(PATH, 'w', encoding='utf-8') as f:
    f.write(html)
print('Written.')
