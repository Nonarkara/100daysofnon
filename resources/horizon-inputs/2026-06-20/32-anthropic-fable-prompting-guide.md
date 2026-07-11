# Input 32 — Anthropic Fable's Prompting Guide: the modern reasons-and-boundaries pattern

**Source:** Infographic titled *"Anthropic Fable's Prompting Guide."* Attribution bottom-right reads *"@danvk verity"* (or similar — partial legibility). *"Fable"* is presumably an Anthropic agent product/internal name (verification pending; not blocking the substance).

## What the guide says

### Why change prompts (4 reasons)

1. **Instructions** — *"Delete the rule lists. One brief instruction now steers it."*
2. **Old prompts** — *"Test deleting old instructions. Default behavior often beats them now."*
3. **Longer turns** — *"It now runs for hours. Check progress instead of watching it."*
4. **Reasoning asks** — *"Asking it to show hidden reasoning can trigger refusals."*

### How to write the prompt (5 steps)

1. **Give the reason.** Open with *"I'm working on [goal] for [audience]. I need [outcome]. With that in mind, [request]."*
2. **Set the boundaries.** Add: *"If I'm describing a problem, give your assessment. Don't fix until I ask."*
3. **Demand evidence.** Add: *"Audit each progress claim against a real result. Failed test? Show output."*
4. **Pause only where it matters.** Add: *"Pause only for irreversible actions, scope changes, or input only I can provide."*
5. **Let it keep lessons.** Add: *"Keep one lesson per file. Update old notes, delete wrong ones."*

### Old vs new (right-column callouts)

- Old prompt = rules for every edge case
- New prompt = reasons plus clear boundaries
- Hand it your hardest problem and let it scope the work itself
- First run: have it mine past chats for lessons
- Easy tests undersell it. Start at the top.

## Why this matters — it UPDATES the earlier prompt-formula inputs

This is the first input today that **explicitly evolves** prior content rather than adding new content. Per the **teach-don't-silently-fix** principle ([[feedback-teach-dont-silently-fix]]), I'm surfacing the update explicitly:

**Earlier today I filed three prompt-formula inputs:**
- Input 13 — 5 named mnemonics (PAR, RTF, TAG, BAB, CARE)
- Input 16 — full 17+ taxonomy (AIDA, STAR, PEEL, SOAPSTONE, SWOT, etc.)
- Input 17 — universal R-T-C-C-O scaffold (Role + Task + Context + Constraints + Output Format)

**Input 32 doesn't contradict those.** It evolves them. The named formulas are still useful as **scaffolds for specific single-turn requests** (a marketing email, a job interview answer, a SWOT analysis). The **reasons-and-boundaries pattern** is the *modern long-turn, agent-driven, give-me-the-context-not-the-rules* pattern for when you're handing the AI a hard problem and letting it run for hours.

They're complementary, not contradictory:

| Use case | Reach for |
|---|---|
| Single-turn structured output (an email, a SWOT, an interview answer, a paragraph) | A named formula (Input 13 / 16) + R-T-C-C-O scaffold (Input 17) |
| Multi-step agent work that runs for hours and reports back | Reasons-and-boundaries (Input 32) — the *Why-Boundaries-Evidence-Pause-Lessons* pattern |

**The Horizon M1 prompt-primitives layer should teach both, and teach the distinction.** A learner who only knows formulas will under-use modern long-running agents. A learner who only knows reasons-and-boundaries will over-engineer single-turn requests.

## The specific advice worth pulling forward

A few of the lines deserve direct elevation into Horizon's curriculum:

**"Old prompt = rules for every edge case. New prompt = reasons plus clear boundaries."**

This is the **single-sentence summary** of how prompt engineering changed between 2024 and 2026 as models got smarter. Worth pinning at the top of M1.

**"Hand it your hardest problem and let it scope the work itself."**

This is the inversion of Input 28 (Prototype-First vs Plan-First). Input 28 said *you* choose the approach. Input 32 says *let the AI scope the work itself given the reason.* Both are valid; the right choice depends on whether you have the judgment to scope correctly yourself. For a learner at Tier 2→T3 (Input 14's ladder), letting the AI scope is often the *better* default because the learner doesn't yet have the scoping intuition.

**"First run: have it mine past chats for lessons."**

This is meta-prompting — using AI to extract its own teachable patterns from your previous work with it. Direct echo of [[feedback-teach-dont-silently-fix]] — the lessons-keeping discipline is what makes the system compound.

**"Asking it to show hidden reasoning can trigger refusals."**

This is the surprising one. Worth fact-checking separately — the claim is that asking newer models for their CoT directly is more likely to trigger refusals than asking them to *act* on their reasoning. The pedagogy implication: don't force the AI to expose every step; trust the output, audit selectively.

## Three Horizon placements

### 1. M1 sub-lesson — "When formulas stop being enough"

Add to M1 as the **third sub-lesson** (after Input 16's "good boss your AI deserves" and Input 28's "prototype-first vs plan-first"). The lesson:

1. *Named formulas (Inputs 13, 16, 17) are for single-turn structured output.*
2. *Reasons-and-boundaries (this input) is for multi-step agent work.*
3. *Here's how to switch between the two depending on what you're asking the AI to do.*

Lesson-end exercise: take a prompt the learner currently uses (formula-shaped), rewrite it as reasons-and-boundaries for a long-turn agent, run both, compare outcomes.

### 2. Pinterest card

Hook line:
> ***"In 2024 you wrote rules. In 2026 you write reasons. Here's the switch in 5 steps."***

Card body: the 5-step pattern (Reason / Boundaries / Evidence / Pause / Lessons) + the *Old vs New* contrast.

### 3. Tips & Techniques card

A 2-minute walkthrough version: *"How to upgrade a 2024-style prompt to a 2026-style prompt in five minutes."* Take a learner's actual prompt, walk through each of the 5 steps, ship the new version.

## Verification notes (EGO-VOID applied)

- ⚠️ *"Anthropic Fable"* — I don't have independent confirmation that this is an official Anthropic product/agent name. Could be the post-author's own framing. Worth verifying before Horizon Research republishes.
- ⚠️ *"@danvk verity"* attribution — bottom-right of the image; partial legibility. If it's Dan Vanderkam or similar, his published work on prompt engineering would be a useful cross-reference for the Horizon Research version.
- ⚠️ The *"asking for hidden reasoning triggers refusals"* claim — surprising and worth fact-checking against actual Claude behavior before teaching it as established practice.
- ✅ The 5-step *reasons-and-boundaries* pattern is broadly consistent with Anthropic's own published prompt-engineering guidance evolving through 2025-2026 (more delegation, less specification).

## Add to the brief

This input contributes (a) the M1 third sub-lesson on prompt-style evolution, (b) Pinterest card, (c) Tips & Techniques walkthrough, AND (d) a meta-correction that explicitly evolves Inputs 13/16/17 from "the prompt-formula layer" to "the prompt-formula layer + the reasons-and-boundaries layer." Update brief.md accordingly.
