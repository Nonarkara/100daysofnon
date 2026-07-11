# Input 16 — Full ChatGPT Prompt-Writing Formulas taxonomy (superset of Input 13)

**Image:** `16-chatgpt-prompt-writing-formulas-full-taxonomy.png`
**Source:** smarterwithai.com (wordmark visible at bottom). This is the same source as Input 13, but a wider table — 17+ formulas vs Input 13's 5.

## The taxonomy — formulas read off the chart

| Acronym | Components | Main purpose |
|---|---|---|
| **AIDA** | Attention · Interest · Desire · Action | Persuasive Writing, Advertising |
| **ASK** | Answer · Source · Knowledge | Explanatory Writing |
| **CREAC** | Claim · Reason · Evidence · Analysis · Counterclaim | Academic Essays |
| **CREATE** | Create · Reasons · Evidence · Analysis · Tie-back | Academic Essays |
| **EPL** | Ethics · Pathos · Logos | Persuasive Writing, Reasoning |
| **FAB** | Features · Advantages · Benefits | Service or Product Promotion |
| **INTRO** | Introduction · Background · Thesis · Roadmap | Academic Essays |
| **OAR** | Objective · Audience · Research | Explanatory Analysis |
| **PEEL** | Point · Evidence · Explanation · Link | Academic Essays |
| **PIE** | Point · Illustrate · Explanation | Explanatory Writing |
| **PSA** | Problem · Solution · Action | Persuasive Writing, Explanation |
| **PSAT** | Problem · Solution · Advantages · Threats | Business Planning |
| **SBD** | Summary · Background · Details | Business Reports |
| **SOAPSTONE** | Speaker · Occasion · Audience · Purpose · Subject · Tone | Media Briefing, Speaker Notes |
| **STAR** | Situation · Task · Action · Result | Job Interviews |
| **SWOT** | Strengths · Weaknesses · Opportunities · Threats | Strategic Planning |
| **TAS** | Topic · Audience · Solution | Argument Writing |
| **TEA** | Topic · Evidence · Analysis | Argument Writing |

(Some classical writing-pedagogy formulas — PEEL, PIE, SOAPSTONE, STAR, SWOT, CREAC, AIDA — were not invented for AI; they're pre-existing rhetorical / business frameworks now repurposed as prompt scaffolds. That's a teaching point itself: *prompt engineering inherits 200 years of rhetorical pedagogy*.)

## Non's three structural directives, verbatim

> *"these could be in the artifact, like a Pinterest-style tab"*

> *"can also be kind of blended into the answers if you give it to people when they answer correctly. Maybe some tips that show that there are many multiple ways of prompting and not just one depending on your goal."*

> *"the main idea is not to treat these as something to memorize, but more like you're telling your colleagues or your staff to work for you. What are the things that you need to tell your colleagues and staff who don't have the same information you have to get to the goal you want?"*

> *"if you don't know about your goal, you can also ask AI to help you with what might be the right goal. Definitely it is usually better, many, many times better, if you have a goal in mind before you go ask AI, because otherwise AI will probably try to find shortcuts, and when that happens you might not get the result you want."*

Each of these is a curriculum directive. Treat them as four separate features Horizon needs to implement.

## Directive 1 — Pinterest library cards

Every formula in the taxonomy above becomes a card in the **Pinterest-style artifact library** (Input 12 spec). One card per acronym, each showing the components, an example, and the use-case. Filter chip: *"Prompt Formula"* — so a learner can browse just the prompt-formula slice when they want to learn or recall one.

Per Input 12, the cards are individually URL-addressable and shareable. A learner stuck on "how do I phrase this email?" can text themselves the AIDA card, or share the STAR card with a friend prepping for an interview. Each card is a small win in the wild.

## Directive 2 — Tip-blending inside platform answers

This is a **product feature**, not just curriculum content. When a Horizon learner asks the platform's AI assistant a question — say *"help me write an outreach email to a potential client"* — the platform's answer should arrive with an **inline tip card**:

