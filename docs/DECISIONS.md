# Decisions

## Confirmed by the owner

- Name: `writing-styles-from-giants`, evoking learning from earlier thinkers, historical figures, books, companies, and institutions.
- License: MIT for original project content. Prefer vetted permissive reuse; preserve third-party licenses and notices under [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md). GPL/AGPL code is not accepted into the distributed project.
- First stable release: `0.0.1`; development is solo before it. Keep `VERSION` unreleased until release preparation.
- Workflow: branch from current `main`, commit validated work promptly, handle the PR, and delete completed local/remote branches in the same task. Private-stage self-merges and cleanup follow [CONTRIBUTING.md](../CONTRIBUTING.md).
- Publication: prepare every commit for eventual public release. Keep local task history, credentials, and caches ignored; delete task-owned temporary files. [SECURITY.md](../SECURITY.md) owns the paths and cleanup policy.
- References: maintain a project-wide bibliography in [REFERENCE.md](REFERENCE.md), with read scope, versions/dates, use, and links to skill-specific evidence and license records. Update it whenever external sources inform a change. Current remote: `https://github.com/hobin01/writing-styles-from-giants.git`.
- Initial catalog: investigate the owner's initial candidates and comparable projects before authoring; ask about undefined methods rather than inventing their behavior. The [initial research](INITIAL_CATALOG_RESEARCH.md) records evidence, clarified intent, and remaining source limits, with implementation evidence recorded separately in [CATALOG_REVIEW.md](CATALOG_REVIEW.md).
- Skill authoring: write instructions primarily in English. Add a separate Korean-specific skill only when Korean linguistic differences justify it; translated instructions alone do not justify a duplicate. This does not restrict the requested output language. Structural rules can be language-independent; English grammar is not Korean grammar.
- Method scope: ASD normal follows the named Karpathy post's informal 80% inspiration, excluding HTML/video; `normal` aliases `standard`; `strict` applies the full eligible project profile, without a conformance guarantee. Hunminjeongeum emphasizes purpose-first introduction/body/conclusion. John von Neumann is excluded at the owner’s request. The initial research selected CTE rather than CFE; its standalone adaptation was later retired in favor of ASD. Use NIST Technical Series Publications Author Instructions. See the [research](INITIAL_CATALOG_RESEARCH.md) for attribution boundaries.
- Review: apply Ponytail to every completed skill and remove unnecessary content while retaining source evidence, exceptions, and meaning-preservation checks.

## Implemented catalog

- 21 methods plus `korean-plain-language`, all experimental. Each portable method records its content version in `method.json`. The companion handles Korean referents, particles/endings, register, terminology and modality.
- The owner chose one checkout-scoped command with explicit selection, opt-in automatic matching, and bilingual help. Codex uses `$wsg`, `$wsg auto` and `$wsg docs`. The slash spellings are `/wsg`, `/wsg:auto` and `/wsg:docs`. Each writing invocation defaults to `standard`; documentation defaults to English. [Invocation contract](../commands/WSG.md)
- For personal testing across projects, the owner chose a Codex user-scope link to the adapter in the long-lived checkout. Future edits and post-merge updates to that checkout reach the same link. [Setup and verification](COMPATIBILITY.md#codex-user-scope)
- Publish English and Korean examples at `light`, `standard` and `strict`. Put the neutral case question and both answers on every level page. Use a substantive question at roughly high-school level or above and omit audience, style, method and format hints. For each method and language, ask `gpt-6-luna` the same question in four isolated sessions, once without the skill and once at each level. Reuse the no-skill answer across the three comparisons. [English gallery](../EXAMPLES.md) · [Korean gallery](../EXAMPLES.ko.md) · [Evaluation procedure](METHOD_AUTHORING.md)
- New Hart’s Rules is source-assisted: unverified edition-specific choices require relevant text, not invented prescriptions.

- Catalog cleanup: at the owner’s request, retain Minto instead of a standalone SCQA opening, ASD instead of the overlapping CTE-inspired implementation, and Orwell instead of the factual Hemingway adaptation. Preserve distinct tasks and all nine regression cases; see [comparison and migration](CATALOG_CONSOLIDATION.md).

## Proposed implementation defaults

These remain proposals, not implemented behavior or user-approved defaults.

| Topic | Proposal |
| --- | --- |
| Delivery | Complete portable method directories; evaluate an existing installer first |
| Runtime | Keep Python foundation checks; add product runtime code only for an observed unmet need |
| Further expansion | Add methods or language adaptations only with source evidence and cases |
| Output languages | Respect the owner's English-first authoring decision; language-specific rules still need reviewed adaptations and their own measurements |
| Installation | Project scope by default; global changes require selection |
| Releases | Reviewed tags create draft GitHub source releases |

## Before public launch

- Revisit collaboration and independent review when preparing `0.0.1` or accepting public contributions. Confirm maintainer and language-review ownership.
- Configure `foundation` CI, review requirements, protected `main`/tags, and deliberate maintainer bypass. Local files do not enforce hosting settings.
- Establish private vulnerability/conduct reporting and release authority.
- Verify method rights and the actual supported host/version/OS matrix. Choose a package identity only if a project-owned package is needed.

Record material changes here or in the document that owns the contract; keep local task logs out of public policy documents.
