from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from scripts.build_example_gallery import GALLERIES, LEVELS, MARKER, ROOT, example_name, render


class ExampleGalleryTest(unittest.TestCase):
    def test_gallery_collects_all_levels_and_only_its_language(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            directory = root / "skills/demo/examples"
            directory.mkdir(parents=True)
            (directory.parent / "method.json").write_text("{}")
            for lang, page in GALLERIES.items():
                (root / page).write_text(MARKER)
                question = "Question" if lang == "en" else "질문"
                for level in LEVELS:
                    page = directory / example_name(level, lang)
                    page.write_text(f"# Case\n\n### {question}\n\n{lang}-case\n\n"
                                    f"### {level.title()}\n\n{lang}-{level}-answer\n")
            for lang in GALLERIES:
                with self.subTest(language=lang):
                    gallery = render(root, lang)
                    self.assertEqual(gallery.count(f"{lang}-case"), 1)
                    for level in LEVELS:
                        self.assertIn(f"{lang}-{level}-answer", gallery)
                        self.assertNotIn(f"{'ko' if lang == 'en' else 'en'}-{level}-answer", gallery)

    def test_published_examples_and_galleries(self):
        for lang, filename in GALLERIES.items():
            with self.subTest(language=lang):
                self.assertEqual((ROOT / filename).read_text(), render(ROOT, lang),
                                 "Run python3 scripts/build_example_gallery.py.")
        for method in (ROOT / "skills").glob("*/method.json"):
            directory = method.parent / "examples"
            readme = (directory / "README.md").read_text()
            for lang in GALLERIES:
                for level in LEVELS:
                    page = directory / example_name(level, lang)
                    with self.subTest(page=page):
                        self.assertIn(f"]({page.name})", readme)
                        self.assertTrue(page.read_text().split(f"\n### {level.title()}\n", 1)[1].strip())

    def test_html_pages_match_the_documents_shown_in_the_gallery(self):
        directory = ROOT / "skills/answer-with-html/examples"
        for lang in GALLERIES:
            for level in LEVELS:
                page = directory / example_name(level, lang)
                with self.subTest(page=page):
                    artifact = page.with_suffix(".html")
                    self.assertIn(f"]({artifact.name})", page.read_text())
                    self.assertIn(artifact.read_text().strip(), page.read_text())
