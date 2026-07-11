# Input 10 — Claude Code as a 6-role web-building team (WEB_TEAM.md pattern)

**Source:** Thai-language LinkedIn / Facebook post titled *"หลายคนใช้ AI ทำเว็บผิดตั้งแต่ Prompt แรก"* (*"Many people use AI to make websites wrong from the first prompt"*). Hashtags: #ClaudeCode #AIAgent #AIAgents #AIOffice #AgenticAI #MultiAgent #VibeCoding.

**Non's verbatim framing:** *"this too is quite cool"* — full endorsement, not critical filing.

## The method, distilled

The post argues that asking Claude Code *"build me a landing page"* produces a page that **looks done but isn't ready to use** — because the AI doesn't know who the buyer is, where the CTA leads, what the form captures, what the mobile version looks like, or who QAs it before client handoff.

The proposed fix is to treat Claude Code as **a 6-role web team, not a single agent**:

| Role | Responsibility |
|---|---|
| **Product Agent** | Goal, audience, offer, CTA, scope |
| **UX Agent** | Sections, flow, wireframe outline, user journey |
| **Frontend Agent** | UI, responsive layout, interaction, components |
| **Backend / API Agent** | Form handling, validation, data flow, integration, error messages |
| **QA Agent** | Responsive, accessibility, copy, state, bugs, confusion points |
| **Release Agent** | Checklist, changelog, handoff note, pre-deploy verification |

## The six-step workflow

1. **Lock the Web Brief before touching code.** Prompt: *"Make a Web Brief for this landing page before coding. Summarize Goal, Audience, Offer, CTA, Constraints, Definition of Done. If anything's missing, ask back first — don't code yet."* The trick is the explicit *"ask back first"* phrase — that switches AI from guess-mode to interview-mode.
2. **Split the 6 agents.** Each owns a function, not just coding.
3. **Create WEB_TEAM.md** — central rules-of-engagement file with: Team Mission, Agent Roles, Workflow, Quality Gate. Same pattern as a CLAUDE.md project file. The post explicitly references CLAUDE.md as the analogue.
4. **Enforce workflow: Brief → UX Plan → Build → Integration → QA → Release.** NOT *Idea → Code → Ship*. Use Claude Code's hooks to run linters / formatters / tests automatically on file events.
5. **Quality Gate before handoff.** QA Agent checks: Responsive (mobile + desktop), CTA clarity, copy clarity, all necessary states (loading/empty/error/success), form validation messages, accessibility (contrast/labels/focus), performance (asset weight), security (no hardcoded secrets, input validation). QA must answer per-item *Pass / Fail / Fix what*, not just *"looks good."*
6. **Retrospective after delivery.** Release Agent summarizes what worked, what broke, which prompts were good, what patterns to keep for next round. This is where the AI Office *learns* — not from each new chat, but from the project's accumulated rules + checklists + workflow files.

## The core insight

> *"A good AI for building websites isn't the AI that codes fastest. It's the AI that works most like a real team."*

This is the same principle Non has been articulating across the rest of these inputs (Input 5: 7-tool toolkit; Input 7: AI as team-member that you can override; class-prep transcript: *"I have ten assistants"*). The post's specific contribution is the **WEB_TEAM.md pattern as a reusable scaffolding** — same shape as CLAUDE.md, applied per-domain instead of per-project.

## Why this matters for Horizon

This input is the **methodology brick** for the orchestration-mindset module (M1) and the agentic-patterns module (M2). Specifically:

- **WEB_TEAM.md is a teachable artifact.** It's a single file with 4 sections (Mission / Roles / Workflow / Quality Gate). A Horizon learner could ship one in 30 minutes per domain. Add this as the *first deliverable of M1* — every learner produces a `*_TEAM.md` for their own working domain (writer's team, marketer's team, researcher's team, smart-city consultant's team, etc.) and uses it for the rest of the course.
- **The Brief-first / Ask-back-first prompt pattern is teachable in one lesson.** Horizon should include this as a core prompt-engineering primitive in M1 — *"how to switch AI from guess-mode to interview-mode."*
- **The Quality Gate checklist (8 items: responsive / CTA / copy / state / form / accessibility / performance / security) is a transferable pattern.** Horizon should teach learners to write their own domain-specific Quality Gates — for a content piece, for a data analysis, for an outreach email, for a smart-city dashboard. The *form* of the checklist transfers; the *content* is per-domain.
- **The Retrospective-after-delivery loop is exactly the missing piece in most AI workflows.** Horizon should make this a graded artifact: every learner writes a retro after each shipped project, and the retros accumulate into a *personal pattern library* (their own playbook). This is durable IP for the learner and a Horizon-distinctive teaching move.

## Add to the Horizon module brief

This input contributes to M1 (orchestration mindset) and M2 (agentic patterns) as a methodological scaffold. The M1 deliverable should be updated:

> **M1 deliverable (updated):** learner produces their own `*_TEAM.md` file defining 4–8 specialized agents for their working domain, plus a Quality Gate checklist they can apply to any artifact in that domain. Submitted as a public Gist or in their portfolio repo.

This is **higher value to the learner** than the original "5-tool workflow document" because it produces a *reusable scaffolding* rather than a snapshot of current practice.

## Note on the post's monetization

The post ends with the standard Thai-community CTA: *"comment WEB and I'll send you the full file."* The "full file" is presumably a polished WEB_TEAM.md template + extended prompts. Horizon should publish its own equivalent template as **freely downloadable**, since making the artifact a paywall content-lead is exactly the kind of value-extraction pattern that bottlenecks Thai AI literacy — and Horizon (with EAD backing) is positioned to undercut on price (free, e-cert-backed) while exceeding on depth.
