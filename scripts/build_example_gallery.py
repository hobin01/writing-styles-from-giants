"""Collect the portable examples into the English and Korean galleries."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MARKER = "<!-- Generated from the portable examples. -->"
LEVELS = ("light", "standard", "strict")
GALLERIES = {"en": "EXAMPLES.md", "ko": "EXAMPLES.ko.md"}


def example_name(level, language):
    return f"{level}.ko.md" if language == "ko" else f"{level}.md"


def render(root, language="en"):
    page = root / GALLERIES[language]
    intro, marker, _ = page.read_text().partition(MARKER)
    if not marker:
        raise ValueError(f"{page.name} is missing the gallery marker.")
    question = "### 질문" if language == "ko" else "### Question"
    other_lang, other_label = ("en", "English") if language == "ko" else ("ko", "한국어")
    links, sections = [], []
    for method in sorted((root / "skills").glob("*/method.json")):
        name = method.parent.name
        directory = method.parent / "examples"
        canonical = (directory / example_name("standard", language)).read_text()
        title = canonical.splitlines()[0].removeprefix("# ")
        context = canonical.split(question + "\n", 1)[1].split("\n### Standard\n", 1)[0].strip()
        other = f"[{other_label}]({GALLERIES[other_lang]}#{name})"
        portable = "스킬별 예제" if language == "ko" else "skill examples"
        index = (directory / "README.md").relative_to(root).as_posix()
        links.append(f"- [{name}](#{name}) · {title} · [{portable}]({index})")
        sections.append(f"## {name}\n\n**{title}** · {other}\n\n{question}\n\n{context}")
        for level in LEVELS:
            path = directory / example_name(level, language)
            heading = f"### {level.title()}"
            answer = path.read_text().split(f"\n{heading}\n", 1)[1].strip()
            if name == "answer-with-html":
                # The downloadable page sits next to its portable Markdown example.
                artifact = path.with_suffix(".html")
                answer = answer.replace(f"]({artifact.name})", f"]({artifact.relative_to(root).as_posix()})", 1)
            sections.append(f"{heading}\n\n{answer}")
    return intro + MARKER + "\n\n" + "\n".join(links) + "\n\n" + "\n\n".join(sections) + "\n"


if __name__ == "__main__":
    for language, filename in GALLERIES.items():
        (ROOT / filename).write_text(render(ROOT, language))
