#!/usr/bin/env python3
"""
build_book.py — assemble novel/chapters/*.md into THE-CONVENIENCE.pdf
Pipeline: markdown chapters -> single HTML (book CSS, paged media) -> Chrome headless print-to-pdf.
Run: python3 novel/build_book.py
"""
import re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).parent
CHAPTERS = ROOT / "chapters"
OUT_HTML = ROOT / "THE-CONVENIENCE.html"
OUT_PDF = ROOT / "THE-CONVENIENCE.pdf"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# Part pages inserted before these file prefixes
PARTS = {
    "01": ("PART ONE", "THE MESSAGE"),
    "06": ("PART TWO", "THE NIGHT SHIFT"),
    "15": ("PART THREE", "THE WIGGLE ROOM"),
}

CSS = """
@page {
  size: 5.5in 8.5in;
  margin: 0.85in 0.75in 0.9in 0.75in;
  @bottom-center { content: counter(page); font: 8.5pt 'Literata', Georgia, serif; color: #333; }
  @top-center { content: "THE CONVENIENCE"; font: 7.5pt 'Literata', Georgia, serif; letter-spacing: 3px; color: #555; }
}
@page front { @top-center { content: none; } @bottom-center { content: none; } }
@page part  { @top-center { content: none; } @bottom-center { content: none; } }
@page chapterstart { @top-center { content: none; } }

html { -webkit-print-color-adjust: exact; }
body {
  font-family: 'Literata', Georgia, 'IBM Plex Sans Thai', 'Noto Sans Thai', serif;
  font-size: 10.6pt; line-height: 1.62; color: #111;
  margin: 0; text-rendering: optimizeLegibility;
}
p { margin: 0; text-indent: 1.4em; orphans: 2; widows: 2; }
p.noindent, h2 + p, .scene-break + p { text-indent: 0; }
.scene-break { text-align: center; border: none; margin: 1.1em 0; }
.scene-break::after { content: "·"; font-size: 12pt; color: #444; }

/* front matter */
.front { page: front; page-break-after: always; text-align: center; }
.halftitle { padding-top: 3.2in; font-size: 13pt; letter-spacing: 6px; }
.titlepage .title { padding-top: 2.6in; font-size: 26pt; letter-spacing: 8px; font-weight: 400; }
.titlepage .subtitle { margin-top: 0.35in; font-size: 10.5pt; font-style: italic; letter-spacing: 1px; }
.titlepage .author { margin-top: 1.9in; font-size: 12pt; letter-spacing: 4px; }
.copyright { page: front; page-break-after: always; font-size: 8.5pt; color: #444; padding-top: 5.6in; text-align: left; line-height: 1.7; }
.epigraph { page: front; page-break-after: always; padding-top: 2.8in; font-size: 10.5pt; font-style: italic; text-align: left; max-width: 3.4in; margin: 0 auto; line-height: 1.8; }
.epigraph .attr { font-style: normal; font-size: 9pt; margin-top: 0.6em; text-indent: 0; text-align: right; }
.epigraph p { text-indent: 0; margin-bottom: 1.4em; }

/* part pages */
.part { page: part; page-break-before: always; page-break-after: always; text-align: center; }
.part .pnum { padding-top: 3.1in; font-size: 10.5pt; letter-spacing: 6px; color: #333; }
.part .pname { margin-top: 0.5in; font-size: 17pt; letter-spacing: 5px; }

/* chapters */
.chapter { page-break-before: always; page: chapterstart; }
.chapter h2 {
  padding-top: 1.5in; margin: 0 0 0.75in 0; font-weight: 400;
  font-size: 13.5pt; letter-spacing: 1.5px; text-align: center; line-height: 1.5;
}
.chapter h2 .chnum { display: block; font-size: 9.5pt; letter-spacing: 5px; color: #555; margin-bottom: 0.9em; }
.interlude h2 { font-style: italic; letter-spacing: 1px; }
.interlude h2 .chnum { font-style: normal; }
"""

