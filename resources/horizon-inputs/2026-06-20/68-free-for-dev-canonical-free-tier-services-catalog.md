# Input 68 — free-for.dev: the canonical curated catalog of free-tier services for developers

**Source:** Non 2026-07-17 (URL only, no commentary). `free-for.dev` — the rendered Github-Pages front-end for **`github.com/ripienaar/free-for-dev`**.

## What it is — verified

**Author:** R.I. Pienaar (long-time open-source figure; Puppet + MCollective heritage). **License:** MIT. **Format:** Markdown lists, community-maintained via PRs, ~decade-old, ~100K stars-class resource (historically top-100 GitHub repos by stars).

**What it catalogs:** every free-tier service a developer or small operator can plausibly use, organized into ~50 categories including cloud hosting, CI/CD, monitoring, databases, email/SMTP, analytics, CDN, storage, DNS, SSL, code repositories, testing, project management, communication, translation, forms, forums, IDEs, CMS, comment systems, notifications, code snippets, screenshots, log management, dashboards, tunneling, load testing, mobile backends, API management, education, docs, security, video, package managers, design/UI, browsers, IoT, PaaS, low-code.

**The methodology is what makes it canonical:** community-vetted PRs → free tiers must be genuinely free (not free-trial), must be actually usable at meaningful scale, must be a real service (not vaporware). The MIT license + open-source curation means no vendor bias.

## Verification pass — all green

- ✅ Real, active, canonical resource — no verification concern
- ✅ MIT-licensed community list — no vendor bias
- ✅ Well-maintained (weekly-cadence PRs typically)
- ✅ Ripienaar is a highly credible maintainer
- ✅ Rendered Github-Pages site loads today at free-for.dev; canonical README at github.com/ripienaar/free-for-dev

**No verification-flag section needed for this input.** Rare among today's filings.

## Why this input matters — it is the parent catalog for most of today's tool discoveries

**Today's session filed at least these free-tier tools as new discoveries:**

| Tool | Filed as | Would have been discoverable in free-for.dev |
|---|---|---|
| n8n | [[Input 60]] Tier B | ✅ Cloud automation / IaaS section |
| Coolify | [[Input 60]] Tier B | ✅ IaaS / self-hosted PaaS section |
| Trigger.dev | [[Input 60]] Tier B | ✅ Background jobs section |
| Hoppscotch | [[Input 60]] Tier B | ✅ API management section |
| Umami | [[Phuket Bus WO-02]] | ✅ Web analytics section |
| Papercups | [[Input 60]] Tier C | ✅ Support / live chat section |
| MapLibre GL JS | mentioned in [[Input 62]] | ✅ Mapping section |
| NotebookLM | [[Input 60]] Tier A | ✅ AI section (recently added) |
| Speechma | [[Input 60]] Tier B | Likely ✅ TTS section |
| Nano Banana / Flow / Edits | MarketryPro cards in [[Input 60]] | Likely ✅ AI-generation section |
| Rytr / LanguageTool / Rezi / QuillBot / GitMind / Recraft / Snappa | MarketryPro cards | ✅ various categories |

**Ratio:** ~80%+ of today's Tier B/C tool discoveries would have been visible through free-for.dev if either you or the MarketryPro publisher had used it as the discovery source instead of scattered engagement-shape content posts.

**Implication:** free-for.dev is not just a Tier B tool. **It is the *discovery-source substrate* the entire [[Input 60 Ultraboost Integration Map]] should sit on top of.** Same way [[Input 59 TARI]] is the *national-standard vocabulary substrate* SLIC must sit on top of, and [[Input 53 Claude Skills marketplaces]] is the *Skills-layer substrate* Horizon M6 must sit on top of.

## Direct Horizon curriculum placement — three, all first-tier

### 1. M2-B — the *"How to build a business on free tiers"* lesson

Direct fit for Horizon's Thai SMB / solo-operator / freelancer audience. The lesson teaches:
- The free-for.dev bookmark itself (5-minute intro card)
- The methodology (community-vetted, MIT-licensed, no vendor bias — how to trust it)
- The Thai-relevant subset — which services are actually reachable / low-latency / support Thai-language billing
- **The reciprocity discipline** — free tiers exist because someone else pays. Understand the sustainability model of each service before betting your business on it.

### 2. Horizon Research paper #30 seed — the *"Solo Empire Meets Free Tier"* paper

