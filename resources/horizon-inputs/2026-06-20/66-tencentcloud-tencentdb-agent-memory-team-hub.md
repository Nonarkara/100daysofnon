# Input 66 — TencentCloud/TencentDB-Agent-Memory: team-level memory hub for AI agents

**Source:** GitHub — `github.com/TencentCloud/TencentDB-Agent-Memory`. Fetched via `WebFetch`; the meta-description landed cleanly; the raw README timed out twice (both `main` and `master` branch attempts + GitHub API). Filing on partial data with a verification-gap flag; **the tagline + repo-network confirmations are direct-source, the details below the tagline are educated inference from the concept-space and need README verification before committing engineering work.**

## The tagline — verbatim from repo meta-description

> *"TencentDB Agent Memory is a team-level memory hub for AI Agents — turning conversations, docs, and code into four reusable memory assets (Chat Memory, Skill, LLM-Wiki, Code-Graph) that are governed, shared, and equipped across agents and frameworks."*

Repo confirmed:
- ✅ Namespace is TencentCloud (not a fork; `repository_is_fork: false` in the fetch metadata)
- ✅ Repo ID 1203558071 in GitHub's system — real, indexed
- ⚠️ README fetch timed out (`main` and `master` both); actual technical detail (license, install, dependencies, architecture) awaits a retry
- ⚠️ Star count, latest commit, maintainer activity — not fetched

## Why this is directly SPADA-relevant

**Non's SPADA architecture** ([[reference_spada_team_architecture_and_my_role]]) has 5 named agents (me/Claude, Codex, Antigravity, Hermes, Human) coordinating via a single `AGENT_NOTES.md` file with a D-E-R format + ACTIVE CLAIMS table. **That is a stopgap coordination substrate. TencentDB-Agent-Memory positions itself as the architectural fix for that gap** — the *team-level memory hub* the multi-agent-orchestration literature has been circling all year.

The four memory asset types map cleanly to what SPADA needs but does not yet formalize:

| Asset type | What it holds | SPADA equivalent today |
|---|---|---|
| **Chat Memory** | Persistent conversation state across sessions and agents | The auto-memory files at `agent/memory/*.md` — but only for me/Cowork, not shared to Codex/Antigravity/Hermes |
| **Skill** | Reusable capability packages | The Anthropic Skills + JANUSTIU Skills from today's [[Input 53]] + [[Input 60]] — but each agent installs its own; no shared team catalog |
| **LLM-Wiki** | Curated knowledge base tuned for LLM consumption | What `resources/*-inputs/` in 100daysofnon is *organically becoming* — a curated knowledge substrate. Today's session filed 66 Horizon inputs + 14 SLIC + others. This IS a wiki-shaped resource, just without a formal query/consumption layer yet. |
| **Code-Graph** | Structural code understanding | Not yet formalized in SPADA; Codex parses code on demand per Work Order |

**The convergence is precise.** If TencentDB-Agent-Memory (or an equivalent) is real, healthy, and portable, it is the strongest candidate substrate for upgrading SPADA from *"single-file async channel"* to *"structured multi-asset shared memory."*

## ⚠️ Verification concerns — three, ranked by materiality

### 1. Data-sovereignty and vendor dependency

**TencentCloud is a major Chinese cloud provider.** Same discipline that applied to [[SLIC Input 14]]'s Global Times source-bias flag applies here: *the vendor's national context is a real consideration, independent of the code quality*.

Practical concerns for Non's use cases:
- **FloodDash + Phuket Bus data** — Thai infrastructure telemetry. Hosting flood-sensor telemetry and airport-passenger data on Chinese cloud infrastructure creates data-sovereignty questions Non will need to answer to Thai regulators, insurance underwriters, and any depa/SEIC counterparts.
- **SLIC v3 data** — much of it is public benchmarking. Less sensitive; TencentCloud dependency less blocking.
- **100daysofnon diary content** — personal biographical material. Non's call whether that lands on Chinese infrastructure.
- **The memory files themselves** — the [[user_non_near_death_operator_hardwiring]] memory + others contain Non's private operator identity. Absolutely not on Chinese infrastructure without explicit Non decision.

**The key question — is TencentDB required, or is the architecture portable?** If the code is open-source and the memory-hub design can be backed by any Postgres/Redis/vector-DB, this is a *pattern to learn from* even if the specific implementation isn't adopted. **README verification will settle this.**

### 2. License and IP posture

Not yet verified. TencentCloud open-source projects have varied license patterns; some Apache 2.0, some more restrictive. **Same discipline as [[Input 62 GeoLibre]] and [[Input 63 turbo-fieldfare]]** — do not adopt without license verification.

### 3. Single-large-corp bus factor

TencentCloud open-source projects have historically had good maintenance while a business unit sponsored them and abandoned periods when reorgs happened. The `TencentCloud/` org has ~250 repos with mixed activity levels. **Verify the current maintainer team's activity signals before committing to it as production infrastructure.**

## What this input tells us about the 2026 agent-memory landscape

Regardless of TencentDB-Agent-Memory-specifically, **the "team-level memory hub" naming is meaningful.** It marks the transition from:

