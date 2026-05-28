#!/usr/bin/env python3
"""
100 Days of Non — day-page generator.

Reads:    diary/day-XXX/{question.md, answer.md, fact-check.md, narration.md,
                         telemetry.json, artifacts/*.png}
          site/data/day-moods.json
Emits:    site/day/XXX/index.html
          site/assets/artifacts/day-XXX/*.png (copied)

Usage:    python3 build.py            # builds every day that has a diary folder
          python3 build.py 1 2 3      # builds specific days
"""

from __future__ import annotations

import html
import json
import os
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DIARY = ROOT / "diary"
SITE = ROOT / "site"
ASSETS_OUT = SITE / "assets" / "artifacts"
MOODS_PATH = SITE / "data" / "day-moods.json"
VERSION = "v0.1.3"

# ── verification glyphs ─────────────────────────────────────────────
GLYPHS = {
    "verified":     ("✓", "VERIFIED"),       # ✓
    "contradicted": ("✗", "CONTRADICTED"),   # ✗
    "unverified":   ("?",       "UNVERIFIED"),
    "unverifiable": ("∅", "UN-VERIFIABLE"), # ∅
    "tension":      ("⫋", "TENSION"),       # ⤬-ish; using ⫋ for variety
    "system":       ("◆", "SYSTEM NOTE"),    # ◆
    "clarification":("⚐", "CLARIFICATION"), # ⚐
    "unknown":      ("?",       "UNKNOWN"),
}

# ── small utilities ─────────────────────────────────────────────────

def esc(s: str) -> str:
    return html.escape(s, quote=False)

def read(p: Path) -> str:
    return p.read_text(encoding="utf-8") if p.exists() else ""

def split_paragraphs(text: str) -> list[str]:
    blocks = []
    for block in re.split(r"\n\s*\n", text.strip()):
        block = block.strip()
        if not block:
            continue
        blocks.append(block)
    return blocks

# ── parsers ────────────────────────────────────────────────────────

MSG_HEADING = re.compile(r"^##\s+Message\s+(\d+)\s*(?:[—-]\s*(.*))?$", re.MULTILINE)
SUBHEADING = re.compile(r"^###\s+(.+)$", re.MULTILINE)

def parse_answer(md: str) -> list[dict]:
    """Return list of message dicts: {n, headline, body_paragraphs}."""
    if not md.strip():
        return []
    # find all message anchors
    matches = list(MSG_HEADING.finditer(md))
    if not matches:
        # treat whole thing as a single block, dropping the H1 if present
        body = re.sub(r"^#[^\n]*\n", "", md, count=1).strip()
        return [{"n": 1, "headline": "", "paragraphs": split_paragraphs(body)}]
    messages = []
    for i, m in enumerate(matches):
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(md)
        chunk = md[start:end].strip()
        # strip any "### subheadings" that follow Phase-4 / structural-beats blocks
        # (we DO want them in output, but rendered quietly — keep them)
        n = int(m.group(1))
        headline = (m.group(2) or "").strip()
        messages.append({
            "n": n,
            "headline": headline,
            "raw": chunk,
            "paragraphs": split_paragraphs(chunk),
        })
    return messages

FC_ROW = re.compile(r"^\|\s*(\d+)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*$")

def classify_state(raw: str) -> str:
    raw_low = raw.lower()
    if "✓" in raw or "verified" in raw_low:
        # check for self-resolved contradiction
        if "✗" in raw and ("self-resolv" in raw_low or "self resolved" in raw_low):
            return "contradicted"
        return "verified"
    if "✗" in raw or "contradicted" in raw_low:
        return "contradicted"
    if "∅" in raw or "un-verifiable" in raw_low or "unverifiable" in raw_low:
        return "unverifiable"
    if "?" in raw and "unverified" in raw_low:
        return "unverified"
    if "?" in raw:
        return "unverified"
    if "⤬" in raw or "tension" in raw_low:
        return "tension"
    if "◆" in raw or "system" in raw_low:
        return "system"
    if "⚐" in raw or "clarification" in raw_low or "⚠" in raw:
        return "clarification"
    return "unknown"

def parse_fact_check(md: str) -> list[dict]:
    """Parse markdown table rows into claim dicts."""
    claims = []
    for line in md.splitlines():
        m = FC_ROW.match(line)
        if not m:
            continue
        if m.group(1) == "#":
            continue
        idx, claim, state_raw, source = m.groups()
        state = classify_state(state_raw)
        claims.append({
            "n": int(idx),
            "claim": claim.strip(),
            "state": state,
            "source": source.strip(),
        })
    return claims

def parse_narration(md: str) -> list[str]:
    if not md.strip():
        return []
    body = re.sub(r"^#[^\n]*\n", "", md, count=1).strip()
    # split into paragraphs, drop H2/H3 lines
    out = []
    for p in split_paragraphs(body):
        if p.startswith("#"):
            continue
        out.append(p)
    return out

def parse_question(md: str) -> dict:
    if not md.strip():
        return {"phase": "", "drop": "", "body": ""}
    # strip H1
    body = re.sub(r"^#[^\n]*\n", "", md, count=1)
    phase_m = re.search(r"\*\*Phase:\*\*\s*(.+)", body)
    phase = phase_m.group(1).strip() if phase_m else ""
    # body = after the front-matter rule
    parts = body.split("---", 1)
    qbody = parts[1].strip() if len(parts) > 1 else body.strip()
    paragraphs = split_paragraphs(qbody)
    drop = paragraphs[0] if paragraphs else ""
    rest = "\n\n".join(paragraphs[1:]) if len(paragraphs) > 1 else ""
    return {"phase": phase, "drop": drop, "body": rest}

# ── inline markdown → HTML (light) ─────────────────────────────────

