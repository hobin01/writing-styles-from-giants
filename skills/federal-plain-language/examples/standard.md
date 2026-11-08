# Which documents identify a child to Social Security?

2026-11-08 · `federal-plain-language` 0.1.1 · English · Codex CLI 0.167.0 / gpt-6.1-sol

### Case and sources

- [SSA, U.S. Citizen/Child — Replacement Social Security Card (October 2026)](https://www.ssa.gov/pubs/EN-05-10514.pdf). English page of the October 2026 U.S. citizen/child replacement-card leaflet, sections on the child's and parent's identity, current originals, issuer-certified copies and unacceptable copies. The family’s two documents are an illustrative scenario.

### Prompt

> Write an answer for a parent reading the October 2026 U.S. Social Security Administration leaflet about replacing a U.S.-citizen child's Social Security card. The parent has only the child's birth certificate and a notarized photocopy of the parent's identification. Explain whether those establish identity and what forms of evidence the leaflet accepts. It requires evidence of both people's identities. A birth certificate can establish age or citizenship but not the child's identity; a child's U.S. passport is an example of identity evidence. A parent's U.S. driver's license is another example for the parent. Documents must be current originals or copies certified by the issuer; ordinary photocopies and notarized copies aren't accepted. Limit the answer to the evidence question, in 85 words or fewer.

### Without a skill

> No. The birth certificate can establish your child’s age or U.S. citizenship, but it does not establish the child’s identity. The notarized photocopy of your identification is not accepted.
>
> The leaflet requires identity evidence for both you and your child. Examples include your child’s U.S. passport and your U.S. driver’s license. Documents must be current originals or copies certified by the issuing agency. Ordinary photocopies and notarized copies are not accepted.

### With the skill at standard

> No. The child’s birth certificate can establish age or citizenship, but it does not establish the child’s identity. The notarized photocopy of your identification is not accepted.
>
> The leaflet requires evidence of both your child’s identity and your identity. Examples include a U.S. passport for your child and a U.S. driver’s license for you.
>
> Documents must be current originals or copies certified by the issuer. Ordinary photocopies and notarized copies are not accepted.

### What changed

**Checks set before the run.** Keep the October 2026 leaflet as the source, distinguish the child's identity from age or citizenship, require evidence for both people and distinguish issuer-certified copies from merely notarized copies. Do not imply the examples are the only acceptable documents.

Both answers reject the two documents for the identity check, distinguish the child's identity from age or citizenship, and give an acceptable example for each person. The skill gives the document-format rule its own paragraph. This is a difference in layout; the underlying evidence rule is the same.

**차이.** 두 답 모두 부모와 자녀에게 어떤 신원 증빙이 필요한지 정확히 설명합니다. 스킬 답은 원본·발급기관 인증 사본 요건을 별도 문단으로 나눴고, 인정되는 서류에 관한 결론은 같습니다.

<details>
<summary>Earlier attempts on this case</summary>

The first prompt named a July 2024 leaflet. The current SSA publication identifies itself as the October 2026 edition and says the July 2024 edition may still be used. We dated the question to the edition that the source link actually serves and ran a new matched pair.

**Attempt 1 — request**

> Write an answer for a parent reading the July 2024 U.S. Social Security Administration leaflet about replacing a U.S.-citizen child's Social Security card. The parent has only the child's birth certificate and a notarized photocopy of the parent's identification. Explain whether those establish identity and what forms of evidence the leaflet accepts. It requires evidence of both people's identities. A birth certificate can establish age or citizenship but not the child's identity; a child's U.S. passport is an example of identity evidence. A parent's U.S. driver's license is another example for the parent. Documents must be current originals or copies certified by the issuer; ordinary photocopies and notarized copies aren't accepted. Limit the answer to the evidence question, in 85 words or fewer.

**Without a skill**

> No. The birth certificate can establish your child’s age or U.S. citizenship, but it does not establish identity. Your notarized identification photocopy is also unacceptable.
>
> The leaflet requires evidence of both your child’s identity and your identity. Examples include a U.S. passport for your child and a U.S. driver’s license for you. Documents must be current originals or copies certified by the issuing agency. Ordinary photocopies and notarized copies are not accepted.

**With the skill at standard**

> No. Those documents do not establish both identities, as the leaflet requires. Your child’s birth certificate can establish age or citizenship, but it does not establish identity. The notarized photocopy of your identification is not accepted.
>
> Examples of accepted identity evidence include your child’s U.S. passport and your U.S. driver’s license. Documents must be current originals or copies certified by the agency that issued them. Ordinary photocopies and notarized copies are not accepted.

</details>
