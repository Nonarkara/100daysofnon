# Input 38 — RAGHub: community-driven directory of RAG frameworks, engines, and evaluation tools

**Source:** X (Twitter) screenshot of a post by **@GitHubProjects**, posted 2026-06-20 06:30 (today, ~10.2k views at screenshot time). Image filed as `38-raghub-rag-frameworks-directory.png`.

**Non's directive:** *"for rag building"* — meaning useful when building RAG systems (in his own work AND for teaching).

## What it is — verified

**Repo:** [github.com/Andrew-Jang/RAGHub](https://github.com/Andrew-Jang/RAGHub) — confirmed real. **53 contributors / 2k stars / 167 forks** at screenshot time. Short URL: osp.fyi/raghub.

A community-driven directory specifically cataloging the **Retrieval-Augmented Generation (RAG)** ecosystem. Where openapps.pro (Input 30) is a *general* OSS directory of 575+ apps, RAGHub is a *specialized* directory for one technical category. **Two complementary directory shapes for Horizon's M4 / M6 lessons.**

## What it catalogs (verified)

- **Compares frameworks by:** use case, scale, complexity, integration, language
- **Distinguishes:** *RAG Frameworks* (libraries) vs *RAG Engines* (standalone platforms) — useful taxonomic distinction Horizon learners need
- **Evaluation tools layer:** ragas, Trulens, Phoenix, Deepchecks — each with a specific niche:
  - **ragas** — quantifies RAG pipeline performance (faithfulness, answer relevancy, context precision)
  - **Trulens** — feedback functions injected after each LLM call, auto-evaluating responses
  - **Phoenix** — observability + embedding visualization (2D/3D projection makes retrieval drift visible)
  - **Deepchecks** — continuous validation + drift detection
- **Coverage:** vector databases, local LLM support, common RAG challenges

## Why this matters for Horizon

RAG is **the canonical use case** for many of today's filed inputs:
- **Vector storage** = pgvector via Supabase (Input 20) or Qdrant / Weaviate / Meilisearch (per openapps.pro Input 30)
- **Knowledge layer** = OKF-shaped Markdown (Input 27) is RAG-source-compatible
- **Data acquisition** = BigSet (Input 29) produces structured datasets that can be embedded for RAG
- **Tool exposure** = WebMCP (Input 33) lets agents call RAG queries as tools
- **Multi-agent orchestration** = RAG is often the retrieval layer that Non's skill (Input 18) coordinates around
- **Knowledge graph for code** = codebase-memory-mcp (Input 19) IS code-specific RAG infrastructure

**RAGHub is the directory that names what tools exist for the RAG-specific slice of the modern agentic stack.**

## Three Horizon placements

### 1. M4 lesson — RAG as the canonical AI-app pattern

Add to M4 (real working systems): ***"Building RAG for your domain — frameworks, engines, evaluation."*** Uses RAGHub as the navigation surface (same way openapps.pro is the general navigation surface in the M4 stack-choosing lesson). Worked example: pick a domain (e.g., a company knowledge base, a help-docs system, a Thai-language LINE bot answering questions from city policy documents), walk through the framework choice + vector DB choice + evaluation tool choice using RAGHub.

### 2. Tips & Techniques card

Hook line:
> ***"Building RAG? Don't pick the first framework you find. RAGHub compares them all (frameworks vs engines, by language, by scale)."***

### 3. Horizon Research paper #13 seed

***"The 2026 RAG Stack: Why Most RAG Apps Are Built on the Wrong Framework and How RAGHub Surfaces the Right One."*** Pairs with the OSS-stack literacy papers (#9 openapps.pro, #11 WebMCP, #12 Visual Plan/Recap). The argument: *most production RAG systems pick a framework based on which one had the best blog post that week; RAGHub lets the framework choice be principled.*

## A practical note for Non's own production work

This is directly applicable to **at least three of Non's existing systems**:

- **The Dao De Jing teaching platform** (the one Non built for his grieving friend, referenced in the TKC + Chonburi lectures) — likely a RAG system over the Dao De Jing text + commentary. RAGHub would help re-evaluate the framework choice.
- **The Nakhon Si Thammarat dashboard** (Mayor Ganop's 4-year track record, LINE bot + purple-dot mapping) — RAG over policy documents + complaint database is a natural extension.
- **The Chula Control Tower** (Input filed in earlier conversation — the system Non built on the 45-min BTS ride) — agentic queries over campus data would benefit from RAG architecture.

For each, RAGHub's evaluation-tools section (ragas / Trulens / Phoenix / Deepchecks) gives Non a way to *measure* RAG quality systematically rather than judging by anecdote. That's the **Skill Preservation principle** (Input 26) applied to RAG quality assurance — don't degrade your judgment about *whether the AI's retrieval is working*; install measurement.

## Cross-references

- **Pairs with [[Input 20 — Supabase]]** — Supabase's pgvector is one of the vector-DB options RAGHub catalogs. M4 should teach the *frameworks-vs-engines* distinction first, then *vector-DB choice* (where Supabase fits), then *evaluation* (where ragas / Trulens / Phoenix / Deepchecks fit).
- **Pairs with [[Input 27 — OKF]]** — OKF-shaped Markdown directories are natural RAG sources. Same MDX-files-as-knowledge pattern that Visual Plan/Recap (Input 37) uses.
- **Pairs with [[Input 29 — BigSet]]** — BigSet generates structured datasets via web research; once you have the structured data, RAG is how an agent queries it. **BigSet + RAGHub-recommended-stack = end-to-end data-to-answers pipeline.**
- **Pairs with [[Input 30 — openapps.pro]]** — general OSS directory; RAGHub is the specialized one. Together they describe the *discovery layer* for the modern OSS stack at two zoom levels.

## Convergence observation worth flagging

This is now the **second specialized OSS directory** today (openapps.pro for general apps, RAGHub for RAG specifically). The pattern is clear: **2026 OSS discovery is moving from generic catalogs to specialized expert-curated directories per technical domain.** Horizon learners benefit from knowing the specialized directories for *their* domain, not just the generic catalog.

For Horizon's M4 / M6 lessons, this means teaching a **two-step discovery discipline:**
1. Start at openapps.pro for the general OSS landscape
2. Drill into specialized directories (RAGHub for RAG, similar directories for other domains as they emerge) for the technical-area choice

## Verification status (EGO-VOID applied)

- ✅ Repo at github.com/Andrew-Jang/RAGHub exists and is described accurately by the post
- ✅ The 4 evaluation tools (ragas, Trulens, Phoenix, Deepchecks) verified to exist and to do what the post claims
- ✅ The RAG Frameworks vs RAG Engines distinction is a real and useful taxonomic categorization
- ⚠️ The 2k stars / 53 contributors / 167 forks numbers are from the screenshot moment; current numbers will differ
- ⚠️ License of RAGHub itself not directly confirmed in this research pass — likely MIT for a community directory but worth confirming before Horizon publishes any derived content

## Add to the brief

Update brief.md: Input 38 contributes (a) M4 RAG lesson, (b) Tips & Techniques card, (c) Horizon Research paper #13, (d) the *"two-step OSS discovery discipline"* convergence observation pairing with Input 30.

Source: [github.com/Andrew-Jang/RAGHub](https://github.com/Andrew-Jang/RAGHub).
