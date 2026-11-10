import importlib.util
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


root = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("wsg", root / "src/wsg/__init__.py")
wsg = importlib.util.module_from_spec(spec)
spec.loader.exec_module(wsg)


class InstallTest(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.base = Path(tmp.name) / "예제 project"
        self.source = Path(tmp.name) / "payload"
        (self.source / "skills").mkdir(parents=True)
        (self.source / "SKILL.md").write_text("Router")
        (self.source / "skills/reference.md").write_text("Read this reference.")

    def test_host_paths_scope_and_idempotence(self):
        for host, project, user in [
            ("codex", ".agents/skills", ".agents/skills"),
            ("claude", ".claude/skills", ".claude/skills"),
            ("pi", ".pi/skills", ".pi/agent/skills"),
            ("opencode", ".opencode/skills", ".config/opencode/skills"),
        ]:
            for user_scope, directory in [(False, project), (True, user)]:
                with self.subTest(host=host, user_scope=user_scope):
                    base = self.base / host / str(user_scope)
                    target = base / directory / "wsg"
                    self.assertIn(str(target), wsg.install(self.source, base, host, user_scope, True))
                    self.assertFalse(base.exists())
                    wsg.install(self.source, base, host, user_scope, False)
                    self.assertEqual((target / "skills/reference.md").read_text(), "Read this reference.")
                    self.assertIn("Already installed", wsg.install(self.source, base, host, user_scope, False))

    def test_preserves_modified_copies_and_symlinks(self):
        wsg.install(self.source, self.base, "codex", False, False)
        target = self.base / ".agents/skills/wsg"
        ref = target / "skills/reference.md"
        ref.write_text("My local edit.")
        with self.assertRaises(ValueError):
            wsg.install(self.source, self.base, "codex", False, False)
        self.assertEqual(ref.read_text(), "My local edit.")
        ref.unlink()
        ref.symlink_to(self.source / "skills/reference.md")
        with self.assertRaises(ValueError):
            wsg.install(self.source, self.base, "codex", False, False)
        target.rename(target.with_name("saved"))
        target.symlink_to(target.with_name("missing"))
        with self.assertRaises(ValueError):
            wsg.install(self.source, self.base, "codex", False, False)
        (self.base / ".pi").symlink_to(self.source, target_is_directory=True)
        with self.assertRaises(ValueError):
            wsg.install(self.source, self.base, "pi", False, False)
        self.assertFalse((self.source / "skills/wsg").exists())

    def test_interrupted_copy_leaves_no_skill(self):
        def interrupted(source, staged):
            staged.mkdir()
            (staged / "SKILL.md").write_text("Partial")
            raise OSError("out of space")

        with patch.object(wsg.shutil, "copytree", side_effect=interrupted):
            with self.assertRaises(OSError):
                wsg.install(self.source, self.base, "claude", False, False)
        self.assertEqual(list((self.base / ".claude/skills").iterdir()), [])