INLINE_BOLD = re.compile(r"\*\*(.+?)\*\*")
INLINE_ITALIC = re.compile(r"(?<!\*)\*([^*\n]+?)\*(?!\*)")
INLINE_CODE = re.compile(r"`([^`\n]+?)`")
WIKILINK = re.compile(r"\[\[([^\]]+?)\]\]")

def inline_md(text: str) -> str:
    """Light inline markdown: bold, italic, code, wikilinks (rendered as quiet refs)."""
    text = esc(text)
    text = INLINE_CODE.sub(r"<code>\1</code>", text)
    text = INLINE_BOLD.sub(r"<strong>\1</strong>", text)
    text = INLINE_ITALIC.sub(r"<em>\1</em>", text)
    text = WIKILINK.sub(r'<span class="wikilink">\1</span>', text)
    # convert single newlines inside a paragraph into <br>
    text = text.replace("\n", "<br>\n")
    return text

# ── HTML pieces ────────────────────────────────────────────────────

def render_strip(active_day: int, last_filed: int) -> str:
    cells = []
    for d in range(1, 101):
        cls = "day-num"
        if d == active_day:
            cls += " active"
        elif d <= last_filed:
            cls += " done"
        else:
            cls += " future"
        if d <= last_filed:
            cells.append(f'<a href="/day/{d:03d}/" class="{cls}">{d:03d}</a>')
        else:
            cells.append(f'<span class="{cls}">{d:03d}</span>')
    return "".join(cells)

def render_nav(day_str: str) -> str:
    return f'''<nav class="nav" aria-label="Site navigation">
  <a href="/" class="nav-brand">100 DAYS OF NON</a>
  <a href="/day/{day_str}/" class="here">RECORD</a>
  <a href="/method/">METHOD</a>
  <a href="/archive/">ARCHIVE</a>
  <a href="/subject/">SUBJECT</a>
  <span class="nav-ver">{VERSION}</span>
</nav>'''

def render_taxonomy_legend() -> str:
    rows = []
    order = ["verified","contradicted","unverified","unverifiable","tension","system","clarification"]
    for k in order:
        glyph, label = GLYPHS[k]
        rows.append(f'<span class="lg-row"><span class="lg-glyph s-{k}">{esc(glyph)}</span><span class="lg-tag">{label}</span></span>')
    return '<div class="taxonomy"><div class="tx-label">VERIFICATION TAXONOMY</div><div class="tx-grid">' + "".join(rows) + '</div></div>'

def render_claim(c: dict) -> str:
    state = c["state"]
    glyph, label = GLYPHS.get(state, GLYPHS["unknown"])
    cls_glyph = f"c-glyph s-{state}"
    cls_tag = f"c-tag s-{state}"
    return (
        '<div class="claim">'
        f'<span class="{cls_glyph}">{esc(glyph)}</span>'
        f'<span class="{cls_tag}">{label}</span>'
        f'<span class="c-text">{inline_md(c["claim"])}</span>'
        + (f'<span class="c-sub s-{state}">{inline_md(c["source"])}</span>' if c["source"] else "")
        + '</div>'
    )

def render_factcheck(claims: list[dict], summary: dict) -> str:
    if not claims:
        return ('<div class="col-label">Fact-check &middot; pending</div>'
                '<div class="fc-empty">No claims have been extracted yet for this day. '
                'The fact-check pass runs after the answer is filed. '
                'When it lands, every verifiable claim will appear here with one of seven glyphs.</div>')
    counts = {"verified":0,"contradicted":0,"unverified":0,"unverifiable":0,"tension":0,"system":0,"clarification":0}
    for c in claims:
        counts[c["state"]] = counts.get(c["state"], 0) + 1
    # cap displayed claims to keep sidebar tractable; show overflow note
    show = claims[:24]
    overflow = max(0, len(claims) - len(show))
    rendered = "\n".join(render_claim(c) for c in show)
    overflow_html = f'<div class="fc-overflow">+ {overflow} additional claims in full record</div>' if overflow else ""
    tally_v = counts["verified"]
    tally_c = counts["contradicted"]
    tally_u = counts["unverified"]
    tally_n = counts["unverifiable"]
    tally_t = counts["tension"] + counts["system"] + counts["clarification"]
    return f'''<div class="col-label">Fact-check &middot; {len(claims)} claims</div>
{rendered}
{overflow_html}
<div class="fc-tally">
  <div><div class="tally-n">{tally_v}</div><div class="tally-l">&#10003; Verified</div></div>
  <div><div class="tally-n {'cx' if tally_c else ''}">{tally_c}</div><div class="tally-l">&#10007; Contradicted</div></div>
  <div><div class="tally-n">{tally_u}</div><div class="tally-l">? Unverified</div></div>
  <div><div class="tally-n">{tally_n}</div><div class="tally-l">&#8709; Un-veri&shy;fiable</div></div>
  <div><div class="tally-n">{tally_t}</div><div class="tally-l">&#9670; Other</div></div>
</div>'''

def render_answer(messages: list[dict], artifact_map: dict, register: str, skip_inline: set[str] | None = None) -> str:
    skip_inline = skip_inline or set()
    out = []
    for msg in messages:
        # message header
        if msg.get("headline"):
            out.append(
                f'<div class="msg-h">'
                f'<span class="msg-n">MSG {msg["n"]:02d}</span>'
                f'<span class="msg-headline">{esc(msg["headline"])}</span>'
                f'</div>'
            )
        else:
            out.append(f'<div class="msg-h"><span class="msg-n">MSG {msg["n"]:02d}</span></div>')
        for para in msg["paragraphs"]:
            if para.startswith("###"):
                # subsection — quiet
                line = para.split("\n", 1)
                title = re.sub(r"^#+\s*", "", line[0]).strip()
                rest = line[1].strip() if len(line) > 1 else ""
                out.append(f'<div class="sub-h">{esc(title)}</div>')
                if rest:
                    # render rest paragraphs
                    for p in split_paragraphs(rest):
                        out.append(render_paragraph(p, artifact_map, skip_inline))
                continue
            if para.startswith("####"):
                continue
            # check for artifact pointer
            out.append(render_paragraph(para, artifact_map, skip_inline))
    return "\n".join(out)

