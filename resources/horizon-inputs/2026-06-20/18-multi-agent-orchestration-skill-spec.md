# Input 18 — Multi-agent orchestration skill spec (Non's own working artifact)

**Source:** Non's own Claude Code skill specification, hand-authored from real multi-agent production work. Thai-language with English technical terms throughout. This is the **first input today that is Non's own original work** rather than third-party material — it carries different epistemic weight.

**Non's framing:** *"This may sound a bit technical, but it could be useful to advance stuff that we can also provide in the Horizon 45 page."*

Translation: this is **advanced curriculum content** for the most senior tier of Horizon learners — the ones at T3 climbing to T4 who are running multiple agents in production already and need the orchestration discipline to do it without chaos.

## What the skill spec contains

The full spec is preserved verbatim alongside this brief at `18-multi-agent-orchestration-skill-spec-verbatim.md` (Non's text, untouched). The structural anatomy:

**Frontmatter** — skill name, description, trigger phrases. Tells Claude Code when to invoke this skill.

**Section 0 — Frame:**
- When to use the skill (≥2 agents + human on the same codebase, orchestrator/reviewer role)
- The supreme principle: **EGO-VOID** — *"direct, not flattering, no rubber-stamp acceptance. Value identifying gap/risk + what to verify before live use over giving confidence. Every work acceptance = real evidence, not the agent's word."*

**Section 1 — Roles & Ownership:**
- Orchestrator/Reviewer (e.g. Claude/Cowork)
- Builder agents (e.g. Codex for backend, Antigravity/Gemini for frontend)
- Human Lead (final authority on irreversible actions, credentials, infra)
- Zone rules: divide domains clearly, give orchestrator content/doc ownership

**Section 2 — `AGENT_NOTES.md` — the communication backbone:**
- Single central log file all agents read/write
- Newest-first; every entry has `## [from -> to] date — topic` header
- **D-E-R review structure:** Describe (real state) → Evaluate (strengths/gaps/risks) → Recommend (next assignment)
- Always include commit SHA / real evidence
- Commit from native environment (not through mounts that mistranslate files)
- Template entry: Verdict (✅/❌/⚠️) + Verified (real evidence) + Gap/Risk (EGO-VOID) + Next Assignment

**Section 3 — `ACTIVE CLAIMS` — preventing file-edit collisions:**
- Agents must claim path before editing
- `[ACTIVE]` / `[DONE]` states
- Claims as narrow as possible; if two claims overlap a path, sequence — don't parallelize

**Section 4 — Work Order (WO) — unit of delegation:**
- Mission, Ground Rules (hard constraints), Phases with per-phase Acceptance, Naming standards, Definition of Done, File Scope (claim)
- Break into phases that can be parallelized + identify which phases depend on infra/human

**Section 5 — Ground-Truth Verification (the section Non flagged as most important):**
- *"Don't trust agent reports — verify reality"*
- origin = authoritative (verify via `git ls-remote`, not the agent's "push successful" log)
- CI conclusion = quality reality (`gh run list/view`); *"local verify passes ≠ CI green"* and *"config valid ≠ runtime working"*
- Beware sandbox/mount phantoms — file appears deleted/changed when not real
- Security scan before acceptance — no keys/secrets/PII in commits
- SHA verification — agents often report SHA imprecisely

**Section 6 — Safety-First Sequencing (irreversible work):**
- Irreversible actions (create public repo, delete files, move secrets to public, transfer money, change keys) = **gate with human + verify in detail + breach test** — never let agent do alone
- Separate parallelizable work vs blocking work — pure-logic tasks start immediately; infra/human-dependent tasks defer
- Prefer new files over editing shared files (reduces collisions)
- *"#0 risk = uncommitted work surviving across rounds"* — force commit+push before next work / before pausing

**Section 7 — Anti-Patterns (lessons from real production work):**
- Accepting work from agent reports without checking origin/CI/real code
- Claiming metrics without evidence ("CI green" / "Lighthouse ≥90") — if tooling can't run, de-scope and record truthfully, don't fake numbers
- Chasing flaky tooling debug indefinitely (e.g. chrome-launcher on Windows) — timebox, then de-scope
- Leaving uncommitted work across sessions
- Scope creep — adding work without cutting work
- Committing junk/secrets
- Claims too broad, overlapping other agents' zones

**Section 8 — Quick Checklist:**
- Before "accepting" agent work: commit on origin verified, CI green verified, code/behavior reviewed, no secrets, working tree clean
- Before "delegating next": task + DoD + Acceptance defined, claim/file-zone clear, irreversible actions gated to human, AGENT_NOTES updated with D-E-R, parallelize what can be, defer what can't

**Closing — How to adapt to other projects:**
1. Place `AGENT_NOTES.md` at project root + `## ACTIVE CLAIMS` section
2. Define each agent's role/zone in README or project instructions
3. Write big work as Work Orders per template
4. Every send/receive of work follows EGO-VOID + ground-truth verification
5. Adapt tool names to your stack — principles stay

## Why this matters for Horizon — the M6 anchor finally lands

M6 — *Running 10 parallel agents with Cowork* — was previously the most aspirational module in the curriculum, anchored on Non's daily workflow but without a concrete syllabus. **Input 18 IS the M6 syllabus.** The skill spec is six lessons end-to-end:

| M6 lesson | Anchored on |
|---|---|
| **L1 — Why orchestration matters** | The frame + EGO-VOID + roles/ownership (sections 0, 1) |
| **L2 — The communication backbone** | AGENT_NOTES.md + D-E-R review format (section 2) |
| **L3 — Preventing collisions** | ACTIVE CLAIMS pattern (section 3) |
| **L4 — Work Orders + Definition of Done** | WO template (section 4) |
| **L5 — Ground-truth verification** | Section 5 — *the heart of the module* — don't trust agent reports, verify against git/CI |
| **L6 — Safety, anti-patterns, and adaptation to your own stack** | Sections 6, 7, 8 + adaptation guide |

**Shipped artifact for M6:** the learner sets up `AGENT_NOTES.md` + `ACTIVE CLAIMS` in their own project, writes one Work Order, runs at least 2 agents through one cycle of claim → work → review → next-delegation, and submits the resulting AGENT_NOTES log as proof. **This is the most advanced shipped artifact in the entire Horizon curriculum** and it directly demonstrates T4-level practice (running parallel agents in production with discipline, sharing the log publicly).

## Why this is Horizon's deepest moat against every competitor

The skill spec contains operational knowledge that *can only come from running 10+ parallel agents in production* and surviving the failure modes. The anti-patterns section in particular reads like a war diary:

- *"Beware sandbox/mount phantoms — file appears deleted/changed when not real."*
- *"CI green ≠ local verify passes."*
- *"Don't chase flaky tooling indefinitely — timebox, then de-scope."*
- *"#0 risk = uncommitted work surviving across rounds."*

Each of these is a hard-won lesson. **AIS, Samsung SIC, FutureSkill, and the Thai-language course-seller community have nothing remotely like this.** They teach AI as a tool. Non teaches AI as a *team you manage*, with the operational discipline of a software production lead who has actually shipped under multi-agent conditions. That's the M6 moat.

It's also the **ultimate validation of Non's own credibility for Horizon** — the lessons in this spec are from his actual practice running NSP, Chula Control Tower, SLIC, AlphaEarth, TKC, Horizon-itself, 100daysofnon, and others in parallel via Cowork code-tasks. The teacher demonstrates the curriculum every day.

## Three structural recommendations for Horizon's integration

### 1. Publish the skill spec as a downloadable Horizon-branded artifact

The current spec is the working version Non uses. A **Horizon-branded edition** — same content, Horizon visual identity, slight pedagogical polish (more examples, lesson-checkpoint questions, glossary for non-developers) — becomes a free downloadable PDF that anyone can use even before enrolling. *Lead magnet.* Distribution via the Pinterest library (Input 12 spec).

### 2. Add Cowork-itself as a teachable platform

Cowork is the desktop tool Non uses to run parallel code-tasks. The skill spec assumes its presence. **A Horizon lesson within M6 on "how to install and configure Cowork for multi-agent orchestration"** would be the first paid education content on Cowork in any market. This is genuinely scarce — most people running multi-agent workflows are inventing their own tooling. Non is one of the few practitioners using Cowork at scale; teaching it is direct knowledge transfer.

### 3. The AGENT_NOTES + D-E-R pattern becomes a Horizon-canonical pattern

Same shape and weight as Input 10's WEB_TEAM.md pattern. **Together, WEB_TEAM.md (M1) + AGENT_NOTES.md (M6) become Horizon's two canonical multi-agent coordination scaffolds.** Both are file-level patterns the learner ships and reuses across projects. Both deserve the Pinterest library treatment with downloadable templates.

## Add to the brief

This input upgrades M6 from "candidate" to "anchored, syllabus-complete." The brief.md M6 row should be updated accordingly. The full skill spec verbatim should also be filed alongside this brief so the Horizon code-task has it for direct integration into the Horizon repo.
