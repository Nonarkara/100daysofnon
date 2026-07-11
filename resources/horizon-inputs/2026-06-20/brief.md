# Horizon AI Platform — module-input brief, 2026-06-20

Non sent six pieces of source material today and said: *"Horizon 45 projects should have a module that expands to cover these."* Filed here as inputs for the next pass of the Horizon AI curriculum at horizon-ai.eda-thailand.com.

Project context (from `resources/ai summaries/EAD_Horizon_AI_Transcript_Cleaned_EN.docx`): EAD is building an AI Assessment + AI Information Platform with two surfaces — **Zuno** (consumer-facing, TikTok-style short-form AI content) and an assessment-driven personalized-learning-path engine targeted at university students and working professionals. EAD's management has started asking about **agentic AI** as a distinct product line. Non's outside-in critique in that meeting was that the platform — even when finished — didn't make him *feel empowered*. He pushed for **purpose-based assessment** (you take the test because it leads to something you want to do today, not for a certificate) and immediacy ("you learn it now, you make a podcast now, you make money now").

These six inputs are sized to that critique.

---

## Input 1 — `01-top-9-agentic-llm-workflows-aiforleaders.jpg`

The canonical "agentic LLM workflow" taxonomy from AIForLeaders.com: **Prompt Chaining, Parallelization, Orchestrator-Worker, Evaluator-Optimizer, Router, Autonomous Workflow, Reflexion, ReWOO, Plan and Execute**. Each pattern has a one-line use case and a "best suited for" callout (e.g. Orchestrator-Worker → Agentic RAG / coding agents; Router → customer support / multi-agent debate; Plan and Execute → business process automation, data pipeline orchestration).

**For Horizon:** this is the *curriculum spine* for the agentic-AI module EAD's management asked about. Nine patterns, nine lessons, nine working demos. Each lesson teaches one pattern by having the learner build a tiny working agent that ships to a public URL within the lesson — purpose-based, immediate, demonstrably ran. The taxonomy is from a marketing infographic so Horizon's version should be its own re-rendering, not a copy; the *list* is in the public discourse, the *teaching* is Horizon's IP.

## Input 2 — `02-museum-of-meaningless-metrics-cartoon.jpg`

Black-and-white cartoon: "Museum of Meaningless Metrics" — Lines of Code, Story Points, Pull Requests, Tokens Spent (with a vanity counter reading 9,876,543,210 captioned *"Our newest exhibit."*).

**For Horizon:** this is the *anti-curriculum*. The thing Horizon's assessment should NOT measure. Non's own failed-the-Ministry-test anecdote in the EAD transcript is the same critique: the test counted certificate-shaped activities, not actual capability. Put this cartoon (or a re-drawn version) on the *opening slide* of the assessment-design module as the visual statement of what purpose-based assessment is rejecting. Then the lesson teaches how to design metrics that actually correlate with the learner producing something live.

## Input 3 — `03-neurable-brainwave-headphones-bangkok-bank-innohub.jpg`

Thai-language post from Bangkok Bank InnoHub about **Neurable** — US startup making consumer headphones that read brain waves. Applications listed: focus tracking, work, learning, gaming control. Plus an explicit section on the ethical/legal frontier of *who owns your brain data*.

**For Horizon:** this is the *future-horizon* module — the "where AI is going beyond the keyboard." Not core curriculum, but a vital "you are operating in a field that moves quarterly" segment. Pair with discussions of Neuralink, Apple Vision Pro neural cues, and other BCI-adjacent work. Also serves as a content seed for Zuno (short-form: "do you own your brain data when your headphones read it?").

## Input 4 — `04-globalbyte-wifi-iot-sensor-no-code.jpg`

Thai-language post from Global Byte Shop showing a Wi-Fi temperature sensor built around an ESP32 in a weatherproof enclosure, OLED reading 19.9°C, components laid out for assembly. Tagline: *"Make a Wi-Fi sensor without code! IoT project that's solid, easy to assemble, no soldering, no programming."*

**For Horizon:** this is the *practitioner module* — the no-code IoT/maker lane. Crucial for Horizon to cover because it's the bridge from "AI on a screen" to "AI in the physical world." A working sensor that posts to a dashboard the learner built in a Horizon lesson is exactly the kind of *immediate, demonstrable, ship-today* artifact Non argued the platform should produce. Pairs naturally with the smart-city work Non already does at Chonburi, Chula, and Nakhon Si Thammarat.

## Input 5 — `05-7-tool-ai-toolkit-claude-team-thai.jpg`

Thai infographic: **"AI Toolkit ของผม 7 ตัวที่ใช้จริงทุกวัน"** — *"My 7 AI tools I use every day"*, tagline *"ไม่ได้ใช้ AI ตัวเดียว แต่ใช้เป็นทีม"* — *"Don't use one AI, use them as a team."* Stack: Claude AI (think) → Gemini (research) → Claude Code (build) → Claude Design (design) → ChatGPT Images (image) → OpenArt (video) → Wispr Flow (voice-to-AI dictation).

