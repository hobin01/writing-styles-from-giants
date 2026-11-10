# Contributing

Read [AGENTS.md](AGENTS.md) and [PROJECT.md](docs/PROJECT.md). External contributors can submit PRs from forks.

## Issues and PRs

- Small documentation fixes can go straight to a PR. Discuss new methods, locales, dependencies, public behavior, or adapters in an issue first. Use one reproducible problem per bug report and source evidence for proposals.
- Branch from current `main` using `feat/`, `fix/`, or `docs/`. Commit validated changes promptly, push, and open/update the PR in the same task under the owner's standing instruction.
- Keep one coherent change per PR. Use a Conventional Commit title and explain breaking changes. Preserve unrelated work and shared history; squash-merge after checks and review rather than pushing directly to protected `main`.
- After merging, update local `main`, delete the completed branch locally and remotely, and prune stale remote-tracking refs. Automatic head-branch deletion is enabled on GitHub; verify it happened. For squash merges, verify the branch head matches the merged PR and has no later work before deleting it. Keep branches with open PRs or unmerged work.
- When working in a separate worktree, fast-forward the clean, long-lived checkout on `main` after the merge so a global WSG link sees the update. If that checkout has local edits or divergent history, preserve them and report the pending update.
- Keep both READMEs aligned in structure, links, commands, and meaning. Record user-visible changes in CHANGELOG.md without artificial version bumps for wording corrections.
- Keep local history, credentials, and caches out of commits and remove task-owned temporary files under [SECURITY.md](SECURITY.md).
- Reuse existing implementations under [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). Original contributions use MIT; retain required upstream notices.
- Add or update consulted projects, sites, papers, books, and guides in [docs/REFERENCE.md](docs/REFERENCE.md) in the same PR, linking detailed method evidence and rights records.

## Validation

```sh
python3 -m unittest discover -s tests -v
python3 scripts/check_repository.py
git diff --check
```

| Change | Required evidence |
| --- | --- |
| Method/rule | Sources/version, read scope, rights, stable rules, exceptions, observable cases |
| Language | Adaptation rationale, measurements if numeric, competent review, locale cases |
| Installer/adapter | Scope, conflicts, idempotency, recovery, removal, host/version/OS tests |
| Selection/levels | Overrides, opt-out, unavailable locale, conflicts, meaning preservation |
| Workflow/release | Least permissions, SHA pins, no secrets in PR jobs, tag/version/archive checks |

Report checks actually run and limitations. Repository tests do not establish writing quality or host activation; new runtime logic needs behavioral tests.

## Review and merge

A repository administrator reviews the final diff and squash-merges through a PR. GitHub requires the up-to-date `foundation` check and resolution of review conversations on `main`, `release`, and `release/*`. The sole maintainer can merge their own PR after the same checks. The separate maintainer-only update rule requires the administrator merge option on a PR. The CI/PR ruleset has no bypass actors. Confirm the PR head and passing checks before merging, and record any independent review received.

Method and locale promotion to `reviewed` still requires source/rights review and competent language review.

## Community

Be respectful and specific; critique work rather than identity. Harassment, discrimination, retaliation, and private-data exposure are unacceptable. Ask the maintainer for a private channel for sensitive conduct or security reports. AI-assisted contributions meet the same rights, evidence, and review requirements. No CLA or DCO is configured.
