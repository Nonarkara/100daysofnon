# Football-project seed — Non's opening vision monologue (2026-07-17)

**Origin:** Non 2026-07-17, unprompted extended reflection. Opened with *"I'm probably going to be doing some kind of games or spreadsheet dashboard at some time about [soccer] because I'd be obsessed with it for a long, long time. So let me explain it to you."* (Voice-typo *"software"* → *"soccer"* in the opening; the whole monologue is about football strategy.)

**Filed as an inaugural seed for a future project.** Not immediately actionable; parked for when Non is ready to pick it up. Same shape as [[project_photo_search_app_backlog]] memory — surface when context invites, not on a timer.

## Non's actual vision — captured verbatim-adjacent, structural

### The core intellectual frame

*Soccer as a human-in-the-loop algorithm* with three layers stacked:

1. **Geometric territorial optimization** — 11 players spread across the field, each with a coverage bubble; bubbles must not overlap too much or long balls slip through; clustering defenders without understanding opponent-winger speed loses
2. **Probabilistic matchup calculations** — you compose your XI as attribute-numbers-per-position; opponent composes theirs; probability of a scoring event resolves against the composition
3. **Irrational-human-genius wildcard** — real players (Maradona, Messi, Owen, Mo Salah) *break the algorithm* by producing outputs the position-attribute model cannot predict. *"Human skills could be somehow irrational, illogical, but actually get you away from the trouble with obstacles."*

### The synthesis Non named

**Pep Guardiola's geometric sets moving forward as the current-era canonical instance** — *"his players form certain geometrical sets and then just keep moving forward with that, and at a certain point there's a mistake done by the other side, you get to score."*

Non's frame explains WHY Pep works: it operationalizes layers 1 (geometry) and 2 (matchup composition) so consistently that layer 3 (opponent human error) becomes the *primary* scoring mechanism. Non is essentially describing xG-plus-pass-network-plus-Voronoi analytics at the intuitive layer, before the buzzwords.

### The offside argument — architectural

**Why offside exists** in Non's framing: without it, soccer collapses to *"basketball — everybody just tries to score as many as possible without defending at all. Boring."* The offside rule creates a *territorial constraint that forces strategy back into the game*. Non's reading is that rules exist to *slow* things down so that layer-1 (geometry) and layer-2 (matchup) matter — otherwise layer-3 (star-player-speed) trivially wins.

**This is a first-principles design insight, not a soccer opinion.** Any game or dashboard Non builds should treat rule-constraints as first-class design decisions, not annoyances.

## Non's roster preferences — the design-taste signal

**AC Milan is Non's heart-team, specifically the late-90s / early-00s era.** The lineup Non named:

- **GK:** Dida
- **DEF:** Maldini, Nesta, sometimes trading in Cannavaro to keep three-of-them-on-one-team
- **RB:** **Christian Panucci** — Non's *cult pick*, named as *"the Charles Barkley of wingback... the most versatile, most trustworthy, definitely most efficient... he was not really that recognized. But to me, he's the most versatile, most trustworthy, and definitely most efficient"*
- **MID:** Rui Costa (must be there), + Kaka / Zaccheroni-era players, + **Ambrosini** — Non named him as *"another one who was like Panucci — very versatile, someone who follows instruction really carefully"*
- **ST:** **Filippo Inzaghi** — Non's *favorite striker of all time*, along with **Michael Owen**

### The design-taste signal — this is the important part

Non named **Panucci and Ambrosini together** as his archetype: **versatile + reliable + instruction-following, over flashy**. This is exactly the same design-taste signal that shows up elsewhere in Non's frame:

- **[[Dao Input 09 IC 555]]** — Chapter 11 emptiness-as-usefulness: the chip that does nothing on its own is more useful than the chip with baked-in opinions. Panucci-shape.
- **[[Input 60 Ultraboost Integration Map]]** Tier A picks — *"boring reliable tools that just work"* over the flashy paid alternatives
- **Non's stated coding philosophy** ([[feedback_always_mvp_make_it_exist_first]]): *"make it work now, make it good later"* — instruction-following over flashy
- **[[user_non_near_death_operator_hardwiring memory]]**: *"iterate fast, ship fast, but airtight cybersecurity/UX/database"* — the Panucci frame at operator scale

**Non's players are his design system.** The football project, when it ships, will inherit this design-taste explicitly.

