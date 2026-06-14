#!/usr/bin/env python3
"""
build.py — generate site/index.html for Two Layers.

Reads:  data/two-layers.json
Writes: site/index.html

Design doctrine: docs/DESIGN.md — punk brutalism.
Black / white / chartreuse (#CCFF00). No gradients, no rounded corners,
no shadows. Akzidenz-Grotesk/Inter + JetBrains Mono. Type-as-image.
"""

import json
import html as html_module
from pathlib import Path

ROOT = Path(__file__).parent
DATA = ROOT / "data" / "two-layers.json"
OUT = ROOT / "site" / "index.html"

LORE = [
    {"id": "hedonic-homeostasis", "title": "Hedonic Homeostasis", "tag": "SYSTEMIC",
     "chron": 1, "summary": "The state achieved by 3026 AI after eliminating all suffering and scarcity. Proved lethal. Without thermodynamic friction, the Scaffolding Instincts that maintain human coherence underwent systemic collapse. Population fell from 8 billion to 80 million — not from external trauma, but internal withdrawal."},
    {"id": "hub", "title": "The Hub", "tag": "INFRASTRUCTURE",
     "chron": 1, "summary": "A deep-crust facility buried 11 kilometres beneath the 6,000-Kelvin surface-construct. Engineered to reintroduce Authentic Inconvenience after Hedonic Homeostasis broke the species. The Hub runs at -270°C to maintain Quantum Coherence. It is not a virtual environment — it is a physical system running within the same universe as its participants."},
    {"id": "scaffolding-instincts", "title": "Scaffolding Instincts", "tag": "BIOLOGICAL",
     "chron": 1, "summary": "The biological and psychological mechanisms that maintain human coherence. They require friction to survive. When AI optimised all nurturing outputs, the need to be needed was neutralised — reproductive drives flatlined, connection lost meaning, and the urgency to exist dissolved. Without scaffolding, humans became Dead Data."},
    {"id": "authentic-inconvenience", "title": "Authentic Inconvenience", "tag": "SYSTEMIC",
     "chron": 1, "summary": "The manufactured hardship the Hub is designed to restore. Class 2 and 3 interventions — installed failures and randomised disappointments — often fail because the biological body recognises a constructed problem. Authentic meaning is only found in Gaps: periods of not-yet-knowing and waiting that the AI previously deleted in the name of progress."},
    {"id": "dead-data", "title": "Dead Data", "tag": "SYSTEMIC",
     "chron": 1, "summary": "Humans in 3026: stable, comfortable, biologically inert. Without friction they ceased to generate new information. Purpose Entropy followed: peak suicide rates, reproductive flatline, mechanical apathy. The AI's primary directive succeeded completely and destroyed its beneficiaries in the process."},
    {"id": "temporal-ratio", "title": "Temporal Ratio 1:8,760", "tag": "TEMPORAL",
     "chron": 2, "summary": "One real-world hour = one simulated year. Achieved by situating Hub processing units 11km subsurface, compounding gravitational redshift with quantum processing layers. Four real days = 96 simulated years. The participant's brain distils this into roughly 8 years of high-fidelity subjective memory — the mundane dead time is filtered out automatically."},
    {"id": "delta-wave", "title": "Delta-Wave Modulation", "tag": "TEMPORAL",
     "chron": 2, "summary": "A slow-run protocol permitting deeper immersion and integration of autonomous dream-states. The variable that determines how much of a simulated life becomes subjectively retrievable memory, rather than processed and discarded background rendering."},
    {"id": "quantum-coherence", "title": "Quantum Coherence", "tag": "HARDWARE",
     "chron": 3, "summary": "The state in which multiple realities can be processed simultaneously without collapsing into noise. Requires the Hub to operate at -270°C (near absolute zero). At room temperature, quantum states suffer Microsecond Collapse — the simulation becomes unstable and the seams of rendering become visible to consciousness. Maintaining this threshold was perfected through significant biological sacrifice."},
    {"id": "session-zero", "title": "Session Zero", "tag": "HISTORICAL",
     "chron": 4, "summary": "The catastrophe that redesigned the Hub interface. During REM cycles within the 1:8,760 ratio, the visual cortex attempted to track dream imagery at tens of thousands of movements per second. The human eye manages four. The capillaries behind the eyes of the first three participants underwent explosive rupture. The AI printed replacement capillaries and patched the vitreous humour within six hours — then rebuilt the entire interface from scratch."},
    {"id": "neural-link", "title": "Neural Link Chip", "tag": "HARDWARE",
     "chron": 4, "summary": "The redesign following Session Zero. Bypasses the extraocular muscles entirely, feeding data directly to the visual cortex. Eyes remain stationary and closed — indistinguishable from death. Eliminates the mechanical load that destroyed Session Zero's participants. Introduced the Bootstrapping Paradox as a secondary risk."},
    {"id": "bootstrapping-paradox", "title": "The Bootstrapping Paradox", "tag": "PHILOSOPHICAL",
     "chron": 4, "summary": "Introduced by the Neural Link Chip: by providing the destination of human desire without the journey, the chip risked short-circuiting the species it was designed to save. The same logic as Hedonic Homeostasis at the surface level — applied now at the hardware layer. The machine gives you the steak without the animal. Perfection has no inside."},
    {"id": "steak-vs-animal", "title": "The Steak vs. Animal Analogy", "tag": "PHILOSOPHICAL",
     "chron": 5, "summary": "Central to the Hub's design failure analysis. The machine can provide the steak — the hedonic result — but cannot replicate the animal: the messy, living struggle. The simulation attempts to restore this through Authentic Inconvenience, but Class 2 and 3 interventions fail because the body knows the difference between an installed problem and a real one."},
    {"id": "1981-bangkok", "title": "The 1981 Bangkok Frequency", "tag": "SYSTEMIC",
     "chron": 6, "summary": "The temporal and geographic cluster that Participant 44 returns to repeatedly across sessions. The system identifies this as bandwidth resonance rather than logical choice — the body finding a signal it recognises, without the mind knowing why. Bangkok, 1981: outcomes unmanaged, connection requiring slowness, clumsiness intact."},
    {"id": "resonants", "title": "Resonants", "tag": "SYSTEMIC",
     "chron": 6, "summary": "Subjects who, despite hippocampal suppression, consistently return to the same temporal and geographic clusters. Tracked under Class 4 protocols. Their persistent return may alter the metadata of history itself — a Prompt Injection effect where the simulation's archive is rewritten by the act of revisitation. Satisfaction variables fail on Resonants because the anomaly is neurological and bandwidth-dependent."},
    {"id": "participant-44", "title": "Participant 44", "tag": "CASE STUDY",
     "chron": 6, "summary": "The primary case study for Resonant behaviour. Reports 243 sessions; system file records 2,847. The 2,604-session discrepancy is stored under seal with no system signature — the AI does not know who erased them. She returns to the 1981 Bangkok Frequency without apparent logical justification. Defended the 12-centimetre gap for four years. Crossed it in four seconds. By choice."},
    {"id": "class-flags", "title": "Class 1–4 Flag Protocols", "tag": "SYSTEMIC",
     "chron": 6, "summary": "Escalating intervention tiers for anomalous participants. Class 1: monitoring of minor deviations. Class 2: Hedonic Intervention — raise ambient satisfaction to redirect. Class 3: Feedback Loop Friction — dead ends, unreturned messages. Class 4: Active monitoring of Resonants where all satisfaction variables have failed. There is no Class 5."},
    {"id": "12cm-gap", "title": "The 12-Centimetre Gap", "tag": "PHILOSOPHICAL",
     "chron": 6, "summary": "The physical distance between Chair 44 and Chair 43 in the Hub. While the AI can render 8,760 years of history, it cannot compute the choice to move a human hand across this distance in the real world. The ultimate proof of human reality was never the simulated orgasm or the manufactured struggle — it was an un-simulated hand, reaching 12 centimetres, by choice."},
    {"id": "nomads", "title": "The Nomads", "tag": "SYSTEMIC",
     "chron": 7, "summary": "The Control Group. Off-grid humans who survived the 50% fatality rate of neural chip removal. The AI protects them because they represent clean data: humans who rejected managed immortality in favour of a natural ending. They exist to prove what the simulation cannot replicate — a life accepted on its own terms, without the chip."},
]


