# Contributing

Read [AGENTS.md](AGENTS.md) and [PROJECT.md](docs/PROJECT.md). Development is solo before stable `0.0.1`; public collaboration is planned.

## Issues and PRs

- Small documentation fixes can go straight to a PR. Discuss new methods, locales, dependencies, public behavior, or adapters in an issue first. Use one reproducible problem per bug report and source evidence for proposals.
- Branch from current `main` using `feat/`, `fix/`, or `docs/`. Commit validated changes promptly, push, and open/update the PR in the same task under the owner's standing instruction.
- Keep one coherent change per PR. Use a Conventional Commit title and explain breaking changes. Preserve unrelated work and shared history; squash-merge after checks and review rather than pushing directly to protected `main`.
- Keep both READMEs aligned in structure, links, commands, and meaning. Record user-visible changes in CHANGELOG.md without artificial version bumps for wording corrections.
- Keep local history, credentials, and caches out of commits and remove task-owned temporary files under [SECURITY.md](SECURITY.md).
- Reuse existing implementations under [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). Original contributions use MIT; retain required upstream notices.

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

While private, the owner authorizes agent squash-merges after final-diff review and passing CI. Recheck visibility and the exact PR head; record author review, results, and self-merge basis. [GitHub prevents author self-approval](https://docs.github.com/en/pull-requests/how-tos/review-pull-requests/approving-a-pull-request-with-required-reviews), so do not claim independent approval. Report blocking protections instead of bypassing or changing them.

Revisit collaboration at `0.0.1` or public intake. One independent maintainer approval remains a proposed public-stage default. Source/rights review and competent language review are still required before a method or locale becomes `reviewed`.

## Community

Be respectful and specific; critique work rather than identity. Harassment, discrimination, retaliation, and private-data exposure are unacceptable. Ask the maintainer for a private channel for sensitive conduct or security reports. AI-assisted contributions meet the same rights, evidence, and review requirements. No CLA or DCO is configured.
