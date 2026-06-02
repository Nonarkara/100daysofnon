# Artifact — Chulalongkorn Vice-Rector Meeting, 2026-05-27 (today)

**Files in this artifact bundle:**

- `2026-05-27-chula-vice-rector-meeting-transcript-raw.txt` — full Thai-language transcript with timestamps, ~33 minutes (recorded during the meeting)
- `2026-05-27-chula-vice-rector-meeting-photo-52bd77a4.png` — screenshot of the Chula Engineering faculty page showing the vice-rector's official bio
- `2026-05-27-chula-vice-rector-meeting-photo-b711e3d7.jpg` — screenshot of the **Chula Control Tower** dashboard Non built on the BTS ride over (the live demo shown to the vice-rector)
- `2026-05-27-chula-vice-rector-meeting-summary.md` — this file: Non's framing + meeting distillation + cross-references

**Filed forward to Day 72 — Phase 6** *The Chonburi / Bangkok / Thailand smart-city work* — same Phase 6 home as the Chonburi anniversary lecture (2026-05-22). This is the **Bangkok** half of that question's premise.

---

## Who Non met with

**รศ.ดร. มาโนช โลหเตปานนท์ (Assoc. Prof. Manoj Lohatepanont, Sc.D.)** — Vice-Rector, **Chulalongkorn University**, in charge of campus design and property (academic-zone side). Faculty of Engineering, Civil Engineering department. **Sc.D. from MIT** (Doctor of Science — the MIT terminal degree). Office in the prestigious central building, accessible from National Stadium BTS via Sasin.

The two-decades-ago connection Non mentions in his framing: Manoj came to give a talk to Non's cohort ~20 years ago, as a Fulbright candidate about to apply for grad school. *Manoj is part of why Non aimed at MIT in the first place — and Non did get in.* Non told Manoj this in the meeting; Manoj was pleased; the conversation was warm even while Non was technically dominating it.

The Vice-Rector's portfolio splits with another VR: **Manoj covers the Academic zone** (the central campus heart, faculties, university operations), the **other VR covers Commercial** (Siam Square, Siam Discovery, Siam Paragon, the area MBK occupies that Chula leased out *"and won't give back"*, EkkaMai building, etc.). This split matters for any engagement scoping.

---

## Non's framing (verbatim)

> This is from the meeting with the vice-rector of Sri Lanka University in charge of campus design and property. Legend had it that I decided just when I was riding a BTS Skytrain from my house over to the university (which I would have gotten off at National Stadium Station and walked over via Sasin to the building where his office is located, right in the heart of the campus). The most prestigious building where the office of the vice-rector should be.
>
> I decided that I wanted to create a digital twin that can do 2D and 3D infrastructure. As we remove buildings, we can see underneath because I knew that he went to MIT and studied civil engineering. I actually did meet him 20 years ago when he came to give a talk for us. He was a Fulbrighter who was about to apply for graduate school, and I think because of him partly I really wanted to go to MIT, which I did and got in. I told him that, and he was really happy, so it was really jovial in the sense that at the same time I was totally dominating him. I was pretty much telling him that, within 45 minutes of the BTS ride, I decided that just come and talk to you and get the requirement from you would be boring for you and for me, so I would just imagine what you would need and I just created it. In 45 minutes I was able to come up with not a demo, it's a full system, because I already did some dashboards, right. I have all these templates that Claude Code has already organized for me. We can pull them easily into the dashboards and then build it up very easily. By the time I arrived and had to walk over to see him, I already had a dashboard pre-built, and all the data are coming in in real time as they connect to the internet. It's connected to GitHub. GitHub is deployed over CloudFlare as the tunnel over to the internet, and then you can see it from your phone or anywhere else as long as you connect to the internet.
>
> I don't even do localhost anymore because I want to know that all my systems are liveable. If that's not the case, then localhost doesn't mean much to me. The localhost only means much when I run all these micro programs, like all these bots that I'm running. I need localhost, but apart from that, for things that I needed to get people to actually get access to, I want that my first stage to be the fact that it actually gets past to the internet. Otherwise, there's no point making it at all.
>
> He was really stunned that I was able to do it in 45 minutes, because these are the things that, less than a year ago, it would have cost him two or three million baht easily on the spot, just for the demo of the real site. I was able to do it in 45 minutes. Of course he knew I was a genius, of course he knew I am a genius, but then the point is I was able to do it too, so it's a genius who can do things and not just talk. This was a conversation after we sat on the same side because the TV was broken and couldn't connect to my Mac, so we had to sit on the same side. I showed him on my 16-inch 8000 computer screen, which I told him about as well, because I needed it to compute all these that I did this in 45 minutes on the BTS ride.

