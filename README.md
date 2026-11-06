# writing-styles-from-giants

[한국어](README.ko.md)

Writing and explanation methods from thinkers, historical figures, influential books, and well-known companies and institutions, made usable as skills for AI agents.

The name evokes **standing on the shoulders of giants**: drawing on the knowledge and practices of those who came before us. Here, style includes sentence expression, argument structure, explanation, and document-writing practices. The goal is **documented source → attributed method → agent skill → task-specific application**.

**Status: foundation only.** Project documents, authoring examples, local checks, and CI/release workflow definitions exist. There are no installable method skills, recommendation workflow, or project installer yet. Hosted workflow execution and host compatibility have not been verified.

## Methods

The initial candidates below are proposals, pending source/rights review, rule authoring, and English/Korean review. A famous name alone is not evidence for a rule.

| Candidate | Intended use | Status |
| --- | --- | --- |
| Orwell-inspired plain prose | Clear sentence expression | Proposed; no skill yet |
| Federal Plain Language Guidelines | Reader-centered explanation | Proposed; no skill yet |
| Minto-inspired structure | Organizing recommendations and arguments | Proposed; no skill yet |

See [source references](THIRD_PARTY_NOTICES.md) and the [project brief](docs/PROJECT.md). Once a method is ready, its catalog entry will link to its actual `SKILL.md` and state its locale and review status. The examples under `templates/` and `evals/` are authoring aids, not released methods or model evaluation results.

## Installation

There is no installation command yet because the production catalog does not exist. An npm package for this project is not required to distribute repository-based skills through an existing installer.

The proposed first delivery evaluates an existing skill installer before building a custom CLI. Publish instructions only after verifying complete-directory installation, project scope, conflicts, updates, and removal. See the [installation contract](docs/ARCHITECTURE.md).

## Planned behavior

- Select a named method explicitly, request a recommendation, or opt out. Automatic application stays within the user's selected scope.
- Offer `light`, `standard`, and `strict` levels. Every level preserves facts, numbers, units, negation, conditions, exceptions, uncertainty, quotations, citations, and code.
- Start with English and Korean. Adapt rules and evaluations to each language; do not convert English word limits into fixed Korean eojeol limits.
- Keep portable content independent of host tools and permissions. Codex, Claude Code, OpenCode, Antigravity, Pi, and Cline are planned targets, not verified integrations.
- Apply documented methods with attribution. Author impersonation, AI-authorship detection, and official compliance certification are outside the scope.

## Contributing

Start with [CONTRIBUTING.md](CONTRIBUTING.md). Keep each issue or PR focused on one problem; method and language changes need source evidence and examples. English contributor documents are canonical; keep this README and the Korean README aligned in section order, tables, commands, and meaning.

Use Python 3.12 or newer for the dependency-free repository checks, from the repository root:

```sh
python3 -m unittest discover -s tests -v
python3 scripts/check_repository.py
git diff --check
```

These check the repository foundation, not LLM writing quality, source rights, or host activation. Keep private drafts in ignored `private/` or `.local/` directories. Ignore rules do not make already tracked files private.

## Repository guide

| Path | Purpose |
| --- | --- |
| [AGENTS.md](AGENTS.md) | Shared agent instructions; CLAUDE.md points here |
| [docs/PROJECT.md](docs/PROJECT.md) | Purpose, scope, milestones, and acceptance criteria |
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | Proposed content, selection, levels, configuration, and installation contracts |
| [docs/METHOD_AUTHORING.md](docs/METHOD_AUTHORING.md) | Source review, rights, rules, and evaluation requirements |
| [docs/LOCALIZATION.md](docs/LOCALIZATION.md) | Language adaptation, measurement, and README parity |
| [docs/COMPATIBILITY.md](docs/COMPATIBILITY.md) | Planned hosts and required verification evidence |
| [docs/DECISIONS.md](docs/DECISIONS.md) | User-defined direction, proposed defaults, and open decisions |
| [MVP plan](docs/superpowers/plans/2026-11-06-mvp.md) | Future implementation sequence |
| [docs/RELEASING.md](docs/RELEASING.md) | CI, versioning, and draft source releases |
| [templates/method/](templates/method/) | Original method-authoring examples |
| [evals/](evals/) | Example evaluation cases; no model runs yet |
| [scripts/](scripts/), [tests/](tests/) | Local foundation checker and unit tests |
| [.github/](.github/) | Issue forms, PR template, CI, release workflow, and dependency-update configuration |

Future production methods belong in `skills/<method-id>/`, retaining the entire skill directory and its references. That catalog has not been created yet.

## Project reference

Repository organization and contributor documentation take inspiration from [mattpocock/skills](https://github.com/mattpocock/skills). The [reference review](docs/REFERENCE.md) records the inspected commit, adopted patterns, and differences. This is a structural reference, not a writing-method source or an affiliation.

## License and attribution

Original project code and documentation are MIT licensed; see [LICENSE](LICENSE). References, standards, books, quotations, trademarks, and upstream implementations keep their own rights. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). No author, company, or institution endorsement is implied.
