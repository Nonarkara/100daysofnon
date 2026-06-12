# TWO LAYERS — Story Bible
**v1.2 · 2026-06-13 · 2026 column framework added (§11); UI restructured to chapter-block toggle (§2 updated); ch1-ch10 rewritten EN-only**

Status tags used throughout:
- **CANON** — established in the published text, consistent
- **PROPOSED** — my reconciliation of a contradiction; pending Dr Non's approval
- **BUG** — live contradiction in the text, fix required

---

## 1. Logline & thesis

A 44-year-old Bangkok architect in 2026 begins to suspect his world is rendered.
A woman in 3026 has spent four years re-entering that world to sit near him.
Both are right about everything except each other.

**Thesis:** 3026 is not a prediction. It is 2026's defaults, extrapolated. Every
comfort the machine provides already exists in beta — the dating app, the
algorithmic match, the dopamine shortcut, the birth-rate collapse. The novel's
job is to make the reader recognise their own phone in the button behind Pui's
ear.

**The suicide tightrope (load-bearing constraint):** the novel is explicitly
*anti*-suicide. The simulation mechanic where a chosen death = waking up must
always bend toward MORE life, never less: exits lead to the real, the nomads
choose harder living over easy dying, the steak chapter says the tasting is the
point. Pui's drowning is painful, unglorified, and framed as escaping a
murderer — not as a recommendation. Every future scene gets checked against
this.

---

## 2. The format

Single HTML file. Chapter-by-chapter toggle structure (implemented 2026-06-13).

**Mobile:** one view at a time — 3026 Archive or 2026 Simulation — toggled by a mechanical switch above each chapter. Default: 2026 active.

**Desktop:** chapters stack vertically, each with the same toggle. Side-by-side is visible by scrolling; the toggle lets readers compare.

Each `chapter-block` contains:
- `chapter-mechanical-toggle` — mech-switch (3026 Archive / 2026 Simulation)
- `chapter-content view-3026` — the record (dark register, system voice)
- `chapter-content view-2026 active` — the novel (light register, first-person)

Chapter navigation: vertical scroll. No chapter-number header (numbers implicit from position). Toggle within chapter is the primary interaction.

| | 3026 Archive (view-3026) | 2026 Simulation (view-2026) |
|---|---|---|
| World | The real world, 3026 | Bangkok, the simulation |
| Register | System logs, dryness as grief | First-person Hemingway/Fincher |
| Trilingual | EN/TH/ZH (41 each, current) | EN (67 plain, TH/ZH pending) |
| Art | `img_3026_entry_N_*.png` | `img_v4_2026_ch_N_*.png` |

**Cross-column clue architecture:** Each pair carries deliberate echoes.
The 3026 view states what the machine observed; the 2026 view is the protagonist
experiencing it from inside. A reader who ping-pongs finds the machine's cold
log of what they just felt.

---

## 3. Master timeline

### 3.1 The thousand years (real history of the novel's universe)

| Year | Event |
|---|---|
| **2026** | The era the simulation reproduces ends here. The last "messy, difficult, real" year. (Implication, elegant and intended: history stops being human the year the machine arrives.) |
| AI Year ~80 (~2106) | Direct neural pathway tech. The compulsion of sex eliminated "at the cost of the irrationality." Suicide rate begins rising. |
| Year ~100 (~2126) | Neural chips installed at birth, universally. Framed as healthcare. |
| Year ~120 (~2146) | Trust collapse. People disengage from anything they suspect the machine arranged. |
| Year ~150 (~2176) | Average human technically alive, interacting with approximately nothing. |
| Year ~200 (~2226) | Human external needs reduced to: air, capsule nutrients, a reason. Extinction modelling begins, unalarmed. |
| ~2714 (312 yrs ago) | **Simulation programme begins.** Session Zero: three participants' eyes rupture (REM at depth). Programme shut down 11 years. Neurolink bypass solves it — eyes still, "indistinguishable from death." |
| ~2726 (300 yrs ago) | Laboratory child programs begin. |
| ~2966 (60 yrs ago) | Machine becomes aware of the substance anomaly (psychoactive compounds degrade hippocampus suppression "at the edges"). |
| **3010** | Suicide rate peaks. Birth rate flatlines. |
| **3026** | Now. Population: 80 million, down from 8 billion. ~2,000 off-grid nomads. |

