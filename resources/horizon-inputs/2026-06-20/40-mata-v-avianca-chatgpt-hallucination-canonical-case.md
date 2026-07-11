# Input 40 — *Mata v. Avianca*: the canonical real-world ChatGPT-hallucination cautionary tale

**Source:** Long-form Thai-language narrative retelling of the **Mata v. Avianca** case. References listed: nytimes, bbc, reuters, theverge, cnn. Hashtags include `#ChatGPT #AI #ปัญญาประดิษฐ์ #ทนายความ #กฎหมาย #TechNews #GenerativeAI #อุทาหรณ์ #กรณีศึกษา`.

**Non's directive:** *"for horizon 45 project"* — explicit. The post is the most widely-cited real-world cautionary tale of AI hallucination in a professional context.

## The case (verified — this is a well-documented 2023 federal case)

- **Plaintiff:** Roberto Mata sued Avianca airlines after a metal serving cart allegedly struck his knee on a flight from El Salvador to JFK
- **Plaintiff's law firm:** Levidow, Levidow & Oberman
- **Lawyer of record:** **Steven A. Schwartz** — a New York lawyer with **30+ years of experience**
- **Court:** U.S. District Court for the Southern District of New York
- **Judge:** **Kevin Castel**

When Avianca filed a motion to dismiss, Schwartz needed to cite legal precedent. **He used ChatGPT for the research.** ChatGPT generated a brief listing six cases:
- *Varghese v. China Southern Airlines*
- *Martinez v. Delta Air Lines*
- *Shaboon v. EgyptAir*
- *Petersen v. Iran Air*
- *Miller v. United Airlines*
- *Estate of Durden v. KLM Royal Dutch Airlines*

**None of these cases existed.** Every one was a hallucination — plausible names, plausible legal language, plausible procedural detail. When Schwartz asked ChatGPT *"Is this a real case?"*, ChatGPT confidently said yes and even fabricated full citations to Westlaw / LexisNexis.

Opposing counsel and Judge Castel could not find any of the cited cases in any legal database. Schwartz was ordered to produce the original opinions. He went back to ChatGPT, which **fabricated entire fake judicial opinions** complete with judge names and reasoning.

When Schwartz submitted those, **Judge Castel sanctioned Schwartz and his colleague Peter LoDuca $5,000** (June 2023). The case became the global headline example of AI hallucination in a professional setting.

**Schwartz's defense:** he believed ChatGPT was a "super search engine" and did not understand it was a generative model that hallucinates. He had never used ChatGPT before.

## Why this is one of the most strategically loaded inputs for Horizon

This case sits at the **intersection of nearly every Horizon governing principle and module Non has been building today.** It's not just a teaching example — it's the *worst-case demonstration of what Horizon's curriculum exists to prevent.*

### Maps onto every governing principle

- **Skill Preservation (Input 26 — Nature, June 2026)** — Schwartz had 30 years of legal-research skill. He stopped applying it because the AI was confident. The case is the **legal-profession version** of the Nature study's colonoscopy-skill-degradation finding, made years before the Nature paper. *Schwartz proves it before science measured it.*
- **The Invisibility Test (Input 25 — Bland AI)** — Schwartz was IMPRESSED by ChatGPT's confident, fluent, well-cited output. **The impression itself was the failure mode.** The Invisibility Test would have caught this: *"If a customer praises your AI for being clever, automation failed."* Schwartz praised the AI; automation failed catastrophically.
- **Start Small, Share Imperfectly (Input 14)** — Schwartz didn't start small. He shipped the AI's full output as a federal court filing. *The motto's inverse: when you scale-without-testing on a high-stakes surface, you ship a public failure.*

### Maps onto every cross-cutter and methodological input