ARTIFACT_REF = re.compile(r"`artifacts/([\w\-\.]+\.png)`")

def render_paragraph(para: str, artifact_map: dict, skip_inline: set[str] | None = None) -> str:
    skip_inline = skip_inline or set()
    # Detect blockquote
    if para.startswith(">"):
        cleaned = re.sub(r"^>\s*", "", para, flags=re.MULTILINE).strip()
        # If contains artifact reference, render an inline artifact card
        # (skip rendering the image if the file is already placed elsewhere via mood config)
        refs = ARTIFACT_REF.findall(cleaned)
        artifact_html = ""
        if refs:
            for fname in refs:
                if fname in skip_inline:
                    continue
                if fname in artifact_map:
                    artifact_html += render_artifact(artifact_map[fname])
        # quiet quote
        return f'<aside class="quote"><div class="quote-text">{inline_md(cleaned)}</div>{artifact_html}</aside>'
    # italic-only parenthetical (message-ends notes etc.)
    if para.startswith("*(") and para.endswith(")*"):
        return f'<p class="aside">{inline_md(para)}</p>'
    if para.startswith("*[") and para.endswith("]*"):
        # artifact pointer
        return f'<p class="aside">{inline_md(para)}</p>'
    # ruler line "---"
    if para.strip() == "---":
        return '<hr class="msg-break">'
    # plain paragraph
    return f'<p>{inline_md(para)}</p>'

def render_artifact(art: dict) -> str:
    url = art["url"]
    cap = art.get("caption", "")
    cls = "artifact"
    if art.get("treatment") == "duotone":
        cls += " art-duo"
    elif art.get("treatment") == "raw":
        cls += " art-raw"
    elif art.get("treatment") == "luminosity":
        cls += " art-lum"
    bleed_cls = " art-bleed" if art.get("bleed") else ""
    return f'''<figure class="{cls}{bleed_cls}">
  <img src="{url}" alt="{esc(cap)}" loading="lazy">
  {f'<figcaption>{esc(cap)}</figcaption>' if cap else ''}
</figure>'''

def render_anchor_artifact(art: dict) -> str:
    """Hero treatment for the day's anchor image — bigger, weightier."""
    if not art:
        return ""
    return f'''<figure class="anchor-art">
  <img src="{art["url"]}" alt="{esc(art.get("caption",""))}" loading="lazy">
  <figcaption><span class="ac-id">{esc(art.get("id",""))}</span> {esc(art.get("caption",""))}</figcaption>
</figure>'''

# ── per-mood CSS overlays ──────────────────────────────────────────

def mood_css(register: str) -> str:
    """Return per-day CSS overlay that varies typography/treatment."""
    if register == "registration":
        return """
/* DAY 1 — registration: vintage commerce-certificate; cool restraint */
.pull-image { font-family: var(--sans); letter-spacing: -0.02em; }
.pull-image .han { font-family: 'Noto Serif TC','Songti TC',serif; font-weight: 700; }
.pull-image .roman { font-family: var(--mono); font-weight: 700; letter-spacing: 0.04em; }
.anchor-art img { filter: grayscale(100%) contrast(1.15) brightness(0.95); }
.day-counter::after { content: " · พ.ศ. ๒๕๖๙ "; font-size: 0.18em; font-family: 'Noto Serif TC',serif; color: var(--dim); vertical-align: super; letter-spacing: 0; }
"""
    if register == "elegy":
        return """
/* DAY 2 — elegy: funeral-booklet weight; deeper black; numerals weighty */
.pull-image { font-weight: 900; letter-spacing: -0.045em; }
.day-counter { font-weight: 900; }
.anchor-art img { filter: grayscale(100%) contrast(1.25) brightness(0.85); }
.death-ledger { margin: 56px 0; display: grid; grid-template-columns: 96px 1fr; gap: 0; border-top: 1px solid var(--faint); border-bottom: 1px solid var(--faint); }
.death-row { display: contents; }
.death-row > * { padding: 18px 16px; border-bottom: 1px solid var(--faint); }
.death-row:last-child > * { border-bottom: none; }
.death-when { font-family: var(--mono); color: var(--dim); font-size: 11px; letter-spacing: 0.12em; text-transform: uppercase; }
.death-who { color: rgba(255,255,255,0.88); font-size: 16px; line-height: 1.5; }
"""
    if register == "catharsis":
        return """
/* DAY 3 — catharsis: punk loudest; canonical portrait full-bleed; PEOPLE WERE WRONG sextet */
.anchor-art { margin: 64px -56px 88px; border: 1px solid var(--faint); }
.anchor-art img { filter: grayscale(100%) contrast(1.3) brightness(0.95); width: 100%; max-height: 92vh; object-fit: cover; }
@media (max-width: 720px) { .anchor-art { margin: 48px -24px 64px; } }
.contact-sheet { display: grid; grid-template-columns: repeat(4, 1fr); gap: 1px; background: var(--faint); margin: 56px 0; }
.contact-sheet figure { margin: 0; background: var(--bg); }
.contact-sheet img { display: block; width: 100%; aspect-ratio: 4/5; object-fit: cover; filter: grayscale(100%) contrast(1.2); }
.contact-sheet figcaption { padding: 8px 10px; font-family: var(--mono); font-size: 9px; color: var(--dim); text-transform: uppercase; letter-spacing: 0.1em; line-height: 1.3; }
@media (max-width: 720px) { .contact-sheet { grid-template-columns: repeat(2, 1fr); } }
.anaphora { margin: 96px -56px; padding: 56px; border-top: 1px solid var(--accent); border-bottom: 1px solid var(--accent); overflow: hidden; max-width: calc(100% + 112px); }
.anaphora-line { font-family: var(--sans); font-weight: 900; line-height: 0.95; letter-spacing: -0.04em; text-transform: uppercase; font-size: clamp(40px, 9vw, 144px); color: var(--fg); display: block; white-space: nowrap; overflow: visible; }
.anaphora-line .end { color: var(--accent); }
.anaphora-line:nth-child(even) { padding-left: 8vw; }
.anaphora-line:nth-child(3n) { padding-left: 4vw; }
@media (max-width: 720px) { .anaphora { margin: 64px -24px; padding: 40px 24px; } .anaphora-line { font-size: clamp(28px, 11vw, 56px); white-space: normal; } .anaphora-line:nth-child(even),.anaphora-line:nth-child(3n) { padding-left: 0; } }
.coda { margin-top: 80px; padding: 32px; border: 1px solid var(--accent); }
.coda-label { font-family: var(--mono); font-size: 11px; color: var(--accent); letter-spacing: 0.18em; text-transform: uppercase; margin-bottom: 16px; }
.coda-text { font-size: 18px; line-height: 1.55; color: var(--fg); }
"""
    return ""

