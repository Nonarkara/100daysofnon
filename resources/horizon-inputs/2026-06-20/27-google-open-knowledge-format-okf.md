# Input 27 — Google Open Knowledge Format (OKF): "a folder of Markdown files" as the vendor-neutral knowledge standard for AI agents

**Source:** Thai-language post (#peesamac #OpenKnowledgeFormat #OKF #GoogleCloud #AIagents). Repo cited: **GoogleCloudPlatform/knowledge-catalog** on GitHub. Version: **v0.1**. Status: open-source, vendor-neutral standard.

## What OKF is (per the post's summary)

A directory of Markdown files. **One file = one concept** (e.g., one ER table, one metric like *weekly active users*, one playbook, one decision). Every file starts with **YAML frontmatter**; the only *required* field is `type`. Other fields (`title`, `description`, `tags`, `timestamp`) are optional.

**The path of the file IS its identity.** Files link to each other with normal Markdown links. The whole directory becomes a knowledge graph by emergence — no graph database required.

**No SDK. No runtime. No special tooling.** Opens in any text editor. Versions in Git. Diffs cleanly. AI agents read it directly.

## The problem OKF claims to solve

Google calls it the **"context assembly problem"** — a company's knowledge is fragmented across Notion, Google Docs, internal wikis, databases, Slack, Confluence, etc. AI agents spend more time *collecting context* than *doing work*.

OKF's argument: stop fragmenting knowledge into proprietary stores. Put it in Markdown files in a Git repo. Any AI agent — Claude, Gemini, GPT, Cursor, Codex — can read Markdown.

## The Karpathy connection

The post cites **Andrej Karpathy** (former head of AI at Tesla, OpenAI co-founder, prominent ML educator) who proposed an *LLM wiki* concept: write knowledge in a single shape that both humans and LLMs read fluently. His often-cited line: *"LLMs never get bored, never forget to update cross-references, and can edit 15 files in parallel in one round."*

OKF is the standardization of that proposal.

## Google's own implementation hook

The post notes that **Google's Knowledge Catalog now ingests OKF**, and Google ships a **reference agent** that walks BigQuery datasets and **auto-generates OKF files** describing the tables, columns, lineage, and example queries. So even existing data infrastructure can be back-fed into OKF format without manual rewriting.

## The post's honest caveat

> *"Some people joke: 'is this a standard, or just a folder?'"*

The post's own response: *"the value isn't in the format — it's in whether other vendors adopt it. Adoption is what makes a standard."*

That's a fair read. The format itself is trivial. The question is whether OpenAI, Anthropic, Cursor, etc. agree to read OKF-shaped repos as canonical context sources. If yes, OKF becomes the de-facto knowledge layer for agents. If no, it stays a Google-internal convention with adapters.

---

## The most strategically important observation in this entire input

**Non has been independently practicing OKF for months — before Google named it.**

Three places where Non's existing systems are already OKF-shaped:

### 1. The auto-memory system

`/Users/nonarkara/Library/Application Support/Claude/.../agent/memory/` is a directory of Markdown files. Each file:
- Has YAML frontmatter with a `metadata.type` field (`user`, `feedback`, `project`, `reference`)
- Has `name`, `description` (matches OKF optional fields)
- Cross-references other memories with `[[name]]` (matches OKF link convention)
- Has an index file `MEMORY.md` (matches OKF directory-listing pattern)

**The auto-memory system IS OKF in everything but name.** Should be trivial to add a `type:` field at the top level (currently nested under `metadata.type`) to be strict-OKF-compliant.

### 2. The 100daysofnon project structure

`/Users/nonarkara/Projects/100daysofnon/diary/day-XXX/` is a directory per day, with markdown files per concept (`question.md`, `answer.md`, `fact-check.md`) and an `artifacts/` subfolder. The folder *itself* is OKF-shape. Adding `type:` to each markdown file (`type: diary-question`, `type: diary-answer`, `type: fact-check`, etc.) would make it OKF-strict.

### 3. Today's input folders

`resources/horizon-inputs/2026-06-20/` and `resources/slic-inputs/2026-06-20/` and `resources/dao-inputs/2026-06-20/` — each is a directory of Markdown files (input briefs) with images. **This whole filing pattern is OKF without the label.**

**Implication:** if Non adopts OKF formally as the project's documentation format, *zero migration work is required* — just add `type:` frontmatter to existing files. The data is already in shape.

## Why this matters for Horizon

### 1. Curriculum content for M1 and M6

**M1 (orchestration mindset):** OKF is the **knowledge layer** for the *agent-as-team* metaphor. WEB_TEAM.md (Input 10) + AGENT_NOTES.md (Input 18) define the team rules and the inter-agent log. OKF defines *the shared knowledge base the team draws from.* Add as M1 lesson: ***"Where your team's knowledge lives — OKF for vendor-neutral agent-readable context."***

**M6 (multi-agent orchestration):** OKF is the **third canonical pattern** alongside Input 10's WEB_TEAM.md and Input 18's AGENT_NOTES.md. Together the three describe a complete agent-operating-discipline at the file level:
- `WEB_TEAM.md` — team rules
- `AGENT_NOTES.md` — running coordination log
- **`<okf-knowledge-base>/` — the shared knowledge graph the team draws from**

This is a Horizon-canonical trinity of file-level scaffolds. Worth a dedicated cross-cutter or a Tips & Techniques card showing the three together.

### 2. Horizon's own platform should ship OKF-native

Per Inputs 12, 17, 23: Horizon has a Pinterest library, a use-case grid, a Research papers surface. All three of these *should be OKF-formatted internally* — markdown files in a Git repo with `type: library-card`, `type: use-case`, `type: research-paper` frontmatter. This gives Horizon learners *the platform's own knowledge as a readable example* of OKF in production. **The platform teaches by being.**

This is a Horizon-distinctive move. AIS / Samsung SIC / FutureSkill all use proprietary LMS backends. Horizon being OKF-native and *publicly diffable on GitHub* would be a moat no competitor can match without redesigning their stack.

### 3. The Karpathy citation gives Horizon Research a strong opener

Horizon Research paper seed #7:

> ***"The Open Knowledge Format and the End of Context Fragmentation: Why Google Followed Karpathy, and What It Means for Thai Organizations Choosing Their Knowledge Stack in 2026"***

Anchored on the OKF spec + Karpathy's LLM-wiki essay + a case study of Non's own auto-memory system as a pre-OKF working example. **Especially useful for Thai government / SEIC / depa stakeholders deciding whether to invest in proprietary knowledge platforms vs vendor-neutral OKF-shaped repositories** — a real procurement decision happening now in the Thai public sector.

## Add to the brief

This input adds (a) OKF as third canonical M1+M6 scaffold pattern, (b) a Horizon platform-architecture recommendation (be OKF-native), (c) a Horizon Research paper seed. Update brief.md.

## Personal-workflow note (sister memory)

Also worth noting in the auto-memory system: **the agent-memory format Non and I have been building is already 95% OKF-compliant.** A small migration (move `metadata.type` to top-level `type`) would make it strict-OKF. This is the kind of low-effort high-leverage move that's worth doing the next time the memory system gets touched.

Source: post cites [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) on GitHub (v0.1, open source).
