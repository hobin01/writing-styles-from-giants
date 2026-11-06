# writing-styles-from-giants

[한국어](README.ko.md)

AI-agent skills for writing and explanation methods from thinkers, historical figures, influential books, companies, and institutions.

The name evokes **standing on the shoulders of giants**: learning from earlier work to give agents concrete ways to organize, write, and explain ideas.

**Status:** documentation and authoring examples only; no installable skills yet. Foundation CI passes. Release and host-compatibility tests are pending.

## Why I started this project

I often asked AI to “be concise” or “summarize the key points” without making the requirements clear. The result differed from what I had in mind, or became “AI slop” I did not want to read.

This project turns documented writing methods and institutional guides into skills with clear sources and application criteria, so I can specify how ideas should be organized, explained, and emphasized.

## Methods

These candidates need source/rights review, rule authoring, and English/Korean review.

| Candidate | Intended use | Status |
| --- | --- | --- |
| Orwell-inspired plain prose | Clear sentences | Proposed; no skill yet |
| Federal Plain Language Guidelines | Reader-centered explanation | Proposed; no skill yet |
| Minto-inspired structure | Recommendations and arguments | Proposed; no skill yet |

See [source references](THIRD_PARTY_NOTICES.md) and the [project scope and next steps](docs/PROJECT.md).

## Installation

Installation instructions will follow a tested catalog. Evaluate the existing [skills CLI](https://github.com/vercel-labs/skills) against our [installation contract](docs/ARCHITECTURE.md) before building an installer.

## Planned behavior

- Respect explicit method selection, recommendation requests, opt-out, and the user's chosen application scope.
- Offer `light`, `standard`, and `strict` levels while preserving facts, numbers, units, negation, conditions, exceptions, uncertainty, quotations, citations, and code.
- Start with English and Korean, using language-specific rules and evaluations rather than fixed word-to-eojeol conversions.
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

These checks cover the repository foundation, not writing quality or host activation. Keep local work history, credentials, and caches ignored; delete task-owned temporary files. See [SECURITY.md](SECURITY.md).

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
| [templates/method/](templates/method/), [evals/](evals/) | Authoring and evaluation examples, not released methods or model results |
| [scripts/](scripts/), [tests/](tests/) | Foundation checker and tests |
| [.github/](.github/) | Collaboration and automation configuration |

## Project reference

The [mattpocock/skills](https://github.com/mattpocock/skills) repository informs our organization and contributor guidance. The [reference review](docs/REFERENCE.md) records the inspected structure and adaptations.

## License and attribution

Original project content is [MIT licensed](LICENSE). Prefer existing MIT/Apache-2.0 implementations under the [reuse policy](THIRD_PARTY_NOTICES.md); third-party material keeps its own license and notices. No author or institution endorsement is implied.
