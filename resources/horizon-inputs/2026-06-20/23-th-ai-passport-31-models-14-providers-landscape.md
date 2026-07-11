# Input 23 — TH-AI Passport: 31 models × 14 providers landscape (June 2026)

**Source:** Thai-language post titled *"TH-AI Passport"*, framed as a single-image landscape view of the AI model ecosystem. Hashtags include `#THAIPassport #AIThailand #โกสินทร์ต้องบินได้ #ChatGPT #ClaudeAI #Gemini #PerplexityAI` and a wider set covering all the providers named. Tagline credited: *"โกสินทร์ต้องบินได้"* — *"Kosin must be able to fly,"* implying a Thai-context aspirational/national-uplift framing.

**Non's two directives:**
1. *"Include this in the research paper that is included in the Horizon45 page."*
2. *"Analyze this as well."*

Both are honored in this file. The research-paper surface is a new Horizon platform feature implied by directive 1 — see the dedicated section below.

## The landscape — 31 models, 14 providers

Organized by provider, with the best-fit task per model as named in the post:

| # | Provider | Models | Best-fit work |
|---|---|---|---|
| 1 | **OpenAI** | GPT 5.5 · GPT Image 2 · O3 | Chat/analysis/code · Image · Deep reasoning + deep search |
| 2 | **Google** | Gemini 3.1 Pro · Gemini 3.5 Flash · Gemini 3.1 Flash Lite · Nano Banana Pro · Nano Banana Flash 2.5 · Veo 3.1 Fast · Lyria 3 Pro · Lyria 3 | Chat/analysis/code (Pro for depth, Flash for speed) · Image (Banana) · Video (Veo) · Music (Lyria) |
| 3 | **Anthropic** | Claude Opus 4.8 · Claude Sonnet 4.6 | Serious chat + document analysis + planning + coding (Opus); ongoing coding + sustained-thinking (Sonnet) |
| 4 | **Perplexity** | Sonar Reasoning Pro · Sonar Deep Research · Sonar | Chat + analysis + code · Deep research synthesis · General chat/code |
| 5 | **X.AI** | Grok 4.1 | Chat / Q&A / analysis / code |
| 6 | **BytePlus** | Seedance Fast · Seedance Standard · Seedream 4.5 · Seedream 4.0 | Video (Seedance) · Image (Seedream) |
| 7 | **Meta AI** | Llama 4 Maverick · Llama 4 Scout | Open-model chat + analysis + code |
| 8 | **Moonshot** | Kimi K2.6 | Chat + analysis + code |
| 9 | **Mistral AI** | Mistral Medium 3 · Mistral Large 3 | Chat + code (Medium); chat + analysis + harder code (Large) |
| 10 | **Z.ai** | GLM-5 | Chat + code |
| 11 | **MiniMax** | MiniMax M2 | Chat + code |
| 12 | **DeepSeek** | DeepSeek-V3.2 | Chat + analysis + code |
| 13 | **Alibaba** | Qwen3-Next | Chat + code |
| 14 | **SCB 10X (Thai)** | Typhoon | Chat + code with **Thai-language context and Thai-use specialization** |

## Non's core thesis from the post

> *"The world of AI is moving from 'use one model for everything' to 'pick the right model for the job.' That's the new skill of the AI-era worker — not just asking AI, but knowing which AI to ask for which kind of work."*

This is **exactly** the thesis Horizon M1 has been building (Input 5: 7-tool AI Toolkit / *"don't use one AI, use them as a team"*). Input 23 is the **landscape-level evidence** for that thesis. Horizon teaches the skill; this input gives the map of available pieces.

---

## Analysis Non requested

### What the landscape tells us about the field's current shape

**Chat/code is commoditized.** 12 of the 14 providers have a chat+code model. The differentiator isn't the existence of one but the *integration* with the user's workflow (Cowork-style multi-agent orchestration, IDE plugins, web vs desktop vs API, etc.). For Horizon learners, *which* chat-code model matters less than *how* they use any of them with the orchestration discipline M1 + M6 teach.

