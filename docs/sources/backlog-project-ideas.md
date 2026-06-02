# Backlog — project ideas Non surfaced during the 100 days

Things Non has dropped into chat as *"remind me about this"* or *"this is a project I have in my mind right now"* but hasn't yet asked to start. Each entry stays here until either (a) he greenlights it as a real project to spin up, or (b) he decides to drop it.

The agent memory holds a parallel project-memory entry for each so the right context-trigger surfaces the idea back to him in conversation.

---

## 2026-05-25 — Personal photo-search app (browser, ~1TB hard drive, natural-language search)

**Verbatim ask:**

> Remind me at some point that I wanted to create this personal-use app where I will throw all the photos that I have into a hard drive. It's probably in 1 TB of data. The system that I wanted to use, maybe through a browser, is the kind whereby I can search any photos I want. These are like my library, a window to the data in the hard drive, but it's intuitive because I can search based on words. I can just use generative AI to say things, and then it searched for me that photo, which, by the way, is something that even Google Photos cannot do yet. You can't even say, "Find a young photo of me" and start from the foundation, which is the file naming itself, all the way up to the HTML in the browser where I can access these photos. We'll talk about it, but this is a project I have in my right now.

**The bar Non set:** *better than Google Photos at "find a young photo of me"* — i.e., self-recognition across time, not just object detection.

**Stack pre-thoughts (kept light until he asks):**
- Local-first on his M5 Max
- CLIP for general image embeddings + a dedicated face-embedding model (ArcFace / InsightFace) keyed to his face
- SQLite / DuckDB for the index, embeddings as vector columns
- Python + FastAPI backend; Next.js or plain HTML frontend
- File naming as the *foundation* layer per his spec — pipeline renames files semantically as part of indexing, not just attaching metadata
- The data set bootstraps naturally on the photos already accumulating in `100daysofnon/diary/day-*/artifacts/` and his ~1TB external drive

**Connection points to existing projects:**
- Could be a module of nonarkara.org (the memory palace personal-OS framing fits)
- Could be standalone
- The 100-days project is already accumulating photographic artifacts — natural seed corpus

**Trigger for surfacing:**
- Any chat where Non mentions photos, photo storage, photo organization, his hard drive, image search, Google Photos, image embeddings, CLIP, family albums
- Any time he's looking for a specific photo and can't find it
- The Day 1 standing artifact invitations (toddler-Pollock photo, row-house photos, etc.) — this app could BE the surface where those artifacts get processed

---

## 2026-05-27 — Faceless YouTube channel as the AI content engine for Non's authority

**Source Non flagged:** a long Thai-language Facebook post summarizing a video by an "AI Master" course-seller titled *"How I Use AI to Automate Content Creation - Step-by-Step Guide (2026)"*. Course seller is the same person who runs the Facebook page *Claude code for Automation & Webapp* — their pitch is the 3,000-baht/month Claude Max stack as their "dev team that works 24 hours, doesn't quit, doesn't ask for raises, takes orders in Thai." Group at facebook.com/groups/876794776824876.

**The architecture from the post (verbatim distillation):**

A **4-agent pipeline** running on the creator's own platform (Non can reproduce with Claude/ChatGPT directly):

1. **Hook Pilot** — specializes in the first 10 seconds; generates multiple hook variants in the host's voice
2. **Script Writer** — takes brief + voice note + channel DNA, produces full script with visual-cue markers (yellow = real host voice, blue = AI voice via ElevenLabs, purple = AI Avatar via HeyGen). Recommended ratio: **10–15% real voice, 50–60% AI voice, 25–35% Avatar**.
3. **Ad Smith** — handles product/sponsor reads so they blend with the script
4. **AI Producer** — wired to YouTube Analytics, can answer *"what should I make next?"* by cross-referencing performance with search trend, returns 5 ideas with reasoning

