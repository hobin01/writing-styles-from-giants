# writing-styles-from-giants

[한국어](README.ko.md)

When I ask an AI to “explain this simply,” it sometimes cuts the part I wanted to understand. Explaining a bicycle brake to a five-year-old is a different job from explaining its mechanism to an engineer. I made this project so I could choose **who the explanation is for and how it should work**. I wanted to put earlier writers’ methods to work on my own questions, which is where “standing on the shoulders of giants” comes in.

Choose the [English examples](EXAMPLES.md) or [한국어 예제](EXAMPLES.ko.md). For each of the 22 skills, GPT-6 Luna received the English and Korean questions independently, with and without the skill. Try [two DNS caches with different clocks](skills/feynman-technique/examples/standard.md), [LIGO’s false-alarm rate](skills/imrad/examples/standard.md), or [Seoul’s subway map redesign](skills/hunminjeongeum/examples/standard.md). Each page shows the sources, both actual answers and what they got right or missed on a task designed for high-school reasoning or above.

## Try it in Codex

Open this repository as your project. Copy one line into a new conversation, including the `$`.

```text
$wsg eli5 Explain why a bicycle wheel slows down when I squeeze the brake.
$wsg asd-ste100 strict Edit this note: The access panel may be opened only after both lamps go out.
$wsg auto Draft a design doc comparing a read cache with reading the database every time.
$wsg docs en
```

- **Know the method?** Use `$wsg METHOD [LEVEL] REQUEST`. Leaving out the level selects `standard` on every call. Choose `light` for a lighter edit or `strict` to check every applicable rule. Conditions and numbers retain their meaning at every level.
- **Want help choosing?** Use `$wsg auto [LEVEL] REQUEST`. It selects a skill for the task and reader, tells you why it fits and uses it to answer.
- **Want to browse?** Use `$wsg docs`. English is the default. `$wsg docs ko` explains each skill in Korean and `$wsg docs en` does so in English.

In Claude Code the same commands are spelled `/wsg`, `/wsg:auto` and `/wsg:docs en`. The configuration belongs to this checkout. [Host verification](docs/COMPATIBILITY.md)

## Which skill should I choose?

For the brake example, **ELI5** helps a child follow the movement from hand to wheel. **Feynman** helps the writer find a missing step in an explanation. For a claim that needs a mathematical proof, use **GTM**. Each name below opens the instructions and a worked example. The [command catalog](commands/catalog.en.md) gives you the exact IDs to type, such as `feynman-technique`.

| What I want to do | Skills |
| --- | --- |
| Explain something | [ELI5](skills/eli5/SKILL.md) · [Feynman](skills/feynman-technique/SKILL.md) · [Boring Professor](skills/boring-professor/SKILL.md) · [Interactive HTML](skills/answer-with-html/SKILL.md) · [Jobs presentation](skills/steve-jobs-presentation/SKILL.md) |
| Build an argument | [GTM proofs](skills/gtm-formal/SKILL.md) · [Aristotelian syllogisms](skills/aristotle-syllogism/SKILL.md) · [Socratic questions](skills/socratic-self-questioning/SKILL.md) · [Hunminjeongeum](skills/hunminjeongeum/SKILL.md) · [Minto Pyramid](skills/minto-pyramid/SKILL.md) |
| Edit the wording | [ASD-STE100-inspired English](skills/asd-ste100/SKILL.md) · [Orwell](skills/orwell-six-rules/SKILL.md) · [Federal Plain Language](skills/federal-plain-language/SKILL.md) · [Microsoft Style](skills/microsoft-writing-style/SKILL.md) · [New Hart’s Rules](skills/new-harts-rules/SKILL.md) · [Korean plain language](skills/korean-plain-language/SKILL.md) |
| Write a document | [Diátaxis](skills/diataxis/SKILL.md) · [Google design doc](skills/google-design-doc/SKILL.md) · [Amazon six-pager](skills/amazon-six-page-narrative/SKILL.md) · [IETF RFC](skills/ietf-rfc/SKILL.md) · [IMRaD](skills/imrad/SKILL.md) · [NIST technical report](skills/nist-technical-publication/SKILL.md) |

In ASD, `normal` is an alias for `standard`. The `strict` level applies the strongest profile this project implements. Full ASD-STE100 compliance has not been verified.

The [bibliography](docs/REFERENCE.md) records the sources for each method. Original material uses the [MIT license](LICENSE). See [third-party rights](THIRD_PARTY_NOTICES.md) and [how to contribute](CONTRIBUTING.md).
