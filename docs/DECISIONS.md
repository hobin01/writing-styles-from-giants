# Decision log

The user's requirements are in [PROJECT.md](PROJECT.md).

## User-defined identity — 2026-11-06

- Project name: `writing-styles-from-giants`, replacing the temporary name Writing Methods.
- Purpose: let AI agents draw on documented writing and explanation methods from earlier thinkers, historical figures, influential books, and well-known companies and institutions. The name evokes standing on the shoulders of giants.
- Scope: extract attributable, actionable methods, including expression, structure, and explanation. Preserve the distinction between applying a method and impersonating its source.

The repository remote is `https://github.com/hobin01/writing-styles-from-giants.git`, configured during private preparation. The project name does not reserve an npm package name. Source categories do not constitute a reviewed method catalog.

## User-selected repository reference: 2026-11-06

Use [mattpocock/skills](https://github.com/mattpocock/skills) as a reference for repository management and README organization. The [reference review](REFERENCE.md) pins the inspected commit and separates observed upstream practices from our adaptations.

## User-defined development workflow: 2026-11-06

- The first stable release is `0.0.1`; development is solo before that milestone. `VERSION` remains `0.0.1-dev` until a release is prepared.
- Work on a separate short-lived branch from current `main`, commit validated changes promptly, and create or update the PR in the same task.
- While the repository is private, the owner permits agent self-merges after final-diff review and passing CI. GitHub author self-approval is unavailable; record an author review and self-merge instead. The full policy is in [CONTRIBUTING.md](../CONTRIBUTING.md).
- Revisit collaboration and independent-review requirements when preparing `0.0.1` or opening public contributions. Repository protections remain separate hosting settings.

## User-defined public-source policy

The repository is intended to become public open source. Prepare commit contents for that from the start, regardless of current visibility. Register retained private files in `.gitignore` before creating or using them. Delete task-owned temporary files after the task instead of adding ignore rules to retain them. [SECURITY.md](../SECURITY.md) owns the handling and cleanup details.

## Proposed implementation defaults

The following are assistant-proposed starter defaults, open to change before runtime implementation. Their presence in the skeleton is not evidence of user approval.

| Topic | Proposed default | Reason |
| --- | --- | --- |
| Original-content license | MIT | Permissive contribution and reuse; external content keeps its rights |
| Delivery | Portable method content; evaluate an existing installer first | A custom CLI or adapter needs evidence of an unmet requirement |
| Runtime | None required for the portable catalog; keep Python foundation checks | Choose another runtime only when actual product logic requires it |
| Method storage | Complete `skills/<id>/` directories | References travel with each skill |
| Initial catalog | Review one method first; Orwell, Federal Plain Language, and Minto-inspired structure are candidates | Prove one complete method before expanding the catalog or tooling |
| Levels | light / standard / strict | Observable rule coverage instead of a fictitious compliance percentage |
| Mode and scope | recommend, standard, project installation | Explicit opt-in to automatic application/global installation |
| Languages | en and ko; reviewed adaptations | No hardcoded cross-language word-count conversion |
| Releases | Reviewed tags produce draft GitHub source releases | Foundation can release source without pretending npm exists |

## Before public launch

- Confirm maintainer/reviewer ownership and public visibility before launch. Choose a package identity only if a project-owned package is needed; npm name availability is unverified.
- Confirm or change the proposed license before accepting external contributions under it.
- Configure a `main` ruleset requiring `foundation` CI, a review, resolved conversations, and blocked force pushes/deletion. Adjust maintainer bypass deliberately.
- Enable private vulnerability reporting and choose the conduct-report contact. Do not publish invented email addresses.
- Set an actual review owner before adding CODEOWNERS. The skeleton intentionally has no fake GitHub handle.
- Protect release tags and configure release authority. GitHub repository settings are not configured by these local files.
- Select the first method sources and locale reviewers; evaluate actual host versions before claiming support.

Product behavior, rule changes, locale measurement, or installer ownership changes need a short dated entry here or a focused design document. Routine implementation choices may be made by the builder with tests; do not turn every small change into an approval ritual.
