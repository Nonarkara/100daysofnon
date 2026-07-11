# Input 39 — SYNTAIX AI's "Top 9 OSS AI Tools" carousel — list useful, star counts unreliable (verified)

**Source:** 9-slide carousel from SYNTAIX AI (visual style: orange-on-black, "+N.NK STARS" callouts on each). Numbered #1 through #9. Filed as `39-syntaix-01-last30days-skill.jpg` through `39-syntaix-09-container.jpg`.

**Non's directive:** *"learn these"* — same active-learning directive as Input 27 (OKF) and Input 34 (BigSet). Not just file; internalize. Per the [[feedback-teach-dont-silently-fix]] principle, I'm surfacing the verification mismatch I discovered immediately rather than absorbing it silently.

## Critical honest finding — star counts are unreliable

**Verified:** Microsoft's MarkItDown (carousel claims **+7.3K stars**) actually has **~139,092 stars** at June 2026 per GitHub. **That's a 19× discrepancy.** The carousel either uses very stale numbers or invented them for content-marketing purposes.

**Implication:** every other star count in this carousel (Last30Days-Skill +12.4K, Headroom +11.3K, Hermes-Agent +10.7K, Taste-Skill +8.4K, Agent-Reach +5.2K, Open-Notebook +4.8K, Career-Ops +4.7K, Container +4.3K) should be treated as **unreliable as published.** If Horizon adopts any of these tools or cites them in Horizon Research, **verify the actual GitHub star count and the actual existence of the named repo before publishing.**

This is the kind of vendor-marketing inflation that EGO-VOID (Input 18) and Skill Preservation (Input 26) exist to defend against. The carousel is *useful as a curation pointer* — these are tools worth investigating — but *unreliable as a metrics source*.

## The 9 tools (with what's verified vs unverified)

### #1 LAST30DAYS-SKILL — research-aggregator skill
- **Claim:** AI agent skill that researches any topic across Reddit / X / YouTube / Hacker News / Polymarket / The Web, synthesizes grounded summary. *+12.4K stars.*
- **Status:** Concept is plausible (matches the Anthropic Skills format from Input 22 + the SearXNG / agent-research pattern). Specific repo not verified in this session. Star count unreliable per above.

### #2 HEADROOM — input compression
- **Claim:** Compresses LLM inputs (logs, tool outputs, files, RAG chunks) before they hit the model. *60-95% fewer tokens.* Available as Library / Proxy / MCP Server. *+11.3K stars.*
- **Status:** Concept is real and important. **Direct complement to Caveman (Input 24).** Caveman compresses *output* tokens; Headroom compresses *input* tokens. **Together they describe the full token-cost-reduction stack.** Specific repo not verified; star count unreliable.

### #3 HERMES-AGENT — long-running agent built by Nous
- **Claim:** Learns workflow, keeps improving, built-in memory, modular & extensible. Private by default. Built by Nous. *+10.7K stars.*
- **Status:** **Nous Research is real** (the team that makes the Hermes model family). A Hermes-Agent product from Nous is plausible but I have not verified the specific repo + star count in this session.

### #4 TASTE-SKILL — aesthetic-quality improvement skill
- **Claim:** Anthropic-Skill-format skill that improves the aesthetic / "taste" of AI outputs. *+8.4K stars.*
- **Status:** Concept fits the Anthropic Skill pattern. Specific repo unverified.

