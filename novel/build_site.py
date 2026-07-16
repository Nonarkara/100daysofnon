#!/usr/bin/env python3
"""
build_site.py — generate the web reader for THE CONVENIENCE.
Reads:  novel/chapters/*.md, novel/marginalia.json
Writes: site/convenience/index.html, site/convenience/read/{1..19}/index.html,
        site/assets/css/convenience.css
Run: python3 novel/build_site.py
"""
import json, re, html as html_module
from pathlib import Path

ROOT = Path(__file__).parent
CHAPTERS = ROOT / "chapters"
SITE = ROOT.parent / "site"
OUT = SITE / "convenience"
CSS_OUT = SITE / "assets" / "css" / "convenience.css"

MARGINALIA = json.loads((ROOT / "marginalia.json").read_text())
BY_FILE = {m["chapter_file"]: m for m in MARGINALIA}

PARTS = {
    "01": ("PART ONE", "The Message"),
    "06": ("PART TWO", "The Night Shift"),
    "15": ("PART THREE", "The Wiggle Room"),
}

UNIVERSE_LINKS = [
    ("/layers/", "Two Layers"),
    ("/convenience/", "The Convenience"),
    ("/book/", "Biography"),
    ("/workshop/", "Workshop"),
    ("/portrait/", "Self-Portrait"),
    ("/atlas/", "Atlas"),
    ("/questions/", "Questions"),
    ("/universe/", "The Map"),
]

def universe_nav(current):
    parts = ['<nav class="universe-nav" aria-label="The universe">',
             '<span class="un-label">100 Days of Non — the universe</span>']
    for i, (href, label) in enumerate(UNIVERSE_LINKS):
        cur = ' aria-current="page"' if href == current else ""
        parts.append(f'<a href="{href}"{cur}>{label}</a>')
        if i < len(UNIVERSE_LINKS) - 1:
            parts.append('<span class="sep">·</span>')
    parts.append("</nav>")
    return "\n      ".join(parts)

def esc(s):
    return html_module.escape(s, quote=False)

def heading_parts(fname, first_line):
    h = first_line.lstrip("#").strip()
    m = re.match(r'(CH\d+|INTERLUDE [A-E])\s*[—-]\s*(.*)', h)
    if m:
        label, title = m.group(1), m.group(2).strip().strip('"')
    else:
        label, title = "", h.strip('"')
    is_int = "interlude" in fname
    return label, title, is_int

def md_to_html_with_notes(md: str, fname: str) -> str:
    """Paragraphs + scene breaks + inline marginalia markers."""
    lines = md.strip().splitlines()
    while lines and (lines[0].startswith("#") or not lines[0].strip()):
        lines.pop(0)
    text = "\n".join(lines)
    blocks = re.split(r"\n\s*\n", text)

    note = BY_FILE.get(fname)
    note_placed = False
    out = []
    note_id = "note-" + fname.replace(".md", "")

    for b in blocks:
        b = b.strip()
        if not b:
            continue
        if re.fullmatch(r"[\*\-—·⁂]{1,5}", b):
            out.append('<hr class="scene-break">')
            continue
        b = esc(b)
        b = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", b, flags=re.S)
        b = re.sub(r"\*(.+?)\*", r"<em>\1</em>", b, flags=re.S)
        b = b.replace("\n", " ")

        # insert the marginalia marker+sidenote right after its anchor phrase,
        # once per chapter, using the checkbox-hack so mobile and desktop
        # share one DOM (desktop floats it into the margin; mobile expands
        # it inline on tap — no JS required either way).
        if note and not note_placed and note["anchor"] in b:
            anchor_esc = esc(note["anchor"])
            src_link = f'<a href="{note["url"]}" target="_blank" rel="noopener">{esc(note["url_label"])}</a>'
            sidenote = (
                f'<label for="{note_id}" class="mn-toggle-label">{note["mark"]}</label>'
                f'<input type="checkbox" id="{note_id}" class="mn-toggle">'
                f'<span class="sidenote">'
                f'<span class="mn-mark">{note["mark"]}</span>'
                f'<span class="mn-title">{esc(note["title"])}</span>'
                f'<span class="mn-body">{esc(note["body"])}</span>'
                f'<span class="mn-source">{esc(note["source"])} — {src_link}</span>'
                f'</span>'
            )
            b = b.replace(anchor_esc, anchor_esc + sidenote, 1)
            note_placed = True

        out.append(f"<p>{b}</p>")
    return "\n".join(out)

