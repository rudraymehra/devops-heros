"""Offline provenance/link checks; no image generation, lab execution or network."""
import importlib.util
import json
from pathlib import Path
import re
import unittest
from urllib.parse import unquote, urlsplit

spec = importlib.util.spec_from_file_location("renderer", Path(__file__).with_name("render-coursework-evidence.py"))
renderer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(renderer)
ROOT = renderer.ROOT
coursework = renderer.coursework


class RenderedEvidenceTests(unittest.TestCase):
    def test_line_numbers_and_omissions_are_explicit(self):
        text = renderer.numbered([f"actual line {i}" for i in range(100)])
        self.assertIn("00001  actual line 0", text)
        self.assertIn("00100  actual line 99", text)
        self.assertIn("source lines omitted", text)
        self.assertNotIn("00050", text)

    def test_only_actual_command_boundaries(self):
        self.assertEqual(renderer.command_blocks(["heading", "$ first", "output", "$ second", "done"]), [(1, 3), (3, 5)])

    def test_all_rendered_artifacts_match_their_original_sources(self):
        count = 0
        for item in coursework.CATALOG:
            folder = (ROOT / item["readme"]).parent / "screenshots/rendered-log-views"
            entries = json.loads((folder / "manifest.json").read_text())
            self.assertTrue(entries, item["key"])
            self.assertEqual({e["image"] for e in entries}, {p.name for p in folder.glob("*.png")})
            for entry in entries:
                with self.subTest(image=str(folder / entry["image"])):
                    image = folder / entry["image"]
                    source = ROOT / entry["source"]
                    self.assertTrue(source.resolve().is_relative_to(ROOT.resolve()))
                    self.assertTrue(image.read_bytes().startswith(coursework.native.PNG_SIGNATURE))
                    self.assertEqual(coursework.native.file_hash(image), entry["image_sha256"])
                    self.assertEqual(coursework.native.file_hash(source), entry["source_sha256"])
                    self.assertIs(entry["native_screenshot"], False)
                    document = (folder / entry["text"]).read_text()
                    self.assertIn("NOT a native", document.splitlines()[0])
                    self.assertIn("Rudray Mehra | 24 BCS 10425 | Batch B", document)
                    self.assertIn(entry["source_sha256"], document)
                    if entry["kind"] == "local-recorded-command":
                        run = json.loads((source.parent / "manifest.json").read_text())
                        original = next(r for r in run["records"] if r.get("log") == source.name)
                        self.assertIn("Actual recorded result: " + original["status"], document)
                        self.assertEqual(original["log_sha256"], entry["source_sha256"])
            count += len(entries)
        self.assertGreaterEqual(count, 85)

    def test_evidence_navigation_has_no_broken_local_links(self):
        pages = [ROOT / "COURSEWORK-EVIDENCE.md", *list((ROOT / "evidence/coursework").glob("*.md"))]
        for item in coursework.CATALOG:
            pages.extend(((ROOT / item["readme"]).parent / "screenshots").rglob("*.md"))
        for page in pages:
            for target in re.findall(r"!?\[[^\]\n]*\]\(([^)\n]+)\)", page.read_text()):
                parsed = urlsplit(target)
                if parsed.scheme or not parsed.path:
                    continue
                with self.subTest(page=page, target=target):
                    self.assertTrue((page.parent / unquote(parsed.path)).exists())

    def test_rejected_images_are_not_linked_from_reviewed_indexes(self):
        reviews = json.loads((ROOT / "evidence/coursework/native-review.json").read_text())["images"]
        for name, review in reviews.items():
            if review["decision"] != "rejected":
                continue
            image = ROOT / name
            for index in [image.parent / "README.md", image.parent.parent / "README.md"]:
                self.assertNotIn("(" + image.name + ")", index.read_text())
                self.assertNotIn("/" + image.name + ")", index.read_text())


if __name__ == "__main__":
    unittest.main(verbosity=2)
