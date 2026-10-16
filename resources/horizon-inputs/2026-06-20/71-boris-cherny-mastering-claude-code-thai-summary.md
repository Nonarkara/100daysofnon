# Input 71 — Boris Cherny's *Mastering Claude Code in 30 Minutes* (Thai summary via @sweexx9 on X)

**Source:** Thai-language summary of Boris Cherny's free 28-minute video, being widely shared on X via @sweexx9. Boris Cherny = Anthropic engineer + creator of Claude Code from scratch. **The video is free; the summary is a distillation, not the primary source.** Non forwarded 2026-07-17 with the direct ask: *"see if this is any use for you."*

**Filed briefly** — this is primarily a *SPADA-orchestrator operational* input, not a Horizon-curriculum-catalog input. Detailed adoption analysis lives in the message-to-Non and the proposed CLAUDE.md draft; this filing captures it for the Horizon Skills-and-Claude-Code layer.

## The video's six named practices (Thai summary distilled)

1. **Agentic framing** — Claude Code is designed for whole-feature work, not line-by-line completion. Don't start with *"write a 3000-line feature"* — plan first.
2. **Q&A over codebase FIRST** — Anthropic uses this on Day 1 of engineer onboarding. Cuts learning time from 2-3 weeks → 2-3 days. Ask: *"how is this file called?"*, *"why does this function have so many arguments? Show git history"*, *"why does fixing this issue require adding if/else here?"* Claude does not just search text — it looks at real usage examples + git history + sometimes GitHub issues.
3. **Plan-first workflow with verification loops** — brainstorm multiple approaches → plan → send for review → ask permission before writing code. **Critical:** give Claude a way to verify its own work (run tests, view screenshots, use browser) → 2-3× quality improvement.
4. **CLAUDE.md — most people use it wrong.** Auto-loaded markdown; three levels: project root (shared via git), user (`~/.claude/CLAUDE.md`), local-not-in-git. Contents: frequent commands, code conventions, important files/structure, team tools, things you keep re-explaining. **Warning: don't write too long — eats context window.** *Killer discipline: when Claude makes a mistake, tell it to write the lesson into CLAUDE.md so it does not repeat next time.*
5. **Shortcuts + setup** — `/terminal-setup`, `/theme`, GitHub app for @claude in issues/PRs, Mac dictation for voice-to-Claude. Key bindings: Shift+Tab (accept), `#` (memory), `!` (bash), `@` (attach), Esc (cancel).
6. **Parallel sessions** — Boris runs 5 terminal tabs + web + git worktrees to prevent collisions. SDK for programmatic use (CI, log analysis).

## Horizon curriculum placement — brief

### M6 Skills-and-Claude-Code layer

Direct fit for the Horizon M6 lesson on Claude Code adoption. Compared to [[Input 22 Codex Desktop Skills install]] and [[Input 53 Anthropic Skills marketplaces]] filed earlier today, this is the *"how to actually use Claude Code well"* companion — not the install/discovery layer but the workflow layer.

Companion citation for Horizon M6 lessons:
- The Anthropic engineer who built it explicitly names the practices → highest-credibility source available for teaching
- The Thai-language distillation is already circulating in Non's target audience — the vocabulary Horizon should use is already Thai-market-established

### Solo Empire pairing

Directly extends the [[Input 54 KitCost]] + [[Input 61 LINE OA MCP]] + [[Input 63 turbo-fieldfare]] Solo-Empire thread — Boris's practices are what turn "one person + Claude" into "one person + Claude that works well."

## Verification pass

- 🟢 Boris Cherny is real, is the Anthropic engineer credited with Claude Code, is publicly named at Anthropic events and in Claude Code release notes
- 🟢 The practices described (agentic use, Q&A-first, plan-first, CLAUDE.md discipline, parallel sessions) are consistent with what other Anthropic engineers and Claude Code power-users describe publicly
- 🟢 CLAUDE.md as an auto-loaded per-project markdown file is documented behavior
- 🟡 **The specific video** (~28 minutes, "Mastering Claude Code in 30 Minutes") — I have not watched it myself, only the Thai summary. If Horizon cites specifics, verify against the actual video before publication.

## Direct SPADA operational implications — the actionable subset

Separate detailed analysis in `resources/spada-notes/2026-07-17-boris-cherny-adoption-notes.md` (proposed). Summary:

- **Q&A-first** — not consistently applied in my Work Orders to Codex; adopt as spec-item
- **Verification loop** — spec explicitly, not as afterthought
- **Project-level CLAUDE.md** — currently absent for 100daysofnon repo; propose creation
- **Mistake-lesson-log discipline** — apply to project-level CLAUDE.md so lessons compound across sessions
- **Parallel sessions via git worktree** — worth confirming SPADA infrastructure supports cleanly

## Cross-references

- [[Input 22 Codex Desktop Skills install]] / [[Input 53 Anthropic Skills marketplaces]] / [[Input 60 Ultraboost Map]] — the install + discovery layer this input completes with the workflow layer
- [[Input 54 KitCost]] / [[Input 61 LINE OA MCP]] / [[Input 63 turbo-fieldfare]] — Solo Empire thread this input strengthens
- [[reference_spada_team_architecture_and_my_role]] — SPADA architecture that adopts these practices
- [[feedback_teach_dont_silently_fix]] — the discipline that maps to *"write the lesson to CLAUDE.md when Claude makes a mistake"*
- [[Non's CLAUDE.md (global standing instructions)]] — the *user-level* CLAUDE.md that already exists; project-level CLAUDE.md is the missing layer
