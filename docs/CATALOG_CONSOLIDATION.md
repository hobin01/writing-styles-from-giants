# Catalog consolidation

Reviewed on 2026-11-07 at the owner's request to remove overlapping writing/explanation skills and keep established representative methods. Current catalog: **21 methods plus one Korean companion**, with 117 rules and 77 synthetic cases. All remain experimental.

## Decision basis

Compare the implemented task, rules, exceptions, and cases. A shared goal such as accuracy is insufficient for deletion; methods remain separate when their audience, required result, or document contract differs. For substantially overlapping implementations, prefer an established named framework or maintained standard with explicit source support. This is a catalog judgment, not a measured popularity ranking or a claim that the original theories are identical.

| Removed skill | Retained representative | Concrete overlap and boundary |
| --- | --- | --- |
| `scqa` | [Minto Pyramid](../skills/minto-pyramid/SKILL.md) | Same business-document reader question and supported answer. SCQ/SCQA opening is now a conditional Minto operation, not a second discovery entry. Minto's public site identifies both Pyramid and SCQ; the four-part wording remains a project adaptation. |
| `caterpillar-technical-english` | [ASD-STE100](../skills/asd-ste100/SKILL.md) | This source-limited implementation supplied glossary consistency, referent disambiguation, and preserved technical relations, already covered by ASD-inspired rules. The maintained standard is the representative for controlled English; its official FAQ also identifies translation support. Historical CTE grammar/dictionaries are not absorbed or claimed equivalent. |
| `hemingway-writing` | [Orwell's six rules](../skills/orwell-six-rules/SKILL.md) | In this factual-writing adaptation, omission/revision reduced to removing unnecessary expression while retaining facts, conditions, and precision. Orwell's explicit six-rule framework covers this task. No claim is made that literary iceberg effects or the authors' full writing practices are interchangeable. |

Sources rechecked for this decision: Minto's public [concept](https://www.barbaraminto.com/concept) and [course](https://www.barbaraminto.com/course) pages, the [official ASD FAQ](https://www.asd-ste100.org/STE_faq.html) on terminology and translation, and Orwell's [essay including the qualified six rules](https://www.orwellfoundation.com/the-orwell-foundation/orwell/essays-and-other-works/politics-and-the-english-language/). These support method scope; they do not independently measure popularity. Exact read scope and rights remain in retained method metadata and [REFERENCE.md](REFERENCE.md).

## Distinctions retained

These groups cover every remaining skill. No new router, alias skill, selection setting, or method combination is introduced.

| Retained skills | Different task or observable result |
| --- | --- |
| ASD-STE100, Orwell, Minto | Controlled technical English; general nonfiction sentence editing; business argument hierarchy. Shared clarity rules do not make these tasks identical. |
| ELI5, Feynman, Boring Professor | Literal age-five audience; mechanism/gap/transfer checking; technical terminology and literal delivery without jokes/metaphors. Feynman has no mandatory child audience; Boring Professor need not test learning. |
| GTM, Aristotle, Socrates | Formal exposition/proof; categorical deduction validity; self-questioning of assumptions and support. A valid inference does not establish its premises, and questioning is not a proof. |
| Hunminjeongeum | Explain why a document is needed, then develop its answer and bounded conclusion. This system/educational purpose-first structure is not the business recommendation hierarchy or an original-research report. |
| Federal Plain Language, Microsoft | Public reader find/understand/act checks; technology/UI instructions with exact product labels and globally usable wording. |
| IMRaD, NIST | Original-study question/method/results/interpretation; broader technical reporting with measurement uncertainty and accessible evidence. |
| Amazon narrative, Google design doc, IETF RFC | Planning/decision narrative with a rendered page budget; software alternatives and trade-offs; precise implementation requirements and their normative force. |
| Diátaxis | Select documentation type by reader need; does not prescribe the selected topic's sentence style or scientific report structure. |
| Answer with HTML | Artifact delivery, interaction, accessibility, and calculation behavior. |
| Jobs presentation | Spoken/presentation sequence, audience benefit, and an honest demonstration or demo plan. |
| New Hart's Rules | Source-assisted edition-specific editorial decisions, rather than general clarity edits. |
| Korean companion | Korean referents, particles/endings, register, and modality. English grammar/dictionary rules do not replace it. |

Overlap does not establish a runtime collision: the skills already require explicit scope and prohibit automatic stacking. Competing audience or structure choices still need resolution if a user requests a combination; for example, a graduate proof cannot silently become an age-five lesson, and Minto's answer placement cannot silently replace a requested purpose-first opening or IMRaD structure. No host-selection or multi-method execution guarantee is made.

## Migration

The three removed directories are gone, without aliases or automatic substitution. Select the retained method explicitly. For SCQ/SCQA openings, select Minto `standard` or `strict` and request only the opening; `light` retains its question/grouping subset and does not enable `scq-opening`. Preserve an explicitly requested opening sequence.

| Retired rule IDs | Retained rule IDs |
| --- | --- |
| SCQA `shared-situation`, `real-complication` | Minto `scq-opening` |
| SCQA `decision-question`, `supported-answer` | Minto `reader-question`, `scq-opening`, `evidence-links` as applicable |
| CTE `controlled-terms` | ASD `consistent-terms` |
| CTE `resolve-ambiguity` | ASD `explicit-action` |
| CTE `retain-technical-relations` | ASD `technical-profile`, plus `preserve-meaning` |
| CTE `reusable-review` | ASD `dictionary-boundary` for unresolved glossary coverage; no CTE checker is implied |
| Hemingway `concrete-detail`, `informed-omission` | Orwell `necessary-words`, plus `sense-over-rule` for necessary information |
| Hemingway `supported-implication`, `revision-pass` | Meaning-preservation invariant and Orwell's exception rule; no new literary rule |

All nine synthetic cases were retained under these rule mappings, with `migratedFrom` recording their origin. SCQA case requests are separate from source data. The glossary-polysemy case now expressly leaves official ASD dictionary approval unverified; a project glossary cannot prove it. Shared invariants remain enabled at every level.

Minto content version is `0.2.0` for the new conditional opening rule. ASD and Orwell are `0.1.1` for clarified scope/regression cases; their existing rule IDs and level policies are unchanged. Other methods and locale rules are unchanged.

## Review and limits

Ponytail review kept one Minto opening rule and the existing ASD/Orwell rules, deleting the three duplicate entrypoints rather than creating a router or copies. Each changed skill retains its own complete evidence, locale record, and cases.

The [initial review](CATALOG_REVIEW.md) and [original run record](../evals/runs/2026-11-07-initial-catalog.json) remain historical evidence for the initial `0.1.0` profiles, including retired skills. They are not new execution results for the consolidated versions. No new model-quality, host-discovery, mixed-method execution, or native-reader evaluation was performed in this change. Repository/format validation is reported in the PR; all skills remain experimental.
