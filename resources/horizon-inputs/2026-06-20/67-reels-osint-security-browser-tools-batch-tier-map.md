# Input 67 — Reels tool-discovery batch (11 items): OSINT / security / browser-native tools + Thai-legal Honesty Layer

**Source:** Non 2026-07-17, batch of 11 Reels/TikTok screenshots without commentary, drawn from four creators: **AriaCodez**, **Carter Perez**, **Cali Tech**, **Piyushikaamriti**. All in the *"look at these cool obscure websites / tools"* engagement-content genre.

## Filed as one brief, not 11 — same discipline as [[Input 60 Ultraboost Integration Map]]

Non has been sending steady tool-discovery drops all day. Filing each of the 11 items as its own Input NN would repeat the noise pattern [[Input 60]] warned against. Value is in *integrated tier classification*, not exhaustive catalog. Individual items are preserved in `/uploads/`.

## The 11 items — one-line each, verified from screenshot content

| # | Item | Verification |
|---|---|---|
| 1 | **Awesome-OSINT-List** (`github.com/Astrosp/Awesome-OSINT-List`, 1.5K stars, 21 open PRs) | 🟢 real, active, well-maintained OSINT-tools catalog |
| 2 | **CYBERTHREAT LIVE MAP** — Kaspersky-style animated globe cyberthreat visualization | 🟢 real Kaspersky product (`cybermap.kaspersky.com`) |
| 3 | **GrayhatWarfare** — open-S3-bucket search *("cause white is boring")* | 🟢 real, legitimate security-research + real misuse-adjacent tool |
| 4 | **deflock.org** + **quad9.net** + `github.com/m1k1o/neko` | 🟢 all real: anti-Flock-Safety civic-tech mapping · non-profit secure DNS · self-hosted virtual browser |
| 5 | **hackingtool — Claude Code plugin** by AriaCodez, wrapping `Z4nzu/hackingtool` (MIT license) | 🟢 real; 183 pentesting + OSINT tools behind a single Claude Code plugin |
| 6 | **React Bits** (`reactbits.dev`) — animated React UI components | 🟢 real, well-known React component library |
| 7 | **IKEA room planner** (`ikea.com/us/en/planners/`) — 3D room design in browser | 🟢 real IKEA product, no install needed |
| 8 | **Kosmi.io** — free watch-party + virtual living-room | 🟢 real, well-known synchronous-video-watching service |
| 9 | **dos.zone** — DOS games in browser | 🟢 real, legitimate DOS-game preservation via emscripten emulator |
| 10 | **Location-guesser tool** ("Search Location" — Global/City, Instant/Low/Medium/High effort tiers, image upload) — likely **GeoSpy** or a peer product | 🟡 real class of tool (AI-powered image geolocation); specific brand not identified from screenshot |
| 11 | **romspure.cc** — ROM piracy site (Sony PSP / PS3 / PS4 / SNK Neo Geo AES / SNES etc.) | 🔴 **piracy — hard skip** (see Tier D below) |

## Tier classification — same shape as [[Input 60]]

### Tier A — install / adopt for Horizon curriculum

**None from this batch.** These are content items, not tools Non installs on his stack.

### Tier B — legitimately curriculum-worthy for Horizon, with Honesty-Layer discipline

**B1. Awesome-OSINT-List** — canonical Thai-language OSINT-tools reference layer for Horizon M2-B (journalism, market-research, due-diligence, corporate-investigations segments). Cite the *pattern* (curated GitHub OSINT list) even if Horizon builds a Thai-language version.

**B2. Kaspersky Cyberthreat Live Map** — teaching visualization for M1 "why cybersecurity matters" lesson. Real-time global cyber-attack visualization is dramatically more effective at conveying threat scale than statistics.

**B3. GrayhatWarfare** — for the *M6 defensive-cybersecurity* segment. Teaches learners about *what a bad actor can find* to inform *how you should audit your own S3 buckets*. Frame defensively, not offensively.

**B4. Quad9 (`quad9.net`)** — secure DNS resolver, non-profit operated. Real Horizon M2-B recommendation for privacy-minded Thai SMBs. Legitimate anti-malware + anti-phishing benefit at zero cost, no install for most users.

**B5. Awesome-OSINT + Kaspersky + Quad9 — Horizon Research paper #28 seed:** *"OSINT and defensive-cybersecurity fundamentals for Thai knowledge workers."* Direct depa/SEIC/MoHE audience fit.

### Tier C — real value, wrong moment or narrow fit

**C1. React Bits (`reactbits.dev`)** — Antigravity's zone; already in the frontend ecosystem she serves; nice pattern-library but not urgent for Horizon curriculum.

**C2. IKEA room planner** — cute; potentially useful for one Horizon M2-A "browser-native design tools" card; low priority.

**C3. dos.zone** — cultural preservation; fun; not curriculum-relevant.

**C4. `m1k1o/neko`** — self-hosted virtual browser; interesting for isolated-browsing security use cases but overlaps with mainstream sandboxed-browsing solutions.

**C5. Kosmi.io** — collaboration/synchronous-viewing product; not immediately Horizon-relevant.

**C6. deflock.org** — legitimate civic-tech; US-specific (Flock Safety is a US product); Thailand doesn't have the same Flock Safety deployment; low direct fit.

### Tier D — hard skip

**D1. romspure.cc — piracy — DO NOT ADOPT / DO NOT LINK / DO NOT MENTION IN HORIZON CURRICULUM.**

