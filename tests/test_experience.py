"""Preserve the manuscript and shipped assets across experience rebuilds."""
import importlib.util
import json
import re
import unittest
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("experience_build", ROOT / "novel/build_experience.py")
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)


class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text, self.sources = [], []

    def handle_data(self, data):
        self.text.append(data)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "src" in attrs:
            self.sources.append(attrs["src"])


class ManuscriptTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(build.OUT.read_text(encoding="utf-8"))

    def test_all_ten_complete_timelines_are_published(self):
        self.assertEqual([c["id"] for c in self.data["chapters"]], list(range(1, 11)))
        for chapter in self.data["chapters"]:
            raw = (ROOT / chapter["source"]).read_text(encoding="utf-8")
            parts = re.split(r"^##\s+(2026 · Doc|3026 · Archive)\s*$", raw, flags=re.M)
            for i, layer in [(2, "simulation"), (4, "archive")]:
                self.assertEqual(chapter[layer], build.render(parts[i]))
                self.assertGreater(len(chapter[layer]), 2000)

    def test_every_source_paragraph_survives(self):
        for chapter in self.data["chapters"]:
            raw = (ROOT / chapter["source"]).read_text(encoding="utf-8")
            raw = re.sub(r"<figure\b.*?</figure>", "", raw, flags=re.S)
            paragraphs = re.split(r"\n\s*\n", raw)
            parsed = Text()
            parsed.feed(chapter["simulation"] + chapter["archive"])
            text = " ".join("".join(parsed.text).split())
            for paragraph in paragraphs:
                if not paragraph.strip() or paragraph.lstrip().startswith(("#", "---")):
                    continue
                expected = re.sub(r"(?m)^>\s?", "", paragraph).replace("*", "")
                expected = " ".join(expected.split())
                self.assertIn(expected, text, f"Missing prose in {chapter['source']}")

    def test_source_art_and_videos_exist(self):
        for chapter in self.data["chapters"]:
            parsed = Text()
            parsed.feed(chapter["simulation"] + chapter["archive"])
            for src in parsed.sources:
                self.assertTrue((ROOT / "site" / src.lstrip("/")).is_file(), src)

    def test_renderer_preserves_quotes_and_escapes_prose(self):
        parsed = Text()
        parsed.feed(build.render('> I kept it.\n\nA <script> is not a memory.\n\n*Still here.*'))
        self.assertEqual(parsed.text, ['I kept it.', '\n', 'A <script> is not a memory.', '\n', 'Still here.'])

    def test_incomplete_figures_fail_instead_of_dropping_content(self):
        with self.assertRaises(ValueError):
            build.render('<figure>\nA missing closing tag')


if __name__ == "__main__":
    unittest.main()
