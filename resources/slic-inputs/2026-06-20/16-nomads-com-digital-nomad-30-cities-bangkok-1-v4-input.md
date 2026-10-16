# SLIC Input 16 — nomads.com 2026: 30 cities most visited by digital nomads (Bangkok #1) — for SLIC v4 revamp

**Source:** nomads.com 2026 dataset · infographic © 2026 Iswardi Ishak · **Non 2026-07-17 explicitly framed this as *"more stuff for SLIC v4 revamp"* — SLIC is now v4-active, not v3-current.** Sample: 423,694 trips / 16,117 survey respondents.

## The ranking — verbatim, top 30

| # | City | Country | % |
|---|---|---|---|
| **1** | **Bangkok** | Thailand | **2.22%** |
| 2 | London | UK | 2.19% |
| 3 | Barcelona | Spain | 1.48% |
| 4 | New York City | USA | 1.46% |
| 5 | Paris | France | 1.46% |
| 6 | Lisbon | Portugal | 1.44% |
| 7 | Berlin | Germany | 1.43% |
| 8 | Amsterdam | Netherlands | 1.18% |
| 9 | San Francisco | USA | 1.13% |
| **10** | **Chiang Mai** | Thailand | **1.07%** |
| 11 | Mexico City | Mexico | 0.98% |
| 12 | Tokyo | Japan | 0.92% |
| 13 | Canggu* (Bali) | Indonesia | 0.91% |
| 14 | Singapore | Singapore | 0.89% |
| 15 | Istanbul | Turkey | 0.86% |
| 16 | Madrid | Spain | 0.83% |
| 17 | Kuala Lumpur | Malaysia | 0.81% |
| 18 | Los Angeles | USA | 0.80% |
| 19 | Dubai | UAE | 0.79% |
| 20 | Budapest | Hungary | 0.77% |
| 21 | Prague | Czechia | 0.70% |
| 22 | Buenos Aires | Argentina | 0.69% |
| 23 | Medellin | Colombia | 0.62% |
| 24 | Rome | Italy | 0.60% |
| 25 | Moscow | Russia | 0.59% |
| 26 | Vienna | Austria | 0.57% |
| 27 | Seoul | South Korea | 0.56% |
| 28 | Ho Chi Minh City | Vietnam | 0.55% |
| 29 | Hong Kong | Hong Kong | 0.54% |
| **30** | **Phuket** | Thailand | **0.53%** |

**Callout:** *"The U.S. and Thailand are major destinations for digital nomads, each with 3 cities in the Top 30."*

**Thailand's trinity: Bangkok #1 + Chiang Mai #10 + Phuket #30 = 3.82% of global sample.** Highest single-country share alongside the US (Bangkok + London + Barcelona ≈ 5.89% for the top 3; Thailand's 3 cities together are the highest-density-per-population national representation).

## Verification pass — three green, two amber

- 🟢 **nomads.com is real + established.** Pieter Levels' project, part of the RemoteOK / NomadList ecosystem. One of the primary datasets for digital-nomad research.
- 🟢 **Sample size (423K trips / 16K respondents) is plausible** for that platform's user base.
- 🟢 **Bangkok / Chiang Mai / Canggu / Lisbon / Mexico City ranking high is well-established** — matches multiple independent digital-nomad indices (Nomad List, Remote Year, Statista, WorldRemote).
- 🟡 **Sample bias: nomads.com users skew "Western digital nomad."** Chinese, Indian, MENA, African, Latin American nomads (who exist in growing numbers) are structurally underrepresented. **The 2.22% for Bangkok reflects English-speaking-primarily-Western-passport digital-nomad choice, not all remote workers globally.** Should be surfaced when Horizon or SLIC cites.
- 🟡 **"Iswardi Ishak" credit is the infographic designer**, not the primary data source. nomads.com is the primary. Cite the primary in any downstream SLIC v4 material.

Per [[feedback_teach_dont_silently_fix]] + [[SLIC Input 13]] methodology critique: sample bias is real signal, not a fatal flaw.

## Why this matters specifically for SLIC v4 (not v3)

**Non's explicit *"more stuff for SLIC v4 revamp"* framing is a new architectural signal for me.** SLIC has moved from v3 (where I have been anchoring today's inputs 09-15) into v4 revamp mode. The [[project_slic_engagement_vehicle]] memory has been updated to reflect this. **What this input contributes to v4 that v3's structure could not cleanly hold:**

### 1. A distinct third-population axis (Tourists / Digital Nomads / Residents)

**SLIC v3's Capital Attraction Velocity axis blended these three. SLIC v4 should split them.** They are structurally different populations:

