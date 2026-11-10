# writing-styles-from-giants

[한국어](README.ko.md)

When I ask an AI to “explain this simply,” it sometimes cuts the part I wanted to understand. Explaining a bicycle brake to a five-year-old is a different job from explaining its mechanism to an engineer. I made this project so I could choose **who the explanation is for and how it should work**. I wanted to put earlier writers’ methods to work on my own questions, which is where “standing on the shoulders of giants” comes in.

What happens when floating ice melts? Read how GPT-6 Luna answers that question with and without ELI5. Or see how Feynman explains why two DNS resolvers disagree. [Floating ice](skills/eli5/examples/standard.md) · [DNS caching](skills/feynman-technique/examples/standard.md)

Every example shows the question and both answers on one page. For each question, you can read GPT-6 Luna’s answer without the skill and its answers at `light`, `standard` and `strict`. The same no-skill answer appears on all three pages so you can use it as a reference. English and Korean answers each came from separate sessions in that language. [English examples](EXAMPLES.md) · [한국어 예제](EXAMPLES.ko.md)

## Install for a local agent

Install the `wsg` command once from the GitHub Release using Python 3.10 or later and [uv](https://docs.astral.sh/uv/getting-started/installation/).

```sh
uv tool install https://github.com/hobin01/writing-styles-from-giants/releases/download/v0.1.2/writing_styles_from_giants-0.1.2-py3-none-any.whl
```

If your shell cannot find `wsg`, run `uv tool update-shell` and open a new terminal. Choose your agent below. Run the install command in the project where you want the skill. To use it in all your projects, add `--global`, for example `wsg install --host codex --global`. Then open the agent in a new session and enter the example **in the chat**.

| Local agent | Install in this project | Try it |
| --- | --- | --- |
| Codex CLI | `wsg install --host codex` | `$wsg eli5 Explain why a bicycle slows down when I squeeze the brake.` |
| Claude Code | `wsg install --host claude` | `/wsg auto Draft a design doc comparing a cache with direct database reads.` |
| OpenCode | `wsg install --host opencode` | `Load the wsg skill and run: docs en` |
| Pi | `wsg install --host pi` | `/skill:wsg feynman-technique Explain why two DNS resolvers can disagree.` |

After selecting the skill, use `METHOD [LEVEL] REQUEST` to choose a method, `auto [LEVEL] REQUEST` to ask WSG to choose and explain its choice, or `docs en` / `docs ko` to browse. Writing defaults to `standard` on each request. Choose `light` for a lighter edit and `strict` for all applicable checks. See [host paths, tested versions and limits](docs/COMPATIBILITY.md).

### ChatGPT

**Desktop with a local project.** Use the Codex installation row above, open that project in the ChatGPT desktop app and check **Skills** in the sidebar. If `wsg` is listed, type `@`, select it, then enter `docs en`. [OpenAI’s skill guide](https://learn.chatgpt.com/docs/build-skills)

**Web.** Create a ChatGPT Project and add the files for the method you want to its **Sources**. For ELI5, download the [instructions](skills/eli5/SKILL.md), [method rules](skills/eli5/method.json) and [locale profile](skills/eli5/locales/en.json). In a chat inside that project, ask: “Use the uploaded ELI5 instructions and rules at standard level. Why does a bicycle slow down when I squeeze the brake?” The files stay available for later chats in that project. This manual setup works one method at a time. For other methods, include any additional reference the instructions require at your chosen level. [ChatGPT Projects](https://learn.chatgpt.com/docs/projects)

## Install offline

Download [Source code (zip)](https://github.com/hobin01/writing-styles-from-giants/archive/refs/tags/v0.1.2.zip), transfer it to the offline computer and extract it. Python 3.10 or later is the only installation prerequisite. From the extracted folder, install for your user with:

```sh
python3 install.py install --host codex --global
```

For a single project, run the following command **from that project**, using the full path to the extracted installer. Choose a host from the table above.

```sh
python3 "/path/to/writing-styles-from-giants-0.1.2/install.py" install --host codex
```

The [dedicated offline ZIP](https://github.com/hobin01/writing-styles-from-giants/releases/download/v0.1.2/wsg-offline-v0.1.2.zip) also includes an installer and has a [SHA-256 checksum](https://github.com/hobin01/writing-styles-from-giants/releases/download/v0.1.2/SHA256SUMS). [Offline installation guide](docs/OFFLINE.md)

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
