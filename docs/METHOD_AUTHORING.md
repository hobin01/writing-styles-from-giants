# Method authoring

Use [templates/method/](../templates/method/) for the authoring shape, not as a production method.

## From a giant to a method

Extract a documented practice from a thinker, book, company, or institution: reader benefit, applicable tasks, operational steps, and exceptions. It may address expression, argument structure, explanation, or document workflow. Reputation or brand voice alone does not establish a rule.

Open with what the method does, when to use it, and observable success criteria. Link source evidence and locale rules. Keep both README catalog entries linked to the real `SKILL.md` and update them with renames, availability, and behavior changes. Add a separate explanation page only when the summary is insufficient.

## Evidence and rights

For each method, record its author or responsible company/institution, source title, edition/date, URL, access date, and what was actually read. Distinguish original text, official educational explanation, publisher excerpt, and secondary summary. A search snippet or a catalog entry alone is not source verification.

Index consulted sources in the project-wide [REFERENCE.md](REFERENCE.md), linking the method's detailed evidence. Reuse an existing bibliography entry when several methods share a source; retain each method's source-to-rule mapping and read scope.

Label each rule `faithful-summary`, `adaptation`, or `project-original`. Preserve the source's exceptions. If only an excerpt was read, do not claim to reproduce the whole book. Do not present an adaptation as an official author, publisher, company, or institution skill or imply endorsement.

Write original operational questions; do not bundle books, dictionaries, proprietary checklists, long quotations, or images without rights. Follow [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md) for reuse and file-level license exceptions.

## Metadata contract

The metadata uses contract version 1. The repository checker validates catalog identities, required evidence fields, references, levels, locale coverage, and case categories. It accepts this repository’s portable two-field, single-line `name`/JSON-quoted `description` frontmatter subset; it is not a general YAML or Agent Skills validator. Source validity, rule quality, and model behavior require review.

| Field | Meaning |
| --- | --- |
| `schemaVersion`, `id`, `version`, `status` | Contract version; stable kebab-case ID matching SKILL frontmatter; semantic content version; draft/experimental/reviewed status |
| `languageScope` | `language-independent`, `en`, or `ko`; restrict language-specific rules within mixed profiles explicitly |
| `title`, `kind` | Display title; sentence, structure, document, explanation, or process |
| `applicability` | Suitable genres/audiences and material exclusions |
| `sources` | Stable source ID, title, URL, version/date, access date, evidence type, access scope, rights note |
| `rules` | Stable rule ID, intent, classification, provenance, source IDs, exceptions, check type, per-level behavior |

Rule classification is `invariant` or `guideline`. Check type is `deterministic`, `judgment`, or `human-review`. Each level maps to `off`, `advisory`, `warning`, or `error`. Invariants cannot be `off`; judgment-based guidelines cannot be declared mechanically verified. Rules without a legitimate external source must use `project-original` with an explanation, not a fabricated citation.

Write canonical instructions in English. Add a separate Korean skill only when linguistic differences require operational rules; do not clone a structural method merely to translate it. `languageScope: language-independent` means the reasoning/structure can serve a requested output language, not that every language has been reviewed. An English-only profile may describe a bounded structural adaptation while keeping grammar/dictionary checks inapplicable outside English.

Each locale file identifies `method`, `methodVersion`, `locale`, review status, reviewed source rules, and a rule-ID map. Localization text may explain an original intent without copying English syntax. If translation changes the rule's meaning, record it as an adaptation with its rationale.

## Review and evaluation

Submit source evidence, applicability, level differences, exceptions, locale status, and cases in the same PR. Rule IDs survive rewording. Retiring or changing a rule includes a migration note; do not silently reuse an ID for different behavior.

Every method stores `cases.json` inside its portable directory, with `type` set to `ordinary`, `exception`, or `meaning-preservation` and `sourceIds` linking its metadata evidence (empty for wholly project-original rules). Every method needs cases for an ordinary use, an important exception, and a meaning-preservation failure. Cases identify relevant rule IDs and observable expectations. Use synthetic or expressly redistributable text, never private client material. Preserve uncertainty, negation, scope, conditions, quantities, citations, and code.

The [example cases](../evals/cases.example.json) demonstrate expectations; they are not model run results. Apply Ponytail after completing each skill and record concrete pruning or retained boundaries in the catalog review. Keep deterministic checks separate from model-judged quality and human reader evaluation. Record the model/version, prompt, host, method version, locale, level, failures, and judging process for a real run. Do not optimize a numeric score by deleting necessary information.

Use an authored example to show a decision a reader might otherwise miss. Give enough source material to check the answer and explain one consequential choice. For a comparison of model outputs, use a fresh context and separate workspace per answer, the same held-out request and preselected checks. Only the treatment receives the method and level. Preserve both answers, ties, and failed attempts. Revise a skill after a failed check and repeat the request in a fresh context. See the [worked examples and trial records](../evals/runs/2026-11-08-worked-examples.md).

A method is `reviewed` only after provenance/rights review, rule review, and an evaluation record. This status is project review, not author endorsement, official certification, or proof of universal quality.
