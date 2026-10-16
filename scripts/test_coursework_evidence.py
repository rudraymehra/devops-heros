"""Offline audit tests; no screen, network, Docker or cloud calls."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
import zipfile
from unittest.mock import patch

spec = importlib.util.spec_from_file_location("coursework", Path(__file__).with_name("coursework-evidence.py"))
coursework = importlib.util.module_from_spec(spec)
spec.loader.exec_module(coursework)


class CourseworkTests(unittest.TestCase):
    def test_all_sessions_mapped_once(self):
        self.assertEqual([i["key"] for i in coursework.CATALOG], ["01-02"] + [f"{n:02d}" for n in range(3, 21)])
        self.assertEqual(len({i["readme"] for i in coursework.CATALOG}), 19)

    def test_entrypoints_and_core_files_exist(self):
        for item in coursework.CATALOG:
            for name in [item["readme"], *item["required"]]:
                self.assertTrue((coursework.ROOT / name).is_file(), name)

    def test_relative_links_from_nested_audit(self):
        self.assertEqual(coursework.link_from(coursework.ROOT / "evidence/coursework", "session2-linux/README.md"), "../../session2-linux/README.md")
        self.assertEqual(coursework.link_from(coursework.ROOT, "path with space/file.md"), "path%20with%20space/file.md")

    def test_reference_is_not_extracted(self):
        with tempfile.TemporaryDirectory() as scratch:
            archive = Path(scratch) / "reference.zip"
            with zipfile.ZipFile(archive, "w") as zipped:
                zipped.writestr("repo/session-03-shell-scripting/screenshots/test.png", b"test fixture, not screenshot evidence")
                zipped.writestr("repo/session-03-shell-scripting/unsafe.sh", "exit 99")
                zipped.writestr("../outside.txt", "not extracted")
            result = coursework.manifest_for_zip(archive)
            self.assertEqual(len(result["groups"]["03"]), 1)
            self.assertEqual(len(result["sha256"]), 64)
            self.assertEqual(sorted(p.name for p in Path(scratch).iterdir()), ["reference.zip"])

    def test_actual_reference_inventory(self):
        path = coursework.ROOT / "evidence/coursework/reference-manifest.json"
        result = json.loads(path.read_text())
        self.assertEqual(sum(map(len, result["groups"].values())), 179)
        self.assertEqual(result["sha256"], "bba4a044dbe172e2371ea91d45c3cc2bddca5f02f95e1512d79760fb9d17698a")

    def test_native_metadata_requires_file(self):
        with tempfile.TemporaryDirectory() as scratch:
            self.assertFalse(coursework.valid_native_file(Path(scratch), {"file": "missing.png", "sha256": "0" * 64}))
            self.assertFalse(coursework.valid_native_file(Path(scratch), {"file": "../outside.png", "sha256": "0" * 64}))

    def test_hash_mismatch_is_not_verified(self):
        with tempfile.TemporaryDirectory() as scratch:
            image = Path(scratch) / "fixture.png"
            image.write_bytes(coursework.native.PNG_SIGNATURE + b"unit test fixture, not submission evidence")
            self.assertFalse(coursework.valid_native_file(Path(scratch), {"file": image.name, "sha256": "0" * 64}))

    def test_unknown_session_rejected_before_actions(self):
        from argparse import Namespace
        with self.assertRaises(SystemExit):
            coursework.run_sessions(Namespace(screenshots=False, sessions="99"))

    def fixture_shot(self, directory):
        image = directory / "fixture.png"
        image.write_bytes(coursework.native.PNG_SIGNATURE + b"unit test only")
        return {"file": image.name, "sha256": coursework.native.file_hash(image)}

    def test_verified_bytes_still_need_visual_review(self):
        with tempfile.TemporaryDirectory() as scratch, patch.object(coursework, "ROOT", Path(scratch)):
            folder = Path(scratch)
            shot = self.fixture_shot(folder)
            self.assertEqual(coursework.screenshot_review(folder, shot, {})[0], "pending")
            reviews = {"fixture.png": {"sha256": shot["sha256"], "decision": "accepted", "note": "test only"}}
            self.assertEqual(coursework.screenshot_review(folder, shot, reviews)[0], "accepted")
            reviews["fixture.png"]["sha256"] = "0" * 64
            self.assertEqual(coursework.screenshot_review(folder, shot, reviews)[0], "pending")

    def test_accepted_missing_image_is_invalid(self):
        with tempfile.TemporaryDirectory() as scratch, patch.object(coursework, "ROOT", Path(scratch)):
            shot = {"file": "absent.png", "sha256": "0" * 64}
            reviews = {"absent.png": {"sha256": "0" * 64, "decision": "accepted", "note": "test only"}}
            self.assertEqual(coursework.screenshot_review(Path(scratch), shot, reviews)[0], "invalid")

    def test_rejected_image_can_be_excluded_without_broken_links(self):
        with tempfile.TemporaryDirectory() as scratch, patch.object(coursework, "ROOT", Path(scratch)):
            shot = {"file": "absent.png", "sha256": "0" * 64}
            reviews = {"absent.png": {"sha256": "0" * 64, "decision": "rejected", "note": "wrong window"}}
            self.assertEqual(coursework.screenshot_review(Path(scratch), shot, reviews)[0], "rejected")
            run = {"records": [{"title": "test", "status": "PASS", "log": "result.txt", "screenshot": shot}]}
            index = coursework.reviewed_run_index(Path(scratch), run, reviews)
            self.assertIn("wrong window", index)
            self.assertIn("result.txt", index)
            self.assertNotIn("absent.png", index)

    def test_changed_rejected_hash_needs_review_again(self):
        with tempfile.TemporaryDirectory() as scratch, patch.object(coursework, "ROOT", Path(scratch)):
            folder = Path(scratch)
            shot = self.fixture_shot(folder)
            reviews = {"fixture.png": {"sha256": "0" * 64, "decision": "rejected", "note": "old review"}}
            self.assertEqual(coursework.screenshot_review(folder, shot, reviews)[0], "pending")


if __name__ == "__main__":
    unittest.main(verbosity=2)
