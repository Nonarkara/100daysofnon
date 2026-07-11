# Input 53 — Claude Skills: progressive-disclosure system + 5 Skills marketplaces (Insightist post)

**Source:** Thai-language post by **Insightist** (same Thai-language content brand as [[Input 7 — CTC 2026 3 AI traps]]). Hashtags: `#Insightist #AI #Claude #Anthropic #Skills`. The post explains Claude Skills + distinguishes them from Projects, MCP, and Custom Instructions, plus lists 5 community Skills marketplaces.

## The substance — distilled

**Claude Skills** is Anthropic's official format for **task-specific workflows loaded dynamically when relevant.** Key technical concept: **progressive disclosure** — Claude decides which Skills apply to a given task and loads only what's needed, preventing context-window overflow.

**4 Skills types:**
1. **Anthropic Skills** — Excel, PowerPoint, Word, PDF (built by Anthropic)
2. **Custom Skills** — built by you for your specific workflow
3. **Organization Provisioned** — distributed across an org (Team/Enterprise plans)
4. **Partner Skills** — Notion, Figma, Atlassian, more — designed to work with each partner's MCP connector

## The clarification post lands — Skills vs Projects vs MCP vs Custom Instructions

This is the **most useful single distinction** in the post. Most learners conflate these four concepts. The post's clarification:

| Concept | What it is | Scope |
|---|---|---|
| **Projects** | Static base knowledge loaded every chat in that project | Per-project |
| **Skills** | Task-specific workflows loaded dynamically when needed | Anywhere in Claude |
| **MCP** | Connects Claude to external services/data sources | Per-tool |
| **Custom Instructions** | Applied broadly to all conversations | Global |

**The compounding insight:** *MCP + Skills together is the right combination.* MCP gives Claude access to tools; Skills teach Claude how to use those tools effectively. **Neither is sufficient alone.** This pairs directly with Input 33's WebMCP standard (tools layer for browsers) and Input 18's multi-agent orchestration discipline (workflow layer).

## 5 community Skills marketplaces

1. [skillsmp.com](https://skillsmp.com/)
2. [claudeskillsmarket.com](https://www.claudeskillsmarket.com/)
3. [skillsdirectory.com](https://www.skillsdirectory.com)
4. [agentskill.club](https://www.agentskill.club/)
5. [skills.pawgrammer.com](https://skills.pawgrammer.com)

**Verification status:** I have not independently checked all 5 URLs in this session. Pattern is consistent with the OSS-marketplace trend documented in Inputs 30 (openapps.pro), 38 (RAGHub), 42 (12-repo list). Per the **two-step OSS discovery discipline** I named earlier today (Input 38) — start at general catalogs, drill into specialized directories — these 5 are the **Claude-Skills-specialized layer** in that taxonomy.

## The Matrix metaphor that closes the post

> *"Claude Skills folder collects Instructions, Scripts and resources that Claude loads dynamically when needed for specialized work. Like the 'I know Kung Fu' scene from The Matrix where Neo loads knowledge into his brain instantly."*

That metaphor is sticky and accurate. Worth pinning as a Horizon teaching anchor — *"Skills are how you load knowledge into your AI's brain on demand."*

## Why this matters for Horizon — concrete M1 + M6 placement

This is the **definitional input** for the Skills layer that today's prior inputs have been circling. **The post deserves to be the canonical reference text** in any Horizon lesson on Skills:

- **[[Input 22 — Codex Desktop Skills install]]** — covered *how* to install. This post covers *what they are* and *how they relate to other Claude concepts.*
- **[[Input 24 — Caveman]]** — Skill that compresses output. This post explains the *progressive-disclosure mechanism* that makes Caveman load only when relevant.
- **[[Input 37 — Visual Plan/Recap]]** — Skills from Builder.io/Agent Native. This post is the *Anthropic-canonical framing* of what skills like those are.
- **[[Input 18 — Non's own multi-agent orchestration skill]]** — Non's skill IS exactly the format this post describes. **Non has been writing Skills for months;** this post explains why that matters at the platform level.

## Three Horizon placements

### 1. M1 + M6 definitional lesson — *"What Claude Skills actually are, and the 4 concepts they're not"*

The Skills vs Projects vs MCP vs Custom Instructions table goes directly into M1 as a foundational clarification. The lesson teaches the learner to *correctly diagnose* which Claude feature solves a given problem.

### 2. Tips & Techniques surface — Skills marketplace navigation card

A 90-second card listing the 5 marketplaces, with the *"start at one, browse, install in 2 minutes"* walkthrough pattern (same shape as the Codex Skills install card from Input 22).

### 3. Horizon Research paper #21 seed

***"Skills, Projects, MCP, Custom Instructions: A 2026 Decision Tree for Choosing the Right Claude Feature for Your Workflow."*** Anchored on this post's clarification. Particularly useful for SEIC / depa stakeholders building internal Claude-based tooling who need to make architecture decisions about which Anthropic feature to invest in.

## Cross-references — Skills is the load-bearing concept of today's M6 architecture

Today's brief has been building toward an explicit **Skills-as-substrate** architecture for Horizon M6. Counting the inputs that contribute:

- **Input 5** — 7-tool AI Toolkit (the *AI as a team* mindset that Skills implement)
- **Input 10** — WEB_TEAM.md (Skills-adjacent file-level scaffold)
- **Input 18** — Non's own multi-agent-orchestration Skill (verbatim Skill spec)
- **Input 22** — Codex Desktop Skills install pattern
- **Input 24** — Caveman (compression Skill, real example)
- **Input 27** — OKF (knowledge layer Skills consume)
- **Input 33** — Persona/WebMCP (browser-tool layer Skills can call)
- **Input 37** — Visual Plan/Recap Skills from Builder.io
- **Input 39** — SYNTAIX list (multiple Skills appeared)
- **Input 42** — 12-repo list (Claude Code + agentic tools, Skills-adjacent)
- **Input 43** — CLAUDE.md architecture (per-project Skill-equivalent)
- **Input 53** (this) — the Anthropic-canonical definition of Skills + 5 marketplaces

**Eleven inputs converge on the Skills concept.** This input is the *naming* of that convergence — the official Anthropic framing that organizes everything else. M6's syllabus should treat Skills as a *named architectural layer* with this post as the canonical definitional reference.
