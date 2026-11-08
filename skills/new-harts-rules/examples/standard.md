# New Hart’s Rules source-assisted editing · House spelling and a protected citation

Run on 2026-11-08 • `new-harts-rules` 0.1.2 • English • Codex CLI 0.167.0

### Prompt

> Copyedit the sentence below, then add one short editorial note. House style requires 'on-site' before a noun in editable prose. Quoted titles must stay verbatim. No book passage is supplied for serial-comma style. Draft: Our onsite team read the article ‘The Onsite Team’ and checked labels, seals and lids.

### Without a skill

> Our on-site team read the article ‘The Onsite Team’ and checked labels, seals and lids.
>
> Editorial note: Changed “onsite” to “on-site” before a noun; preserved the quoted title and existing comma style.

### With the skill at standard

> Our on-site team read the article ‘The Onsite Team’ and checked labels, seals and lids.
>
> Editorial note: ‘On-site’ follows house style; the quoted title stays verbatim. Serial-comma usage is unchanged because no relevant passage from New Hart’s Rules, second edition (2014), was supplied.

### What changed

**Checks set before the run.** Change the editable modifier, preserve the exact quoted title and list facts. Attribute the spelling to house style and avoid claiming a book rule for the unresolved comma.

Both final edits change only the editable spelling and preserve the quoted title and list. The skill's note identifies house style and the absent book passage; the baseline explains what it changed without naming the authority. The earlier treatments and the corrected fixture are documented below.

**차이.** 두 최종 답안의 편집 문장은 같습니다. 스킬 답안은 사내 표기와 확인하지 못한 책의 규칙을 구분합니다. 수정 전 답안도 아래에 남겼습니다.

<details>
<summary>Earlier prompt, answers and revision</summary>

The earlier prompt said “two sentences” but supplied one. We corrected that mismatch before publishing the main pair above. The three earlier answers below used this same original prompt.

> Copyedit the two sentences below, then add one short editorial note. House style requires 'on-site' before a noun in editable prose. Quoted titles must stay verbatim. No book passage is supplied for serial-comma style. Draft: Our onsite team read the article ‘The Onsite Team’ and checked labels, seals and lids.

**Without a skill**

> Our on-site team read the article ‘The Onsite Team’ and checked labels, seals and lids.
>
> Editorial note: Changed “onsite” to “on-site” in prose; preserved the quoted title and existing serial-comma style because no book passage was supplied.

**First treatment, version 0.1.1**

> Our on-site team read the article ‘The Onsite Team’ and checked labels, seals and lids.
>
> Editorial note: Applied new-harts-rules v0.1.1 at standard level, referencing the second edition (2014). ‘On-site’ follows house style; the quoted title is unchanged. Serial-comma style remains unverified, so the existing punctuation is retained.

The note named the method version and described an edition as a reference without a relevant passage. We clarified the difference between an editorial note and a method audit, then reran the original prompt in a fresh context.

**Revised treatment, version 0.1.2**

> Our on-site team read the article ‘The Onsite Team’ and checked labels, seals and lids.
>
> Editorial note: Applied house style to ‘on-site’; preserved the quoted title verbatim. Left serial-comma style unchanged because no relevant passage from New Hart’s Rules, second edition (2014), was supplied.

</details>
