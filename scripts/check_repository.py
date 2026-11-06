"""Check the documentation foundation; this is not a product or model validator."""

import argparse
import json
import re
import subprocess
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlparse

REQUIRED = (
    "AGENTS.md", "CLAUDE.md", "README.md", "README.ko.md", "CONTRIBUTING.md",
    "LICENSE", "SECURITY.md", "THIRD_PARTY_NOTICES.md", "VERSION", "CHANGELOG.md",
    "docs/PROJECT.md", "docs/ARCHITECTURE.md", "docs/METHOD_AUTHORING.md",
    "docs/LOCALIZATION.md", "docs/COMPATIBILITY.md", "docs/DECISIONS.md",
    "docs/RELEASING.md", "docs/superpowers/plans/2026-11-06-mvp.md",
    ".gitignore", ".github/workflows/ci.yml", ".github/workflows/release.yml",
)
PRIVATE_DIRS = {"private", ".local", "work", "outputs", "node_modules", "dist", "__pycache__", ".venv", ".git"}
LEVELS = {"light", "standard", "strict"}
SEVERITIES = {"off", "advisory", "warning", "error"}


def public_path_errors(paths):
    errors = []
    for value in paths:
        path = PurePosixPath(value)
        secret_name = (
            path.name in {".env", ".npmrc", "AGENTS.local.md"}
            or (path.name.startswith(".env.") and path.name != ".env.example")
            or path.suffix in {".key", ".pem"}
            or path.name.endswith((".local.json", ".local.yaml", ".local.yml"))
        )
        if PRIVATE_DIRS.intersection(path.parts) or secret_name:
            errors.append(f"Private/generated path must not be tracked: {value}")
    return errors


def relative_link_errors(root, pages):
    errors = []
    root = root.resolve()
    for page in pages:
        if page.is_symlink():
            errors.append(f"{page.name}: symbolic-link documents are not allowed in the foundation.")
            continue
        page = page.resolve()
        if not page.is_relative_to(root) or public_path_errors([page.relative_to(root).as_posix()]):
            errors.append(f"{page.name}: document is outside the public repository boundary.")
            continue
        content = re.sub(r"```.*?```", "", page.read_text(), flags=re.DOTALL)
        for destination in re.findall(r"\[[^\]\n]+\]\(([^)\n]+)\)", content):
            destination = destination.strip().strip("<>")
            parsed = urlparse(destination)
            if parsed.scheme in {"http", "https", "mailto"} or not parsed.path:
                continue
            target = (page.parent / unquote(parsed.path)).resolve()
            if parsed.scheme or not target.is_relative_to(root):
                errors.append(f"{page.relative_to(root)}: link escapes repository: {destination}")
            elif public_path_errors([target.relative_to(root).as_posix()]):
                errors.append(f"{page.relative_to(root)}: link targets private/generated material: {destination}")
            elif not target.exists():
                errors.append(f"{page.relative_to(root)}: missing link target: {destination}")
    return errors


def release_errors(version, changelog, tag):
    if not re.fullmatch(r"v(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)", tag):
        return ["Release tag must be stable vMAJOR.MINOR.PATCH without leading zeros."]
    errors = []
    if version != tag[1:]:
        errors.append("Release tag does not match VERSION.")
    if f"## [{tag[1:]}]" not in changelog.splitlines():
        errors.append("Release version has no CHANGELOG section.")
    return errors