A note on the nickname: "Sri Lanka University" is Non's playful nickname for **Chulalongkorn**. The transcript is unambiguously Chula (จุฬา) throughout; the screenshots are Chula's eng.chula.ac.th faculty page and the Chula Control Tower dashboard. Non's nickname stays in his framing per the standing rule.

---

## The Chula Control Tower dashboard (what's actually in the photo)

The dashboard Non demoed is branded **"Chula Control Tower / Chulalongkorn University, Bangkok / CT-01"**. From the screenshot:

- **Top bar:** city status modules, world-clock strip (San Francisco / Boston / London / Singapore / Tokyo / Sydney) — the visual signature of a war-room console, not a tech-demo
- **Main view:** 3D buildings on top of central Bangkok aerial imagery, the Chula campus footprint with **building heights inferred from satellite shadow length** (Non's "ninja trick" — he had no building data, so he asked the AI to estimate height from shadows; he flagged this to the VR as something to replace with real data once NDA is in place)
- **Left rail:** city reports, news/markets, ASK QUALITY, PROJ PORTFOLIO (12 / 0), MATERIAL LASS (faculty buildings: Roma 1, Roma R, Phong Tho, Henri Du...), PARKING & CARRIERS (1,673 / 12,000), CO POP Box, MJoMI, basis counters, ANYWHERE bilas, Hospice 015, Sponsor 24
- **Right rail:** TRENDS / FORECAST / SCHEDULES, embed of the **Chulalongkorn University Facebook page** showing the current **"ARCH CU EXPO 2026: Design for Future Living"** event (Faculty of Architecture's 92nd anniversary, May 18-29, 2026)
- **Bottom:** ASK CCT (chat-with-the-dashboard input), Weekday/Weekend toggle

The Facebook embed pulls in real time. The news layer refreshes every 5 minutes. Satellite imagery (NASA + JAXA) refreshes every 24 hours. The whole thing runs on GitHub Pages → CloudFlare tunnel → public URL. No localhost.

---

## What happened in the meeting — the substance

### 1. The demo (~00:00 – 04:00)

Non walks in with the dashboard already built. Shows the God Mode view, the 2D/3D toggle, satellite layers (NASA + JAXA), the news layer, the infrastructure layers (fire hoses around campus pulled from the **กฟภ. / Bangkok Metropolitan electricity authority**), the building-height-from-shadow trick. Says he built it on the BTS ride because *"just coming to talk to you and gather requirements would be boring for you and for me."*

### 2. The VR's response (~04:00 – 05:00)

*"Chula has been trying to do this for years. The vendors that come in keep saying 'you need this, you need that' but don't deliver, and some of them don't understand our nature — we've been here a hundred years, the infrastructure is already in the ground, you can't come in and do greenfield. This is the first thing I've seen that actually understands our nature."*

The Vice-Rector's pitch back to Non:

- **Use Chula as a sandbox for the whole city** — the campus is big enough to count as a small city, has users, has IoT (some), can stress-test patterns before pushing them out to Bangkok proper
- **The C-suite (rector level) wants:** Actual Utilization + Consumption metrics per faculty/building, PM (air quality), Energy
- **What they have today:** basic graphs, PLC sensors, but every new dashboard requires writing an application from scratch. They want the *substrate* Non just showed.

### 3. The NSP demo as the closer (~05:00 – 07:00)

Non pivots to the **National Streaming Platform** (same one shown at Chonburi, same one running in code-task all week). Reveals that he undercut the official quote: government said the NSP would cost **200 million baht** to start and the pilot alone would cost **20 million**. Non built the working prototype last night. *"My version uses the 'ninja method' — bypass the broadcast pipeline entirely, run the whole thing as a digital twin on my second-hand computer. No telco, no broadband pipeline, no contract."* Estimate: a real-deployment version would cost under **10 million**, not 200.

### 4. The Phuket war-room demo (~07:00 – 09:00)

Same demo Non used at Chonburi: real-time traffic, accident hotspots, topography overlay (red dots = accident locations cluster on the hills, which is the diagnostic), satellite, marine (because of the airport), tide tracking. *"I'm not charging Phuket because the friend who connected me is doing me a favor. But the system itself is set up; I'm done with the architecture."*

### 5. The Nakhon Si Thammarat dependent-population system reveal (~09:00 – 10:30)

Non shows the **citizen-complaint LINE bot + AI-assisted intake** dashboard. Brutal stat:

> Dr. [name] at NECTEC took 7 years and 100 million baht to build the same thing.
> **I built it last week in 45 minutes.**

What makes Non's version better than NECTEC's: an AI in the back that explains *why* each complaint is stuck — which agency, what category, what's blocking it — without operators having to write the rule base. The intake is single-image: send one photo, the system extracts GPS + timestamp + IP from EXIF, validates it's not a stale photo or a fake-IP submission, runs an NSFW/abuse filter (because *"some people just send dick pics into the system, I had to add a screening filter"*), and routes the case automatically.

### 6. The engagement structure proposal (~10:30 – 16:30)

Non lays out the deal mechanically:

- **Deliverable:** free
- **Engagement vehicle:** **SLIC** asks for a *study budget* to send people in to learn what Chula's faculties actually need. The Vice-Rector provides the *endorsement* that opens doors to the operational units inside Chula.
- **Why not depa directly:** depa engagement = "everything has to be slow, royal-protocol, ceremony every time." SLIC moves faster.
- **NDA needed** because Non needs real building/floor/utility data instead of his ninja-guesses. The VR confirms — Academic zone NDA is straightforward.
- **Cost basis on Non's side:** ~200,000 baht for his machine (had to spend it because he needs **128GB to run Qwen 35 locally** for client work under NDA where data can't leave the device). CapEx already paid. *"Now I can do this for anyone for free."*

The VR's confirmation: *"OK — if we proceed, the engagement will be via the SLIC company, not depa."* Non: *"Yes. depa can be the brand stamp to make it look legitimate, but the operational vehicle is SLIC."*

### 7. The C-suite priorities, in the VR's own words (~21:00 – 22:00)

> **First priority: Energy.** Especially AC — Chula has to replace the entire AC system at some point, and we need to track it through that transition. **SDG, carbon-neutral, net-zero by 2040–2050** are increasing in importance. How can we monitor whether emissions actually decline?
>
> So it's not just about energy directly, but **carbon accounting** too, once the data is flowing.

Non's response: he can count trees from satellite imagery for the carbon-offset side (asks for the tree ID layer; says it'll appear in the GitHub-deployed dashboard in 5 seconds once he has the IDs). For consumption, he'll need fire-hose access to the building-level meters.

