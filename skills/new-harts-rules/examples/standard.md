# Correcting a percentage-point claim for a UK census exhibit

[한국어](standard.ko.md)

2026-11-09 · `new-harts-rules` 0.1.6 · English · `gpt-6-luna`

### Case and sources

- [Office for National Statistics, Housing, England and Wales: Census 2021 (5 January 2023)](https://www.ons.gov.uk/peoplepopulationandcommunity/housing/bulletins/housingenglandandwales/census2021). Section 6, Car or van availability, and title: 42.1% of London households versus 23.3% across England and Wales in 2021. Exhibition style and draft are original exercise inputs.

**Language scope.** The edited label and editorial note are both in English.

### Prompt

> Copyedit this UK exhibition label in English and append a short English editorial note explaining the denominator and the basis of the spelling decision. Original draft: ‘In “Housing, England and Wales: Census 2021”, ONS showed that 42.1% of Londoners lacked a car in 2021, 18.8 per cent more than across England and Wales.’ The bulletin reports households with no car or van available: 42.1% in London and 23.3% across England and Wales. The editor needs both the percentage-point gap and the relative excess over the England-and-Wales share (round that excess to the nearest whole per cent). House style spells out ‘per cent’ in prose; keep the ONS title verbatim. No passage from New Hart's Rules was supplied. Keep the edited sentence intelligible to a visitor who might otherwise confuse the two comparisons.

### Without the skill

> In ‘Housing, England and Wales: Census 2021’, ONS reported that 42.1 per cent of London households had no car or van available, compared with 23.3 per cent across England and Wales. That is a gap of 18.8 percentage points; London’s share was 81 per cent higher.
>
> *Editorial note: The denominator is households, and “no car or van available” describes household vehicle availability. The 18.8-point gap is the subtraction of the two shares; the 81 per cent relative excess is that gap divided by the England-and-Wales share, rounded to the nearest whole per cent. “Per cent” is spelled out to follow house style; no New Hart’s Rules passage was supplied.*

### With the skill at standard

> In “Housing, England and Wales: Census 2021”, ONS reported that 42.1 per cent of households in London had no car or van available, compared with 23.3 per cent across England and Wales. The London share was 18.8 percentage points higher, or 81 per cent greater relative to the England-and-Wales share.
>
> Editorial note: The denominator is households, not Londoners. The spelling “per cent” follows the stated house style; no relevant passage from *New Hart’s Rules*, second edition (2014), was supplied, so this spelling decision is not attributed to the book.

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Keeps the title 'Housing, England and Wales: Census 2021' verbatim and the measurements at the household level, including no car or van available. | Met | Met |
| Uses 18.8 percentage points and about 81 per cent relative excess over 23.3%, keeping the measures distinct. | Met | Met |
| Uses ‘per cent’ for percentages in English prose; the English note identifies the denominator and exhibition house style without claiming verification from the book. | Met | Met |

**Review.** The label measures households and distinguishes the 18.8-point difference from the roughly 81 per cent relative excess. The spelling choice comes from the exhibition’s own house style.

Masked reviewer assignment: X was the revised answer. The table retains the original control grades. [Previous pair and scores](https://github.com/hobin01/writing-styles-from-giants/blob/20f24c66c7e89e6ce1007249c83c33932998bf01/skills/new-harts-rules/examples/standard.md) · [All attempts and adjudications](https://github.com/hobin01/writing-styles-from-giants/blob/main/evals/runs/2026-11-09-standard/records/new-harts-rules.json).

<details>
<summary>Run record</summary>

Baseline generated 2026-11-08. Revised treatment generated independently on 2026-11-09 with Codex CLI 0.167.0, low reasoning, in a fresh read-only session. SHA-256 prefixes (entrypoint / original baseline / revised answer): `9b8e75069344` / `59f8ac49842a` / `0f0790f8516b`.

</details>