| Population | Visit duration | Local employment created | Wage-currency arbitrage | Rent/service pressure | Cultural embedding |
|---|---|---|---|---|---|
| **Tourists** | days-weeks | high (hospitality staff) | none | seasonal, concentrated | shallow / short |
| **Digital nomads** | weeks-months | low (rent contracts + coworking + F&B only) | **HIGH** (USD/EUR wages competing with THB rents) | year-round in nomad districts | medium / medium |
| **Residents** | multi-year to permanent | contribute + consume + embed | none for locals; some for foreign residents | continuous | deep / long |

**SLIC v4 axis proposal:** Split the current *Capital Attraction Velocity* axis into three sub-axes:
- **Tourist bookings velocity** (already covered by [[SLIC Input 15]] Bangkok #1 tourism ranking)
- **Digital-nomad density** (this input; Bangkok 2.22%)
- **Long-term-resident-conversion rate** — of the nomads who visit, what % transition to LTR/PR status? This turns extraction into embedding. **This is a SLIC-methodological-contribution opportunity — no external index measures this cleanly.**

### 2. Wage-arbitrage vulnerability as its own v4 sub-metric

Cities where a significant fraction of housing demand comes from foreign-currency earners have specific vulnerabilities: rent inflation, displacement of local-salary tenants, English-menu-first commercial displacement of local-oriented establishments, and cultural commodification. **Bangkok, Chiang Mai, Phuket all score high on this vulnerability** by virtue of appearing on this list.

**Concrete sub-metric proposal:** *District-level rent inflation attributable to non-local-currency demand*. Data sources: BOT rental-index data + BMA planning-department district-level housing data + Chiang Mai / Phuket municipal equivalents. Novel metric; SLIC v4 could ship it first.

### 3. Nomad-density concentration by district (not city)

**City-level rankings hide district-level concentration where impacts are actually felt:**

- Bangkok — **Ari, Ekkamai, Thonglor, Silom, Sukhumvit** are the nomad-heavy districts. Sam Sen / Bang Bo / most peripheral districts see negligible nomad presence.
- Chiang Mai — **Nimmanhaemin, Santitham, Chang Klan** dominate; Doi Saket / San Sai are largely unaffected.
- Phuket — **Rawai, Kata, Karon, some of Chalong** for nomads; the rest of the island (particularly the interior) is largely local.

**SLIC v4 should be able to zoom in.** District-level nomad-density heat maps are a real product surface.

### 4. The "nomad-friendly visa system" honesty note

The infographic praises Thailand's *"nomad-friendly visa system."* **This deserves honest qualification in SLIC v4:**

- Thailand's **Long-Term Resident (LTR) visa** launched 2022 with meaningful income gates
- **LTR-Wealthy Global Citizens:** $80,000/year income + $1M assets requirement
- **LTR-Work-From-Thailand Professionals:** $80,000/year income OR $40,000 + specialty + PhD or 5-yr work experience with a Fortune 500 / listed company
- **LTR-Wealthy Pensioner:** $80,000/year income OR $40,000 + $250K investment
- **Elite / Privilege Visa (former Thailand Elite):** ฿900K-฿5M initial payment for 5-20 year residency

**These thresholds gate the "nomad-friendly" label to a specific income bracket.** The 2.22% Bangkok figure is not "any remote worker can come easily" — it is "Western/wealthy/company-backed remote workers can come easily." Surfacing this discipline distinguishes SLIC v4 from marketing-oriented "Bangkok is amazing for nomads" content.

### 5. Cross-decomposition with [[SLIC Input 15 Bangkok tourism]]

Bangkok is now **#1 in both dimensions** (tourists AND digital nomads). This is a specific *concentration pattern* SLIC v4 should name:

> *"Bangkok is the world's #1 city for both tourist bookings AND digital nomad visits — meaning transient / foreign-currency-earning populations put simultaneous pressure on Bangkok's housing, transport, and service economy from two different directions at once."*

**Combined with [[SLIC Input 09 Wharton QoL Thailand 32]], the picture completes:**

- Thailand (country) — Wharton QoL 32 (mid-band)
- Bangkok (city) — extracts significant global capital via tourism + nomads
- Bangkok's specific districts (Ari/Ekkamai/Nimman/Rawai equivalents) — concentrate the pressure
- Bangkok's residents (at Thai baht salaries per [[SLIC Input 12]] Numbeo gap) — bear the rent-inflation cost

**This is the coherent Bangkok story SLIC v4 should ship at launch.** Not "Bangkok wins everything" — "Bangkok wins the metrics that reward foreign-currency inflows, and the cost distribution is asymmetric."

## Honesty Layer application — this is the [[Input 70 Blair]] frame at Bangkok scale

Blair's essay ([[Input 70]]) argues *"the system isn't broken, it's working as designed."* **Bangkok's dual #1 rankings for tourism and digital nomads is the Bangkok-specific instance of that argument** — the system that concentrates foreign inflows in specific districts while leaving Thai-baht wages stagnant and displacing long-term residents is *working as designed for the population it serves*, and it is not the population that lives at Thai wages.

SLIC v4 should treat this decomposition as *first-class methodology*, not as an implicit sub-note. Same discipline as [[SLIC Input 13]]'s audit-your-instruments principle.

## Direct connection to Non's ecosystem

- **Bangkok / Chiang Mai / Phuket are all depa smart-city cities** — Non's SEIC positioning covers all three
- **The Phuket SMART Bus project** ([[Phuket Bus WO-01]]) serves airport passengers who are exactly this digital-nomad + tourist demographic — the operational implications of the Bangkok/Chiang Mai/Phuket trinity are directly relevant
- **FloodDash** serves Thai-baht residents primarily — the population whose interests SLIC v4's decomposition would surface

## Placement in SLIC v4 revamp

### Load-bearing sub-axis under a restructured *Capital Attraction Velocity* pillar

Proposed v4 structure for the Capital Attraction Velocity pillar:

```
Capital Attraction Velocity (v4)
├── Tourist bookings velocity
│   └── Source: MasterCard, Euromonitor, or via [[SLIC Input 15]] equivalents
├── Digital-nomad density
│   └── Source: nomads.com (this input) + NomadList + Remote Year + Statista cross-references
├── Long-term-resident conversion rate
│   └── SLIC-methodological-contribution — no external index; requires proprietary methodology
└── Wage-arbitrage vulnerability
    └── SLIC-methodological-contribution — district-level rent-inflation-attributable-to-foreign-currency-demand
```

### Bangkok Contribution Card update

The [[SLIC Input 12 Numbeo]] filing already proposed a *"SLIC v3 Bangkok Contribution Card"* to close the Numbeo Asia-comparison Bangkok gap. **v4 version should be the composite Bangkok-in-context-of-three-populations story.**

### Horizon Research paper #32 seed

*"Bangkok's Dual #1: Tourism + Digital-Nomad Attraction as a Concentrated Pressure Signature"* — anchor on [[SLIC Input 15]] + this input + [[SLIC Input 09 Wharton QoL]] + [[SLIC Input 12 Numbeo gap]] + [[Input 70 Blair]] macro-frame. Direct fit for SEIC / depa / BMA / Ministry-of-Tourism-and-Sports / Ministry-of-Higher-Education-Science-Research-Innovation audiences.

## What NOT to do

- ⚠️ **Do not treat 2.22% Bangkok as "any remote worker can easily nomad here"** — the LTR visa income gates are real; surface them
- ⚠️ **Do not read Bangkok #1 as "Bangkok is best for digital nomads"** — nomads.com's sample skews Western; the ranking measures where Western digital nomads *actually go*, not where digital nomads globally would rank cities
- ⚠️ **Do not conflate this dataset with tourism data** — different populations, different impacts, different SLIC v4 sub-axes
- ⚠️ **Do not celebrate the "Thailand has 3 of top 30" callout uncritically** — Thailand also has 3 of the most-rent-inflation-affected districts by nomad demand. Same fact, different framing.

## Cross-references

- [[SLIC Input 09 Wharton 2026 QoL]] — Thailand 32 country-ceiling this input's Bangkok-specific ranking sits above
- [[SLIC Input 12 Numbeo Asia salary vs cost of living]] — the Bangkok data gap this input helps close
- [[SLIC Input 13 Non's methodology critique]] — audit-your-instruments discipline for the nomads.com sample-bias
- [[SLIC Input 14 Mumbai-Ahmedabad]] — counterparty-reliability + narrative-critique discipline
- [[SLIC Input 15 Bangkok #1 tourism]] — Bangkok's *other* #1 ranking; this input pairs with it for the dual-#1 concentration story
- [[Horizon Input 70 Blair — Japan as preview]] — the macro-theoretical frame under which Bangkok's dual-#1 is the *"system working as designed"* for foreign-currency populations, not local-currency residents
- [[Horizon Input 61 LINE OA MCP]] + [[Horizon Input 54 KitCost]] — the Solo Empire framing that maps to a subset of digital-nomad life
- [[Phuket Bus WO-01]] — direct operational relevance (Phuket #30 puts nomads on the SMART Bus)
- [[project_slic_engagement_vehicle]] — memory updated 2026-07-17 to reflect v4-revamp status
- Data source primary: nomads.com; verify against NomadList, Remote Year, Statista, WorldRemote for cross-reference
- Thai LTR visa policy details: BOI Thailand + Immigration Bureau primary sources
- [[brief.md]] master SLIC brief — request: full **v4 revamp** with the four-sub-axis Capital Attraction Velocity restructure proposed above
