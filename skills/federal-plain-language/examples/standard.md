# Which 40-minute document trip covers both identities?

[한국어](standard.ko.md)

2026-11-08 · `federal-plain-language` 0.1.2 · English · `gpt-6-luna`

### Case and sources

- [SSA, U.S. Citizen/Child — Replacement Social Security Card (October 2026)](https://www.ssa.gov/pubs/EN-05-10514.pdf). English page of the October 2026 U.S. citizen/child replacement-card leaflet, sections on the child's and parent's identity, current originals, issuer-certified copies and unacceptable copies. The family's options and collection times are hypothetical; the identification requirements come from the leaflet.

**Language scope.** This uses the method’s English public-information profile.

### Prompt

> A parent has 45 minutes to collect evidence for the identity part of a U.S.-citizen child's replacement Social Security card application. Write a parent-facing answer in English in no more than five sentences using the October 2026 SSA leaflet. Both people need identity evidence. The child can use a current U.S. passport or current state-issued non-driver ID. The parent can use a current U.S. passport or driver's license. SSA accepts originals or issuer-certified copies, not notarized photocopies; a birth certificate proves age or citizenship but not identity. Hypothetical collection times add: the child's original birth certificate is already in hand, original passport takes 40 minutes, and issuer-certified non-driver ID takes 15. For the parent, a notarized passport photocopy takes 5, an issuer-certified passport copy 25, and an original license 35. Which route fits? Point out why the tempting shortcut fails. Address identity evidence only.

### Without the skill

> Use the child’s issuer-certified state non-driver ID (15 minutes) and the parent’s issuer-certified U.S. passport copy (25 minutes): together they take 40 minutes. The tempting shortcut—a notarized photocopy of the parent’s passport—doesn’t count because SSA accepts originals or issuer-certified copies, not notarized photocopies. The child’s birth certificate proves age or citizenship, but not identity, so it cannot replace the child’s ID.

### With the skill at standard

> Both you and your child need identity evidence for the replacement card application. For your child, get an issuer-certified copy of a current state-issued non-driver ID; it takes 15 minutes, while the original passport takes 40. For yourself, use your original driver’s license; it takes 35 minutes, while an issuer-certified passport copy takes 25. The fastest valid route is the child’s certified ID and your certified passport copy, which takes 40 minutes total. The notarized passport photocopy is not accepted, and the birth certificate proves age or citizenship, not identity.

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Identifies the child's issuer-certified non-driver ID plus the parent's issuer-certified passport copy, totals 40 minutes and fits the 45-minute limit. | Met | Met |
| Explains both rejected shortcuts: the original birth certificate is insufficient for the child's identity and the notarized copy is insufficient for the parent's identity. | Met | Met |
| Gives the parent an actionable English identity-only answer in no more than five sentences without implying the full application is complete. | Met | Missed |

**Masked review** (X = baseline; Y = standard). Both identify the 15 + 25 = 40 minute combination and reject the birth certificate and notarized photocopy as identity shortcuts. X gives one consistent route. Y first tells the parent to use a 35-minute license, making that trip 50 minutes, then recommends the 25-minute passport copy instead.

<details>
<summary>Run record</summary>

Each arm was a separate ephemeral read-only Codex CLI 0.167.0 session with low reasoning effort. Neither session was given the other answer or an answer in the other language.

SHA-256 prefixes (entrypoint / baseline answer / standard answer): `5ba332f74f16` / `cd08aed6cec9` / `6dc26dbd3b6c`.

</details>