**For Horizon:** this is *literally* the operating model Non has been articulating since the May 27 class-prep transcript ("I have ten assistants, and these are good assistants"). It belongs at the *opening* of the Pro-Prompting / orchestration module: AI is plural, not singular; the skill is composing the right tool to the right step, not mastering one tool deeply. The 7-tool list itself is just an example; the *principle* is the lesson. Note that the infographic is in Thai, which is the right register for Horizon's audience.

## Input 6 — AIS Academy In-House Training, 5 skills × 3 courses (Thai-language Facebook post)

The current Thai-language enterprise-training competitive landscape. AIS Academy is offering three flagship courses and bundles five skills:

1. **Pro-Prompting** — *Generative AI for Enhanced Work Productivity*
2. **Smart Copilot** — *Microsoft 365 Copilot Boosting Productivity*
3. **AI Creative** — *Creative AI: Redefining Art*
4. **Data & Strategy** — *Generative AI for Enhanced Work Productivity* + *Microsoft 365 Copilot Boosting Productivity*
5. **AI Ethics & Security** — across all three courses

URL: https://shorturl.at/lhOTC. Hashtags: #AISAcademy #InHouseTraining.

**For Horizon:** this is the *market-positioning* input. AIS is the incumbent enterprise trainer in Thailand for AI skills. Their 5×3 curriculum is competent, conservative, and built around Microsoft Copilot — which is reasonable for corporate clients but doesn't address the *agentic* shift EAD's management has been asking about, doesn't push purpose-based assessment, and doesn't ship learner-built artifacts. Horizon's positioning needs to be: **what AIS doesn't teach.** Specifically — agentic patterns (input 1), purpose-based assessment design (input 2), the physical-world bridge (input 4), and the multi-tool orchestration mindset (input 5). The Ethics module remains essential and Horizon shouldn't undershoot AIS there.

---

## Proposed Horizon module structure built from these inputs

Seven inputs map to a five-module addition + one cross-cutting theme:

| Module | Anchored by | Teaches | Shipped artifact |
|---|---|---|---|
| **M1 — AI as a team (orchestration mindset)** | Input 5 | Tool selection per step, not one-tool-mastery | Learner's own 5-tool workflow, documented |
| **M2 — Agentic patterns (the 9)** | Input 1 | One pattern per lesson, each with a working agent | 9 small live agents, all reachable from a learner-built portfolio page |
| **M3 — Purpose-based assessment design** | Input 2 | How to measure capability without counting vanity metrics | Learner's own assessment, applied to themselves |
| **M4 — AI in the physical world** | Input 4 | No-code IoT + smart-city patterns; bridge from screen to thing | Live sensor posting to a learner-built dashboard |
| **M5 — Frontier ethics & data sovereignty** | Input 3 | BCI, brain data, content provenance, model autonomy | Learner-written position paper on one frontier issue, published |
| *Cross-cutting:* **Executive Judgment in the Age of AI Defaults** | Input 7 (CTC 2026 "3 AI traps") | When to override AI; how to bet against it on purpose | Embedded in every module as a "AI said X — do you agree?" decision exercise |

Cross-cutting against the AIS 5-skill bundle (input 6):
- Horizon M1 ⊇ AIS Pro-Prompting (Horizon teaches it but as the *opening*, not the whole product)
- Horizon doesn't compete on AIS Smart Copilot (Microsoft 365 is downstream of M1; not core to Horizon)
- Horizon M5 covers AIS Ethics + extends to frontier-tech sovereignty
- Horizon M2, M3, M4 + the Executive Judgment cross-cutter are *categorically not in the AIS catalog* — those are the moats.

See `07-ctc2026-3-ai-traps-killing-creativity.md` in this folder for the full Trap-1-2-3 source material that anchors the Executive Judgment cross-cutter.

---

## Updates from inputs 8, 9, 10 (added 2026-06-20 second pass)