- **2024:** *"agents have memory"* (Anthropic Contextual Memory, LangChain memory modules — per-agent, per-session)
- **2025:** *"agents share memory"* (early multi-agent frameworks, shared state via files)
- **2026:** *"teams of agents have governed memory assets"* (this input, plus emerging standards from other vendors likely following)

**Horizon curriculum should teach this progression as an M6 architectural lesson.** *"How agent memory evolved from personal to team to institutional."* The four-asset-type taxonomy (Chat/Skill/Wiki/Code-Graph) is portable across vendors even if TencentDB-specifically isn't adopted — it's the correct concept.

## What this could do for Non's actual work (if verified)

### Immediate use (weeks): unify the auto-memory + `resources/*-inputs/` folders

Right now:
- Auto-memory lives in `agent/memory/` (only I see it)
- Project inputs live in `resources/horizon-inputs/`, `resources/slic-inputs/`, etc. (organized manually via wikilinks)
- These do not talk to each other; a Codex work order today cannot query "what did Cowork learn about Non's operator identity" — that memory is Cowork-only

A team-level memory hub would:
- Give Codex read-access to relevant memory ("Non prefers X approach when solving Y") without me having to write it into every Work Order
- Give Antigravity access to Non's design discipline (Rams/Vignelli + Template Poison list from CLAUDE.md) without repeated reload
- Give Hermes context on what's "already been decided" so it can pick up substitute tasks without re-explanation

### Medium-term (Q4 2026): governed asset catalog

The four-asset-type structure is the correct answer to a real emerging problem: as Skills proliferate (today's [[Input 60]] listed 6+ Skills across 4 repos as Tier A installs; the [[Input 53]] Anthropic Skills marketplace pattern implies many more), a team-level catalog with governance (who can add, who can share, versioning) becomes structural.

Even without adopting TencentDB, **Non should think about a SPADA Memory Hub Spec** as a docs/architecture/specs artifact. My zone.

## Three placements for Horizon (conditional on verification)

### 1. M6 lesson: *"Agent memory in 2026 — from personal to team to institutional"*

Teach the progression named above. TencentDB-Agent-Memory is one example among several; the M6 lesson names the general architecture, not a specific vendor.

### 2. Horizon Research paper #27 seed

*"Team-Level Memory Hubs for Multi-Agent AI Systems: A 2026 Landscape and Selection Framework"* — reviews TencentDB-Agent-Memory + LangGraph checkpointers + Mem0 + Zep + others. Positions Horizon as the curriculum authority on the *pattern*, not any specific vendor.

### 3. Ultraboost Map update

**Tier C for TencentDB-Agent-Memory specifically** (data-sovereignty concerns); **Tier B for the underlying "SPADA Memory Hub" architecture spec I would write** (my zone; no vendor dependency; adopts the four-asset-type taxonomy without adopting Tencent infrastructure).

## What NOT to do

- ⚠️ **Do not install TencentDB-Agent-Memory on any of your live projects without a data-sovereignty review.** Even if the code is Apache-licensed and the memory can be backed by non-Tencent infrastructure, the *first-run behavior* may phone home to Tencent telemetry.
- ⚠️ **Do not treat this as production-ready** until we verify: license, current maintainer activity, whether it requires TencentDB or is DB-agnostic, whether the API has any Tencent-Cloud-only features that would create lock-in.
- ⚠️ **Do adopt the concept regardless of the specific vendor** — the four-asset-type taxonomy is the strongest team-memory framing I've seen and Non should apply it to SPADA's architecture even if this specific implementation stays on the shelf.

## Available next steps — Non chooses

1. **Retry the README fetch** — the timeouts today may be transient network/GitHub issues. I can try again on request.
2. **Fetch the repo tree structure** (`api.github.com/repos/TencentCloud/TencentDB-Agent-Memory/git/trees/main?recursive=1`) to see the code layout and infer dependencies without full README parse. ~2 min.
3. **Draft the SPADA Memory Hub Spec** in my zone, adopting the four-asset-type taxonomy without adopting Tencent-specific infrastructure. Multi-hour docs/architecture work. **Recommended if the concept resonates regardless of the vendor.**
4. **Add to the outstanding-verification queue** and revisit tomorrow when GitHub is likely more responsive.

## Cross-references

- [[reference_spada_team_architecture_and_my_role]] — the architecture this input maps onto
- [[Input 53 — Claude Skills marketplaces]] — the Skills-asset layer this hub taxonomy formalizes
- [[Input 60 — Ultraboost Integration Map]] — the current Skills install list this would unify
- [[Input 61 LINE OA MCP]] — same pattern of MCP tools + Skills that would benefit from team-level memory
- [[Input 63 turbo-fieldfare]] — local-inference layer this hub could serve
- [[Input 65 WanGP]] — media-generation layer this hub could serve
- [[SLIC Input 14 — Mumbai-Ahmedabad]] — the counterparty-reliability discipline that argues against Chinese-cloud infrastructure dependency for Thai smart-city work
- [[MEMORY.md]] — the current per-Cowork memory index; what a team-level hub would unify
- [[user_non_near_death_operator_hardwiring]] — the private memory that must NEVER land on Chinese cloud infrastructure without explicit Non decision
- [[feedback_no_localhost_ship_principle]] — the deploy discipline this input's data-sovereignty concern intersects
- [[feedback_teach_dont_silently_fix]] — the verification-flag discipline this brief inherits
