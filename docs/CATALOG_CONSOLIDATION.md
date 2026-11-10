# Catalog consolidation

Reviewed on 2026-11-07 at the owner's request to remove overlapping writing/explanation skills and keep established representative methods. At consolidation the catalog had **21 methods plus one Korean companion**, with 117 rules and 77 synthetic cases. All remain experimental.

## Decision basis

Compare the implemented task, rules, exceptions, and cases. A shared goal such as accuracy is insufficient for deletion; methods remain separate when their audience, required result, or document contract differs. For substantially overlapping implementations, prefer an established named framework or maintained standard with explicit source support. This is a catalog judgment, not a measured popularity ranking or a claim that the original theories are identical.

| Removed skill | Retained representative | Concrete overlap and boundary |
| --- | --- | --- |
| `scqa` | [Minto Pyramid](../skills/minto-pyramid/SKILL.md) | Same business-document reader question and supported answer. SCQ/SCQA opening is now a conditional Minto operation, not a second discovery entry. Minto's public site identifies both Pyramid and SCQ; the four-part wording remains a project adaptation. |
| `caterpillar-technical-english` | [ASD-STE100](../skills/asd-ste100/SKILL.md) | This source-limited implementation supplied glossary consistency, referent disambiguation, and preserved technical relations, already covered by ASD-inspired rules. The maintained standard is the representative for controlled English; its official FAQ also identifies translation support. Historical CTE grammar/dictionaries are not absorbed or claimed equivalent. |
| `hemingway-writing` | [Orwell's six rules](../skills/orwell-six-rules/SKILL.md) | In this factual-writing adaptation, omission/revision reduced to removing unnecessary expression while retaining facts, conditions, and precision. Orwell's explicit six-rule framework covers this task. No claim is made that literary iceberg effects or the authors' full writing practices are interchangeable. |

Sources rechecked for this decision: Minto's public [concept](https://www.barbaraminto.com/concept) and [course](https://www.barbaraminto.com/course) pages, the [official ASD FAQ](https://www.asd-ste100.org/STE_faq.html) on terminology and translation, and Orwell's [essay including the qualified six rules](https://www.orwellfoundation.com/the-orwell-foundation/orwell/essays-and-other-works/politics-and-the-english-language/). These support method scope; they do not independently measure popularity. Exact read scope and rights remain in retained method metadata and [REFERENCE.md](REFERENCE.md).

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

The migration shipped as Minto method version `0.2.0` and ASD and Orwell method version `0.1.1`. Each current skill records its content version in `method.json`.
