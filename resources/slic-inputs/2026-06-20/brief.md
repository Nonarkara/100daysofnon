# SLIC Index v3 — input brief, 2026-06-20

Non sent the Visual Capitalist / Voronoi infographic *"The Cities with the Most Billionaires in 2026"* and flagged it as useful to the SLIC project at `~/projects/slic/v3`.

## What's in the data

Top-25 cities by billionaire count, color-coded by continent. Key facts visible in the graphic:

- **Top 10:** New York (146) — Shenzhen (132) — Shanghai (120) — Beijing (107) — London (102) — Mumbai (90) — Hong Kong (88) — San Francisco (84) — Moscow (82) — Hangzhou (64)
- **Bangkok ranks #17 with 38 billionaires** — that's the SLIC-relevant data point. Bangkok is on the same chart as Hong Kong, Singapore (#12, 51), Mumbai, Shanghai.
- **Insight callouts on the graphic:** Chinese cities account for 34% of billionaires across the top 25. 18 of the 32 billionaire capitals are in Asia, accounting for 58% of the 1,853 total billionaires on the global list.
- **Source:** Visual Capitalist / Voronoi, 2026 dataset. Image filed at `most-billionaires-by-city-2026-voronoi-visualcapitalist.png`.

## Why this matters for SLIC v3