**Tooling stack:**
- ElevenLabs for voice clone (Professional Clone, not Instant; V3 not V2 — V3 reduces source-accent)
- HeyGen for AI Avatar (multi-angle recording for natural eye movement)
- Shure SM7B or Blue Yeti mic + closet-with-clothes recording booth, 30+ minutes of clean voice
- Editor in India at ~$75/clip, 24–48h turnaround (the post is emphatic: *"AI ตัดต่อวิดีโอไม่ได้จริงๆ"* — AI can't do real editing yet; outsource to human)
- Thumbnail technique: pull reference from top-performing videos in niche (500K+ views), upload required assets, prompt for composition + mood without micro-controlling pixels

**The five DNA layers** that have to be set before any agent runs (else the AI sounds like a robot):
1. **Niche** — narrow ("AI tools for content creators" > "technology")
2. **Persona** — ghostwriter-brief level of detail (background, energy, explanation style)
3. **Products/services** the channel sells
4. **Voice guidelines** — how it speaks
5. **Compliance rules** — sponsor disclosure, etc.

**The hard rules from the post:**
- Never open with the Avatar — first 10 seconds MUST be real voice or high-energy voiceover. Avatars are for the middle.
- AI provides *structure*; voice notes from the human provide *substance*. Skipping the voice notes = generic-sounding fail.
- Search-driven content plan (how-to, comparison, tutorial) is non-negotiable for an Expert channel — *"don't make up topics; steal what's already working and add your expertise."*

**Cost math (from the post):**
- $75/clip × daily posting = ~$2,250/month ≈ 80,000 baht
- Start at 2–3/week, scale only when revenue model is proven

**Why this fits Non specifically — connections to the existing portfolio:**

- Non already runs **OpenClaw council** — a multi-agent architecture. The 4-agent pipeline above maps directly onto an OpenClaw council with personas: Hook Pilot, Script Writer, Ad Smith, Producer. No new infra needed; just new personas.
- Non already uses **Whisper Flow** for voice transcription daily — the "voice note input" layer is already in his workflow.
- Non gives **hundreds of talks per year** (per Day 3 Msg 6: *"I'm now like a speaker, a world-class speaker who speaks a couple hundred times a year now"*). Each talk is already content with no current public surface. A faceless YouTube channel could be the *scaling layer* for talks that today exist only as ephemeral live events.
- Non explicitly frames AI as **"ten assistants"** in his class-prep thinking (filed at `diary/_teaching/2026-05-28-class-prep-thinking-aloud.md`). The 4-agent pipeline is a concrete instance of that mental model.
- The **TKC workshop** Non does (4P methodology, ninja prototypes, S-curve framing) could be a content category. The **smart-city dashboards** could be another. The **100daysofnon** project itself could be a meta-category.
- The deployment principle is the same as everything else Non does: ship live, no localhost-equivalent (no AI-edits-then-sits-in-Drive — it goes to YouTube).

**Stack pre-thoughts (kept light until he asks):**
- Reuse OpenClaw council infrastructure for the 4 agents
- ElevenLabs Professional Clone of Non's voice (he already has 30+ hours of clean audio from his lectures and the Otter.ai transcripts in this project)
- HeyGen Avatar trained on the lecture photos (the Chonburi 14, the Chula meeting screenshots, etc.)
- The 100daysofnon transcripts are already the *voice note* layer — they're his unedited thinking, in his voice
- Editor outsourcing via Fiverr/Onlinejobs.ph — the post specifies India, but Philippines and Thailand also work
- DNA layers can be coded into a `channel-dna.md` per channel; Niche could start at *"AI in smart-city / civic-tech practice from a working practitioner"* (very narrow, no one else doing it)

**The course-seller pitch — separate question:**

The post ends with a course pitch (3,000 baht/month Claude Max as dev team, faceted membership for full template access, group at the FB URL above). Non probably doesn't need the course itself — he's already a Level 4–5 Claude operator running 10+ parallel tasks. But the course seller's *audience* is a relevant signal: there's a Thai-language market of small business owners wanting exactly this kind of system, and Non has more credibility to teach it than the course seller does (PhD, four-continent track record, actual production systems).

**Trigger for surfacing:**
- Any time Non mentions YouTube, video content, faceless channels, ElevenLabs, HeyGen, voice cloning, AI avatars
- Any time Non talks about scaling his lectures, his teaching reach, or his Thai/Chinese-language presence
- Any time the OpenClaw council architecture is being extended — this is a natural personas-extension target
- Any time Non wonders if he should be doing more public-facing content given his demoed expertise
- When Day 92+ of the 100daysofnon project opens up (current obsessions / future plans) and the question of "what's next after teaching" surfaces

---

## 2026-05-27 (companion to the YouTube entry above) — Ross Simmons 4-zone AI business automation, summarized in Thai

**Source Non flagged:** another Thai-language Facebook post from the *same* course-seller (Claude code for Automation & Webapp page, fb.com/groups/876794776824876 — same person who pitched the YouTube post above). This one summarizes a video by **Ross Simmons** (founder of Foundation Marketing and Distribution.AI) hosted on HubSpot Marketing, where Simmons claims to save 20+ hours/week by running 4 automation zones.

**The architecture from the post — 4 zones, do them one at a time:**

1. **Customer Service** — Custom GPT in ChatGPT (Explore GPTs → Create), upload FAQ + product details + policies + common questions. Instruction template: *"answer questions about our products/services, be friendly and helpful, recommend support if unsure."* Connect to website / email / social / messaging. Claim: saves 5–10 hours/week from this zone alone, and it's the fastest-to-deploy.
2. **Content Pipeline (~30 minutes start to publish)** —
   - *Blog:* Perplexity (topic research, real-time) → ChatGPT (draft) → Claude (tone + clarity pass) → Canva (images) → CMS publish
   - *Social:* Notion (weekly themes) → Perplexity (research) → ChatGPT (copy from screenshot of calendar) → Buffer / Distribution.AI / Hootsuite (schedule)
   - **Key trick: batch in single weekly session.** Don't make one piece at a time. Schedule and walk away.
3. **Sales** — *"relevance not volume."* Perplexity (prospect list by industry/location/size) → LinkedIn Sales Navigator (filter) → email finder tool → ChatGPT (personalized outreach drafts per company) → Zapier (automation glue).
   - **Follow-up cadence:** Day 1 personalized intro, Day 3 useful insight/resource, Day 7 relevant case study, Day 14 polite check-in.
4. **Data Analysis** — Upload data to Claude, ask in plain language: *"look at this sales report, what trends matter?"* / *"which pages should I optimize for SERP?"* HubSpot users: Breeze AI Assistant (no export needed). Plus predictive: sales forecasting, churn risk, budget projection. Zapier for the trigger→automation→result loop (e.g., form submission → CRM + spreadsheet + confirmation email, all simultaneously).

**Why this is filed as a separate entry from the YouTube one above:**

The YouTube post above is a *specific build* — a 4-agent pipeline for one channel. This post is a *general business operating system* across 4 different functional zones. Same course-seller, different scope.

**Why Non probably doesn't need to build this for himself:**

He already runs all of it, just under different names:

| Ross's zone | Non's existing equivalent |
|---|---|
| Custom GPT customer service | OpenClaw council personas |
| Perplexity → ChatGPT → Claude → publish pipeline | This very project (100daysofnon) plus his code-task fleet |
| Personalized outreach automation | His relationship-driven engagement (Mayor Ganop, depa/SEIC, Chula VR) is the *opposite* of automated outreach — it's high-touch, low-volume, infinitely-relevant. He doesn't have a Sales zone because he doesn't need one. |
| Claude on uploaded data + workflow automation | He uses Claude on data daily; the code-task fleet IS the workflow automation |

**Where the value of this post sits for Non specifically:**

- **As a teaching artifact.** When Non teaches AI to non-technical Thai audiences (TKC employees, students, smart-city stakeholders), this 4-zone breakdown is the *most accessible* framing he could use. The Custom-GPT-for-FAQ start is the lowest-friction "do one thing this week" assignment a workshop can give.
- **As a market signal.** The course-seller is monetizing this content because there's a Thai-language audience for it — small business owners, marketers, content creators. Non has *more* credibility than the course-seller (PhD, four-continent track record, actual production systems) and could either (a) compete in this market, (b) collaborate with the seller, or (c) ignore it. Worth knowing the market exists.
- **As input for the [[faceless YouTube channel]] above** — the 4-zone framing could be a content category on the YouTube channel: *"4 AI automation zones explained in Thai, by a working practitioner."*

**Trigger for surfacing:**
- Any time Non is preparing a workshop or talk for non-technical Thai audience and wants a beginner-friendly framework
- Any time the question of *"how should small businesses start with AI"* comes up in his consulting work (TKC employees asking, depa partners asking, etc.)
- Any time the YouTube channel project [[2026-05-27 — Faceless YouTube channel as the AI content engine for Non's authority]] gets activated and needs a content category
- Any time Non wonders whether to enter the Thai-language AI-education market
