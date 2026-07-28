#!/usr/bin/env python3
"""
build_layers.py — generate the gated dual-timeline reader.

Reads:  novel/layers-chapters/*.md
Writes: site/layers/index.html

Gate law (desktop):
  1. Read 2026 column to the end → unlocks that chapter's 3026 column
  2. Read 3026 column to the end → unlocks the next chapter's 2026 column
  3. Columns that are locked refuse scroll / show a hold message

Mobile: stacked single-column with the same unlock sequence (2026 → 3026 → next).
"""

from __future__ import annotations

import html as html_module
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "novel" / "layers-chapters"
OUT = ROOT / "site" / "layers" / "index.html"
ART = ROOT / "site" / "assets" / "artworks"

# Verified plates only (wrong Commons hits blacklisted)
TRUSTED = {
    "hopper-nighthawks.jpg",
    "friedrich-wanderer.jpg",
    "caravaggio-thomas.jpg",
    "hiroshige-rain.jpg",
    "rembrandt-philosopher.jpg",
    "vermeer-balance.jpg",
    "bosch-garden.jpg",
    "goya-sleep-of-reason.jpg",
    "schiele-embrace.jpg",
    "caillebotte-rain.jpg",
}

# Story-role remaps when a chapter asks for a missing/wrong file
FALLBACKS = {
    "magritte-false-mirror.jpg": "vermeer-balance.jpg",
    "de-chirico-street.jpg": "friedrich-wanderer.jpg",
    "delvaux-hands.jpg": "caravaggio-thomas.jpg",
    "redon-eye.jpg": "goya-sleep-of-reason.jpg",
    "klimt-kiss.jpg": "schiele-embrace.jpg",
    "munch-scream.jpg": "goya-sleep-of-reason.jpg",
}


def resolve_art(src: str) -> str:
    name = Path(src).name
    if name in FALLBACKS:
        name = FALLBACKS[name]
    if name in TRUSTED and (ART / name).exists():
        return f"/assets/artworks/{name}"
    for c in sorted(TRUSTED):
        if (ART / c).exists():
            return f"/assets/artworks/{c}"
    return src


def h(s: str) -> str:
    return html_module.escape(s)


