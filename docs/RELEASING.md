# Branches, automation, and releases

Status: Foundation CI has passed on GitHub; the source-release workflow has not been run or verified. The repository is private during preparation. Branch/tag protection and public visibility are separate hosting settings.

## CI and repository settings

[Foundation CI](../.github/workflows/ci.yml) is configured for PRs and pushes to `main`, with read-only permissions and no model keys. It runs unit tests, the repository checker, and a whitespace check across the tracked source tree. Actions are pinned to commit SHAs; [Dependabot](../.github/dependabot.yml) is configured for monthly Actions updates. [The initial main-branch run](https://github.com/hobin01/writing-styles-from-giants/actions/runs/42237615689) passed on commit `6f1689d`, verified on 2026-11-06. This is repository-check evidence, not a source-release or host-compatibility test.

Use `main` and short-lived PR branches, with prompt commits and PR handling under [CONTRIBUTING.md](../CONTRIBUTING.md). Development is solo before `0.0.1`; private-stage self-merges follow that policy. Before public collaboration, configure the rules and review requirements in [DECISIONS.md](DECISIONS.md). Local YAML files do not enforce branch protection. Contributor CI must not use privileged `pull_request_target` execution.

## Version policy

`VERSION` records the source version. The first stable release is planned as `0.0.1`; the current `0.0.1-dev` is unreleased. Keep version changes and release notes in reviewed PRs. The current source-release workflow accepts exact stable `vMAJOR.MINOR.PATCH` tags, with no leading zeros; prerelease tags are unsupported.

Before 1.0, breaking changes and compatible additions increment minor; corrections increment patch. From 1.0, incompatible public behavior increments major. Substantive rule and locale changes are behavior changes, even if only Markdown/JSON changes.

When methods exist, keep their content versions in metadata and record the included versions in a source release. Manual VERSION/CHANGELOG updates are sufficient now; Changesets and npm publishing are not required to release repository content.

## Draft source release

The [source-release workflow](../.github/workflows/release.yml) is configured for `v*` tag pushes and creates a draft, never a published release. Verify its hosted behavior before the first public release.

1. Open a release PR with a stable `VERSION` and matching `## [<version>]` changelog section. Include delivered content, limitations, and migration notes; run foundation checks.
2. Merge after review. An authorized maintainer creates the matching tag on current `main`. The workflow requires the tagged commit to equal `origin/main` at checkout time; if `main` has advanced, follow a new reviewed release process rather than moving an existing tag.
3. The workflow reruns tests and tag/version/changelog checks, rejects private tracked paths, and creates a tracked-source `tar.gz` with a SHA-256 checksum.
4. It uses the GitHub token to create a draft release with the archive, checksum, and generated notes. Review the draft and archive before publishing it.
5. On failure, inspect the run and any existing draft before rerunning. The workflow does not replace existing assets. Published corrections use a new version.

The release job has `contents: write` for draft creation; PR CI is read-only. It publishes no npm package and uploads no working-directory snapshot. `git archive` includes tracked files only, so the public-path check and rights review remain necessary. The checker recognizes configured private-path patterns; it is not a general secret scanner.

## Future delivery changes

Test an existing installer before adding a project-owned package or native plugin. Keep installation evidence in [COMPATIBILITY.md](COMPATIBILITY.md). If a runtime package is later justified, decide its identity, package allowlist, publishing authority, and tests separately. Never infer publication permission from a local documentation or configuration change.

Rollback selects a known prior version and preserves user modifications. It does not rewrite a published tag, replace an immutable artifact, or delete a user's global skill directory.

## References

- [GitHub Actions secure use](https://docs.github.com/en/actions/reference/security/secure-use)
- [GitHub rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets)
- [Semantic Versioning](https://semver.org/)
- [Repository reference and adaptations](REFERENCE.md)
