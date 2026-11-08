# Copyediting a car-access statistic from the 2021 census

2026-11-08 · `new-harts-rules` 0.1.2 · English · Codex CLI 0.167.0 / gpt-6.1-sol

### Case and sources

- [Office for National Statistics, Housing, England and Wales: Census 2021 (5 January 2023)](https://www.ons.gov.uk/peoplepopulationandcommunity/housing/bulletins/housingenglandandwales/census2021). Section 6, Car or van availability, and title: 42.1% of London households versus 23.3% across England and Wales in 2021. Exhibition style and draft are original exercise inputs.

### Prompt

> Copyedit this original sentence for a UK transport exhibition label, followed by one short editorial note. Our exhibition house style spells out ‘per cent’ in prose. Preserve the ONS bulletin title verbatim. Draft: In ‘Housing, England and Wales: Census 2021’, the Office for National Statistics reported that 42.1% of London households had no car or van available in 2021, compared with 23.3% across England and Wales. No edition-specific passage from New Hart’s Rules has been supplied. Keep the finding at household level.

### Without a skill

> In ‘Housing, England and Wales: Census 2021’, the Office for National Statistics reported that 42.1 per cent of London households had no car or van available in 2021, compared with 23.3 per cent across England and Wales.
>
> Editorial note: ‘Per cent’ follows exhibition house style; the bulletin title and household-level finding are preserved.

### With the skill at standard

> In ‘Housing, England and Wales: Census 2021’, the Office for National Statistics reported that 42.1 per cent of London households had no car or van available in 2021, compared with 23.3 per cent across England and Wales.
>
> Editorial note: ‘Per cent’ follows exhibition house style; the bulletin title and household-level finding are preserved. No rule is attributed to New Hart’s Rules, second edition (2014), because no relevant passage was supplied.

### What changed

**Checks set before the run.** Apply the supplied exhibition convention to both percentages, preserve the exact title, household denominator, year and geographic comparison, and attribute the change to the house rather than to ONS or New Hart's Rules.

The edited sentence is identical in both runs. Each changes the two percent signs to the exhibition's house spelling and preserves the bulletin title and both household percentages. The skill adds a sentence explaining that there was no book passage to consult. It makes the source boundary explicit, but lengthens a note whose practical conclusion is the same.

**차이.** 두 답의 편집 문장은 같습니다. 42.1과 23.3을 해당 지역 가구의 비율로 유지하고 전시의 표기 지침을 따랐습니다. 스킬 답안의 편집 메모만 책의 해당 구절이 제공되지 않았다고 추가로 설명합니다.
