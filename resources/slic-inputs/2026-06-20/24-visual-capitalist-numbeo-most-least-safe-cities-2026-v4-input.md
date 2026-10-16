# SLIC Input 24 — Visual Capitalist / Numbeo "Most and Least Safe Cities 2026" — SLIC v4 adds the Safety axis dimension

**Source:** Visual Capitalist · underlying data: **Numbeo 2026 Mid-Year Safety Index by City** · 401 cities · major cities = ≥2M residents (UN standardized definition 2025) · **crowdsourced (user-submitted) perceptions of crime and personal safety.** Non 2026-09-18 (implicit SLIC v4 pattern continuation).

## The rankings — verbatim

**2026 Safest (Score/100 — HIGHER = safer perceived):**
| # | City | Score |
|---|---|---|
| 1 | Doha, Qatar | 85 |
| 2 | Dubai, UAE | 84 |
| 3 | Taipei, Taiwan | 83 |
| 4 | Hong Kong SAR, China | 78 |
| 5 | Singapore | 78 |
| 6 | Tokyo, Japan | 76 |
| 7 | Shenzhen, China | 76 |
| 8 | Riyadh, Saudi Arabia | 75 |
| 9 | Jeddah, Saudi Arabia | 75 |
| 10 | Seoul, South Korea | 75 |

**2026 Least Safe (Score/100 — LOWER = less safe perceived):**
| # | City | Score |
|---|---|---|
| 1 | Caracas, Venezuela | 19 |
| 2 | Johannesburg, South Africa | 19 |
| 3 | Durban, South Africa | 20 |
| 4 | Salvador, Brazil | 24 |
| 5 | Fortaleza, Brazil | 24 |
| 6 | Rio de Janeiro, Brazil | 25 |
| 7 | Recife, Brazil | 25 |
| 8 | Guayaquil, Ecuador | 25 |
| 9 | Cape Town, South Africa | 26 |
| 10 | Cali, Colombia | 29 |

**Bangkok is absent from both lists** — same systematic Numbeo-Bangkok-gap pattern as [[SLIC Input 12]] / [[SLIC Input 18]] / [[SLIC Input 19]]. Bangkok is presumably in the middle band (likely 55-70 range based on regional-neighbor calibration; needs direct Numbeo close-out per the persistent-gap discipline).

## ⚠️ Methodology critique — first-class per [[SLIC Input 13]] discipline

**Numbeo Safety Index = crowdsourced perception, not observational crime data.** Three specific biases must be surfaced before any SLIC v4 use:

### 1. Numbeo users skew expat / higher-income
Already established across today's session (Inputs 12, 18, 19). *"Safety"* here is expat-perceived safety, not median-resident lived reality. A Cape Town cook commuting from a township experiences the city differently than a Cape Town remote worker in Camps Bay.

### 2. Authoritarian-safety scoring distortion
**Top 10 has zero Western democratic cities.** The Numbeo Safety Index systematically rewards cities that combine:
- Strong surveillance (Shenzhen, HK, Singapore, Tokyo, Doha, Riyadh)
- Low visible informal-economy activity
- Strict-penalty-enforcement regimes
- Heavy expat neighborhoods physically separated from local high-crime zones

**Doha at 85 does not mean Doha is objectively safest in every metric** — it means expats in Doha perceive high personal safety, which is what Qatar's authoritarian-with-services governance model produces. Same for Dubai, Riyadh, Jeddah. **This ranking cannot distinguish "safe" from "authoritarian-surveilled" from "spatially-segregated."**

**For a SLIC v4 that speaks to Thai smart-city audiences, this distortion matters** — Thai smart-city policy conversations should not silently adopt a metric that would score authoritarian governance highly as *the model to pursue.*

### 3. Spatial-inequality invisibility
Cape Town at 26 has genuinely high crime rates BUT the number also reflects extreme spatial segregation — expat perception depends on which parts of the city they inhabit. **A city-average score erases neighborhood-scale reality.** This is exactly the resolution problem [[SLIC Input 23 Time Out]] Talat Noi #14 highlighted for a different metric: **neighborhood-level resolution is often more meaningful than city-level averages.**