def build_page(idx, total, fname, prev_href, next_href, part_banner):
    raw = (CHAPTERS / fname).read_text(encoding="utf-8")
    first = raw.strip().splitlines()[0] if raw.strip() else ""
    label, title, is_int = heading_parts(fname, first)
    disp_label = label.replace("CH", "Chapter ") if label.startswith("CH") else label.title()
    body = md_to_html_with_notes(raw, fname)
    kind_class = "interlude" if is_int else "his"
    eyebrow = "THE CONVENIENCE" + (f" · {disp_label.upper()}" if disp_label else "")

    part_html = ""
    if part_banner:
        pnum, pname = part_banner
        part_html = f'<div class="part-banner"><span class="pnum">{pnum}</span><span class="pname">{pname}</span></div>'

    nav_bits = []
    if prev_href:
        nav_bits.append(f'<a class="ch-nav-prev" href="{prev_href}">← Previous</a>')
    else:
        nav_bits.append('<span class="ch-nav-spacer"></span>')
    nav_bits.append(f'<a class="ch-nav-toc" href="/convenience/">Contents</a>')
    if next_href:
        nav_bits.append(f'<a class="ch-nav-next" href="{next_href}">Next →</a>')
    else:
        nav_bits.append('<span class="ch-nav-spacer"></span>')
    chapter_nav = '<nav class="ch-nav" aria-label="Chapter navigation">' + "".join(nav_bits) + '</nav>'

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)} — The Convenience</title>
<meta name="description" content="{esc(title)}, from THE CONVENIENCE — a Bangkok novel by Non Arkara.">
<meta property="og:type" content="book">
<meta property="og:title" content="{esc(title)} — The Convenience">
<meta property="og:site_name" content="100 Days of Non">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,500;0,7..72,600;1,7..72,400&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/surface.css">
<link rel="stylesheet" href="/assets/css/convenience.css">
</head>
<body class="reader {kind_class}">
<main class="ch-main">
{chapter_nav}
{part_html}
<header class="ch-head">
<p class="eyebrow">{eyebrow}</p>
<h1>{esc(title)}</h1>
<p class="ch-progress">{idx} of {total}</p>
</header>
<article class="prose">
{body}
</article>
{chapter_nav}
{universe_nav("/convenience/")}
</main>
</body>
</html>
"""

def build_index(chapter_meta):
    rows = []
    for i, (fname, label, title, is_int, part) in enumerate(chapter_meta, start=1):
        disp = label.replace("CH", "Chapter ") if label.startswith("CH") else label.title()
        cls = "toc-int" if is_int else "toc-his"
        part_html = f'<li class="toc-part">{part[0]} — {part[1]}</li>' if part else ""
        rows.append(part_html)
        rows.append(f'<li class="{cls}"><a href="/convenience/read/{i}/"><span class="toc-num">{disp}</span><span class="toc-title">{esc(title)}</span></a></li>')
    toc = "\n        ".join(r for r in rows if r)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>The Convenience — a Bangkok novel</title>
<meta name="description" content="A Bangkok novel about a man, a message from a dead woman's account, and the night shift that trained the machines to feel. Read free, with sidenotes on Descartes, Zhuangzi, the Buddha, AlphaGo, and the simulation argument.">
<meta property="og:type" content="book">
<meta property="og:url" content="https://100.nonarkara.org/convenience/">
<meta property="og:title" content="The Convenience — a Bangkok novel">
<meta property="og:description" content="A message arrives from a dead woman's account, timestamped tomorrow. Nineteen chapters, read free.">
<meta property="og:site_name" content="100 Days of Non">
<meta name="twitter:card" content="summary">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,500;0,7..72,600;1,7..72,400&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/surface.css">
<link rel="stylesheet" href="/assets/css/convenience.css">
</head>
<body class="cover-body">
<main>
<header class="cover">
<p class="eyebrow">A NOVEL · <b>BANGKOK, 2026</b></p>
<h1>The Convenience</h1>
<p class="sub">Twenty-two months after Pui died, her LINE account sends a photograph of him asleep — timestamped tomorrow.</p>
<p class="meta">19 chapters · ~65,000 words · free to read</p>
<p class="also"><a href="/convenience/read/1/">Start reading →</a></p>
</header>

<section class="epigraphs">
<blockquote><p>I will suppose that some malicious demon of the utmost power and cunning has employed all his energies in order to deceive me.</p><cite>— René Descartes, <em>Meditations</em>, 1641</cite></blockquote>
<blockquote class="th"><p>เลขออกแล้วตั้งแต่เมื่อวาน เราแค่ยังไม่รู้</p><p class="tr"><em>The numbers already came out yesterday. We just don't know them yet.</em></p><cite>— a lottery vendor, Bang Rak</cite></blockquote>
</section>

<section class="how-to-read">
<p class="eyebrow small">HOW TO READ THIS</p>
<p>The narrator's chapters and Pui's interludes are typeset differently on purpose — warm paper for his first person, colder graphite for hers, the same split this site uses for <a href="/layers/">Two Layers</a>. Eight chapters carry a small <span class="mn-mark-inline">†</span> in the margin — real sources (Descartes, Zhuangzi, the Buddha, AlphaGo's Move 37, Bostrom's simulation argument) that the story leans on. Tap or click one to open it. Everything quoted there is public domain, open-licensed, or a plain fact with a link to read the whole thing free.</p>
</section>

<nav class="toc" aria-label="Contents">
<h2>Contents</h2>
<ol class="toc-list">
{toc}
</ol>
</nav>

{universe_nav("/convenience/")}
</main>
</body>
</html>
"""

def main():
    files = sorted(CHAPTERS.glob("*.md"))
    total = len(files)
    chapter_meta = []
    for f in files:
        raw = f.read_text(encoding="utf-8")
        first = raw.strip().splitlines()[0] if raw.strip() else ""
        label, title, is_int = heading_parts(f.name, first)
        part = PARTS.get(f.name[:2])
        chapter_meta.append((f.name, label, title, is_int, part))

    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "index.html").write_text(build_index(chapter_meta), encoding="utf-8")

    for i, (fname, label, title, is_int, part) in enumerate(chapter_meta, start=1):
        prev_href = f"/convenience/read/{i-1}/" if i > 1 else None
        next_href = f"/convenience/read/{i+1}/" if i < total else None
        page = build_page(i, total, fname, prev_href, next_href, part)
        d = OUT / "read" / str(i)
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(page, encoding="utf-8")

    print(f"Built {total} chapter pages + index → {OUT}")

if __name__ == "__main__":
    main()
