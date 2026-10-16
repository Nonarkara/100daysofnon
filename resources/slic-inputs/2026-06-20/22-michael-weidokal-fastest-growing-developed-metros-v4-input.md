# SLIC Input 22 — Michael Weidokal: Fastest-growing developed-economy metros (post-2020) — SLIC v4 adds the fifth population-flow sub-axis

**Source:** michaelweidokal.com · *"The Fastest-Growing Major Metropolitan Areas in Developed Economies"* · population growth since 2020 · metros ≥1M population · top 25. Non 2026-09-18 with the note *"for my slic v4, things are cooking up with all these data."*

## The ranking — verbatim, top 25

| # | Metro | Country | Growth |
|---|---|---|---|
| 1 | Austin | US | 14.8% |
| 2 | Raleigh | US | 12.9% |
| 3 | Calgary | Canada | 13.0% |
| 4 | Edmonton | Canada | 11.5% |
| 5 | Dallas-Fort Worth | US | 11.0% |
| 6 | Orlando | US | 10.6% |
| 7 | Charlotte | US | 10.5% |
| 8 | Houston | US | 10.5% |
| 9 | San Antonio | US | 10.0% |
| 10 | Jacksonville | US | 9.5% |
| 11 | Nashville | US | 9.0% |
| 12 | Tampa | US | 8.5% |
| 13 | Brisbane | Australia | 8.0% |
| 14 | Perth | Australia | 8.0% |
| 15 | Phoenix | US | 7.8% |
| 16 | Atlanta | US | 6.1% |
| 17 | Auckland | New Zealand | 6.1% |
| 18 | Melbourne | Australia | 6.0% |
| 19 | Adelaide | Australia | 6.0% |
| 20 | Vancouver | Canada | 6.0% |
| 21 | Ottawa-Gatineau | Canada | 6.0% |
| 22 | Madrid | Spain | 5.5% |
| 23 | Barcelona | Spain | 5.0% |
| 24 | Amsterdam | Netherlands | 4.5% |
| 25 | Incheon | South Korea | 4.5% |

