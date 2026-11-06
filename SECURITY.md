# Security and local files

Prepare every commit for public open-source release, regardless of current repository visibility.

## Local-only files

| Content | Location |
| --- | --- |
| Local task history, session logs, and personal notes | `.local/history/`; editor history under `.history/` |
| Credentials and private configuration | `.local/credentials/` or `.credentials/`; existing secret-file patterns are in `.gitignore` |
| Reusable caches | `.cache/` and tool-specific cache paths in `.gitignore` |

Register local-only paths in `.gitignore` before creating or using them. A leading dot alone does not exclude a path from Git. Existing `private/` remains ignored. Read local-only content only when the task needs it; never copy it into public fixtures, logs, commits, or releases.

Public design decisions and release notes stay versioned. Local task transcripts and personal work history do not. Delete task-owned scratch scripts, comparison copies, debug dumps, and temporary exports when finished, including after failures. Prefer automatically cleaned system temporary directories; preserve other contributors' files.

Before committing, inspect staged content and confirm cleanup. Ignore rules do not remove tracked files or erase Git history; the repository checker rejects known private/generated paths, not every possible secret.

## Reporting

Use GitHub private vulnerability reporting when available; otherwise ask the maintainer for a private channel. Keep credentials, private drafts, client inputs, and private source copies out of issues and PRs. Use synthetic examples.

If a secret was committed, stop distributing it, rotate or revoke it through its owner, and coordinate history/artifact cleanup. There are no production releases or configured reporting contacts yet.