def md_to_html(md: str) -> str:
    """Minimal markdown: strip the agent's ## heading (we rebuild it), paragraphs, scene breaks, em/it."""
    lines = md.strip().splitlines()
    # drop leading heading line(s)
    while lines and (lines[0].startswith("#") or not lines[0].strip()):
        lines.pop(0)
    text = "\n".join(lines)
    blocks = re.split(r"\n\s*\n", text)
    out = []
    for b in blocks:
        b = b.strip()
        if not b:
            continue
        if re.fullmatch(r"[\*\-—·⁂]{1,5}", b):
            out.append('<hr class="scene-break">')
            continue
        b = b.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        b = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", b, flags=re.S)
        b = re.sub(r"\*(.+?)\*", r"<em>\1</em>", b, flags=re.S)
        b = b.replace("\n", " ")
        out.append(f"<p>{b}</p>")
    return "\n".join(out)

def heading_parts(fname: str, first_line: str):
    """Return (label, title, is_interlude) from the chapter file's own heading."""
    h = first_line.lstrip("#").strip()
    m = re.match(r"(CH\d+|INTERLUDE [A-E])\s*[—-]\s*(.*)", h)
    if m:
        label, title = m.group(1), m.group(2).strip().strip('"')
    else:
        label, title = "", h.strip('"')
    is_int = "interlude" in fname
    if label.startswith("CH"):
        label = "CHAPTER " + label[2:]
    return label, title, is_int

def main():
    files = sorted(CHAPTERS.glob("*.md"))
    if len(files) < 19:
        print(f"WARNING: only {len(files)}/19 chapter files present")
    body = []

    # front matter
    body.append('<div class="front halftitle">THE CONVENIENCE</div>')
    body.append("""<div class="front titlepage">
      <div class="title">THE<br>CONVENIENCE</div>
      <div class="subtitle">a Bangkok novel</div>
      <div class="author">NON ARKARA</div></div>""")
    body.append("""<div class="copyright">
      <p class="noindent">This is a work of fiction set in a parallel timeline. Names, characters,
      businesses, and events are products of imagination or are used fictitiously.
      Any resemblance to actual persons, living, dead, or continued, is the point.</p>
      <p class="noindent">First assembly, Bangkok, 2026.<br>
      Set in Literata. Thai set in IBM Plex Sans Thai.<br>
      Drafted with the assistance of machines trained, in part, on human moments
      labeled by night-shift workers whose names do not appear in any credits.</p></div>""")
    body.append("""<div class="front epigraph">
      <p>I will suppose that some malicious demon of the utmost power and cunning
      has employed all his energies in order to deceive me.</p>
      <p class="attr">— René Descartes, <em>Meditations</em></p>
      <p style="margin-top:2.2em">เลขออกแล้วตั้งแต่เมื่อวาน เราแค่ยังไม่รู้<br>
      <em>The numbers already came out yesterday. We just don't know them yet.</em></p>
      <p class="attr">— a lottery vendor, Bang Rak</p></div>""")

    ch_counter = 0
    for f in files:
        prefix = f.name[:2]
        if prefix in PARTS:
            pnum, pname = PARTS[prefix]
            body.append(f'<div class="part"><div class="pnum">{pnum}</div><div class="pname">{pname}</div></div>')
        raw = f.read_text(encoding="utf-8")
        first = raw.strip().splitlines()[0] if raw.strip() else ""
        label, title, is_int = heading_parts(f.name, first)
        if not is_int:
            ch_counter += 1
            label = f"CHAPTER {ch_counter}" if not label else label
        cls = "chapter interlude" if is_int else "chapter"
        body.append(f'<div class="{cls}"><h2><span class="chnum">{label}</span>{title}</h2>')
        body.append(md_to_html(raw))
        body.append("</div>")

    html = f"""<!doctype html><html><head><meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,600;1,7..72,400&family=IBM+Plex+Sans+Thai:wght@400;600&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>
{chr(10).join(body)}
</body></html>"""
    OUT_HTML.write_text(html, encoding="utf-8")
    print(f"HTML: {OUT_HTML} ({len(html)//1024}KB)")

    r = subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-pdf-header-footer",
                        "--virtual-time-budget=20000",
                        f"--print-to-pdf={OUT_PDF}", str(OUT_HTML)],
                       capture_output=True, text=True, timeout=300)
    if OUT_PDF.exists():
        print(f"PDF: {OUT_PDF} ({OUT_PDF.stat().st_size//1024}KB)")
    else:
        print("PDF FAILED:", r.stderr[-400:])
        sys.exit(1)

if __name__ == "__main__":
    main()
