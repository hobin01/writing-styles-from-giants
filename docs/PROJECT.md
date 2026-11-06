# writing-styles-from-giants: project definition

Status: documentation foundation, 2026-11-06. User-defined direction and implementation proposals are distinguished below.

## Identity and purpose

The user-defined project name is `writing-styles-from-giants`. It evokes standing on the shoulders of giants: learning from earlier thinkers, historical figures, influential books, and well-known companies and institutions.

The project turns their documented writing and explanation methods into skills that AI agents can use. A method can guide sentence expression, argument structure, reader-oriented explanation, or a document-writing process. Recognition helps discover candidate sources; source evidence and evaluation determine what a skill may claim.

The user selected [mattpocock/skills](https://github.com/mattpocock/skills) as the repository-management reference. [REFERENCE.md](REFERENCE.md) records the inspected structure and our adaptations. The repository is currently private; public collaboration remains a goal.

The founder's motivation is recorded in the [README](../README.md): vague requests for concise summaries produced writing that missed the intended result or felt like AI slop. The project aims to make writing requirements concrete through documented methods.

## Development stage

The owner will work alone before the first stable `0.0.1` release. Use separate branches and handle commits and PRs promptly, including during solo development. While the repository is private, the agent may self-merge after final-diff review and passing CI under [CONTRIBUTING.md](../CONTRIBUTING.md). This is a user-defined workflow, separate from the product implementation proposals below.

## Product requirements

1. Make documented methods from thinkers, historical figures, books, companies, and institutions usable as AI-agent skills, with attribution.
2. Recommend a suitable method or apply one automatically within a selected scope; respect explicit choices and opt-out.
3. Vary guideline coverage and enforcement by level while preserving meaning at every level.
4. Target Codex, Claude Code, OpenCode, Antigravity, Pi, and Cline without tying portable content to one host.
5. Plan an `npx`-style installation experience with target selection, symlinks, and project/global scope. This does not require a project-owned npm package or installer.
6. Prepare for public GitHub contributions with documented PR, branch, CI, and release rules.
7. Start with English and Korean and expand with language-specific adaptations.
8. Separate public project content from private local material.

## Terms

| Term | Meaning |
| --- | --- |
| Source | The document or other evidence that establishes a writing practice |
| Method | Attributed operational rules derived from a source, with applicability and exceptions |
| Skill | A portable directory containing the agent instructions, method data, locale rules, and references |
| Locale | Language-specific rules and measurements, not just translated instructions |
| Level | `light`, `standard`, or `strict` guideline coverage/enforcement; invariants stay active |
| Recommendation / application | Suggesting a method / using its rules on text; neither follows merely from installation |

## Proposed delivery sequence

1. Author and evaluate one complete method with English/Korean variants. Orwell, Federal Plain Language, and Minto-inspired structure are candidates, not reviewed or shipped skills. Choose the first after source and rights review.
2. Demonstrate explicit method selection and level behavior in a host. Use a short skill workflow for recommendations before adding a scripted router or configuration loader.
3. Evaluate an existing skill installer against the installation contract. Record gaps before proposing a custom CLI or adapter. Publish only the host/OS combinations actually tested.
4. Expand the catalog and host coverage from evidence. All six hosts remain targets; Windows, native plugin wrappers, and post-edit hooks need their own tests before support claims.

This is an implementation proposal, not user approval of new defaults. The proposed starting mode is recommendation at `standard` level, with project-scoped installation. STE-inspired support is a later candidate and cannot imply verified ASD-STE100 compliance.

## Acceptance criteria

- Every released method has source/version, summary-vs-adaptation labels, rights notes, stable rule IDs, applicable tasks, exceptions, and locale review status.
- Recommendations explain fit and limitations. Explicit method selection wins; incompatibility is explained rather than silently substituting another method.
- Every level has observable cases. No level may discard a fact, alter its scope, or strengthen its certainty.
- A supported installation path preserves the whole skill directory, defaults to project scope, and exposes scope, conflicts, link/copy behavior, updates, and removal. Modified or unowned content is preserved.
- A detected path is not proof of activation. Report actual host/version/OS evidence and unsupported combinations.
- Model evaluations record model/version, prompt, method/locale/level, cases, failures, and unperformed checks. Repository tests do not prove writing quality.
- Public CI needs no model API keys or external account. Optional model evaluations run separately with bounded cost and sanitized inputs.

## Current foundation

Present: project and contributor documents, authoring examples, foundation-check scripts and unit tests, ignore rules, issue forms, a PR template, SHA-pinned CI/release workflow definitions, and Dependabot configuration.

Not implemented: production methods, recommendation/application workflow, runtime router, installer integration, custom CLI, native plugins, npm publishing, automatic hooks, and model evaluations. Foundation CI has passed on GitHub; see [RELEASING.md](RELEASING.md) for the evidence. Release workflow execution, repository protection settings, and runtime host compatibility have not been verified.

## Boundaries

Keep the first deliverable focused on an actual writing method. A dedicated runtime, custom installer, host adapter framework, or plugin marketplace is justified only by an observed requirement existing tools cannot satisfy.

No dashboard, paid service, remote content upload, model hosting, arbitrary plugin execution, person impersonation, authorship detector, or certified-STE claim is planned. Source books, dictionaries, and proprietary checklists keep their own rights and must not be bundled without permission.
