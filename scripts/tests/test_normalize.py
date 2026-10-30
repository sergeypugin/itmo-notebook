"""Compatibility tests for the legacy entry point."""
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from scripts import main as canonical_main
from scripts import normalize


class NormalizeCompatibilityTest(unittest.TestCase):
    def test_delegates_arguments_to_canonical_cli(self):
        with mock.patch.object(normalize.canonical_main, "main", return_value=7) as run:
            self.assertEqual(normalize.main(["--check", "--root", "notes"]), 7)
        run.assert_called_once_with(["--check", "--root", "notes"])

    def test_wrapper_uses_temporary_root(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "page.md").write_text("# Title\n\n", encoding="utf-8")
            self.assertEqual(normalize.main(["--check", "--root", str(root)]), 0)


if __name__ == "__main__":
    unittest.main()