**Regional distribution — Anglo-immigrant-driven dominance:**
- **US Sun Belt: 14 cities** (of 25 = 56%)
- **Canada: 4** (Calgary, Edmonton, Vancouver, Ottawa-Gatineau)
- **Australia: 4** (Brisbane, Perth, Melbourne, Adelaide)
- **New Zealand: 1** (Auckland)
- **Spain: 2** (Madrid, Barcelona)
- **Netherlands: 1** (Amsterdam)
- **South Korea: 1** (Incheon, at #25 with 4.5%)

**Publisher callouts:** *"14 of top 25 are in the US, with rapid growth across the Sun Belt · Canada and Australia also feature prominently, driven by immigration and internal migration · European metros show moderate growth, while growth in Japan, South Korea and Taiwan is limited to a few areas."*

## Two absences that are the actual story

**Japan absent** — no Tokyo, no Osaka. **Consistent with [[Input 70 Blair]]'s Japan-as-preview thesis + [[SLIC Input 17 BCG]] Tokyo not in top 20 Intelligent Cities.** Japan's population is contracting; even Tokyo (the only Japanese metro that had been growing marginally) has plateaued. **Blair-frame receipt at metro-growth scale.**

**Southeast Asia entirely absent** — no Bangkok, HCMC, Hanoi, KL, Jakarta, Singapore, Manila. **This is methodological, not comparative:** the chart's *"developed economies"* scope systematically excludes emerging-Asia metros, most of which are growing much faster than any city on this list. Bangkok's greater metropolitan area continues to grow modestly (~1% per year) but Bangkok proper is *losing* population to suburbanization + demographic contraction. Chiang Mai / Phuket / Pattaya are outside scope.

## Two convergences that are the SLIC v4 story

### 1. The migration-FROM-BAD-VALUE-TO-Sun-Belt pattern

Non's red-circled BAD VALUE cities from [[SLIC Input 19]] Emelianov quadrant (**SF, Paris, London, NYC, LA**) are precisely the coastal-premier cities Americans are moving *away* from. The US Sun Belt cities dominating this ranking (Austin, Raleigh, Dallas, Orlando, Houston, San Antonio, Jacksonville, Nashville, Tampa, Phoenix, Atlanta, Charlotte) are where the migration is going *to*. **[[Input 70 Blair]]'s macro-frame + Emelianov's city-value quadrants + this input together tell a single coherent story:** the internal-US migration is people leaving cities whose cost outpaced quality for cities whose growth is outpacing infrastructure.

### 2. The growth-vs-climate-vulnerability paradox

The US Sun Belt cluster in this ranking is climate-front-line territory:

- **Austin, San Antonio, Dallas-Fort Worth** — extreme heat, drought, aquifer depletion
- **Houston** — hurricane exposure, urban flooding, subsidence
- **Phoenix** — extreme-heat mortality, Colorado River water crisis
- **Tampa, Orlando, Jacksonville** — hurricane exposure + sea-level rise
- **Atlanta, Charlotte, Nashville, Raleigh** — moderate but rising climate exposure

**Fastest-growing metros in developed economies are systematically in the worst geological/climate-vulnerable positions.** This is a specific paradox SLIC v4's *geological/climate vulnerability* axis (from v3, retained) has always tracked but never quite named. **The permanent-resident growth is going toward — not away from — the cities most exposed to climate risk over the SLIC-v4-relevant 10-30 year horizon.**

Whether this is *rational* (federal-flood-insurance subsidies + air-conditioning + housing-affordability calculus) or *irrational* (climate-risk-myopia + Sun-Belt-narrative capture) is a specific research question. **Either answer is SLIC v4 methodological content.**

## SLIC v4 architectural addition — the fifth population-flow sub-axis

Updated Capital Attraction Velocity architecture (adds this input):

```
Capital Attraction Velocity (v4 — 5-way split)
├── Tourist bookings velocity              — [[SLIC 15]]
├── Digital-nomad density                  — [[SLIC 16]]
├── Retiree density + healthcare-load      — [[SLIC 18]]
├── Permanent-resident population growth   — this input ← NEW
│   ├── Domestic-migration in-flows
│   ├── International-immigration in-flows
│   ├── Growth-vs-climate-vulnerability decomposition
│   └── Growth-vs-affordability decomposition
├── Long-term-resident-conversion rate     — SLIC-methodological-contribution
└── Wage-arbitrage vulnerability           — [[SLIC 20]] + methodological-contribution
```

**Each population-flow sub-axis measures a different reader-question:**
- Tourists: who visits for days
- Digital nomads: who lives here for months
- Retirees: who moves here for decade+ of low-employment residency
- **Permanent residents: who commits to stay**
- Long-term-resident conversion: how many transient populations become the above
- Wage-arbitrage: how the currency-differential across these populations affects local wages

**This is the full 5-population + 1-conversion + 1-vulnerability architecture SLIC v4 should ship.**

## Bangkok / Thailand — across TEN external metrics now

| Metric | Thailand / Bangkok |
|---|---|
| Wharton 2026 QoL | Thailand: 32 (country) |
| Numbeo Asia salary vs cost | Bangkok not included |
| Tourist bookings 2026 | Bangkok: **#1** |
| Digital-nomad density | Bangkok: **#1** (Chiang Mai #10) |
| BCG Intelligent Cities | Bangkok not in top 20 |
| Cost-to-retire | Thailand not labeled (~$290-350K est.) |
| Emelianov Value Quadrant | Bangkok not visible; Chiang Mai BEST VALUE |
| OECD Senior Poverty | Thailand not OECD; NSO ~15-25% |
| Deutsche Bank net salary | Bangkok #59 · $844/mo |
| IMF unemployment | Thailand: 1.0% (methodologically narrow) |
| **Fastest-growing developed metros (this)** | **Thailand not in scope; Bangkok proper losing population** |

**The v4 launch narrative — now with permanent-resident population dynamics added:**

> ***Thailand and Bangkok win the metrics that measure transient foreign-currency population attraction (tourists #1, digital nomads #1), score mid-band on Wharton country QoL and Deutsche Bank professional wages, are absent from the developed-economy fastest-growth ranking (in scope and in reality — Bangkok proper is losing population to suburbanization), and pair a 1.0% headline unemployment with a 55% informal-sector reality. This is a foreign-currency-inflow-optimized city that is simultaneously demographic-outflow at its core — a specific policy signature.***

## Verification pass

- 🟢 Michael Weidokal is a real economist who publishes at michaelweidokal.com; the fastest-growing-metros series is a recurring piece
- 🟢 The US Sun Belt dominance pattern is well-documented in US Census Bureau data
- 🟢 The Canada / Australia immigration-driven growth pattern is consistent with StatsCan and ABS data
- 🟡 **Specific percentages** — verify against Census / StatsCan / ABS / Eurostat / national-statistics sources before Horizon or SLIC v4 cites specific figures
- 🟡 **"Since 2020" methodology** — verify whether the 2020 baseline is pre-pandemic Jan-2020 or post-shock late-2020, which affects some rankings notably
- 🟡 **Metro-boundary definitions** vary across countries (MSA vs Combined Statistical Area vs Australian GCCSA vs European NUTS3 metropolitan definitions). Cross-country comparisons need methodology-standardization notes.

Per [[SLIC Input 13]] audit-your-instruments discipline: these are surface-in-downstream-use, not blocking.

## Horizon Research paper #38 seed

*"Fastest-Growing Developed-Economy Metros vs Climate Vulnerability: The Sun Belt Paradox and What It Says About the 10-30 Year Livability Horizon."* Anchor: this input + [[SLIC Input 09 Wharton QoL]] + [[Input 70 Blair]] + [[SLIC Input 19]] Emelianov + climate-risk primary sources (IPCC AR6, US National Climate Assessment, World Bank Climate Change Knowledge Portal). Direct fit for SEIC / depa / BMA / academic-urban-planning audiences — particularly Thai-context, because Bangkok faces its own version of the climate-vulnerability-vs-growth trade-off (geological subsidence, sea-level rise, urban heat island).

## The SLIC v4 spec doc is now writable

**With this input, the v4 architecture has stabilized:**

- **10 external metrics** in the Bangkok/Thailand decomposition
- **5 population-flow sub-axes** under Capital Attraction Velocity
- **Populations Left Behind** sub-axis under Sub-numerical Human Conditions (5 sub-metrics)
- **BCG 5-domain framework** as reference (Outcomes / Strategy / Adoption / Ways of Working / Enablers)
- **Emelianov 4-quadrant visualization** as v4 launch visual
- **Peer-Comparator Cluster methodology** established
- **Headline-vs-reality gap** as v4 methodology-item
- **Counterparty Reliability** axis from [[SLIC Input 14]]
- **Global-Index Alignment** cross-check discipline
- **Retirement-time-cost + formal-informal-wage-gap** sub-metrics

**Recommend I draft the full SLIC v4 spec doc now.** My zone; multi-hour docs/architecture work; produces the reference architecture the actual v4 build can Codex against. **Say the word.**

## What NOT to do

- ⚠️ **Do not celebrate Bangkok's absence from this list as a positive** — being outside the *developed-economy fast-growth* scope is not a Bangkok-strength story; it is a scope-story
- ⚠️ **Do not treat the US Sun Belt cluster as unambiguously successful** — the climate-vulnerability paradox is real; today's growth city may be tomorrow's climate-refugee-origin
- ⚠️ **Do not extrapolate the migration-FROM-BAD-VALUE pattern to non-US contexts uncritically** — Thai internal migration has different structural drivers (agricultural-to-urban, dominant Bangkok primate-city pattern) than US coastal-to-Sun-Belt dynamics
- ⚠️ **Do not cite specific percentages until cross-verified** against national statistics sources

## Cross-references

- [[SLIC Input 09 Wharton QoL]] · [[SLIC Input 10 Goldman Korea]] · [[SLIC Input 12 Numbeo]] · [[SLIC Input 13 methodology critique]] · [[SLIC Input 14 Mumbai-Ahmedabad]] · [[SLIC Input 15 tourism]] · [[SLIC Input 16 nomads]] · [[SLIC Input 17 BCG]] · [[SLIC Input 18 cost-to-retire]] · [[SLIC Input 19 Emelianov + OECD senior poverty]] · [[SLIC Input 20 Deutsche Bank]] · [[SLIC Input 21 IMF unemployment]]
- [[Horizon Input 70 Blair — Japan as preview]] — the macro-frame Japan's absence from this list reinforces
- [[Horizon Input 58 Manabu machine-consumes-itself]] — the theoretical layer
- [[Jim Carrey grandfather grounding coda]] — the population-left-behind counterpart to this growth-inflow story
- [[project_slic_engagement_vehicle]] — v4-revamp status
- Michael Weidokal · michaelweidokal.com — primary source; verify specific figures against Census / StatsCan / ABS / Eurostat before publication
- IPCC AR6 + US National Climate Assessment + World Bank Climate Change Knowledge Portal — climate-risk primary sources for the Horizon Research paper #38 climate-vs-growth analysis
- [[brief.md]] master SLIC brief — request: adopt Permanent-Resident Population Growth as 5th population sub-axis; commission v4 spec doc write-up
