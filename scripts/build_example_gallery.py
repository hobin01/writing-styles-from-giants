"""Rebuild the English and Korean galleries from their portable comparisons."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MARKER = "<!-- Standard examples below are generated. -->"
GALLERIES = {
    "en": ("EXAMPLES.md", "standard.md", "portable example"),
    "ko": ("EXAMPLES.ko.md", "standard.ko.md", "스킬별 예제"),
}


def render(root, language="en"):
    filename, example_name, link_label = GALLERIES[language]
    other_language, other_label = ("ko", "한국어") if language == "en" else ("en", "English")
    other_page, other_example, _ = GALLERIES[other_language]
    page = (root / filename).read_text()
    intro, marker, _ = page.partition(MARKER)
    if not marker:
        raise ValueError(f"{filename} is missing the gallery marker.")
    methods = sorted((root / "skills").glob("*/method.json"))
    links = []
    sections = []
    for method in methods:
        example = method.parent / "examples" / example_name
        title, body = example.read_text().strip().split("\n", 1)
        name = method.parent.name
        # The portable page links to its sibling; the gallery links to the same method's section.
        body = body.removeprefix(f"\n[{other_label}]({other_example})\n")
        switch = f"[{other_label}]({other_page}#{name})"
        links.append(f"- [{name}](#{name}) · [{link_label}]({example.relative_to(root).as_posix()})"
                     f" · {switch}")
        sections.append(f"## {name}\n\n**{title.removeprefix('# ')}**\n\n{switch}\n" + body)
    return intro + MARKER + "\n\n" + "\n".join(links) + "\n\n" + "\n\n".join(sections) + "\n"


if __name__ == "__main__":
    pages = {ROOT / entry[0]: render(ROOT, lang) for lang, entry in GALLERIES.items()}
    for path, content in pages.items():
        path.write_text(content)