SLIC (Smart Living Index / Smart Livability Index — naming TBD per the SLIC repo's own conventions) is one of Non's city-ranking dashboard projects, currently at v3. Earlier work (May 2026) tied SLIC to the depa/SEIC ecosystem and academic engagements with Chulalongkorn. The dashboard ranks cities on smart-livability indicators.

Billionaire concentration is a **legitimate-but-underused indicator of urban economic gravity**. It belongs on a SLIC-style dashboard because:

1. **It's a hard signal of where global capital concentrates.** Cities with billionaires have outsized influence on investment flows, talent migration, real-estate dynamics, and political access. SLIC is supposed to surface what makes cities competitive; billionaire density is one input.
2. **Bangkok at #17 is a comparison anchor.** When SLIC ranks Bangkok against Singapore, Hong Kong, Mumbai, Shanghai for ASEAN-and-region purposes, billionaire counts give a frictionless cross-city baseline.
3. **It complements smart-city KPIs the way GDP per capita can't.** Billionaire concentration is a tail-of-distribution signal; GDP per capita is a mean signal. The two together describe more of a city's economic shape than either alone.
4. **It's visually compelling.** SLIC dashboards live or die on the first 30 seconds of a Mayor's attention. A "billionaire density map" tile is the kind of thing that earns the next 30 seconds.

## Suggested integration into SLIC v3

**Three lightweight additions** — pick what fits the repo's actual current state:

1. **A "Billionaire Density" tile** on the city-comparison surface. Shows the count and the city's rank globally for any selected city. Source the data from the Visual Capitalist chart for the v3 launch, then upgrade to a live feed (Forbes Real-Time Billionaires API has it, but it's expensive; Visual Capitalist publishes annually and is free to cite with attribution).
2. **An ASEAN-cluster view** that compares Bangkok specifically against Hong Kong (#7, 88), Singapore (#12, 51), Mumbai (#6, 90), and Shanghai (#3, 120). This is the comparison set that matters most to Thai mayors and depa stakeholders — those are the cities Bangkok is competing with for capital, talent, and tourism.
3. **A "wealth concentration vs livability" scatter** — billionaire count on X-axis, SLIC composite livability score on Y-axis. The interesting cities are the off-diagonal ones: high-livability-low-billionaire (the Copenhagen/Helsinki/Vienna cluster) and high-billionaire-low-livability (a different argument for a different audience). This is the kind of visualization that gets shared on LinkedIn by city planners.

## Cross-reference

This input also has *secondary* value for [[Horizon AI Platform]] — specifically for **M5 (frontier ethics)** when discussing how AI startup valuations / billionaire wealth concentration intersect with the AI copyright lawsuits visualization (Input 12 to Horizon). A graphic showing AI-company founders on the billionaire list against the plaintiffs suing those companies would be a strong M5 discussion prompt. Not blocking; flag.

## Note on path

Non specified `~/projects/slic/v3` for the SLIC repo location. The previously-running SLIC code-task (local_691d60e3) is at `/Users/nonarkara/Projects/slic-index/v3-current`. If Non has moved/renamed the folder since May, the new path may be `/Users/nonarkara/Projects/slic/v3` or similar. The SLIC code-task message-send should resolve to whichever is current; if there's ambiguity, the task itself can figure it out.

---

## Third SLIC input added 2026-06-20 — "Hours of Work for $1,000 by OECD Country" (Visual Capitalist / Voronoi)

**Image:** `hours-to-earn-1000-usd-oecd-2023-voronoi.png`
**Source on the chart:** OECD via Our World in Data, 2023 PPP-adjusted annual wages ÷ 2023 annual working hours per worker.

### What it shows

Bar chart of OECD countries ranked by *how many hours of work to earn $1,000 (PPP-adjusted)*. Highlights from the list:

- **Highest hours required (least time-efficient):** Colombia 86, Mexico 78, Greece 60, Costa Rica 53, Hungary 51, Chile 51
- **Median band:** Czechia 48, Slovakia 47, Portugal 45, Poland 43, Estonia 42, Latvia 38, South Korea 38, Türkiye 37, Israel 34, Italy 34, **Japan 34**, Spain 30
- **Sub-30 (most time-efficient):** New Zealand 28, Ireland 27, Slovenia 27, Finland 25, Canada 25, France 25, UK 24, Sweden 24, Australia 23, **US 22**, Belgium 21, Germany 20, Austria 20, Denmark 19, Netherlands 19, Norway 19, Switzerland 18, Iceland 16, **Luxembourg 16**

5.4× spread between Luxembourg (16h) and Colombia (86h) for the same purchasing-power-adjusted thousand dollars.

### Why this matters for SLIC

**Thailand is not OECD-member, so it's absent from this chart** — but that absence is the SLIC opportunity. SLIC could compute Thailand's equivalent figure using the same OECD methodology (Thai annual wages ÷ Thai annual working hours, PPP-adjusted) and surface where Thailand sits on this scale. Best guess: Thailand probably falls between Mexico (78) and Colombia (86) given PPP-adjusted wage levels — that's the SLIC tile that lands.

This metric is the **purest possible livability indicator** because it collapses two variables (wage, work hours) into one (time-cost of money). It is the closest thing to a *single number that says how livable a country is from the perspective of a working person*.

### Integration recommendation — a 3-dimensional livability surface

With this input, SLIC's livability scoring now has three orthogonal axes from three different inputs:

| Axis | Source | What it measures |
|---|---|---|
| **Wealth concentration** | Most-billionaires chart (filed earlier today) | Tail-of-distribution economic gravity |
| **Demographic optimism** | UN WPP 2024 population curve (`shared-inputs/2026-06-20/`) | Whether people are betting on the future |
| **Time-cost of money** | OECD hours-for-$1000 chart (this input) | How efficiently a working life converts to material returns |

A **3D radar / spider chart per city** on the SLIC dashboard would let mayors compare cities across all three axes at once. The interesting cities are the ones with imbalances:

- High wealth concentration + low birth rate + high time-cost = **wealth-extractive, future-thin, hard to live in** (much of CIS, parts of LatAm)
- High wealth concentration + low birth rate + low time-cost = **wealthy plateau, declining future** (Switzerland, Japan, Luxembourg, the Nordics)
- Low wealth concentration + high birth rate + high time-cost = **young, poor, working hard** (much of Africa, parts of South Asia)
- Bangkok's profile against this 3D space is the SLIC-distinctive analysis: probably **medium wealth concentration, low-and-falling birth rate, high time-cost** — the *wealthy-plateau-without-the-wealth* corner, which is uniquely informative for Thai policy stakeholders.

### Cross-references

- Same SLIC integration shape as the prior two inputs — pick what fits v3's current state, don't over-build
- The OECD methodology can be reused to compute the Thailand number Horizon-style: a small backend script that pulls Thai wage + work-hours data from NSO or Bank of Thailand, divides, adjusts for PPP using World Bank data, and outputs the comparable number. That's a 1-hour task for the SLIC code-task to ship.
- Pairs with [[Horizon AI Platform]] M3 (purpose-based assessment): hours-to-earn-$1000 is exactly the kind of *single revealing metric* the M3 module argues vanity dashboards never compute.

---

## Fifth SLIC input added 2026-06-20 — "Europe's Biggest Economic Centers" (Visual Capitalist / Voronoi)

**Image:** `europe-biggest-economic-centers-voronoi-2026.png`
**Source on the chart:** Voronoi / Visual Capitalist, citing Eurostat + Office for National Statistics. **2021 GDP in current prices via NUTS-2 region** (note: the data is 4–5 years old at time of filing — still the best comparable cross-country dataset Europe publishes).

### What it shows

Top-20 European NUTS-2 regions by Regional GDP, mapped geographically plus listed numerically:

| Rank | Region | GDP (€B) |
|---|---|---|
| 1 | **Île-de-France** (Greater Paris) | 866 |
| 2 | **Lombardy** (Milan) | 721 |
| 3 | **Upper Bavaria** (Munich) | 507 |
| 4 | Eastern Midlands | 358 |
| 5 | Community of Madrid | 316 |
| 6 | Catalonia (Barcelona) | 308 |
| 7 | Rhône-Alpes (Lyon) | 298 |
| 8 | Stockholm | 281 |
| 9 | Düsseldorf | 270 |
| 10 | Darmstadt (Frankfurt area) | 267 |
| 11–20 | Lazio, North Holland, Köln, Berlin, Région Sud, Andalusia, Tuscany, etc. | 150–260 range |

**Headline insight on the chart:** the **"Blue Banana"** — the corridor of European industry and population density that hosts **over half of the top 20 regions** (London → Amsterdam → Rhine → Milan).

### Why this matters for SLIC v3 — a 5th axis + the corridor lens

This is the **fifth axis** the SLIC dashboard can score on, complementing today's four (wealth concentration / demographic optimism / time-cost of money / constraint conversion):

**Axis 5: economic-corridor membership** — does this city sit inside a megalopolitan economic corridor, or in geographic isolation?

The Blue Banana is the canonical example for Europe. Asia has its own corridor candidates the SLIC dashboard could surface for Thai-context comparison:

- **Pan-Asian East Coast Corridor** — Tokyo / Yokohama → Seoul → Shanghai → Hong Kong → Shenzhen / Pearl River Delta → Singapore
- **South Asian corridor** — Mumbai / Pune → Bangalore → Hyderabad → Chennai
- **ASEAN mainland corridor** — Bangkok / EEC → Phnom Penh → Ho Chi Minh City

**Bangkok's positioning:** sits inside the ASEAN-mainland corridor but at its western anchor — analogous to Milan's position at the southern end of the Blue Banana. Both are *gateway cities* between a developed economic corridor and the periphery. SLIC could surface Bangkok's role as the *EEC + Eastern Economic Corridor + Thailand-Cambodia-Vietnam gateway* as a positive frame, not a negative one.

### Integration recommendation

Three additions to v3:

1. **Corridor-membership tile** — for any selected city, show which economic corridor (if any) it belongs to, the corridor's total GDP, and the city's role inside the corridor (anchor / midpoint / gateway / periphery).
2. **Cross-continental comparator** — let SLIC users compare Bangkok against any European NUTS-2 region by GDP. Concrete framings the dashboard would enable: *"Bangkok's metro-area GDP vs Lombardy"* or *"the EEC corridor vs the Blue Banana"*.
3. **Megalopolis-formation indicator** — track the *change* in corridor connectivity over time (rail capacity, flight density, freight volume). Cities increasing their corridor connectivity are climbing; cities falling out are stagnating.

### Combined with the four prior axes today

SLIC's livability scoring is now five-dimensional:

| Axis | Source | Bangkok's likely position |
|---|---|---|
| Wealth concentration | billionaire density | medium (#17 globally) |
| Demographic optimism | TFR direction | low-and-falling |
| Time-cost of money | hours for $1000 PPP | high (~80h, est.) |
| Constraint conversion | breakout-pattern membership | moderate / unrealized |
| **Economic-corridor membership** | this input | **ASEAN-mainland corridor, gateway role** |

The 5-axis radar/spider per city is now the SLIC City Profile. Bangkok's profile becomes *"wealthy-plateau-without-the-wealth, but with corridor-gateway potential"* — a more nuanced and actionable diagnosis than any single number.

### Caveat on the data

The chart uses 2021 GDP data. By 2026 the rankings may have shifted (post-pandemic recovery patterns, energy crisis impact, AI-economy regional concentration). Horizon-style EGO-VOID discipline: **note the data vintage on any SLIC tile that uses this dataset, and check for newer NUTS-2 releases before publishing.** Eurostat usually releases NUTS-2 GDP with a 2-3 year lag, so 2023 numbers should be available by mid-2026.

### Cross-references

- **Same Voronoi / Visual Capitalist publisher** as the billionaires chart (input 1 of SLIC today) and the hours-for-$1000 chart (input 3 today). The publisher is becoming Horizon's de-facto open-data source — worth noting in the methodology section of any SLIC research paper.
- **Pairs with the constraint-conversion input** (LinkedIn — Zhao) — the Blue Banana cities all sit in *the opposite* of constraint (wealthy, dense, well-connected). The constraint-conversion question for SLIC becomes: which non-corridor cities are converting their constraints to compete with the corridor anchor cities?

---

## Sixth SLIC input added 2026-06-20 — Thai FDI 2026 surge: 73% YoY increase

**Source:** The Nation Thailand article. **Hard verifiable data** from the Department of Business Development (กรมพัฒนาธุรกิจการค้า), Ministry of Commerce, reported by Director-General **Poonpong Naiyanapakorn** in his capacity as secretary of the Foreign Business Committee. Hashtags: `#TheNationThailand #TheNation #investment #economy`.

### What the data shows

| Metric | Value |
|---|---|
| **Period** | January–May 2026 (first 5 months) |
| **Approved foreign investors** | **528** |
| **Total investment value** | **฿153.56 billion** (~US$4.4B at June 2026 FX) |
| **YoY change** | **+73%** vs. same period 2025 |
| **Per-investor average** | ~฿291 million (~US$8.3M) — mid-cap, not micro |
| **Legal framework** | Foreign Business Act B.E. 2542 (1999) — *direct foreign business establishments, NOT BOI-promoted investments which are a separate stream* |

### Why this matters for SLIC v3 — the 6th axis

Adds **Axis 6: Capital Attraction Velocity** — the YoY change in foreign investment approvals + total value. This is the *most directly verifiable* axis SLIC has — the Department of Business Development publishes this data monthly with full investor counts and totals, cleanly comparable across years.

**Bangkok's likely profile** (assuming most FBA-approved investors land in the BMR + EEC corridor): a sharp positive signal on the velocity axis. This is the **first axis today on which Bangkok / Thailand looks unambiguously strong**. Combined with the other 5 axes:

| Axis | Source | Bangkok's position |
|---|---|---|
| Wealth concentration | billionaire density | medium (#17 globally) |
| Demographic optimism | TFR direction | low-and-falling |
| Time-cost of money | hours-for-$1000 PPP | high (~80h, est.) |
| Constraint conversion | breakout-pattern | moderate / unrealized |
| Economic-corridor membership | Europe NUTS-2 comparator | ASEAN-mainland corridor gateway |
| **Capital attraction velocity** | this input | **+73% YoY — strong-positive** |

The composite picture: *wealthy-plateau-without-the-wealth + low-fertility + high-time-cost + moderate-constraint-conversion + corridor-gateway role* — **but with sharp foreign-investment momentum.** That's actually a *promising* profile: a place that's not yet wealthy and faces demographic headwinds, but is currently winning the capital-attraction race in its region. The investment surge is the *forward-looking* signal that may eventually correct the other axes.

### Integration recommendation — three additions to v3

1. **"Capital Attraction Velocity" tile** — YoY % change in FBA approvals + total value, refreshed monthly from the DBD's public data feed. Becomes a SLIC live-data integration (not a one-time scrape). The DBD publishes the data in Thai-language PDF + a portal; SLIC should script the pull.

2. **Per-investor average size** — derives from (total value ÷ investor count). For Thailand 2026 = ฿291M per investor. For comparison cities, SLIC could pull equivalent: Singapore's EDB-approved investors, Vietnam's MPI-approved investors, Indonesia's BKPM-approved investors. **A "where do the medium-sized fish swim?" map** of ASEAN.

3. **Geographic concentration overlay** — when the DBD releases per-investor location data, map FDI approvals onto Thailand by province. Likely heavy concentration on BMR + EEC corridor. **Compare to the Europe Blue Banana map (5th input today)** — Thailand's FDI map is the *emerging* version of Europe's mature corridor map. SLIC could surface that visual analogy directly.

### Cross-references

- **Pairs with the billionaire-density input** (1st SLIC today) — FDI is the *flow* that becomes the billionaire *stock* over decades. The 73% YoY surge is the leading indicator that may shift Bangkok up the global billionaire-density rankings in the 2030s.
- **Pairs with the constraint-conversion input** (4th SLIC today) — Thailand's FDI surge in 2026 is itself a *constraint-conversion* story. The constraint: tariff-uncertainty in US/China, supply-chain de-risking. The conversion: Thailand's geographic + political-stability positioning as the *China+1* / *ASEAN-hub* destination. SLIC could surface FDI velocity AS the empirical proof of constraint conversion working.
- **Pairs with the European-corridor input** (5th SLIC today) — the FDI is likely landing in the ASEAN-mainland corridor, with Thailand's EEC as a strengthening anchor. SLIC could trend the *corridor's collective FDI* over time to track corridor-formation velocity.
- **Caveat on the 73% number** — single-year surges can be base-effect distortions (low 2025 baseline due to political uncertainty in late 2024 / early 2025) rather than structural improvements. SLIC's tile should show *3-year and 5-year* rolling averages alongside the headline YoY to prevent over-reading a one-period number.

### Verification status (EGO-VOID applied)

- ✅ Source named (DBD Director-General Poonpong Naiyanapakorn)
- ✅ Legal framework cited correctly (Foreign Business Act B.E. 2542 / 1999)
- ⚠️ The Nation Thailand article cited but specific URL not captured — Horizon-style EGO-VOID: SLIC's published version should link directly to The Nation Thailand's article and to the DBD's primary data release
- ⚠️ The 73% number should be cross-verified against the DBD's own primary release (the Department publishes monthly figures in Thai). The article is journalism citing the DBD; the DBD is the primary source.
- ⚠️ Currency conversion (~US$4.4B at June 2026 FX) is estimated; verify against current spot rate before publishing.