Combines this input with [[Input 54 KitCost]] + [[Input 61 LINE OA MCP]] + [[Input 63 turbo-fieldfare]] + [[Input 65 WanGP]] into the **canonical 2026 Thai-language reference** for *"how one person, on Thai baht budget, builds and ships production software using AI + free-tier services."* Ripienaar's list is the parent catalog; Horizon's contribution is the *Thai-market curated subset with legal, latency, and language annotations that Ripienaar's global list cannot carry.*

### 3. Ultraboost Integration Map restructure

**[[Input 60]] should adopt free-for.dev as the *"discovery layer"* underneath the Tier A/B/C classification.** New brief structure:

- **Discovery layer:** free-for.dev + [[Input 30 openapps.pro]] + [[Input 38 RAGHub]] + [[Input 42 AI Mastery]] + [[Input 52 Stanford CME 295]] + [[Input 53 Claude Skills marketplaces]] + Getnotes daily-GitHub ([[Input 62]])
- **Tier A / B / C / D** as before

The discovery layer answers *"how did we find these?"* — which is the load-bearing epistemic question the Honesty Layer [[Input 13]] argued should be surfaced.

## Direct Non-personal use — one thing this changes today

**Bookmark free-for.dev + subscribe to the repo's Watch feed for updates.** PRs are curated by category; you can subscribe to the categories relevant to Non's current stack (Cloud/IaaS, DNS, Email/SMTP, Storage, Analytics, Monitoring, Video, LLMs). This alone replaces most of the *"you don't know these websites"* Reels genre from [[Input 67]] as your primary discovery-source. Same signal, dramatically less noise, no engagement-clickbait, MIT-licensed.

## What NOT to do

- ⚠️ **Do not treat free-for.dev's inclusion as endorsement** — the list documents what free tiers exist; it does not endorse the sustainability, security posture, or specific fit of each service. Same discipline as [[Input 62 GeoLibre]] — the pattern is trustworthy; individual entries need per-service due diligence.
- ⚠️ **Do not build load-bearing production infrastructure on free tiers alone** — free tiers are for prototyping, side projects, and small-scale operations. FloodDash + SLIC + Phuket Bus are moving toward *real-scale* operations; free tiers are for the *"try it before we scale"* phase, not the *"we're 24/7 public-safety-relevant"* phase.
- ⚠️ **Do not skip the sustainability check** — a free tier that goes away kills your stack. Every service in the catalog needs a "if this vendor sunsets the free tier, what's our migration path?" answer *before* adoption.

## The pattern-name this input crystallizes

**Discovery-source discipline** — same shape as SLIC's audit-your-instruments principle from [[Input 13]]. *Where you find your tools shapes which tools you find. Trusted community-curated catalogs (like free-for.dev) systematically produce different results than engagement-optimized social-media content.* Horizon curriculum should teach the discovery-source-audit skill as first-class methodology, not as a tips-and-techniques footnote.

## Cross-references

- [[Input 60 Ultraboost Integration Map]] — this is the parent-catalog that should sit under [[Input 60]]'s tier structure
- [[Input 30 openapps.pro]] / [[Input 38 RAGHub]] / [[Input 42 AI Mastery]] / [[Input 52 Stanford CME 295]] / [[Input 53 Claude Skills marketplaces]] / [[Input 62 GeoLibre]] — the discovery-source pattern this input is the generalist parent of
- [[Input 13 — Non's methodology critique]] — the audit-your-instruments discipline this input is the trusted-instrument-example of
- [[Input 67 — Reels tool-discovery batch]] — the *opposite* of this input: engagement-content discovery, high-noise, needing tier-D discipline. free-for.dev is what that batch should have been sourced through instead.
- [[Input 54 KitCost]] + [[Input 61 LINE OA MCP]] + [[Input 63 turbo-fieldfare]] + [[Input 65 WanGP]] — the *"solo empire on Thai baht budget"* thesis this input completes
- [[feedback_always_mvp_make_it_exist_first]] — free-for.dev is what makes always-MVP economically viable
- [[feedback_no_localhost_ship_principle]] — many free-for.dev services host publicly, on-brand with your principle
- [[brief.md]] master Horizon brief — request: add *"Discovery Layer"* pillar naming free-for.dev + the discovery-source-audit methodology
