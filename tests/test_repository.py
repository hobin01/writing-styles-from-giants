import copy
import importlib.util
import json
import subprocess
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts/check_repository.py"
spec = importlib.util.spec_from_file_location("repository_checks", MODULE_PATH)
checks = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checks)


class RepositoryChecksTest(unittest.TestCase):
    def test_local_history_credentials_and_caches_are_rejected(self):
        paths = [
            '.local/history/session.md', '.local/credentials/account.json',
            '.history/change.json', '.credentials/token.json',
            'credentials.json', 'credentials.yaml', 'credentials.yml',
            'secrets.json', 'secrets.yaml', 'secrets.yml',
            '.cache/catalog.json', '.pytest_cache/state', '.mypy_cache/state',
            '.ruff_cache/state', '.coverage', '.coverage.worker', '.DS_Store',
        ]
        for path in paths:
            with self.subTest(path=path):
                self.assertTrue(checks.public_path_errors([path]))
        self.assertEqual(checks.public_path_errors([
            '.github/workflows/ci.yml', '.gitignore', '.env.example',
            '.public-note.md', 'credentials.example.json', 'docs/PROJECT.md',
        ]), [])

    def test_ignore_rules_exclude_local_files_without_hiding_public_dotfiles(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / '.gitignore').write_text((MODULE_PATH.parents[1] / '.gitignore').read_text())
            subprocess.run(['git', 'init', '--quiet', '--template='], cwd=root, check=True)
            local = [
                '.local/history/session.md', '.local/credentials/account.json',
                '.history/change.json', '.credentials/token.json', 'credentials.json',
                'secrets.yaml', '.cache/catalog.json', '.ruff_cache/state', '.coverage.worker',
            ]
            result = subprocess.run(
                ['git', '-c', 'core.excludesFile=/dev/null', 'check-ignore', '--no-index', '--stdin'],
                cwd=root, input='\n'.join(local) + '\n', capture_output=True, text=True,
            )
            self.assertEqual(set(result.stdout.splitlines()), set(local))
            public = ['.github/workflows/ci.yml', '.gitignore', '.env.example', '.public-note.md',
                      'credentials.example.json', 'scratch.tmp', 'work/check.md', 'outputs/debug.txt']
            result = subprocess.run(
                ['git', '-c', 'core.excludesFile=/dev/null', 'check-ignore', '--no-index', '--stdin'],
                cwd=root, input='\n'.join(public) + '\n', capture_output=True, text=True,
            )
            self.assertEqual(result.returncode, 1)
            self.assertEqual(result.stdout, '')

    def test_private_paths_are_rejected_but_public_examples_are_allowed(self):
        paths = ["private/draft.md", ".local/install.json", ".env.production", "id.key", "AGENTS.local.md"]
        self.assertEqual(len(checks.public_path_errors(paths)), len(paths))
        self.assertEqual(checks.public_path_errors([".env.example", "docs/PROJECT.md", "skills/plain/SKILL.md"]), [])

    def test_missing_and_escaping_links_are_reported(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "docs").mkdir()
            (root / "docs/valid.md").write_text("Valid\n")
            page = root / "README.md"
            page.write_text("[ok](docs/valid.md#section) [missing](docs/missing.md) [escape](../private.md) [web](https://example.com)\n")
            errors = checks.relative_link_errors(root, [page])
            self.assertEqual(len(errors), 2)
            self.assertTrue(any("missing.md" in error for error in errors))
            self.assertTrue(any("escapes" in error for error in errors))

    def test_private_documents_and_symlinks_are_rejected_before_reading(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "private").mkdir()
            secret = root / "private/draft.md"
            secret.write_text("Synthetic private fixture.\n")
            link = root / "public.md"
            link.symlink_to(secret)
            for page in (secret, link):
                with self.subTest(page=page.name):
                    self.assertTrue(checks.relative_link_errors(root, [page]))

    def test_release_requires_exact_stable_tag_version_and_changelog(self):
        self.assertEqual(checks.release_errors("0.1.0", "## [0.1.0]\n", "v0.1.0"), [])
        for tag in ["v01.1.0", "v0.1.0;echo bad", "v0.1.0-rc.1", "0.1.0"]:
            with self.subTest(tag=tag):
                self.assertTrue(checks.release_errors("0.1.0", "## [0.1.0]\n", tag))
        self.assertTrue(checks.release_errors("0.1.0-dev", "## [0.1.0]\n", "v0.1.0"))
        self.assertTrue(checks.release_errors("0.1.0", "## [Unreleased]\n", "v0.1.0"))

    def test_example_references_and_invariants_are_checked(self):
        method = {
            "id": "example-method", "version": "0.1.0", "sources": [],
            "rules": [{"id": "preserve", "classification": "invariant", "sourceIds": [],
                       "levels": {"light": "error", "standard": "error", "strict": "error"}}],
        }
        locale = {"method": "example-method", "methodVersion": "0.1.0", "rules": {"preserve": {}}}
        cases = [{"id": "case", "method": "example-method", "locale": "en", "level": "strict", "ruleIds": ["preserve"], "expectations": ["Keep meaning."]}]
        self.assertEqual(checks.example_errors(method, {"en": locale}, cases), [])
        method["rules"][0]["levels"]["light"] = "off"
        cases[0]["ruleIds"] = ["unknown-rule"]
        errors = checks.example_errors(method, {"en": locale}, cases)
        self.assertTrue(any("invariant" in error for error in errors))
        self.assertTrue(any("unknown rule" in error for error in errors))

    def catalog_fixture(self):
        method = json.loads((MODULE_PATH.parents[1] / "templates/method/method.example.json").read_text())
        locales = {"en": json.loads((MODULE_PATH.parents[1] / "templates/method/locales/en.json").read_text())}
        cases = [{"id": kind, "type": kind, "method": method["id"], "locale": "en", "level": "strict",
                  "source": "Only remove the old file after verifying the backup.", "ruleIds": ["preserve-meaning"],
                  "sourceIds": [], "expectations": ["Retain the backup verification condition."]}
                 for kind in ("ordinary", "exception", "meaning-preservation")]
        return method, locales, cases

    def test_catalog_rejects_broken_evidence_and_unverifiable_errors(self):
        method, locales, cases = self.catalog_fixture()
        self.assertEqual(checks.method_errors(method, locales, cases), [])
        mutations = (
            lambda m, l, c: m["rules"][1].update(provenance="faithful-summary"),
            lambda m, l, c: m["rules"][1]["levels"].update(strict="error"),
            lambda m, l, c: c[0].update(sourceIds=["unknown"]),
            lambda m, l, c: c.pop(),
            lambda m, l, c: l["en"].update(methodVersion="9.0.0"),
            lambda m, l, c: m["rules"][0].update(classification="guideline"),
            lambda m, l, c: m.update(languageScope="all-certified"),
        )
        for mutate in mutations:
            with self.subTest(mutation=mutate):
                m, l, c = copy.deepcopy((method, locales, cases))
                mutate(m, l, c)
                self.assertTrue(checks.method_errors(m, l, c))

    def test_catalog_checks_portable_unit_and_directory_identity(self):
        method, locales, cases = self.catalog_fixture()
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            unit = root / "skills/example-method"
            (unit / "locales").mkdir(parents=True)
            (unit / "SKILL.md").write_text("---\nname: example-method\ndescription: \"Edit explanatory prose.\"\n---\nApply the selected rules.\n")
            (unit / "method.json").write_text(json.dumps(method))
            (unit / "locales/en.json").write_text(json.dumps(locales["en"]))
            (unit / "cases.json").write_text(json.dumps(cases))
            files = [p for p in root.rglob("*") if p.is_file()]
            self.assertEqual(checks.catalog_errors(root, files), [])
            skill = unit / "SKILL.md"
            valid = skill.read_text()
            for bad in ("Edit: clear prose", "true", "null", "[\"use\", \"clear\"]"):
                skill.write_text(valid.replace('"Edit explanatory prose."', bad))
                self.assertTrue(checks.catalog_errors(root, files))
            skill.write_text(valid + "[external local file](../../README.md)\n")
            self.assertTrue(any("escapes" in e for e in checks.catalog_errors(root, files)))
            skill.write_text(valid)
            method["id"] = "another-method"
            (unit / "method.json").write_text(json.dumps(method))
            self.assertTrue(any("directory" in e for e in checks.catalog_errors(root, files)))
            self.assertTrue(any("missing" in e for e in checks.catalog_errors(root, [p for p in files if p.name != "cases.json"])))
            (unit / "method.json").write_text("null")
            self.assertTrue(checks.catalog_errors(root, files))

    def test_catalog_does_not_read_unadmitted_locale_paths(self):
        method, locales, cases = self.catalog_fixture()
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            unit = root / "skills/example-method"
            (unit / "locales").mkdir(parents=True)
            (unit / "SKILL.md").write_text("---\nname: example-method\ndescription: \"Edit prose.\"\n---\nApply rules.\n")
            (unit / "method.json").write_text(json.dumps(method))
            (unit / "cases.json").write_text(json.dumps(cases))
            (unit / "locales/en.json").symlink_to(root / "private-missing.json")
            files = [unit / name for name in ("SKILL.md", "method.json", "cases.json")]
            errors = checks.catalog_errors(root, files)
            self.assertTrue(any("at least one locale" in e for e in errors))
            self.assertFalse(any("cannot load" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
