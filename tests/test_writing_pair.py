import json
from pathlib import Path
from subprocess import CompletedProcess
import unittest
from unittest.mock import patch

from scripts.run_writing_pair import ROOT, generate, run_pair


class WritingPairTest(unittest.TestCase):
    @patch("scripts.run_writing_pair.subprocess.run")
    def test_both_arms_use_luna_and_only_treatment_receives_skill(self, run):
        calls = []

        def codex(args, *, cwd, input, **kwargs):
            calls.append((cwd, input))
            self.assertEqual(args[args.index("--model") + 1], "gpt-6-luna")
            self.assertEqual(list(Path(cwd).iterdir()), [])
            answer = f"Answer {len(calls)}"
            Path(args[args.index("-o") + 1]).write_text(answer)
            item = {"type": "agent_message", "text": answer}
            events = [dict(type="item.completed", item=item), dict(type="turn.completed")]
            return CompletedProcess(args, 0, "\n".join(map(json.dumps, events)), "")

        run.side_effect = codex
        task = "Explain the rule.\nPreserve `--strict` as text."
        pair = run_pair(ROOT / "skills/eli5", task)
        self.assertEqual([pair["without"], pair["standard"]], ["Answer 1", "Answer 2"])
        self.assertNotEqual(calls[0][0], calls[1][0])
        for wd, msg in calls:
            self.assertFalse(Path(wd).exists())
            self.assertEqual(msg.partition("\nUser request:\n")[2], task)
        self.assertNotIn("<SKILL.md>", calls[0][1])
        self.assertIn("<SKILL.md>", calls[1][1])

    @patch("scripts.run_writing_pair.subprocess.run")
    def test_tool_use_is_rejected_even_with_a_completed_turn(self, run):
        for event_type in ("item.started", "item.completed"):
            with self.subTest(event_type=event_type):
                events = [{"type": event_type, "item": {"type": "command_execution"}},
                          {"type": "turn.completed"}]
                run.return_value = CompletedProcess([], 0, "\n".join(map(json.dumps, events)), "")
                with self.assertRaisesRegex(RuntimeError, "tool use"):
                    generate("Write one sentence.")

    @patch("scripts.run_writing_pair.generate", side_effect=["Actual first answer", RuntimeError("model unavailable")])
    def test_failed_treatment_preserves_baseline_without_substitution(self, generate_mock):
        result = run_pair(ROOT / "skills/eli5", "Explain this rule.")
        self.assertEqual(generate_mock.call_count, 2)
        self.assertEqual(result, {"model": "gpt-6-luna", "without": "Actual first answer",
                                  "failure": {"arm": "standard", "message": "model unavailable"}})
