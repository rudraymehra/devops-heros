"""Offline tests for honest command recording; no Docker, cloud or screen access."""
import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location("native_evidence", Path(__file__).with_name("capture-native-evidence.py"))
capture = importlib.util.module_from_spec(spec)
spec.loader.exec_module(capture)


class EvidenceTests(unittest.TestCase):
    def test_real_success(self):
        code, output = capture.execute([sys.executable, "-c", "print('actual result')"], Path.cwd(), 5)
        self.assertEqual((code, output), (0, "actual result\n"))

    def test_nonzero_is_preserved(self):
        code, output = capture.execute([sys.executable, "-c", "print('failed check'); raise SystemExit(7)"], Path.cwd(), 5)
        self.assertEqual(code, 7)
        self.assertIn("failed check", output)

    def test_missing_executable(self):
        self.assertEqual(capture.execute(["/nonexistent/campusfix-test-executable"], Path.cwd(), 1)[0], 127)

    def test_timeout_is_not_success(self):
        code, output = capture.execute([sys.executable, "-c", "import time; time.sleep(5)"], Path.cwd(), 0.05)
        self.assertEqual(code, 124)
        self.assertIn("No success claimed", output)

    def test_account_number_redacted(self):
        code, output = capture.execute([sys.executable, "-c", "print('123456789012')"], Path.cwd(), 5)
        self.assertEqual(code, 0)
        self.assertEqual(output, "[AWS_ACCOUNT_ID]\n")

    def test_logs_do_not_claim_screenshots(self):
        with tempfile.TemporaryDirectory() as root:
            run = capture.EvidenceRun(Path(root) / "run")
            self.assertTrue(run.check("test", "Self-test", [sys.executable, "-c", "print('real')"]))
            index = (run.output / "README.md").read_text()
            self.assertIn("Rudray Mehra", index)
            self.assertIn("NOT CAPTURED", index)
            self.assertEqual(run.records[0]["log_sha256"], capture.file_hash(run.output / "test.txt"))
            self.assertIsNone(run.records[0]["screenshot"])

    def test_existing_run_is_never_overwritten(self):
        with tempfile.TemporaryDirectory() as root:
            with self.assertRaises(FileExistsError):
                capture.EvidenceRun(Path(root))

    def test_cancelled_capture_is_not_success(self):
        with tempfile.TemporaryDirectory() as root:
            with patch("builtins.input", return_value=""), patch.object(capture.subprocess, "run", return_value=subprocess.CompletedProcess([], 0)):
                self.assertIsNone(capture.capture_window(Path(root) / "cancelled.png", "Test"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