### 8. The job offer (~26:00 – 27:00)

The VR offers Non a role: **Chulalongkorn's new AI Center** is being built; the previous director has rotated out; the VR is the interim caretaker but doesn't have bandwidth and needs to hand it off. Asks Non if he'd consider coming on **full-time as AI Office** — *"someone with credentials, mid-career, to lead AI development for the university."*

Non's counter: *"Let me come in as **Practitioner in Residence** first, not full director. Don't want to overcommit. I'm interested in the supercomputer-utilization question first — applied AI in academic settings. I see my friend at KMUTL has a supercomputer sitting unused; I asked if I could move in and use it because every second on a real cluster turns my 5–20-second prompts into 1 millisecond."*

The VR likes this: *"Yes — that's our exact problem. We have universities, we have the equipment, we don't have utilization. That's the brief."*

### 9. The personal closer (~25:00 – end)

VR asks if Non is still abroad. Non: *"No, I came back. Mom went to Boston with my brother, didn't like it. I went to teach at NYU Shanghai for 3 years and brought her every month, she didn't like that either. Dad passed several years ago. So mom doesn't move. I came back. And Thailand isn't as bad as it was 20 years ago when I was trying to get out — we get 35 million tourists now, must be doing something right."*

VR's wrap: *"We'll send a team next week, scope what we actually have inside the house, then come back. Let's drive the academic side first; the commercial side will join later."*

