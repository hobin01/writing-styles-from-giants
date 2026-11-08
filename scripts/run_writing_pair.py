"""Read a public task from stdin and run two isolated GPT-6 Luna writing sessions."""

import argparse
import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
MODEL = "gpt-6-luna"


def generate(task, instructions=""):
    message = "Work only from this message. Do not use tools. Give the requested writing or artifact.\n"
    if instructions:
        message += f"Apply this writing method at standard level:\n{instructions}\n"
    message += f"\nUser request:\n{task}"
    with tempfile.TemporaryDirectory(prefix="writing-") as workspace:
        if Path(workspace).resolve().is_relative_to(ROOT):
            raise RuntimeError("Set TMPDIR outside the checkout to isolate evaluation sessions.")
        final = Path(workspace) / "answer.txt"
        result = subprocess.run(
            ["codex", "exec", "--ephemeral", "--ignore-user-config",
             "--disable", "plugins", "--disable", "shell_tool", "--enable", "omit_skill_descriptions",
             "--sandbox", "read-only", "--skip-git-repo-check", "--model", MODEL,
             "-c", 'model_reasoning_effort="low"', "-c", "project_doc_max_bytes=0",
             "-c", "suppress_unstable_features_warning=true", "--json", "-o", str(final), "-"],
            cwd=workspace, input=message, text=True, capture_output=True, timeout=240,
        )
        if result.returncode:
            raise RuntimeError(f"{MODEL} session failed: {result.stderr[-800:]} {result.stdout[-800:]}")
        events = [json.loads(line) for line in result.stdout.splitlines() if line.strip()]
        items = [event["item"] for event in events if event["type"].startswith("item.")]
        if (not events or events[-1]["type"] != "turn.completed"
                or any(item["type"] not in {"agent_message", "reasoning"} for item in items)
                or any(event["type"] in {"error", "turn.failed"} for event in events)):
            raise RuntimeError("Incomplete turn, CLI error or tool use during writing evaluation.")
        replies = [event["item"]["text"] for event in events if event["type"] == "item.completed"
                   and event["item"]["type"] == "agent_message"]
        if not replies or not replies[-1].strip() or final.read_text().rstrip("\n") != replies[-1].rstrip("\n"):
            raise RuntimeError("The final message and output file do not agree.")
        return replies[-1]


def run_pair(method_dir, task):
    paths = [method_dir / "SKILL.md", method_dir / "method.json", *sorted((method_dir / "locales").glob("*.json"))]
    instructions = "\n".join(f"<{p.name}>\n{p.read_text()}\n</{p.name}>" for p in paths)
    result = {"model": MODEL}
    for arm, context in (("without", ""), ("standard", instructions)):
        try:
            result[arm] = generate(task, context)
        except (OSError, ValueError, RuntimeError, subprocess.TimeoutExpired) as error:
            result["failure"] = {"arm": arm, "message": str(error)}
            break
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("method", choices=sorted(p.parent.name for p in (ROOT / "skills").glob("*/method.json")))
    args = parser.parse_args()
    task = sys.stdin.read()
    if not task.strip():
        parser.error("Supply the same nonempty writing request for both arms on stdin.")
    result = run_pair(ROOT / "skills" / args.method, task)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    sys.exit(1 if "failure" in result else 0)
