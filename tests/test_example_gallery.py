import unittest

from scripts.build_example_gallery import ROOT, render


class ExampleGalleryTest(unittest.TestCase):
    def test_published_gallery_contains_the_current_skill_examples(self):
        self.assertEqual((ROOT / "EXAMPLES.md").read_text(), render(ROOT),
                         "Run python3 scripts/build_example_gallery.py after changing a comparison.")

    def test_each_skill_introduces_its_standalone_comparison(self):
        for method in (ROOT / "skills").glob("*/method.json"):
            with self.subTest(method=method.parent.name):
                examples = method.parent / "examples"
                self.assertTrue((examples / "standard.md").is_file())
                self.assertRegex((examples / "README.md").read_text(), r"\[[^\]\n]+\]\(standard\.md\)")
