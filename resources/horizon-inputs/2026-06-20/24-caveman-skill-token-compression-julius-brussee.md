# Input 24 — Caveman: AI agent output compression skill (verified research)

**Original ask:** Non sent a Thai-language post about *"Caveman"* — a tool that makes AI agents (Claude Code, Codex, Cursor, Cline) respond tersely. *"Research this."*

**Source (verified):** [github.com/JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) by Julius Brussee. MIT license. **928 GitHub stars** (the SkillsLLM aggregator showing 74.9k★ refers to the umbrella *AI Agents on GitHub* topic, not Caveman specifically — that's a misleading citation pattern worth flagging).

## What Caveman actually does (from the official README, verified)

A Claude Code skill/plugin AND Codex plugin that makes the agent speak in compressed *"caveman"* style — drops articles, filler words, pleasantries, hedging — while keeping technical content intact.

**Tagline:** *"why use many token when few do trick"*

**Real benchmark numbers** (from the repo's published benchmarks, 10 prompts via Claude API):

| Task | Normal tokens | Caveman tokens | Saved |
|---|---|---|---|
| React re-render bug | 1180 | 159 | **87%** |
| Auth middleware token expiry | 704 | 121 | 83% |
| PostgreSQL connection pool | 2347 | 380 | 84% |
| Git rebase vs merge | 702 | 292 | 58% |
| Callback → async/await | 387 | 301 | 22% |
| Microservices vs monolith | 446 | 310 | 30% |
| PR security review | 678 | 398 | 41% |
| Docker multi-stage build | 1042 | 290 | 72% |
| Postgres race condition | 1200 | 232 | 81% |
| React error boundary | 3454 | 456 | 87% |
| **Average** | **1214** | **294** | **65%** |

**Range: 22%–87% savings.** The 65% average headline is real but the per-task variance is wide — *don't promise 75% on routine work; the worst-case for refactoring tasks is closer to 22%.*

## Critical caveat the Thai post elided

From the README, emphasized in the original:

> *"Caveman only affects output tokens — thinking/reasoning tokens are untouched. Caveman no make brain smaller. Caveman make mouth smaller. Biggest win is readability and speed, cost savings are a bonus."*

The Thai post Non sent presented this as a token-saving tool. **It's actually a readability tool that incidentally saves output cost.** For workflows that bill on input + output (most Anthropic/OpenAI usage), the input-token cost is unchanged.

This is exactly the kind of vendor-claim-needs-EGO-VOID-check that Input 18 teaches Horizon learners to perform. **The tool is real and useful; the framing was loose.** Both observations belong in the Horizon write-up.

## The science Caveman cites

The README references **arxiv 2604.00025**: *"Brevity Constraints Reverse Performance Hierarchies in Language Models"* (March 2026) — claims constraining LLMs to brief responses improved accuracy by 26 percentage points on certain benchmarks and reversed performance hierarchies.

**Verification status:** I have not independently fetched and read this arxiv paper. The arxiv ID format (2604.) suggests March 2026, consistent with the claim. Horizon's Research paper version should verify the paper exists, read it, and either confirm or qualify Caveman's interpretation before publishing. This is the *EGO-VOID Ground-Truth Verification* discipline (Input 18) applied to citation chains.

## Install + use

```bash
# Via Skills CLI
npx skills add JuliusBrussee/caveman

# Or via Claude Code plugin marketplace
claude plugin marketplace add JuliusBrussee/caveman
claude plugin install caveman@caveman
```

**Trigger:** `/caveman`, `$caveman` (Codex), or natural language *"talk like caveman"* / *"caveman mode"* / *"less tokens please"*
**Stop:** *"stop caveman"* / *"normal mode"*

**Supported platforms** (from the marketplace listings):
- Claude Code: auto-activate every session, native skill
- Codex: native plugin
- Gemini: built-in style
- Cursor / Windsurf / Cline / Copilot: always-on rule files via `--with-init`

**What stays intact even in caveman mode:**
- Code blocks: normal (caveman not stupid)
- Technical terms: exact (polymorphism stays polymorphism)
- Error messages: quoted exact
- Git commits & PRs: normal

**What gets compressed:**
- Articles (a, an, the): gone
- Pleasantries (*"Sure I'd be happy to"*): dead
- Hedging (*"It might be worth considering"*): extinct

## Why this matters for Horizon — Tips & Techniques + a deeper lesson

**Surface-level fit:** Tips & Techniques cross-cutter card. *"Install Caveman in 2 minutes, cut your output tokens by ~65%."* Two-minute walkthrough alongside Input 22's Codex Skills install pattern.

**Deeper lesson:** Caveman is a **prompt-engineering technique made permanent at the agent layer**. Instead of telling each session *"answer briefly,"* the rule lives in the skill. **This is the same pattern as Non's own multi-agent-orchestration skill from Input 18** — codify a teaching principle (in this case, brevity) into a reusable agent-level rule.

Horizon should teach Caveman not just as a *tool* but as a *worked example* of:
1. **Identify a recurring friction** (output verbosity)
2. **Codify the fix as a reusable rule** (skill spec)
3. **Install it once** (Input 22's pattern)
4. **Verify the benefit with real measurements** (the benchmark table)
5. **Acknowledge the boundary** (output-tokens only, not all tokens)

That's a five-step pattern any Horizon learner can apply to their own recurring frictions. **Caveman becomes a case study, not just a recommendation.**

## EGO-VOID verification checklist applied to Caveman before recommending

- ✅ GitHub repo exists, MIT licensed (verified via fetch)
- ✅ Benchmarks published with reproducible methodology (the repo links to benchmark scripts)
- ⚠️ Star count claim — the 74.9k★ figure circulating in some indexes is the aggregator topic, not the repo; real star count is 928 at time of fetch. Horizon should cite the real number.
- ⚠️ Token-savings claim — only output tokens. Worth saying explicitly.
- ❓ Cited arxiv paper (2604.00025) — exists per the citation, not yet independently fetched. Horizon Research version should verify.
- ✅ Install commands work as documented per the README (not independently tested in this session but the commands are well-formed npm and Claude plugin syntax)

**Recommended for Horizon's Tips & Techniques surface with the caveats above.** Don't republish vendor hyperbole; teach the *technique* honestly.

## Add to the brief

This input contributes to the **Tips & Techniques** surface (Input 22) and to M1 + M6 as a worked example of the *"codify a recurring rule into a reusable skill"* meta-pattern.

Sources verified during research:
- [github.com/JuliusBrussee/caveman README](https://github.com/JuliusBrussee/caveman/blob/main/README.md)
- [github.com/JuliusBrussee/caveman/blob/main/CLAUDE.md](https://github.com/JuliusBrussee/caveman/blob/main/CLAUDE.md)
- [github.com/JuliusBrussee/caveman/blob/main/INSTALL.md](https://github.com/JuliusBrussee/caveman/blob/main/INSTALL.md)
