# Method authoring

Use [templates/method/](../templates/method/) as a documentation example. It intentionally lives outside `skills/` and contains no production-ready source-derived method.

## From a giant to a method

Sources may be a thinker's or historical figure's documented principles, a book's writing or explanation framework, or a company or institution's published communication practices. The project name describes learning from these sources; prominence alone does not establish a method's validity.

Identify the concrete practice an agent can apply: what it helps a reader do, which writing tasks it fits, the steps or questions to use, and when to make an exception. A method may address expression, argument structure, explanation, or document workflow. Keep its documented scope; do not infer a rule from a person's reputation or a brand's voice alone.

Open a released method with a short explanation of what it does, when to use it, and observable success criteria. Keep agent steps concise and link detailed source evidence and locale rules. Add a one-line catalog entry linked to the real `SKILL.md` in both READMEs; update those entries with renames, availability, and substantive behavior changes. A separate human-facing page is useful only when the method needs more explanation than its summary provides.

## Evidence and rights

For each method, record its author or responsible company/institution, source title, edition/date, URL, access date, and what was actually read. Distinguish original text, official educational explanation, publisher excerpt, and secondary summary. A search snippet or a catalog entry alone is not source verification.

Label each rule `faithful-summary`, `adaptation`, or `project-original`. Preserve the source's exceptions. If only an excerpt was read, do not claim to reproduce the whole book. Do not present an adaptation as an official author, publisher, company, or institution skill or imply endorsement.

Write original concise operational questions. Do not bundle books, standard dictionaries, proprietary checklists, long quotations, or images without the necessary rights. An MIT upstream implementation does not relicense its references. Record upstream code reuse and file-level exceptions in [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md).

## Metadata contract

The example JSON uses contract version 1. A future runtime validator must enforce it; the current checker only verifies example integrity, not a full production schema.

| Field | Meaning |
| --- | --- |
| `schemaVersion`, `id`, `version`, `status` | Contract version; stable kebab-case ID matching SKILL frontmatter; semantic content version; draft/experimental/reviewed status |
| `title`, `kind` | Display title; sentence, structure, document, explanation, or process |
| `applicability` | Suitable genres/audiences and material exclusions |
| `sources` | Stable source ID, title, URL, version/date, access date, evidence type, access scope, rights note |
| `rules` | Stable rule ID, intent, classification, provenance, source IDs, exceptions, check type, per-level behavior |

Rule classification is `invariant` or `guideline`. Check type is `deterministic`, `judgment`, or `human-review`. Each level maps to `off`, `advisory`, `warning`, or `error`. Invariants cannot be `off`; judgment-based guidelines cannot be declared mechanically verified. Rules without a legitimate external source must use `project-original` with an explanation, not a fabricated citation.

Each locale file identifies `method`, `methodVersion`, `locale`, review status, reviewed source rules, and a rule-ID map. Localization text may explain an original intent without copying English syntax. If translation changes the rule's meaning, record it as an adaptation with its rationale.

## Review and evaluation

Submit source evidence, applicability, level differences, exceptions, locale status, and cases in the same PR. Rule IDs survive rewording. Retiring or changing a rule includes a migration note; do not silently reuse an ID for different behavior.

Every method needs cases for an ordinary use, an important exception, and a meaning-preservation failure. Cases identify relevant rule IDs and observable expectations. Use synthetic or expressly redistributable text, never private client material. Preserve uncertainty, negation, scope, conditions, quantities, citations, and code.

The [example cases](../evals/cases.example.json) demonstrate expectations; they are not model run results. Keep deterministic checks separate from model-judged quality and human reader evaluation. Record the model/version, prompt, host, method version, locale, level, failures, and judging process for a real run. Do not optimize a numeric score by deleting necessary information.

A method is `reviewed` only after provenance/rights review, rule review, and an evaluation record. This status is project review, not author endorsement, official certification, or proof of universal quality.
