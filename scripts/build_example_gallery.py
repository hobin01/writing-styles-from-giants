"""Collect the portable examples into the English and Korean galleries."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MARKER = "<!-- Generated from the portable examples. -->"
LEVELS = ("light", "standard", "strict")
GALLERIES = {"en": "EXAMPLES.md", "ko": "EXAMPLES.ko.md"}
HEADINGS = {
    "en": ("Question", "With the skill", "Without the skill"),
    "ko": ("질문", "스킬 적용", "스킬 미적용"),
}


def example_name(level, language):
    return f"{level}.ko.md" if language == "ko" else f"{level}.md"


def read_example(path, language):
    text = path.read_text()
    title = text.partition("\n")[0]
    if not title.startswith("# ") or not title[2:].strip():
        raise ValueError(f"{path} needs a question title.")

    def split_at(body, heading):
        before, marker, after = body.partition(f"\n### {heading}\n")
        if not marker:
            raise ValueError(f"{path} is missing the {heading} section.")
        return before.strip(), after

    question_label, applied_label, without_label = HEADINGS[language]
    _, body = split_at(text, question_label)
    question, answers = split_at(body, applied_label)
    applied, without = split_at(answers, without_label)
    if not any(line.startswith("> ") and line[2:].strip() for line in question.splitlines()):
        raise ValueError(f"{path} needs the full quoted question.")
    if not applied.strip("> \t\r\n") or not without.strip("> \t\r\n"):
        raise ValueError(f"{path} needs both answers.")
    return title[2:], question, applied, without.strip()


def render(root, language="en"):
    page = root / GALLERIES[language]
    intro, marker, _ = page.read_text().partition(MARKER)
    if not marker:
        raise ValueError(f"{page.name} is missing the gallery marker.")
    question_label, applied_label, without_label = HEADINGS[language]
    other_lang, other_label = ("en", "English") if language == "ko" else ("ko", "한국어")
    links, sections = [], []
    for method in sorted((root / "skills").glob("*/method.json")):
        name = method.parent.name
        directory = method.parent / "examples"
        other = f"[{other_label}]({GALLERIES[other_lang]}#{name})"
        portable = "스킬별 예제" if language == "ko" else "skill examples"
        index = (directory / "README.md").relative_to(root).as_posix()
        shared = None
        for level in LEVELS:
            path = directory / example_name(level, language)
            title, question, applied, without = read_example(path, language)
            if shared is None:
                shared = (title, question, without)
                links.append(f"- [{name}](#{name}) · {title} · [{portable}]({index})")
                sections.append(f"## {name}\n\n**{title}** · {other}\n\n### {question_label}\n\n{question}")
            elif shared != (title, question, without):
                raise ValueError(f"{path} must use the same title, question, sources and control answer at every level.")
            if name == "answer-with-html":
                # The downloadable page sits next to its portable Markdown example.
                artifact = path.with_suffix(".html")
                applied = applied.replace(f"]({artifact.name})", f"]({artifact.relative_to(root).as_posix()})", 1)
            sections.append(f"### {level.title()}\n\n#### {applied_label}\n\n{applied}\n\n"
                            f"#### {without_label}\n\n{without}")
    return intro + MARKER + "\n\n" + "\n".join(links) + "\n\n" + "\n\n".join(sections) + "\n"


if __name__ == "__main__":
    for language, filename in GALLERIES.items():
        (ROOT / filename).write_text(render(ROOT, language))
