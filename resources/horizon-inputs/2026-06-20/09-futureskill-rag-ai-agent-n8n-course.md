# Input 9 — FutureSkill: RAG + AI Agent + n8n + Automation course

**Source:** Thai-language promotional post for FutureSkill's RAG / AI Agent / n8n Automation course. Landing page: https://page.futureskill.co/rag-ai-agent. Promo bundle: 3,390 baht (from 6,470), 4-month installments, e-Tax invoicing, SPayLater. Includes bonuses: Claude Cowork installation course (claimed value 1,190) + Skill.md prompt-pack with install guide. Curriculum: 10 hours 24 minutes, 60 lessons, three expert instructors covering AI Agent / n8n / RAG.

**Non's verbatim framing:**

> *"This tool, but you can learn from my code page. I have much better workflows or a better way of building these without having to use any of the complicated software that requires even a tiny set of skills of computer engineers."*

**Sales positioning of the FutureSkill course (translated and condensed):**

The course positions itself for **2026's new careers**:
- AI Agent design for businesses
- Automation system setup for pages / shops / SMEs
- Freelance AI Workflow work
- RAG-AI chatbot automation (e.g., LINE OA)

Pitch: many businesses want to use AI but *"don't have anyone who can do it"* — that gap is where the skilled freelancer makes money. Outcomes claimed: side-income alongside full-time work, freelancing in AI, adding new services without hiring a team, becoming the person clients pay to do AI for them.

Course tech: AI Agent, **n8n** (visual workflow tool), RAG (retrieval-augmented generation), LINE OA integration.

---

## Why Non flagged this one differently from the others

Inputs 6 (AIS) and 8 (Samsung) are positioned as *competitive landscape to be analyzed*. Input 9 is positioned by Non as *competitive landscape Horizon's curriculum is already better than*. The key claim: *"I have much better workflows or a better way of building these without having to use any of the complicated software."*

Specifically, the FutureSkill course depends on **n8n** — a visual workflow tool that adds an abstraction layer between the user and the underlying AI agents. Non's approach (the one he's running in production at NSP, Chula Control Tower, Chonburi, etc.) skips n8n entirely:

- **n8n approach:** visual drag-and-drop nodes → workflow defined in a tool → tool calls AI → result. Requires learning n8n's UI, paying for n8n hosting, understanding their node ecosystem.
- **Non's approach:** Claude Code directly → orchestration patterns from input 1 (Prompt Chaining / Orchestrator-Worker / etc.) implemented as plain code or as Skill.md files → no visual abstraction layer. The "complicated software" Non doesn't need is n8n itself.

**This is a real differentiator for Horizon.** The agentic-AI module (M2) can be taught two ways: the n8n-flavored way (visual workflows, drag-and-drop, abstraction over agents) or the Non-flavored way (read the codebase, write the orchestration in plain code, no extra tool to learn). Non's approach has the merit that the *only* tool the learner needs is Claude Code itself — same tool they're learning to use. The n8n approach has the merit that it's friendlier to non-coders.

The right call for Horizon depends on the audience. If Horizon is for university students + working professionals (per the EAD transcript), the audience splits — some will want n8n's accessibility, others will want Non's direct power. Horizon could teach both as parallel tracks: *"M2-A: agentic patterns via visual workflows (n8n style)"* and *"M2-B: agentic patterns in plain code (the practitioner track)."* The practitioner track is Non's IP and the moat — no one else teaches it in Thai-language curriculum.

The Cowork-installation bonus FutureSkill bundles is also notable: Cowork is the desktop tool Non himself uses to orchestrate his fleet of code-tasks. FutureSkill knows it's a real tool. Horizon teaching how to *use* Cowork (not just install it) is another moat candidate.

## Add to the Horizon module brief

This input modifies M2 in the brief. Updated M2 entry:

> **M2 — Agentic patterns (the 9)** — anchored by Input 1, with two parallel tracks:
> - **M2-A: visual-first track (n8n-style)** for learners who want low-code accessibility
> - **M2-B: code-first track (Claude Code direct)** for learners who want to skip the abstraction layer
> Each track teaches the same 9 patterns. Each track ends with the learner having shipped 9 working agents to a public URL. The choice between tracks is positional, not hierarchical — the n8n graduate and the Claude Code graduate can both produce the same outcomes.

The brief should also surface that **Cowork itself** is teachable as a Horizon module — the multi-task orchestration pattern Non uses daily is the *living embodiment* of the AI-as-team principle from input 5. A Horizon module on *"running 10 parallel agents with Cowork"* would be the highest-novelty content in the curriculum and the most direct competitor to the FutureSkill course's value proposition.
