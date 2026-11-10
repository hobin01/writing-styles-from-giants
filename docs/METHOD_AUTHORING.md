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

The [template cases](../templates/method/cases.json) demonstrate all three case types. Apply Ponytail after completing each skill and record concrete pruning or retained boundaries in the PR. Report repository checks, observed model behavior and human reader evaluations separately.

## Publish a gallery example

Choose a real system, study or public decision with enough information to reason about at roughly high-school level or above. Link the primary source and distinguish exercise inputs from observed data. Ask a substantive question in ordinary language. Leave the method, intended audience, document structure, stylistic rules and grading criteria out of the prompt. Preserve necessary source wording, technical terms and target language. For example, ask what happens to the water level when floating ice melts. The ELI5 skill supplies the audience.

Prepare matched English and Korean questions and decide what constitutes a correct answer before generation. For each language, give `gpt-6-luna` the identical question in four fresh, isolated sessions. One session receives only the question. Each of the other three receives the question, the selected level, the method instructions and required references. Keep other answers and the reviewer’s checks out of every session. Use the one no-skill answer as the common reference across all three levels.

With a signed-in Codex CLI, run `python3 scripts/run_writing_pair.py METHOD < prompt.txt` for the no-skill and standard answers. Run the same command with `--level light` and `--level strict` for the other two answers. Repeat using the question in the other language. Report an unavailable model or rejected tool-using session.

Read each output in its original language. Check calculations, decisions and factual conditions. Check the answers with the skill against its language scope and the rules active at that level. Exercise an interactive artifact in a browser. If a skill answer fails, fix the method and regenerate its six skill answers on the same questions. If a session answers in the wrong language, repeat the identical prompt. Preserve the no-skill answer as generated, including any factual mistakes. A change to a question requires fresh answers for that language. Keep the model’s wording intact. Use GitHub Markdown math delimiters for TeX outside code and preserve the expressions themselves.

Give each method’s `examples/README.md` a title, a short description of the skill and an explanation of its three levels. Link the English and Korean pages for each level. Each page contains the question title, full neutral question, sources, answer with the skill and answer without the skill. The two answers are the comparison. Keep judgments and run records out of the example pages. Run `python3 scripts/build_example_gallery.py` to rebuild both galleries.

A method is `reviewed` only after provenance/rights review, rule review, and an evaluation record. This status is project review, not author endorsement, official certification, or proof of universal quality.
