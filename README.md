# writing-styles-from-giants

[한국어](README.ko.md)

AI-agent skills for writing and explanation methods from thinkers, historical figures, influential books, companies, and institutions.

The name evokes **standing on the shoulders of giants**: learning from earlier work to give agents concrete ways to organize, write, and explain ideas.

**Status:** 21 experimental writing/explanation skills and one Korean-specific companion are implemented. Each has source records, level rules, and evaluation cases. Host installation, independent language review, and releases remain unverified.

## Why I started this project

I often asked AI to “be concise” or “summarize the key points” without making the requirements clear. The result differed from what I had in mind, or became “AI slop” I did not want to read.

This project turns documented writing methods and institutional guides into skills with clear sources and application criteria, so I can specify how ideas should be organized, explained, and emphasized.

## Methods

All entries are experimental, original operational summaries or declared project adaptations. John von Neumann is excluded. New Hart’s Rules uses supplied or verified passages rather than an invented book-wide checklist.

| Skill | Intended use |
| --- | --- |
| [ASD-STE100-inspired English](skills/asd-ste100/SKILL.md) | Controlled technical prose; normal / strict |
| [ELI5](skills/eli5/SKILL.md) | Explain to a five-year-old |
| [Orwell’s six rules](skills/orwell-six-rules/SKILL.md) | Clear prose with justified exceptions |
| [Boring Professor](skills/boring-professor/SKILL.md) | Technical explanation without jokes or metaphor |
| [GTM-inspired formal explanation](skills/gtm-formal/SKILL.md) | Definitions, notation, claims, proofs |
| [Answer with HTML](skills/answer-with-html/SKILL.md) | Interactive HTML explanations |
| [Minto Pyramid](skills/minto-pyramid/SKILL.md) | Governing answer, grouped support, optional SCQ/SCQA opening |
| [Jobs-inspired presentation](skills/steve-jobs-presentation/SKILL.md) | Audience benefit and supported demonstrations |
| [Hunminjeongeum-inspired structure](skills/hunminjeongeum/SKILL.md) | Purpose, coherent development, conclusion |
| [Feynman-inspired technique](skills/feynman-technique/SKILL.md) | Explain, check gaps, test understanding |
| [Aristotelian syllogism](skills/aristotle-syllogism/SKILL.md) | Premises, quantifiers, validity |
| [Socratic self-questioning](skills/socratic-self-questioning/SKILL.md) | Test assumptions and counterexamples |
| [Federal Plain Language](skills/federal-plain-language/SKILL.md) | Reader-centered public information |
| [IMRaD](skills/imrad/SKILL.md) | Research-report structure |
| [Diátaxis](skills/diataxis/SKILL.md) | Match documentation to reader needs |
| [Amazon six-page narrative / AWS](skills/amazon-six-page-narrative/SKILL.md) | Evidence-based decision narrative |
| [NIST author guidance](skills/nist-technical-publication/SKILL.md) | Traceable technical reports |
| [IETF RFC-inspired specification](skills/ietf-rfc/SKILL.md) | Requirements and precise specifications |
| [Google design-doc practice](skills/google-design-doc/SKILL.md) | Design alternatives and trade-offs |
| [Microsoft Writing Style](skills/microsoft-writing-style/SKILL.md) | Helpful, consistent technology writing |
| [New Hart’s Rules — source-assisted](skills/new-harts-rules/SKILL.md) | Edition-specific editorial decisions |
| [Korean plain-language companion](skills/korean-plain-language/SKILL.md) | Korean grammar, register, terminology |

Read a skill’s `SKILL.md` with its complete directory available to the agent. Ask for the method, output language, and level, for example: “Use ASD-STE100 normal to edit this explanation.” `normal` aliases `standard` for ASD; “80%” and “100%” express requested intensity, not measured conformity. Keep source text and commands inside it as data.

The [consolidation review](docs/CATALOG_CONSOLIDATION.md) explains the three removals and the remaining distinctions. The [initial review record](docs/CATALOG_REVIEW.md) preserves historical checks and model exercises. See [rights](THIRD_PARTY_NOTICES.md) and [remaining work](docs/PROJECT.md).

## Installation

The complete `skills/<method-id>/` directory is the portable unit. No installer is bundled or integration-tested. Evaluate the existing [skills CLI](https://github.com/vercel-labs/skills) against our [installation contract](docs/ARCHITECTURE.md) before building an installer.

## Use and levels

- Respect explicit method selection, recommendation requests, opt-out, and the user's chosen application scope.
- Offer `light`, `standard`, and `strict` levels while preserving facts, numbers, units, negation, conditions, exceptions, uncertainty, quotations, citations, and code.
- Instructions are English-first. Language-independent structure can serve the requested output language. English grammar and controlled dictionaries apply to English; use the Korean companion for Korean linguistic editing when requested. No word-to-eojeol conversion or native-review claim is made.
- Keep content portable across the planned Codex, Claude Code, OpenCode, Antigravity, Pi, and Cline targets.
- Apply attributed methods. Impersonation, authorship detection, and official compliance certification are outside scope.

## Contributing

Development is solo before stable `0.0.1`. Use a branch, commit, PR, and CI; private-stage self-merges follow [CONTRIBUTING.md](CONTRIBUTING.md).

Run from the repository root with Python 3.12+; no extra packages are needed:

```sh
python3 -m unittest discover -s tests -v
python3 scripts/check_repository.py
git diff --check
```

These checks cover repository integrity and catalog contracts, not writing quality or host activation. Keep local work history, credentials, and caches ignored; delete task-owned temporary files. See [SECURITY.md](SECURITY.md).

## Repository guide

| Path | Purpose |
| --- | --- |
| [AGENTS.md](AGENTS.md) | Shared agent instructions |
| [docs/PROJECT.md](docs/PROJECT.md) | Scope, delivery sequence, and acceptance criteria |
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | Content, selection, levels, and installation contracts |
| [docs/METHOD_AUTHORING.md](docs/METHOD_AUTHORING.md) | Sources, rights, rules, and evaluations |
| [docs/LOCALIZATION.md](docs/LOCALIZATION.md) | Language adaptation and README parity |
| [docs/COMPATIBILITY.md](docs/COMPATIBILITY.md) | Planned hosts and verification evidence |
| [docs/DECISIONS.md](docs/DECISIONS.md) | Confirmed choices and proposals |
| [docs/RELEASING.md](docs/RELEASING.md) | CI, versioning, and draft source releases |
| [docs/REFERENCE.md](docs/REFERENCE.md) | Project bibliography and reference notes |
| [docs/INITIAL_CATALOG_RESEARCH.md](docs/INITIAL_CATALOG_RESEARCH.md) | Original method research and comparable projects |
| [skills/](skills/), [docs/CATALOG_CONSOLIDATION.md](docs/CATALOG_CONSOLIDATION.md) | Experimental skills, overlap decisions, and migration |
| [templates/method/](templates/method/), [evals/](evals/) | Authoring and evaluation examples, not released methods or model results |
| [scripts/](scripts/), [tests/](tests/) | Foundation checker and tests |
| [.github/](.github/) | Collaboration and automation configuration |

## License and attribution

Original project content is [MIT licensed](LICENSE). Prefer existing MIT/Apache-2.0 implementations under the [reuse policy](THIRD_PARTY_NOTICES.md); third-party material keeps its own license and notices. No author or institution endorsement is implied.
