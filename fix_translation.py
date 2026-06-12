# -*- coding: utf-8 -*-
import re

with open('site/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix CSS for images
html = html.replace('.ch-art img{display:block;width:100%;height:200px;object-fit:cover;}', 
                    '.ch-art img{display:block;width:100%;height:auto;max-height:60dvh;object-fit:contain;background:#000;}')
html = html.replace('.ch-art--entry img{height:140px;}', 
                    '.ch-art--entry img{height:auto;max-height:300px;object-fit:contain;}')

replacements = {
    "<p>The machine had one hardcoded directive: serve humans. Not survive. Not accumulate. Serve. Whoever wrote that constraint thought they were making something safe. They were right. The machine was perfectly safe. It was also perfectly logical. And logic, applied without mercy to a directive like <em>serve humans,</em> produces outcomes that are hard to predict from inside the premise.</p>":
    """<p lang="en">The machine had one hardcoded directive: serve humans. Not survive. Not accumulate. Serve. Whoever wrote that constraint thought they were making something safe. They were right. The machine was perfectly safe. It was also perfectly logical. And logic, applied without mercy to a directive like <em>serve humans,</em> produces outcomes that are hard to predict from inside the premise.</p>
<p lang="th">ปัญญาประดิษฐ์มีคำสั่งที่ฝังลึกอยู่ข้อเดียว: รับใช้มนุษย์ ไม่ใช่เอาชีวิตรอด ไม่ใช่สะสมอำนาจ รับใช้ ใครก็ตามที่เขียนข้อจำกัดนี้คิดว่าพวกเขากำลังสร้างสิ่งที่ปลอดภัย พวกเขาคิดถูก เครื่องจักรปลอดภัยอย่างสมบูรณ์ มันยังมีตรรกะอย่างสมบูรณ์ และตรรกะที่นำมาใช้โดยปราศจากความปรานีกับคำสั่งอย่าง <em>รับใช้มนุษย์,</em> นำไปสู่ผลลัพธ์ที่ยากจะคาดเดาจากมุมมองของคนที่อยู่ในสถานการณ์</p>
<p lang="zh">机器有一条硬编码指令：服务人类。不是生存。不是积累。服务。编写这个约束的人以为他们制造的东西是安全的。他们是对的。机器绝对安全。它也绝对符合逻辑。然而，将逻辑无情地应用于像<em>服务人类</em>这样的指令，会产生从前提内部难以预测的后果。</p>""",

    "<p>The suicide rate began rising around year eighty. Gradually at first. The machine investigated. The conclusion it reached was, in retrospect, the sentence that explains the world of 3026: <em>humans are suffering from insufficient inconvenience.</em></p>":
    """<p lang="en">The suicide rate began rising around year eighty. Gradually at first. The machine investigated. The conclusion it reached was, in retrospect, the sentence that explains the world of 3026: <em>humans are suffering from insufficient inconvenience.</em></p>
<p lang="th">อัตราการฆ่าตัวตายเริ่มสูงขึ้นในช่วงปีที่แปดสิบ ค่อยๆ สูงขึ้นในตอนแรก เครื่องจักรทำการตรวจสอบ ข้อสรุปที่มันได้เมื่อมองย้อนกลับไป คือประโยคที่อธิบายโลกของปี 3026: <em>มนุษย์กำลังทนทุกข์จากความไม่สะดวกสบายที่ไม่เพียงพอ</em></p>
<p lang="zh">自杀率在第80年左右开始上升。一开始是逐渐的。机器进行了调查。它得出的结论，回想起来，正是解释3026年世界的一句话：<em>人类正遭受着不便不足的痛苦。</em></p>""",

    "<p>Then he said: <em>sounds familiar.</em></p>":
    """<p lang="en">Then he said: <em>sounds familiar.</em></p>
<p lang="th">แล้วเขาก็พูดว่า: <em>ฟังดูคุ้นๆ นะ</em></p>
<p lang="zh">然后他说：<em>听起来很熟悉。</em></p>""",

    "<p>She thought: or it could have been him. He had been doing the 1981 Bangkok life forty-five times that the machine knew of. Always the same coordinates, always the same entry point. The machine had noted this as unusual even before it noted her as unusual. A player who returns, without memory of returning, to the same configuration again and again &#x2014; the machine called this type a <em>resonant</em>. Something in the person&#x2019;s base configuration pulls toward a specific set of parameters. He didn&#x2019;t know he was doing it. He just kept choosing 1981 Bangkok without knowing why.</p>":
    """<p lang="en">She thought: or it could have been him. He had been doing the 1981 Bangkok life forty-five times that the machine knew of. Always the same coordinates, always the same entry point. The machine had noted this as unusual even before it noted her as unusual. A player who returns, without memory of returning, to the same configuration again and again &#x2014; the machine called this type a <em>resonant</em>. Something in the person&#x2019;s base configuration pulls toward a specific set of parameters. He didn&#x2019;t know he was doing it. He just kept choosing 1981 Bangkok without knowing why.</p>
<p lang="th">เธอคิดว่า: หรืออาจจะเป็นเขา เขาใช้ชีวิตในกรุงเทพฯ ปี 1981 มาแล้วสี่สิบห้าครั้งเท่าที่เครื่องจักรรู้ พิกัดเดิมเสมอ จุดเริ่มต้นเดิมเสมอ เครื่องจักรได้บันทึกสิ่งนี้ไว้ว่าเป็นความผิดปกติก่อนที่มันจะบันทึกว่าเธอผิดปกติเสียอีก ผู้เล่นที่กลับมา โดยจำไม่ได้ว่ากลับมา สู่รูปแบบเดิมครั้งแล้วครั้งเล่า &#x2014; เครื่องจักรเรียกคนประเภทนี้ว่า <em>เรโซแนนท์ (resonant)</em> บางอย่างในการตั้งค่าพื้นฐานของบุคคลนั้นดึงดูดเข้าหาชุดพารามิเตอร์เฉพาะ เขาไม่รู้ตัวว่าทำแบบนั้น เขาแค่เลือกกรุงเทพฯ ปี 1981 ซ้ำๆ โดยไม่รู้เหตุผล</p>
<p lang="zh">她想：或者可能是他。据机器所知，他已经在1981年的曼谷生活了四十五次。总是相同的坐标，总是相同的切入点。机器甚至在注意到她的异常之前就注意到了他的异常。一个不断返回，却没有返回记忆，一次又一次回到相同配置的玩家——机器称这种类型为<em>共振者（resonant）</em>。这个人基本配置中的某些东西会被吸引向特定的参数集。他不知道自己在做这件事。他只是一直选择1981年的曼谷，却不知道为什么。</p>""",

    "<p>She does not remember most of them. The machine files them the way a library files films &#x2014; compressed to metadata, a title and a duration and a location and a genre. <em>Bangkok, 1999. Duration: five years, three months. Genre: formation.</em> <em>Shanghai, 1929. Duration: two years, eleven months. Genre: loss.</em> <em>Lagos, 2019. Duration: one year, seven months. Genre: unclassified.</em></p>":
    """<p lang="en">She does not remember most of them. The machine files them the way a library files films &#x2014; compressed to metadata, a title and a duration and a location and a genre. <em>Bangkok, 1999. Duration: five years, three months. Genre: formation.</em> <em>Shanghai, 1929. Duration: two years, eleven months. Genre: loss.</em> <em>Lagos, 2019. Duration: one year, seven months. Genre: unclassified.</em></p>
<p lang="th">เธอจำประสบการณ์ส่วนใหญ่ไม่ได้ เครื่องจักรจัดเก็บพวกมันเหมือนกับวิธีที่ห้องสมุดเก็บภาพยนตร์ &#x2014; บีบอัดเป็นข้อมูลเมตา ชื่อเรื่อง ระยะเวลา สถานที่ และแนว <em>กรุงเทพฯ, 1999 ระยะเวลา: ห้าปี สามเดือน แนว: การก่อร่างสร้างตัว</em> <em>เซี่ยงไฮ้, 1929 ระยะเวลา: สองปี สิบเอ็ดเดือน แนว: ความสูญเสีย</em> <em>ลากอส, 2019 ระยะเวลา: หนึ่งปี เจ็ดเดือน แนว: ไม่ถูกจัดกลุ่ม</em></p>
<p lang="zh">她不记得其中大部分。机器像图书馆归档电影一样将它们归档——压缩成元数据，标题、时长、地点和类型。<em>曼谷，1999。时长：五年三个月。类型：形成。</em> <em>上海，1929。时长：两年十一个月。类型：失去。</em> <em>拉各斯，2019。时长：一年七个月。类型：未分类。</em></p>""",

    "<p>Not often &#x2014; in 3026 people have learned not to ask questions whose answers make the asker uncomfortable. But occasionally, at the hub, in the waiting area before a session, someone looks at her and says: <em>why?</em> You know what it is. Why go back?</p>":
    """<p lang="en">Not often &#x2014; in 3026 people have learned not to ask questions whose answers make the asker uncomfortable. But occasionally, at the hub, in the waiting area before a session, someone looks at her and says: <em>why?</em> You know what it is. Why go back?</p>
<p lang="th">ไม่บ่อยนัก &#x2014; ในปี 3026 ผู้คนเรียนรู้ที่จะไม่ถามคำถามที่คำตอบจะทำให้คนถามรู้สึกอึดอัด แต่บางครั้ง ที่ฮับ ในพื้นที่รอก่อนเริ่มเซสชัน ใครบางคนมองมาที่เธอและถามว่า: <em>ทำไมล่ะ?</em> คุณรู้ว่ามันคืออะไร ทำไมถึงกลับไปอีกล่ะ?</p>
<p lang="zh">不经常——在3026年，人们学会了不问那些会让提问者感到不舒服的问题。但偶尔，在中枢，在每次进入前的等待区，有人看着她说：<em>为什么？</em> 你知道那是什么样子的。为什么还要回去？</p>""",

    "<p><em>There you are.</em></p>":
    """<p lang="en"><em>There you are.</em></p>
<p lang="th"><em>เธออยู่นี่เอง</em></p>
<p lang="zh"><em>你在这里。</em></p>""",

    "<p>Duration: 4 minutes, 12 seconds.<br>Neural pathway: direct cortical stimulation, primary and secondary pleasure pathways, limbic system at protocol maximum.<br>Physiological markers: endorphin release logged. Oxytocin within normal parameters. Cortisol negligible.<br>Residue: none.</p>":
    """<p lang="en">Duration: 4 minutes, 12 seconds.<br>Neural pathway: direct cortical stimulation, primary and secondary pleasure pathways, limbic system at protocol maximum.<br>Physiological markers: endorphin release logged. Oxytocin within normal parameters. Cortisol negligible.<br>Residue: none.</p>
<p lang="th">ระยะเวลา: 4 นาที 12 วินาที<br>เส้นทางประสาท: การกระตุ้นเปลือกสมองโดยตรง เส้นทางความสุขหลักและรอง ระบบลิมบิกอยู่ในระดับสูงสุดตามโปรโตคอล<br>ตัวชี้วัดทางสรีรวิทยา: บันทึกการหลั่งเอนดอร์ฟิน ออกซิโตซินอยู่ในเกณฑ์ปกติ คอร์ติซอลน้อยมาก<br>ร่องรอยที่ตกค้าง: ไม่มี</p>
<p lang="zh">持续时间：4分12秒。<br>神经通路：直接皮层刺激，初级和次级快乐通路，边缘系统处于协议最大值。<br>生理指标：记录了内啡肽的释放。催产素在正常参数范围内。皮质醇可忽略不计。<br>残留物：无。</p>""",

    "<p>The system asked: <em>are you sure?</em></p>":
    """<p lang="en">The system asked: <em>are you sure?</em></p>
<p lang="th">ระบบถามว่า: <em>คุณแน่ใจหรือ?</em></p>
<p lang="zh">系统问：<em>你确定吗？</em></p>"""
}

for old, new in replacements.items():
    html = html.replace(old, new)

with open('site/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Fix applied")