> *"This is an outreach email — try the AIDA formula next time. **A**ttention (open with something that stops the scroll), **I**nterest (show you understand their problem), **D**esire (show what changes for them), **A**ction (one clear ask). The reason this works better than a generic 'write me an email' prompt is that AIDA makes you commit to which beat you're hitting in which sentence, and the recipient feels the deliberateness."*

The tip is delivered *adjacent to* the answer, not instead of it. The learner gets what they asked for AND the prompt-engineering teaching that would have produced a better answer. **The platform models the meta-skill in every interaction.**

This is a Horizon-distinctive product feature. None of the competitors (AIS, Samsung SIC, FutureSkill) have a teaching-AI that surfaces prompt patterns inline. It's a directly buildable feature — pattern-match the learner's request against the formula taxonomy, surface the best match.

## Directive 3 — Delegate-to-a-colleague framing

Non's most pedagogically important sentence in this message:

> *"the main idea is not to treat these as something to memorize, but more like you're telling your colleagues or your staff to work for you. What are the things that you need to tell your colleagues and staff who don't have the same information you have to get to the goal you want?"*

This **reframes prompt engineering from a technical skill to a managerial skill.** The Horizon learner already knows how to delegate to a junior — they do it at work. The taxonomy is just the *vocabulary* for naming what they already do when they're being good delegators.

A Horizon lesson that lands this directly:

> *"Imagine a smart new junior just joined your team. They're capable but they don't know your project, your audience, your goals, or your tone. To get a useful first draft from them on an email, you'd tell them: who the recipient is, what you want them to feel, what the call-to-action is, and what tone to strike. That's exactly **AIDA** — Attention, Interest, Desire, Action. You already know how to do this with a junior; the taxonomy is just the menu of which delegation pattern fits which job."*

This connects directly back to the Input 5 / Input 10 framings ("AI as a team," WEB_TEAM.md) — same insight, formalized for the prompt-engineering layer. **The formulas aren't engineering tricks; they're explicit versions of what good delegators already do tacitly.**

## Directive 4 — Goal-first principle

> *"if you don't know about your goal, you can also ask AI to help you with what might be the right goal. Definitely it is usually better, many, many times better, if you have a goal in mind before you go ask AI, because otherwise AI will probably try to find shortcuts, and when that happens you might not get the result you want."*

This is the **first principle of using AI well.** It deserves its own lesson at the very top of M1. The structure:

1. *"What is the result you want?"* — goal-first. Sit with the question for 60 seconds before opening any AI.
2. *"What does done look like?"* — define completion criteria before any work begins.
3. *"If I don't have a goal yet, what's the right goal?"* — *and now* you can ask AI, but with the explicit framing *"help me find the right goal,"* not *"do the work."* This is the meta-prompt — using AI to clarify the question before using AI to produce the answer.
4. *"What shortcut would AI take if I left this vague?"* — pre-empt the failure mode. If the goal is vague, AI will resolve the vagueness by hallucinating a goal, executing on it, and the learner gets the wrong result.

This is the **inverse of Input 7's executive-judgment cross-cutter** (when to override AI). Here it's *when to formulate the question before asking AI at all.* Both belong in the M1 primitives layer.

Together, the four directives produce one of the strongest M1 lessons: **how to be the good boss your AI deserves.**

## Add to the brief

This input expands M1's prompt-primitives layer from Input 13's 5 mnemonics + Input 10's 3 primitives = 8 rows to **roughly 20+ rows once Input 16's full taxonomy is included.** The grid is large enough that it deserves its own surface — a **Prompt Formula Reference** sub-tool within Horizon, beyond just a printable cheatsheet.

The four directives above should be filed as **product / pedagogy requirements** for the Horizon repo, not as curriculum content alone. Specifically the **inline tip-blending feature** (Directive 2) is a platform feature that should be specced and built — it's a Horizon-distinctive moat against every competitor.
