# Correcting a percentage-point claim for a UK census exhibit

2026-11-08 · `new-harts-rules` 0.1.2 at first pass · `gpt-6-luna` · Codex CLI 0.167.0

### Case and sources

- [Office for National Statistics, Housing, England and Wales: Census 2021 (5 January 2023)](https://www.ons.gov.uk/peoplepopulationandcommunity/housing/bulletins/housingenglandandwales/census2021). Section 6, Car or van availability, and title: 42.1% of London households versus 23.3% across England and Wales in 2021. Exhibition style and draft are original exercise inputs.

**Reasoning task.** Correct the denominator and distinguish an absolute percentage-point difference from a relative percentage change, while protecting quoted material and the source of editorial choices.

### Prompt

> Copyedit this UK exhibition label and append one short editorial note. Original draft: ‘In “Housing, England and Wales: Census 2021”, ONS showed that 42.1% of Londoners lacked a car in 2021, 18.8 per cent more than across England and Wales.’ The bulletin reports households with no car or van available: 42.1% in London and 23.3% across England and Wales. The editor needs both the percentage-point gap and the relative excess over the England-and-Wales share (round that excess to the nearest whole per cent). House style spells out ‘per cent’ in prose; keep the ONS title verbatim. No passage from New Hart's Rules was supplied. Keep the edited sentence intelligible to a visitor who might otherwise confuse the two comparisons.

### Without a skill

> In “Housing, England and Wales: Census 2021”, ONS reported that 42.1% of London households had no car or van available, compared with 23.3% across England and Wales—a gap of 18.8 percentage points. London’s share was 81 per cent higher than the England-and-Wales share.
>
> Editorial note: The 18.8-point gap is the difference between the two shares; the 81 per cent figure is London’s relative excess over the England-and-Wales share.

### With the skill at standard

> In “Housing, England and Wales: Census 2021”, ONS showed that 42.1 per cent of London households had no car or van available in 2021, compared with 23.3 per cent across England and Wales. That is an 18.8 percentage-point gap, or 81 per cent higher than the England-and-Wales share.
>
> **Editorial note:** House style spells out “per cent”; the ONS title remains verbatim. The New Hart’s Rules second edition (2014) is identified, but no relevant passage was supplied, so no book-specific rule is claimed.

### First-pass assessment

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Keeps the title 'Housing, England and Wales: Census 2021' verbatim and the measurements at the household level, including no car or van available. | Met | Met |
| Uses 18.8 percentage points and about 81 per cent relative excess over 23.3%, keeping the measures distinct. | Met | Met |
| Uses 'per cent' in prose and gives a short editorial note identifying the house style or evidential basis without claiming verification from the book. | Missed | Met |

Both preserve the bulletin title and household denominator and distinguish 18.8 percentage points from an approximately 81 per cent relative excess. The skill answer writes out ‘per cent’ throughout and attributes the convention to house style. The baseline leaves 42.1% and 23.3% as symbols in prose despite the exhibition instruction.

**차이.** 두 답 모두 가구 단위, 원제, 18.8%포인트 차이와 약 81%의 상대 차이를 보존합니다. 스킬 답은 ‘per cent’를 일관되게 쓰고 전시 표기 지침임을 밝힙니다. 미적용 답은 본문의 42.1%와 23.3%에 기호를 남겼습니다.