def example_errors(method, locales, cases):
    errors = []
    try:
        rules = method["rules"]
        ids = {rule["id"] for rule in rules}
        if len(ids) != len(rules):
            errors.append("Example method has duplicate rule IDs.")
        source_ids = {source["id"] for source in method["sources"]}
        for rule in rules:
            if not set(rule["sourceIds"]).issubset(source_ids):
                errors.append(f"Rule {rule['id']} refers to an unknown source.")
            levels = rule["levels"]
            if set(levels) != LEVELS or not set(levels.values()).issubset(SEVERITIES):
                errors.append(f"Rule {rule['id']} has invalid levels.")
            if rule["classification"] == "invariant" and "off" in levels.values():
                errors.append(f"Rule {rule['id']} disables an invariant.")
        for locale, data in locales.items():
            if data["method"] != method["id"] or data["methodVersion"] != method["version"]:
                errors.append(f"Locale {locale} has mismatched method/version.")
            if set(data["rules"]) != ids:
                errors.append(f"Locale {locale} does not cover the example rule IDs.")
        case_ids = set()
        for case in cases:
            if case["id"] in case_ids:
                errors.append(f"Duplicate example case ID: {case['id']}")
            case_ids.add(case["id"])
            if case["method"] != method["id"] or case["locale"] not in locales or case["level"] not in LEVELS:
                errors.append(f"Invalid example case context: {case['id']}")
            if not set(case["ruleIds"]).issubset(ids):
                errors.append(f"Example case {case['id']} refers to an unknown rule.")
            if not case["expectations"]:
                errors.append(f"Example case {case['id']} has no observable expectations.")
    except (KeyError, TypeError, AttributeError) as error:
        errors.append(f"Malformed example metadata: {error}")
    return errors


def validate(root, tag=None):
    root = root.resolve()
    errors = [f"Missing required file: {path}" for path in REQUIRED if not (root / path).is_file()]
    tracked = subprocess.run(["git", "ls-files", "-z"], cwd=root, capture_output=True, text=True, check=False)
    public = subprocess.run(["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"], cwd=root, capture_output=True, text=True, check=False)
    if tracked.returncode or public.returncode:
        return errors + ["Run in a Git repository so public paths can be checked."]
    errors.extend(public_path_errors(filter(None, tracked.stdout.split("\0"))))
    files = []
    for name in filter(None, public.stdout.split("\0")):
        if public_path_errors([name]):
            continue
        path = root / name
        resolved = path.resolve()
        if path.is_symlink():
            errors.append(f"Public source symlinks are not supported by the foundation checker: {name}")
        elif not resolved.is_relative_to(root) or public_path_errors([resolved.relative_to(root).as_posix()]):
            errors.append(f"Public source path resolves outside the public boundary: {name}")
        elif path.is_file():
            files.append(path)
    errors.extend(relative_link_errors(root, [path for path in files if path.suffix == ".md"]))
    for path in files:
        if path.suffix == ".json":
            try:
                json.loads(path.read_text())
            except (ValueError, UnicodeError) as error:
                errors.append(f"Invalid JSON in {path.relative_to(root)}: {error}")
    public_names = {path.relative_to(root).as_posix() for path in files}
    example_names = {"templates/method/method.example.json", "templates/method/locales/en.json", "templates/method/locales/ko.json", "evals/cases.example.json"}
    try:
        if not example_names.issubset(public_names):
            raise ValueError("Required example files are missing or outside the public boundary.")
        method = json.loads((root / "templates/method/method.example.json").read_text())
        locales = {locale: json.loads((root / f"templates/method/locales/{locale}.json").read_text()) for locale in ("en", "ko")}
        cases = json.loads((root / "evals/cases.example.json").read_text())
        errors.extend(example_errors(method, locales, cases))
    except (OSError, ValueError) as error:
        errors.append(f"Cannot load authoring examples: {error}")
    for workflow in [path for path in files if path.parent == root / ".github/workflows" and path.suffix == ".yml"]:
        for action in re.findall(r"uses:\s*([^\s]+)", workflow.read_text()):
            if not re.fullmatch(r"[^@]+@[0-9a-f]{40}", action):
                errors.append(f"Action must use an immutable SHA: {action}")
    if tag is not None:
        try:
            if not {"VERSION", "CHANGELOG.md"}.issubset(public_names):
                raise ValueError("Release metadata is missing or outside the public boundary.")
            errors.extend(release_errors((root / "VERSION").read_text().strip(), (root / "CHANGELOG.md").read_text(), tag))
        except (OSError, ValueError) as error:
            errors.append(f"Cannot read release metadata: {error}")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tag", help="Validate a stable release tag against VERSION and CHANGELOG.")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    errors = validate(root, args.tag)
    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors))
        return 1
    print("Foundation checks passed: required files, relative file links, JSON examples, action pins, and tracked public paths.")
    print("Not checked: external URLs, Markdown heading anchors, full JSON/YAML schemas, LLM quality, or host activation.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
