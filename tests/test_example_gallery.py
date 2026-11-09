from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from scripts.build_example_gallery import GALLERIES, HEADINGS, LEVELS, MARKER, ROOT, example_name, read_example, render


class ExampleGalleryTest(unittest.TestCase):
    def test_gallery_collects_both_answers_for_every_level_in_its_language(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            directory = root / "skills/demo/examples"
            directory.mkdir(parents=True)
            (directory.parent / "method.json").write_text("{}")
            for lang, filename in GALLERIES.items():
                (root / filename).write_text(MARKER)
                question, applied, without = HEADINGS[lang]
                for level in LEVELS:
                    path = directory / example_name(level, lang)
                    path.write_text(f"# Case\n\n### {question}\n\n> {lang}-case\n"
                                    f"\n### {applied}\n\n> {lang}-{level}-applied\n"
                                    f"\n### {without}\n\n> {lang}-baseline\n")
            for lang in GALLERIES:
                with self.subTest(language=lang):
                    gallery = render(root, lang)
                    self.assertEqual(gallery.count(f"{lang}-case"), 1)
                    for level in LEVELS:
                        _, applied, without = HEADINGS[lang]
                        self.assertIn(f"### {level.title()}\n\n#### {applied}\n\n> {lang}-{level}-applied\n\n"
                                      f"#### {without}\n\n> {lang}-baseline", gallery)
                        self.assertNotIn(f"{'ko' if lang == 'en' else 'en'}-{level}-", gallery)
            path = directory / "strict.md"
            original = path.read_text()
            for text in ("en-case", "en-baseline"):
                with self.subTest(drift=text):
                    path.write_text(original.replace(text, "Changed"))
                    with self.assertRaises(ValueError):
                        render(root)

    def test_example_requires_a_question_and_two_answers(self):
        with TemporaryDirectory() as tmp:
            page = Path(tmp) / "light.md"
            sample = ("# Case\n\n### Question\n\n> What follows?\n\n**Sources** · Example\n"
                      "\n### With the skill\n\n> Applied.\n\n### Without the skill\n\n> Control.\n")
            for missing in ["What follows?", "Applied.", "Control.", "### Without the skill"]:
                with self.subTest(missing=missing):
                    page.write_text(sample.replace(missing, ""))
                    with self.assertRaises(ValueError):
                        read_example(page, "en")

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

    def test_html_pages_match_the_documents_shown_in_the_gallery(self):
        directory = ROOT / "skills/answer-with-html/examples"
        for lang in GALLERIES:
            for level in LEVELS:
                page = directory / example_name(level, lang)
                with self.subTest(page=page):
                    artifact = page.with_suffix(".html")
                    _, _, applied, _ = read_example(page, lang)
                    self.assertIn(f"]({artifact.name})", applied)
                    self.assertIn(artifact.read_text().strip(), applied)
                    self.assertIn(f"]({artifact.relative_to(ROOT).as_posix()})",
                                  (ROOT / GALLERIES[lang]).read_text())