## SLIC v4 architectural addition — Safety as a proper axis

**Safety was not previously in the SLIC v4 axis architecture.** This input fills a real gap.

Proposed structure:

```
Safety (v4 — NEW axis, decomposed to avoid Numbeo-perception distortion)
├── Perceived safety
│   ├── Numbeo Safety Index (this input) — with expat-bias caveat
│   ├── Gallup World Poll "feel safe walking alone at night" (recommended cross-check)
│   └── OECD Better Life Index safety domain (for OECD members)
├── Observed crime
│   ├── UNODC homicide rate
│   ├── National police reported-crime rates (Thai NSO / Royal Thai Police)
│   ├── UN CTS victimization surveys
│   └── Gun-death rates (where applicable)
├── Emergency-response quality
│   ├── Fire response time
│   ├── Ambulance response time
│   ├── Police response time
│   └── Emergency-hotline availability
└── Spatial-inequality of safety
    ├── Coefficient of variation across city districts (novel metric — SLIC methodological contribution)
    ├── Rich-district safety score minus poor-district safety score
    └── Public-space accessibility by demographic
```

**The multi-source decomposition is what protects SLIC v4 from the perception-bias distortion.** No single index defines safety; the composite forces the honesty [[SLIC Input 13]] argues for.

## Direct connection to today's SLIC v4 arc

- **[[SLIC Input 21 IMF unemployment]]** — the SEA cluster with low unemployment (Thailand 1.0%, Singapore 2.0%, Vietnam 2.1%, Japan 2.5%, S.Korea 2.8%, Malaysia 3.0%, HK 3.3%, Taiwan 3.4%) largely overlaps with the SEA safety cluster (HK, Singapore, Tokyo, Shenzhen, Seoul, Taipei = 6 of top 10). **These are same-model-different-outcome benchmarks** — Bangkok is SEA but has more Western-democratic-messy characteristics than the Singapore/HK/Shenzhen governance model.
- **[[SLIC Input 20 Deutsche Bank]] Peer-Comparator Cluster methodology** — same discipline applies here. Bangkok's actual safety-peer cluster is likely Mumbai / Delhi / Manila / Jakarta / mid-band emerging-market capitals, NOT Singapore / HK / Doha (aspirational-peers, not actual-peers).
- **[[SLIC Input 23 Time Out]] neighborhood-resolution** — safety at neighborhood level within Bangkok varies dramatically (Silom night vs Ari day vs Klong Toei vs Sukhumvit); city-level averaging erases that.
- **[[Input 70 Blair]] macro-frame** — safety as a specific case where the *"system working as designed"* pattern applies at the metric-methodology layer: Numbeo's methodology is *designed to produce* rankings that favor authoritarian-strong-state governance because those are the conditions expat users report perceiving as safe. Design produces output.

## Bangkok / Thailand across TWELVE external metrics — updated

| Metric | Thailand / Bangkok |
|---|---|
| Wharton 2026 QoL | Thailand: 32 (country) |
| Numbeo Asia salary vs cost | Bangkok not included |
| Tourist bookings 2026 | Bangkok: **#1** |
| Digital-nomad density | Bangkok: **#1** (Chiang Mai #10) |
| BCG Intelligent Cities | Bangkok NOT in top 20 |
| Cost-to-retire | Thailand not labeled (~$290-350K est.) |
| Emelianov Value Quadrant | Bangkok not visible; Chiang Mai BEST VALUE |
| OECD Senior Poverty | Thailand not OECD; NSO ~15-25% |
| Deutsche Bank net salary | Bangkok #59 · $844/mo |
| IMF unemployment | Thailand: 1.0% (methodologically narrow) |
| Fastest-growing developed metros | Thailand not in scope; BKK proper losing pop |
| Time Out Coolest Neighborhoods | Talat Noi #14 (Bangkok best-ever) |
| **Numbeo Safety Index (this)** | **Bangkok not in top/bottom 10 — presumed 55-70 mid-band, needs close-out** |

## The v4 launch narrative — safety-axis added

