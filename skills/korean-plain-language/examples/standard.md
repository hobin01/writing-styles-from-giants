# Which months qualified for Seoul’s pilot refund?

[한국어](standard.ko.md)

2026-11-09 · `korean-plain-language` 0.1.9 · English · `gpt-6-luna`

### Case and sources

- [서울특별시 내 손안에 서울, ‘월 5만원대’ 청년 맞춤형 기후동행카드 나온다 (2024-02-21)](https://mediahub.seoul.go.kr/archives/2010350). City's February 2024 announcement, especially the retrospective refund, separate registration rule and monthly eligibility conditions under the original pilot.

**Language scope.** The editor’s explanation is in English; the object being edited is Korean. Quoted Korean phrases demonstrate tense, modality and polite endings.

### Prompt

> Write a brief editorial memo in English for an editor working on a Korean exhibit about Seoul’s 2024 youth Climate Card pilot. The draft says ‘지우와 민서는 지금 환급금을 받아요’. At the time, each completed 30-day pass used without a refund could qualify for a 7,000-won refund. Physical cards counted only after registration; mobile cards required no separate card registration. Both types required a refund application. Assume all other eligibility conditions were met. Jiwoo completed a first physical pass before registration, completed the second after registration, and refunded a third on day 18. Minseo completed two mobile passes without refund. Explain how much each could have applied for and why. Explain the time and payment implication in the draft and suggest a short Korean 해요체 phrase to fix it. Keep the editorial explanation in English; retain Korean where discussing the actual wording.

### Without the skill

> **Editorial memo**
>
> The statement ‘지우와 민서는 지금 환급금을 받아요’ implies that both are receiving refunds now. That is not supported: the amounts described are potential refunds they could have applied for, and both card types required an application.
>
> Jiwoo could have applied for **7,000 won** for the second pass only. The first physical pass was completed before the card was registered, so it did not count. The third pass was refunded on day 18, so it was not a completed 30-day pass used without a refund.
>
> Minseo could have applied for **14,000 won**: two completed 30-day mobile passes used without refunds, at 7,000 won each. Mobile cards did not need separate card registration, but still required a refund application.
>
> A concise 해요체 replacement is: **‘지우와 민서는 환급금을 신청할 수 있어요.’** This makes clear that the refunds were available to apply for, not necessarily already paid.

### With the skill at standard

> The draft’s “지우와 민서는 지금 환급금을 받아요” says Jiwoo and Minseo are receiving refunds now. The pilot’s refund was a past opportunity to apply for payment, so this wording may wrongly suggest a current payment or a guaranteed one. Replace it with **“환급금을 신청할 수 있었어요”** (“They could apply for a refund”).
>
> - **Jiwoo — 7,000 won.** The first physical pass was completed before registration, so it did not qualify. The second was completed after registration and without a refund, so Jiwoo could apply for 7,000 won. The third was refunded on day 18, so it did not qualify as a completed 30-day pass used without a refund.
> - **Minseo — 14,000 won.** Both mobile passes were completed without refunds. Mobile cards did not need separate registration, so each pass could qualify for 7,000 won.
>
> Both still had to apply; eligibility did not mean the refund was already received.

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Correctly gives Jiwoo 7,000 won, counting only the second pass and explaining why the unregistered and refunded passes do not count. | Met | Met |
| Correctly gives Minseo 14,000 won for two completed passes; distinguishes not having to register the mobile card from having to apply for either refund. | Met | Met |
| Explains the draft's timing and payment implications in English and proposes Korean 해요체 wording that conveys past eligibility to apply without implying current entitlement or automatic payment. | Missed | Met |

**Review.** Jiwoo could apply for 7,000 won and Minseo for 14,000. Mobile registration was waived, but both people still needed to apply. The proposed Korean wording describes eligibility at the time.

Masked reviewer assignment: X was the revised answer. The table retains the original control grades. [Previous pair and scores](https://github.com/hobin01/writing-styles-from-giants/blob/20f24c66c7e89e6ce1007249c83c33932998bf01/skills/korean-plain-language/examples/standard.md) · [All attempts and adjudications](https://github.com/hobin01/writing-styles-from-giants/blob/main/evals/runs/2026-11-09-standard/records/korean-plain-language.json).

<details>
<summary>Run record</summary>

Baseline generated 2026-11-08. Revised treatment generated independently on 2026-11-09 with Codex CLI 0.167.0, low reasoning, in a fresh read-only session. SHA-256 prefixes (entrypoint / original baseline / revised answer): `22797d4c7797` / `b2b7f3a4df0d` / `af8afbb2a4fc`.

</details>
