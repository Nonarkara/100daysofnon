# Input 62 — Getnotes' GitHub Daily: GeoLibre — browser-based open-source GIS

**Source:** Thai-language *"GitHub Daily — โปรเจกต์เด่นวันนี้"* post by **Getnotes** (Thai content publisher covering trending GitHub projects, similar-shape to [[Input 30 openapps.pro]] + [[Input 38 RAGHub]] + [[Input 42 AI Mastery]] pattern). Hashtags: `#Getnotes #GitHubDaily #GeoLibre #GIS #OpenSource #MapData #Geospatial #DataAnalytics #DeveloperTools #Jupyter`.

## The claim — verbatim capabilities

**GeoLibre** — presented as an open-source browser-native GIS tool:

- Open maps, view + analyze in browser (no install required)
- 2D and 3D area + building visualization
- Layer management + display customization
- Attribute Table view
- **Spatial SQL analysis**
- **Jupyter Notebook integration**
- Native apps for Windows / macOS / Linux / Android
- Map sharing + website-embed
- **Local device processing — no forced cloud upload** (privacy positive)

Target users named in the post: data analysts, map-app developers, researchers/students, real estate + urban planning teams, government agencies, GIS-curious beginners.

**Explicit caveat from the post itself:** *"GeoLibre เป็นโปรเจกต์ใหม่ที่กำลังพัฒนา ฟีเจอร์บางส่วนอาจยังไม่ครบเท่าโปรแกรม GIS รุ่นใหญ่ เช่น QGIS หรือ ArcGIS"* — new project under active development, feature parity with QGIS/ArcGIS not yet claimed.

## ⚠️ Verification flag — the *"GeoLibre"* name specifically needs checking

**I cannot confirm "GeoLibre" from my training data.** It may be:

1. A **real newer OSS project** I have no signal on (plausible — 2025-2026 GIS-in-browser tooling has been active)
2. **A Getnotes-language rendering of an existing project** — possibly [[MapLibre GL JS]] (which is real, an open-source Mapbox GL JS fork widely used) plus a companion editor/analysis layer built on top
3. A **misattribution or spelled variant** of another project

**Do not adopt into Horizon curriculum, Non's stack, or downstream materials until the GitHub repository URL is verified and the current maintainer/license/activity status is checked.** Estimated verification: 5 minutes via WebSearch — happy to run if you say the word.

**The description sounds like an integration of several real components:**
- MapLibre GL JS (base map rendering)
- Something like GeoParquet or DuckDB Spatial (Spatial SQL)
- WASM-based geospatial libs (browser processing)
- JupyterLab extension bridge

If GeoLibre is a real all-in-one wrapper of that stack, it's genuinely valuable. If it's an aspirational description of what such a tool *could* be, it's not shippable.

## Why this matters IF verified — direct relevance to your live stack

Regardless of GeoLibre-the-specific-project's status, **the concept — browser-native, local-processing GIS with no install — is directly relevant to at least three of Non's live projects.** If GeoLibre proves out, adopt it. If not, the same architectural pattern is available via MapLibre GL JS + DuckDB Spatial + a lightweight WebGL layer.

### FloodDash ([[FloodDash WO-01]])

Phase 3 of the FloodDash Work Order calls for a **sensor-map layer on flood.nonarkara.org** rendering ~800 thaiwater.net stations. A browser-native GIS tool is *exactly* the substrate for that — sensors as GeoJSON, colored by `pct_of_alert_threshold`, clickable to per-station detail pages. No heavy JS bundle, no forced-upload of Thai hydro-sensor data to a US cloud service.

### Phuket SMART Bus ([[Phuket Bus WO-01]])

The current `/ops` view's map is squeezed to ~40% width per the mobile-redesign spec. A properly-integrated browser-GIS layer (routes, stops, real-time bus positions, airport-queue heat) would upgrade this from a static thumbnail to an operational tool. Full-width 60vh map on mobile per the WO-01 layout.

### SLIC v3

Every SLIC axis has a GIS underlay — geological/climate vulnerability is literally geospatial; wealth concentration, capital-attraction, demographic optimism all render better as maps than as tables. A SLIC v3 "browse Bangkok by axis" interactive map ships faster on a browser-GIS substrate than on any traditional GIS stack.

## Where this fits in the day's overall pattern

Same pattern as [[Input 30 openapps.pro]], [[Input 38 RAGHub]], [[Input 42 AI Mastery list]], [[Input 52 Stanford CME 295]], [[Input 60 Ultraboost Integration Map]] — **2026 discovery is moving toward expert-curated specialized resources at every layer of depth and audience.** Getnotes' daily-GitHub-spotlight publishing is the Thai-language slot in this pattern.

**Practical Horizon Ultraboost Map update proposed:** GeoLibre (if verified real and healthy) would be a **Tier B** candidate on [[Input 60]] — same tier as n8n / Trigger.dev / Hoppscotch / Speechma. Install-later after Tier A is settled.

## Horizon placements (conditional on verification)

### 1. M6 tools catalog

*"GIS without leaving the browser"* — a card in the specialized-tools section covering GeoLibre + MapLibre GL JS + DuckDB Spatial as an alternative to QGIS/ArcGIS install-heavy workflows.

### 2. M2-B Thai use-case module — real estate + urban planning + government segment

The Getnotes post explicitly names these audiences. Horizon has these audiences in its M2-B target list. A dedicated *"GIS work without an IT department"* lesson lands.

### 3. Pinterest library card

A single card comparing browser-GIS vs desktop-GIS with the *"no install, no cloud upload, works with your Jupyter"* value proposition front-and-center.

## What NOT to do

- ⚠️ **Don't install GeoLibre on the production Coolify VPS ([[Input 60]]) until the GitHub repo, license, and maintainer status are verified.** A GeoLibre with a permissive license (MIT/Apache 2) is fine; a GeoLibre with an AGPL-3 or unknown license might complicate the license discipline your [[feedback_no_localhost_ship_principle]] + hosting-mixed projects imply.
- ⚠️ **Don't build FloodDash phase-3 or SLIC v3 map layers on GeoLibre-specifically without a fallback.** Design for the *pattern* (browser-native GIS with GeoJSON input) so if GeoLibre proves immature, you swap to MapLibre GL JS + a lightweight WebGL layer without a rewrite.
- ⚠️ **Don't cite GeoLibre in any Horizon Research paper without verifying the project's actual status.** Same discipline as the [[SLIC Input 10 — Goldman Korea claim]] flag.

## Cross-references

- [[Input 30 — openapps.pro]] / [[Input 38 — RAGHub]] / [[Input 42 — AI Mastery]] / [[Input 52 — Stanford CME 295]] — the OSS-discovery pattern this input joins
- [[Input 53 — Claude Skills marketplaces]] / [[Input 60 — Ultraboost Integration Map]] — the toolchain integration layer this input might join
- [[FloodDash WO-01]] — the direct-application project for a browser-GIS layer
- [[Phuket Bus WO-01]] — the second direct-application project
- [[SLIC brief.md]] — the third direct-application project (v3 axis maps)
- [[feedback_teach_dont_silently_fix]] — the verification-flag discipline this brief inherits
- [[Mata v. Avianca]] — the cautionary case that argues for repo-verification before adoption