> ***Bangkok's safety score sits in the middle band of Numbeo's perception index — not authoritarian-strong-state levels like Singapore/HK/Tokyo/Doha, not structural-violence levels like Caracas/Johannesburg/Rio, but the messy-democratic middle. This is a legitimate reading of a specific methodology; SLIC v4 pairs it with UNODC observational crime data + neighborhood-level variance + emergency-response-time metrics rather than adopting it alone.***

## Horizon Research paper #40 seed

*"When Safety Rankings Reward Authoritarianism: What Bangkok Loses By Adopting Perception-Based Safety Indices Uncritically."* Anchor: this input + [[SLIC Input 13]] methodology critique + [[Input 70 Blair]] macro-frame + UNODC data + a comparison across (Singapore-model / HK-model / Tokyo-model / Doha-model / Bangkok-democratic-model). Direct fit for SEIC / depa / BMA / Ministry-of-Interior / Ministry-of-Justice audiences considering whether to adopt strong-state surveillance in the name of "smart city" measures.

## Verification pass

- 🟢 Numbeo Safety Index is a real, well-known crowdsourced index
- 🟢 Visual Capitalist is a legitimate infographic publisher
- 🟢 The regional clusters (East Asia + Middle East safest by Numbeo methodology; Latin America + South Africa least safe) are consistent across multiple prior Numbeo Safety Index editions
- 🟡 **Specific 2026 mid-year figures** — verify against Numbeo's live index at numbeo.com/crime before Horizon or SLIC v4 cites
- 🟡 **Bangkok's actual position** in the 401-city dataset — should be pulled directly from Numbeo, not extrapolated
- 🟡 **The perception-vs-observation distinction** is the load-bearing critique — surface in every downstream use

## What NOT to do

- ⚠️ **Do not treat Doha #1 as recommending Doha-model governance to Bangkok** — the ranking reflects methodology + expat-user-base composition; not a normative recommendation
- ⚠️ **Do not compare Bangkok to Singapore/HK/Tokyo directly on this metric** — Peer-Comparator Cluster discipline applies; Bangkok's actual safety peers are mid-band SEA + mid-band emerging markets
- ⚠️ **Do not romanticize the least-safe city rankings as inherent character** — Cape Town, Johannesburg, Rio all have deep structural histories (apartheid-legacy, cocaine-trade dynamics, informal-settlement policing) that a safety score cannot express and that policy responses must engage
- ⚠️ **Do not skip the neighborhood-resolution nuance** — Bangkok has safe districts and unsafe districts; averaging erases the [[SLIC Input 23]] discipline

## The v4 spec doc is now more-than-ready — this is the third day I recommend drafting

The architecture has all the pieces:
- **12 external metrics** in the Bangkok/Thailand decomposition
- **5 population-flow sub-axes** under Capital Attraction Velocity
- **Populations Left Behind** sub-axis (5+ sub-metrics)
- **Safety axis (this input)** — new
- **Neighborhood resolution ([[SLIC 23]])** — new
- **Top-down / bottom-up decomposition** — new
- **Coexistence-over-erasure design principle** — Non's design system elevated to methodology
- **BCG 5-domain framework** as reference
- **Emelianov 4-quadrant visualization**
- **Peer-Comparator Cluster methodology**
- **Headline-vs-reality gap** methodology-item
- **Counterparty Reliability** axis
- **Global-Index Alignment** cross-check discipline

**Say the word and I ship the v4 spec doc — this is exactly the moment.**

## Cross-references

- [[SLIC Inputs 09-23]] full chain
- [[Horizon Input 70 Blair]] — macro-frame explaining why Numbeo methodology systematically favors authoritarian-strong-state governance in its safety rankings
- [[project_slic_engagement_vehicle]] — v4-revamp status
- Numbeo Crime Index at numbeo.com/crime — primary source, verify specifics
- UNODC + UN CTS + national police statistics — recommended cross-reference sources for the observational-crime layer
- Gallup World Poll "feel safe walking alone at night" — recommended cross-reference for perception layer
- [[brief.md]] master SLIC brief — request: adopt Safety as new axis with 4-way decomposition; commission v4 spec doc write-up
