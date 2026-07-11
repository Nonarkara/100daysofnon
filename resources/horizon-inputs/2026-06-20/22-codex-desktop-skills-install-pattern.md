# Input 22 — Codex Desktop Skills: install persistent AI skills in 2 minutes

**Source:** Thai-language post crediting a ProgrammingKnowledge2 video tutorial. Hashtags: `#ChatGPTCodex #AIAgent #CodingTips #AISkills`.

**Non's framing — explicit category instruction:** *"These tips and techniques are too good to not include it somehow somewhere in the tip and technique sections."*

This is **Tips & Techniques** content for the Horizon platform — short, actionable, immediately repeatable.

## The 6-step install pattern (the actionable content)

1. **Open Codex Desktop App** (Windows/Mac, from Microsoft Store or OpenAI; the web version does not have this)
2. **Plugins** menu in the left sidebar
3. **Skills** tab at the top of Plugins. Three categories visible:
   - **Recommended** — system-curated, safe defaults
   - **System** — built-in capabilities (e.g. Image Gen)
   - **Personal** — your own installs
4. **Pick a skill** by browsing categories or searching. Recommended first for first-timers.
5. **Install** by clicking the **+** next to the name, or open and use the toggle. Example named: `Playwright` → installs a Playwright CLI Skill for browser-test automation, immediately available.
6. **(Advanced) Add community marketplace** — Settings → Plugins → **+** → Add More → paste URL `https://github.com/hashgraph-online/awesome-codex-plugins.git`. Adds 50+ community-built skills. **Safety note:** check Scanner Score ≥ 80 before installing community plugins.

The post's punchline: *"Less than 2 minutes. Codex is permanently upgraded. Skills stay with the agent across restarts — you've taught the AI a workflow once, and it remembers."*

## Why this matters for Horizon — the Skills-install layer

This input complements Input 18 perfectly. Input 18 taught **how to write a skill** (Non's own multi-agent-orchestration skill spec — the structure, the EGO-VOID frame, the AGENT_NOTES.md pattern). Input 22 teaches **how to install and use someone else's skill.**

Together they describe the **complete Skills lifecycle:**

| Stage | Input that covers it | Horizon module |
|---|---|---|
| **Discover** existing skills | Input 22 (marketplace + Recommended) | M1 + M6 Tips & Techniques |
| **Install** + configure | Input 22 (6-step pattern) | M1 + M6 Tips & Techniques |
| **Use** in workflow | Implicit across M1, M2, M6 | M1, M2-B, M6 |
| **Write your own** | Input 18 (the skill-authoring spec) | M6 advanced lesson |
| **Share with community** | Implied — the awesome-codex-plugins repo pattern | M6 + cross-cutter Pinterest library |

This is the full lifecycle. Most Thai-language AI courses (AIS, Samsung SIC, FutureSkill) teach *using* AI; almost none teach *installing reusable capabilities* and *authoring your own*. Horizon now has both halves.

## How this lands in the Horizon "Tips & Techniques" surface

Non's framing names a specific platform surface: **"Tips and Technique sections."** This isn't a module — it's a *cross-cutting how-to layer* that lives alongside the curriculum.

Recommendation: a dedicated **Tips & Techniques** tab inside Horizon, populated with bite-sized 2-minute walkthroughs like this one. Per Input 12's Pinterest library spec, each tip is its own card. The cards have a different filter chip from the prompt-formula cards or the use-case cards — they're filterable as *Tips* or *Walkthroughs*.

**Seed candidates for the Tips & Techniques surface from today's inputs:**

| Tip | Source input |
|---|---|
| Install Codex Skills in 2 minutes | Input 22 (this one) |
| The 5 named prompt formulas (PAR/RTF/TAG/BAB/CARE) | Input 13 |
| The full prompt formula taxonomy (17+) | Input 16 |
| The universal R-T-C-C-O scaffold | Input 17 |
| Brief-first / Ask-back-first prompting | Input 10 |
| Quick Tips: *List 5 options* + *Ask clarifying questions first* | Input 17 |
| WEB_TEAM.md template (download) | Input 10 |
| AGENT_NOTES.md template (download) | Input 18 |
| Codebase Knowledge Graph for big repos | Input 19 |
| Supabase for backend-from-AI-built-frontend | Input 20 |
| The Conversation → App pipeline | Input 21 |

That's 11 cards from today alone, all bite-sized 2-minute reads with concrete actions. The Tips & Techniques surface populates fast.

## Caveat — verification discipline applies

The post claims *"Codex 10x smarter in 2 minutes"* — vendor-style hyperbole. Horizon's version should publish the install steps without the hype framing. Same EGO-VOID discipline from Inputs 7 and 18: *teach the technique honestly, without claiming performance you haven't measured.*

Also: the `awesome-codex-plugins` repo is third-party community code. Horizon should add an explicit security-review step to its lesson, not just *"check Scanner Score ≥ 80."* Real lesson: **read the skill's code before installing it — Scanner Score is a heuristic, not a guarantee.**

## Add to the brief

This input contributes to the **Tips & Techniques** cross-cutter (new — not in the brief yet). Update brief.md to add it.