# ── master template ────────────────────────────────────────────────

BASE_CSS = """
:root {
  --bg: #000;
  --fg: #fff;
  --accent: #CCFF00;
  --dim: rgba(255,255,255,0.45);
  --faint: rgba(255,255,255,0.12);
  --sans: 'Space Grotesk','Helvetica Neue',Arial,sans-serif;
  --mono: 'JetBrains Mono','Courier New',monospace;
  --micro: 11px;
  --body: 14px;
  --emph: 18px;
  --pull: clamp(56px, 13vw, 180px);
  --counter: clamp(80px, 18vw, 144px);
  --nav-h: 40px;
  --strip-h: 32px;
  --header-h: 72px;
  --col-x: 24px;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
html, body { background: var(--bg); color: var(--fg); font-family: var(--sans); font-size: var(--body); line-height: 1.6; -webkit-font-smoothing: antialiased; overflow-x: hidden; }
a { color: inherit; text-decoration: none; }
strong { font-weight: 700; color: var(--fg); }
em { font-style: italic; color: rgba(255,255,255,0.7); }
code { font-family: var(--mono); font-size: 12px; color: var(--accent); }
.wikilink { font-family: var(--mono); font-size: 12px; color: var(--dim); border-bottom: 1px dotted var(--faint); }

/* ── Global nav ─────────────────────────────────────────────── */
.nav { position: fixed; top: 0; left: 0; right: 0; height: var(--nav-h); background: var(--bg); border-bottom: 1px solid var(--faint); display: flex; align-items: center; padding: 0 48px; gap: 24px; z-index: 101; font-family: var(--mono); font-size: var(--micro); letter-spacing: 0.12em; }
.nav-brand { color: var(--fg); text-transform: uppercase; margin-right: auto; white-space: nowrap; flex-shrink: 0; font-weight: 700; }
.nav a { color: var(--dim); text-transform: uppercase; padding: 0 2px; min-height: 44px; display: inline-flex; align-items: center; }
.nav a:hover { color: var(--fg); }
.nav a.here { color: var(--accent); }
.nav-ver { color: var(--dim); font-family: var(--mono); font-size: 10px; letter-spacing: 0.12em; }

/* ── Day strip ──────────────────────────────────────────────── */
.strip { position: fixed; top: var(--nav-h); left: 0; right: 0; height: var(--strip-h); background: var(--bg); border-bottom: 1px solid var(--faint); display: flex; align-items: center; padding: 0 48px; gap: 6px; overflow-x: auto; z-index: 100; font-family: var(--mono); font-size: var(--micro); letter-spacing: 0.08em; scrollbar-width: none; }
.strip::-webkit-scrollbar { display: none; }
.day-num { color: var(--faint); padding: 2px 4px; white-space: nowrap; }
.day-num.done  { color: rgba(255,255,255,0.55); }
.day-num.active { color: var(--accent); font-weight: 700; }
.day-num.future { color: var(--faint); }
a.day-num:hover { color: rgba(255,255,255,0.85); }

/* ── 1px vertical rule ──────────────────────────────────────── */
.col-rule { position: fixed; top: var(--header-h); left: var(--col-x); bottom: 0; width: 1px; background: var(--faint); z-index: 10; pointer-events: none; }

/* ── Layout ─────────────────────────────────────────────────── */
main { margin-top: var(--header-h); padding: 56px 56px 120px; max-width: 1400px; }
.day-counter { font-family: var(--mono); font-size: var(--counter); font-weight: 700; line-height: 0.85; letter-spacing: -0.04em; color: var(--fg); }
.day-meta { font-family: var(--mono); font-size: var(--micro); color: var(--dim); letter-spacing: 0.15em; text-transform: uppercase; margin-top: 10px; }
.pull-image { font-family: var(--sans); font-size: var(--pull); font-weight: 700; line-height: 0.88; letter-spacing: -0.025em; text-transform: uppercase; white-space: nowrap; overflow: hidden; text-overflow: clip; color: var(--fg); margin: 64px -56px 0; padding-left: 56px; }
@media (max-width: 720px) { .pull-image { margin: 40px -24px 0; padding-left: 24px; font-size: clamp(40px, 13vw, 80px); } }
.phase-row { display: flex; align-items: baseline; gap: 16px; margin-top: 72px; }
.phase-tag { font-family: var(--mono); font-size: var(--micro); color: var(--dim); letter-spacing: 0.15em; text-transform: uppercase; white-space: nowrap; }
.rule-h { width: 100%; height: 1px; background: var(--faint); }
.q-label { font-family: var(--mono); font-size: var(--micro); color: var(--accent); letter-spacing: 0.15em; text-transform: uppercase; margin-top: 28px; }
.q-drop { font-family: var(--sans); font-size: clamp(40px, 6.5vw, 72px); font-weight: 800; line-height: 0.95; letter-spacing: -0.03em; text-transform: uppercase; margin-top: 16px; max-width: 900px; }
.q-text { font-size: var(--emph); line-height: 1.55; color: rgba(255,255,255,0.8); max-width: 660px; margin-top: 18px; }

/* ── Content grid ───────────────────────────────────────────── */
.content-grid { display: grid; grid-template-columns: minmax(0,1fr) 320px; gap: 0 64px; margin-top: 56px; align-items: start; }
.col-label { font-family: var(--mono); font-size: var(--micro); color: var(--dim); letter-spacing: 0.15em; text-transform: uppercase; margin-bottom: 16px; }
@media (max-width: 1024px) { .content-grid { grid-template-columns: 1fr; gap: 56px; } }

/* ── Answer column ──────────────────────────────────────────── */
.answer-col p { font-size: var(--body); line-height: 1.85; color: rgba(255,255,255,0.88); margin-top: 1.4em; }
.answer-col p:first-of-type { margin-top: 0; }
.answer-col p.aside { color: var(--dim); font-style: italic; font-size: 13px; }
.answer-col aside.quote { margin: 2em 0; padding: 12px 18px; border-left: 1px solid var(--accent); }
.answer-col aside.quote .quote-text { color: rgba(255,255,255,0.6); font-size: 13px; line-height: 1.6; }
.msg-h { display: flex; gap: 16px; align-items: baseline; margin-top: 3em; padding-top: 18px; border-top: 1px solid var(--faint); }
.msg-h:first-child { margin-top: 0; padding-top: 0; border-top: none; }
.msg-n { font-family: var(--mono); font-size: 11px; color: var(--accent); letter-spacing: 0.15em; flex-shrink: 0; }
.msg-headline { font-family: var(--mono); font-size: 11px; color: var(--dim); letter-spacing: 0.06em; line-height: 1.5; text-transform: uppercase; }
.sub-h { font-family: var(--mono); font-size: 11px; color: var(--dim); letter-spacing: 0.15em; text-transform: uppercase; margin-top: 2em; margin-bottom: 0.5em; }
hr.msg-break { border: none; height: 1px; background: var(--faint); margin: 2em 0; }

/* ── Narration ──────────────────────────────────────────────── */
.narration { margin-top: 80px; padding-left: 28px; border-left: 1px solid var(--faint); }
.narration p { font-size: var(--body); line-height: 1.85; color: rgba(255,255,255,0.45); margin-top: 1.3em; }
.narration p:first-of-type { margin-top: 0; }

/* ── Fact-check column ──────────────────────────────────────── */
.fc-col { font-family: var(--mono); font-size: 11px; position: sticky; top: calc(var(--header-h) + 16px); max-height: calc(100vh - var(--header-h) - 32px); overflow-y: auto; padding-right: 8px; scrollbar-width: thin; scrollbar-color: var(--faint) transparent; }
.fc-col::-webkit-scrollbar { width: 4px; }
.fc-col::-webkit-scrollbar-thumb { background: var(--faint); }
@media (max-width: 1024px) { .fc-col { position: static; max-height: none; overflow: visible; padding-right: 0; } }
.fc-empty { color: var(--dim); font-style: italic; font-family: var(--sans); font-size: 13px; line-height: 1.6; padding: 12px; border: 1px dashed var(--faint); }
.claim { display: grid; grid-template-columns: 14px 96px 1fr; column-gap: 6px; padding: 8px 0; border-bottom: 1px solid rgba(255,255,255,0.06); align-items: start; }
.c-glyph { line-height: 1.4; }
.c-tag { color: rgba(255,255,255,0.3); text-transform: uppercase; letter-spacing: 0.06em; line-height: 1.4; }
.c-text { color: rgba(255,255,255,0.72); line-height: 1.4; }
.c-sub { grid-column: 3; color: rgba(255,255,255,0.32); font-size: 10px; margin-top: 2px; line-height: 1.4; }
.s-verified, .c-glyph.s-verified { color: rgba(255,255,255,0.7); }
.s-contradicted, .c-glyph.s-contradicted, .c-tag.s-contradicted, .c-sub.s-contradicted { color: var(--accent); }
.s-unverified, .c-glyph.s-unverified { color: rgba(255,255,255,0.4); }
.s-unverifiable, .c-glyph.s-unverifiable { color: rgba(255,255,255,0.3); }
.s-tension, .c-glyph.s-tension, .c-tag.s-tension { color: var(--accent); }
.s-system, .c-glyph.s-system { color: rgba(255,255,255,0.3); }
.s-clarification, .c-glyph.s-clarification { color: rgba(255,255,255,0.4); }
.fc-overflow { font-size: 10px; color: rgba(255,255,255,0.25); margin-top: 12px; }
.fc-tally { display: grid; grid-template-columns: repeat(5, 1fr); gap: 0; margin-top: 20px; padding-top: 14px; border-top: 1px solid var(--faint); }
.tally-n { font-size: 22px; font-weight: 700; line-height: 1; color: rgba(255,255,255,0.85); }
.tally-n.cx { color: var(--accent); }
.tally-l { font-size: 9px; color: rgba(255,255,255,0.25); text-transform: uppercase; letter-spacing: 0.08em; margin-top: 4px; }

/* ── Artifacts ──────────────────────────────────────────────── */
figure.artifact { margin: 40px 0; border: 1px solid var(--faint); }
figure.artifact img { display: block; width: 100%; height: auto; filter: grayscale(100%) contrast(1.2) brightness(0.9); }
figure.artifact.art-bleed { margin-left: -56px; margin-right: -56px; border-left: none; border-right: none; }
@media (max-width: 720px) { figure.artifact.art-bleed { margin-left: -24px; margin-right: -24px; } }
figure.artifact figcaption { font-family: var(--mono); font-size: 10px; color: var(--dim); padding: 12px 16px; text-transform: uppercase; letter-spacing: 0.12em; border-top: 1px solid var(--faint); line-height: 1.5; }
figure.anchor-art { margin: 48px 0; border: 1px solid var(--faint); }
figure.anchor-art img { display: block; width: 100%; height: auto; }
figure.anchor-art figcaption { font-family: var(--mono); font-size: 10px; color: var(--dim); padding: 14px 18px; text-transform: uppercase; letter-spacing: 0.14em; border-top: 1px solid var(--faint); display: flex; gap: 12px; align-items: baseline; }
.ac-id { color: var(--accent); flex-shrink: 0; }

/* ── Telemetry block ────────────────────────────────────────── */
.telemetry { margin-top: 88px; padding-top: 32px; border-top: 1px solid var(--faint); }
.t-number { font-family: var(--mono); font-size: var(--counter); font-weight: 700; line-height: 0.85; letter-spacing: -0.04em; color: rgba(255,255,255,0.08); }
.t-meta { font-family: var(--mono); font-size: var(--micro); color: var(--dim); letter-spacing: 0.12em; text-transform: uppercase; margin-top: 10px; }
.t-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; margin-top: 28px; padding-top: 18px; border-top: 1px solid var(--faint); }
.t-cell .t-cell-n { font-family: var(--mono); font-size: 28px; font-weight: 700; line-height: 1; color: var(--fg); }
.t-cell .t-cell-l { font-family: var(--mono); font-size: 9px; color: var(--dim); text-transform: uppercase; letter-spacing: 0.08em; margin-top: 6px; }

/* ── Taxonomy legend ────────────────────────────────────────── */
.taxonomy { margin-top: 64px; padding-top: 24px; border-top: 1px solid var(--faint); }
.tx-label { font-family: var(--mono); font-size: 10px; color: var(--dim); letter-spacing: 0.18em; text-transform: uppercase; margin-bottom: 16px; }
.tx-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 8px 24px; font-family: var(--mono); font-size: 10px; }
.lg-row { display: flex; gap: 8px; align-items: baseline; }
.lg-glyph { color: var(--fg); }
.lg-tag { color: var(--dim); letter-spacing: 0.1em; text-transform: uppercase; }

/* ── Footer ─────────────────────────────────────────────────── */
footer { margin-top: 64px; padding-top: 24px; border-top: 1px solid var(--faint); font-family: var(--mono); font-size: var(--micro); color: var(--dim); letter-spacing: 0.1em; text-transform: uppercase; display: flex; justify-content: space-between; flex-wrap: wrap; gap: 8px; }

/* ── Mobile ─────────────────────────────────────────────────── */
@media (max-width: 720px) {
  main { padding: 36px 24px 80px; }
  .nav { padding: 0 16px; gap: 14px; overflow-x: auto; }
  .nav::-webkit-scrollbar { display: none; }
  .strip { padding: 0 16px; }
  .col-rule { left: 8px; }
  .q-drop { font-size: clamp(36px, 11vw, 56px); }
  figure.artifact { margin: 32px 0; }
}
"""

PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{day_str} — {title} · 100 Days of Non</title>
<meta name="description" content="{desc}">
<meta property="og:type" content="article">
<meta property="og:url" content="https://100.nonarkara.org/day/{day_str}/">
<meta property="og:title" content="Day {day_str} — {title} · 100 Days of Non">
<meta property="og:description" content="{desc}">
<meta property="og:site_name" content="100 Days of Non">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Space+Grotesk:wght@400;500;700;800&family=Noto+Serif+TC:wght@700;900&display=swap" rel="stylesheet">
<style>
{base_css}
{mood_css}
</style>
</head>
<body>
{nav}
<nav class="strip" aria-label="Day navigation">{strip}</nav>
<div class="col-rule" aria-hidden="true"></div>
<main>
  <div class="day-counter">{day_str}</div>
  <div class="day-meta">{date_human} &nbsp;·&nbsp; PHASE {phase_short} &nbsp;·&nbsp; DAY {day_int} OF 100 &nbsp;·&nbsp; {register_upper}</div>

  {pull_html}

  <div class="phase-row">
    <span class="phase-tag">Phase {phase_label}</span>
    <div class="rule-h"></div>
  </div>

  <div class="q-label">Question</div>
  <p class="q-drop">{q_drop}</p>
  {q_body_html}

  {anchor_art_html}
  {anchor_extra_html}

  <div class="content-grid">
    <div class="answer-col">
      <div class="col-label">Answer &mdash; Non Arkara &middot; {word_count} words &middot; {msg_count} messages</div>
      {answer_html}
      {extra_html}
      {narration_html}
    </div>
    <aside class="fc-col">
      {factcheck_html}
    </aside>
  </div>

  <section class="telemetry">
    <div class="t-number">{latency_str}</div>
    <div class="t-meta">{telemetry_meta}</div>
    <div class="t-grid">
      <div class="t-cell"><div class="t-cell-n">{word_count}</div><div class="t-cell-l">words</div></div>
      <div class="t-cell"><div class="t-cell-n">{msg_count}</div><div class="t-cell-l">messages</div></div>
      <div class="t-cell"><div class="t-cell-n">{artifact_count}</div><div class="t-cell-l">artifacts</div></div>
      <div class="t-cell"><div class="t-cell-n">{claim_count}</div><div class="t-cell-l">claims</div></div>
    </div>
  </section>

  {taxonomy_html}

  <footer>
    <span>100 Days of Non &middot; Non Arkara &middot; {version}</span>
    <span>Day {day_str} of 100 &middot; <a href="/">Lobby</a> &middot; <a href="/day/{prev_str}/">Prev</a> · <a href="/day/{next_str}/">Next</a></span>
  </footer>
