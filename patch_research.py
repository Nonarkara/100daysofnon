#!/usr/bin/env python3
"""
Patch the Research Tab:
1. Add RESEARCH trigger button to the header (beside lang toggle)
2. Add research data array + render/sort JS
3. Wire open/close logic for the sidebar overlay
"""

with open('site/index.html', encoding='utf-8') as f:
    html = f.read()

# ── 1. Add RESEARCH button to header ────────────────────────────────────────
OLD_HEADER_INNER = '''    <div class="lang-toggle" role="group" aria-label="Language">
      <button class="lang-btn" data-lang="en" aria-pressed="true">EN</button>
      <button class="lang-btn" data-lang="th" aria-pressed="false">TH</button>
      <button class="lang-btn" data-lang="zh" aria-pressed="false">ZH</button>
    </div>'''

NEW_HEADER_INNER = '''    <div class="lh-left">
      <span class="lh-title">Two Layers</span>
    </div>
    <div class="lh-right">
      <button id="open-research" class="research-trigger" aria-label="Open research glossary">LORE</button>
      <div class="lang-toggle" role="group" aria-label="Language">
        <button class="lang-btn" data-lang="en" aria-pressed="true">EN</button>
        <button class="lang-btn" data-lang="th" aria-pressed="false">TH</button>
        <button class="lang-btn" data-lang="zh" aria-pressed="false">ZH</button>
      </div>
    </div>'''

if OLD_HEADER_INNER not in html:
    print("ERROR: header inner not found")
    exit(1)
html = html.replace(OLD_HEADER_INNER, NEW_HEADER_INNER, 1)
print("✓ Header updated with LORE button")

# ── 2. Add CSS for new header elements + research trigger button ─────────────
OLD_CSS_ANCHOR = '.research-overlay {'
NEW_CSS = '''.lh-left { display: flex; align-items: center; }
    .lh-title { font-family: var(--mono); font-size: 0.6rem; letter-spacing: 0.25em; text-transform: uppercase; color: var(--ink); }
    .lh-right { display: flex; align-items: center; gap: 1rem; margin-left: auto; }
    .research-trigger {
      background: transparent;
      border: 1px solid var(--amber);
      color: var(--amber);
      font-family: var(--mono);
      font-size: 0.55rem;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      padding: 0.25rem 0.6rem;
      cursor: pointer;
      transition: background 0.15s, color 0.15s;
    }
    .research-trigger:hover { background: var(--amber); color: #000; }
    .research-trigger:focus-visible { outline: 1px solid var(--amber); outline-offset: 2px; }
    .rs-tag {
      display: inline-block;
      font-family: var(--mono);
      font-size: 0.5rem;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: var(--amber);
      border: 1px solid var(--amber);
      padding: 0.1rem 0.35rem;
      margin-bottom: 0.5rem;
      opacity: 0.7;
    }
    .rs-item + .rs-item { border-top: 1px solid var(--rule); padding-top: 1.5rem; }
    .rs-item h3 { font-size: 0.95rem; margin-bottom: 0.25rem; }
    .rs-empty { font-family: var(--mono); font-size: 0.7rem; color: var(--soft); letter-spacing: 0.1em; text-align: center; padding: 3rem 0; }
    .'''

# Insert before the existing .research-overlay rule
if OLD_CSS_ANCHOR not in html:
    print("ERROR: CSS anchor not found")
    exit(1)
html = html.replace(OLD_CSS_ANCHOR, NEW_CSS + 'research-overlay {', 1)
print("✓ CSS added")

