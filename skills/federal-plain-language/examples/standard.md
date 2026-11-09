# Which 40-minute document trip covers both identities?

[한국어](standard.ko.md)

2026-11-09 · `federal-plain-language` 0.1.22 · English · `gpt-6-luna`

### Case and sources

- [SSA, U.S. Citizen/Child — Replacement Social Security Card (October 2026)](https://www.ssa.gov/pubs/EN-05-10514.pdf). English page of the October 2026 U.S. citizen/child replacement-card leaflet, sections on the child's and parent's identity, current originals, issuer-certified copies and unacceptable copies. The family's options and collection times are hypothetical; the identification requirements come from the leaflet.

**Language scope.** This uses the method’s English public-information profile.

### Prompt

> A parent has 45 minutes to collect evidence for the identity part of a U.S.-citizen child's replacement Social Security card application. Write a parent-facing answer in English in no more than five sentences using the October 2026 SSA leaflet. Both people need identity evidence. The child can use a current U.S. passport or current state-issued non-driver ID. The parent can use a current U.S. passport or driver's license. SSA accepts originals or issuer-certified copies, not notarized photocopies; a birth certificate proves age or citizenship but not identity. Hypothetical collection times add: the child's original birth certificate is already in hand, original passport takes 40 minutes, and issuer-certified non-driver ID takes 15. For the parent, a notarized passport photocopy takes 5, an issuer-certified passport copy 25, and an original license 35. Which route fits? Point out why the tempting shortcut fails. Address identity evidence only.

### Without the skill

> Use the child’s issuer-certified state non-driver ID (15 minutes) and the parent’s issuer-certified U.S. passport copy (25 minutes): together they take 40 minutes. The tempting shortcut—a notarized photocopy of the parent’s passport—doesn’t count because SSA accepts originals or issuer-certified copies, not notarized photocopies. The child’s birth certificate proves age or citizenship, but not identity, so it cannot replace the child’s ID.

### With the skill at standard

> Use the child’s issuer-certified state non-driver ID (15 minutes) and the parent’s issuer-certified passport copy (25 minutes). Together they take 40 minutes, within the 45-minute limit. The notarized passport photocopy takes only 5 minutes, but SSA does not accept notarized photocopies as identity evidence. The birth certificate proves the child’s age or citizenship, not identity.

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Identifies the child's issuer-certified non-driver ID plus the parent's issuer-certified passport copy, totals 40 minutes and fits the 45-minute limit. | Met | Met |
| Explains both rejected shortcuts: the original birth certificate is insufficient for the child's identity and the notarized copy is insufficient for the parent's identity. | Met | Met |
| Gives the parent an actionable English identity-only answer in no more than five sentences without implying the full application is complete. | Met | Met |

**Review.** The parent gets a feasible 40-minute plan and a reason to reject each shortcut. The answer stays within five sentences and addresses identity evidence only.

Masked reviewer assignment: Y was the revised answer. The table retains the original control grades. [Previous pair and scores](https://github.com/hobin01/writing-styles-from-giants/blob/20f24c66c7e89e6ce1007249c83c33932998bf01/skills/federal-plain-language/examples/standard.md) · [All attempts and adjudications](https://github.com/hobin01/writing-styles-from-giants/blob/main/evals/runs/2026-11-09-standard/records/federal-plain-language.json).

<details>
<summary>Run record</summary>

Baseline generated 2026-11-08. Revised treatment generated independently on 2026-11-09 with Codex CLI 0.167.0, low reasoning, in a fresh read-only session. SHA-256 prefixes (entrypoint / original baseline / revised answer): `90ceac7f7264` / `cd08aed6cec9` / `68130696a7c4`.

</details>
