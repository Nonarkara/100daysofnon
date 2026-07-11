# Input 19 — codebase-memory-mcp: Knowledge Graph backend for AI coding agents

**Source:** Thai-language SynapTechAI post (#SynapTechAI #AIAgent #CodingAgent #MCP #DevTools). About **codebase-memory-mcp** — a tool that scans an entire codebase and converts it into a queryable **Knowledge Graph** that AI coding agents can hit directly, instead of grep/read/dependency-chase one file at a time.

## What the tool does

**The problem it solves:** Claude Code, Codex, Gemini CLI and other coding agents currently behave like a developer on day one of a new team — they grep, open files, trace dependencies, read functions, follow the call graph one node at a time. On a big codebase this is slow and token-expensive.

**The solution:** scan the whole codebase up-front into a Knowledge Graph the AI can query. The graph captures: functions, classes, call graphs, HTTP routes, service dependencies, component relationships, Dockerfiles, Kubernetes manifests, Kustomize overlays.

**Performance claims (from the post):**
- Index Linux Kernel (~28M lines / 75,000 files) in **~3 minutes**
- Structural queries **<1ms**
- Massive token reduction vs. file-by-file reading
- Runs entirely local, no source code leaves the machine
- No API key
- Single binary, macOS / Linux / Windows

**Tech inside:** Tree-sitter for AST parsing + Hybrid LSP for type / semantic understanding (gives the *"go to definition"* IDE-grade semantics, not just text matching).

**Use cases the post highlights:**
- *"What services does this route call?"*
- *"If I change this function, what's affected?"*
- *"Find dead code"*
- *"Summarize the architecture of this big repo"*
- *"Analyze this diff — where are the risks?"*
- *"Share the graph artifact across the team so no one re-indexes from scratch"*

**The post's core argument:**

> *"A good coding agent isn't just a smart model. It needs context, memory, graph, rules, and workflow to understand real work. The future of AI coding agents isn't 'what model are you using?' — it's 'how well does it understand your codebase?'"*

## Why this matters for Horizon — fits M6 + validates the curriculum's direction

This input doesn't need a new module. It belongs in **M6 (Running 10 parallel agents with Cowork)** as **the next-generation tooling** the curriculum prepares learners for.

The M6 syllabus from Input 18 covers the *coordination layer* — AGENT_NOTES.md, ACTIVE CLAIMS, Work Orders, Ground-Truth Verification. Input 19's codebase-memory-mcp is the *context layer* — what each agent sees when it sits down to work. The two layers together describe the *complete operating environment* for production multi-agent work in 2026+.

**Suggested integration into M6:**

| M6 lesson | Add from Input 19 |
|---|---|
| **L5 — Ground-truth verification** | Codebase Knowledge Graph as a *source of structural truth* — when an agent claims *"this function isn't called anywhere"*, you can verify against the graph in <1ms rather than trusting the agent or re-grepping yourself |
| **L6 — Safety, anti-patterns, adaptation** | Add a sub-lesson: *"Tooling at the context layer — what's coming and how to choose."* codebase-memory-mcp is the named example. The lesson teaches the *category* of tool (Knowledge Graph backends for agents) so learners can evaluate alternatives as the space matures. |

## The broader curriculum argument

The post's framing — *good agents need context, memory, graph, rules, workflow* — is **exactly the argument Horizon's full curriculum makes across modules:**

| Agent need | Horizon module that teaches it |
|---|---|
| **Context** | M1 (orchestration mindset + brief-first prompting) |
| **Memory** | Cross-cutter on Retrospective + Pattern Library (Input 10) |
| **Graph** | M6 (multi-agent coordination) + Input 19 (codebase graphs as the technical layer) |
| **Rules** | M1's WEB_TEAM.md + M6's AGENT_NOTES.md (the file-level rule scaffolds) |
| **Workflow** | M6's Work Orders + the entire curriculum's "ship-then-retro" cadence |

**This is the strongest external validation of Horizon's curriculum architecture yet seen.** The SynapTechAI post and Horizon's brief are converging on the same view of where AI development is going — and Horizon got there first across 19 inputs of inductive design today.

## Suggested Pinterest card

Per the Input 12 spec: one Pinterest card per input, this one tagged M6 + Tooling + Future-Direction. The card's hook line: ***"Smart model ≠ useful agent. The future asks: how well does it know your codebase?"*** That line stops a scroll on LINE / TikTok and lands a curious mid-career developer on the Horizon landing page.

## Note on caveat for the post's claims

The performance numbers (28M lines in 3 minutes, <1ms queries) are vendor / advocacy claims from the post, not independently benchmarked here. Before Horizon teaches codebase-memory-mcp as a recommended tool, the team should validate the numbers against a comparable open repo (e.g. index Kubernetes or PostgreSQL source, time the build, benchmark query latency) and add the verified numbers to the lesson. **EGO-VOID applies to recommended tooling too:** don't claim performance you haven't verified.

This is the exact discipline the M6 Ground-Truth Verification lesson teaches. Horizon should model that discipline in its own curriculum-development process.
