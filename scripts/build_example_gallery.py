"""Rebuild the single-file gallery from the portable standard comparisons."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MARKER = "<!-- Standard examples below are generated. -->"


def render(root):
    page = (root / "EXAMPLES.md").read_text()
    intro, marker, _ = page.partition(MARKER)
    if not marker:
        raise ValueError("EXAMPLES.md is missing the gallery marker.")
    methods = sorted((root / "skills").glob("*/method.json"))
    links = []
    sections = []
    for method in methods:
        example = method.parent / "examples/standard.md"
        title, body = example.read_text().strip().split("\n", 1)
        name = method.parent.name
        links.append(f"- [{name}](#{name}) · [portable copy]({example.relative_to(root).as_posix()})")
        sections.append(f"## {name}\n\n**{title.removeprefix('# ')}**\n" + body)
    return intro + MARKER + "\n\n" + "\n".join(links) + "\n\n" + "\n\n".join(sections) + "\n"


if __name__ == "__main__":
    (ROOT / "EXAMPLES.md").write_text(render(ROOT))