**Image generation is consolidating around 4 names.** GPT Image (OpenAI), Nano Banana (Google), Seedream (BytePlus), and the open-model ecosystem. Each has stylistic biases. M2-A learners doing creative work need to know all four to pick situationally.

**Video generation is duopoly+.** Google Veo + BytePlus Seedance are the two named flagships; Sora is conspicuously absent from the post (worth noting — either omitted by oversight or treated as part of OpenAI's general stack). Horizon M2-A or a future *applied-creative* track teaches video-generation prompting against these.

**Music generation is single-provider.** Lyria (Google) is the only named music model. This is a narrow market; Horizon doesn't need a dedicated music module, but a Tips & Techniques card on *"if you need music"* is worth including.

**Deep research is a real category, not just a buzzword.** OpenAI O3 and Perplexity Sonar Deep Research are both flagship offerings positioned for this. This validates the *purpose-based assessment* thesis from M3 — *"research" is no longer just searching; it's synthesis-with-citation, and the right tool genuinely matters.*

**The Thai-context model: Typhoon (SCB 10X)** — this is the single most important entry in the landscape *for Horizon's audience*. Most learners producing Thai-language content, working in Thai business contexts, or building Thai-language consumer products should reach for Typhoon as the *default* model for Thai-context work, not as a fallback. Horizon should:
- Position Typhoon as **the canonical model** for Thai-language tasks
- Teach learners *when* to reach for Typhoon vs an English-trained model and *why*
- Build a relationship with SCB 10X if possible (Horizon's EAD provenance gives institutional standing to do so)

**Conspicuous absences from the landscape post:**
- **No voice / speech / TTS models named** (Whisper, ElevenLabs, OpenAI Voice, etc.) — Horizon's curriculum mentions Wispr Flow (Input 5) for voice-to-AI; the post omitting voice is an oversight, not a market gap.
- **No embedding-only models named** (Voyage, Cohere embeddings, BGE, etc.) — these matter for the pgvector / RAG use cases (Inputs 19, 20).
- **No agent-orchestration platforms named** (Cowork, LangChain, AutoGen, CrewAI, etc.) — these are *meta-providers* that compose across the 31 models. They sit one layer up from the model layer. Horizon teaches Cowork specifically (M6).
- **No coding-specific models named** (Claude Code is the application, not the model; same for Codex, Cursor) — the post treats coding as a use-case rather than a separate category. This is a minor framing choice but worth noting for the research paper.

### Strategic implications for Horizon

**Pricing matrix:** The post treats all 31 models as functionally available, but real access varies (Typhoon free at SCB 10X for limited use; Claude Opus paid via Anthropic Console; Gemini Pro paid via Google AI Studio; OpenAI O3 expensive per call; open models like Llama/Qwen/DeepSeek free if self-hosted but require GPU). Horizon's research paper should add a **cost-and-access matrix** alongside the capability matrix. A learner in Thailand asking "which should I use?" needs *both* axes: capability + cost.

**Model-task fit table the learner can use:**

| If you're doing this... | Reach for these (in priority order) |
|---|---|
| Thai-language anything | Typhoon → Claude Sonnet → Gemini Pro |
| Code (production) | Claude Sonnet 4.6 → Claude Opus 4.8 → Gemini 3.1 Pro |
| Deep research + citation | Sonar Deep Research → O3 → Gemini Deep Research |
| Image generation | Nano Banana Pro → GPT Image 2 → Seedream 4.5 |
| Video generation | Veo 3.1 Fast → Seedance Standard |
| Long-context document analysis | Claude Opus 4.8 → Gemini 3.1 Pro |
| Fast, cheap chat in volume | Gemini Flash → Llama 4 Scout (self-hosted) |

This table is a Horizon-distinctive **decision aid** — a learner using it once internalizes the "pick the right model" skill the post argues is the new differentiator.

### What's missing from the landscape that Horizon should teach

The post is descriptive (here are the 31 models). It doesn't address:
- **When to use multiple models in a single workflow** — Horizon M1 teaches this (the 7-tool toolkit pattern from Input 5)
- **How to switch between models without redoing all your prompts** — Horizon should teach the *portability discipline* (write prompts in formula-shapes per Inputs 13, 16, 17, not in model-specific tricks)
- **How to evaluate when to upgrade to a newer model** — M3's purpose-based assessment applies: *did changing models improve the outcome metric you actually care about, or just the benchmark score?*
- **How to budget across providers** — practical cost management as multi-provider use scales

These are the **integration-layer skills** the post doesn't teach but Horizon can. They're a Horizon moat.

## The new platform surface Non named — "Research Paper that is included in the Horizon45 page"

This is a **new product feature for Horizon**: a research-papers/whitepapers section on the platform.

### Spec proposal

**Surface name:** *Horizon Research* (or similar — name TBD)

**Surface purpose:** publish substantive long-form analysis that:
- Establishes Horizon's authority in the Thai AI-education market
- Functions as recruiting content (the academic-credibility version of Pinterest cards)
- Provides citable references for Horizon learners writing their own work
- Earns inbound links from Thai-language tech press and depa/SEIC ecosystem partners

**Seed papers from today's inputs:**
1. ***"The AI Model Landscape — June 2026 (Thailand Edition)"*** — Input 23 expanded with cost-and-access matrix, the Typhoon-default-for-Thai positioning, and the integration-layer skills section above
2. ***"From AI-Built Frontend to Real System — The Supabase Bridge"*** — Input 20 expanded with worked examples in Thai business contexts
3. ***"Multi-Agent Orchestration in Production — Lessons from Running 10 Parallel Agents"*** — Non's own skill spec from Input 18, published in Horizon-branded edition as a case study of his actual practice
4. ***"The 5 At-Risk Thai Jobs and What to Build Instead"*** — Input 11 expanded with Thai-specific labor-market data and the survival-pivot matrix
5. ***"The 4-Tier AI-Adoption Ladder for Thai Professionals"*** — Input 14 expanded with case studies from Non's TKC, Chonburi, Chula engagements

Each paper is downloadable as PDF, has a citation handle (e.g. `Horizon/RP/2026-06/01`), and is the long-form version of a Pinterest library card. **The research-paper surface and the Pinterest library reinforce each other** — cards are the entry point; papers are the depth.

The research-paper surface gives Horizon an **academic credibility layer** that no Thai-language AI-education competitor has. Combined with Non's actual academic credentials (PhD, four-continent practice), this is the moat that makes Horizon a credible *peer-of-academic-institutions* offering, not just a paid course.

## Cross-references

- **Validates Input 5 (7-tool toolkit)** at the landscape level — the *team-of-tools* approach the toolkit illustrates is now backed by a 31-model field of choices
- **Refines Input 16 (prompt formulas)** — formulas should be written in *model-agnostic* shape (R-T-C-C-O), so a learner who switches from Claude Sonnet to Typhoon for a Thai task doesn't need to relearn the prompt
- **Refines Input 18 (multi-agent orchestration)** — multi-agent now means *multi-model-multi-agent* — your Cowork fleet can include agents running on different model providers per their best-fit work
- **Refines Input 20 (Supabase)** — the pgvector embeddings discussion needs to mention which embedding model (Voyage, Cohere, BGE) goes with which retrieval model (Sonar Deep Research as a retrieval consumer, etc.)
- **Anchors the new Horizon Research surface** alongside the existing Pinterest library, Personal Path Generator, Backend Buddy, and Tips & Techniques surfaces

## Add to the brief

This input adds (a) a new platform surface — *Horizon Research* — and (b) refines the integration-layer skills Horizon teaches. Update brief.md accordingly.
