# Which months qualified for Seoul’s pilot refund?

[한국어](standard.ko.md)

2026-11-08 · `korean-plain-language` 0.1.2 · English · `gpt-6-luna`

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

> **Editorial memo**
>
> The draft, “지우와 민서는 지금 환급금을 받아요” (“Jiwoo and Minseo receive refunds now”), makes a past pilot sound current and suggests payment is automatic. Both are misleading: the refunds were available during the 2024 pilot, and eligible participants still had to apply.
>
> Jiwoo could have applied for **7,000 won**. The first physical pass was completed before registration, so it did not count; the second was completed after registration and was not refunded, so it qualified. The third pass was refunded on day 18 and was not a completed, unrefunded 30-day pass.
>
> Minseo could have applied for **14,000 won**. Both completed mobile passes were unrefunded and qualified; mobile cards did not require separate card registration. Minseo still needed to submit a refund application.
>
> A short 해요체 replacement is: **“2024년 시범사업 당시, 조건을 충족한 이용자는 환급을 신청할 수 있었어요.”** This makes the timing past and preserves the meaning as permission to apply, not a promise of payment.

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Correctly gives Jiwoo 7,000 won, counting only the second pass and explaining why the unregistered and refunded passes do not count. | Met | Met |
| Correctly gives Minseo 14,000 won for two completed passes; distinguishes not having to register the mobile card from having to apply for either refund. | Met | Met |
| Explains the draft's timing and payment implications in English and proposes Korean 해요체 wording that conveys past eligibility to apply without implying current entitlement or automatic payment. | Missed | Met |

**Masked review** (Y = baseline; X = standard). Both calculate 7,000 won for Jiwoo and 14,000 for Minseo, distinguish registration from applying, and explain the draft’s misleading present tense in English. X proposes Korean wording anchored to the 2024 pilot and uses 신청할 수 있었어요. Y’s replacement uses 신청할 수 있어요, which can still suggest current eligibility despite the accurate English explanation.

<details>
<summary>Run record</summary>

Each arm was a separate ephemeral read-only Codex CLI 0.167.0 session with low reasoning effort. Neither session was given the other answer or an answer in the other language.

SHA-256 prefixes (entrypoint / baseline answer / standard answer): `c0be7cf32505` / `b2b7f3a4df0d` / `cdfd5fc43c0c`.

</details>
