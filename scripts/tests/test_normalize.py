"""Тесты единой точки входа."""
import io
import subprocess
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest import mock

from scripts import normalize


class NormalizeTest(unittest.TestCase):
    def run_main(self, *args):
        output = io.StringIO()
        with mock.patch.object(normalize.subprocess, "run") as run, redirect_stdout(output):
            run.return_value = subprocess.CompletedProcess(args=[], returncode=0)
            code = normalize.main(list(args))
        return code, run.call_args_list

    def test_rejects_unknown_arguments(self):
        code, calls = self.run_main("--fix")

        self.assertEqual(code, 2)
        self.assertEqual(calls, [])

    def test_fix_run_uses_expected_commands(self):
        code, calls = self.run_main()

        self.assertEqual(code, 0)
        commands = [call.args[0] for call in calls]
        self.assertEqual(len(commands), 3)
        self.assertTrue(commands[0][1].endswith("ensure_blank_after_embed.py"))
        self.assertTrue(commands[1][1].endswith("convert_links.py"))
        self.assertEqual(commands[1][2:], ["apply-all"])
        self.assertTrue(commands[2][1].endswith("check_math.py"))

    def test_check_run_passes_check_flag(self):
        code, calls = self.run_main("--check")

        self.assertEqual(code, 0)
        for call in calls:
            self.assertEqual(call.args[0][-1], "--check")

    def test_stops_on_first_failure(self):
        with mock.patch.object(normalize.subprocess, "run") as run:
            run.return_value = subprocess.CompletedProcess(args=[], returncode=1)
            code = normalize.main(["--check"])

        self.assertEqual(code, 1)
        self.assertEqual(run.call_count, 1)


class NormalizeIntegrationTest(unittest.TestCase):
    """Настоящие скрипты на временном хранилище не запускаются: они смотрят в itmo-notebook."""

    def test_scripts_exist(self):
        for script, _ in normalize.FIX_COMMANDS:
            self.assertTrue((normalize.SCRIPT_DIR / script).is_file(), script)

    def test_repository_is_canonical(self):
        result = subprocess.run(
            ["python", str(normalize.SCRIPT_DIR / "normalize.py"), "--check"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
