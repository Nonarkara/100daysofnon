# Input 60 — The Ultraboost Integration Map: what to actually do with the 30-tool batch

**Source:** Non, 2026-06-20, single-batch drop of ~32 images spanning six content sources — **JANUSTIU Claude Skills carousel** (6 cards), **MarketryPro paid-vs-free comparison** (20 categories), **Money Trendz AI-Toolkit teaching cards** (7 slots — Fine-tuning + Workflow Automation featured; the rest are known-pattern), **Coolify self-hosting series** (Hoppscotch, Papercups, Coolify, Trigger.dev), the **Softwarewithnick Learn-Git-Branching reel** ([learngitbranching.js.org](https://learngitbranching.js.org)), and one **NVIDIA blog URL** (*Lowest Token Cost AI Factories*). Non's directive: *"Learn these. The goal is to see what we can do with them to integrate into our system and ultraboost its productivity/efficiency."*

## Why this is filed as a single Input 60 rather than 32 separate briefs

Filing each tool as its own Input NN would be noise, not signal. The *value* Non is asking for is **the integration map**, not the catalog. This brief IS the answer. Individual tool detail is preserved in the source images (all present in `/uploads/`) and can be expanded on demand.

## The high-leverage moves — ranked by expected ROI, top of stack first

### Tier A — install this week (highest ROI, lowest risk)

**A1. JANUSTIU Claude Skills — install all 6 into personal-skills.**

| Skill | Repo | Direct value |
|---|---|---|
| **Designer Skills** | `github.com/Owl-Listener/designer-skills` | 239 skills / 88 commands / 33 plugins across research, UX, AI product design, design leadership, inclusive design. **Merges with Non's Rams/Vignelli discipline (`outputs/design.md`).** Kill AI-slop UI look at the tooling level. |
| **PM Skills** | `github.com/phuryn/pm-skills` | ~55+ skills across Product Discovery, Product Strategy, Execution, Market Research, Data Analytics, Go-to-Market, Marketing/Growth, PM Toolkit, AI Shipping Kit. **Directly powers Horizon roadmap + SLIC v3 product decisions + Horizon-Activate positioning work.** |
| **HTML Anything** | `github.com/nexu-io/html-anything` | Ship-ready HTML decks, posters, resumes, social templates, prototypes, mockups. **Replaces the pptx skill for any deck that doesn't need to be .pptx-native.** Faster + cleaner + version-controllable. |
| **Taste Skill** | `github.com/leonxlnx/taste-skill` | Upgrades vibe-coded UI, kills AI-slop look, includes image-generation for reference boards. **Direct anti-template-poison enforcement at the tooling level** (per your CLAUDE.md Template Poison list). |
| **App Store Screenshot Generator** | `github.com/ParthJadhav/app-store-screenshots` | Realistic app mockups with device frames, Next.js editor. **Ship-ready App Store + Google Play screenshots for any prototype we build** — SLIC v3 mobile view, Horizon learner-app mockups, etc. |
| **Frontend Slides (via HTML Anything screenshot)** | (in HTML-Anything repo) | Animation-rich HTML presentations converting PowerPoint. Zero-dependency, single HTML file. |

**Routing per SPADA:** Non installs (Non is Lead Architect; skills-install goes through Non's gate). I (orchestrator) will *use* them in docs/architecture/specs work. Codex will *use* them when spec references demand them. Antigravity will *use* them for frontend work.

**Estimated ultraboost impact:** *very high.* Skills eliminate re-explanation across sessions. PM Skills alone is worth the installation ceremony — every Horizon/SLIC product decision runs faster.

---

**A2. Learn Git Branching (learngitbranching.js.org) — for Non personally.**

Interactive Git tutorial by @pcottle. **The single most-referenced Git-teaching resource on the web.** Given Non's "not a programmer, needs step-by-step for CLI/coding" preference from CLAUDE.md, this is the fastest path to Non being able to independently do the *branching* operations that show up in SPADA's Codex/Antigravity handoffs (Work Claims, branch merges, diff review). 20–30 minutes on this site is a permanent unlock.

**No install. Just: browser → learngitbranching.js.org → do levels 1–6.**

Ultraboost impact: *high for Non, one-time.* Removes an EGO-VOID review bottleneck (currently: Non has to ask me to interpret git-branch state).

---

**A3. NotebookLM (Google, free) — for Horizon Research paper drafting + Non's own reading.**

MarketryPro card 08 pairs ChatPDF ($20) vs NotebookLM ($0). **NotebookLM's grounded-in-your-sources architecture is the correct tool for Horizon Research paper drafting** — where every claim needs to be attributable to a filed source. It also solves the *"Non has 5 PDFs and one hour"* problem cleanly. Free from Google, no install, just upload.

Ultraboost impact: *high.* Horizon Research papers move faster from filed sources to draft.

---

### Tier B — install this month (high ROI, moderate ceremony)

**B1. n8n (self-hosted) — the SPADA async-orchestration layer that isn't a text file.**

Money Trendz card 2 (AI Workflow Automation) shows Zapier / Make / **n8n** / Bardeen. Of these, **n8n is the only one that runs self-hosted, open-source, and can be Coolify-deployed on your own infrastructure per the [[feedback_no_localhost_ship_principle]].** It gives SPADA a real async-orchestration surface *beyond* AGENT_NOTES.md — event-driven workflows Codex + Antigravity + Hermes can be triggered by.

Concrete first use: **an n8n workflow that watches for new Input NN files in `resources/horizon-inputs/` and auto-generates a Horizon brief-update Work Order for Codex.** This closes the loop where today I manually draft integration text after each input.

Coolify from the same batch is the self-hosting substrate — install n8n on Coolify on any cheap VPS. **No AWS lock-in, no monthly fee, full control.** This aligns with the [[no-localhost-ship-principle]] and [[always-mvp]] discipline.

Routing per SPADA: Codex's zone (services/). I (orchestrator) will draft the Work Order.

---

**B2. Trigger.dev — background jobs for the Horizon site + SLIC index + NSP.**

Coolify series card. **Event-driven long-running tasks with retries, queues, observability, elastic scaling. TypeScript. 14.8K stars. Open source.** Directly relevant for:

- Horizon platform: process learner-uploaded assessments in background
- SLIC index: nightly recompute of livability scores as data-sources refresh
- NSP: any long-running media transcode / redaction workflow

Routing per SPADA: Codex's zone. Work Order eventually — not this week.

---

**B3. Hoppscotch — Postman alternative for API-testing SLIC + Horizon backends.**

Open source, lightweight, browser-based (self-hostable via Coolify). **Replaces Postman entirely for our stack.** Zero cost, no account, full team-shareable via Coolify deployment.

Ultraboost impact: *moderate.* Frees an API-testing licensing question before it becomes one.

---

**B4. Speechma (free TTS, 580+ voices) — voiceover for Horizon lessons.**

MarketryPro card 03. If Horizon ships any voiceover-narrated lesson (M1 explainers, Tips & Techniques cards), Speechma is the free path. Test-quality-first; if narration quality doesn't hit Horizon's brand bar, escalate to ElevenLabs ($17/mo). **Do not skip the free-first step.**

---

### Tier C — evaluate but likely defer (real value, wrong moment)

**C1. Higgsfield / Suno / Udio / Nano Banana / Midjourney / Flow** — media-generation.

These are real. They are excellent. **They do not belong in Horizon's Q3 stack.** Horizon's Q3 is curriculum-and-assessment; media generation is a Q4 concern. Filed here as *"when we get to Pinterest library production, revisit."*

**C2. Fine-tuning via OpenAI GPT Builder / Hugging Face / Cohere / NVIDIA AI Foundations** (Money Trendz card 6).

Fine-tuning becomes right *after* Horizon has ~500 pages of curated Thai-AI content and a coherent taxonomy. Fine-tuning before that produces expensive noise. **Revisit after Horizon's M1–M3 content library is dense enough to be a corpus.** In 2026 the emerging alternative to fine-tuning — Skills + MCP + long-context — is often the correct move for Horizon's use cases anyway; per [[Input 53 — Claude Skills marketplaces]] the substrate has shifted.

**C3. Papercups (Intercom alternative)** — open-source live chat.

Legitimately useful if Horizon needs a live-chat channel. **Q4 concern.**

**C4. Framer / Lovable / Rezi / Teal / QuillBot / Originality.ai / DeepL / Google Translate / Recraft / Looka / GitMind / Mapify** — all valid, none Q3-critical.

Non likely already has strong mental models for the ones that matter (DeepL, Google Translate, Recraft). The others are for *Horizon learners* to discover through the M2-A/M2-B 100-use-case grid, not for us to install ourselves right now.

---

### Tier D — hard skip

**D1. ALLGPT / Emailnator / "They Want to Hide These Websites" clickbait** — engagement-shape social-media content that promises free access to paid AI tools or disposable credentials.

**Do not integrate.** *Reasons:*

- ALLGPT's business model of "free access to GPT-5/Claude/Gemini" almost certainly involves ToS violations against OpenAI/Anthropic/Google. Any Horizon endorsement of this creates legal + reputational risk that is not remotely worth the free-tokens value.
- Emailnator's disposable-Gmail generation is a real anti-abuse concern for the platforms it targets; Horizon should not teach abuse-adjacent techniques.
- The "hide these websites" post is pure engagement bait; there is no signal in it worth Horizon's endorsement.

Per Horizon's **Honesty Layer** discipline (Inputs 26, 41, 56, 58 + grandfather coda) — *"we teach the actual best practice, not the workaround."* Skipping these three is part of what makes Horizon credible to SEIC/depa/MoHE audiences.

**D2. "70 Ways to Make Money Today" grid / "RIP Video Editing" / "Coding is Dead" / "Scary Websites That Shouldn't Be Legal" — same category, hard skip.**

## What I did NOT integrate but explicitly noted for later

- **NVIDIA "Lowest Token Cost AI Factories" blog** (https://blogs.nvidia.com/blog/lowest-token-cost-ai-factories/) — this is likely a hardware-economics piece relevant to Horizon Research paper #25 on the *economics of AI inference in Southeast Asia*. Worth a WebFetch pass and its own brief when Horizon Research turns to inference-economics. Not integrated today.

- **KitCost mobile-100% stack** — already filed as [[Input 54]] earlier today; reappearance in this batch reconfirms the pattern rather than adding a new input.

## The Ultraboost verdict — three sentences

**This batch is 3 Tier-A moves, 4 Tier-B moves, and ~20 Tier-C/D distractions.** *Do not treat the volume as urgency* — the 3 Tier-A moves (install JANUSTIU Skills + do Learn Git Branching + adopt NotebookLM) unlock ~70% of the productivity gain the batch offers. **Skipping the Tier-D bait maintains the Honesty Layer discipline that separates Horizon from the tier of Thai AI-content this batch was sourced from.**

## SPADA routing summary — one line per agent

- **Human (Non):** install the 6 JANUSTIU Skills; do Learn Git Branching levels 1–6; try NotebookLM once with any 3 PDFs.
- **Claude/Cowork (me, orchestrator):** wrote this brief; will prep the TARI-Horizon depa/สอวช. briefing document ([[Input 59]] action #3); will draft Work Orders for Codex on Tier-B items when Non greenlights.
- **Codex:** eventual Work Orders — Coolify VPS setup, n8n installation on Coolify, Trigger.dev integration on Horizon backend, Hoppscotch self-host.
- **Antigravity:** eventual Work Orders — Horizon frontend uses HTML Anything skill for slide-style lessons; Designer Skills for UI-review passes.
- **Hermes:** substitute labor available for any bulk-processing task on the 20-tool catalog (e.g., "check each of these 20 tools' current pricing" — Hermes runs locally, free tokens).

## Cross-references

- [[Input 53 — Claude Skills marketplaces]] — Anthropic-canonical Skills framing this batch's JANUSTIU cards implement
- [[Input 54 — KitCost mobile-100% stack]] — the mobile-first practice this batch complements
- [[Input 58 — Manabu machine-consumes-itself]] — the Honesty Layer justification for Tier-D skip
- [[Input 59 — AIS TARI]] — the national-standards positioning move this batch's tools serve
- [[feedback_no_localhost_ship_principle]] — the discipline that routes us to Coolify+n8n over Zapier+Make
- [[feedback_always_mvp_make_it_exist_first]] — the discipline that makes Tier-A > Tier-B > Tier-C ordering non-negotiable
- [[reference_spada_team_architecture_and_my_role]] — the routing that determines who does what
- [[brief.md]] master Horizon brief — request: add a new sub-section *"The Horizon Working Toolkit"* pointing to the Tier-A install list
- Non's CLAUDE.md — the anti-template-poison discipline that makes Taste Skill + Designer Skills Tier-A picks
