# Decisions

## Confirmed by the owner

- Name: `writing-styles-from-giants`, evoking learning from earlier thinkers, historical figures, books, companies, and institutions.
- License: MIT for original project content. Prefer vetted permissive reuse; preserve third-party licenses and notices under [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md). GPL/AGPL code is not accepted into the distributed project.
- First stable release: `0.0.1`; development is solo before it. Keep `VERSION` unreleased until release preparation.
- Workflow: branch from current `main`, commit validated work promptly, handle the PR, and delete completed local/remote branches in the same task. Private-stage self-merges and cleanup follow [CONTRIBUTING.md](../CONTRIBUTING.md).
- Publication: prepare every commit for eventual public release. Keep local task history, credentials, and caches ignored; delete task-owned temporary files. [SECURITY.md](../SECURITY.md) owns the paths and cleanup policy.
- Repository references: keep documentation and project-management references in [REFERENCE.md](REFERENCE.md). Current remote: `https://github.com/hobin01/writing-styles-from-giants.git`.

## Proposed implementation defaults

These remain proposals, not implemented behavior or user-approved defaults.

| Topic | Proposal |
| --- | --- |
| Delivery | Complete portable method directories; evaluate an existing installer first |
| Runtime | Keep Python foundation checks; add product runtime code only for an observed unmet need |
| Initial catalog | Review one method first; Orwell, Federal Plain Language, and Minto-inspired structure are candidates |
| Selection | Recommendation mode, `standard` level, explicit automatic-application opt-in |
| Languages | English/Korean, each with reviewed adaptations and its own measurements |
| Installation | Project scope by default; global changes require selection |
| Releases | Reviewed tags create draft GitHub source releases |

## Before public launch

- Revisit collaboration and independent review when preparing `0.0.1` or accepting public contributions. Confirm maintainer and language-review ownership.
- Configure `foundation` CI, review requirements, protected `main`/tags, and deliberate maintainer bypass. Local files do not enforce hosting settings.
- Establish private vulnerability/conduct reporting and release authority.
- Verify method rights and the actual supported host/version/OS matrix. Choose a package identity only if a project-owned package is needed.

Record material changes here or in the document that owns the contract; keep local task logs out of public policy documents.
