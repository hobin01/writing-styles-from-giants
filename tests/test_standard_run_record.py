import hashlib
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RECORDS = ROOT / "evals/runs/2026-11-09-standard/records"


class StandardRunRecordTest(unittest.TestCase):
    def test_recorded_answers_match_their_prompts_and_hashes(self):
        for path in RECORDS.glob("*.json"):
            record = json.loads(path.read_text())
            for revision in record["revisions"]:
                self.assertEqual(set(revision["runs"]), {"en", "ko", "transfer"})
                for key, run in revision["runs"].items():
                    with self.subTest(method=path.stem, version=revision["version"], case=key):
                        if run.get("valid") is False:
                            self.assertTrue(run["reason"])
                            self.assertNotIn("answer", run)
                            continue
                        case = record["cases"][key]
                        for field, value in (("answer", run["answer"]), ("prompt", case["prompt"])):
                            self.assertEqual(hashlib.sha256(value.encode()).hexdigest(), run[field + "_sha256"])
                        self.assertEqual(len(run["adjudicated_standard"]), len(case["checks"]))

    def test_gallery_uses_the_published_scores_for_this_run(self):
        records = sorted(RECORDS.glob("*.json"))
        self.assertEqual(len(records), 13)
        for path in records:
            record = json.loads(path.read_text())
            final = record["revisions"][-1]
            for lang, filename in (("en", "standard.md"), ("ko", "standard.ko.md")):
                page = (ROOT / "skills" / path.stem / "examples" / filename).read_text()
                if "2026-11-09 ·" not in page:
                    continue  # A later gallery can publish a different evaluation.
                with self.subTest(method=path.stem, lang=lang):
                    run = final["runs"][lang]
                    self.assertIn(run["answer_sha256"][:12], page)
                    self.assertIn(f"`{path.stem}` {final['version']} ·", page)
                    for check, passed in zip(record["cases"][lang]["checks"], run["adjudicated_standard"]):
                        verdict = ("Met" if passed else "Missed") if lang == "en" else ("충족" if passed else "미충족")
                        rows = [s for s in page.splitlines() if s.startswith(f"| {check} | ")]
                        self.assertEqual(len(rows), 1)
                        self.assertTrue(rows[0].endswith(f"| {verdict} |"))
