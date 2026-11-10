# Security and local files

The latest published patch is the supported version.

## Local-only files

| Content | Location |
| --- | --- |
| Local task history, session logs, and personal notes | `.local/history/`; editor history under `.history/` |
| Credentials and private configuration | `.local/credentials/` or `.credentials/`; existing secret-file patterns are in `.gitignore` |
| Reusable caches | `.cache/` and tool-specific cache paths in `.gitignore` |

Register local-only paths in `.gitignore` before creating or using them. A leading dot alone does not exclude a path from Git. Existing `private/` remains ignored. Read local-only content only when the task needs it; never copy it into public fixtures, logs, commits, or releases.

Public design decisions and release notes stay versioned. Local task transcripts and personal work history do not. Delete task-owned scratch scripts, comparison copies, debug dumps, and temporary exports when finished, including after failures. Prefer automatically cleaned system temporary directories; preserve other contributors' files.

Before committing, inspect staged content and confirm cleanup. Ignore rules do not remove tracked files or erase Git history; the repository checker rejects known private/generated paths, not every possible secret.

## Repository controls

GitHub enforces PR and status-check rules on `main`, `release` and `release/*`. Only repository administrators can merge to these branches or create `v*` tags. Version tags cannot be updated or deleted. Published releases are immutable. See the [active rulesets](https://github.com/hobin01/writing-styles-from-giants/rules).

PR workflows use read-only permissions. External Actions require a full commit SHA. GitHub runs CodeQL on Python and Actions, scans for supported secrets and blocks pushes that contain them. Dependabot alerts and security updates are enabled.

## Reporting

Report vulnerabilities privately through [GitHub security advisories](https://github.com/hobin01/writing-styles-from-giants/security/advisories/new). Keep credentials, private drafts, client inputs, and private source copies out of issues and PRs. Use synthetic examples.

If a secret was committed, stop distributing it, rotate or revoke it through its owner, and coordinate history/artifact cleanup.