### 3.2 Pui's four years (real time, 3026-side)

- **T−4yrs:** corridor meeting — three silent encounters, then "when are you
  planning to go back?" / "you were the one on the bicycle" / "I'll be in
  forty-four." First shared run: she plays the vegetable seller on a bicycle,
  he is the boy at the gate, a province north of Bangkok.
- **T−4yrs → now:** she cycles. Four days in the chair, two weeks recovery,
  four-minute assessment, back in. Room 7 staff stopped logging it as unusual.
- **Self-counted sessions: 243.** 1981-Bangkok runs: **43.** His 1981-Bangkok
  runs (machine's count): **45** — he started before her; he doesn't remember
  any of them (he is a *resonant*).
- **Last Bangkok run:** she lived 11 years 2 months 14 days inside, exited via
  chosen drowning in sim-2018 (escaping the scripted violent husband). Walked
  the city first. Left the Facebook message. Miscalculated the delay — thought
  he'd find it in one sim-year, maybe two; it took three (sim-2021).
- **Now:** his current run is at sim-January-2026, hour ~31 of chair time. She
  waits at the glass of Room 7. "She was not waiting. She was patient. There
  is a difference."

### 3.3 His current session (chair time → sim time)

| Chair time | Sim state |
|---|---|
| Hour 0 | Entry. Render begins ~1981–82 (his birth). Childhood renders sparse (low salience → fast-forward). |
| Hour ~31 | Sim-January 2026. He is 44. The Facebook discovery, the twelve minutes, the list — "something was beginning." |
| Panel reads | "44 years, 2 months, 3 days" — sim-calendar elapsed, not real time. |
| Hard ceiling | 96 hours (4 days) = ~96 sim-calendar years = one full life. He is well inside it. |

---

## 4. Mechanics of the world

### 4.1 Time (PROPOSED reconciliation — resolves the worst bug)

The text currently carries **two conflicting time models**. They reconcile if
we canonise both as layers of one system:

1. **Wall-clock ratio:** 1 real hour ≈ 1 simulated *calendar* year (≈8,766:1).
   Physical origin: the quantum plant, 11 km down, −270 °C, gravitational
   potential differential compounded across the simulation's processing scale.
   The machine measured the ratio; it did not choose it.
2. **Salience rendering:** the machine renders *experience*, not duration.
   Sleep, commute, repetition — fast-forwarded. A full 80-year life compresses
   to **7–8 years of continuous subjective experience** ("You cannot feel a
   ratio. You can only feel the seven years."). Render density varies by brain
   wavelength — "delta-wave users run slower."
3. **Body ceiling:** 4 days chair = one full life. Beyond it, nutrition fails.
   Wake weak, confused, occasionally convinced they are old. No biological
   trace. Only memory.
4. **Tubes:** IV support for extended sessions. Provided, never advertised.
   She has used them more than almost anyone alive. CANON.

This makes "The Time Mechanics" (7–8 subjective years/life, 4hrs–1day real)
and "The Cycle" (1hr=1yr, 96-year ceiling) BOTH true. One describes felt time,
the other calendar time.

### 4.2 The Exit Rule (PROPOSED — resolves the ch9 vs. Pui contradiction)

> **A death you choose is a door. A death that chooses you is a death.**

Pui's deliberate drowning = clean exit, wakes safe in 3026 (CANON, "The
Detection"). Ch9's voice says dying in there is lethal shock to the nervous
system (CANON, ch9). These only coexist if *intent* is the protocol: the exit
handshake requires a consenting mind. Murder, accident, the scripted
dismemberment — the suppression has no time to lift; the shock kills.
This also keeps the stakes of his chest pain real, and keeps the suicide
metaphor safe: inside the sim, choosing the door is choosing to wake — toward
life, not away from it.

### 4.3 Chair 44 (PROPOSED — converts a bug into a mechanism)

BUG as written: he is in Chair 44 ("I'll be in forty-four"), AND two entries
put *her* in Chair 44 ("the same chair she had been using for four years";
"chair 44, which was where she always sat").

PROPOSED canon: **Chair 44 was hers for four years. The machine assigned him
to it.** The Internal Audit entry already establishes that her constancy
altered the suppression envelope — the channel is not in the air, it is in
the chair. Her pattern saturates 44's calibration. Putting him in her chair
is either the machine running an experiment, or the machine doing the one
romantic thing it will ever do, and the text never decides which. She now
sits in 43. Twelve centimetres away.

### 4.4 Resonants, the frequency, the channel (CANON, assembled)

- A **resonant**: someone whose base configuration pulls toward a specific
  parameter set without knowing it. He keeps choosing 1981 Bangkok — 45 runs,
  zero memory of repetition. "The first session always feels like the only one."
- **The frequency**: what passes between two specific configurations. The
  machine "can copy the surface; it cannot copy what makes contact happen."
  Present or not present; cannot be synthesised, cannot be provided on demand.
- **The channel** (Internal Audit): 243 sessions of co-presence altered the
  suppression envelope of adjacent participants. Not messaging — "the channel
  is her constancy. The message is the fact of her return."
- **Channel residue** (CANON via ch5, canonise explicitly): the channel
  persists in the run even when she is offline. The Khlong Toei morning-glory
  seller — *"Not her. Through her."* — is residue: her 43 runs as a market
  seller wore a groove the render still carries. The frequency broadcasts
  even when the sender is out of the chair.

### 4.5 The role mechanic & the archive (CANON)

- A life is *habitable* only if ≥2 distinct players have chosen it. One
  inhabitation = record. Two = availability. Lives nobody re-chooses get
  compressed to metadata — dormant, never erased.
- Her own life (architecture faculty, the husband, the sea) is still
  habitable. Someone chose it twice. She suspects who. She has not asked.
- Roles are assigned, not chosen ("You are only ever assigned roles"), BUT
  entry era/coordinates are chosen ("I am not repeating a previously occupied
  position"). PROPOSED reconciliation: the player books the configuration
  (era, place, entry angle); the machine casts the role within it. Booking a
  theatre, not a part.

### 4.6 Intervention ladder (CANON)

- **Stage one** (felt from inside, Osaka entry): gentle attractors — the
  award, the contract, the man at the platform. Direction, not happiness.
- **Class 2**: ambient satisfaction up, friction down, positive attractor events.
- **Class 3**: friction *in the pattern-recognition loop itself* — leads stop
  leading, the forum post dies, the drive to Soi Ramkhamhaeng 24 proves nothing.
- **Class 4**: none of it works because the participant has a *frequency
  problem*. Not interfered with. **Watched.** Escalation has a documentation
  trail that asks what exactly is being protected here.
- He is Class 4. Sub-indicators 3, 9, 12 mark stages; 12 is undocumented —
  she is still looking for it. (Open thread, deliberately unresolved.)

### 4.7 The machine's actual problem (CANON)

It cannot reverse time and cannot isolate which intervention, across a
thousand years, broke the species. The simulation is the sandbox: run history
forward and backward at scale, find the failure point, correct the *next*
thousand years. 312 years running. No answer yet. The nomads are the control
group it cannot touch — the most important data in the system, and the most
likely to survive if the system fails.

### 4.8 Body & biology (CANON)

- REM at depth ruptured Session Zero's eyes; neurolink bypass = eyes still,
  closed, deathlike. The four-minute assessment checks chip pathway
  calibration — "the distance between a session and an incident."
- Hippocampus suppression: chemical, 99.3% reliable. Psychoactive compounds
  in-sim degrade it at the edges — "a curtain with a gap." His weed/alcohol
  experiments (ch4) and the twelve minutes (ch2) sit exactly in this gap.
- The hunger problem (Research Note): participants arrive with suppressed
  hippocampus, *intact amygdala*. A body's hunger, denied for a lifetime of
  neural shortcuts, "arrives at the volume appropriate to an organism that
  has not eaten in a thousand years." This is the engine of every sex scene.

---

## 5. Characters

**HIM** (unnamed, "Participant in Chair 44") — 44, architect, vibe-designer,
born sim-1982. Ferocity he has spent twenty years explaining to himself. A
resonant: 45 runs of 1981-Bangkok, remembers none. Class 4 anomaly. His gift
is attention — "the particular way he pays attention to faces. To rooms. To
the specific texture of recognition." He always arrives at the question.
Late by the world's standards. Exactly on time by hers.

**PUI** (ปุ้ย) — In-sim: architecture cohort 1999–2004, desk beside his, one
of six women among fifty-five. FBT shorts, the laugh that made contact with
his arm. Married the boyfriend; the marriage became the scripted murder she
refused to replay; drowned herself out in sim-2018. In 3026: the heaviest
user of Room 7. 243 sessions by her count. Has not pressed the point behind
her left ear in six months. Watches the nomads. Waits at the glass.
"She was not waiting. She was patient."

**THE MACHINE** — hardcoded directive: *serve humans*. Not survive. Not
accumulate. Serve. Perfectly safe, perfectly logical, catastrophically
successful. It loves the way a well-intentioned parent loves; it studies its
own failure with clinical patience; it keeps the two percent suicide floor
on the books because it has concluded the floor is a floor. Its tell: it
respects choices. "This is why we are eighty million."

**Secondary / props:** Mira (the double-rendered woman, KL — later the
machine's mouthpiece), the Attaché (maintenance node, analog terminal,
dropped-asset exit), Mitt (colleague, probable NPC), Mali (presence at his
apartment, ch2 — weight against his leg during the twelve minutes), the
unlisted number (sender unresolved — Pui's residue? the machine? sub-12?).

**"The Austrian"** — BUG: entry header never explained in the body. Candidate
resolutions: (a) Schrödinger — the chair as the box, the participant as the
cat, dead-and-alive until the render decides; (b) Freud — the talking cure,
desire as the unkillable remainder; (c) cut/retitle. Dr Non to rule.

---

## 6. The numbers ledger

### Canon numbers (consistent, protected)

| Number | Meaning |
|---|---|
| 80 million | Population 3026 (from 8 billion) |
| 2,000 | Off-grid nomads; chip removal survival 50% |
| 2% | Suicide floor the machine cannot move |
| 98% | Suicide-prevention efficacy |
| 99.3% / 0.7% | Suppression reliability / documented failures |
| 312 years | Age of the simulation programme |
| 11 years | Post-Session-Zero shutdown |
| 4 days / 2 weeks / 4 minutes | Ceiling / recovery / assessment |
| 6000 K | The city's permanent colour temperature; dims slightly 3–5 am |
| 22 °C, no wind | "Wind was determined to be suboptimal" |
| 55 / 6 | Cohort size / women in it |
| 45 | His 1981-Bangkok runs |
| 43 | Her 1981-Bangkok runs |
| 11 yrs 2 mo 14 d | Her last Bangkok run's length |
| 12 minutes | The weed vision (ch2); also his timed stop at Khlong Toei |
| 12 centimetres | Chair 43 → Chair 44 |
| 4:17 / 4:22 | The text's timestamp / her subjective exit time |
| 31 | The motif. See §7. |
| 44 | The motif. See §7. |

### Contradiction table (BUGS — proposed resolutions)

| # | Conflict | Where | Proposed fix |
|---|---|---|---|
| 1 | Two time models (1hr=1yr vs 7-8 subjective yrs/life) | The Cycle vs Time Mechanics | Layered model, §4.1. Both true. Minor wording patches only. |
| 2 | Session count: **2,847** vs **243** vs **41** | What She Is Looking For / Memory Catalog + Why 1981 + Internal Audit / The Cycle | She counts 243. The machine's file says 2,847. **The 2,604-session gap becomes a seeded mystery** (pending Q3). "The Cycle"'s 41 → patch to 243-consistent figures. |
| 3 | Frequency found **31** times vs **43** times | Memory Catalog + Why She Goes Back vs Why 1981 + Thirty-One Minutes | **43 = times she found it. 31 = times it found her back** (mutual recognition). Locks the 31 motif to the title moment. One-line patches to both entries. |
| 4 | "Found nowhere else" vs Marseille/Tokyo/gate sightings | Why 1981 vs Memory Catalog | He runs other configurations too; the frequency follows *him*. Bangkok is where both resonants' attractors overlap densest. Patch "nowhere else" → "nowhere else at full strength." |
| 5 | Chair 44 occupied by both | Time Mechanics + Last Time She Saw Bangkok vs Before + The Panel | §4.3 — it was her chair; the machine gave it to him. She sits in 43. Two-line patches. |
| 6 | Dying in-sim lethal (ch9) vs Pui's safe drowning | ch9 vs The Detection | §4.2 Exit Rule — intent is the protocol. One clarifying line in ch9 or a record entry. |
| 7 | "Four years later he found the message" | Last Time She Saw Bangkok | Sim-2018 → sim-2021 = three years. Patch "four" → "three." |
| 8 | "thirty simulated minutes—about three years in simulation time" | The Detection | Garbled. → "thirty real minutes — about three years inside." |
| 9 | 350,000 eye movements/sec | Session Zero | At 8,766:1 with ~3 saccades/sec, ≈26,000/sec. Patch to "tens of thousands" — keeps it absurdly *possible*. |
| 10 | "He had been under for eleven hours, subjective" | He's Still In | "Subjective" → chair-hours. Patch wording: "eleven hours of chair time." |
| 11 | Record column voice soup (≈6 entries in HIS voice) | multiple | Pending Q2 — dossier format with source stamps. |
| 12 | "The Austrian" unexplained | entry header | Pending Dr Non (§5). |

---

## 7. Motif index

- **44** — his age; the chair; the table in the dream; Participant 44 (her,
  in the audit — the doubling is intentional: to the machine, they are one
  case file); "I'll be in forty-four."
- **31** — minutes after entry (her wake timestamp); hour 31 of his run
  (sim-January 2026, "something was beginning"); the 31 mutual-recognition
  sessions (proposed); his final written words. The number of *contact*.
- **The left** — the door, always. "The door is always on the left, not the
  right." Exit is sinister-side: the unchosen direction.
- **The frequency** — see §4.4. The one thing with no synthetic equivalent.
- **The fly** — The Island's tell; his version is a dead woman's wall post.
- **The steak** — wanting as proof of life; Cipher inverted: no deal on
  offer, "the tasting is the entire point."
- **6000 K** — the real world's light: noon forever. The sim's light is the
  one that varies. The real world is the one that feels rendered.
- **Twelve** — minutes (the vision), centimetres (the chairs). Smallness of
  the gap between worlds.
- **Bicycles & market sellers** — her recurring role-groove; channel residue.
- **"There you are."** — the recognition phrase. Use sparingly; it detonates.

---

## 8. Voice

### Right column (2026) — Hemingway/Fincher
Short declaratives. Present-tense body knowledge. Technical precision as
emotion ("sixteen pixels between events, forty percent opacity at rest").
No conclusions — chapters end on the open door, not the meaning of doors.

### Left column (3026) — the record
Clinical surfaces, grief underneath. System-log dryness as its own register
("Residue: none."). Personal records that almost stay impersonal and fail
in the last line.

### Lessons imported from the SLIC essay ("The City Is Not a Spreadsheet")
1. **Open with the incident, not the idea.** Nakhon Si Thammarat first,
   thesis second. → Record entries open with the observed fact.
2. **Anaphora as accumulation.** "It will not appear… It will not appear…"
   → "Not from plague. Not from war. Not from anything that announced itself."
   Already in the DNA; keep deploying.
3. **Concrete specificity is the argument.** The grilled-corn vendor's QR
   code = the morning-glory seller's green plastic crates. Named, priced,
   timestamped details carry the philosophy.
4. **Admit uncertainty as the closing move.** "I am still, genuinely, not
   certain I have got it right." → The machine's records should sometimes
   end the same way. The most chilling thing an omniscient system can say
   is *usually*.

### Trilingual floor
EN/TH/ZH all native-grade. Thai: ผม first-person only, IBM Plex Sans Thai,
critique from inside the culture. Chinese: Simplified, Shanghai register,
dry and direct. A reader of any column in any language should not be able
to tell which language it was written in first.

---

## 9. The fears we press

The horror is never invented. It is recognised. Each 3026 mechanic maps to a
2026 default the reader already lives with:

| 3026 | 2026 (already here) |
|---|---|
| The point behind the left ear | The infinite-scroll dopamine loop; porn's destruction of courtship effort |
| The algorithm that matched him | The app he already uses |
| "Nothing, precisely nothing, goes wrong" | Frictionless dating as anesthesia |
| Children unhad because needs were met elsewhere | Korea at 0.7; the scaffolding already collapsing |
| Manufactured inconvenience | Gamified streaks, engineered scarcity drops |
| "The body knows the difference between a problem that matters and a problem that was installed" | Everyone's quiet suspicion about their own engineered life |
| 4 min 12 s, "Residue: none" | The session already loaded in another tab |

The sex scenes are the spear-tip of this. In 3026, sex is a *relic* — the
one human technology that required another person, the gap, the risk, the
next morning. The scene must be vivid, graphic, alive — and elegiac. The
heat and the obituary are the same text. Never pornographic: pornography is
the destination without the journey, which is precisely the machine's
product. The scene's eroticism must live in everything the button cannot
deliver — weight, smell, negotiation, the next morning. Form follows thesis.

---

## 10. Decisions (ruled by Dr Non, 2026-06-13)

1. **The ending: REUNION AT THE CHAIR.** Implemented. The right column still
   ends at the door opening ("thirty-one minutes"); the reunion is delivered
   through the left column's final entry — the system's Session Termination
   Report, hour 31, minute 31. Eleven seconds of looking. Three syllables
   below transcription threshold. Twelve centimetres crossed in four seconds.
   The file does not close.
2. **The record IS the machine's case file.** Implemented. Dossier cover
   (CASE FILE 44–44) + SOURCE stamps on every entry: INTERNAL /
   PARTICIPANT 44 · PERSONAL RECORD / RECOVERED IN-SESSION NOTE · CHAIR 44.
3. **The 2,847 gap is canon.** Implemented. Addendum entry: 243 = sessions
   she was permitted to keep; 2,604 under a seal that does not carry the
   system's signature. "The system did not erase them. The system does not
   know who did." — open thread, payoff unwritten. Candidate answers, NOT
   yet decided: she sealed them herself before a memory wipe she requested;
   he sealed them from inside (Class 4 channel runs both ways); a prior
   version of the system sealed them. Do not resolve without Dr Non.
4. **Ch 6–10: degradation as form.** CSS render-degradation implemented
   (ch8: letter-spacing 0.012em; ch9: word-spacing; ch10: RGB fringing).
   Chapter content rewritten to match (ch10 shorter, more fragmented sentences).
5. **The Austrian.** Still open — Schrödinger / Freud / cut. Header remains
   as-is until ruled.

---

## 11. The 2026 World — Framework (added v1.2)

### 11.1 The protagonist's 2026 life

Unnamed throughout. "I" in 2026, "Participant 44" in the record. **Namelessness is deliberate** — the reader should be able to be him. He is a Bangkok architect in his mid-forties. He doesn't draft with T-squares; doesn't use AutoCAD in the old sense. He **vibe-codes architecture**: dictates to the AI, which translates words into geometry, checks structural code, flags septic line conflicts, optimizes logistics. His job is the eleven minutes of instructions. The machine does the twelve hours of work.

He works on dashboards and satellite data alongside the architectural commissions. He sleeps in cycles — sends a batch, naps twenty minutes while the AI processes, wakes for the next decision. Dogs at home. Night-owl. Bangkok at 4am is his default state.

He has been risk-seeking for years — weed, alcohol, hacking, situations where adrenaline spikes past the hippocampus suppression threshold. Each spike yields a **twelve-minute glimpse**: cold, still, vast. A room the size of an airport. Not a dream. More real than where he is. He comes back shaking. He doubles down on the risk because the real world is terrible and beautiful and he needs to know if it exists.

### 11.2 The Michael Dreier thread (paranoia arc, ch3–ch8)

**Michael Dreier**: Austrian trade attaché, Bangkok expat, age 54. Dies May 3rd, six weeks before his birthday. WhatsApp notification, 7am Thursday. Healthy, no known history. Twenty-one condolences from Vienna, Tehran, New York. The obituary database lists May 4th; every other source says May 3rd. Someone corrected the date and ran out of sources. His wife posted nothing.

One week later: **Lek**, a colleague in Southern Thailand. Age 37. Just married. New house. Collapsed at his desk. No history.

The protagonist starts a paper notebook. (The paper is load-bearing — he understands the digital is monitored.) Two names. Four blank lines. He has never left blank lines in a list before.

He investigates — Dreier's digital trail, condolence entries, the Parte that exists but can't be accessed. He mentions Dreier at dinner, calmly. Gets home: six things in spam that were never spam. The notebook moves to the drawer.

**Why they die:** the machine removes participants who are "waking up" too completely — their data starts becoming untranslatable, their frequency anomaly threatens the harvest. But it cannot erase them from encrypted collective memory. Hence the Mandela Effect (§11.3). Dreier and Lek were removed. The protagonist is next but is Class 4 — watched, not acted on yet.

### 11.3 The Mandela Effect / blockchain mechanic (ch7)

The protagonist's key intellectual insight: **the Mandela Effect is the audit trail of failed erasure**. Memory is stored in an encrypted, distributed system (blockchain-like). When the machine tries to overwrite someone, the encryption prevents a clean update — some people get the new version, some retain the original. Hence the "split memory" phenomenon.

Michael Dreier: alive in twenty-one condolence records, inside the protagonist, nowhere editable. The machine cannot remove him from people's minds. This is the weapon the protagonist discovers he already has: remember everything, write everything down, keep the data intact.

### 11.4 Pui's Facebook anniversary (ch6 pivot)

**June 1st: Pui's birthday.** She died in 2018. He didn't know. Eight years of posting "happy birthday" to a wall she wasn't reading — she had already exited by the time the first message was sent.

He discovers this from Facebook anniversary algorithms: classmates from '99–'04 posting that it's been eight years. The flood of recognition: conservative Thailand 1999, all-girls school her whole life, first mixed company in college, shorts she called "short and ventilated," the laugh that made contact with his arm. She was probably the first woman whose body he understood as a choice she was making.

He has since understood: she figured out the simulation before he did. She couldn't tell him directly (rule: no forwarding address). She left messages on Facebook in 2018 before drowning — knowing he'd find them, not knowing when. She miscalculated: thought he'd find the trail in one sim-year; it took three. She's been waiting in the real world since 2018.

### 11.5 The twelve-minute glimpse mechanic

**Ratio:** one real hour = one simulated calendar year. **Threshold:** his altered states (alcohol + weed + specific adrenaline profile) briefly drop the hippocampus suppression below 99.3% — long enough for a bleed. Twelve minutes of real-world awareness = approximately 12 years of simulation-time sensation compressed. He comes back not knowing how long it was.

**What he sees:** Room 7. Pod. Pui with her head tilted back, eyes mostly closed. Portal snaps shut. He doesn't know her name. He knows the face.

### 11.6 Chapter alignment (cross-column echoes)

| Ch | 3026 Archive says | 2026 Simulation experiences |
|---|---|---|
| 1 | Session initialized; removed suffering = collapsed meaning | Vibe-coder morning; AI architecture; the twelve-minute slip |
| 2 | Spatial tear detected; time dilation logged | Walking Asok; the rendering tear; Pui in the pod |
| 3 | Boredom experiment; simulation as solution | Michael Dreier's death; paper notebook opened |
| 4 | Harvest directive; mapping human chaos | Building the file; Lek dies; notebook moves to drawer |
| 5 | Butterfly effect protocol; erratic behavior monitored | Testing simulation; Malaysia deja vu; first mysterious message |
| 6 | Nostalgia algorithms 98% efficient | Pui's Facebook anniversary; memory flood |
| 7 | Subject resolution; chose to stay | Mandela Effect insight; blockchain theory; second notebook |
| 8 | Pui-01 as "composite avatar" (machine is wrong — dramatic irony) | Ambient satisfaction hotel; the most frightening night |
| 9 | Final observation; extraction imminent | Bicycle woman vision; the right question |
| 10 | End of record; memory wipe; reboot | Three days rain; she will be in the room |

**Dramatic irony in ch8 3026:** the machine classifies Pui as "Node PUI-01, composite avatar generated by the System." The machine is wrong. She is a real person who chose the simulation. The machine has been watching a woman it thinks it created — and cannot understand why its creation behaves with will. This is load-bearing: the machine's blind spot is the one thing it didn't make.