def md_inline(text: str) -> str:
    text = h(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*(.+?)\*", r"<em>\1</em>", text)
    text = re.sub(r"`(.+?)`", r"<code>\1</code>", text)
    return text


def parse_chapter(path: Path) -> dict:
    raw = path.read_text(encoding="utf-8")
    title_m = re.search(r"^#\s+(.+)$", raw, re.M)
    title = title_m.group(1).strip() if title_m else path.stem

    parts = re.split(r"^##\s+(2026 · Doc|3026 · Archive)\s*$", raw, flags=re.M)
    # parts[0] = preamble, then pairs of (heading, body)
    sim_body = ""
    arc_body = ""
    for i in range(1, len(parts), 2):
        heading = parts[i]
        body = parts[i + 1] if i + 1 < len(parts) else ""
        if heading.startswith("2026"):
            sim_body = body
        else:
            arc_body = body

    return {
        "id": int(re.match(r"^(\d+)", path.name).group(1)),
        "title": title,
        "short": re.sub(r"^CH\d+\s*[—–-]\s*", "", title).strip(),
        "sim_html": render_body(sim_body, layer="sim"),
        "arc_html": render_body(arc_body, layer="arc"),
    }


def render_body(body: str, layer: str) -> str:
    """Convert chapter body markdown+HTML islands into reader HTML."""
    out: list[str] = []
    lines = body.strip("\n").split("\n")
    i = 0
    para: list[str] = []
    in_blockquote = False
    bq: list[str] = []

    def flush_para():
        nonlocal para
        if not para:
            return
        text = " ".join(para).strip()
        para = []
        if not text:
            return
        cls = ""
        if layer == "arc" and text.startswith("[UNVERIFIED"):
            cls = ' class="signal"'
        elif layer == "arc" and text.startswith("[END SIGNAL"):
            cls = ' class="meta"'
        elif layer == "arc" and re.match(r"^(SYSTEM|CASE|Participant|Temporal|Behavioral|Cardiac|Neural|Muscular|STATUS|OVERRIDE)", text):
            # keep as normal prose; meta lines marked elsewhere
            pass
        out.append(f"<p{cls}>{md_inline(text)}</p>")

    def flush_bq():
        nonlocal bq, in_blockquote
        if not bq:
            in_blockquote = False
            return
        bits = []
        for ln in bq:
            cleaned = re.sub(r"^>\s?", "", ln)
            bits.append(f"<p>{md_inline(cleaned)}</p>")
        inner = "\n".join(bits)
        out.append(f'<aside class="msg-text-only">{inner}</aside>')
        bq = []
        in_blockquote = False

    while i < len(lines):
        line = lines[i]

        # HTML figure blocks (plate / msg-video) — pass through with art remap
        if line.strip().startswith("<figure"):
            flush_para()
            flush_bq()
            chunk = [line]
            i += 1
            while i < len(lines) and "</figure>" not in lines[i - 1]:
                chunk.append(lines[i])
                if "</figure>" in lines[i]:
                    i += 1
                    break
                i += 1
            block = "\n".join(chunk)
            # remap artwork src on <img> only — never touch <video src>
            def repl_img(m):
                return f'<img{m.group(1)}src="{resolve_art(m.group(2))}"'

            block = re.sub(r"<img([^>]*?)src=\"([^\"]+)\"", repl_img, block)
            out.append(block)
            continue

        # horizontal rules
        if re.match(r"^-{3,}\s*$", line.strip()):
            flush_para()
            flush_bq()
            i += 1
            continue

        # blockquotes (mysterious texts)
        if line.startswith(">"):
            flush_para()
            in_blockquote = True
            bq.append(line)
            i += 1
            continue
        if in_blockquote and line.strip() == "":
            flush_bq()
            i += 1
            continue
        if in_blockquote and not line.startswith(">"):
            flush_bq()
            # fall through to handle this line

        if line.strip() == "":
            flush_para()
            i += 1
            continue

        # skip markdown headings inside body
        if line.startswith("#"):
            i += 1
            continue

        para.append(line.strip())
        i += 1

    flush_para()
    flush_bq()
    return "\n".join(out)


CHAPTERS = [parse_chapter(p) for p in sorted(SRC.glob("*.md"))]


def ch_buttons() -> str:
    bits = []
    for c in CHAPTERS:
        locked = " locked" if c["id"] > 1 else ""
        active = " active" if c["id"] == 1 else ""
        bits.append(
            f'<button class="ch-sel-btn{active}{locked}" data-ch="{c["id"]}" '
            f'type="button" {"disabled" if c["id"] > 1 else ""}>'
            f'{c["id"]:02d}</button>'
        )
    return "\n".join(bits)


def spreads() -> str:
    chunks = []
    for c in CHAPTERS:
        active = " active" if c["id"] == 1 else ""
        chunks.append(f'''
    <section class="spread{active}" data-ch="{c["id"]}" data-world="sim" data-gate="sim">
      <div class="split">
        <div class="col sim" id="sim-{c["id"]}" data-side="sim" data-ch="{c["id"]}">
          <p class="col-head">2026 <b>·</b> Doc</p>
          <p class="col-tag">{h(c["short"])}</p>
          <div class="prose">
{c["sim_html"]}
          </div>
          <div class="gate-end" data-end="sim" hidden>
            <p class="gate-msg">End of 2026 · Chapter {c["id"]}. Cross the gutter — read 3026 to unlock the next.</p>
            <button type="button" class="gate-btn" data-unlock="arc">Open 3026 archive →</button>
          </div>
        </div>

        <div class="gutter" aria-hidden="true"></div>

        <div class="col arc is-locked" id="arc-{c["id"]}" data-side="arc" data-ch="{c["id"]}">
          <div class="lock-veil" aria-hidden="true">
            <p>3026 locked</p>
            <p class="lock-sub">Finish 2026 first.</p>
          </div>
          <p class="col-head">3026 <b>·</b> the Archive</p>
          <p class="col-tag">CASE 44-44 · SESSION 2848 · CH{c["id"]:02d}</p>
          <div class="prose">
{c["arc_html"]}
          </div>
          <div class="gate-end" data-end="arc" hidden>
            <p class="gate-msg">End of 3026 · Chapter {c["id"]}.</p>
            <button type="button" class="gate-btn" data-unlock="next">{"Continue to Chapter " + str(c["id"]+1) + " →" if c["id"] < len(CHAPTERS) else "Close the file →"}</button>
          </div>
        </div>
      </div>
    </section>''')
    return "\n".join(chunks)


HTML = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Two Layers — Doc / Pui</title>
  <meta name="description" content="A bingeable dual-timeline novel. 2026 Bangkok — Doc receives videos from nowhere. 3026 Hub — Pui has watched him live it 2,847 times. Finish one side to unlock the other.">
  <meta property="og:title" content="Two Layers — Doc / Pui">
  <meta property="og:description" content="Two worlds. One gate. Read 2026 to the end, then 3026, then the next.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;700&family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,500;1,7..72,400&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/assets/css/surface.css">
  <style>
    html, body {{ height: 100%; }}
    body {{
      display: flex; flex-direction: column; min-height: 100vh; overflow: hidden;
      --sim-paper: #f4efe6; --sim-ink: #1a1612; --sim-soft: #6b6358; --sim-faint: #9a9084;
      --sim-accent: #f59e0b; --sim-rule: #d4cbb8;
      --arc-paper: #0c1016; --arc-ink: #d6dde6; --arc-soft: #8b96a5; --arc-faint: #5a6573;
      --arc-accent: #f59e0b; --arc-rule: #243041;
    }}
    .lh {{
      flex: 0 0 auto; padding: 0.85rem clamp(1rem, 3vw, 1.8rem);
      border-bottom: 1px solid var(--rule); background: var(--paper); z-index: 10;
    }}
    .lh-row {{
      display: flex; align-items: baseline; justify-content: space-between;
      flex-wrap: wrap; gap: 0.4rem 1.2rem; max-width: 100rem; margin: 0 auto;
    }}
    .lh .mark {{
      font-family: var(--mono); font-size: 0.6875rem; letter-spacing: 0.2em;
      text-transform: uppercase; color: var(--ink);
    }}
    .lh .mark b {{ color: var(--amber); font-weight: 700; }}
    .lh .thesis {{
      font-style: italic; color: var(--soft); font-size: 0.9rem; font-family: var(--serif);
    }}
    .lh-back {{
      font-family: var(--mono); font-size: 0.625rem; letter-spacing: 0.12em;
      text-transform: uppercase; color: var(--soft); text-decoration: none;
      border-bottom: 1px solid var(--rule); padding-bottom: 2px;
    }}
    .lh-back:hover {{ color: var(--amber); border-color: var(--amber); }}

    .ch-sel {{
      display: flex; justify-content: center; flex-wrap: wrap; gap: 0.3rem;
      padding: 0.55rem clamp(1rem, 3vw, 1.8rem);
      border-bottom: 1px solid var(--rule); background: var(--paper);
    }}
    .ch-sel-btn {{
      font-family: var(--mono); font-size: 0.6rem; letter-spacing: 0.12em;
      text-transform: uppercase; background: transparent; border: 1px solid var(--rule);
      color: var(--soft); padding: 0.45rem 0.75rem; cursor: pointer; line-height: 1;
      min-height: 44px; min-width: 44px;
    }}
    .ch-sel-btn:hover:not(:disabled) {{ border-color: var(--soft); color: var(--ink); }}
    .ch-sel-btn.active {{ background: var(--ink); color: var(--paper); border-color: var(--ink); font-weight: 700; }}
    .ch-sel-btn.locked, .ch-sel-btn:disabled {{
      opacity: 0.35; cursor: not-allowed;
    }}
    .ch-sel-btn.done:not(.active) {{ border-color: var(--amber); color: var(--amber); }}

    .pivot {{
      display: none; width: 100%; justify-content: center; gap: 0.3rem; margin-top: 0.4rem;
    }}
    .pivot button {{
      font-family: var(--mono); font-size: 0.6rem; letter-spacing: 0.1em; text-transform: uppercase;
      background: transparent; border: 1px solid var(--rule); color: var(--soft);
      padding: 0.55rem 0.9rem; min-height: 44px; cursor: pointer;
    }}
    .pivot button.active {{ background: var(--ink); color: var(--paper); border-color: var(--ink); }}

    .reader {{ flex: 1 1 auto; position: relative; overflow: hidden; }}
    .spread {{ position: absolute; inset: 0; display: none; }}
    .spread.active {{ display: block; }}
    .split {{ height: 100%; display: grid; grid-template-columns: 1fr 2px 1fr; }}
    .gutter {{ background: var(--rule); position: relative; }}
    .gutter::before {{
      content: ''; position: absolute; left: 50%; top: 50%; transform: translate(-50%, -50%);
      width: 6px; height: 6px; background: var(--amber); border-radius: 50%;
    }}

    .col {{
      height: 100%; overflow-y: auto;
      padding: clamp(1.8rem, 4vw, 3rem) clamp(1.2rem, 4vw, 3rem) 6rem;
      scrollbar-width: thin; position: relative;
    }}
    .col.sim {{ background: var(--sim-paper); color: var(--sim-ink); }}
    .col.arc {{ background: var(--arc-paper); color: var(--arc-ink); }}
    .col.is-locked {{ overflow: hidden; }}
    .col.is-locked .prose,
    .col.is-locked .col-tag,
    .col.is-locked .col-head {{ filter: blur(2px); opacity: 0.35; pointer-events: none; user-select: none; }}

    .lock-veil {{
      display: none; position: sticky; top: 30%; z-index: 5;
      text-align: center; font-family: var(--mono); letter-spacing: 0.14em;
      text-transform: uppercase; font-size: 0.75rem; padding: 1.5rem;
    }}
    .col.arc .lock-veil {{ color: var(--arc-accent); }}
    .col.sim .lock-veil {{ color: var(--sim-accent); }}
    .col.is-locked .lock-veil {{ display: block; }}
    .lock-sub {{ margin-top: 0.6rem; letter-spacing: 0.08em; opacity: 0.7; font-size: 0.65rem; }}

    .col-head {{
      font-family: var(--mono); font-size: 0.625rem; letter-spacing: 0.18em;
      text-transform: uppercase; margin-bottom: 0.4rem;
    }}
    .col.sim .col-head {{ color: var(--sim-soft); }}
    .col.arc .col-head {{ color: var(--arc-soft); }}
    .col-head b {{ color: var(--amber); font-weight: 700; }}
    .col-tag {{
      font-style: italic; font-family: var(--serif); font-size: 0.85rem;
      margin-bottom: 2.4rem; line-height: 1.5;
    }}
    .col.sim .col-tag {{ color: var(--sim-faint); }}
    .col.arc .col-tag {{ color: var(--arc-faint); }}

    .prose p {{
      font-family: var(--serif);
      font-size: clamp(1.0625rem, 1.6vw, 1.1875rem);
      line-height: 1.72; margin-bottom: 1.1em; text-wrap: pretty;
    }}
    .col.sim .prose p:first-of-type {{
      font-size: clamp(1.25rem, 2vw, 1.5rem); line-height: 1.55;
    }}
    .col.arc .prose p {{
      font-family: var(--mono); font-size: 0.8125rem; line-height: 1.65;
      letter-spacing: 0.01em;
    }}
    .col.arc .prose p.signal {{
      color: var(--amber); border-left: 2px solid var(--amber);
      padding-left: 0.9rem; margin: 1.6em 0; font-style: italic;
    }}
    .col.arc .prose p.meta {{
      color: var(--arc-faint); font-size: 0.7rem; letter-spacing: 0.08em;
      text-transform: uppercase;
    }}

    .plate {{
      margin: 2rem 0; border: 1px solid currentColor; opacity: 0.95;
    }}
    .col.sim .plate {{ border-color: var(--sim-rule); }}
    .col.arc .plate {{ border-color: var(--arc-rule); }}
    .plate img {{ display: block; width: 100%; height: auto; }}
    .plate figcaption {{
      font-family: var(--mono); font-size: 0.625rem; letter-spacing: 0.08em;
      padding: 0.55rem 0.7rem; line-height: 1.45; text-transform: uppercase;
    }}
    .col.sim .plate figcaption {{ color: var(--sim-soft); background: rgba(0,0,0,0.03); }}
    .col.arc .plate figcaption {{ color: var(--arc-soft); background: rgba(255,255,255,0.03); }}

    .msg-video, .msg-text-only {{
      margin: 1.8rem 0; border: 1px solid var(--amber);
      background: rgba(245, 158, 11, 0.06);
    }}
    .col.arc .msg-video, .col.arc .msg-text-only {{ background: rgba(245, 158, 11, 0.08); }}
    .msg-video figcaption, .msg-text-only > p:first-child {{
      font-family: var(--mono); font-size: 0.625rem; letter-spacing: 0.14em;
      text-transform: uppercase; color: var(--amber); padding: 0.55rem 0.75rem;
      border-bottom: 1px solid rgba(245, 158, 11, 0.35);
    }}
    .msg-video video {{ display: block; width: 100%; max-height: 360px; background: #000; }}
    .msg-video .msg-text, .msg-text-only p {{
      font-family: var(--mono) !important; font-size: 0.8125rem !important;
      color: inherit; padding: 0.75rem; margin: 0 !important; letter-spacing: 0.02em;
    }}

    .gate-end {{
      margin-top: 2.5rem; padding-top: 1.5rem; border-top: 1px solid currentColor;
      text-align: center;
    }}
    .gate-msg {{
      font-family: var(--mono); font-size: 0.7rem; letter-spacing: 0.1em;
      text-transform: uppercase; margin-bottom: 1rem; opacity: 0.8;
    }}
    .gate-btn {{
      font-family: var(--mono); font-size: 0.7rem; letter-spacing: 0.12em;
      text-transform: uppercase; background: var(--amber); color: #111;
      border: 1px solid var(--amber); padding: 0.85rem 1.2rem; cursor: pointer;
      min-height: 44px;
    }}
    .gate-btn:active {{ transform: scale(0.97); }}
    .gate-btn:hover {{ filter: brightness(1.05); }}

    .lf {{
      flex: 0 0 auto; padding: 0.7rem clamp(1rem, 3vw, 1.8rem);
      border-top: 1px solid var(--rule); background: var(--paper);
      font-family: var(--mono); font-size: 0.625rem; letter-spacing: 0.08em;
      color: var(--soft); text-transform: uppercase;
    }}
    .lf a {{ color: var(--amber); text-decoration: none; border-bottom: 1px solid var(--amber); }}

    @media (max-width: 900px) {{
      body {{ overflow: auto; }}
      .reader {{ overflow: visible; flex: 1 1 auto; }}
      .spread {{ position: relative; inset: auto; display: none; min-height: 70vh; }}
      .spread.active {{ display: block; }}
      .split {{ display: block; height: auto; }}
      .gutter {{ display: none; }}
      .col {{ height: auto; overflow: visible; padding-bottom: 3rem; }}
      .col.is-locked {{ display: none; }}
      .spread[data-world="sim"] .col.arc {{ display: none; }}
      .spread[data-world="sim"] .col.sim {{ display: block; }}
      .spread[data-world="arc"] .col.sim {{ display: none; }}
      .spread[data-world="arc"] .col.arc:not(.is-locked) {{ display: block; }}
      .pivot {{ display: flex; }}
      .plate img {{ max-height: 50vh; object-fit: cover; }}
      .msg-video video {{ max-height: 50vh; }}
    }}

    @media (prefers-reduced-motion: reduce) {{
      .gate-btn:active {{ transform: none; }}
      .col.is-locked .prose {{ filter: none; }}
    }}
  </style>
</head>
<body>
  <header class="lh">
    <div class="lh-row">
      <p class="mark">TWO LAYERS <b>·</b> DOC / PUI</p>
      <p class="thesis">Finish 2026. Then 3026. Then the next.</p>
      <a class="lh-back" href="/universe/">Universe</a>
    </div>
  </header>

  <nav class="ch-sel" aria-label="Chapters">
{ch_buttons()}
    <div class="pivot" role="tablist" aria-label="World">
      <button type="button" data-world="sim" role="tab" aria-selected="true" class="active">2026 · Doc</button>
      <button type="button" data-world="arc" role="tab" aria-selected="false" disabled>3026 · Archive</button>
    </div>
  </nav>

  <main class="reader" id="reader">
{spreads()}
  </main>

  <footer class="lf">
    <p>Artworks: Wikimedia Commons &amp; Art Institute of Chicago · Videos arrive as Doc receives them · <a href="/">Universe →</a></p>
  </footer>

  <script>
  (function () {{
    var KEY = 'two-layers-gate-v2';
    var state = {{ ch: 1, unlockedArc: {{}}, unlockedCh: {{ '1': true }}, doneArc: {{}} }};
    try {{
      var saved = JSON.parse(localStorage.getItem(KEY) || 'null');
      if (saved && saved.unlockedCh) state = saved;
    }} catch (e) {{}}

    var spreads = Array.prototype.slice.call(document.querySelectorAll('.spread'));
    var selBtns = Array.prototype.slice.call(document.querySelectorAll('.ch-sel-btn'));
    var pivot = document.querySelector('.pivot');
    var pivotBtns = Array.prototype.slice.call(pivot.querySelectorAll('button'));

    function isDesktop() {{ return window.matchMedia('(min-width: 901px)').matches; }}

    function save() {{
      try {{ localStorage.setItem(KEY, JSON.stringify(state)); }} catch (e) {{}}
    }}

    function showChapter(n, world) {{
      n = Number(n);
      if (!state.unlockedCh[String(n)]) return;
      state.ch = n;
      spreads.forEach(function (s) {{
        var id = Number(s.getAttribute('data-ch'));
        s.classList.toggle('active', id === n);
      }});
      selBtns.forEach(function (b) {{
        var id = Number(b.getAttribute('data-ch'));
        b.classList.toggle('active', id === n);
        b.classList.toggle('locked', !state.unlockedCh[String(id)]);
        b.classList.toggle('done', !!state.doneArc[String(id)]);
        b.disabled = !state.unlockedCh[String(id)];
      }});
      var spread = document.querySelector('.spread[data-ch="' + n + '"]');
      if (!spread) return;
      var arc = spread.querySelector('.col.arc');
      var arcUnlocked = !!state.unlockedArc[String(n)];
      arc.classList.toggle('is-locked', !arcUnlocked);
      var w = world || (arcUnlocked && spread.getAttribute('data-world') === 'arc' ? 'arc' : 'sim');
      if (!arcUnlocked) w = 'sim';
      spread.setAttribute('data-world', w);
      spread.setAttribute('data-gate', w);
      pivotBtns.forEach(function (b) {{
        var bw = b.getAttribute('data-world');
        var on = bw === w;
        b.classList.toggle('active', on);
        b.setAttribute('aria-selected', on ? 'true' : 'false');
        if (bw === 'arc') b.disabled = !arcUnlocked;
      }});
      // reset scroll on chapter change
      spread.querySelectorAll('.col').forEach(function (c) {{ c.scrollTop = 0; }});
      // reveal gate-end once unlocked appropriately — visibility driven by scroll watchers
      refreshGateEnds(spread);
      save();
    }}

    function nearBottom(el) {{
      return el.scrollTop + el.clientHeight >= el.scrollHeight - 48;
    }}

    function refreshGateEnds(spread) {{
      if (!spread) return;
      var n = spread.getAttribute('data-ch');
      var sim = spread.querySelector('.col.sim');
      var arc = spread.querySelector('.col.arc');
      var simEnd = sim.querySelector('.gate-end');
      var arcEnd = arc.querySelector('.gate-end');
      // On mobile, columns aren't scroll containers — show end after content
      if (!isDesktop()) {{
        simEnd.hidden = false;
        if (!arc.classList.contains('is-locked')) arcEnd.hidden = false;
        return;
      }}
      simEnd.hidden = !nearBottom(sim);
      if (!arc.classList.contains('is-locked')) {{
        arcEnd.hidden = !nearBottom(arc);
      }} else {{
        arcEnd.hidden = true;
      }}
    }}

    spreads.forEach(function (spread) {{
      spread.querySelectorAll('.col').forEach(function (col) {{
        col.addEventListener('scroll', function () {{
          if (col.classList.contains('is-locked')) return;
          refreshGateEnds(spread);
          // Auto-offer unlock when hitting bottom of sim
          if (col.getAttribute('data-side') === 'sim' && nearBottom(col)) {{
            var n = col.getAttribute('data-ch');
            if (!state.unlockedArc[n]) {{
              // keep button visible; user confirms
            }}
          }}
        }}, {{ passive: true }});
      }});
    }});

    document.addEventListener('click', function (e) {{
      var btn = e.target.closest('.gate-btn');
      if (!btn) return;
      var spread = btn.closest('.spread');
      var n = Number(spread.getAttribute('data-ch'));
      var action = btn.getAttribute('data-unlock');
      if (action === 'arc') {{
        state.unlockedArc[String(n)] = true;
        save();
        showChapter(n, 'arc');
        var arc = spread.querySelector('.col.arc');
        arc.classList.remove('is-locked');
        if (isDesktop()) arc.scrollTop = 0;
        else window.scrollTo(0, 0);
      }} else if (action === 'next') {{
        state.doneArc[String(n)] = true;
        var next = n + 1;
        if (next <= spreads.length) {{
          state.unlockedCh[String(next)] = true;
          save();
          showChapter(next, 'sim');
          if (!isDesktop()) window.scrollTo(0, 0);
        }} else {{
          save();
          alert('File open. Session 2849 not initialized.');
        }}
      }}
    }});

    selBtns.forEach(function (b) {{
      b.addEventListener('click', function () {{
        showChapter(b.getAttribute('data-ch'));
      }});
    }});

    pivotBtns.forEach(function (b) {{
      b.addEventListener('click', function () {{
        if (b.disabled) return;
        var spread = document.querySelector('.spread.active');
        if (!spread) return;
        showChapter(spread.getAttribute('data-ch'), b.getAttribute('data-world'));
        if (!isDesktop()) window.scrollTo(0, 0);
      }});
    }});

    window.addEventListener('resize', function () {{
      var spread = document.querySelector('.spread.active');
      refreshGateEnds(spread);
    }});

    // boot
    showChapter(state.ch || 1);
    // mobile: gate-ends always available at bottom of content
    if (!isDesktop()) {{
      spreads.forEach(refreshGateEnds);
    }}
  }})();
  </script>
</body>
</html>
'''

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(HTML, encoding="utf-8")
print(f"Wrote {OUT} ({OUT.stat().st_size:,} bytes)")
print(f"Chapters: {len(CHAPTERS)}")
for c in CHAPTERS:
    print(f"  {c['id']:02d} {c['short']}")
