# SLIC Input 12 — Salary vs Cost of Living in Asia, 4 cities (Numbeo-sourced infographic)

**Source:** Infographic *"Salary vs Cost of Living in Asia — How far does your income actually go?"* citing **Numbeo** at the bottom. Publisher not identified on the image itself.

## The numbers — verbatim

| City | Avg Monthly Salary (USD) | Living Costs (USD) | Rent City Centre (USD) | Rent as % of Salary |
|---|---|---|---|---|
| **Singapore** | $4,291 | $1,135 | $2,691 | **62.7%** |
| **Seoul** | $2,933 | *(not stated)* | $870 | **29.7%** |
| **Tokyo** | $2,622 | *(not stated)* | $1,511 | **57.6%** |
| **Kuala Lumpur** | $1,586 | *(not stated)* | $690 | **43.5%** |
| **Bangkok** | 🚨 **missing** | — | — | — |

**Infographic's own breakdown percentages (Singapore only shows all three):**
- Singapore: 50% salary retained / 26% living costs / 24% rent
- Seoul: 65% salary / 35% rent
- Tokyo: 42% salary / 58% rent
- Kuala Lumpur: 56% salary / 44% rent

**Headline insight (verbatim):** *"High salary ≠ high savings. Singapore earns more… But spends more too."* Bottom footer: *"Rising global costs are shrinking real income."*

## Math check — three green, one yellow, one glitch

| Check | Result |
|---|---|
| Tokyo 58% rent share vs 1511/2622 = 57.6% | 🟢 clean |
| Kuala Lumpur 44% rent share vs 690/1586 = 43.5% | 🟢 clean |
| Seoul 35% rent share vs 870/2933 = 29.7% | 🟡 close but not exact — the 35% likely includes utilities or transport, not just rent |
| Singapore 24% rent share vs 2691/4291 = 62.7% | 🔴 **large discrepancy** — the graphic's *"24% rent + 26% living costs + 50% remainder"* only holds if rent is ~$1,030 (median-across-all-districts), NOT the $2,691 *city-centre* figure it displays. **The graphic is mixing two different rent metrics without labeling.** |

Per [[feedback_teach_dont_silently_fix]]: surfacing the Singapore inconsistency rather than propagating it.

## The gap that matters most for SLIC — Bangkok is missing

**A Salary-vs-Cost-of-Living infographic for Asia that omits Bangkok is a data gap SLIC v3 can plug.** Numbeo has Bangkok data (as it does for most major cities); the infographic's exclusion is editorial, not source-limitation. SLIC v3 should:

1. **Pull the equivalent Bangkok numbers from Numbeo** (avg salary, city-centre rent, living cost index)
2. **Publish a "SLIC v3 Bangkok Contribution" card** that slots Bangkok into this exact comparison table
3. **Analyze what Bangkok's rent-share-of-salary reveals** relative to Seoul (29.7%), KL (43.5%), Tokyo (57.6%), Singapore (62.7%)

**Hypothesized Bangkok positioning:** Bangkok's rent-to-salary ratio likely sits between KL (43.5%) and Tokyo (57.6%) — reflecting Bangkok's dual character as a middle-income capital with premium-district housing costs concentrated in the CBD. SLIC's actual number will refine this hypothesis.

## Direct SLIC v3 axis implications

| SLIC axis | What this input contributes |
|---|---|
| **Time-cost of money** | Fresh cross-Asia comparators; the *hours-to-cover-rent* figure derives directly (e.g., Tokyo worker at $2,622 needs 58% of monthly hours just for rent = every third hour of the month) |
| **Wealth concentration** | Rent-to-salary ratio is a *distribution* signal, not just a level; Singapore's 62.7% city-centre-rent burden means the median worker cannot live in the city centre |
| **Constraint conversion** | Singapore's dual reality (highest salary + highest rent burden) is the *unconverted-constraint* pattern SLIC's axis is named for |
| **Capital attraction velocity** | Cities that require 40%+ of salary for rent create a *retention constraint* on the workforce their capital-attraction depends on; this is worth surfacing as a SLIC v3 metric |
| **Global-index alignment** (new axis proposed in [[Input 09]]) | Numbeo joins Wharton QoL Index as a first-class benchmark source SLIC should cross-reference |

## Direct sciti/SCITI implications (per Non's routing note)

Filed cross-reference at `/Users/nonarkara/Projects/100daysofnon/resources/sciti-inputs/2026-06-20/01-numbeo-asia-salary-vs-cost-of-living.md`. ⚠️ **The "sciti" project folder did not previously exist** — I created it and dropped this input as its first artifact. If *"sciti"* means something specific (Smart City Institute of Thailand? SCITI as an acronym? your teaching identity as ดร.นนท์ — Dr. Non — from the AI-course PDF?), correct me and I'll rename the folder. Not blocking to file it now.

For sciti-adjacent audiences (academic, policy, urban-studies), this input's value is:

- **Comparative housing-cost burden across Asian first-tier cities** — a table any smart-city / urbanism seminar can use
- **The Bangkok data gap** as a research contribution opportunity
- **The Numbeo methodology as a teaching case study** — crowdsourced data has both real signal and real bias; sophisticated audiences should learn to read both

## Verification flags

- ⚠️ Numbeo is crowdsourced. It has real signal (~half a million user contributions globally) and real bias (users skew expat/higher-income). Cite as *directional*, not authoritative. The [[Input 09 — Wharton 2026 QoL Index]] is a stronger academic-grade cross-reference.
- ⚠️ The exact publish date of this infographic is unclear. Cost-of-living data is time-sensitive; if the figures are >12 months stale, they need refresh before publication.
- ⚠️ The Singapore rent-percentage discrepancy noted above means the infographic itself should not be cited as-is; the *underlying Numbeo data* is the citation.

## Cross-references

- [[Input 09 — Wharton 2026 QoL Index]] — academic-grade comparator; Numbeo is crowdsourced complement
- [[Input 10 — Goldman Korea retail margin call]] — Seoul salary $2,933 context helps calibrate what a Korean retail investor was leveraged *against* when the wipe-out came
- [[Input 11 — Mag 7 earnings calendar]] — Tokyo/Seoul/KL/Singapore markets are the ADR-adjacent transmission channels
- [[Plummeting Population brief]] — cost-of-living pressure is a proximate cause of the birthrate collapse across Tokyo/Seoul/Singapore
- [[Bangkok Chao Phraya geological history brief]] — the physical-substrate context for the Bangkok data-gap Numbeo doesn't cover
- [[Jim Carrey grandfather coda]] — the 75-year-old FoodPanda rider is *below* even the Numbeo-median Bangkok respondent
- [[brief.md]] master SLIC brief — add proposed **Bangkok Contribution Card** to Numbeo Asia comparator
- Sciti-inputs mirror: `/Users/nonarkara/Projects/100daysofnon/resources/sciti-inputs/2026-06-20/01-numbeo-asia-salary-vs-cost-of-living.md`