</main>
</body>
</html>
"""

# ── per-mood content extras ────────────────────────────────────────

def render_pull(mood: dict, register: str) -> str:
    """The single typographic anchor at the top of the page."""
    pull = mood.get("pull", "")
    if register == "registration":
        han = mood.get("pull_han", "")
        roman = mood.get("pull_roman", "")
        return f'<div class="pull-image" aria-hidden="true"><span class="han">{esc(han)}</span> &nbsp; <span class="roman">{esc(roman)}</span></div>'
    return f'<div class="pull-image" aria-hidden="true">{esc(pull)}</div>'

def render_anaphora(lines: list[dict]) -> str:
    rows = []
    for ln in lines:
        prefix = esc(ln.get("prefix", "PEOPLE WERE WRONG TO THINK"))
        end = esc(ln.get("end", ""))
        rows.append(f'<span class="anaphora-line">{prefix} <span class="end">{end}</span></span>')
    return '<section class="anaphora" aria-label="People were wrong">' + "\n".join(rows) + '</section>'

def render_contact_sheet(artifacts: list[dict]) -> str:
    figs = []
    for a in artifacts:
        figs.append(
            f'<figure><img src="{a["url"]}" alt="{esc(a.get("caption",""))}" loading="lazy">'
            f'<figcaption>{esc(a.get("caption",""))}</figcaption></figure>'
        )
    return '<section class="contact-sheet" aria-label="Photographic contact sheet">' + "\n".join(figs) + '</section>'

def render_death_ledger(rows: list[dict]) -> str:
    html_rows = []
    for r in rows:
        html_rows.append(f'<div class="death-row"><div class="death-when">{esc(r["when"])}</div><div class="death-who">{esc(r["who"])}</div></div>')
    return '<section class="death-ledger" aria-label="Death chronology">' + "\n".join(html_rows) + '</section>'

def render_coda(text: str, label: str = "Coda — Non's voice") -> str:
    return f'<aside class="coda"><div class="coda-label">{esc(label)}</div><div class="coda-text">{inline_md(text)}</div></aside>'

# ── main build ─────────────────────────────────────────────────────

def build_day(day: int, all_filed_days: list[int], moods: dict) -> None:
    day_str = f"{day:03d}"
    diary_dir = DIARY / f"day-{day_str}"
    if not diary_dir.exists():
        print(f"[skip] {diary_dir} not found")
        return

    site_dir = SITE / "day" / day_str
    site_dir.mkdir(parents=True, exist_ok=True)

    # ── load source ──
    answer_md = read(diary_dir / "answer.md")
    question_md = read(diary_dir / "question.md")
    narration_md = read(diary_dir / "narration.md")
    fc_md = read(diary_dir / "fact-check.md")
    telemetry = {}
    tel_path = diary_dir / "telemetry.json"
    if tel_path.exists():
        try:
            telemetry = json.loads(tel_path.read_text())
        except Exception as e:
            print(f"[warn] telemetry.json parse failed for {day_str}: {e}")

    # ── copy artifacts ──
    out_art_dir = ASSETS_OUT / f"day-{day_str}"
    out_art_dir.mkdir(parents=True, exist_ok=True)
    artifact_map: dict[str, dict] = {}
    src_art_dir = diary_dir / "artifacts"
    if src_art_dir.exists():
        for f in sorted(src_art_dir.glob("*.png")):
            dst = out_art_dir / f.name
            if dst.exists():
                dst.chmod(0o644)
            shutil.copyfile(f, dst)
            dst.chmod(0o644)
            artifact_map[f.name] = {
                "url": f"/assets/artifacts/day-{day_str}/{f.name}",
                "caption": "",
            }

    # ── load mood ──
    mood = moods.get(day_str, {})
    register = mood.get("register", "default")

    # captions for artifacts from mood config
    for art_def in mood.get("artifact_captions", []):
        fname = art_def["file"]
        if fname in artifact_map:
            artifact_map[fname].update({
                "caption": art_def.get("caption", ""),
                "id": art_def.get("id", ""),
                "treatment": art_def.get("treatment", "luminosity"),
                "bleed": art_def.get("bleed", False),
            })

    # ── parse ──
    messages = parse_answer(answer_md)
    fc_claims = parse_fact_check(fc_md)
    narration_paras = parse_narration(narration_md)
    q = parse_question(question_md)

    # ── compose pieces ──
    title = mood.get("title", "")
    desc = mood.get("desc", q.get("body", "")[:160])
    phase_full = telemetry.get("phase") or q.get("phase") or mood.get("phase","")
    phase_short = mood.get("phase_short", phase_full.split("—")[0].strip() if "—" in phase_full else "I")
    phase_label = phase_full if phase_full else mood.get("phase","")

    # word count: prefer telemetry; fall back to a fresh count of the parsed body
    word_count = telemetry.get("answer_word_count", 0)
    if not word_count:
        text_for_count = " ".join(p for m in messages for p in m["paragraphs"])
        word_count = len(re.findall(r"\b\w+\b", text_for_count))
    msg_count = telemetry.get("answer_message_count", 0) or len(messages)
    artifact_count = telemetry.get("artifact_count", 0) or len(artifact_map)
    fc_sum = telemetry.get("fact_check_summary", {})
    claim_count = fc_sum.get("total_claims", 0) or len(fc_claims)

    pull_html = render_pull(mood, register)

    q_drop = mood.get("q_drop") or q.get("drop","").replace("\n","<br>")
    q_body_html = ""
    body = q.get("body","")
    if body:
        # split into paragraphs
        paras = split_paragraphs(body)
        q_body_html = "\n".join(f'<p class="q-text">{inline_md(p)}</p>' for p in paras)

    anchor_art_html = ""
    if mood.get("anchor_artifact"):
        af = mood["anchor_artifact"]
        if af in artifact_map:
            anchor_art_html = render_anchor_artifact(artifact_map[af])

    # files placed elsewhere via mood config — don't render inline too
    skip_inline = set(mood.get("contact_sheet", [])) | set(mood.get("inline_artifacts", []))
    if mood.get("anchor_artifact"):
        skip_inline.add(mood["anchor_artifact"])
    answer_html = render_answer(messages, artifact_map, register, skip_inline) if messages else \
        '<p class="aside">No answer has been filed yet for this day. When Non answers, this surface populates.</p>'

    # mood-specific inserts — split into "anchor_extra" (between portrait and answer)
    # and "tail_extra" (between answer body and narration)
    anchor_extra_parts: list[str] = []
    tail_extra_parts: list[str] = []
    if register == "elegy":
        ledger = mood.get("death_ledger")
        if ledger:
            anchor_extra_parts.append(render_death_ledger(ledger))
        for fname in mood.get("inline_artifacts", []):
            if fname in artifact_map:
                tail_extra_parts.append(render_artifact(artifact_map[fname]))
    elif register == "catharsis":
        ana = mood.get("anaphora")
        if ana:
            anchor_extra_parts.append(render_anaphora(ana))
        sheet = mood.get("contact_sheet", [])
        sheet_full = [artifact_map[f] for f in sheet if f in artifact_map]
        if sheet_full:
            tail_extra_parts.append(render_contact_sheet(sheet_full))
        for fname in mood.get("inline_artifacts", []):
            if fname in artifact_map:
                tail_extra_parts.append(render_artifact(artifact_map[fname]))
        if mood.get("coda"):
            tail_extra_parts.append(render_coda(mood["coda"], mood.get("coda_label","Coda — Non's voice")))
    elif register == "registration":
        for fname in mood.get("inline_artifacts", []):
            if fname in artifact_map:
                tail_extra_parts.append(render_artifact(artifact_map[fname]))

    anchor_extra_html = "\n".join(anchor_extra_parts)
    extra_html = "\n".join(tail_extra_parts)

    narration_html = ""
    if narration_paras:
        narration_html = '<div class="narration"><div class="col-label">Narration &mdash; Biographer</div>' + \
            "\n".join(f"<p>{inline_md(p)}</p>" for p in narration_paras) + "</div>"

    factcheck_html = render_factcheck(fc_claims, fc_sum)

    # latency
    latency_str = telemetry.get("latency_display","—:—:—")
    if latency_str == "—:—:—":
        latency_str = "&mdash;:&mdash;:&mdash;"
    telemetry_meta = mood.get("telemetry_note", "Response latency pending — Telegram bot not yet wired")

    last_filed = max(all_filed_days) if all_filed_days else day
    strip_html = render_strip(day, last_filed)
    nav_html = render_nav(day_str)
    taxonomy_html = render_taxonomy_legend()

    prev_str = f"{max(1, day-1):03d}"
    next_str = f"{min(100, day+1):03d}"

    date_human = mood.get("date_human","")
    if not date_human:
        # try to pull from telemetry T0
        t0 = telemetry.get("T0_local_approx") or telemetry.get("T0_approx") or ""
        date_human = t0.split(" ")[0] if t0 else ""

    page = PAGE_TEMPLATE.format(
        day_str=day_str,
        day_int=day,
        prev_str=prev_str,
        next_str=next_str,
        title=esc(title),
        desc=esc(desc.replace("\n"," ")),
        base_css=BASE_CSS,
        mood_css=mood_css(register),
        nav=nav_html,
        strip=strip_html,
        date_human=esc(date_human),
        phase_label=esc(phase_label),
        phase_short=esc(phase_short),
        register_upper=esc(register.upper()),
        pull_html=pull_html,
        q_drop=q_drop,
        q_body_html=q_body_html,
        anchor_art_html=anchor_art_html,
        anchor_extra_html=anchor_extra_html,
        answer_html=answer_html,
        extra_html=extra_html,
        narration_html=narration_html,
        factcheck_html=factcheck_html,
        latency_str=latency_str,
        telemetry_meta=esc(telemetry_meta),
        word_count=word_count,
        msg_count=msg_count,
        artifact_count=artifact_count,
        claim_count=claim_count,
        taxonomy_html=taxonomy_html,
        version=VERSION,
    )
    (site_dir / "index.html").write_text(page, encoding="utf-8")
    print(f"[ok]   day {day_str} → site/day/{day_str}/index.html ({len(page):,} bytes)")

def main():
    moods = json.loads(MOODS_PATH.read_text()) if MOODS_PATH.exists() else {}
    # all days that have a diary folder
    all_diary_days = []
    for d in sorted(DIARY.glob("day-*")):
        try:
            n = int(d.name.split("-")[1])
            # only days with a non-empty answer.md count as "filed" for strip
            if (d / "answer.md").exists() and (d / "answer.md").stat().st_size > 100:
                all_diary_days.append(n)
        except Exception:
            pass

    if len(sys.argv) > 1:
        targets = [int(x) for x in sys.argv[1:]]
    else:
        targets = all_diary_days

    for d in targets:
        build_day(d, all_diary_days, moods)

if __name__ == "__main__":
    main()
