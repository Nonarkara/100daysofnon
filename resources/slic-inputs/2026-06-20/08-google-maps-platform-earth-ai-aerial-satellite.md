# SLIC Input 08 — Google Maps Platform: Earth AI now offers Aerial + Satellite Insights

**Source:** Google Maps Platform LinkedIn post (verified, 52,385 followers, "Promoted"). Mirror of Horizon Input 55. Shortlink: **https://goo.gle/4ubyHov**. Hashtags: `#GoogleMapsPlatform #GeospatialAI #DataDriven #TechInnovation`.

> *"We've expanded our Earth AI imagery portfolio to include Aerial and Satellite Insights. Businesses can now combine high-resolution, bird's-eye views with the ground-level detail of Street View. This makes large-scale planning and regional assessments faster and more accurate than ever. From site selection to asset management, you can now see the bigger picture without losing the fine details."*

## Why this matters for SLIC v3 — geospatial-AI is now a first-class data source

SLIC v3 was designed around a **plug-in data-source architecture** (`design.md §6.7`). Earth AI just shipped exactly the layer SLIC needed: programmatic aerial + satellite + Street View + AI-derived insights for site/region/asset analysis.

The visualization in the post (orange-to-yellow thermal/heat overlay radiating from a central point in a residential/commercial neighborhood) is the *exact shape* of insight SLIC's livability scoring needs to consume — densities, heat-islands, vegetation, flood-risk, all visible at the neighborhood scale.

## Direct SLIC axis impact

| SLIC axis | Earth AI contribution |
|---|---|
| **Geological/climate vulnerability** (already a v3 axis) | Aerial time-series for flood, slope, vegetation, urban-heat-island; longitudinal change detection |
| **Capital attraction velocity** | Google names "site selection" as a flagship use case — direct alignment |
| **Constraint conversion** | Visual proof of whether a constraint zone has been mitigated; bypass the field-visit step |
| **Economic-corridor membership** | Corridor-scale (EEC/NEC/ASEAN) regional scoring becomes substantially cheaper |
| **Demographic optimism** | Aerial detection of new construction, occupancy patterns, infrastructure investment as forward indicators |

## SLIC v3 plug-in implementation pathway

1. **Provisional spec entry:** "Geospatial-AI data source — Google Earth AI (preliminary)" in `design.md §6.7`
2. **API research:** verify what's actually programmatically accessible (the post says "Sign-up at the link above" — pricing, API surface, and Thailand-coverage all need verification)
3. **Comparable layer:** check Sentinel Hub, ESRI Living Atlas, Planet Labs, Maxar as comparable geospatial-AI sources — Earth AI should be one of several candidates evaluated, not a sole-source lock-in
4. **Routing per SPADA:** the actual integration code goes to Codex via Work Order, not me

## Verification flags

- ⚠️ Verify product availability and pricing at https://goo.gle/4ubyHov
- ⚠️ Verify Thailand-coverage quality (Earth AI may be US-first)
- ⚠️ The 52,385 follower count and "Promoted" status are from the social post itself

## Cross-references

- [[brief.md]] master SLIC brief
- Horizon Input 55 (mirror)
- SLIC `design.md §6.7` plug-in data-source architecture
- [[reference_spada_team_architecture_and_my_role]] — integration code routing
