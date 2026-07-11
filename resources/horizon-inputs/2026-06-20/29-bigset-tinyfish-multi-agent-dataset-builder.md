# Input 29 — BigSet (TinyFish): open-source multi-agent system that builds structured datasets from plain English

**Source carousel:** 7 slides from `@fullstackparody` (Instagram-style social tutorial). Filed as `29-bigset-00-intro.jpg` through `29-bigset-06-outcome.jpg`.

**Non's directive:** *"learn these"* — same active-learning directive as Input 27 (OKF). Not just file; internalize.

## Verified source-of-truth (via web search)

- **Repo:** [github.com/tinyfish-io/bigset](https://github.com/tinyfish-io/bigset) — verified to exist
- **License:** **AGPL-3.0** (copyleft — important; see Implications section below)
- **Launched:** ~2 June 2026 per [MarkTechPost coverage](https://www.marktechpost.com/2026/06/02/tinyfish-launches-bigset-an-open-source-multi-agent-system-that-builds-structured-live-datasets-from-plain-english-descriptions/)
- **Pitch:** *"What if you had all the data in the world?"* (the repo's tagline)

## What BigSet does

Take a plain-English sentence — e.g. *"List of Top 20 Tech Influencers. Get their emails, names, country, LinkedIn profile url"* — and BigSet's two-tier multi-agent system (orchestrator + parallel sub-agents) produces a **verified structured table with source links per row**, generated from live web research in **2–5 minutes**. Set a refresh cadence (30 min / 6 hr / 12 hr / daily / weekly) and the dataset stays current. Export as CSV or XLSX.

**Architecture (from the slides + verified):**

| Component | Role | Slide |
|---|---|---|
| **TinyFish Search/Fetch** | Web search + page fetching (the data acquisition layer) | Step 2 |
| **OpenRouter** | LLM routing — Claude Sonnet for schema inference, Qwen for research agents | Step 3 |
| **Clerk** | User authentication, JWT templates (Convex template specifically) | Step 4 |
| **Convex** | Backend/database (paired with Postgres) | Step 5 |
| **Mastra Studio** | Agent orchestration framework | Step 5 |
| **Postgres** | Relational storage | Step 5 |
| **Docker + Make** | Self-host with one command (`make dev`) | Step 1 + 5 |

Services after `make dev`:
- BigSet app → `localhost:3500`
- Convex → `localhost:6791`
- Mastra Studio → `localhost:4111`

## The 5-step setup (from the @fullstackparody carousel — verified against the repo's claims)

1. **Clone the repo + copy env.** `git clone https://github.com/tinyfish-io/bigset.git` / `cd bigset` / `cp .env.example .env`. Requires Docker + Make pre-installed.
2. **TinyFish API key.** tinyfish.ai → API Keys → generate. Paste as `TINYFISH_API_KEY`. Free tier has generous rate limits per the post.
3. **OpenRouter API key.** openrouter.ai → Settings → Keys → create. Add **$5–$10 in credits.** Paste as `OPENROUTER_API_KEY`.
4. **Clerk auth.** dashboard.clerk.com → create app → pick sign-in method. Copy Publishable Key + Secret Key. JWT Templates → new with **Convex template** → grab Issuer URL.
5. **Run `make dev`.** Auto: installs deps, starts Postgres + Convex, generates admin key, deploys schema, brings up frontend. Open `localhost:3500` and sign in.

Note: "5 minutes" total per the carousel; realistically 20-40 minutes if all the third-party signups go smoothly.

## Why BigSet matters for Horizon — three teaching layers

### Layer 1 — Tips & Techniques (the 5-step walkthrough)

Per Input 22's Tips & Techniques surface spec, the 5-step BigSet setup IS a perfect Tips & Techniques card. Two-minute walkthrough, immediate actionable. Caveat (per Input 26 / EGO-VOID): the *"5 minute"* claim should be honestly restated as *"~20-40 minutes for first-time setup including third-party account creations."*

### Layer 2 — M6 worked example (the new agentic-AI reference architecture)

BigSet is the **most complete reference architecture** for an agentic-AI product we've seen in today's 28 prior inputs. It composes TinyFish + OpenRouter + Clerk + Convex + Mastra + Postgres into a working production system that anyone can self-host. That stack is the **2026 default for OSS agentic-AI products** — Horizon's learners building real systems should know it.

Add to M6 as a worked-example lesson: ***"BigSet as an architecture you can clone: how the modern open-source agentic stack composes."*** The lesson teaches:

- Why this stack and not another (each component's job + alternatives at each layer)
- How the agent layer (Mastra) sits *between* the LLM routing layer (OpenRouter) and the data acquisition layer (TinyFish)
- How auth (Clerk) and storage (Convex + Postgres) plug into the agent layer rather than being separate concerns
- The orchestrator + parallel sub-agents pattern (echoes Input 1's Top 9 Agentic Workflows — specifically the *Orchestrator-Worker* pattern)

### Layer 3 — Horizon Research paper #8

Paper seed for the Horizon Research surface (per Input 23): *"The 2026 Open-Source Agentic Stack: A Reference Architecture from BigSet."* Walks through the composition, names alternatives at each layer, discusses the AGPL-3.0 implications for productization, compares to Anthropic Skills (Input 22) and Caveman (Input 24) as adjacent OSS infrastructure.

## Critical license note that the @fullstackparody carousel didn't mention

**BigSet is AGPL-3.0.** This is *copyleft, not permissive.* Implications:

- ✅ **Self-hosted internal use** — completely fine. Run BigSet inside your org, no obligation to publish anything.
- ⚠️ **SaaS-hosted-for-others** — AGPL's network-use clause triggers. If Horizon hosts a BigSet-derived service for external users, **the modified source must be made available under AGPL.** This is the classic "AGPL trap" — fine for users, painful for productizers who haven't planned for it.
- ⚠️ **Bundled into a commercial product** — same. Any commercial Horizon offering using BigSet code must publish modified source.

**The honest recommendation:** Horizon's learners should know about BigSet as a *teach-and-deploy* tool — clone it, learn the architecture, optionally use it for internal data work. **Don't** silently bundle BigSet code into commercial Horizon offerings without explicit AGPL compliance planning.

This is the kind of caveat the @fullstackparody carousel didn't mention (it's a setup-tutorial format, not a productization-advisory format). Horizon's version of the lesson must include it. EGO-VOID discipline applied to licensing.

## Cross-references — how BigSet pairs with today's other inputs

- **Pairs with [[Input 19 — codebase-memory-mcp]]** — both are *context-layer* infrastructure for agents. codebase-memory-mcp builds graphs from existing codebases; BigSet builds tables from web research. Together they describe the *new context backbone* for agentic AI in 2026.
- **Pairs with [[Input 20 — Supabase]]** — BigSet uses Convex + Postgres (a Supabase competitor). Both are real-world options for the *backend layer* of the modern agentic stack. Horizon M4 should teach learners how to choose between them.
- **Pairs with [[Input 27 — OKF]]** — once BigSet generates a structured dataset, exporting to OKF (one file per row, `type:` frontmatter, Markdown links between rows that reference each other) would make the dataset *vendor-neutrally consumable* by any other agent. **BigSet + OKF together = the production knowledge layer.**
- **Pairs with [[Input 18 — Non's multi-agent orchestration skill]]** — BigSet's orchestrator + parallel sub-agents architecture is exactly what Non's skill spec teaches at the meta-level. BigSet is a worked example of EGO-VOID-disciplined multi-agent work shipped as a product.

## Application for SLIC (forwarded separately)

**Critical use-case overlap with SLIC v3.** SLIC needs constantly-updated city-level data: FDI numbers (Input 6 of SLIC today), TFR + birth rates (Input 2 of SLIC today), billionaire density (Input 1), hours-for-$1000 (Input 3), economic-corridor membership (Input 5). All of these traditionally require *custom scrapers per data source* — expensive to build, expensive to maintain.

**BigSet collapses that problem.** Describe what each SLIC tile needs in plain English, set the refresh cadence, get a verified structured table with source links. *"List of cities in ASEAN by billionaire density, last 12 months, with source URLs."* — BigSet builds that table, refreshes it monthly, and SLIC's tile just renders it.

Per Non's "learn this" directive: I'm forwarding this BigSet pattern as a candidate **data-acquisition substrate** to the SLIC code-task. SLIC's existing tile architecture would benefit substantially.

## Add to the brief

This input contributes (a) Tips & Techniques walkthrough, (b) M6 worked-example lesson, (c) Horizon Research paper #8, (d) license discipline content for the AGPL caveat, (e) cross-project SLIC infrastructure recommendation.

Source: [github.com/tinyfish-io/bigset](https://github.com/tinyfish-io/bigset) (AGPL-3.0). Coverage: [MarkTechPost launch announcement](https://www.marktechpost.com/2026/06/02/tinyfish-launches-bigset-an-open-source-multi-agent-system-that-builds-structured-live-datasets-from-plain-english-descriptions/).