---

## Three things this artifact establishes for the first time

### A. The vice-rector by name: Manoj Lohatepanont (MIT Sc.D., Chula CivE)

A named contemporary peer with a 20-year-old connection back to the Fulbright talk that helped point Non at MIT. This is a *long arc* — the Fulbright scholar who inspired the high-schooler is now the Vice-Rector offering the now-mid-career-architect a directorship at the university's AI Center. Worth holding.

### B. The "no localhost" shipping principle, named on the record

> *"I don't even do localhost anymore because I want to know that all my systems are liveable. If that's not the case, then localhost doesn't mean much to me. The localhost only means much when I run all these micro programs, like all these bots that I'm running."*

This is the **Non shipping principle** in its current form (2026): GitHub → CloudFlare tunnel → public URL from the first frame. Local-only is reserved for bots and dev infra. If a system isn't reachable from a stranger's phone the moment it exists, it's not finished — it's not even started.

### C. The SLIC engagement vehicle is now explicit

SLIC (the unit Non uses for funded academic engagements — distinct from depa, which is policy-only) is the contracting entity for the Chula work. The currently-running **SLIC index v3** code-task (overnight, for tomorrow's TKC class) is the *tooling layer* that this engagement plugs into. Worth a project memory.

---

## Cross-references

### To the **Chonburi AlphaEarth code-task** (local_f5ba5cff)

The Chula Control Tower dashboard uses the same satellite + 3D-buildings + news + Facebook-embed substrate the Chonburi AlphaEarth pilot is building toward. **Three deployment targets now share the substrate:** Nakhon Si Thammarat (live, 4 years), Chonburi (in production), Chula campus (just initiated). Treat the substrate as one codebase, three skins. The embedding-based change detection layer the AlphaEarth pilot is building should be portable to all three — Chula will want it for *building utilization changes over time* (vacant office detection, foot-traffic shift detection from satellite).

### To the **SLIC index v3 code-task** (local_691d60e3)

SLIC is the contracting entity for the Chula academic-zone engagement. The SLIC index v3 work isn't *only* tomorrow's TKC class material — it's also the operational backbone for the Chula deal that's just being scoped. Worth a heads-up to that task.

### To the **TKC code-task** (local_2391dc11)

The "ninja method" / 45-minute-prototype / build-first-write-TOR-around-it principle keeps showing up across three engagements in two weeks (Nakhon Si Thammarat, Chonburi, Chula). The TKC game manual should reflect this is not an attitude — it's *the methodology*. Three case-study slots in the manual: Mayor Ganop (4-year track record), Mayor of Chonburi (current build), VR Manoj of Chula (today's initiation). One pattern, three audiences, escalating institutional weight.

### To the **100daysofnon project** (Phase 5 — career arcs)

The 20-year Manoj → MIT → return-to-Thailand → Manoj-offers-AI-Center arc is *biographical material* worth cross-referencing into Phase 5 when career arcs are filed. The Fulbright-talk-that-pointed-young-Non-at-MIT detail is the *origin* of the MIT decision; the AI Center offer is the *closing* of that arc 20 years later.

### To **Day 72's original question** (`question.md`)

> *"The Chonburi / Bangkok / Thailand smart-city work. The client behind it. What you tell them versus what you actually believe about whether smart-city tech helps."*

The Chula meeting closes the Bangkok half of the premise. Combined with the Chonburi lecture artifact, Day 72's frame is now: three live municipal/institutional engagements (Nakhon Si Thammarat / Chonburi / Chula), one platform, one shipping principle, three different client cultures. The honest-belief question (does smart-city tech help, or is Non running a high-quality version of a category that doesn't really work?) is now sharper because the Chula VR explicitly said the C-suite wants *carbon-neutral-by-2050 tracking*, which is a soft KPI by smart-city failure-mode standards. Non's actual belief on whether that KPI is real or theatrical is the next thing to surface.
