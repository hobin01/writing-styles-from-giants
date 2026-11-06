# Contributing

Read [AGENTS.md](AGENTS.md) and [docs/PROJECT.md](docs/PROJECT.md). Small corrections can go straight to a PR. Open an issue first for a new method, locale, dependency, public behavior change, or host adapter so contributors do not duplicate work.

## Issues and scope

- Use the bug form for a reproducible problem, including a documentation or translation error. Put the smallest example and expected result before analysis; one problem per issue.
- Use the proposal form for a new method, language, or project change. Identify the writing task, source evidence, and review needs. New methods and public PRs remain part of this project's intended contribution model.
- The repository is private during preparation. The first stable release is planned as `0.0.1`; development is solo until that release. Public contribution and repository protections require separate hosting setup.

Acceptance follows [PROJECT.md](docs/PROJECT.md), with method evidence owned by [METHOD_AUTHORING.md](docs/METHOD_AUTHORING.md). The [repository reference](docs/REFERENCE.md) explains which upstream management practices we adapt.

## Branches and PRs

- Branch from current `main`: `feat/<topic>`, `fix/<topic>`, or `docs/<topic>`.
- Keep one coherent change per PR. Rebase or merge current `main` without rewriting another contributor's branch.
- Commit each coherent, validated change promptly, push the working branch, and open or update its PR in the same task. This is the owner's standing instruction; completed authorized work does not need a separate request to commit or create its PR.
- Use a Conventional Commit PR title: `feat:`, `fix:`, `docs:`, `test:`, `ci:`, or `chore:`. Explain breaking behavior explicitly.
- Squash merge after checks and review. Do not push directly to protected `main`, force-push it, or change released tags.
- PRs describe the concrete behavior, source/rights implications, tests actually run, and limitations. Do not post private drafts or real client inputs as examples.
- Update the changelog for user-visible behavior or delivered content. Documentation corrections that do not change behavior need no artificial version bump.
- Keep both READMEs aligned in section order, tables, links, commands, and meaning. The language switch link is intentionally different; locale-specific method rules need their own review rather than literal matching.

## Required evidence

| Change | Evidence |
| --- | --- |
| Method/rule | Source/version, read scope, rights note, rule IDs, exceptions, observable cases |
| Language | Adaptation rationale, counting definition if numeric, native-language review, locale-specific cases |
| Installer/adapter | Scope/conflict/idempotency/rollback/uninstall tests and supported host/version evidence |
| Router/levels | Explicit override, off mode, unsupported locale, rule conflict, and invariant-preservation cases |
| Workflow/release | Least permissions, immutable action pins, no secrets in PR jobs, tag/version/artifact checks |

Run:

```sh
python3 -m unittest discover -s tests -v
python3 scripts/check_repository.py
git diff --check
```

These are current foundation checks. Later runtime changes must add the appropriate commands and tests in the same PR; do not treat these checks as LLM behavior validation.

## Review and merging

While the repository is private, the owner authorizes the agent to review and squash-merge completed work after the final diff and required CI checks pass. Check current visibility and the exact PR head before merging. Record the author review, check results, and private-stage self-merge basis in the PR; this is not independent approval.

[GitHub does not allow a PR author to approve their own PR](https://docs.github.com/en/pull-requests/how-tos/review-pull-requests/approving-a-pull-request-with-required-reviews). Use the permitted self-merge path instead of claiming an approving review. If repository rules block it, report the blocker rather than bypassing protections or changing settings.

Review the collaboration policy when preparing `0.0.1` or opening the repository to contributors. One independent maintainer approval remains a proposed default for public collaboration, not a requirement for the current solo/private stage. Rights/source evidence and competent language review remain necessary before marking a method or locale `reviewed`.

## Community

Be respectful and specific. Critique the behavior or evidence, not a contributor's identity. Harassment, discrimination, private-data exposure, and retaliatory conduct are not acceptable. Ask a maintainer for a private channel if a conduct report contains sensitive information; do not post it publicly. The launch checklist includes establishing that channel.

Original contributions are offered under the repository's MIT license. Contributors must have the rights to submit their work and retain necessary third-party notices. AI-assisted work follows the same source, rights, review, and test requirements. No CLA or DCO is configured in this foundation; do not claim otherwise.
