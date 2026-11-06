# CI and releases

Foundation CI is verified; the source-release workflow is not. Branch/tag protection and visibility remain hosting settings, not guarantees of local configuration.

## CI

[Foundation CI](../.github/workflows/ci.yml) runs tests, repository checks, and tracked-source whitespace checks on PRs and `main`, with read-only permissions and no model keys. Actions use SHA pins; [Dependabot](../.github/dependabot.yml) proposes monthly updates. [The first main run](https://github.com/hobin01/writing-styles-from-giants/actions/runs/42237615689) passed on `6f1689d`.

Use the branch/PR policy in [CONTRIBUTING.md](../CONTRIBUTING.md). Configure public-stage protections from [DECISIONS.md](DECISIONS.md); do not run contributor code through privileged `pull_request_target` jobs.

## Versions

The first stable release is `0.0.1`; [VERSION](../VERSION) remains unreleased until preparation. Keep version and changelog changes in a PR. Before 1.0, breaking changes and additions increment minor, corrections patch; from 1.0, incompatible public changes increment major. Rule/locale changes can be behavior changes even when only Markdown/JSON changes.

Method metadata carries its own content version. Record included method versions in release notes. Manual VERSION/CHANGELOG updates suffice; a runtime package or Changesets is not required.

## Draft source release

The [workflow](../.github/workflows/release.yml) accepts stable `vMAJOR.MINOR.PATCH` tags without leading zeros; prerelease tags are unsupported. Verify its hosted behavior before the first public release.

1. Prepare a stable VERSION and matching `## [<version>]` changelog section in a reviewed PR, including limitations and migration notes. Run foundation and applicable method/host checks.
2. Tag current `main` through an authorized maintainer. The workflow requires the tagged commit to equal `origin/main` at checkout; never move an existing release tag to work around a mismatch.
3. The job reruns tests, tag/version/changelog and public-path checks, then creates a tracked-source `tar.gz` and SHA-256 checksum. Include required upstream licenses/notices under [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md).
4. GitHub creates a draft with the archive, checksum, and generated notes. Inspect them before publication. The job has `contents: write`; PR CI remains read-only. No npm package is published.
5. Inspect failed runs and existing drafts before retrying. Existing assets are not silently replaced; published corrections use a new version.

`git archive` includes tracked files only, so review still matters: path checks are not a general secret scanner. Rollback selects a prior version while preserving user modifications, rather than rewriting tags or deleting user skill roots. A local change does not authorize release publication or hosting-setting changes.