### #5 MARKITDOWN — Microsoft file-to-Markdown converter
- **Claim from carousel:** +7.3K stars. Converts PDFs / Word / Excel / PowerPoint / Text Files to Markdown. `pip install markitdown`.
- **VERIFIED via search:** Real Microsoft tool at [github.com/microsoft/markitdown](https://github.com/microsoft/markitdown). **Built by Microsoft's AutoGen team.** **MIT license.** Supports PDF, PowerPoint, Word, Excel, Images (EXIF + OCR), Audio (EXIF + speech transcription), HTML, CSV, JSON, XML, ZIP, YouTube URLs, EPubs, more. Requires Python 3.10+. Install: `pip install 'markitdown[all]'`. **Actual stars: ~139,092 (19× higher than carousel's 7.3K).**
- **Critical Horizon relevance:** **This is the OKF-compatibility bridge** — Markitdown converts *any* document into clean Markdown that can be directly tagged with OKF frontmatter and dropped into an OKF-shaped knowledge directory. Every Horizon learner running their first OKF knowledge base should start with Markitdown to convert their existing PDFs / Word docs / Excel sheets.

### #6 AGENT-REACH — multi-platform search CLI
- **Claim:** Searches Twitter/X, Reddit, YouTube, GitHub, Bilibili, etc. from one CLI. No API fees. *+5.2K stars.*
- **Status:** Direct positioning competitor to TinyFish (BigSet's web-fetch layer, Input 29). The "no API fees" claim is the differentiator; TinyFish is paid. Unverified specifics.

### #7 OPEN-NOTEBOOK — Jupyter alternative with DB connectors
- **Claim:** Connects PostgreSQL / MySQL / MongoDB / S3 / MinIO / Snowflake / BigQuery / CSV / Parquet. AI-era Jupyter alternative. *+4.8K stars.*
- **Status:** Concept fits the *modern Jupyter alternative* pattern (similar to Marimo, also in openapps.pro from Input 30). Specific repo unverified.

### #8 CAREER-OPS — AI job-search copilot
- **Claim:** End-to-end job search automation — finds jobs (scans 1000+ sources daily), tailors resume, auto-applies with rules, smart follow-up, interview prep, real-time stats. *+4.7K stars.*
- **Status:** Specific use-case agent. Useful as a Horizon teaching example of *"narrow AI agent applied to a specific personal-life domain."* Unverified specifics.

### #9 CONTAINER — second-brain organizer with AI chat
- **Claim:** Capture anything, auto-organize with AI tags, smart natural-language search, connect ideas across knowledge, AI chat with your data. Web/Mac/Windows. *+4.3K stars.*
- **Status:** Concept aligns with the [[Input 27 — OKF]] knowledge-layer + [[Input 19 — codebase-memory-mcp]] graph-layer pattern, applied to personal knowledge management. Also competes with Supermemory (listed in openapps.pro Input 30) and AppFlowy/AFFiNE/Logseq. Specific repo unverified.

## What this whole carousel teaches Horizon — three placements

### 1. M6 lesson — the convergence map of 2026 OSS AI tooling

Today's prior inputs covered specific tools in specific niches. **This carousel is the *list view* that names how the niches connect.** Six of the nine map directly onto today's filed inputs:

- **#2 Headroom** + **Caveman** (Input 24) = full token-compression stack (input + output)
- **#5 Markitdown** + **OKF** (Input 27) = OKF-compatibility bridge for legacy documents
- **#6 Agent-Reach** + **BigSet** (Input 29) = data-acquisition layer alternatives (free vs paid)
- **#7 Open-Notebook** + **Supabase** (Input 20) = data-tier alternatives (notebook vs full backend)
- **#1 Last30Days-Skill** + **Codex Skills install** (Input 22) + **Caveman** (Input 24) + **Visual Plan/Recap** (Input 37) = the Anthropic-Skill ecosystem
- **#9 Container** + **OKF** + **Supermemory** + **Logseq/AppFlowy** (from Input 30) = personal-knowledge-management layer

**Teach the convergence, not just the tools.** Tools come and go; the *architectural slots* they fill are durable.

### 2. Tips & Techniques card — "How to verify a top-N OSS list before trusting it"

The carousel's star-count inflation is itself a teaching artifact. Card content:
- Don't trust headline metrics in vendor-curated lists
- Always click through to the actual GitHub repo
- Check: current star count, last-commit date, contributor count, issues velocity, license
- The list is a *pointer* to investigate, not a *verdict* to trust

This is **EGO-VOID applied to OSS curation discovery**. Same discipline that applied to Caveman (Input 24) and Bland AI (Input 25).

### 3. Horizon Research paper #14 — *"On Vendor-Curated 'Top N' Lists: A 2026 Field Guide to Verification"*

Anchored on this carousel + the Markitdown verification finding + the EGO-VOID discipline. Particularly useful for Thai-language audience that consumes a lot of this content format.

## Critical Markitdown integration recommendation

**Independent of the carousel's reliability**, Markitdown is verified real and load-bearing for Horizon's architecture commitment to OKF. **Update the OKF lesson (Input 27) to mention Markitdown explicitly as the canonical first step:**

> *"You have existing PDFs / Word docs / Excel sheets that contain your team's knowledge? Don't manually retype. Run Markitdown (`pip install 'markitdown[all]'`) on the directory. Output: clean Markdown files. Add `type:` frontmatter per OKF spec. Done — you have an OKF-shaped knowledge base in minutes."*

That sentence converts *months of manual knowledge-migration work* into *one-command-and-some-frontmatter*. **For depa / SEIC / Chula / Mayor Ganop clients that have piles of legacy policy documents,** this is the *practical* path to an agent-ingestible knowledge base. Worth the M1 + M4 + OKF cross-reference.

## Add to the brief

This input contributes (a) M6 convergence-map lesson, (b) Tips & Techniques card on verifying OSS lists, (c) Horizon Research paper #14 seed, (d) **Markitdown as canonical OKF-bridge tool** added to the OKF lesson.

The convergence observation: **after 38 inputs, today has now produced *3 directories* (openapps.pro Input 30 + RAGHub Input 38 + this carousel Input 39) — each at a different curation register.** Generic / specialized / influencer-curated. Horizon's M4 + M6 should teach learners to read all three with appropriate trust levels (high for openapps.pro's hand-curation, high for RAGHub's community-driven model, **low for influencer-curated star-counted lists** — verify before adopting).
