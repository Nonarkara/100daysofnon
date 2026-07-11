# Input 37 — Builder.io / Agent Native: Visual Plan + Visual Recap skills for coding agents

**Source:** Thai-language post by *#peesamac* (the same source as Input 27 on OKF). Hashtags: `#peesamac #AI #ClaudeCode #vibecoding #BuilderIO`. Released **mid-June 2026** per the post — extremely recent.

**Verified during research:**

- ✅ Repo: [github.com/BuilderIO/skills](https://github.com/BuilderIO/skills) — "Skills for coding agents"
- ✅ Framework repo: [github.com/BuilderIO/agent-native](https://github.com/BuilderIO/agent-native) — "A framework for building agent-native applications"
- ✅ Plans app: 100% free and open source, hosted version + local-files mode (writes MDX locally + localhost bridge) + self-host option
- ✅ Skills confirmed to exist: visual-plan, visual-recap, quick-recap, others
- ⚠️ Steve Sewell as CEO — publicly known fact about Builder.io but not directly confirmed in this search; consistent with his role at Builder.io
- ⚠️ "2.2k stars" specific count — not directly verified; broadly plausible for a Builder.io mid-June 2026 release
- ⚠️ MIT license claim — likely accurate per Builder.io's standard but worth confirming before Horizon publishes a recommendation

## What it is

A set of **install-once skills for coding agents** (Claude Code, Codex, Cursor, GitHub Copilot — uses the shared `.agents` path convention) that solve a specific failure mode of agentic coding:

**The problem:** *"You give the agent a task, it jumps into writing code without planning. If it does plan, the plan is a wall of chat text that's hard to read. By the time you realize it's planning wrong, the code is already written."*

**The solution:** convert *long-text plans in chat* into **visual plans with diagrams, wireframes, file maps, annotated code, and open-questions sections** that you can click on and comment on before approving the agent's actual work.

## The two headline skills

### `/visual-plan` — *before* the agent writes code

Generates a plan as an MDX document (Markdown + React components) that includes:
- Diagrams + UI flows
- API specs + schema maps
- **File map** (which files will be touched)
- Annotated code samples
- Open questions for the human reviewer

You review, comment, approve, *then* the agent codes. Plans are viewed in the **Agent-Native Plans app** (hosted free, or local-mode writes MDX to your repo + localhost bridge, or self-host).

### `/visual-recap` — *after* code is written

After a PR is generated, Visual Recap produces an **interactive recap** with:
- File map (what changed)
- Diagrams (architecture impact)
- Schema map diffs
- API diffs
- Annotated diffs
- UI state summaries
- Focused key-changes section

**Reviewers see the SHAPE of the change before reading code line-by-line.**

There's also a GitHub Action that auto-generates Visual Recap for every PR.

### Other skills in the same repo

The post mentions but doesn't unpack: `/agent-watchdog`, `/plan-arbiter`, `/read-the-damn-docs`, `/quick-recap`. All worth investigating in the Horizon Research write-up.

## The conceptual insight worth elevating

The post's closing observation lands the architectural argument:

> *"The faster agents write code, the more the bottleneck moves to 'can I review fast enough?' Having a visual plan before code lets you catch the misses faster."*

This is **the same insight as Bland AI's Invisibility Test (Input 25)** applied to agent-code review — the value isn't in *how impressive the agent's output is*; the value is in *how well a human can verify it before it ships.* Visual plans + visual recaps are the **review-side counterpart** to the Invisibility Test's customer-side framing.

It's also the **operational tooling for the EGO-VOID frame** in Non's own multi-agent-orchestration skill (Input 18) — *"don't trust agent reports, verify against real evidence."* Visual Recap IS that verification, made fast enough that the human can keep up with the agent's velocity.

## Why this matters for Horizon — M6 deepens, plus a new structural lesson

### Three placements

**1. M6 deep upgrade — Visual Plan/Recap as the planning + review tooling layer**

The M6 syllabus from Input 18 (Non's multi-agent-orchestration skill) covers EGO-VOID + AGENT_NOTES.md + ACTIVE CLAIMS + Work Orders + Ground-Truth Verification. **Visual Plan adds the *pre-execution* surface; Visual Recap adds the *post-execution* surface.** Together they make the EGO-VOID discipline *visually consumable in time-with-agent-velocity* — not text-only after-the-fact.

Add to M6 as a sub-lesson: ***"Making EGO-VOID viable at agent-velocity — Visual Plan/Recap as the review-side tooling."***

**2. Pinterest card**

Hook line:
> ***"The faster the agent codes, the slower you can keep up. Visual plans + visual recaps fix that — install once, review at agent-speed."***

**3. Horizon Research paper #12 seed**

***"The Review Bottleneck: Why Agent-Velocity Demands Visual Tooling, and How Builder.io's Skills Move the Frontier."*** Pairs with Input 25 (Bland AI invisibility test), Input 26 (Skill Preservation), Input 32 (Anthropic Fable's modern prompting). The convergent argument: **as agents get faster, the human's verification capacity becomes the binding constraint; the answer is not slower agents but faster verification tools.**

## Cross-references — Visual Plan/Recap as a connective tissue

- **[[Input 18 — Non's multi-agent orchestration skill]]** — Visual Plan/Recap is the *display layer* for the AGENT_NOTES.md + Work Order discipline Non's skill teaches at the text-file layer. Same review discipline, more reviewable interface.
- **[[Input 25 — Bland AI / Invisibility Test]]** — review-side application of the same insight. Don't try to impress with output complexity; design for verifiability.
- **[[Input 26 — Skill Preservation]]** — Visual Plan keeps the human *engaged in the planning step* even when AI is writing the code. Counter-degradation for the planning skill, even if the coding skill atrophies. The plan-arbiter skill in the same repo is specifically about this.
- **[[Input 27 — OKF]]** — Plans are MDX files. MDX in a directory IS OKF-shape. The Plans app's local-mode writes plans to the repo. **The plans are OKF-compatible by default.** Two architecture commitments aligning.
- **[[Input 32 — Anthropic Fable Prompting Guide]]** — the *"longer turns, check progress instead of watching"* observation lands here. Visual Recap IS the progress-check tool that makes long-turn agents reviewable.
- **[[Input 22 — Codex Desktop Skills install]]** — same install-once-and-it's-everywhere pattern, applied to a different layer (planning + reviewing instead of style compression).

## Architecture observation worth surfacing

This is the **second open-source skills package** today (Caveman Input 24 + this) that fits the [Anthropic Skills](https://www.anthropic.com/news/skills) ecosystem and works across Claude Code + Codex + Cursor + Copilot via the `.agents` shared-path convention.

That convention itself is becoming a **de facto standard** — same shape as WebMCP (Input 33) is becoming for browser-side agent tools, same shape as OKF (Input 27) is becoming for knowledge layer. The *.agents directory*, the *document.modelContext registration*, the *OKF type-tagged Markdown* — three vendor-neutral conventions emerging in parallel in 2026, all converging on the same architectural posture: *write once in a standard shape, any vendor's agent reads it.*

**Horizon's M6 syllabus should explicitly name this convergence.** The teaching point: *the OSS agentic ecosystem is finding its conventions, and learners who adopt them now will be portable across whichever agent vendor wins the next round.*

## Add to the brief

Update brief.md to note Input 37 as M6 upgrade (Visual Plan/Recap as review-side tooling) + Horizon Research paper #12 + Pinterest card + the `.agents` convention as part of the 2026 standard-convergence observation.

Source: [github.com/BuilderIO/skills](https://github.com/BuilderIO/skills), [github.com/BuilderIO/agent-native](https://github.com/BuilderIO/agent-native), [agent-native.com](https://agent-native.com).
