# CI and releases

The [Foundation workflow](../.github/workflows/ci.yml) validates pull requests and the protected branches. It runs the unit tests, repository and whitespace checks, builds a wheel, installs it and compares the installed catalog with the checkout. PR jobs use a read-only token. Actions are pinned to commit SHAs and [Dependabot](../.github/dependabot.yml) checks for updates.

## Publish a version

1. Update [VERSION](../VERSION), [CHANGELOG.md](../CHANGELOG.md) and both README installation URLs in a PR. The wheel takes its version from `VERSION`; each method records its own content version in `method.json`. Describe behavior changes, migration steps and known limitations.
2. Run the [contributor checks](../CONTRIBUTING.md#validation) and `python3 scripts/check_repository.py --tag vX.Y.Z`. Review the final diff and squash-merge after CI passes.
3. A repository administrator tags the merged `main` commit and pushes the new stable `vMAJOR.MINOR.PATCH` tag. The [release workflow](../.github/workflows/release.yml) checks the tag against `VERSION`, the changelog and the current tip of `main`. Let it finish before merging the next release.
4. Inspect the draft on GitHub. Download the source archive, wheel, offline ZIP and `SHA256SUMS` together. Run `sha256sum -c SHA256SUMS` (or `shasum -a 256 -c SHA256SUMS` on macOS). Test the wheel in a clean uv tool environment, check its methods and rights notices, and verify the release notes refer to the correct tag. Extract the offline ZIP, run its `install.py` from a separate project with Python, and compare the installed catalog with the wheel.
5. Publish the draft. Verify the public asset URL with the README install command. GitHub locks published assets and tags. Ship corrections in a new patch release.

The wheel has no runtime dependencies and is distributed through GitHub Releases. The source archive contains the tracked files at the tag. CI and releases do not need model credentials.

The release workflow builds the offline ZIP from the wheel package and includes the [offline instructions](OFFLINE.md). Both forms run the same installer.