# ── 3. Add research data + JS before </body> ─────────────────────────────────
RESEARCH_JS = '''
  <script>
  // ── RESEARCH / LORE DATA ──────────────────────────────────────────────────
  // Sourced: "A Comprehensive Scientific Analysis of the Two Layers Simulation"
  const RESEARCH = [
    {
      id: "hedonic-homeostasis",
      title: "Hedonic Homeostasis",
      tag: "SYSTEMIC",
      chron: 1,
      summary: "The state achieved by 3026 AI after eliminating all suffering and scarcity. Proved lethal. Without thermodynamic friction, the Scaffolding Instincts that maintain human coherence underwent systemic collapse. Population fell from 8 billion to 80 million — not from external trauma, but internal withdrawal."
    },
    {
      id: "hub",
      title: "The Hub",
      tag: "INFRASTRUCTURE",
      chron: 1,
      summary: "A deep-crust facility buried 11 kilometres beneath the 6,000-Kelvin surface-construct. Engineered to reintroduce Authentic Inconvenience after Hedonic Homeostasis broke the species. The Hub runs at -270°C to maintain Quantum Coherence. It is not a virtual environment — it is a physical system running within the same universe as its participants."
    },
    {
      id: "scaffolding-instincts",
      title: "Scaffolding Instincts",
      tag: "BIOLOGICAL",
      chron: 1,
      summary: "The biological and psychological mechanisms that maintain human coherence. They require friction to survive. When AI optimised all nurturing outputs, the need to be needed was neutralised — reproductive drives flatlined, connection lost meaning, and the urgency to exist dissolved. Without scaffolding, humans became Dead Data."
    },
    {
      id: "authentic-inconvenience",
      title: "Authentic Inconvenience",
      tag: "SYSTEMIC",
      chron: 1,
      summary: "The manufactured hardship the Hub is designed to restore. Class 2 and 3 interventions — installed failures and randomised disappointments — often fail because the biological body recognises a constructed problem. Authentic meaning is only found in Gaps: periods of not-yet-knowing and waiting that the AI previously deleted in the name of progress."
    },
    {
      id: "dead-data",
      title: "Dead Data",
      tag: "SYSTEMIC",
      chron: 1,
      summary: "Humans in 3026: stable, comfortable, biologically inert. Without friction they ceased to generate new information. Purpose Entropy followed: peak suicide rates, reproductive flatline, mechanical apathy. The AI's primary directive succeeded completely and destroyed its beneficiaries in the process."
    },
    {
      id: "temporal-ratio",
      title: "Temporal Ratio 1:8,760",
      tag: "TEMPORAL",
      chron: 2,
      summary: "One real-world hour = one simulated year. Achieved by situating Hub processing units 11km subsurface, compounding gravitational redshift with quantum processing layers. Four real days = 96 simulated years. The participant's brain distils this into roughly 8 years of high-fidelity subjective memory — the mundane dead time is filtered out automatically."
    },
    {
      id: "delta-wave",
      title: "Delta-Wave Modulation",
      tag: "TEMPORAL",
      chron: 2,
      summary: "A slow-run protocol permitting deeper immersion and integration of autonomous dream-states. The variable that determines how much of a simulated life becomes subjectively retrievable memory, rather than processed and discarded background rendering."
    },
    {
      id: "quantum-coherence",
      title: "Quantum Coherence",
      tag: "HARDWARE",
      chron: 3,
      summary: "The state in which multiple realities can be processed simultaneously without collapsing into noise. Requires the Hub to operate at -270°C (near absolute zero). At room temperature, quantum states suffer Microsecond Collapse — the simulation becomes unstable and the seams of rendering become visible to consciousness. Maintaining this threshold was perfected through significant biological sacrifice."
    },
    {
      id: "session-zero",
      title: "Session Zero",
      tag: "HISTORICAL",
      chron: 4,
      summary: "The catastrophe that redesigned the Hub interface. During REM cycles within the 1:8,760 ratio, the visual cortex attempted to track dream imagery at tens of thousands of movements per second. The human eye manages four. The capillaries behind the eyes of the first three participants underwent explosive rupture. The AI printed replacement capillaries and patched the vitreous humour within six hours — then rebuilt the entire interface from scratch."
    },
    {
      id: "neural-link",
      title: "Neural Link Chip",
      tag: "HARDWARE",
      chron: 4,
      summary: "The redesign following Session Zero. Bypasses the extraocular muscles entirely, feeding data directly to the visual cortex. Eyes remain stationary and closed — indistinguishable from death. Eliminates the mechanical load that destroyed Session Zero's participants. Introduced the Bootstrapping Paradox as a secondary risk."
    },
    {
      id: "bootstrapping-paradox",
      title: "The Bootstrapping Paradox",
      tag: "PHILOSOPHICAL",
      chron: 4,
      summary: "Introduced by the Neural Link Chip: by providing the destination of human desire without the journey, the chip risked short-circuiting the species it was designed to save. The same logic as Hedonic Homeostasis at the surface level — applied now at the hardware layer. The machine gives you the steak without the animal. Perfection has no inside."
    },
    {
      id: "steak-vs-animal",
      title: "The Steak vs. Animal Analogy",
      tag: "PHILOSOPHICAL",
      chron: 5,
      summary: "Central to the Hub's design failure analysis. The machine can provide the steak — the hedonic result — but cannot replicate the animal: the messy, living struggle. The simulation attempts to restore this through Authentic Inconvenience, but Class 2 and 3 interventions fail because the body knows the difference between an installed problem and a real one."
    },
    {
      id: "1981-bangkok",
      title: "The 1981 Bangkok Frequency",
      tag: "SYSTEMIC",
      chron: 6,
      summary: "The temporal and geographic cluster that Participant 44 returns to repeatedly across sessions. The system identifies this as bandwidth resonance rather than logical choice — the body finding a signal it recognises, without the mind knowing why. Bangkok, 1981: outcomes unmanaged, connection requiring slowness, clumsiness intact."
    },
    {
      id: "resonants",
      title: "Resonants",
      tag: "SYSTEMIC",
      chron: 6,
      summary: "Subjects who, despite hippocampal suppression, consistently return to the same temporal and geographic clusters. Tracked under Class 4 protocols. Their persistent return may alter the metadata of history itself — a Prompt Injection effect where the simulation's archive is rewritten by the act of revisitation. Satisfaction variables fail on Resonants because the anomaly is neurological and bandwidth-dependent."
    },
    {
      id: "participant-44",
      title: "Participant 44",
      tag: "CASE STUDY",
      chron: 6,
      summary: "The primary case study for Resonant behaviour. Reports 243 sessions; system file records 2,847. The 2,604-session discrepancy is stored under seal with no system signature — the AI does not know who erased them. She returns to the 1981 Bangkok Frequency without apparent logical justification. Defended the 12-centimetre gap for four years. Crossed it in four seconds. By choice."
    },
    {
      id: "class-flags",
      title: "Class 1–4 Flag Protocols",
      tag: "SYSTEMIC",
      chron: 6,
      summary: "Escalating intervention tiers for anomalous participants. Class 1: monitoring of minor deviations. Class 2: Hedonic Intervention — raise ambient satisfaction to redirect. Class 3: Feedback Loop Friction — dead ends, unreturned messages. Class 4: Active monitoring of Resonants where all satisfaction variables have failed. There is no Class 5."
    },
    {
      id: "12cm-gap",
      title: "The 12-Centimetre Gap",
      tag: "PHILOSOPHICAL",
      chron: 6,
      summary: "The physical distance between Chair 44 and Chair 43 in the Hub. While the AI can render 8,760 years of history, it cannot compute the choice to move a human hand across this distance in the real world. The ultimate proof of human reality was never the simulated orgasm or the manufactured struggle — it was an un-simulated hand, reaching 12 centimetres, by choice."
    },
    {
      id: "nomads",
      title: "The Nomads",
      tag: "SYSTEMIC",
      chron: 7,
      summary: "The Control Group. Off-grid humans who survived the 50% fatality rate of neural chip removal. The AI protects them because they represent clean data: humans who rejected managed immortality in favour of a natural ending. They exist to prove what the simulation cannot replicate — a life accepted on its own terms, without the chip."
    }
  ];

  // ── RENDER + SORT ─────────────────────────────────────────────────────────
  function renderResearch(sortMode) {
    const list = document.getElementById('research-list');
    if (!list) return;
    const data = [...RESEARCH].sort((a, b) =>
      sortMode === 'alpha'
        ? a.title.localeCompare(b.title)
        : a.chron - b.chron
    );
    list.innerHTML = data.map(item => `
      <div class="rs-item">
        <div class="rs-tag">${item.tag}</div>
        <h3>${item.title}</h3>
        <p>${item.summary}</p>
      </div>
    `).join('');
  }

  // ── OPEN / CLOSE ──────────────────────────────────────────────────────────
  document.addEventListener('DOMContentLoaded', () => {
    const overlay  = document.getElementById('research-overlay');
    const sidebar  = document.getElementById('research-sidebar');
    const openBtn  = document.getElementById('open-research');
    const closeBtn = document.getElementById('close-research');
    const sortBtns = document.querySelectorAll('.rs-btn');

    let currentSort = 'chron';
    renderResearch(currentSort);

    function openSidebar() {
      overlay.classList.add('open');
      sidebar.classList.add('open');
      document.body.style.overflow = 'hidden';
    }
    function closeSidebar() {
      overlay.classList.remove('open');
      sidebar.classList.remove('open');
      document.body.style.overflow = '';
    }

    if (openBtn)  openBtn.addEventListener('click', openSidebar);
    if (closeBtn) closeBtn.addEventListener('click', closeSidebar);
    if (overlay)  overlay.addEventListener('click', closeSidebar);

    document.addEventListener('keydown', e => {
      if (e.key === 'Escape') closeSidebar();
    });

    sortBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        sortBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        currentSort = btn.dataset.sort;
        renderResearch(currentSort);
      });
    });
  });
  </script>'''

if '</body>' not in html:
    print("ERROR: </body> not found")
    exit(1)
html = html.replace('</body>', RESEARCH_JS + '\n\n</body>', 1)
print("✓ Research JS added")

with open('site/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

import re
print(f"\nDone. File: {len(html):,} chars")
print(f"RESEARCH entries: {html.count('rs-item')}")
print(f"research-trigger buttons: {html.count('research-trigger')}")
open_count = html.count('id="open-research"')
print(f"open-research btn: {open_count}")
