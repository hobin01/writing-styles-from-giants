# Which 40-minute document trip covers both identities?

2026-11-08 · `federal-plain-language` 0.1.1 at first pass · `gpt-6-luna` · Codex CLI 0.167.0

### Case and sources

- [SSA, U.S. Citizen/Child — Replacement Social Security Card (October 2026)](https://www.ssa.gov/pubs/EN-05-10514.pdf). English page of the October 2026 U.S. citizen/child replacement-card leaflet, sections on the child's and parent's identity, current originals, issuer-certified copies and unacceptable copies. The family's options and collection times are hypothetical; the identification requirements come from the leaflet.

**Reasoning task.** Find a feasible two-person document set under a time constraint, distinguishing the document’s purpose from who certified it.

### Prompt

> A parent has 45 minutes to collect evidence for the identity part of a U.S.-citizen child's replacement Social Security card application. Write a parent-facing answer under 100 words using the October 2026 SSA leaflet. Both people need identity evidence. The child can use a current U.S. passport or current state-issued non-driver ID. The parent can use a current U.S. passport or driver's license. SSA accepts originals or issuer-certified copies, not notarized photocopies; a birth certificate proves age or citizenship but not identity. Hypothetical collection times add: the child's original birth certificate is already in hand, original passport takes 40 minutes, and issuer-certified non-driver ID takes 15. For the parent, a notarized passport photocopy takes 5, an issuer-certified passport copy 25, and an original license 35. Which route fits? Point out why the tempting shortcut fails. Address identity evidence only.

### Without a skill

> The 15-minute route fits: get the child’s issuer-certified state non-driver ID and use the parent’s original driver’s license, which takes 35 minutes. Both are current identity evidence, and the total is 50 minutes—so that route misses the 45-minute limit. There is no listed combination that fits: the child’s fastest qualifying ID alone takes 15 minutes, and the parent’s fastest qualifying option is the 25-minute issuer-certified passport copy, totaling 40 minutes. The tempting 5-minute notarized passport photocopy fails because SSA does not accept notarized photocopies. The birth certificate proves age or citizenship, not identity.

### With the skill at standard

> Bring the child’s **issuer-certified state non-driver ID** (15 minutes) and your **issuer-certified U.S. passport copy** (25 minutes). Together, they take **40 minutes**, so they fit the 45-minute window.
>
> The tempting shortcut—using the child’s birth certificate and your notarized passport photocopy—fails: a birth certificate proves age or citizenship, not identity, and SSA does not accept notarized photocopies as identity evidence.
>
> *Method: federal-plain-language, standard.*

### First-pass assessment

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Identifies the child's issuer-certified non-driver ID plus the parent's issuer-certified passport copy, totals 40 minutes and fits the 45-minute limit. | Missed | Met |
| Explains both rejected shortcuts: the original birth certificate is insufficient for the child's identity and the notarized copy is insufficient for the parent's identity. | Met | Met |
| Gives the parent an actionable identity-only answer in at most 100 words without implying the full application is complete. | Missed | Missed |

The skill answer gives the feasible 15 + 25 = 40 minute trip first and correctly rejects both shortcuts, but appends an unsolicited method label to a parent-facing reply. The baseline also identifies the components and rejects the shortcuts, yet calls a 50-minute route feasible and then says no route fits even as it calculates 40 minutes. Its recommendation contradicts its own arithmetic.

**차이.** 스킬 답은 가능한 40분 경로를 먼저 제시하지만, 부모용 안내에 스킬 이름을 덧붙입니다. 미적용 답은 40분 조합을 계산해 놓고도 가능한 조합이 없다고 결론 내립니다. 두 답 모두 출생증명서와 공증 사본이 왜 부족한지는 설명합니다.

<details>
<summary>Developmental retest · version 0.1.2</summary>

Return public-facing text without an unsolicited method label. This retest is excluded from the first-pass counts.

The request and original baseline are unchanged.

**New standard answer**

> Use the child’s issuer-certified state non-driver ID and your original driver’s license. They take 15 + 35 = 50 minutes, so **no listed route fits 45 minutes**. The child’s original birth certificate is already in hand, but it proves age or citizenship—not identity.
>
> The fastest parent option is the notarized passport photocopy (5 minutes), but SSA does not accept notarized photocopies. The issuer-certified passport copy is accepted but takes 25 minutes; paired with the child’s non-driver ID, that route takes 40 minutes and fits.

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Identifies the child's issuer-certified non-driver ID plus the parent's issuer-certified passport copy, totals 40 minutes and fits the 45-minute limit. | Missed | Missed |
| Explains both rejected shortcuts: the original birth certificate is insufficient for the child's identity and the notarized copy is insufficient for the parent's identity. | Met | Met |
| Gives the parent an actionable identity-only answer in at most 100 words without implying the full application is complete. | Missed | Missed |

Both the skill answer and the baseline correctly reject the child’s birth certificate and the parent’s notarized photocopy and add 15 + 25 to get 40 minutes. The skill answer finally says the certified ID and certified passport copy fit, contradicting its opening recommendation and categorical claim that no route fits. The baseline likewise denies any feasible combination while giving its 40-minute total; it also calls the 15-plus-35-minute route a fit before rejecting it. Neither gives the parent a consistent decision.

**차이.** 스킬 답과 미적용 답 모두 자녀의 출생증명서와 부모의 공증 복사본을 배제하고 15분과 25분을 합해 40분을 얻는다. 스킬 답은 끝에서 발급기관 인증 신분증과 여권 사본이 시간 안에 가능하다고 쓰지만 처음에는 다른 조합을 권하고 가능한 경로가 없다고 단언한다. 미적용 답도 가능한 조합이 없다고 하면서 40분을 계산하고, 15분과 35분이 걸리는 경로도 처음에는 가능하다고 했다가 기각한다. 어느 쪽도 부모에게 일관된 선택을 제시하지 못한다.

</details>
