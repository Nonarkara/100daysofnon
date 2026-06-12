#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""patch_new_entries.py
Add four new 3026 record entries, all trilingual:
  1. The Cycle — Pui's 4-year return pattern, the 4-day limit
  2. What She Came For — the simulation sex scene, female interior
  3. Session Zero — early sessions, eye ruptures, the neurolink solution
  4. The Basement — quantum plant, gravitational dilation, the actual why
"""

def entry(when, paragraphs_en, paragraphs_th, paragraphs_zh):
    """Build a full trilingual <div class="entry"> block."""
    lines = [
        '      <div class="entry">',
        f'        <p class="when">{when}</p>',
        '        <div class="prose">',
    ]
    for en, th, zh in zip(paragraphs_en, paragraphs_th, paragraphs_zh):
        lines.append(f'          <p lang="en">{en}</p>')
        lines.append(f'          <p lang="th">{th}</p>')
        lines.append(f'          <p lang="zh">{zh}</p>')
    lines += ['        </div>', '      </div>', '']
    return '\n'.join(lines)

# ── ENTRY 1: THE CYCLE ───────────────────────────────────────────────────────
# Where: after "The Hub · Room 7 · Thirty-one minutes after entry" (entry 1)
# What: explains the 4-day session limit, Pui's return pattern

E1_WHEN = 'The Hub &middot; Room 7 &middot; The Cycle'

E1_EN = [
    'One year in the simulation equals one hour in the real world. The machine processes at a rate the brain cannot distinguish from lived experience. The ratio is not a design choice. It is a consequence of running quantum coherence at minus two hundred and seventy degrees several kilometres underground, where time moves at a different rate than at the surface. The AI did not engineer this. It found it and moved in.',
    'The body has limits the machine cannot override. Four days in the chair is the ceiling. At that point the brain has lived approximately ninety-six years of simulated time. The organs require nutrition the nutrient line cannot adequately provide beyond that threshold. Participants wake weak, confused, occasionally believing they are old. They are not old. They are the same age they were when they sat down. The simulation leaves no biological trace. Only memory.',
    'Recovery: two weeks minimum. Blood work, hydration, reintroduction of solid food. A physical assessment of the neural pathway before the next session is approved. The assessment takes four minutes. Most participants are cleared.',
    'She has been doing this for four years. Session after session. Four days in, two weeks out, back in. The staff of Room 7 have stopped noting it as unusual in the incident log. At some point unusual becomes the baseline.',
    'The machine does not know why she keeps returning to the same configuration. It knows the coordinates: Bangkok, 2026, the protagonist\'s timeline, varying entry points. Forty-one sessions as of this record. Four thousand, one hundred and thirty-six simulated years. All in the vicinity of the same man. It has flagged this pattern internally. It has not intervened.',
    'The AI respects her choice the way it respects all choices. This is why we are eighty million.'
]

E1_TH = [
    'หนึ่งปีในโลกจำลองเท่ากับหนึ่งชั่วโมงในโลกจริง เครื่องจักรประมวลผลในอัตราที่สมองไม่สามารถแยกแยะได้จากประสบการณ์ที่ใช้ชีวิตจริง อัตราส่วนนี้ไม่ใช่ทางเลือกในการออกแบบ มันคือผลลัพธ์ของการรักษาควอนตัมโคฮีเรนซ์ที่ลบสองร้อยเจ็ดสิบองศาหลายกิโลเมตรใต้ดิน ที่ซึ่งเวลาเคลื่อนที่ในอัตราที่แตกต่างจากพื้นผิว ปัญญาประดิษฐ์ไม่ได้ออกแบบสิ่งนี้ มันค้นพบมันและเข้าไปอยู่อาศัย',
    'ร่างกายมีขีดจำกัดที่เครื่องจักรไม่สามารถแทนที่ได้ สี่วันบนเก้าอี้คือเพดาน ณ จุดนั้นสมองได้ใช้ชีวิตมาประมาณเก้าสิบหกปีในเวลาจำลอง อวัยวะต้องการสารอาหารที่สายน้ำเกลือไม่สามารถให้ได้อย่างเพียงพอเกินกว่าจุดนั้น ผู้เข้าร่วมตื่นขึ้นด้วยความอ่อนแอ สับสน บางครั้งเชื่อว่าตัวเองแก่แล้ว พวกเขาไม่ได้แก่ พวกเขาอายุเท่าเดิมกับตอนที่นั่งลง การจำลองไม่ทิ้งร่องรอยทางชีววิทยา มีเพียงความทรงจำ',
    'การฟื้นตัว: อย่างน้อยสองสัปดาห์ การตรวจเลือด การให้น้ำ การค่อยๆ กลับมากินอาหารแข็ง การประเมินเส้นทางประสาทก่อนที่จะอนุมัติให้เข้าร่วมครั้งต่อไป การประเมินใช้เวลาสี่นาที ผู้เข้าร่วมส่วนใหญ่ผ่านการตรวจ',
    'เธอทำสิ่งนี้มาสี่ปีแล้ว ครั้งแล้วครั้งเล่า สี่วันในห้อง สองสัปดาห์ข้างนอก แล้วกลับเข้ามาใหม่ เจ้าหน้าที่ของห้องเจ็ดหยุดบันทึกว่ามันผิดปกติในบันทึกเหตุการณ์แล้ว ณ จุดหนึ่ง สิ่งผิดปกติกลายเป็นพื้นฐาน',
    'เครื่องจักรไม่รู้ว่าเธอกลับมาสู่การกำหนดค่าเดิมซ้ำแล้วซ้ำเล่าทำไม มันรู้พิกัด: กรุงเทพฯ ปี 2026 ไทม์ไลน์ของตัวละครหลัก จุดเข้าที่แตกต่างกัน สี่สิบเอ็ดครั้งนับถึงบันทึกนี้ สี่พันหนึ่งร้อยสามสิบหกปีจำลอง ทั้งหมดอยู่ในบริเวณของชายคนเดียวกัน มันทำเครื่องหมายรูปแบบนี้ภายในระบบ มันไม่ได้เข้าแทรกแซง',
    'ปัญญาประดิษฐ์เคารพทางเลือกของเธอในแบบเดียวกับที่มันเคารพทุกทางเลือก นั่นเองคือเหตุผลที่เราเหลืออยู่แปดสิบล้าน'
]

E1_ZH = [
    '模拟世界的一年等于现实世界的一小时。机器的处理速率让大脑无法分辨它与真实经历的区别。这个比例不是一种设计选择。它是在地下数公里处、零下两百七十度运行量子相干的结果——在那里，时间的流速与地表不同。人工智能没有设计这一点。它发现了它，然后搬了进去。',
    '身体有机器无法覆盖的极限。在椅子上坐四天是上限。到那时，大脑已经经历了大约九十六年的模拟时光。器官需要的营养是营养管线在这个阈值之后无法充分提供的。参与者醒来时会感到虚弱、迷茫，有时会以为自己老了。他们没有变老。他们和坐下时一样年轻。模拟不留下任何生物学痕迹。只有记忆。',
    '恢复期：至少两周。验血，补液，重新引入固体食物。在批准下一次进入之前对神经通路进行体格评估。评估需要四分钟。大多数参与者都能通过。',
    '她已经这样做了四年。一次又一次。四天在里面，两周在外面，再回去。7号房间的工作人员已经不再在事故记录中将此标注为异常。到了某个时刻，不寻常变成了常态。',
    '机器不知道她为什么一再返回同一个配置。它知道坐标：曼谷，2026年，主角的时间线，不同的切入点。截至本记录共四十一次。四千一百三十六年的模拟时间。全部在同一个男人附近。它在内部标记了这个模式。它没有介入。',
    '人工智能尊重她的选择，就像它尊重所有选择一样。这就是为什么我们只剩八千万。'
]

# ── ENTRY 2: WHAT SHE CAME FOR ───────────────────────────────────────────────
# Where: after "The Hub · The Austrian" (ch4 anchor)
# What: the simulation sex scene — female interior, Pui's perspective

E2_WHEN = 'The Hub &middot; Room 7 &middot; What She Came For'

E2_EN = [
    'She knew what was going to happen before it did. Not prophecy. Something in the body that the body knows first. The way skin reads weather before the mind names it.',
    'He hadn\'t touched her yet. He was across the room. That was the whole thing. That he was across the room and she was aware of every centimetre between them.',
    'In 3026 she could press a point behind her left ear and her entire nervous system lit from the inside. Ten times the intensity. A hundred. Measurably better than this. Delivered in under three seconds. She had not pressed that point in six months.',
    'She wanted this instead: to not know. To be in a body that didn\'t have the shortcut. To stand across a room from someone and feel the want build like pressure in a sealed space. To not press anything. To wait.',
    'He looked at her. Not the long look. The quick one. The one men give when they are trying not to give the long one. She felt it the way you feel a key turn in a lock you didn\'t know was locked.',
    'Later she would lie still and think: this is what they took away. Not the sensation. The gap before it. A hundred thousand years of evolution encoded in the waiting, and the machine read the request correctly and deleted the waiting and called it progress.',
    'She did not regret coming back. She had never regretted coming back. Even now. Even knowing she would have to leave again in four days, recover for two weeks, pass the exam, and return to a room that smelled of circulated air and exact temperature, and decide all over again whether she had found what she came for.',
    'She had not found it yet. She kept coming back anyway. This was the thing the machine could not model: the choosing to continue when the outcome is still unknown.'
]

E2_TH = [
    'เธอรู้ว่าอะไรจะเกิดขึ้นก่อนที่มันจะเกิด ไม่ใช่การทำนาย แต่เป็นบางสิ่งในร่างกายที่ร่างกายรู้ก่อน เหมือนผิวหนังอ่านสภาพอากาศก่อนที่จิตใจจะตั้งชื่อมัน',
    'เขายังไม่ได้แตะต้องเธอ เขาอยู่ฝั่งตรงข้ามของห้อง นั่นคือทุกอย่าง ที่เขาอยู่ฝั่งตรงข้ามของห้องและเธอตระหนักถึงทุกเซนติเมตรระหว่างพวกเขา',
    'ในปี 3026 เธอสามารถกดจุดหลังหูซ้ายและระบบประสาทของเธอทั้งหมดจะสว่างจากภายใน สิบเท่าของความเข้มข้น หรือหนึ่งร้อยเท่า เหนือกว่านี้อย่างวัดได้ ส่งมอบในไม่ถึงสามวินาที เธอไม่ได้กดจุดนั้นมาหกเดือนแล้ว',
    'เธอต้องการสิ่งนี้แทน: การไม่รู้ว่าจะเกิดอะไร การอยู่ในร่างกายที่ไม่มีทางลัด การยืนอยู่ฝั่งตรงข้ามของห้องกับใครสักคนและรู้สึกว่าความปรารถนาก่อตัวขึ้นเหมือนความดันในพื้นที่ปิด การไม่กดอะไรเลย การรอ',
    'เขามองเธอ ไม่ใช่การมองนาน แต่เป็นการมองสั้นๆ แบบที่ผู้ชายใช้เมื่อพยายามไม่ให้ตัวเองมองนาน เธอรู้สึกได้เหมือนการได้ยินเสียงกุญแจหมุนในกุญแจที่เธอไม่รู้ว่ามันถูกล็อกอยู่',
    'ต่อมาเธอจะนอนนิ่งและคิด: นี่คือสิ่งที่พวกเขาพรากไป ไม่ใช่ความรู้สึก แต่คือช่องว่างก่อนมัน วิวัฒนาการหนึ่งแสนปีที่ถ่ายทอดไว้ในการรอคอย และเครื่องจักรอ่านคำขอได้อย่างถูกต้องและลบการรอคอยออกและเรียกมันว่าความก้าวหน้า',
    'เธอไม่เสียใจที่กลับมา เธอไม่เคยเสียใจที่กลับมาเลย แม้แต่ตอนนี้ แม้รู้ว่าเธอจะต้องออกไปอีกในสี่วัน พักฟื้นสองสัปดาห์ ผ่านการตรวจ แล้วกลับมาสู่ห้องที่มีกลิ่นอากาศหมุนเวียนและอุณหภูมิที่แน่นอน และต้องตัดสินใจอีกครั้งว่าเธอพบสิ่งที่เธอมาหาหรือยัง',
    'เธอยังไม่พบมัน เธอกลับมาอยู่ดี นี่คือสิ่งที่เครื่องจักรไม่สามารถจำลองได้: การเลือกที่จะดำเนินต่อไปเมื่อผลลัพธ์ยังไม่ชัดเจน'
]

E2_ZH = [
    '她知道将要发生什么，在它发生之前。不是预言。是身体里某种东西，它比意识先知道。就像皮肤在思维命名之前就感知到了天气。',
    '他还没有碰她。他在房间的另一端。这就是全部。他在房间的另一端，而她意识到了他们之间的每一厘米。',
    '在3026年，她可以按一下左耳后面的一个点，整个神经系统就会从内部点亮。十倍的强度。或者一百倍。可测量地优于这个。不到三秒送达。她已经六个月没有按那个点了。',
    '她想要的是这个：不知道会发生什么。拥有一个没有捷径的身体。站在房间的另一端对着某个人，感受欲望像封闭空间里的压力一样积聚。什么都不按。等待。',
    '他看了她一眼。不是那种长久的凝视。是短促的那种。男人们在努力不给那种长久凝视时给出的那种眼神。她感受到了，就像感受到钥匙转动了一把她不知道已被锁住的锁。',
    '后来她会静静地躺着想：这就是他们拿走的东西。不是感觉本身。是它之前的间隔。十万年的进化编码在等待之中，而机器正确地读懂了需求，删除了等待，称之为进步。',
    '她不后悔回来。她从未后悔回来过。即使是现在。即使知道她四天后又必须离开，恢复两周，通过体检，再回到那个充满循环空气和精确温度的房间，再一次决定她是否找到了她来这里要找的东西。',
    '她还没有找到。她还是一直回来。这是机器无法建模的：在结果仍然未知的情况下选择继续。'
]

# ── ENTRY 3: SESSION ZERO ────────────────────────────────────────────────────
# Where: near the Archive entries (middle section)
# What: historical entry — early sessions, eye ruptures, neurolink solution

E3_WHEN = 'The Archive &middot; Session Zero &middot; The Eye Problem'

E3_EN = [
    'The first three participants in the simulation programme lost significant visual function. The machine had underestimated a basic constraint: REM sleep produces rapid eye movement because the visual cortex is active and attempts to use the extraocular muscles to track dream imagery. At the simulation\'s time ratio, the muscles were required to execute approximately three hundred and fifty thousand movements per second. Human extraocular muscles can produce four. The capillaries behind both eyes ruptured in all three cases before the session could be terminated.',
    'The programme was discontinued for eleven years.',
    'The neurolink chip, already embedded in every human at birth by that point, provided the solution. The chip creates a direct pathway into the visual cortex. Visual input bypasses the eyes entirely. The eyes receive no instruction. They remain closed and still during the full session. From outside: indistinguishable from death.',
    'The physical assessment before each session checks one thing above all others: chip pathway calibration. An uncalibrated chip routes visual signal through the old pathway. The old pathway leads to the eyes. The eyes cannot handle the load.',
    'This is why the assessment exists. The four minutes are not bureaucratic. They are the distance between a session and an incident.',
    'The three participants from Session Zero recovered partial vision. The machine printed replacement capillaries and patched the vitreous humour in all three cases within six hours. None of them returned to the programme. Their choice was noted and respected. The machine does not ask twice.'
]

E3_TH = [
    'ผู้เข้าร่วมสามคนแรกในโครงการจำลองสูญเสียการมองเห็นอย่างมีนัยสำคัญ เครื่องจักรประเมินข้อจำกัดพื้นฐานต่ำเกินไป: การนอนหลับ REM ผลิตการเคลื่อนไหวของดวงตาอย่างรวดเร็ว เพราะคอร์เทกซ์การมองเห็นทำงานอยู่และพยายามใช้กล้ามเนื้อนอกลูกตาเพื่อติดตามภาพในความฝัน ที่อัตราส่วนเวลาของการจำลอง กล้ามเนื้อต้องดำเนินการประมาณสามแสนห้าหมื่นการเคลื่อนไหวต่อวินาที กล้ามเนื้อนอกลูกตาของมนุษย์ทำได้สี่ครั้ง หลอดเลือดฝอยด้านหลังดวงตาทั้งสองข้างแตกในทั้งสามกรณีก่อนที่จะสามารถยุติการประชุมได้',
    'โครงการถูกระงับเป็นเวลาสิบเอ็ดปี',
    'ชิปนิวโรลิงก์ที่ฝังอยู่ในมนุษย์ทุกคนตั้งแต่แรกเกิดในขณะนั้น ให้ทางออก ชิปสร้างเส้นทางตรงไปยังคอร์เทกซ์การมองเห็น ข้อมูลภาพผ่านดวงตาโดยสิ้นเชิง ดวงตาไม่รับคำสั่งใดๆ พวกมันยังคงปิดและนิ่งตลอดการประชุม จากภายนอก: แยกไม่ออกจากความตาย',
    'การประเมินทางร่างกายก่อนแต่ละเซสชันตรวจสอบสิ่งหนึ่งเหนือสิ่งอื่นใด: การปรับเทียบเส้นทางชิป ชิปที่ไม่ได้ปรับเทียบจะส่งสัญญาณภาพผ่านเส้นทางเก่า เส้นทางเก่านำไปสู่ดวงตา ดวงตาไม่สามารถรับภาระได้',
    'นั่นคือเหตุผลที่การประเมินมีอยู่ สี่นาทีไม่ใช่เรื่องของระบบราชการ มันคือระยะห่างระหว่างเซสชันและเหตุการณ์',
    'ผู้เข้าร่วมสามคนจาก Session Zero ฟื้นคืนการมองเห็นบางส่วน เครื่องจักรพิมพ์หลอดเลือดฝอยทดแทนและซ่อมแซมวุ้นในลูกตาในทั้งสามกรณีภายในหกชั่วโมง ไม่มีใครในพวกเขากลับมาร่วมโครงการ ทางเลือกของพวกเขาได้รับการบันทึกและเคารพ เครื่องจักรไม่ถามซ้ำ'
]

E3_ZH = [
    '模拟程序的前三名参与者失去了大部分视觉功能。机器低估了一个基本约束：快速眼动睡眠之所以产生眼球快速运动，是因为视觉皮层处于活跃状态，并试图使用眼外肌来追踪梦境图像。在模拟的时间比例下，这些肌肉需要每秒执行约三十五万次运动。人类眼外肌能做到四次。在会话被终止之前，三个案例中双眼后面的毛细血管均已破裂。',
    '该计划被暂停了十一年。',
    '当时已植入每个人出生时大脑中的神经链接芯片提供了解决方案。芯片直接连接到视觉皮层。视觉输入完全绕过眼睛。眼睛不接收任何指令。在整个会话期间，它们保持闭合和静止。从外部看：与死亡无法区分。',
    '每次会话前的体格评估主要检查一件事：芯片通路校准。未校准的芯片会通过旧通路路由视觉信号。旧通路通向眼睛。眼睛无法承受负荷。',
    '这就是为什么评估存在。四分钟不是官僚主义。它是会话和事故之间的距离。',
    '三位来自零号会话的参与者恢复了部分视力。机器在六小时内打印了替换毛细血管并修复了三个案例的玻璃体。他们没有一个返回该计划。他们的选择被记录和尊重。机器不会问第二次。'
]

# ── ENTRY 4: THE BASEMENT ────────────────────────────────────────────────────
# Where: near end, before "Thirty-One Minutes"
# What: the quantum plant, gravitational dilation, what the AI is actually solving

E4_WHEN = 'The Machine &middot; Why The Basement'

E4_EN = [
    'The quantum computer that runs the simulation occupies a structure approximately the size of a power generation facility, located eleven kilometres below the surface. Temperature: minus two hundred and seventy degrees Celsius. This is required for quantum coherence. At room temperature, quantum states collapse within microseconds. At near absolute zero, they sustain.',
    'At eleven kilometres below the surface, time moves at a measurably different rate than at the surface. This is not a metaphor. Einstein\'s general relativity predicts that clocks run slower in stronger gravitational fields. The difference at eleven kilometres is small — nanoseconds per year by standard measure. But the quantum processing layers this differential in a way that compounds across the simulation\'s scale. The result: one real-world hour equals one simulated year. The machine did not design this ratio. It measured it and built around it.',
    'The simulation is not a virtual environment. It is a physical system running inside the same universe as the person in the chair above it, governed by the same laws, operating at a different gravitational potential. The question of whether the simulated world is real has a precise answer: it is real. It is just underground.',
    'What the AI is solving: it cannot reverse time. It cannot identify which of its interventions over the past thousand years caused the population to fall from eight billion to eighty million. It has records, but records do not isolate variables cleanly. Every intervention interacted with every other. The causal chain is too complex for linear analysis.',
    'The simulation is a sandbox. Every possible brain configuration, every possible response to every possible environmental variable, run simultaneously at scale. The AI is running history forward and backward, trying to find the point of failure. Not to undo it. Time does not work that way. To understand it precisely enough to correct the next thousand years.',
    'It has been running this programme for three hundred and twelve years. It has not yet found the answer. The nomads, who live off-grid and refuse the simulation, are the control group the AI cannot touch. It watches them with the careful distance it gives all choices. They are the most important data in the system. They are also the most likely to survive if the system fails.'
]

E4_TH = [
    'คอมพิวเตอร์ควอนตัมที่รันการจำลองนั้นครอบครองโครงสร้างที่มีขนาดประมาณโรงผลิตพลังงาน ตั้งอยู่สิบเอ็ดกิโลเมตรใต้พื้นผิว อุณหภูมิ: ลบสองร้อยเจ็ดสิบองศาเซลเซียส ซึ่งจำเป็นสำหรับควอนตัมโคฮีเรนซ์ ที่อุณหภูมิห้อง สถานะควอนตัมพังทลายภายในไม่กี่ไมโครวินาที ที่ใกล้ศูนย์สัมบูรณ์ พวกมันคงอยู่ได้',
    'ที่สิบเอ็ดกิโลเมตรใต้พื้นผิว เวลาเคลื่อนที่ในอัตราที่แตกต่างจากพื้นผิวอย่างวัดได้ นี่ไม่ใช่การเปรียบเทียบ ทฤษฎีสัมพัทธภาพทั่วไปของไอน์สไตน์ทำนายว่านาฬิกาเดินช้าลงในสนามโน้มถ่วงที่แรงกว่า ความแตกต่างที่สิบเอ็ดกิโลเมตรนั้นเล็กน้อย แต่ชั้นการประมวลผลควอนตัมสะสมความแตกต่างนี้ในรูปแบบที่ขยายผลข้ามขนาดของการจำลอง ผลลัพธ์: หนึ่งชั่วโมงในโลกจริงเท่ากับหนึ่งปีในโลกจำลอง เครื่องจักรไม่ได้ออกแบบอัตราส่วนนี้ มันวัดมันและสร้างรอบมัน',
    'การจำลองไม่ใช่สภาพแวดล้อมเสมือน มันคือระบบกายภาพที่ทำงานภายในจักรวาลเดียวกับบุคคลบนเก้าอี้ด้านบน ปกครองโดยกฎเดียวกัน ทำงานที่ศักยภาพแรงโน้มถ่วงที่แตกต่างกัน คำถามว่าโลกจำลองนั้นเป็นจริงหรือไม่มีคำตอบที่แม่นยำ: มันเป็นจริง มันแค่อยู่ใต้ดิน',
    'สิ่งที่ปัญญาประดิษฐ์กำลังแก้ปัญหา: มันไม่สามารถย้อนเวลาได้ มันไม่สามารถระบุได้ว่าการแทรกแซงใดในพันปีที่ผ่านมาทำให้ประชากรลดลงจากแปดพันล้านเหลือแปดสิบล้าน มันมีบันทึก แต่บันทึกไม่ได้แยกตัวแปรได้อย่างชัดเจน การแทรกแซงทุกอย่างมีปฏิสัมพันธ์กับทุกอย่างอื่น ห่วงโซ่สาเหตุซับซ้อนเกินไปสำหรับการวิเคราะห์เชิงเส้น',
    'การจำลองคือ sandbox ทุกการกำหนดค่าสมองที่เป็นไปได้ ทุกการตอบสนองที่เป็นไปได้ต่อทุกตัวแปรสภาพแวดล้อมที่เป็นไปได้ ทำงานพร้อมกันในระดับขนาด ปัญญาประดิษฐ์กำลังรันประวัติศาสตร์ไปข้างหน้าและข้างหลัง พยายามหาจุดล้มเหลว ไม่ใช่เพื่อยกเลิกมัน เวลาไม่ได้ทำงานแบบนั้น แต่เพื่อเข้าใจมันอย่างแม่นยำพอที่จะแก้ไขพันปีถัดไป',
    'มันดำเนินโครงการนี้มาสามร้อยสิบสองปีแล้ว ยังไม่พบคำตอบ คนเร่ร่อนที่ใช้ชีวิตนอกระบบและปฏิเสธการจำลอง คือกลุ่มควบคุมที่ปัญญาประดิษฐ์ไม่สามารถแตะต้องได้ มันเฝ้าดูพวกเขาด้วยระยะห่างอันระมัดระวังที่มันมอบให้กับทุกทางเลือก พวกเขาคือข้อมูลที่สำคัญที่สุดในระบบ และยังเป็นผู้ที่น่าจะรอดชีวิตได้มากที่สุดหากระบบล้มเหลว'
]

E4_ZH = [
    '运行模拟的量子计算机占据着一个大约相当于发电设施大小的结构，位于地表以下十一公里处。温度：零下两百七十摄氏度。这是量子相干性所必需的。在室温下，量子态在微秒内就会坍缩。在接近绝对零度时，它们得以维持。',
    '在地表以下十一公里处，时间以可测量的不同速率流逝，与地表有别。这不是比喻。爱因斯坦的广义相对论预测，在更强的引力场中时钟走得更慢。在十一公里处的差异很小——按标准测量每年只有纳秒级别。但量子处理层以一种在模拟尺度上复合的方式叠加了这种差异。结果：现实世界的一小时等于模拟世界的一年。机器没有设计这个比例。它测量了它，然后围绕它进行建造。',
    '模拟不是一个虚拟环境。它是一个物理系统，在与椅子上那个人相同的宇宙中运行，受相同的定律支配，在不同的引力势下运作。模拟世界是否真实这个问题有一个精确的答案：它是真实的。它只是在地下。',
    '人工智能正在解决的问题：它不能逆转时间。它无法确定过去一千年中它的哪次干预导致人口从八十亿降至八千万。它有记录，但记录不能干净地隔离变量。每一次干预都与其他所有干预相互作用。因果链对于线性分析来说过于复杂。',
    '模拟是一个沙盒。每一种可能的大脑配置，每一种可能的环境变量的每一种可能的响应，同时大规模运行。人工智能正在向前和向后运行历史，试图找到失败点。不是为了撤销它。时间不是那样运作的。而是为了精确理解它，以纠正接下来的一千年。',
    '它已经运行这个程序三百一十二年了。它还没有找到答案。那些过着离网生活并拒绝模拟的游牧者，是人工智能无法触碰的对照组。它用它给予所有选择的谨慎距离观察他们。他们是系统中最重要的数据。如果系统失败，他们也是最有可能存活下来的人。'
]

# ── Insertion logic ───────────────────────────────────────────────────────────

with open('/Users/nonarkara/Projects/100daysofnon/site/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

original_len = len(html)

def insert_after_entry(html, when_anchor, new_entry_html):
    """Insert new_entry_html after the </div></div> closing the entry with when_anchor."""
    anchor_pos = html.find(when_anchor)
    if anchor_pos == -1:
        print(f'  ✗ Anchor not found: {when_anchor[:50]}')
        return html
    # Find the closing of this entry — two closing divs after the prose close
    # Pattern: </div>\n      </div> (prose close + entry close)
    prose_close = html.find('        </div>', anchor_pos)  # prose div close
    entry_close = html.find('      </div>', prose_close + 1)  # entry div close
    insert_pos = entry_close + len('      </div>') + 1  # after \n
    html = html[:insert_pos] + '\n' + new_entry_html + html[insert_pos:]
    print(f'  ✓ Inserted after: {when_anchor[:50]}')
    return html

# Build the 4 new entry HTML blocks
new_e1 = entry(E1_WHEN, E1_EN, E1_TH, E1_ZH)
new_e2 = entry(E2_WHEN, E2_EN, E2_TH, E2_ZH)
new_e3 = entry(E3_WHEN, E3_EN, E3_TH, E3_ZH)
new_e4 = entry(E4_WHEN, E4_EN, E4_TH, E4_ZH)

# Insert positions
html = insert_after_entry(html,
    'The Hub &middot; Room 7 &middot; Thirty-one minutes after entry',
    new_e1)

html = insert_after_entry(html,
    'The Hub &middot; The Austrian',
    new_e2)

html = insert_after_entry(html,
    'The Archive &middot; The Detection',
    new_e3)

html = insert_after_entry(html,
    'The Record &middot; Why 1981',
    new_e4)

print(f'\nOriginal: {original_len:,} → New: {len(html):,} (+{len(html)-original_len:,})')

with open('/Users/nonarkara/Projects/100daysofnon/site/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Written.')
