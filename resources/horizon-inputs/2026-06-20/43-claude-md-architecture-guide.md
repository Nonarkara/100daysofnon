# Input 43 — "How to Design a CLAUDE.md That Actually Works"

**Source:** Infographic *"CLAUDE CODE ARCHITECTURE GUIDE — How to Design a CLAUDE.md That Actually Works"* by Claude Code Series 2026.

**The substance:**

**01 — The 3 Scopes** (with conflict resolution): GLOBAL `~/.claude/CLAUDE.md` (personal defaults) → PROJECT `./CLAUDE.md` (project-specific rules) → FOLDER `./src/CLAUDE.md` (module-level overrides). **Last scope wins on conflicts.**

**02 — WHAT/WHY/HOW Framework:**
- **WHAT** (Context): project name + purpose, tech stack + versions, repo structure map, key dependencies, env variables
- **WHY** (Principles): architecture decisions, code style + lint rules, naming conventions, anti-patterns, error handling
- **HOW** (Workflows): Build, Test, Lint, Commit format, Deploy & CI/CD steps

**04 — Be Specific (Vague vs Precise):** *"Write clean code"* → *"Use camelCase for variables, PascalCase for components."* *"Test everything"* → *"npm test --watch, min 80% coverage for utils/"*

**05 — The 5 rules that make it work:**
1. **Run /init first** — let Claude scaffold the baseline, then curate
2. **Stay under 500 lines** — too long = ignored context
3. **Use Hooks for 100% enforcement** — *"CLAUDE.md is ~70% followed. Hooks are absolute."*
4. **Update it monthly** — living document
5. **Reference files, don't duplicate** — point to `package.json`, `tsconfig` — don't copy contents

**Tagline:** *"CLAUDE.md is not a README for humans. It's onboarding docs for your AI teammate."*

## Three Horizon placements

**M6 deep upgrade:** CLAUDE.md joins the trinity of canonical file-level scaffolds — WEB_TEAM.md (Input 10) + AGENT_NOTES.md (Input 18) + **CLAUDE.md** (this) — now four with OKF as the knowledge layer. Together they describe the **complete per-project agent-operating substrate.**

**Pinterest card** — *"CLAUDE.md is not a README for humans. It's onboarding docs for your AI teammate."*

**The "70% followed / Hooks are absolute" insight** is one of the sharpest single-line operational truths in any input today. Goes into M6 as a separate lesson: ***"When to trust soft instructions vs when to enforce with hooks."*** EGO-VOID applied to agent-instruction reliability.

**Direct Non application:** Non runs ~10 parallel code-tasks daily, every one of which reads a CLAUDE.md. The 500-line rule and hooks-vs-instructions insight apply to his own working files. Worth a sweep through his repos to check which CLAUDE.md files have crept past 500 lines.

Source: 2026 Claude Code Series.