Thai law: Copyright Act B.E. 2537 (as amended) makes ROM downloading and distribution copyright infringement. Sony/Sega/Nintendo etc. actively pursue infringement in Thailand. Any Horizon material that surfaces romspure.cc even critically would expose Horizon to takedown notices and reputational risk. Same discipline as [[Input 60]] Tier D (ALLGPT/Emailnator).

**D2. The AI-location-guesser tool (#10) — Tier D CONDITIONALLY.**

- Legitimate uses: journalism, missing-persons investigation, disaster-response geolocation, satellite/aerial context for photojournalism
- Illegitimate uses: stalking, doxing, non-consensual location identification of private individuals from social-media photos

**Thai-legal bounds Horizon must name if this tool is taught:** PDPA (Personal Data Protection Act 2019) — geolocation data derived from a person's image without consent is PDPA-scoped. Computer Crime Act B.E. 2560 provisions on unauthorized access to identifying information. **If Horizon teaches this tool at all, it must be paired with the same discipline named for WanGP in [[Input 65]]: first-class ethical bounds, not footnotes.** Recommended: skip in curriculum; if a specific defensive-cybersecurity lesson genuinely needs it, teach only within an authorized-pentesting frame with explicit Thai-legal citations.

**D3. The hackingtool Claude Code plugin — Tier D CONDITIONALLY.**

- Legitimate uses: authorized penetration testing, red-team engagements with signed scope agreements, capture-the-flag security education
- Illegitimate uses: unauthorized network intrusion, unauthorized vulnerability exploitation

**Thai-legal bounds:** Computer Crime Act B.E. 2560 sections 5-11 criminalize unauthorized access, interception, and modification of computer data. Possession of hacking tools is not itself illegal in Thailand (unlike some jurisdictions) but *use* against systems without written authorization is. **The plugin's convenience (183 tools behind a single Claude Code command) also lowers the bar for accidental or reckless deployment.**

**Recommendation:** do not adopt into any of your live projects; do not add to [[Input 60]] Ultraboost Map; if Horizon teaches OSINT/security at all, teach the *concept* + link to *educational resources at TryHackMe / HackTheBox / OffSec* which have proper authorized-lab frameworks. Do not funnel Horizon learners to `hackingtool` where authorization is on the learner.

## The engagement-creator ecosystem pattern to name

**AriaCodez / Carter Perez / Cali Tech / Piyushikaamriti** are the English-language equivalents of the Thai-language *"You don't know these websites"* engagement genre (same pattern as MoneyTrendz.ai from [[Input 60]]). Their content-marketing shape:

- Rapid-fire tool-showcase in ~30-second vertical video
- Deliberately-obscure or slightly-taboo tools amplify "insider knowledge" positioning
- Some meme/shock text overlays (visible in browser tab bars) for engagement
- Real signal exists inside; noise ratio is high; some items are hard-skip

**Horizon curriculum should not derive Thai learner recommendations from this genre's picks uncritically.** The genre optimizes for saves/shares, not for professional utility. Same discipline as the [[SLIC Input 13]] audit-your-instruments principle: audit your discovery sources.

## Direct implications for Non's live projects — small

- **FloodDash** — Quad9 recommendation could go into the "About the data" page as the recommended DNS for anyone using flood.nonarkara.org from public WiFi. Minor.
- **Phuket SMART Bus** — no direct fit
- **SLIC v3** — Awesome-OSINT-List has geospatial + demographic-research tools worth surveying for SLIC's data-source plug-in architecture; light research value
- **Non's own smart-city research** — the OSINT + GeoSpy + Kaspersky-map material is directly relevant to smart-city surveillance-ethics + civic-cyber-resilience frames; **potential Horizon Research paper #29 seed**: *"Smart cities and the surveillance stack: what Thai policymakers should know about the OSINT tools already deployed against Thai citizens by external actors."*

## The Horizon Honesty Layer application — this batch is a test

Today's session built the Horizon Honesty Layer through [[Input 26]], [[Input 41]], [[Input 56]], [[Input 58]] + grandfather coda + [[SLIC Input 13]]. This batch tests it. **The correct response is not "block everything scary" or "elevate everything Non forwards."** The correct response is:

1. Tier A/B — items that pass both technical-legitimacy and Thai-legal-ethical tests get through with normal discipline
2. Tier C — real value, wrong moment or narrow scope; parked
3. Tier D — items where Thai law + the Honesty Layer + the *"if we teach this, we own the harm"* discipline says *no*

**Same shape as [[Input 60]] rejected ALLGPT / Emailnator; this brief rejects romspure.cc + conditional-rejects the hacking + geolocation tools.** Consistent application of the discipline.

## Cross-references

- [[Input 60 Ultraboost Integration Map]] — the pattern this brief follows for tier classification + hard-skip discipline
- [[Input 65 WanGP]] — the sibling "capability + Thai-legal-bounds must be first-class" template applied here
- [[Input 26 Skill Preservation]] / [[Input 41 Acemoglu]] / [[Input 58 Manabu]] — the Horizon Honesty Layer this brief operationalizes
- [[SLIC Input 13 — Non's methodology critique]] — audit-your-instruments discipline applied to *discovery-source audit* here
- Thai Copyright Act B.E. 2537 (as amended) — Tier D piracy citation
- Thai Computer Crime Act B.E. 2560 — Tier D unauthorized-hacking + geolocation citations
- Thai PDPA (Personal Data Protection Act 2019) — Tier D geolocation-of-persons citation
- [[Horizon Input 62 — GeoLibre]] — the *legitimate* geospatial-tool filing pattern that contrasts with the geolocation-guesser filing here
- [[brief.md]] master Horizon brief — request: add *"Discovery Source Audit"* to the M6 methodology layer; add the four-tier framework as the canonical adoption-decision template
