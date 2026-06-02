# Artifact — Chonburi Lecture, 2026-05-22 (5 days before this filing)

**Files in this artifact bundle:**

- `2026-05-22-chonburi-lecture-transcript-raw.txt` — full Thai-language transcript with timestamps, 240 lines (recorded during the lecture)
- 14 photos: `2026-05-22-chonburi-lecture-photo-*.jpg` — Non on stage in the **Smart City Officer** jacket (branding visible: **depa · SEIC · UNL FunIT Global**), the audience, the dashboard projected behind him, the Mayor of Chonburi and senior staff in the front row
- `2026-05-22-chonburi-lecture-summary.md` — this file: Non's framing + the AI-cleaned English summary content + cross-references
- (note: filed forward to Day 72 — Phase 6 *The Chonburi / Bangkok / Thailand smart-city work* — because that's the canonical home for client-facing smart-city lecture content)

---

## Non's framing (verbatim)

> Here is a lecture that I gave just last week in Chonburi. It was an anniversary of my being the advisor to the mayor in Smart City Promotion, so I got to see the mayor many times during the festival time of Buffalo racing when he hosted me for the first time there. So I'm giving you both a transcript in Thai and the cleanup version that one of the AI did, which might help you here.

The lecture is **the customer-facing version of the work the Chonburi AlphaEarth pilot is the production version of.** What Non shows on stage is a working dashboard; what the AlphaEarth code-task is building is the same dashboard with embedding-based change detection layered on top.

---

## What this artifact establishes for the first time on the record: the depa / SEIC / UNL FunIT Global affiliation

The photos show Non in a **Smart City Officer** jacket whose branding is **depa · SEIC · UNL FunIT Global**. This resolves the open question hanging over the earlier UNL trial (the dashboard work that ended with the UNL CTO's sales-funnel response and Non's decision to rebuild on free OSS):

- **depa** = Digital Economy Promotion Agency (Thai government, MDES)
- **SEIC** = Smart Economy & Industry Center (depa unit)
- **UNL FunIT Global** = UNL is an ecosystem partner inside that program

Meaning: Non was not a UNL *customer evaluating a vendor at arm's length*. He is an **officially badged Smart City Officer inside the depa/SEIC program**, and UNL is one of the tools that program supplies him with. The trial-and-reject-and-rebuild move was therefore an *ecosystem-internal quality call* — a senior practitioner inside the program telling depa/SEIC, by walking, that the vendor tooling isn't good enough for the bespoke dashboards he ships. That is a different and more politically loaded thing than "consultant tries SaaS, doesn't like it." Worth remembering when reading any future UNL/depa correspondence.

---

## The lecture — distilled (from the raw Thai transcript and the AI-cleaned English summary)

### 1. Opening: Digital Twin demo (00:00 – 00:09)

Walks on stage and immediately puts up a **Digital Twin of Chonburi** — satellite imagery, 3D buildings, news feed, Facebook feed, traffic. Says he built the whole thing in about **45 minutes**. Pulls satellite imagery directly from **NASA, JAXA (Japan), ISRO (India)** — points out that any country that launches a satellite is obligated by treaty to share imagery on request, but agencies don't advertise this because they don't want the requests. He asked. He got the imagery. The image updates every 24 hours; slightly fresher than Google's.

The dashboard pulls news about Chonburi and the city's own Facebook posts side-by-side, and runs an AI in the back to detect whether what the city says matches what citizens are saying. Then layers: tides (10-year historical baseline for fishermen), fish piers, fish markets, EEC corridor relations, vulnerable-population mapping (echoes the **Nakhon Si Thammarat** work — knowing where the dependent population lives, who's flood-risk-adjacent, who's closest to which hospital).

Honest admission to the Mayor: *"I guessed at about 40% of what Chonburi actually needs. The other 60% I don't know yet because I'm an outsider. My job is to come learn what the city actually needs and fill in that 60%."*

### 2. Chulalongkorn 3D map (~09:00 – 12:00)

Switches to a **Chulalongkorn University** dashboard — same Digital Twin pattern but he has insider knowledge ("I used to teach there, I used to live nearby on Ratchadamri"). Traffic-jam intersections, building energy, **underground utility layer** built by photographing a hundred-year-old blueprint that he was afraid to touch ("I just took a photo. Then told the AI 'this corner is Siam Square, that corner is MBK' — it geo-aligned the rest itself"). Switches between 2D bright-mode and 3D — says he has about **100 dashboards to show today** and invites everyone to pick one to take home and learn to extend.

### 3. NSP — National Streaming Platform (~09:34 – 14:00)

*"I don't watch TV. But I got a new brief: build a national streaming platform — like Netflix but for every Thai TV channel."* Demos the same NSP that's been in code-task all week: every channel previewable, the killer feature being a **zero-cost national Early Warning System** — when there's a tsunami or flood, every channel switches to the alert simultaneously; when the alert ends, every channel returns to its own programming. Compares cost: LINE broadcast costs ~7 satang per message × tens of thousands of citizens, becomes real money. The NSP EWS costs **zero per broadcast** because it rides the same infrastructure people are already watching for free. Adds the accessibility mode for low-vision users.

### 4. Phuket war room (~14:00 – 17:00)

Phuket governor's dashboard: real-time traffic, accident hotspots, satellite layers, news layer, weather/storm tracking. Used during the floods earlier this year. Same pattern — multi-source data layered onto a single map view, designed for a single executive to read in under 30 seconds.

### 5. The grief-built Dao De Jing platform (~17:00 – 19:00)

Brief mention of the **Dao De Jing teaching platform** he built for a friend whose mother was dying (the same artifact discussed at the TKC workshop five days later, on 2026-05-27 — cross-reference Day 71). Used here as an example of *what a 45-minute build looks like when it has to actually carry weight.*

### 6. The 4P framework — the core IP of the lecture (~19:00 – 28:00)

Hand-drawn on the board (the same pattern as the 4C at TKC — invented live, not pulled from a slide):

- **Purpose** — what is the city actually trying to do? Not "be smart" — that's not a purpose. Reduce flood-recovery time? Get the dependent-population census working? Cut emergency-response latency by a factor of two?
- **Practical** — can this be done with the budget, the staff, the political timeline? If a 20-million-baht national platform would normally only buy a feasibility study, *the practical answer is to build the prototype first and write the TOR around it*. (Same ninja-pencil principle he runs at TKC.)
- **Proof** — show the working thing. Not slides about the working thing. The thing.
- **People** — the system has to be operable by the people who are already there. If a dashboard requires a PhD to maintain, the city will abandon it the day Non leaves.

The 4P is the **smart-city consulting methodology**. It is *distinct from* the TKC 4C (Compensation / Cause / Community / Career — employee-experience layer) and *distinct from* the TKC G/D/U/C (Growth / Delivery / Utilization / Communication — org-outcome layer). Three different four-element frameworks in Non's working vocabulary, each for a different stratum:

| Framework | Layer | Audience | Source |
|---|---|---|---|
| **4P** Purpose / Practical / Proof / People | smart-city methodology | mayors, city executives, depa | Chonburi lecture 2026-05-22 |
| **4C** Compensation / Cause / Community / Career | employee experience | mid-career employees in matrix orgs | TKC workshop 2026-05-27 |
| **G/D/U/C** Growth / Delivery / Utilization / Communication | org-side outcome metrics | C-suite, board | TKC matrix-org deck |

### 7. Failed smart-city case studies (~28:00 – 36:00)

Walks through what *doesn't* work, by name:

- **Chinese ghost cities** — built without the Purpose layer; built because the budget existed
- **Songdo, South Korea** — built without the People layer; technologically beautiful, socially empty
- **Nusantara, Indonesia** — built without the Practical layer; the political timeline doesn't survive the construction timeline
- **Masdar, UAE** — built without the Proof layer; the promised carbon-neutrality never materialized in operation
- **Ulaanbaatar 5G** — built without the Purpose layer; "we have 5G" is not a city problem
- **Singapore bike-sharing** — built without the People layer; the operational behavior of actual cyclists wasn't designed for

Each one mapped back to which P was missing. This is the rhetorical move that makes the 4P work in a Thai municipal-government audience: it doesn't say *don't try*, it says *here's how to know when you're about to fail*.

### 8. Nakhon Si Thammarat as proof-of-method (~36:00 – 44:00)

The case study that anchors the whole lecture. Over four years (the years Non has been advising Mayor Ganop):

- **LINE bot for citizen complaint intake** — instead of going to city hall, citizens send a photo to a LINE bot
- **Purple-dot mapping** — every complaint becomes a geo-located dot; the dashboard shows the dots aging from purple→red as they remain unresolved
- **Resolution time: 68 hours → 42 hours** — measured, not estimated
- **Annual reports: ~300 → ~10,000** — citizens reported 30× more issues because the friction collapsed (this is the data point that *closes* every smart-city skeptic in the room)
- **International recognition** — the awards Non mentions in the opening line ("ได้รับรางวัลเยอะมากจากทั่วโลก") are these

The Nakhon Si Thammarat dashboard is the canonical example of what the 4P produces when all four are present. The Chonburi work is the attempt to repeat that pattern in a different geography.

### 9. Satit Phadung Witya school — AR/VR case (~44:00 – 50:00)

A school-level smart deployment: AR/VR teaching tools, but framed by Purpose first — *what learning outcome is this for?* — rather than starting from the tech. Used as a counter-example to "we bought VR headsets, now what?" deployments that fail the Purpose test.

### 10. City ranking dashboard (~50:00 – 56:00)

Demo of a **city-ranking dashboard** — every Thai municipality scored on smart-city readiness across the 4P. Chonburi scored **39.5 / 100** at time of the lecture. Non shows the breakdown: where Chonburi is strong (Purpose alignment with the Mayor's term), where it's weak (People — operator capacity inside the city staff). The ranking isn't punitive; it's diagnostic. The Mayor's response (in the front row) is the political payoff — he can show his cabinet *where exactly* to invest the next year's smart-city budget.

### 11. Closing: the 100-dashboard offer (~56:00 – end)

Closes with the same offer he closed the TKC workshop with five days later: *each person in the room picks one dashboard, I'll teach you to extend it, you take it home and ship something in a month.* The teaching method is the prototype-handoff itself; the lecture isn't the deliverable, the dashboard people leave with is.

---

## Cross-references

### To the **Chonburi AlphaEarth code-task** (active engagement — local_f5ba5cff)

- The dashboard Non demos on stage IS the production target for the AlphaEarth pilot. The pilot's job is to layer embedding-based change detection (64-dim per 10m × 10m per year, 2017→) onto the existing Digital Twin so the Mayor can see *what changed and where* between any two years, not just current state.
- The **40% / 60% gap** Non confessed to on stage is the brief for the next AlphaEarth iteration: the 60% Non doesn't know yet is exactly what the embedding-based change-detection can surface without him having to guess.
- The Nakhon Si Thammarat purple-dot-mapping pattern is the UI precedent — same dot-aging visual language should carry into the Chonburi AlphaEarth surface.

### To the **TKC code-task** (active engagement — local_2391dc11)

- The **4P framework** is transferable methodology. The TKC game-manual currently centers the 4C and the G/D/U/C. The 4P is the *outside-in* version — useful when the TKC product team needs to evaluate a candidate engagement (*does this project have all four P's? if not, which one is missing, and can we add it?*). Worth a section in the manual.
- The **ninja-pencil / 45-minute prototype / build-first-write-TOR-around-it** principle is the same principle in both rooms. Same DNA, different audience. TKC's manual should reflect this is not TKC-specific tradecraft — it's how Non works everywhere.
- The **failed-smart-city case studies** (Songdo, Nusantara, Masdar, etc.) are a teaching pattern TKC teams could repurpose for *failed-product case studies* — same "diagnose which P was missing" rhetorical move.

### To the **100daysofnon project** (Phase 6 — current obsessions, Day 72)

- **Smart City Officer affiliation** (depa · SEIC · UNL FunIT Global) is now on the record — answers the implicit question of "what gives Non standing to walk into a mayor's office and demand 45 minutes."
- **Four-years-in with Mayor Ganop / Nakhon Si Thammarat** is the *track record* that lets him claim the Chonburi engagement. Cross-reference Day 71 (TKC workshop), where the same Mayor Ganop / Tommy / lawsuit footnote surfaced.
- **The buffalo-racing-festival origin** of the Chonburi relationship is the human anchor — the political relationship started over hosting, not over a procurement document. That's the texture worth preserving for Phase 6.

---

## Note on photo provenance

All 14 photos are from the **2026-05-22 Chonburi lecture**. The Smart City Officer jacket appears in multiple shots — branding is legible on the chest. The Mayor of Chonburi is identifiable in front-row shots. Other figures in the room (audience, senior city staff) are not individually identified in this artifact and should be treated as third parties under the Phase-4-style consent gate if any future use surfaces them by name.