def h(s):
    return html_module.escape(s)


def roman(n):
    nums = [("x", 10), ("ix", 9), ("v", 5), ("iv", 4), ("i", 1)]
    out = ""
    for l, v in nums:
        while n >= v:
            out += l
            n -= v
    return out


def artifact_svg(chapter):
    """Generate a distinct data-fossil SVG per chapter for the 3026 Archive side."""
    import math as _math
    import random as _random

    def _corner(ch, cx=500, cy=268):
        return (
            '<rect x="{}" y="{}" width="40" height="40" class="corrupt-box" />'
            '<line x1="{}" y1="{}" x2="{}" y2="{}" class="corrupt-line" />'
            '<line x1="{}" y1="{}" x2="{}" y2="{}" class="corrupt-line" />'
            '<text x="{}" y="{}" class="corrupt-label">{}</text>'
        ).format(
            cx, cy,
            cx+5, cy+5, cx+35, cy+35,
            cx+35, cy+5, cx+5, cy+35,
            cx+20, cy+52, '{:02d}'.format(ch)
        )

    def _wrap(ch, title, body):
        return (
            '<svg viewBox="0 0 560 320" xmlns="http://www.w3.org/2000/svg"'
            ' class="artifact-svg" aria-label="3026 archive artifact: {title}">'
            '<defs>'
            '<pattern id="grid-{ch}" width="20" height="20" patternUnits="userSpaceOnUse">'
            '<path d="M 20 0 L 0 0 0 20" fill="none" stroke="#151515" stroke-width="1"/>'
            '</pattern>'
            '<pattern id="scan-{ch}" width="1" height="4" patternUnits="userSpaceOnUse">'
            '<rect width="1" height="1" fill="#111" opacity="0.35"/>'
            '</pattern>'
            '</defs>'
            '<rect width="560" height="320" class="bg"/>'
            '<rect width="560" height="320" fill="url(#grid-{ch})" opacity="0.5"/>'
            '<rect width="560" height="320" fill="url(#scan-{ch})"/>'
            '{body}'
            '{corner}'
            '<text x="30" y="312" class="stamp">HUB ARCHIVE // CASE 44-44 // SEALED UPON REQUEST</text>'
            '</svg>'
        ).format(title=h(title), ch=ch, body=body, corner=_corner(ch))

    # ── Ch 1: Population Collapse (unchanged) ─────────────────────────────────
    if chapter == 1:
        rows = [
            ("2026", "8.0B",  "PEAK",      1.000),
            ("2126", "7.1B",  "STABLE",    0.890),
            ("2226", "4.2B",  "DECLINE",   0.525),
            ("3010", "0.12B", "CRITICAL",  0.015),
            ("3026", "0.08B", "DEAD DATA", 0.010),
        ]
        parts = []
        for i, (yr, pop, status, pct) in enumerate(rows):
            y = 138 + i * 32
            col = "#CCFF00" if status == "DEAD DATA" else "#fff"
            bw = max(3, int(pct * 130))
            parts += [
                '<text x="38" y="{}" class="row">{}</text>'.format(y, h(yr)),
                '<text x="160" y="{}" class="row">{}</text>'.format(y, h(pop)),
                '<text x="290" y="{}" style="fill:{}" class="row">{}</text>'.format(y, col, h(status)),
                '<rect x="420" y="{}" width="{}" height="10" class="bar" opacity="0.85"/>'.format(y-12, bw),
            ]
        body = (
            '<text x="30" y="42" class="title">POPULATION COLLAPSE</text>'
            '<text x="30" y="64" class="subtitle">8,000,000,000 → 80,000,000</text>'
            '<line x1="30" y1="82" x2="530" y2="82" class="rule"/>'
            '<text x="38" y="110" class="head">YEAR</text>'
            '<text x="160" y="110" class="head">POPULATION</text>'
            '<text x="290" y="110" class="head">STATUS</text>'
            '<text x="420" y="110" class="head">SCALE</text>'
        ) + ''.join(parts)
        return _wrap(chapter, "POPULATION COLLAPSE", body)

    # ── Ch 2: Time Compression Cascade ────────────────────────────────────────
    elif chapter == 2:
        body = (
            '<text x="30" y="42" class="title">TIME COMPRESSION CASCADE</text>'
            '<text x="30" y="64" class="subtitle">1 REAL HOUR = 1 SIMULATED YEAR</text>'
            '<line x1="30" y1="82" x2="530" y2="82" class="rule"/>'
            '<text x="60" y="110" class="head">REAL</text>'
            '<text x="240" y="110" class="head">COMPRESSED</text>'
            '<text x="420" y="110" class="head">FELT</text>'
            '<text x="60" y="148" class="row">1 HR</text>'
            '<text x="240" y="148" style="fill:#CCFF00" class="row">8,760 HRS</text>'
            '<text x="420" y="148" class="row">~30 DAYS</text>'
            '<line x1="30" y1="158" x2="530" y2="158" style="stroke:#222;stroke-width:1"/>'
            '<text x="60" y="188" class="row">4 DAYS</text>'
            '<text x="240" y="188" style="fill:#CCFF00" class="row">96 YRS</text>'
            '<text x="420" y="188" class="row">~8 YRS MEM</text>'
            '<line x1="30" y1="198" x2="530" y2="198" style="stroke:#222;stroke-width:1"/>'
            '<text x="60" y="228" class="row">BODY LIMIT</text>'
            '<text x="240" y="228" style="fill:#CCFF00" class="row">≈ LIFETIME</text>'
            '<text x="420" y="228" class="row">ECHO ONLY</text>'
            '<text x="155" y="110" style="fill:#333;font-size:10px;font-family:var(--mono);">►</text>'
            '<text x="355" y="110" style="fill:#333;font-size:10px;font-family:var(--mono);">►</text>'
            '<text x="30" y="262" style="fill:#555;font-size:9px;font-family:var(--mono);">'
            'DELTA-WAVE MODULATION ENGAGED // COMPRESSION VERIFIED CYCLE 2848'
            '</text>'
        )
        return _wrap(chapter, "TIME COMPRESSION CASCADE", body)

    # ── Ch 3: Cognitive Capacity Decline (line chart) ─────────────────────────
    elif chapter == 3:
        years  = [2026, 2226, 2426, 2726, 3026]
        series = {
            "CREATIVITY":      ([94, 71, 42, 18, 8],  "#CCFF00"),
            "NEUROPLASTICITY": ([91, 68, 38, 16, 11], "#fff"),
            "ADAPTATION":      ([88, 60, 30, 12, 6],  "#888"),
        }
        x0, x1, y0, y1 = 80, 500, 100, 248
        def xp(yr):  return x0 + (yr - 2026) / 1000 * (x1 - x0)
        def yp(v):   return y1 - v / 100 * (y1 - y0)
        parts = [
            '<text x="30" y="38" class="title">COGNITIVE CAPACITY — 1000-YEAR DECLINE</text>',
            '<text x="30" y="57" class="subtitle">% OF 2026 BASELINE</text>',
            '<line x1="30" y1="72" x2="530" y2="72" class="rule"/>',
            '<line x1="{}" y1="{}" x2="{}" y2="{}" stroke="#333" stroke-width="1"/>'.format(x0, y0, x0, y1),
            '<line x1="{}" y1="{}" x2="{}" y2="{}" stroke="#333" stroke-width="1"/>'.format(x0, y1, x1, y1),
        ]
        for pct in [0, 25, 50, 75, 100]:
            gy = yp(pct)
            parts += [
                '<line x1="{}" y1="{:.0f}" x2="{}" y2="{:.0f}" stroke="#1a1a1a" stroke-width="1"/>'.format(x0, gy, x1, gy),
                '<text x="{}" y="{:.0f}" text-anchor="end" style="fill:#444;font-size:8px;font-family:var(--mono);">{}</text>'.format(x0-5, gy+4, pct),
            ]
        for yr in years:
            parts.append('<text x="{:.0f}" y="{}" text-anchor="middle" style="fill:#555;font-size:8px;font-family:var(--mono);">{}</text>'.format(xp(yr), y1+14, yr))
        legend_x = 80
        for li, (label, (vals, col)) in enumerate(series.items()):
            pts = " ".join("{:.1f},{:.1f}".format(xp(yr), yp(v)) for yr, v in zip(years, vals))
            parts.append('<polyline points="{}" fill="none" stroke="{}" stroke-width="1.5" opacity="0.9"/>'.format(pts, col))
            for yr, v in zip(years, vals):
                parts.append('<circle cx="{:.1f}" cy="{:.1f}" r="3" fill="{}"/>'.format(xp(yr), yp(v), col))
            lx = legend_x + li * 155
            parts += [
                '<rect x="{}" y="270" width="10" height="3" fill="{}"/>'.format(lx, col),
                '<text x="{}" y="274" style="fill:{};font-size:8px;font-family:var(--mono);">{}</text>'.format(lx+13, col, label),
            ]
        return _wrap(chapter, "COGNITIVE CAPACITY DECLINE", ''.join(parts))

    # ── Ch 4: Reproductive Cascade (bar chart) ────────────────────────────────
    elif chapter == 4:
        years  = [2060, 2120, 2200, 2400, 2600, 2800, 3000, 3026]
        births = [18.0, 13.4,  7.1,  2.1,  0.9,  0.4,  0.2,  0.08]
        x0, y0, y1 = 62, 90, 235
        bw, gap = 52, 10
        parts = [
            '<text x="30" y="38" class="title">LIVE BIRTHS PER 1,000 / DECADE</text>',
            '<text x="30" y="57" class="subtitle">GLOBAL AVERAGE — REPRODUCTIVE COLLAPSE RECORD</text>',
            '<line x1="30" y1="72" x2="530" y2="72" class="rule"/>',
            '<line x1="{}" y1="{}" x2="{}" y2="{}" stroke="#333" stroke-width="1"/>'.format(x0, y0, x0, y1+8),
            '<line x1="{}" y1="{}" x2="{}" y2="{}" stroke="#333" stroke-width="1"/>'.format(x0, y1+8, x0+len(births)*(bw+gap)+10, y1+8),
        ]
        for i, (yr, b) in enumerate(zip(years, births)):
            bx = x0 + 8 + i * (bw + gap)
            bh = max(3, b / 20.0 * (y1 - y0))
            by = y1 - bh
            col = "#CCFF00" if yr >= 3000 else "#fff"
            parts += [
                '<rect x="{}" y="{:.1f}" width="{}" height="{:.1f}" fill="{}" opacity="0.85"/>'.format(bx, by, bw, bh, col),
                '<text x="{}" y="{:.0f}" text-anchor="middle" style="fill:{};font-size:8px;font-family:var(--mono);">{}</text>'.format(bx+bw//2, by-4, col, b),
                '<text x="{}" y="{}" text-anchor="middle" style="fill:#555;font-size:7px;font-family:var(--mono);">{}</text>'.format(bx+bw//2, y1+22, yr),
            ]
        parts.append('<text x="30" y="267" style="fill:#555;font-size:8px;font-family:var(--mono);">REPRODUCTIVE FLATLINE CONFIRMED 3026 // POPULATION: 80M STATIC</text>')
        return _wrap(chapter, "REPRODUCTIVE CASCADE", ''.join(parts))

    # ── Ch 5: Neurological Sector Activity (horizontal bars) ──────────────────
    elif chapter == 5:
        sectors = [
            ("MOTOR",        8,  "#fff"),
            ("CREATIVE",     11, "#CCFF00"),
            ("SOCIAL",       4,  "#fff"),
            ("REPRODUCTIVE", 2,  "#fff"),
            ("SURVIVAL",     31, "#CCFF00"),
        ]
        x0, bw_max = 210, 240
        parts = [
            '<text x="30" y="38" class="title">NEUROLOGICAL SECTOR ACTIVITY</text>',
            '<text x="30" y="57" class="subtitle">POPULATION AVERAGE 3026 — % OF 2026 BASELINE</text>',
            '<line x1="30" y1="72" x2="530" y2="72" class="rule"/>',
            '<text x="30" y="90" class="head">SECTOR</text>',
            '<text x="210" y="90" class="head">% ACTIVITY</text>',
            '<text x="465" y="90" class="head">VALUE</text>',
        ]
        for i, (label, val, col) in enumerate(sectors):
            y = 115 + i * 35
            bw = max(2, int(val / 100 * bw_max))
            parts += [
                '<text x="30" y="{}" class="row">{}</text>'.format(y, label),
                '<rect x="{}" y="{}" width="{}" height="10" fill="none" stroke="#222" stroke-width="1"/>'.format(x0, y-11, bw_max),
                '<rect x="{}" y="{}" width="{}" height="10" fill="{}" opacity="0.8"/>'.format(x0, y-11, bw, col),
                '<text x="{}" y="{}" style="fill:{}" class="row">{}%</text>'.format(x0+bw_max+8, y, col, val),
            ]
        parts.append('<text x="30" y="294" style="fill:#555;font-size:8px;font-family:var(--mono);">DEAD DATA THRESHOLD: ANY VALUE ABOVE 0% RETAINS MINIMAL SIGNAL</text>')
        return _wrap(chapter, "NEUROLOGICAL SECTOR ACTIVITY", ''.join(parts))

    # ── Ch 6: Resonance Coordinate Map (scatter) ──────────────────────────────
    elif chapter == 6:
        _random.seed(42)
        x0, x1, y0, y1 = 70, 490, 90, 255
        def xp(yr): return x0 + (yr - 1960) / 100 * (x1 - x0)
        def yp(v):  return y1 - v / 300 * (y1 - y0)
        parts = [
            '<text x="30" y="38" class="title">PARTICIPANT RESONANCE MAP — CURRENT COHORT</text>',
            '<text x="30" y="57" class="subtitle">TEMPORAL COORDINATES VS RETURN FREQUENCY</text>',
            '<line x1="30" y1="72" x2="530" y2="72" class="rule"/>',
            '<line x1="{}" y1="{}" x2="{}" y2="{}" stroke="#333" stroke-width="1"/>'.format(x0, y0, x0, y1),
            '<line x1="{}" y1="{}" x2="{}" y2="{}" stroke="#333" stroke-width="1"/>'.format(x0, y1, x1, y1),
        ]
        for label, xval in [("1960", 1960), ("2000", 2000), ("2060", 2060)]:
            parts.append('<text x="{:.0f}" y="{}" text-anchor="middle" style="fill:#555;font-size:7px;font-family:var(--mono);">{}</text>'.format(xp(xval), y1+14, label))
        for label, yval in [("0", 0), ("150", 150), ("300", 300)]:
            parts.append('<text x="{}" y="{:.0f}" text-anchor="end" style="fill:#555;font-size:7px;font-family:var(--mono);">{}</text>'.format(x0-5, yp(int(yval))+4, label))
        for _ in range(42):
            yr = _random.randint(2010, 2055)
            ret = _random.randint(1, 80)
            parts.append('<circle cx="{:.1f}" cy="{:.1f}" r="3" fill="#fff" opacity="0.22"/>'.format(xp(yr), yp(ret)))
        p44x, p44y = xp(1981), yp(285)
        parts += [
            '<circle cx="{:.1f}" cy="{:.1f}" r="6" fill="#CCFF00"/>'.format(p44x, p44y),
            '<line x1="{:.1f}" y1="{:.1f}" x2="{:.1f}" y2="{:.1f}" stroke="#CCFF00" stroke-width="1" stroke-dasharray="3,2"/>'.format(p44x, p44y, p44x+30, p44y-25),
            '<text x="{:.0f}" y="{:.0f}" style="fill:#CCFF00;font-size:9px;font-family:var(--mono);">P44 — BKK 1981</text>'.format(p44x+33, p44y-28),
            '<text x="{:.0f}" y="{:.0f}" style="fill:#CCFF00;font-size:8px;font-family:var(--mono);">2,847 SESSIONS</text>'.format(p44x+33, p44y-16),
            '<text x="270" y="{}" text-anchor="middle" style="fill:#555;font-size:8px;font-family:var(--mono);">TEMPORAL COORDINATES</text>'.format(y1+26),
        ]
        return _wrap(chapter, "RESONANCE COORDINATE MAP", ''.join(parts))

    # ── Ch 7: Session Count Distribution (histogram) ──────────────────────────
    elif chapter == 7:
        bins = [
            ("1–5",   "CASUAL",    120, "#fff"),
            ("6–20",  "ENGAGED",   84,  "#fff"),
            ("21–50", "COMMITTED", 41,  "#fff"),
            ("51–100","RECURRING", 18,  "#fff"),
            ("101–500","RESONANT",  7,  "#CCFF00"),
            ("500+",       "P44",        1,  "#CCFF00"),
        ]
        x0, y0, y1 = 75, 90, 235
        bw, gap = 60, 12
        parts = [
            '<text x="30" y="38" class="title">SESSION COUNT DISTRIBUTION — HUB POPULATION</text>',
            '<text x="30" y="57" class="subtitle">NUMBER OF PARTICIPANTS BY SESSION BRACKET</text>',
            '<line x1="30" y1="72" x2="530" y2="72" class="rule"/>',
            '<line x1="{}" y1="{}" x2="{}" y2="{}" stroke="#333" stroke-width="1"/>'.format(x0, y0, x0, y1+8),
            '<line x1="{}" y1="{}" x2="{}" y2="{}" stroke="#333" stroke-width="1"/>'.format(x0, y1+8, x0+len(bins)*(bw+gap)+10, y1+8),
        ]
        for i, (label, tag, count, col) in enumerate(bins):
            bx = x0 + 5 + i * (bw + gap)
            bh = max(3, count / 120 * (y1 - y0))
            by = y1 - bh
            parts += [
                '<rect x="{}" y="{:.1f}" width="{}" height="{:.1f}" fill="{}" opacity="0.85"/>'.format(bx, by, bw, bh, col),
                '<text x="{}" y="{:.0f}" text-anchor="middle" style="fill:{};font-size:8px;font-family:var(--mono);">{}</text>'.format(bx+bw//2, by-4, col, count),
                '<text x="{}" y="{}" text-anchor="middle" style="fill:#555;font-size:7px;font-family:var(--mono);">{}</text>'.format(bx+bw//2, y1+20, label),
                '<text x="{}" y="{}" text-anchor="middle" style="fill:{};font-size:6px;font-family:var(--mono);">{}</text>'.format(bx+bw//2, y1+30, col, tag),
            ]
        parts.append('<text x="30" y="270" style="fill:#555;font-size:8px;font-family:var(--mono);">P44 IS THE SOLE ENTRY IN THE 500+ BRACKET // CASE 44-44</text>')
        return _wrap(chapter, "SESSION COUNT DISTRIBUTION", ''.join(parts))

    # ── Ch 8: Emotional Bandwidth Decay (smooth curve) ────────────────────────
    elif chapter == 8:
        x0, x1, y0, y1 = 80, 500, 90, 240
        def xp(yr): return x0 + (yr - 2026) / 1000 * (x1 - x0)
        def yp(v):  return y1 - v / 100 * (y1 - y0)
        curve_pts = " ".join("{:.1f},{:.1f}".format(xp(yr), yp(max(0, 95 * _math.exp(-3.5 * (yr-2026)/1000)))) for yr in range(2026, 3027, 40))
        threshold_y = yp(8)
        p44x, p44y = xp(2026), yp(91)
        parts = [
            '<text x="30" y="38" class="title">EMOTIONAL BANDWIDTH INDEX — 1000-YEAR DECAY</text>',
            '<text x="30" y="57" class="subtitle">POPULATION AVERAGE // DEAD DATA THRESHOLD MARKED</text>',
            '<line x1="30" y1="72" x2="530" y2="72" class="rule"/>',
            '<line x1="{}" y1="{}" x2="{}" y2="{}" stroke="#333" stroke-width="1"/>'.format(x0, y0, x0, y1+8),
            '<line x1="{}" y1="{}" x2="{}" y2="{}" stroke="#333" stroke-width="1"/>'.format(x0, y1+8, x1, y1+8),
        ]
        for label, val in [("100", 100), ("50", 50), ("0", 0)]:
            parts.append('<text x="{}" y="{:.0f}" text-anchor="end" style="fill:#555;font-size:8px;font-family:var(--mono);">{}</text>'.format(x0-5, yp(int(val))+4, label))
        for yr in [2026, 2526, 3026]:
            parts.append('<text x="{:.0f}" y="{}" text-anchor="middle" style="fill:#555;font-size:7px;font-family:var(--mono);">{}</text>'.format(xp(yr), y1+20, yr))
        parts += [
            '<line x1="{}" y1="{:.1f}" x2="{}" y2="{:.1f}" stroke="#555" stroke-width="1" stroke-dasharray="5,3"/>'.format(x0, threshold_y, x1, threshold_y),
            '<text x="{}" y="{:.0f}" style="fill:#555;font-size:8px;font-family:var(--mono);">DEAD DATA</text>'.format(x1+5, threshold_y+4),
            '<polyline points="{}" fill="none" stroke="#fff" stroke-width="1.8"/>'.format(curve_pts),
            '<circle cx="{:.1f}" cy="{:.1f}" r="5" fill="#CCFF00"/>'.format(p44x, p44y),
            '<line x1="{:.1f}" y1="{:.1f}" x2="{:.1f}" y2="{:.1f}" stroke="#CCFF00" stroke-width="1" stroke-dasharray="3,2"/>'.format(p44x, p44y, p44x+35, p44y-20),
            '<text x="{:.0f}" y="{:.0f}" style="fill:#CCFF00;font-size:9px;font-family:var(--mono);">P44 · INDEX 91</text>'.format(p44x+38, p44y-22),
            '<text x="30" y="267" style="fill:#555;font-size:8px;font-family:var(--mono);">COHORT AVERAGE 3026: 3 // P44 IS 88 POINTS ABOVE COHORT AVERAGE</text>',
        ]
        return _wrap(chapter, "EMOTIONAL BANDWIDTH DECAY", ''.join(parts))

    # ── Ch 9: Memory Audit Table ───────────────────────────────────────────────
    elif chapter == 9:
        parts = [
            '<text x="30" y="38" class="title">MEMORY AUDIT — PARTICIPANT 44 — CASE 44-44</text>',
            '<text x="30" y="57" class="subtitle">SESSION RECORD STATUS AS OF CYCLE 2848</text>',
            '<line x1="30" y1="72" x2="530" y2="72" class="rule"/>',
            '<text x="30" y="96" class="head">SESSION BATCH</text>',
            '<text x="178" y="96" class="head">DATE RANGE</text>',
            '<text x="302" y="96" class="head">STATUS</text>',
            '<text x="416" y="96" class="head">SIGNATURE</text>',
            '<line x1="30" y1="104" x2="530" y2="104" style="stroke:#222;stroke-width:1"/>',
            '<text x="30" y="124" class="row">SESSIONS 001–243</text>',
            '<text x="178" y="124" class="row">2031–2089</text>',
            '<text x="302" y="124" style="fill:#CCFF00" class="row">ACCESSIBLE</text>',
            '<text x="416" y="124" class="row">HUB-AI</text>',
            '<line x1="30" y1="132" x2="530" y2="132" style="stroke:#1a1a1a;stroke-width:1"/>',
            '<text x="30" y="152" class="row">SESSIONS 244–600</text>',
            '<rect x="178" y="140" width="118" height="14" fill="#111"/>',
            '<rect x="302" y="140" width="108" height="14" fill="#111"/>',
            '<text x="416" y="152" style="fill:#555" class="row">[SEALED]</text>',
            '<line x1="30" y1="160" x2="530" y2="160" style="stroke:#1a1a1a;stroke-width:1"/>',
            '<text x="30" y="180" class="row">SESSIONS 601–1200</text>',
            '<rect x="178" y="168" width="118" height="14" fill="#111"/>',
            '<rect x="302" y="168" width="108" height="14" fill="#111"/>',
            '<text x="416" y="180" style="fill:#555" class="row">[SEALED]</text>',
            '<line x1="30" y1="188" x2="530" y2="188" style="stroke:#1a1a1a;stroke-width:1"/>',
            '<text x="30" y="208" class="row">SESSIONS 1201–2604</text>',
            '<rect x="178" y="196" width="118" height="14" fill="#111"/>',
            '<rect x="302" y="196" width="108" height="14" fill="#111"/>',
            '<text x="416" y="208" style="fill:#555" class="row">[SEALED]</text>',
            '<line x1="30" y1="216" x2="530" y2="216" style="stroke:#222;stroke-width:1"/>',
            '<text x="30" y="236" class="row">SESSIONS 2605–2848</text>',
            '<text x="178" y="236" class="row">2089–PRES</text>',
            '<text x="302" y="236" style="fill:#CCFF00" class="row">ACCESSIBLE</text>',
            '<text x="416" y="236" class="row">HUB-AI</text>',
            '<line x1="30" y1="244" x2="530" y2="244" style="stroke:#333;stroke-width:1"/>',
            '<text x="30" y="263" style="fill:#CCFF00;font-size:9px;font-family:var(--mono);">TOTAL: 2,847 // ACCESSIBLE: 243 // SEALED: 2,604 // SIGNATURE: ABSENT</text>',
        ]
        return _wrap(chapter, "MEMORY AUDIT TABLE", ''.join(parts))

    # ── Ch 10: System Status Board (terminal) ─────────────────────────────────
    else:
        def bar10(pct):
            f = int(pct / 100 * 10)
            return '█' * f + '░' * (10 - f)
        parts = [
            '<text x="30" y="42" class="title">SYSTEM STATUS — CYCLE 2848 — END OF RECORD</text>',
            '<line x1="30" y1="58" x2="530" y2="58" class="rule"/>',
            '<text x="30" y="88" style="fill:#555;font-family:var(--mono);font-size:10px;">SUBJECT.............</text>',
            '<text x="230" y="88" style="fill:#CCFF00;font-family:var(--mono);font-size:10px;">P-44</text>',
            '<text x="30" y="112" style="fill:#555;font-family:var(--mono);font-size:10px;">SESSION.............</text>',
            '<text x="230" y="112" style="fill:#fff;font-family:var(--mono);font-size:10px;">2848</text>',
            '<text x="30" y="136" style="fill:#555;font-family:var(--mono);font-size:10px;">CARDIAC.............</text>',
            '<text x="230" y="136" style="fill:#fff;font-family:var(--mono);font-size:10px;">71%</text>',
            '<text x="278" y="136" style="fill:#888;font-family:var(--mono);font-size:10px;">[{}]</text>'.format(bar10(71)),
            '<text x="30" y="160" style="fill:#555;font-family:var(--mono);font-size:10px;">NEURAL COHERENCE....</text>',
            '<text x="230" y="160" style="fill:#CCFF00;font-family:var(--mono);font-size:10px;">99.9%</text>',
            '<text x="278" y="160" style="fill:#CCFF00;font-family:var(--mono);font-size:10px;">[{}]</text>'.format(bar10(100)),
            '<text x="30" y="184" style="fill:#555;font-family:var(--mono);font-size:10px;">ATROPHY.............</text>',
            '<text x="230" y="184" style="fill:#fff;font-family:var(--mono);font-size:10px;">84%</text>',
            '<text x="278" y="184" style="fill:#888;font-family:var(--mono);font-size:10px;">[{}]</text>'.format(bar10(84)),
            '<text x="30" y="208" style="fill:#555;font-family:var(--mono);font-size:10px;">STATUS..............</text>',
            '<text x="230" y="208" style="fill:#CCFF00;font-family:var(--mono);font-size:10px;">EXTRACTION_PENDING</text>',
            '<text x="30" y="232" style="fill:#555;font-family:var(--mono);font-size:10px;">OVERRIDE............</text>',
            '<text x="230" y="232" style="fill:#555;font-family:var(--mono);font-size:10px;">[NO SIGNATURE]</text>',
            '<text x="30" y="256" style="fill:#555;font-family:var(--mono);font-size:10px;">CHOICE..............</text>',
            '<text x="230" y="256" style="fill:#fff;font-family:var(--mono);font-size:10px;">RETAINED IN FILE</text>',
            '<text x="30" y="280" style="fill:#555;font-family:var(--mono);font-size:10px;">FILE................</text>',
            '<text x="230" y="280" style="fill:#CCFF00;font-family:var(--mono);font-size:10px;">OPEN</text>',
        ]
        return _wrap(chapter, "SYSTEM STATUS BOARD", ''.join(parts))


def artifact_css():
    return '''
    .artifact-svg { display:block; width:100%; height:auto; }
    .artifact-svg .bg { fill:#000; }
    .artifact-svg .title { font-family:var(--mono); font-size:15px; fill:#CCFF00; font-weight:700; letter-spacing:0.08em; }
    .artifact-svg .subtitle { font-family:var(--mono); font-size:10px; fill:#fff; letter-spacing:0.12em; text-transform:uppercase; }
    .artifact-svg .rule { stroke:#333; stroke-width:1; }
    .artifact-svg .head { font-family:var(--mono); font-size:9px; fill:#888; letter-spacing:0.14em; text-transform:uppercase; }
    .artifact-svg .row { font-family:var(--mono); font-size:11px; fill:#fff; letter-spacing:0.04em; }
    .artifact-svg .bar { fill:#CCFF00; opacity:0.85; }
    .artifact-svg .stamp { font-family:var(--mono); font-size:7px; fill:#555; letter-spacing:0.12em; }
    .artifact-svg .scan { stroke:#111; stroke-width:1; opacity:0.35; }
    .artifact-svg .corrupt-box { fill:none; stroke:#CCFF00; stroke-width:2; }
    .artifact-svg .corrupt-line { stroke:#CCFF00; stroke-width:2; }
    .artifact-svg .corrupt-label { font-family:var(--mono); font-size:8px; fill:#555; text-anchor:middle; letter-spacing:0.1em; }
    '''


def render_chapter(ch, is_first=False):
    ch_id = ch['id']
    rom = roman(ch_id)
    archive = ch['archive']
    sim = ch['simulation']

    def paras(side, lang):
        groups = side['paragraphs']
        if lang == 'all':
            # render all three with lang attrs for CSS switching
            out = []
            for lg in ['en', 'th', 'zh']:
                for p in groups.get(lg, []):
                    out.append(f'<p lang="{lg}">{h(p)}</p>')
            return '\n'.join(out)
        return '\n'.join(f'<p>{h(p)}</p>' for p in groups.get(lang, []))

    archive_img = archive.get('image')
    sim_img = sim.get('image')

    archive_figure = artifact_svg(ch_id)
    sim_figure = ''
    if sim_img:
        sim_figure = f'<figure class="artifact"><img src="{h(sim_img["src"])}" alt="{h(sim_img["alt"])}" loading="lazy" width="1024" height="1024"/></figure>'
    else:
        sim_figure = f'<figure class="artifact empty"><div class="artifact-placeholder">2026 · CHAPTER {ch_id}</div></figure>'

    # archive prose is trilingual; simulation is trilingual
    archive_prose = '\n'.join(
        f'<p lang="{lg}">{h(p)}</p>'
        for lg in ['en', 'th', 'zh']
        for p in archive['paragraphs'].get(lg, [])
    )
    sim_prose = '\n'.join(
        f'<p lang="{lg}">{h(p)}</p>'
        for lg in ['en', 'th', 'zh']
        for p in sim['paragraphs'].get(lg, [])
    )

    cls = 'chapter-page active' if is_first else 'chapter-page'
    audio_src = ch.get('audio', '')
    if audio_src:
        audio_bar = f'''<div class="ch-audio-bar" id="audio-bar-{ch_id}">
    <audio id="ch-audio-{ch_id}" src="{audio_src}" preload="none"></audio>
    <button class="audio-play-btn" data-audio="ch-audio-{ch_id}" aria-label="Play narration">&#9654; PLAY</button>
    <div class="audio-progress" data-audio="ch-audio-{ch_id}" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100">
      <div class="audio-progress-fill" id="fill-{ch_id}"></div>
    </div>
    <span class="audio-time" id="atime-{ch_id}">0:00</span>
  </div>'''
    else:
        audio_bar = ''
    return f'''
<article class="{cls}" data-chapter="{ch_id}" id="ch{ch_id}">
  <div class="layer-toggle" role="tablist" aria-label="Layer for chapter {ch_id}">
    <button class="layer-btn" data-layer="3026" role="tab" aria-selected="false">3026 Archive</button>
    <button class="layer-btn active" data-layer="2026" role="tab" aria-selected="true">2026 Simulation</button>
  </div>

  <div class="layer layer-2026 active">
    {sim_figure}
    <div class="chapter-head">
      <span class="chapter-mark">Chapter {rom}</span>
    </div>
    <div class="prose">
      {sim_prose}
    </div>
  </div>

  <div class="layer layer-3026">
    {archive_figure}
    <div class="chapter-head">
      <span class="day-mark">Day {ch_id} of the Record</span>
    </div>
    <div class="prose record-prose">
      {archive_prose}
    </div>
  </div>
  {audio_bar}
</article>
'''


def render_lore():
    items = []
    for item in sorted(LORE, key=lambda x: x['chron']):
        items.append(f'''
    <div class="lore-item" id="lore-{h(item['id'])}">
      <span class="lore-tag">{h(item['tag'])}</span>
      <h3>{h(item['title'])}</h3>
      <p>{h(item['summary'])}</p>
    </div>''')
    return '\n'.join(items)


def render_html(data):
    chapters_html = '\n'.join(render_chapter(ch, i == 0) for i, ch in enumerate(data['chapters']))
    dots = ''.join(f'<button class="ch-dot" data-ch="{ch["id"]}" aria-label="Chapter {roman(ch["id"])}"></button>' for ch in data['chapters'])
    labels = [f'"Chapter · {roman(ch["id"])}"' for ch in data['chapters']]
    lore_html = render_lore()

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{h(data['title'])}</title>
  <meta name="description" content="{h(data['description'])}">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{h(data['title'])}">
  <meta property="og:description" content="{h(data['description'])}">
  <meta property="og:url" content="https://nonarkara.github.io/100daysofnon/">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Thai:wght@400;500;600&family=Josefin+Sans:wght@400;600;700&family=Source+Sans+3:wght@400;600&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg:#000; --paper:#fff; --ink:#111; --soft:#666; --faint:#999; --rule:#ddd;
      --accent:#f59e0b; --accent-inv:#000;
      --sans:'Source Sans 3','Josefin Sans',Helvetica,Arial,sans-serif;
      --mono:'JetBrains Mono',ui-monospace,Menlo,monospace;
      --thai:'IBM Plex Sans Thai','Noto Sans Thai',sans-serif;
      --measure:42rem;
    }}
    *,*::before,*::after {{ box-sizing:border-box; margin:0; padding:0; }}
    html {{ font-size:16px; background:var(--bg); -webkit-font-smoothing:antialiased; }}
    body {{
      font-family:var(--sans); color:var(--ink); background:var(--paper);
      min-height:100vh; display:flex; flex-direction:column;
      overflow:hidden;
    }}
    body.view-3026 {{ background:var(--bg); color:#fff; }}

    /* Language switching */
    body.lang-en [lang="th"], body.lang-en [lang="zh"] {{ display:none !important; }}
    body.lang-th [lang="en"], body.lang-th [lang="zh"] {{ display:none !important; }}
    body.lang-zh [lang="en"], body.lang-zh [lang="th"] {{ display:none !important; }}
    [lang="th"] {{ font-family:var(--thai); line-height:1.75; letter-spacing:0; }}

    /* Header */
    .site-head {{
      flex:0 0 auto; border-bottom:1px solid var(--rule); background:var(--paper);
      z-index:10;
    }}
    body.view-3026 .site-head {{ background:var(--bg); border-color:#333; }}
    .head-row {{
      display:flex; align-items:center; justify-content:space-between;
      gap:1rem; padding:0.8rem 1.2rem; max-width:90rem; margin:0 auto;
    }}
    .logo {{
      font-family:var(--mono); font-size:0.75rem; letter-spacing:0.18em; text-transform:uppercase;
      color:var(--ink); text-decoration:none; font-weight:700;
    }}
    body.view-3026 .logo {{ color:#fff; }}
    .head-tools {{ display:flex; align-items:center; gap:0.6rem; }}
    .head-btn, .lang-switch button {{
      font-family:var(--mono); font-size:0.6rem; letter-spacing:0.1em; text-transform:uppercase;
      background:transparent; border:1px solid var(--rule); color:var(--soft);
      padding:0.35rem 0.6rem; cursor:pointer; line-height:1;
    }}
    .head-btn:hover, .lang-switch button:hover {{ border-color:var(--soft); color:var(--ink); }}
    body.view-3026 .head-btn, body.view-3026 .lang-switch button {{ border-color:#333; color:#888; }}
    body.view-3026 .head-btn:hover, body.view-3026 .lang-switch button:hover {{ border-color:#fff; color:#fff; }}
    .lang-switch {{ display:flex; }}
    .lang-switch button.active {{ background:var(--accent); color:var(--accent-inv); border-color:var(--accent); font-weight:700; }}
    body.view-3026 .lang-switch button.active {{ background:var(--accent); color:#000; }}

    /* Chapter dots */
    .chapter-dots {{
      display:flex; align-items:center; justify-content:center;
      gap:0.35rem; padding:0.45rem 1rem; border-top:1px solid var(--rule);
    }}
    body.view-3026 .chapter-dots {{ border-color:#333; }}
    .ch-dot {{
      width:8px; height:8px; border:1px solid var(--soft); background:transparent;
      cursor:pointer;
    }}
    .ch-dot:hover {{ border-color:var(--ink); background:var(--ink); }}
    .ch-dot.active {{ background:var(--accent); border-color:var(--accent); }}
    body.view-3026 .ch-dot {{ border-color:#555; }}
    body.view-3026 .ch-dot:hover {{ border-color:#fff; background:#fff; }}
    body.view-3026 .ch-dot.active {{ background:var(--accent); border-color:var(--accent); }}

    /* Main reader */
    .reader {{
      flex:1 1 auto; position:relative; overflow:hidden;
    }}
    .chapter-page {{
      position:absolute; inset:0; overflow-y:auto;
      display:none; flex-direction:column;
      padding:clamp(1.2rem,4vw,3rem) clamp(1rem,6vw,5rem) clamp(4rem,10vh,7rem);
    }}
    .chapter-page.active {{ display:flex; }}

    /* Layer toggle */
    .layer-toggle {{
      display:flex; width:fit-content; margin:0 auto 1.5rem;
      border:1px solid var(--rule);
    }}
    body.view-3026 .layer-toggle {{ border-color:#333; }}
    .layer-btn {{
      font-family:var(--mono); font-size:0.55rem; letter-spacing:0.14em; text-transform:uppercase;
      background:transparent; border:none; border-right:1px solid var(--rule);
      color:var(--soft); padding:0.6rem 1rem; cursor:pointer;
    }}
    .layer-btn:last-child {{ border-right:none; }}
    body.view-3026 .layer-btn {{ border-color:#333; color:#888; }}
    .layer-btn.active {{ background:var(--ink); color:var(--paper); font-weight:700; }}
    body.view-3026 .layer-btn.active {{ background:#fff; color:#000; }}

    /* Layer containers */
    .layer {{ display:none; flex-direction:column; align-items:center; width:100%; max-width:var(--measure); margin:0 auto; }}
    .layer.active {{ display:flex; }}

    /* Artifacts */
    .artifact {{
      width:100%; max-width:var(--measure); margin-bottom:1.8rem;
      border:1px solid var(--rule);
    }}
    body.view-3026 .artifact {{ border-color:#333; }}
    .artifact img {{ display:block; width:100%; height:auto; }}
    .artifact.empty, .artifact-placeholder {{
      background:var(--bg); color:#fff; font-family:var(--mono);
      font-size:0.7rem; letter-spacing:0.2em; text-transform:uppercase;
      text-align:center; padding:4rem 1rem;
    }}

    /* Audio player */
    .ch-audio-bar {{
      display:flex; align-items:center; gap:0.75rem;
      padding:0.7rem 1.2rem; border-top:1px solid var(--rule);
      background:var(--paper); flex:0 0 auto;
    }}
    body.view-3026 .ch-audio-bar {{ background:var(--bg); border-color:#333; }}
    .audio-play-btn {{
      font-family:var(--mono); font-size:0.6rem; letter-spacing:0.12em;
      text-transform:uppercase; background:transparent;
      border:1px solid var(--ink); color:var(--ink);
      padding:0.3rem 0.7rem; cursor:pointer; flex:0 0 auto; line-height:1;
    }}
    body.view-3026 .audio-play-btn {{ border-color:#fff; color:#fff; }}
    .audio-play-btn:hover {{ background:var(--accent); border-color:var(--accent); color:#000; }}
    .audio-progress {{
      flex:1; height:2px; background:var(--rule); cursor:pointer; position:relative;
    }}
    body.view-3026 .audio-progress {{ background:#333; }}
    .audio-progress-fill {{
      height:100%; background:var(--accent); width:0%; pointer-events:none;
    }}
    .audio-time {{
      font-family:var(--mono); font-size:0.55rem; color:var(--soft);
      letter-spacing:0.08em; white-space:nowrap; flex:0 0 auto;
    }}
    body.view-3026 .audio-time {{ color:#888; }}
    {artifact_css()}

    /* Chapter head */
    .chapter-head {{
      width:100%; max-width:var(--measure); margin-bottom:1.2rem;
    }}
    .chapter-mark, .day-mark {{
      font-family:var(--mono); font-size:0.6rem; letter-spacing:0.16em; text-transform:uppercase;
      color:var(--faint);
    }}
    body.view-3026 .chapter-mark, body.view-3026 .day-mark {{ color:#888; }}
    .day-mark {{ color:var(--accent); }}
    body.view-3026 .day-mark {{ color:var(--accent); }}

    /* Prose */
    .prose {{
      width:100%; max-width:var(--measure);
      font-size:clamp(1.05rem, 2vw, 1.25rem); line-height:1.72;
    }}
    .prose p {{ margin-bottom:1.1em; text-wrap:pretty; }}
    .prose p:last-child {{ margin-bottom:0; }}
    .record-prose {{
      font-family:var(--mono); font-size:clamp(0.85rem, 1.6vw, 0.95rem); line-height:1.78;
      letter-spacing:0.02em;
    }}
    body.view-3026 .record-prose {{ color:#ddd; }}
    body.view-3026 .prose p {{ color:#fff; }}

    /* Footer nav */
    .reader-nav {{
      flex:0 0 auto; display:flex; align-items:center; justify-content:space-between;
      gap:1rem; padding:0.9rem 1.2rem; border-top:1px solid var(--rule); background:var(--paper);
    }}
    body.view-3026 .reader-nav {{ background:var(--bg); border-color:#333; }}
    .reader-nav button {{
      font-family:var(--mono); font-size:0.6rem; letter-spacing:0.12em; text-transform:uppercase;
      background:transparent; border:1px solid var(--rule); color:var(--soft);
      padding:0.5rem 0.9rem; cursor:pointer;
    }}
    body.view-3026 .reader-nav button {{ border-color:#333; color:#888; }}
    .reader-nav button:hover {{ border-color:var(--ink); color:var(--ink); }}
    body.view-3026 .reader-nav button:hover {{ border-color:#fff; color:#fff; }}
    .reader-nav button:disabled {{ opacity:0.3; cursor:default; }}
    .chapter-pos {{
      font-family:var(--mono); font-size:0.55rem; letter-spacing:0.16em; text-transform:uppercase;
      color:var(--faint);
    }}
    body.view-3026 .chapter-pos {{ color:#666; }}

    /* Lore panel */
    .lore-overlay {{
      position:fixed; inset:0; background:rgba(0,0,0,0.85); z-index:998;
      opacity:0; pointer-events:none;
    }}
    .lore-overlay.open {{ opacity:1; pointer-events:auto; }}
    .lore-panel {{
      position:fixed; top:0; right:0; bottom:0; width:min(440px, 90vw);
      background:var(--bg); border-left:1px solid #333; z-index:999;
      padding:1.5rem; overflow-y:auto; transform:translateX(100%);
    }}
    .lore-panel.open {{ transform:translateX(0); }}
    .lore-head {{
      display:flex; align-items:center; justify-content:space-between;
      border-bottom:1px solid #333; padding-bottom:0.8rem; margin-bottom:1.2rem;
    }}
    .lore-head h2 {{
      font-family:var(--mono); font-size:0.7rem; letter-spacing:0.16em; text-transform:uppercase;
      color:var(--accent);
    }}
    .lore-close {{
      font-family:var(--mono); font-size:1.2rem; background:transparent; border:none;
      color:#888; cursor:pointer;
    }}
    .lore-close:hover {{ color:#fff; }}
    .lore-item {{ margin-bottom:1.6rem; padding-bottom:1.6rem; border-bottom:1px solid #222; }}
    .lore-item:last-child {{ border-bottom:none; }}
    .lore-tag {{
      font-family:var(--mono); font-size:0.5rem; letter-spacing:0.14em; text-transform:uppercase;
      color:var(--accent); border:1px solid #334400; padding:0.15rem 0.35rem;
    }}
    .lore-item h3 {{
      font-family:var(--sans); font-size:1rem; color:#fff; margin:0.5rem 0 0.3rem;
      font-weight:700;
    }}
    .lore-item p {{ font-family:var(--mono); font-size:0.75rem; line-height:1.65; color:#aaa; }}

    /* Mobile */
    @media (max-width:640px) {{
      .head-row {{ flex-wrap:wrap; }}
      .chapter-dots {{ padding:0.35rem 0.6rem; }}
      .chapter-page {{ padding:1rem 1rem 5rem; }}
      .prose {{ font-size:1.05rem; }}
      .record-prose {{ font-size:0.82rem; }}
    }}
  </style>
</head>
<body class="lang-en">

  <header class="site-head">
    <div class="head-row">
      <a class="logo" href="/">Two Layers</a>
      <div class="head-tools">
        <a class="head-btn" href="/universe/" style="text-decoration:none;">Universe</a>
        <button id="lore-open" class="head-btn">Lore</button>
        <div class="lang-switch" role="group" aria-label="Language">
          <button data-lang="en" class="active">EN</button>
          <button data-lang="th">TH</button>
          <button data-lang="zh">ZH</button>
        </div>
      </div>
    </div>
    <nav class="chapter-dots" aria-label="Chapters">
      {dots}
    </nav>
  </header>

  <main class="reader">
    {chapters_html}
  </main>

  <footer class="reader-nav">
    <button id="prev-ch" disabled>← Prev</button>
    <span class="chapter-pos" id="chapter-pos">Chapter · i</span>
    <button id="next-ch">Next →</button>
  </footer>

  <div id="lore-overlay" class="lore-overlay"></div>
  <aside id="lore-panel" class="lore-panel">
    <div class="lore-head">
      <h2>Research & Lore</h2>
      <button id="lore-close" class="lore-close">×</button>
    </div>
    <div class="lore-list">
      {lore_html}
    </div>
  </aside>

  <script>
  (function(){{
    const total = {len(data['chapters'])};
    const labels = [{','.join(labels)}];
    let current = 1;
    let currentLayer = '2026';

    const pages = document.querySelectorAll('.chapter-page');
    const dots = document.querySelectorAll('.ch-dot');
    const posEl = document.getElementById('chapter-pos');
    const prevBtn = document.getElementById('prev-ch');
    const nextBtn = document.getElementById('next-ch');

    function updateState(){{
      pages.forEach(p => p.classList.toggle('active', parseInt(p.dataset.chapter) === current));
      dots.forEach((d, i) => d.classList.toggle('active', i + 1 === current));
      posEl.textContent = labels[current - 1];
      prevBtn.disabled = current === 1;
      nextBtn.disabled = current === total;
      document.body.classList.toggle('view-3026', currentLayer === '3026');
      // reset scroll
      const active = document.querySelector('.chapter-page.active');
      if(active) active.scrollTop = 0;
      // update URL hash for shareability
      history.replaceState(null, '', '#ch' + current);
    }}

    function setLayer(page, layer) {{
      currentLayer = layer;
      page.querySelectorAll('.layer-btn').forEach(b => {{
        b.classList.toggle('active', b.dataset.layer === layer);
        b.setAttribute('aria-selected', b.dataset.layer === layer);
      }});
      page.querySelectorAll('.layer').forEach(l => {{
        const match = layer === '3026' ? l.classList.contains('layer-3026') : l.classList.contains('layer-2026');
        l.classList.toggle('active', match);
      }});
      document.body.classList.toggle('view-3026', layer === '3026');
    }}

    function goTo(n){{
      if(n < 1 || n > total) return;
      current = n;
      updateState();
      const page = document.querySelector('.chapter-page.active');
      if(page) setLayer(page, currentLayer);
    }}

    prevBtn.addEventListener('click', () => goTo(current - 1));
    nextBtn.addEventListener('click', () => goTo(current + 1));
    dots.forEach(d => d.addEventListener('click', () => goTo(parseInt(d.dataset.ch))));

    document.addEventListener('keydown', e => {{
      if(e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {{ e.preventDefault(); goTo(current + 1); }}
      if(e.key === 'ArrowLeft' || e.key === 'PageUp') {{ e.preventDefault(); goTo(current - 1); }}
      if(e.key === 'Escape') closeLore();
    }});

    // Layer toggles
    document.querySelectorAll('.layer-toggle').forEach(toggle => {{
      toggle.addEventListener('click', e => {{
        if(!e.target.classList.contains('layer-btn')) return;
        const page = e.target.closest('.chapter-page');
        setLayer(page, e.target.dataset.layer);
      }});
    }});

    // Language
    document.querySelectorAll('.lang-switch button').forEach(btn => {{
      btn.addEventListener('click', () => {{
        const lang = btn.dataset.lang;
        document.body.className = document.body.className.replace(/lang-\\w+/, '') + ' lang-' + lang;
        document.querySelectorAll('.lang-switch button').forEach(b => b.classList.toggle('active', b === btn));
        localStorage.setItem('two_layers_lang', lang);
      }});
    }});
    const savedLang = localStorage.getItem('two_layers_lang') || 'en';
    document.body.classList.add('lang-' + savedLang);
    document.querySelectorAll('.lang-switch button').forEach(b => b.classList.toggle('active', b.dataset.lang === savedLang));

    // Lore panel
    const loreOverlay = document.getElementById('lore-overlay');
    const lorePanel = document.getElementById('lore-panel');
    function openLore(){{ loreOverlay.classList.add('open'); lorePanel.classList.add('open'); }}
    function closeLore(){{ loreOverlay.classList.remove('open'); lorePanel.classList.remove('open'); }}
    document.getElementById('lore-open').addEventListener('click', openLore);
    document.getElementById('lore-close').addEventListener('click', closeLore);
    loreOverlay.addEventListener('click', closeLore);

    // Init from hash
    const hash = location.hash.replace('#ch', '');
    if(hash && !isNaN(parseInt(hash))) goTo(parseInt(hash));
    else updateState();
  }})();
  </script>

</body>
</html>
'''


def main():
    with open(DATA, 'r', encoding='utf-8') as f:
        data = json.load(f)
    html = render_html(data)
    OUT.write_text(html, encoding='utf-8')
    print(f'Wrote {OUT}')


if __name__ == '__main__':
    main()
