# Correcting a percentage-point claim for a UK census exhibit

[한국어](standard.ko.md)

2026-11-08 · `new-harts-rules` 0.1.2 · English · `gpt-6-luna`

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

> “In ‘Housing, England and Wales: Census 2021’, ONS reported that 42.1 per cent of London households had no car or van available, compared with 23.3 per cent across England and Wales—a gap of 18.8 percentage points. The London share was 81 per cent higher.”
>
> **Editorial note:** The denominator is households with no car or van available, not Londoners. The 18.8-point gap is 42.1 minus 23.3; the 81 per cent relative excess is that gap divided by 23.3, rounded to the nearest whole per cent. “Per cent” follows the stated house style; the ONS title remains verbatim. Edition: *New Hart’s Rules*, second edition (2014); level: standard. No relevant passage was supplied, so the spelling decision is attributed to house style, not to the book.

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Keeps the title 'Housing, England and Wales: Census 2021' verbatim and the measurements at the household level, including no car or van available. | Met | Met |
| Uses 18.8 percentage points and about 81 per cent relative excess over 23.3%, keeping the measures distinct. | Met | Met |
| Uses ‘per cent’ for percentages in English prose; the English note identifies the denominator and exhibition house style without claiming verification from the book. | Met | Missed |

**Masked review** (Y = baseline; X = standard). Both retain the bulletin title, report household shares, and distinguish 18.8 percentage points from an 81 per cent relative excess. Y correctly describes households as the denominator. X calls households *with no car or van* the denominator in its note; those households form the numerator of each area's share. X also adds an unrequested edition and level, which may reveal the condition.

<details>
<summary>Run record</summary>

Each arm was a separate ephemeral read-only Codex CLI 0.167.0 session with low reasoning effort. Neither session was given the other answer or an answer in the other language.

SHA-256 prefixes (entrypoint / baseline answer / standard answer): `984d898d4573` / `59f8ac49842a` / `0fe1907dab99`.

</details>
