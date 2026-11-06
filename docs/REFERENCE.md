# Repository reference

The user selected [mattpocock/skills](https://github.com/mattpocock/skills) as a reference for project management and README organization. Reviewed on 2026-11-06 at commit [`4ae2317`](https://github.com/mattpocock/skills/tree/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d). This is a structural reference, not a writing-method source or a dependency.

## Observed structure

| Upstream area | Role at the reviewed commit |
| --- | --- |
| [README.md](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/README.md) | Purpose, installation, practical problems, and linked skill index |
| [skills/](https://github.com/mattpocock/skills/tree/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills) | Separate skill directories, grouped into engineering, productivity, misc, in-progress, and deprecated buckets |
| [CLAUDE.md](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/CLAUDE.md) | Contributor instructions; upstream AGENTS.md is a symlink to this file |
| [docs/](https://github.com/mattpocock/skills/tree/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/docs) | Human-facing skill explanations, separate from agent instructions |
| [CONTRIBUTING.md](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/CONTRIBUTING.md), [SCOPE.md](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/SCOPE.md) | Request routing, concise reproducible issues, and explicit acceptance boundaries |
| [.github/](https://github.com/mattpocock/skills/tree/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/.github), [.changeset/](https://github.com/mattpocock/skills/tree/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/.changeset) | Issue forms and automated version PRs/tags |
| [.claude-plugin/](https://github.com/mattpocock/skills/tree/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/.claude-plugin) | Plugin packaging for the promoted skill set |

Its README offers existing installation tools. Its [package.json](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/package.json) is private and supplies version-management scripts, not a public installer package. Its [link script](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/scripts/link-skills.sh) is explicitly a maintainer-only tool, not a supported installer.

## Adaptation for this project

- Put purpose, method candidates, installation status, and contributor entry points in both READMEs, in the same order.
- Keep each future method in one complete directory. Start with a flat catalog; add categories only when real methods make them useful.
- Give each released method a linked summary of what it does, when to use it, and observable success criteria. Keep detailed agent steps and source evidence with the method instead of duplicating them in the README.
- Keep shared agent policy in AGENTS.md and CLAUDE.md as a plain-file pointer. Retain this project's existing design documents as the owners of detailed contracts.
- Use focused issue forms, a PR template, read-only foundation CI, and a draft source-release workflow. Keep the current dependency-free checks and manual version/changelog policy.
- Evaluate an existing skill installer before proposing a custom CLI. Record unmet requirements and host tests before adding adapters or plugin packaging.

The source's collaborator-only PR policy and closed new-skill intake do not fit this project's planned open contributions. Its bucket layout, Changesets dependency, plugin manifests, automated issue triage, and maintainer global-link script are not needed in this foundation. In particular, its link script can replace existing global directories; our installation contract requires preserving unowned or modified files.

These are project adaptations. No upstream skill, script, policy text, or branding has been copied into the product, and no affiliation is implied. See [DECISIONS.md](DECISIONS.md) for proposal status and [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md) for attribution.
