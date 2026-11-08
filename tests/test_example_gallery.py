import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from scripts.build_example_gallery import GALLERIES, MARKER, ROOT, render


class ExampleGalleryTest(unittest.TestCase):
    def test_language_selection_does_not_mix_answer_files(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            method = root / "skills/demo"
            (method / "examples").mkdir(parents=True)
            (method / "method.json").write_text("{}")
            for page in ("EXAMPLES.md", "EXAMPLES.ko.md"):
                (root / page).write_text(MARKER)
            (method / "examples/standard.md").write_text("# English\n\n[한국어](standard.ko.md)\n\nAnswer in English.")
            (method / "examples/standard.ko.md").write_text("# 한국어\n\n[English](standard.md)\n\n한국어 답안.")
            self.assertIn("Answer in English.", render(root, "en"))
            self.assertNotIn("한국어 답안.", render(root, "en"))
            self.assertIn("한국어 답안.", render(root, "ko"))
            self.assertNotIn("Answer in English.", render(root, "ko"))
            self.assertIn("[English](EXAMPLES.md#demo)", render(root, "ko"))
            self.assertNotIn("[English](standard.md)", render(root, "ko"))

    def test_published_galleries_contain_their_own_language_examples(self):
        for lang, (page, _, _) in GALLERIES.items():
            with self.subTest(language=lang):
                self.assertEqual((ROOT / page).read_text(), render(ROOT, lang),
                                 "Run python3 scripts/build_example_gallery.py after changing a comparison.")

    def test_each_skill_introduces_its_standalone_comparison(self):
        for method in (ROOT / "skills").glob("*/method.json"):
            with self.subTest(method=method.parent.name):
                examples = method.parent / "examples"
                readme = (examples / "README.md").read_text()
                for _, example, _ in GALLERIES.values():
                    self.assertTrue((examples / example).is_file())
                    self.assertIn(f"]({example})", readme)
