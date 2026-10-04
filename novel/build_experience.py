#!/usr/bin/env python3
"""Publish the complete Two Layers text for the interactive adaptation."""
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "novel" / "layers-chapters"
OUT = ROOT / "site" / "experience" / "story.json"


def inline(text):
    text = html.escape(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    return re.sub(r"\*(.+?)\*", r"<em>\1</em>", text)


def render(body):
    blocks, paragraph, figure = [], [], []

    def flush():
        if paragraph:
            quote = paragraph[0].startswith(">")
            text = " ".join(re.sub(r"^>\s?", "", line) for line in paragraph)
            tag = "blockquote" if quote else "p"
            blocks.append(f"<{tag}>{inline(text)}</{tag}>")
            paragraph.clear()

    for line in body.splitlines():
        if figure or line.strip().startswith("<figure"):
            flush()
            figure.append(line)
            if "</figure>" in line:
                markup = "\n".join(figure)
                # Match the existing reader's verified-art substitutions.
                for missing, verified in {
                    "magritte-false-mirror.jpg": "vermeer-balance.jpg",
                    "de-chirico-street.jpg": "friedrich-wanderer.jpg",
                    "delvaux-hands.jpg": "caravaggio-thomas.jpg",
                    "redon-eye.jpg": "goya-sleep-of-reason.jpg",
                    "klimt-kiss.jpg": "schiele-embrace.jpg",
                    "munch-scream.jpg": "goya-sleep-of-reason.jpg",
                }.items():
                    markup = markup.replace(missing, verified)
                blocks.append(markup)
                figure.clear()
        elif not line.strip() or line.startswith("#") or re.match(r"^-{3,}\s*$", line):
            flush()
        else:
            if paragraph and line.startswith(">") != paragraph[0].startswith(">"):
                flush()
            paragraph.append(line.strip())
    flush()
    if figure:
        raise ValueError("Unclosed figure in manuscript")
    return "\n".join(blocks)


def build():
    chapters = []
    for path in sorted(SOURCE.glob("[0-9][0-9]-*.md")):
        raw = path.read_text(encoding="utf-8")
        parts = re.split(r"^##\s+(2026 · Doc|3026 · Archive)\s*$", raw, flags=re.M)
        if len(parts) != 5:
            raise ValueError(f"Expected both timelines: {path.name}")
        layers = {parts[i].split(" · ")[0]: render(parts[i + 1]) for i in (1, 3)}
        chapters.append({
            "id": int(path.name[:2]),
            "title": re.sub(r"^# CH\d+ [—–-] ", "", raw.splitlines()[0]),
            "source": str(path.relative_to(ROOT)),
            "simulation": layers["2026"],
            "archive": layers["3026"],
        })
    if [c["id"] for c in chapters] != list(range(1, 11)):
        raise ValueError("Expected exactly ten chapters in sequence")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps({"version": 1, "chapters": chapters}, ensure_ascii=False), encoding="utf-8")
    print(f"Built {OUT.relative_to(ROOT)}: {len(chapters)} complete chapters, both timelines")


if __name__ == "__main__":
    build()