**Input 8 (Samsung Innovation Campus coverage analysis)** — three explicit positioning callouts added to the module plan:
- *Prerequisite linkout:* new-to-Python learners get sent to Samsung first (Horizon doesn't compete on beginner Python or "AI in the Workplace 101")
- *Differentiator vs AIS:* AIS teaches Copilot productivity; Horizon teaches composing AI as a team + overriding it
- *Differentiator vs FutureSkill (input 9):* FutureSkill teaches via n8n abstraction; Horizon teaches both n8n-style AND code-first with Claude Code direct

See `08-samsung-innovation-campus-coverage-analysis.md` for the full competitive-coverage table.

**Input 9 (FutureSkill RAG/n8n course)** — Non flagged this with the strongest claim of any input: *"I have much better workflows or a better way of building these without having to use any of the complicated software."* The key implication: M2 should be taught as **two parallel tracks** — M2-A visual/n8n-style for low-code accessibility, M2-B code-first for practitioners who skip the abstraction layer. Both produce the same outcome (9 working agents shipped). Adding a candidate Horizon module: **"Running 10 parallel agents with Cowork"** — direct teaching of Non's actual daily workflow, which is the moat against every other Thai-language curriculum.

See `09-futureskill-rag-ai-agent-n8n-course.md` for the full positioning analysis.

**Input 10 (Claude Code as 6-role web team / WEB_TEAM.md pattern)** — methodological scaffolding that improves M1 and M2. The key deliverable change: M1 now produces a reusable `*_TEAM.md` file (4 sections: Mission / Roles / Workflow / Quality Gate) per learner per domain, not a snapshot of current practice. Three primitives added to M1's prompt-engineering content:
- **Brief-first + Ask-back-first prompt pattern** — switches AI from guess-mode to interview-mode
- **Quality Gate checklist as transferable form** — learners write per-domain QG checklists
- **Retrospective-after-delivery loop** — graded artifact, accumulates into learner's personal pattern library

See `10-claude-code-as-6-role-web-team.md` for the full method breakdown.

## Updated Horizon module structure (incorporating 8/9/10)

| Module | Anchored by | Teaches | Shipped artifact |
|---|---|---|---|
| **M1 — AI as a team (orchestration mindset)** | Inputs 5 + 10 | Tool selection per step; brief-first prompting; WEB_TEAM.md pattern | Learner's own `*_TEAM.md` for their domain + Quality Gate checklist |
| **M2-A — Agentic patterns (visual / n8n-style)** | Inputs 1 + 9 | The 9 patterns via low-code workflows | 9 working agents shipped via n8n |
| **M2-B — Agentic patterns (code-first / Claude Code direct)** | Inputs 1 + 9 + 10 | The 9 patterns in plain code, Cowork-orchestrated | 9 working agents shipped via Claude Code + Cowork |
| **M3 — Purpose-based assessment design** | Input 2 | How to measure capability without counting vanity metrics | Learner's own assessment, applied to themselves |
| **M4 — AI in the physical world** | Input 4 | No-code IoT + smart-city patterns | Live sensor posting to a learner-built dashboard |
| **M5 — Frontier ethics & data sovereignty** | Input 3 | BCI, brain data, content provenance, model autonomy | Learner-written position paper on one frontier issue, published |
| **M6 — Running 10 parallel agents with Cowork** *(new candidate)* | Non's own daily workflow + Input 9 | The Cowork orchestration pattern Non runs in production | Learner runs their own multi-task workflow, ships at least 3 outcomes from one parallel orchestration session |
| *Cross-cutting:* **Executive Judgment in the Age of AI Defaults** | Input 7 | When to override AI | Embedded in every module |
| *Cross-cutting:* **Retrospective + Pattern Library** | Input 10 | Compound learning across projects | Every module ends with a retro; retros build the learner's personal playbook |

---

## Update from Input 11 (added 2026-06-20 third pass)

**Input 11 — Sanook / MSN Thailand: "5 Thai jobs at risk within 5 years"** (Data Entry, Basic CS, Basic Translation, Basic Graphic Design, Basic Content Writing). Non called this *"definitely useful to Horizon."* It is the single most important input yet — not a new module, but the **opening recruiting frame** the entire curriculum should be sold against.

Each of the 5 at-risk categories has a survival pivot, and each pivot maps cleanly to one or more Horizon modules. Sample: *Data Entry → Validator / Data Analyst → M2-B + M3.* *Basic CS → Empathy/Complex CS → M1 + Executive-Judgment cross-cutter.* *Basic Graphic → Strategic Designer → M1 + Executive Judgment.* See `11-msn-sanook-5-thai-jobs-at-risk-within-5-years.md` for the full pivot matrix.

**Two additions to the curriculum spec the Horizon code-task should produce:**

1. A *"Why Horizon"* opening section anchored on this 5-category framing — landing-page copy, enrollment pitch, executive-summary opener.
2. A *"Survival Pivot Matrix"* downloadable graphic — at-risk role → target role → Horizon module(s) that get you there. Single page, shareable on Thai-language social.

**Follow-on research task to flag for Non:** the Sanook article was syndicated from cafef.vn (Vietnamese source). Horizon should commission a **Thailand-specific version** of the same analysis — possibly via NSO data, depa labor-market work, or one of Non's depa/SEIC contacts. Same dynamics, higher local credibility, becomes Horizon's own owned IP.

---

## Update from Input 13 (added 2026-06-20 fourth pass)

**Input 13 — "Top 5 ChatGPT Prompt Formats"** (PAR, RTF, TAG, BAB, CARE). Named mnemonics for prompt shapes — the kind of acronym-anchored framework that actually transfers to learners under pressure (same pedagogy as Non's own 4P, 4C, G/D/U/C frameworks). See `13-top-5-chatgpt-prompt-formats.md` for the full table.

**Adds to M1's prompt-engineering primitives:**
- The 5 mnemonics join the 3 already in M1 from Input 10 (Brief-first / Quality Gate / Retrospective)
- Total: an 8-row prompt-primitives grid that becomes the most-referenced page in M1

**M1 deliverable updated again:** learner now produces (a) `*_TEAM.md`, (b) Quality Gate checklist, and (c) a personal **Prompt Format Cheatsheet** listing the 5 mnemonics + any custom ones they've coined. In their working language. Printed and pinned.

**Image as Pinterest-card material:** Input 13 is also a perfect candidate for the Pinterest-style artifact library (Input 12 spec). The 5-acronym grid is single-image, immediately scannable, and the kind of card people screenshot and save.

---

## Update from Input 14 (added 2026-06-20 fifth pass) — the foundational tier ladder

**Input 14 — Four-Tier AI-Adoption Ladder** (train-metaphor infographic). Non's framing was the strongest of any input today: *"this could serve as a foundation of tiers of skills we want people to be able to achieve in the Horizon 45 project."* This is named as foundation, not addition.

The four tiers:

| Tier | Name | Break that moves you up |
|---|---|---|
| **T1** | The Skilled Professional (isolated) | Break isolation |
| **T2** | The Hesitant Solo Operator (pulling alone) | Break manual labor |
| **T3** | The AI-Leveraged Professional | Break invisibility |
| **T4** | Consistent Impact & Growth (*"Start Small, Share Imperfectly"*) | — |

Each module now indexes against which tier-break it serves. See `14-four-tier-ai-adoption-train-metaphor.md` for the full tier↔module mapping.

The maxim **"Start Small, Share Imperfectly"** becomes Horizon's **operating motto** — printed on landing page, certificate, every retrospective template. It's the affirmative version of Input 2's vanity-metrics warning and Input 11's survival-by-perfection trap warning.

**Restructured curriculum narrative:**

1. **Why Horizon** (anchored on Input 11 — the 5 at-risk jobs)
2. **The Tier Ladder** (anchored on Input 14 — the 4 tiers + train metaphor)
3. **The Modules** (M1 through M6 + cross-cutters, each indexed to which tier-break it serves)
4. **The Pinterest Library** (Input 12 spec)
5. **Operating Motto: Start Small, Share Imperfectly**

**Enrollment-time recommendation engine:** the M3 self-assessment now has a 5-question diagnostic spine that places the learner on the tier ladder and recommends which module to enter first.

---

## Update from Input 15 (added 2026-06-20 sixth pass) — new module M7: AI-enabled scam defense

**Input 15 — Mastercard / GASA online scam carousel** (3 slides). Non's framing: *"Let's feature this data in a part where we're going to be teaching people about online scamming."* This is effectively a new-module ask. The data: $442b lost worldwide, 80% targeted, 29% engaged, 71% of engagers experienced loss.

**Candidate addition — M7: AI-enabled scams and how to defend against them.** Six lessons: threat surface, how AI weaponized scams, pattern recognition, defense techniques, build-your-own-defense (household plan), community angle (deliver the plan to one elderly relative + one community group). See `15-online-scam-data-mastercard-gasa-2025.md` for the full module spec.

**Why M7 makes the curriculum complete, not just expanded:**

M1–M6 are *offensive* — building with AI, shipping with AI. M7 is *defensive* — recognizing when AI is weaponized against you. A Horizon graduate now wields AI as a builder AND defends against it as a target. The asymmetry of teaching only offense leaves graduates personally vulnerable; M7 closes that.

**Updated recruiting copy** (combines Inputs 11, 14, 15):

> *"Your job may disappear. Your inbox is already under attack. You have two years to climb four tiers — from isolated skilled professional to the consistently-shipping, AI-leveraged, scam-resistant operator your family and your community can trust. Horizon teaches both halves."*

**Follow-on data task:** the Mastercard / GASA numbers are global. For Thai audience impact, Horizon should localize with current Thai-specific figures from GASA's country breakout, the Thai Royal Police AOC (Anti-Online Scam Operation Center), Bank of Thailand suspicious-transaction data, and depa's consumer-protection unit. Higher-impact opening for M7 than the global slides alone.

---

## Updated full module structure (incorporating 14, 15)

| Module | Tier-break served | Anchored by |
|---|---|---|
| **M1 — AI as a team (orchestration mindset)** | T2→T3 | inputs 5, 10, 13 |
| **M2-A — Agentic patterns (visual / n8n)** | T2→T3 | inputs 1, 9 |
| **M2-B — Agentic patterns (code-first)** | T2→T3 | inputs 1, 9, 10 |
| **M3 — Purpose-based assessment + enrollment diagnostic** | T1→T2 | inputs 2, 14 |
| **M4 — AI in the physical world** | T2→T3 | input 4 |
| **M5 — Frontier ethics & data sovereignty** | T3→T4 | inputs 3, 12 |
| **M6 — Running 10 parallel agents with Cowork** | T2→T3 | Non's daily workflow + input 9 |
| **M7 — AI-enabled scam defense (NEW)** | T1→T2 (literacy) + T3→T4 (community delivery) | input 15 |
| *Cross-cutting:* **Executive Judgment** | T1→T2 (permission to override AI) | input 7 |
| *Cross-cutting:* **Retrospective + Pattern Library** | T3→T4 (compounding visibility) | input 10 |
| *Cross-cutting:* **Pinterest Library** | T3→T4 (visible surface) | input 12 |
| *Operating motto:* **"Start Small, Share Imperfectly"** | governs all tier-breaks | input 14 |

---

## Update from Input 16 (added 2026-06-20 seventh pass) — full prompt-formula taxonomy + four pedagogy directives

**Input 16 — ChatGPT Prompt Writing Formulas (full taxonomy).** Superset of Input 13. 17–19 named formulas: AIDA, ASK, CREAC, CREATE, EPL, FAB, INTRO, OAR, PEEL, PIE, PSA, PSAT, SBD, SOAPSTONE, STAR, SWOT, TAS, TEA. Many predate AI (PEEL, PIE, SOAPSTONE, SWOT, STAR, AIDA come from classical rhetoric / business pedagogy) — teaching point in itself: *prompt engineering inherits 200+ years of rhetorical pedagogy*. See `16-chatgpt-prompt-writing-formulas-full-taxonomy.md` for the full table.

**Non's four structural directives, all to integrate:**

1. **Pinterest library cards** — one card per formula, each independently URL-addressable per Input 12's spec
2. **Inline tip-blending in platform answers** — when the Horizon AI assistant answers a learner's question, also surface an inline tip card showing which prompt formula would have produced a better question. This is a **product feature**, not just curriculum — none of the competitors have it. Build the pattern-matcher.
3. **Delegate-to-a-colleague framing** — reframe prompt engineering from "technical skill to memorize" to "managerial skill you already have." *"What would you tell a new junior who doesn't have your context?"* That sentence is the unlock. Connects back to Inputs 5, 10 (AI as team, WEB_TEAM.md).
4. **Goal-first principle** — first principle of M1, deserves its own opener lesson at the very top: *"What is the result you want? What does done look like? If you don't have a goal yet, the first prompt is 'help me find the right goal,' not 'do the work.'"* This is the inverse of Input 7's executive-judgment cross-cutter — *when to formulate the question before asking AI at all.*

**M1's prompt-primitives layer grows again** — from 8 rows (Inputs 10 + 13) to ~20+ rows with Input 16's full taxonomy. The grid now deserves its own surface beyond a printable cheatsheet: a **Prompt Formula Reference** sub-tool inside Horizon with filters, examples, "best for" tags, and one-click copy-to-clipboard for each formula.

**Lesson that lands all four directives in one place** (proposed M1 opener):

> *"How to be the good boss your AI deserves. Step 1: define your goal before you open the AI. Step 2: imagine your prompt is a brief to a smart new junior who doesn't have your context — what do they need to know? Step 3: pick the named formula that fits this kind of brief (the taxonomy is the menu). Step 4: write the prompt. Step 5: when the output isn't what you wanted, ask what was missing from the brief, not what was wrong with the junior."*

---

## Update from Input 17 (added 2026-06-20 eighth pass) — the goldmine input

**Input 17 — "100 ChatGPT Use Cases" catalog.** Non's framing was the strongest yet: *"This is probably a gold mine for the Horizon 45 project."* Image at `17-100-chatgpt-use-cases-catalog.png`, full unpack at `17-100-chatgpt-use-cases-catalog.md`.

The input packs **three pedagogical layers in one visual**:

1. **20 domains × 5 use cases = ~100-use-case taxonomy** — Education / Professional Dev / Creative Writing / Entertainment / Business / Tech Support / Health & Wellness / Learning New Skills / Language & Literature / Social Interaction / Art & Design / News & Current Events / Organizational Tools / Content Creation / Philosophy & Ethics / Daily Assistance / Personal Finance / Environmental Awareness.
2. **An embedded universal Prompt Formula: Role + Task + Context + Constraints + Output Format (R-T-C-C-O)** — the **most complete universal scaffold** across Inputs 13, 16, 17. Every other formula (AIDA, STAR, PEEL, BAB, SWOT, etc.) is a specialization of R-T-C-C-O for a specific class of task.
3. **An embedded Quick Tip + 1-minute Self-check** — *"List 5 options"* + *"Ask clarifying questions first"* + a 3-step self-diagnostic (name 2 categories you use weekly, write a 1-sentence prompt, identify the output format).

**Canonization recommendation:** R-T-C-C-O becomes Horizon's *canonical* prompt scaffold (M1 baseline, taught first). All other formulas from Inputs 13, 16 are taught as *named specializations* of it, not as equals. Cleaner pedagogy: one canonical scaffold + a menu of specializations.

**Three new product surfaces this unlocks:**

1. **"What do you want AI to do?" landing-page entry** — the 20×5 grid becomes the prospect's first interaction. Each cell is a click → sample prompt + sample output + matched formula + Horizon module that teaches the underlying skill. The lowest-friction enrollment funnel Horizon can build. No competitor in Thai-language AI ed has it.
2. **Pinterest library expansion to 100+ cards** — one card per use case, each with R-T-C-C-O prompt example. Multiplies social-distribution surface area.
3. **Personal Path Generator** — combine Input 14's tier-ladder (where am I?) + Input 17's use-case grid (what do I do?) + the M1–M7 structure → personalized 3-month roadmap. **This is the holy grail LMS feature** that justifies the per-learner spend, directly buildable from already-filed inputs.

**Updated curriculum narrative (rev 2):**

1. **Pick your use case** (Input 17 — the 100-grid as landing entry)
2. **See where you are** (Input 14 — tier-ladder diagnostic)
3. **Why Horizon** (Input 11 — at-risk jobs frame as threat motivation)
4. **Your personalized path** (Personal Path Generator combining 14 + 17)
5. **The Modules** (M1–M7 + cross-cutters)
6. **The Pinterest Library** (Input 12 + Input 17 expansion to 100+ cards)
7. **Operating Motto: Start Small, Share Imperfectly** (Input 14)

This is now a complete curriculum *architecture*, not just a module list.

---

## Update from Inputs 18 + 19 (added 2026-06-20 ninth pass) — M6 finally anchored, with future-tooling layer

**Input 18 — Non's own multi-agent-orchestration skill spec.** This is the *first input today that is Non's own original work*, not third-party material. It carries different epistemic weight. Image-equivalent: a complete Claude Code skill spec in Thai with English technical terms. See `18-multi-agent-orchestration-skill-spec.md` for the full unpack.

**M6 — Running 10 parallel agents with Cowork — upgrades from "candidate module" to "anchored, syllabus-complete."** The skill spec IS the M6 syllabus, six lessons end-to-end:

1. Why orchestration matters + EGO-VOID + roles/ownership
2. AGENT_NOTES.md as communication backbone + D-E-R review format
3. ACTIVE CLAIMS pattern (preventing file-edit collisions)
4. Work Orders + Definition of Done
5. Ground-Truth Verification (don't trust agent reports — verify against git/CI directly)
6. Safety, anti-patterns, adaptation to your own stack

**M6 shipped artifact:** learner sets up `AGENT_NOTES.md` + `ACTIVE CLAIMS` in their own project, writes one Work Order, runs at least 2 agents through one cycle of claim → work → review → next-delegation, and submits the resulting AGENT_NOTES log as proof. **The most advanced shipped artifact in the entire Horizon curriculum.** Direct T4 demonstration.

**The new canonical pattern pair:** WEB_TEAM.md (M1, from Input 10) + AGENT_NOTES.md (M6, from Input 18) are Horizon's two canonical multi-agent coordination scaffolds. Both ship as downloadable templates via the Pinterest library.

**Why M6 is the deepest moat against every competitor:** the skill spec contains operational knowledge that *can only come from running 10+ parallel agents in production and surviving the failure modes.* Anti-patterns like *"sandbox/mount phantoms"*, *"CI green ≠ local verify"*, *"#0 risk = uncommitted work surviving across rounds"* are hard-won, not theoretical. AIS / Samsung SIC / FutureSkill / Thai-language course-seller community have *nothing* like this. They teach AI as a tool; Non teaches AI as a team you manage with the discipline of a software production lead who has actually shipped under multi-agent conditions.

**Three structural recommendations for the Horizon integration** (see Input 18 brief for full):
1. Publish a Horizon-branded edition of the skill spec as a free downloadable PDF (lead-magnet)
2. Add Cowork-itself as a teachable platform (first paid Cowork education in any market)
3. WEB_TEAM.md + AGENT_NOTES.md become Horizon-canonical patterns with downloadable templates

---

**Input 19 — codebase-memory-mcp / Knowledge Graph backend for AI coding agents.** SynapTechAI Thai-language post. The tool indexes a whole codebase into a queryable graph (functions, classes, call graphs, HTTP routes, service deps, K8s manifests) so agents don't grep file-by-file. Performance claims: Linux Kernel 28M lines in ~3 min, <1ms structural queries, local-only, no API key, single binary.

**Fits M6** as the *next-generation tooling layer* — the *context layer* that complements Input 18's *coordination layer*. Together they describe the complete operating environment for production multi-agent work in 2026+.

**Strongest external validation of Horizon's full curriculum architecture yet:** the SynapTechAI post argues *"good coding agents need context, memory, graph, rules, workflow"* — which maps **exactly** onto Horizon's M1 (context) + Retrospective cross-cutter (memory) + M6 (graph/rules/workflow). The industry is converging on the view Horizon's brief has been inductively building all day.

**Discipline note:** the performance claims in the post are vendor advocacy, not independently benchmarked. The M6 Ground-Truth Verification lesson teaches *don't claim performance you haven't verified*; Horizon must model the same discipline before recommending the tool. Validate against a comparable open repo before publishing.

**Total: 47 inputs absorbed for Horizon** (43 CLAUDE.md architecture, 44 Claude-for-Solopreneurs-30-commands, 45 Thai B2B-easy-mode Kiyosaki-echo, 46 SynapTech-7 OSS tools, 47 Plaemanga practitioner-honest SaaS lessons). Plus 2 cross-project shared inputs at `shared-inputs/` (geological-history + the Jim-Carrey-quote-paired-with-grandfather grounding coda — the latter does NOT belong in Horizon's frame and is filed deliberately outside it). The brief is the source-of-truth for the Horizon integration work.

---

## Update from Input 27 — Google Open Knowledge Format (OKF) as platform architecture

**Input 27 — Google OKF v0.1 (GoogleCloudPlatform/knowledge-catalog).** Vendor-neutral knowledge standard: a folder of Markdown files, one file per concept, `type:` field required in YAML frontmatter, Markdown links between files form an emergent knowledge graph. Solves Google's named *"context assembly problem"* — knowledge fragmentation across Notion / Docs / DBs / wikis. Karpathy's *LLM-wiki* concept standardized. See `27-google-open-knowledge-format-okf.md` for full unpack.

**Three Horizon implications:**

1. **OKF becomes the third canonical M6 file-level scaffold** alongside WEB_TEAM.md (Input 10) and AGENT_NOTES.md (Input 18). The trinity: team rules + running coordination log + shared knowledge base. Together they describe a complete agent-operating-discipline at the file level.

2. **Horizon's own platform should ship OKF-native** — Pinterest library cards, use-case grid entries, Research papers all as `type:`-tagged Markdown in a public Git repo. Platform teaches by being. No Thai-language competitor has this architecture; AIS / Samsung SIC / FutureSkill all use proprietary LMS backends.

3. **Horizon Research paper #7:** *"The Open Knowledge Format and the End of Context Fragmentation: Why Google Followed Karpathy, and What It Means for Thai Organizations Choosing Their Knowledge Stack in 2026"* — especially relevant for Thai gov / SEIC / depa stakeholders making real-now procurement decisions on knowledge infrastructure.

**The most strategically important observation:** Non has been independently practicing OKF for months. The auto-memory system, the 100daysofnon project structure, and the input-folders I've been building today are all already 95% OKF-compliant — just need top-level `type:` field promotion. **Zero migration cost. Existing data is already in shape.** Horizon could ship OKF-native within days, not weeks.

---

## Update from Inputs 20, 21, 22, 23 (added 2026-06-20 tenth pass)

**Input 20 — Supabase as the backend bridge** (`20-supabase-backend-as-bridge-for-ai-built-frontends.md`). Anchors M4 with a concrete tool stack. The 7 Supabase pillars (Postgres / Auth / Auto-API / Storage / Realtime / Edge Functions / Vector-pgvector). The 5 you-still-need-to-know layers (DB design / Auth / RLS / Env vars / Deploy+Backup) IS the M4 syllabus. Enables a **Backend Buddy** product feature (Horizon AI assistant offers guided session: schema design + RLS policy starter + Edge Function stubs + deployment checklist). No competitor has this.

**Input 21 — Conversation → App pipeline** (`21-meetings-as-requirements-pipeline.md`). Methodology cross-cutter, not a module. Names the flow: Conversation → Report → Requirements → Design → Prototype → App. Concrete example: Facebook-Page-content app from meeting. Adds lessons to M1 (where good prompts come from), M3 (meeting transcripts as honest source of purpose data), M2-B (capstone: from recorded meeting to working app), M4 (full journey). **Meta-observation: this IS the pipeline Non and the orchestrator have been running on the Horizon project itself today. Horizon could ship as a self-case-study.**

**Input 22 — Codex Desktop Skills install pattern** (`22-codex-desktop-skills-install-pattern.md`). Tips & Techniques content (per Non's directive *"include in tips and techniques sections"*). The 6-step install pattern + community marketplace. Together with Input 18, describes the complete Skills lifecycle (discover → install → use → write your own → share). Adds **Tips & Techniques surface** as new Horizon platform feature with 11 seed cards from today's inputs.

**Input 23 — TH-AI Passport / 31 models × 14 providers landscape** (`23-th-ai-passport-31-models-14-providers-landscape.md`). Non's directive: *"include in the research paper that is included in the Horizon45 page; analyze this as well."* Adds **Horizon Research surface** as a new platform feature — long-form analysis papers establishing Horizon's academic credibility. Five seed papers proposed from today's inputs (the landscape one, Supabase, multi-agent orchestration, at-risk-jobs, the 4-tier ladder). Critical strategic positioning: **Typhoon (SCB 10X) is the canonical model for Thai-language tasks** — not a fallback. Horizon should build a relationship with SCB 10X via its depa/SEIC standing.

## Updated platform surfaces (now seven)

| Surface | Purpose | Source |
|---|---|---|
| **Use-case landing grid** | 100-cell entry to the platform | Input 17 |
| **Tier-ladder diagnostic** | Place learner on the 4-tier ladder | Input 14 |
| **Personal Path Generator** | Personalized 3-month roadmap | Inputs 14 + 17 |
| **Pinterest library** | Visual artifact library | Input 12 |
| **Backend Buddy** | Guided Supabase system-design tool | Input 20 |
| **Tips & Techniques** | Bite-sized 2-minute walkthroughs | Input 22 + many seed cards from today |
| **Horizon Research** | Long-form analysis papers | Input 23 |

## Updated full module + cross-cutter structure

| Module | Tier-break | Anchored by |
|---|---|---|
| M1 — AI as a team | T2→T3 | 5, 10, 13, 16, 17, 21 |
| M2-A — Agentic patterns (visual/n8n) | T2→T3 | 1, 9 |
| M2-B — Agentic patterns (code-first) | T2→T3 | 1, 9, 10, 21 (capstone) |
| M3 — Purpose-based assessment | T1→T2 | 2, 14, 21 |
| M4 — AI in the physical world / real systems | T2→T3 | 4, 20, 21 |
| M5 — Frontier ethics & data sovereignty | T3→T4 | 3, 12 |
| M6 — Running 10 parallel agents with Cowork | T2→T3 | 18, 19, 22 (skills install) |
| M7 — AI-enabled scam defense | T1→T2 (literacy) + T3→T4 (community delivery) | 15 |
| Cross-cutter — Executive Judgment | T1→T2 | 7 |
| Cross-cutter — Retrospective + Pattern Library | T3→T4 | 10 |
| Cross-cutter — Pinterest Library | T3→T4 | 12 |
| Cross-cutter — Conversation → App pipeline | spans all tiers | 21 |
| Cross-cutter — Model selection per task | spans all tiers | 23 |
| Operating motto: *Start Small, Share Imperfectly* | governs all | 14 |
| Companion principle: ***The Invisibility Test*** (good AI is invisible; the day customers praise it for being clever is the day automation failed) | governs M3 + every shipped artifact | 25 (Bland AI) |
| Third governing principle: ***Skill Preservation*** (use AI to extend your skill, not hollow it out; deliberate practice without AI, blind review, skill audits) | governs M3 + the learner's lifelong development | 26 (Nature June 2026) |

---

## Update from Inputs 24 + 25 (added 2026-06-20 eleventh pass)

**Input 24 — Caveman (Julius Brussee)** — Claude Code skill that compresses AI agent output by ~65% (range 22-87%). Verified at github.com/JuliusBrussee/caveman (928★, MIT). **Critical caveat the Thai post elided:** only affects *output* tokens, not thinking tokens — biggest win is readability/speed, cost savings are a bonus. Goes into Tips & Techniques as install walkthrough AND into M1+M6 as worked example of the *"codify a recurring rule into a reusable skill"* meta-pattern (same shape as Non's own multi-agent-orchestration skill, Input 18).

**Input 25 — Bland AI / "Good AI is invisible"** — LinkedIn post by Anastasiia S. about Bland AI's deliberately-boring marketing campaign starring Paul Lieberstein (Toby from The Office). The pedagogical heart of the input is one sentence: *"The best AI does not impress your customer. It just works, and nobody notices. The day your phone agent gets praised for being clever is the day automation failed."*

**This is the most pedagogically loaded single sentence of the day.** It deserves naming as a Horizon-canonical principle: **The Invisibility Test.** A learner shipping any AI feature asks: *"Will a customer praise this for being clever?"* If yes, the design has missed its job. The Invisibility Test goes alongside the *Start Small, Share Imperfectly* motto as the **second governing principle** of Horizon's curriculum.

**Convergence observation across all 25 inputs:** every major Horizon theme today now points at the same underlying argument — **AI's measurable value comes from invisible reliability, not visible impressiveness.** Bland AI's marketing IS Horizon's curriculum, demonstrated.

**Four Horizon placements for Input 25:**
1. M3 opener: The Invisibility Test as lead diagnostic
2. Pinterest library card
3. Horizon Research seed paper: *"The Invisibility Test: A Working Theory of Production-AI Success Metrics"*
4. Executive Judgment cross-cutter case-study addition

---

## What Horizon needs to do with this brief

If Horizon already has a curriculum doc / module spec in its own repo, this brief should be *forwarded into* that doc as a 2026-06-20 update. If Horizon is still mid-design, this brief is sufficient to anchor the next design pass.

If you tell me where the Horizon repo lives on your machine (it's not currently mounted to this dispatch session — likely under `~/Projects/consulting/horizon-*` or `~/Projects/ead/*` or similar), I'll spawn a code-task there with this brief + the five images forwarded so the Horizon worker can absorb them into the actual curriculum spec.

---

## Update from Input 28 — Prototype-First vs Plan-First (meta-decision aid)

**Input 28 — Thai infographic *"สร้างโปรเจกต์ด้วย AI แบบไหนดี?"*** Two approaches presented as a binary self-identification: **Prototype-First** (*fast, flexible, learn from real things*) vs **Plan-First** (*systematic, controlled direction, easy to scale*). See `28-prototype-first-vs-plan-first.md` for full unpack.

**Contribution to Horizon:** the curriculum already teaches both approaches across different modules (prototype-first in *Start Small Share Imperfectly* + Non's 45-min ninja builds; plan-first in Input 21's Conversation→App pipeline + Input 18's Work Orders + Input 10's WEB_TEAM.md). **Input 28 names the *choice between approaches* as itself a skill** — a meta-frame that elevates context-aware approach-selection to an explicit lesson.

**M1 lesson addition:** *"Choosing your approach — prototype-first vs plan-first."* Decision criteria: reversibility of decisions in scope, clarity of success criteria, cost of building the wrong thing, coordination cost across humans. Defaults: prototype-first for solo/exploratory/low-stakes; plan-first for team/regulated/high-stakes. Mid-stream switches need explicit acknowledgment.

**Three placements:**
1. M1 second sub-lesson (after Input 16's "good boss your AI deserves")
2. Pinterest card — *"Two ways to build with AI. Both work. Picking the wrong one for your context is the most expensive AI mistake you can make."*
3. Tips & Techniques 2-minute walkthrough with three worked-example projects (solo founder testing landing page → prototype-first; government dashboard with 6-month timeline → plan-first; regulated-industry AI agent → plan-first with prototype loops inside each phase)
