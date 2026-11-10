import io
import sys
import tempfile
import unittest
from contextlib import ExitStack
from pathlib import Path
from unittest.mock import patch

from src import wsg


class HostSelectionTest(unittest.TestCase):
    def setUp(self):
        ctx = ExitStack()
        self.addCleanup(ctx.close)
        root = Path(ctx.enter_context(tempfile.TemporaryDirectory()))
        self.project = root / "project"
        self.project.mkdir()
        self.payload = root / "payload"
        self.payload.mkdir()
        (self.payload / "VERSION").write_text("0.1.0")
        ctx.enter_context(patch.object(Path, "cwd", return_value=self.project))
        self.terminal = ctx.enter_context(patch.object(sys.stdin, "isatty", return_value=True))
        self.output = ctx.enter_context(patch("sys.stdout", new_callable=io.StringIO))
        ctx.enter_context(patch.object(self.output, "isatty", return_value=True))
        executables = {"codex": "/a/codex", "pi": "/b/pi"}
        self.which = ctx.enter_context(patch.object(wsg.shutil, "which", side_effect=executables.get))

    def run_install(self, *args):
        with patch.object(sys, "argv", ["wsg", "install", *args]):
            wsg.main(self.payload)

    def test_detect_and_install_only_selected_hosts(self):
        with patch("builtins.input", return_value="pi"):
            self.run_install()
        self.assertIn("Detected on PATH: codex, pi", self.output.getvalue())
        self.assertEqual([path.relative_to(self.project) for path in self.project.rglob("VERSION")],
                         [Path(".pi/skills/wsg/VERSION")])

    def test_multiple_names_and_explicit_hosts(self):
        with patch("builtins.input", return_value="pi codex pi"):
            self.assertEqual(wsg.select_hosts(None), ["pi", "codex"])
        self.which.reset_mock()
        self.terminal.return_value = False
        self.run_install("--host", "claude", "--host", "pi")
        self.assertTrue((self.project / ".claude/skills/wsg/VERSION").is_file())
        self.assertTrue((self.project / ".pi/skills/wsg/VERSION").is_file())
        self.which.assert_not_called()

    def test_later_conflict_preserves_all_selected_destinations(self):
        existing = self.project / ".claude/skills/wsg"
        existing.mkdir(parents=True)
        (existing / "custom.md").write_text("local edit")
        with self.assertRaisesRegex(SystemExit, "Existing path"):
            self.run_install("--host", "codex", "--host", "claude")
        self.assertFalse((self.project / ".agents").exists())
        self.assertEqual((existing / "custom.md").read_text(), "local edit")

    def test_cancel_invalid_and_noninteractive_input_leave_no_installation(self):
        with patch("builtins.input", return_value=" "):
            self.run_install()
        with patch("builtins.input", side_effect=EOFError):
            self.run_install()
        with patch("builtins.input", return_value="pi invalid"), self.assertRaisesRegex(SystemExit, "invalid"):
            self.run_install()
        self.which.side_effect = lambda name: None
        with self.assertRaisesRegex(SystemExit, "No supported CLI"):
            self.run_install()
        self.terminal.return_value = False
        with self.assertRaisesRegex(SystemExit, "--host"):
            self.run_install()
        self.assertEqual(list(self.project.iterdir()), [])
