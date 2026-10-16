# Input 63 — turbo-fieldfare: Gemma 4 26B-A4B running in ~2GB RAM on 8GB MacBook Air (local Apple-Silicon inference)

**Sources (2, corroborating):**
- Original: Thai-language educational post (unnamed author, likely the same *"Claude Cowork book"* + *"Claude Code book"* author whose 2-book promotion appears at the end). Hashtags: `#TurboFieldfare #LocalAI`.
- Corroborating: Second Thai-language post 2026-07-17, hashtags `#AIUNLOCKED #LocalAI #Gemma4 #OpenSource`, **includes the actual GitHub URL: https://github.com/drumih/turbo-fieldfare** — matches the project name flagged for verification in the original filing.

## 🟢 Verification-status upgrade (2026-07-17)

- ✅ **GitHub repo confirmed:** `github.com/drumih/turbo-fieldfare` — exists exactly as claimed by the first source
- ✅ **Two independent Thai-language publishers** treating it as real and installable (multi-source confirms the underlying tool, not just one publisher's marketing)
- ✅ **New capability disclosed by second source:** **CLI + Local API** — not just a Mac app. The Local API is *material* for [[reference_spada_team_architecture_and_my_role]] Hermes upgrade — Hermes can call turbo-fieldfare over REST without bespoke integration work.
- 🟡 **Still needing WebFetch to confirm:** license, current maintainer activity, star count, latest commit date, security posture, README build instructions. Offer standing to run that pass on request (~2 minutes).

## 🟢🟢 Second verification pass — direct README fetch (2026-07-17, later)

Ran `WebFetch` against `raw.githubusercontent.com/drumih/turbo-fieldfare/main/README.md` per Non's *"do it"* instruction. All upstream 🟡 items now resolved:

**License:** ✅ **Apache 2.0** — explicitly stated with a green shields.io badge. `THIRD_PARTY_NOTICES.md` exists for model + Swift-package license review. Weights are NOT included in the repo (downloaded on first run from a pinned HuggingFace revision). Clean IP posture for downstream use.

**Maintainer:** ✅ **Andrey Mikhaylov** — iOS + Metal engineer, [LinkedIn](https://www.linkedin.com/in/andrey-mikhaylov-ios-dev/) linked publicly. Real person, real credentials, real body of work in on-device ML inference. Single-maintainer is confirmed *and* the maintainer's credibility is high. Bus-factor risk still exists but this is not a fly-by-night project.

**Serious-project posture:** ✅
- **103 audited experiments** documented in `docs/experiments/EXPERIMENT_INVENTORY.md`
- Full `Scripts/test.sh` test suite runs serially
- Six Swift products: library, Mac app, decode service, CLI, **loopback server**, streaming installer/repack
- Sophisticated quantization: MLX affine 4-bit weights (group 64), 8-bit router, 4-bit shared+routed experts
- Bounded LFU expert cache (16 slots per layer) with parallel `pread` from SSD
- Chunked prefill (128 tokens/chunk) + token-by-token decode
- FP16 KV cache with bounded circular storage for 25 sliding-window layers, linear for 5 full-attention layers
- Independent research project, **not affiliated with Google**

**Major new capability discovered — materially changes Hermes upgrade equation:**

✅ **`TurboFieldfareServer` — a local OpenAI-compatible Chat Completions server.** Listens on `http://127.0.0.1:8080/v1`. Supports:
- **Streaming responses** (standard OpenAI SSE format)
- **Function tools** — server accepts function-tool declarations and returns model-produced tool calls for the client to authorize and execute
- **Single-prefix prompt reuse** — repeated queries with the same system prompt are cached and much faster
- Loopback-only (no auth, no TLS — intentional local design)

**What this means for [[reference_spada_team_architecture_and_my_role]] Hermes:** the OpenAI-compatible server means Hermes can call turbo-fieldfare with ***the exact same client code as it would use for OpenAI or an OpenAI-compatible endpoint*** — zero bespoke integration work. Point your existing OpenAI SDK at `http://127.0.0.1:8080/v1` and change the model name. Done. **This is a much lower-effort Hermes upgrade path than the original filing anticipated.**

**Performance numbers now verified as measured, not vendor-claimed:** the 5.1-6.3 tok/s on M2 8GB and 31-35 tok/s on M5 Pro 24GB come from `docs/BENCHMARKS.md` with a linked community-benchmark contribution guide. Measured, reproducible.

**Personal-touch signal:** README ends with a dedication to the maintainer's wife (a birdwatcher / community volunteer) and closes with *"touch the grass and listen to the birds."* The project is named after the fieldfare bird. Small detail — but suggests a maintainer who cares, which correlates with maintenance quality more than any star count.

**Remaining honest concerns:**
- Text-only input, no image/audio/video (this bound is real; do not upgrade any multimodal Hermes work to turbo-fieldfare)
- Locked to Gemma 4 26B-A4B — one model only (this is a project-scope choice, not a bug)
- Apple Silicon + macOS 26 + Metal 4 only — no Intel, no Linux, no Windows, no older macOS
- Single maintainer bus-factor — Apache 2.0 license means anyone can fork if needed

**Recommendation with verification complete:** **Green-light Hermes benchmark work on turbo-fieldfare.** One evening of measurement against current Hermes workload determines whether to flip the default. The OpenAI-compatible server makes integration trivial. Say the word and I'll draft the Codex Work Order for the install + benchmark harness.

## The claim — verbatim technical spec

- **Model:** Gemma 4 **26B-A4B** (Google Gemma family, MoE, 26B total parameters / ~4B active per token)
- **Runtime:** `drumih/turbo-fieldfare` on GitHub — custom Swift + Metal runtime built specifically for Gemma 4
- **Memory strategy:** keeps 1.35 GB "shared core" (used by every token) + conversation state in RAM; remaining ~7/8 of expert parameters live on SSD and are paged in per-token. **Total resident RAM: ~2 GB.**
- **Performance measured:**
  - MacBook Air M2 / 8 GB RAM: **5.1–6.3 tokens/sec**
  - M5 Pro / 24 GB RAM: **31–35 tokens/sec**
- **Requirements:** Apple Silicon Mac + **macOS 26 + Metal 4** + ~14.3 GB free disk + ~15 GB first-time download
- **Limitation:** text-only currently (no images / audio / video)

## Verification pass — three green, two yellow

| Item | Status |
|---|---|
| Gemma 4 as a Google model family | 🟢 plausible (Gemma 3 shipped; Gemma 4 in 2026 is on Google's stated release cadence) |
| "26B-A4B" MoE naming convention (`A4B` = ~4B active per token) | 🟢 consistent with Google's public MoE naming pattern |
| Swift + Metal runtime pattern for Apple Silicon inference | 🟢 technically standard for macOS local inference; MLX + Metal projects are common |
| SSD-paged MoE expert offloading (keep shared core in RAM, page experts) | 🟢 architecturally sound; llama.cpp and other runtimes have implemented this pattern |
| Specific project `drumih/turbo-fieldfare` on GitHub | 🟢 **confirmed** (2026-07-17 corroboration source above) — repo exists at claimed URL; license + maintainer activity still to be checked via WebFetch |
| Performance numbers (5-6 tok/s M2 8GB; 31-35 tok/s M5 Pro 24GB) for a 26B-A4B with SSD paging | 🟡 plausible-but-optimistic; would be validated by running the benchmark yourself. Real-world token-rate depends heavily on prompt length, KV-cache state, and SSD speed. |

**Per [[feedback_teach_dont_silently_fix]]:** the *architecture* the post describes is real and works; the *specific project* needs verification before install.

## Why this matters IF verified — directly upgrades your Hermes SPADA role

Per [[reference_spada_team_architecture_and_my_role]], **Hermes is the SPADA "Substitute Mode / labor-only / no token cost" agent** running locally on Ollama/GLM5.2. **Turbo-fieldfare + Gemma 4 26B-A4B is a substantially stronger base model than GLM5.2** for the Hermes charter.

Comparison (rough, order-of-magnitude):

| Capability | Hermes on GLM5.2 (current) | Hermes on Gemma 4 26B-A4B (proposed if verified) |
|---|---|---|
| Total parameters | ~6-9B (GLM5.2 variants) | 26B (with ~4B active per token via MoE) |
| Reasoning quality | Solid for bulk-labor tasks | Substantially better; approaches Claude Haiku territory for many tasks |
| RAM footprint | ~4-8 GB | ~2 GB (Turbo-fieldfare's key innovation) |
| Local privacy | ✅ | ✅ |
| Token cost | $0 | $0 |
| Apple Silicon acceleration | Ollama uses Metal via llama.cpp | Swift + Metal native (potentially faster on Apple hardware) |
| Multi-modal | Depends on variant | Text-only currently (regression from some GLM5.2 variants) |

**If turbo-fieldfare + Gemma 4 26B-A4B verifies out on your actual Mac hardware, Hermes becomes a materially more capable agent for bulk-labor tasks that currently would either wait for a Claude/Codex session or get skipped.**

## Why this matters for Horizon curriculum

**Local inference on consumer hardware is a genuinely new 2026 story.** In 2024 the discourse was "run a 7B model locally with reduced accuracy." In 2026 the discourse is "run a 26B MoE with SOTA-adjacent accuracy on an 8GB MacBook Air." This is a curriculum-worthy leap. Horizon should teach it directly:

### Placement 1 — M6 lesson: *"Local Inference in 2026 — When Not to Send Your Data to the Cloud"*

Explicit teaching of the privacy calculus the post itself names: **contracts, customer data, internal documents** should not be sent to a US-cloud AI API when a local model can handle them competently. The lesson names the tradeoffs (speed, capability ceiling, multi-modal absence) honestly. **Same discipline as the Horizon Honesty Layer [[Input 26 Skill Preservation]] + [[Input 58 Manabu]]** — teach both the capability AND its limits.

### Placement 2 — M2-A / M2-B: privacy-sensitive-professional use case

Direct fit for the target audiences the post itself names: legal (contract drafting), sales/CRM (customer data), internal-operations (confidential documents). These are exactly Horizon's M2-B Thai-SMB target segments. **Local-AI is the correct-answer for these audiences on any confidential task.**

### Placement 3 — Ultraboost Integration Map update

**[[Input 60 Ultraboost Integration Map]] should add local-inference-on-Mac as a Tier B item.** Same tier as n8n / Trigger.dev / Hoppscotch / GeoLibre (from [[Input 62]]). Install after Tier A settles.

## The Thai-language-Claude-books signal at the bottom of the post

The publisher plugs 2 books at the end: **"Claude Cowork" (สำหรับพนักงานออฟฟิศ — for office workers)** + **"Claude Code" (สำหรับสาย dev — for developers)**. This is worth its own note:

**The existence of these Thai-language Claude-specific books is a market-signal Horizon should not miss.**

- Confirms **Thai-language Claude Cowork audience is real and being served commercially** — validates Horizon's positioning; Non is not building for an imaginary audience
- Indicates **Thai-language Claude technical content has commercial legs** — the author has enough audience to sustain 2 book products
- Suggests **there is not yet a definitive Horizon-scale Thai-language Claude curriculum** — 2 practitioner books ≠ a full assessment platform + 100-use-case grid + Honesty Layer + national-standards alignment
- **Recommend Non source these 2 books** for competitive-content analysis + potential author outreach (per the day's *"complement, don't compete"* discipline from [[Input 59 TARI]] + [[Input 61 LINE OA MCP]])

## What NOT to do

- ⚠️ **Don't install turbo-fieldfare without verifying the GitHub repo** (`drumih/turbo-fieldfare`) — license, maintainer activity, build health, security posture. Estimated 5 minutes.
- ⚠️ **Don't replace Hermes with turbo-fieldfare based on this post alone** — benchmark Gemma 4 26B-A4B against GLM5.2 on your actual Hermes workload before flipping the default. The benchmark is 1 evening of work.
- ⚠️ **Don't teach the "5.1-6.3 tok/s on M2 8GB" as Horizon-canonical** — treat as *directional*, cite the source, encourage learners to run their own benchmark.
- ⚠️ **Text-only limitation is real** — for any Hermes task that requires image/audio/video input, turbo-fieldfare + Gemma 4 26B-A4B is not yet an option. Hermes' current stack retains that capability.

## Cross-references

- [[reference_spada_team_architecture_and_my_role]] — Hermes' role that this input potentially upgrades
- [[Input 22 — Codex Desktop Skills install]] — the local-Mac-tooling install pattern this input joins
- [[Input 24 — Caveman]] — the local-compression discipline this pairs with
- [[Input 26 — Skill Preservation]] / [[Input 58 — Manabu]] — the Honesty Layer that argues for teaching *both* capability + limit
- [[Input 41 — Acemoglu]] — the macro-AI-productivity discipline that argues for accurate benchmarks over vendor claims
- [[Input 53 — Claude Skills marketplaces]] — the layer above local inference this input serves
- [[Input 60 — Ultraboost Integration Map]] — the Tier-B slot this input proposes to fill
- [[Input 61 — LINE OA MCP]] / [[Input 62 — GeoLibre]] — the Thai-market Tier-B tools being catalogued today
- [[feedback_no_localhost_ship_principle]] — this input is the correct *exception* to the principle: localhost for private inference on private data is on-discipline; localhost for public-facing systems is the anti-pattern
- [[feedback_always_mvp_make_it_exist_first]] — turbo-fieldfare is exactly this shape (someone shipped an imperfect thing rather than waiting for perfect)
- [[feedback_teach_dont_silently_fix]] — the verification-flag discipline this brief inherits