- **EGO-VOID + Ground-Truth Verification (Input 18 — Non's own multi-agent orchestration skill)** — the *don't trust agent reports, verify against real evidence* discipline is the exact thing Schwartz failed to do. **He didn't ground-truth.** Had he done what Non's skill teaches — *"verify origin = authoritative, verify the cases exist in actual legal databases"* — the entire failure would have been caught.
- **Executive Judgment in the Age of AI Defaults (Input 7 — CTC 2026 3 AI traps)** — Schwartz fell into Trap #2 inverted (*AI says yes, so trust it*) and Trap #3 (*believing AI will do everything correctly*). The case is the executive-judgment cross-cutter's most powerful case study.
- **Teach-don't-silently-fix (today's [[feedback-teach-dont-silently-fix]])** — when ChatGPT said *"yes the cases are real"*, Schwartz didn't push back, didn't ask for evidence, didn't redo the work together. He silently trusted. The principle, violated, ends in $5,000 sanction.
- **Reasons-and-boundaries prompting (Input 32 — Anthropic Fable Prompting Guide)** — if Schwartz had used the *"Demand evidence: audit each progress claim against a real result. Failed test? Show output"* discipline from Input 32, the hallucination would have surfaced at his desk, not in Judge Castel's courtroom.
- **Always MVP (today's [[feedback-always-mvp-make-it-exist-first]])** — Non's own principle is *make it work now, make it good later.* Schwartz did the inverse — *shipped without verifying it worked at all.* The case shows the failure mode of *shipping without the work-now step.* MVP includes *verifying the M part actually exists.*

### The single sentence that lands the whole case for Horizon learners

From the post's closing:

> ***"Misplaced confidence may lead to the end of a career you built your whole life."***

That sentence belongs at the top of M5 + M7 + the Executive Judgment cross-cutter. It's the negative version of Horizon's recruiting frame (Input 11: at-risk jobs; Input 14: tier ladder; Input 25: invisibility) — *the same skill that brings career flourishing in the AI era can, mishandled, end the career flourishing it was supposed to enable.*

## Four Horizon placements

### 1. M5 (Frontier ethics & data sovereignty) — the canonical case study

M5 already has the Neurable BCI input (Input 3) and the "Who's Suing Whom in AI" copyright map (Input 12). **Add the Mata v. Avianca case as the third-leg-of-the-stool case study.** The three together cover:
- Neurable = the *frontier* tech ethics (BCI, brain data)
- Who's Suing Whom = the *ecosystem* ethics (copyright, training data)
- **Mata v. Avianca = the *operator* ethics (your own use of AI in a professional context)**

The three frame the M5 ethics landscape from frontier-to-ecosystem-to-individual.

### 2. M7 (AI-enabled scam defense) — add a sister lesson on AI-confidence defense

M7 (Input 15) teaches defense against AI-enabled scams (others using AI against you). **Add a sister lesson on AI-confidence defense (yourself using AI in ways that hurt you).** Mata v. Avianca is the canonical example. Lesson: *the AI that fabricates content for a scammer is the same AI that fabricates content for you — you can be your own scammer's victim if you don't verify.*

### 3. Executive Judgment cross-cutter — the headline case-study

Add Mata v. Avianca to the Executive Judgment cross-cutter's case-study library. **It is now the highest-stakes single example in that library**, sitting alongside the CTC 2026 case studies from Input 7 (Hatari yantra fans, the 90-year-old Indonesian brand). Where CTC's cases show *judgment beating AI by overriding it*, Mata v. Avianca shows *judgment failing by NOT overriding it.* Together they bracket the principle from both sides.

### 4. Horizon Research paper #15 seed

***"Mata v. Avianca Three Years Later: What the First Famous AI-Hallucination Case Teaches a Mature 2026 Curriculum."*** Particularly useful for **Thai legal / consulting / professional-services audiences** — the case is foreign (US federal court) but the lesson is universal. The paper's argument: *the case happened in 2023 with primitive LLMs; modern 2026 models hallucinate less but still hallucinate confidently, and the verification discipline matters MORE not less because the confidence has gotten more polished.*

## A small but important caveat about the Thai post's framing

The post opens with a strong claim that AI is *"a robot without moral conscience"* and frames the lesson as *"AI doesn't have responsibility."* That's substantively correct but slightly misleading in framing — the moral failure in Mata v. Avianca was **Schwartz's**, not the AI's. ChatGPT did exactly what generative models do (generate plausible text); the human signed his name to it without verifying. **The lesson isn't "AI is bad" — it's "verification is the human's irreducible job."** Horizon's version of any paper using this case should land that nuance to avoid the post's slight anti-AI framing.

## Connection to today's other Horizon inputs

Counting the cross-references I made above, **this single input connects to at least 11 of the day's prior inputs** (3, 7, 11, 12, 14, 15, 18, 25, 26, 32, plus my own "teach don't silently fix" and "always MVP" memories). It is genuinely the case study that ties the curriculum together.

## Note on the Atlantic URL at the bottom of the post

Non's message ended with an unrelated Atlantic article URL (*"Why So Many Smart People Aren't Happy"*, April 2016). Almost certainly an unintended share from another browser tab. Not filed as part of this input. If Non wants to discuss happiness research separately, I'll spawn that as its own thread.

Sources implicit and verified well-attested:
- Mata v. Avianca court documents (S.D.N.Y., docket 1:22-cv-01461)
- New York Times coverage (May/June 2023)
- BBC, Reuters, The Verge, CNN — all named in the post
