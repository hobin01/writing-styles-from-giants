import re
import unittest
from pathlib import Path


class CommandCatalogTest(unittest.TestCase):
    def test_each_docs_language_links_every_selectable_method_once(self):
        root = Path(__file__).resolve().parents[1]
        methods = sorted(path.parent.name for path in (root / "skills").glob("*/method.json"))
        for language in ("en", "ko"):
            with self.subTest(language=language):
                catalog = (root / "commands" / f"catalog.{language}.md").read_text()
                entries = re.findall(r"^\| \[`([a-z0-9-]+)`\]\(([^)]+)\) \| (.+?) \|$", catalog, re.M)
                self.assertEqual(sorted(name for name, _, _ in entries), methods)
                for name, target, purpose in entries:
                    self.assertEqual(target, f"../skills/{name}/SKILL.md")
                    self.assertTrue(purpose.strip())