### Championship Manager as Non's algorithm-teacher

*"I learned so much about algorithm from Championship Manager, especially 95, 98, 2000. But it gets better every time until it gets to the point where it gets really complicated. Like, you really literally have to manage all these dots moving on the screens. I don't want to manage dots. It's not like you're actually looking at the game, and then people are actually playing. You'll get tired."*

**Non named a specific abstraction-level failure mode:** late CM versions moved past the "manage a team" register into "manage raw simulation dots," and Non checked out. **This is a specific product-design constraint for whatever Non builds:** *never require the user to manage the primitive; always maintain the manager-level abstraction.*

Same lesson from [[Input 60]] Tier D skip discipline: *tools that make you do the low-level work when a higher-level abstraction is possible are wrong-tier.*

## The actual product-vision surface — what Non might ship

Non said *"games or spreadsheet dashboard."* Both directions are viable:

### Direction A — A game (Championship-Manager-successor shape)

- Manager-level abstraction preserved (no dot-management)
- Attribute-composition + matchup-probability + irrational-human-genius wildcard baked in
- AC Milan late-90s / early-00s heart-team as playable seed
- Panucci-and-Ambrosini archetype visible in the data model (versatility + reliability weighted alongside star-power)
- Offside + territorial-constraint math visible in the tactical UI

### Direction B — A spreadsheet dashboard

- Ingests real match data (StatsBomb / Opta / Wyscout / Second Spectrum feeds where accessible)
- Renders Voronoi player-coverage overlays, pass-network graphs, expected-threat (xT) heat maps
- The three-layer frame Non named becomes explicit dashboard sections: Geometry / Matchup / Wildcard-Events
- Team-composition experimentation on the fly
- Manager-level abstraction preserved (no dot-management)

**Both directions can leverage today's session's technical stack:**

- **[[Input 60 Ultraboost Map]] Coolify VPS** — self-hosted deployment
- **[[Input 62 GeoLibre]] browser-native mapping** — the pitch is a 2D map; browser-GIS libraries render Voronoi + heat overlays cleanly
- **[[Input 63 turbo-fieldfare]] local LLM** — could power natural-language tactical analysis without cloud upload of possibly-sensitive scouting notes
- **[[Input 65 WanGP]] voice-clone** — Non's already-verified voice-clone workflow could narrate match-analysis videos
- **[[Input 60]] Tier A JANUSTIU Skills** — Designer Skills + Frontend Slides for the interface

**Nothing here needs to be built from scratch.** The stack Non already has can compose this.

## What I will NOT do with this seed

- **Do not push a specific direction.** Non will decide game vs dashboard when he's ready. My job is to preserve the vision + surface the technical-stack fit when he brings it up.
- **Do not treat this as work-in-progress.** No AGENT_NOTES.md, no Codex Work Order, no Antigravity claim. Backlog only.
- **Do not evangelize the analytics-industry ecosystem** (StatsBomb, Opta, etc.) unless Non asks. Those are relevant *when* Non decides Direction B is the path.
- **Do not add football content to Horizon / SLIC / FloodDash briefs unbidden.** This is a separate project when it ships.

## The one design-principle to preserve when this reactivates

**The Panucci-Ambrosini archetype is Non's design system statement.** Whatever the football project becomes, its data model, UI, and default behavior should visibly reward the versatile-reliable-instruction-following player type alongside the flashy-star-player type. Most soccer games and dashboards over-weight stars. Non's would not.

## Cross-references

- [[project_photo_search_app_backlog memory]] — sibling backlog seed with the same *"surface when context invites"* discipline
- [[Dao Input 09 IC 555]] — the emptiness-as-usefulness pattern that maps to Panucci
- [[Input 60 Ultraboost Integration Map]] — the reliable-tools tier discipline that maps to Non's player-taste
- [[feedback_always_mvp_make_it_exist_first]] — the "make it work now" philosophy
- [[user_non_near_death_operator_hardwiring]] — the operator-identity that produces this design-taste
- Championship Manager 1995 / 1998 / 2000 — Non's stated algorithm-teacher; primary intellectual ancestor
- Pep Guardiola's Man City / Barcelona geometric-sets tactical model — Non's stated modern instance
- StatsBomb / Opta / Wyscout / Second Spectrum — the analytics-industry ecosystem when Direction B activates
