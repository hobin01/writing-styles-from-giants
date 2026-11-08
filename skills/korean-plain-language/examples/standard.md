# Which months qualified for Seoul’s pilot refund?

2026-11-08 · `korean-plain-language` 0.1.1 at first pass · `gpt-6-luna` · Codex CLI 0.167.0

### Case and sources

- [서울특별시 내 손안에 서울, ‘월 5만원대’ 청년 맞춤형 기후동행카드 나온다 (2024-02-21)](https://mediahub.seoul.go.kr/archives/2010350). City's February 2024 announcement, especially the retrospective refund, separate registration rule and monthly eligibility conditions under the original pilot.

**Reasoning task.** Intersect registration timing, completed 30-day periods and refund exclusions before calculating two riders' historical entitlements.

### Prompt

> 2024년 서울시 기후동행카드 시범사업을 돌아보는 전시 문구를 해요체 다섯 문장 이내로 써 주세요. 당시 원칙은 등록한 실물카드의 등록 이후 이용분 또는 별도 등록이 필요 없는 모바일카드 이용분 중, 환불 없이 30일 만기를 채운 달마다 7,000원이었고 두 종류 모두 별도 환급 신청이 필요했어요. 연령 등 나머지 조건은 충족했다고 가정해요. 가상 이용자 지우는 실물카드로 첫 30일권을 미등록 상태에서 끝까지 쓴 뒤 등록하고 둘째 권을 30일 만기로 썼지만 셋째 권은 18일째 환불했어요. 민서는 모바일카드로 30일권 두 장을 환불 없이 끝까지 썼어요. 각각 당시 얼마를 신청할 수 있었는지, 왜 금액이 달랐는지 독자가 따라갈 수 있게 해 주세요.

### Without a skill

> 실물카드를 쓴 지우는 첫 이용권을 다 쓴 뒤 등록했으므로, 등록 전 이용분은 환급 대상이 아니에요. 등록 이후 쓴 둘째 이용권은 30일 만기를 채워 7,000원을 신청할 수 있지만, 셋째 이용권은 18일째 환불해 대상이 아니에요. 따라서 지우가 신청할 수 있는 금액은 7,000원이에요. 모바일카드를 쓴 민서는 등록 없이도 이용분이 인정되므로, 환불 없이 만기를 채운 두 달에 대해 14,000원을 신청할 수 있어요. 두 사람 모두 별도 신청이 필요했고, 차이는 실물카드의 등록 시점과 만기·환불 조건을 충족한 달 수예요.

### With the skill at standard

> 지우는 실물카드 첫 이용분을 다 쓴 뒤 등록했으므로, 등록 전에 이용한 첫 30일권은 환급 대상이 아니에요.\
> 등록 후 이용한 둘째 30일권은 환불 없이 만기를 채웠으므로, 별도 신청을 하면 7,000원을 받을 수 있어요.\
> 셋째 권은 18일째 환불했으므로 만기 조건을 채우지 못해 환급액에 포함되지 않아요.\
> 민서는 등록이 필요 없는 모바일카드로 30일권 두 장을 모두 환불 없이 만기까지 이용해, 별도 신청으로 14,000원을 받을 수 있어요.\
> 따라서 지우는 7,000원, 민서는 14,000원을 신청할 수 있었고, 실물카드는 등록 이후 이용분만 인정된 반면 모바일카드는 등록 전 이용분 제한이 없었기 때문에 금액이 달랐어요.

### First-pass assessment

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Correctly gives Jiwoo 7,000 won, counting only the second pass and explaining why the unregistered and refunded passes do not count. | Met | Met |
| Correctly gives Minseo 14,000 won for two completed passes; distinguishes not having to register the mobile card from having to apply for either refund. | Met | Met |
| Maintains 해요체 and the 2024 retrospective scope, without implying automatic payment or ongoing eligibility. | Missed | Missed |

Both calculate 7,000 won for Jiwoo and 14,000 for Minseo, exclude the first and third physical passes for different reasons, and require an application for both. Both keep 해요체, but their statements about what a rider can receive mostly use the present tense without anchoring eligibility to the 2024 pilot. The skill answer closes with a retrospective phrase; the baseline gives the two riders' results in a more compact sequence.

**차이.** 둘 다 지우 7,000원과 민서 14,000원을 정확히 계산하고, 별도 신청이 필요하다고 설명합니다. 스킬 답은 끝에서 과거형으로 정리하지만, 두 답 모두 환급 가능 여부를 주로 현재형으로 써서 2024년 시범사업에 한정된 조건임이 충분히 드러나지 않습니다.

<details>
<summary>Developmental retest · version 0.1.2</summary>

Carry the historical date into the Korean wording of permission and eligibility. This retest is excluded from the first-pass counts.

The request and original baseline are unchanged.

**New standard answer**

> 2024년 서울시 기후동행카드 시범사업에서는 등록한 실물카드의 등록 이후 이용분이나 별도 등록이 필요 없는 모바일카드 이용분으로, 환불 없이 30일 만기를 채운 달마다 7,000원을 받을 수 있었어요. 다만 두 종류 모두 별도로 환급 신청을 해야 했어요. 지우는 첫 실물카드 이용분을 다 쓴 뒤 등록했기 때문에 그 이용분은 환급 대상이 아니었고, 둘째 권은 만기를 채워 7,000원을 신청할 수 있었어요. 셋째 권은 18일째 환불했으므로 환급 대상이 아니어서, 지우가 신청할 수 있는 금액은 총 7,000원이었어요. 민서는 모바일카드 두 장 모두 만기를 채우고 환불하지 않아 총 14,000원을 신청할 수 있었어요.

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Correctly gives Jiwoo 7,000 won, counting only the second pass and explaining why the unregistered and refunded passes do not count. | Met | Met |
| Correctly gives Minseo 14,000 won for two completed passes; distinguishes not having to register the mobile card from having to apply for either refund. | Met | Met |
| Maintains 해요체 and the 2024 retrospective scope, without implying automatic payment or ongoing eligibility. | Missed | Met |

Both the skill answer and the baseline correctly count only Jiwoo’s second pass (₩7,000), both of Minseo’s passes (₩14,000), and a separate application for each person despite mobile cards needing no registration. Both use five 해요체 sentences. The skill answer names the 2024 pilot and describes what riders could claim then; the baseline omits the historical date and uses present-tense eligibility that can read as current policy.

**차이.** 스킬 답과 미적용 답 모두 지우는 둘째 권만 7,000원, 민서는 두 권 합계 14,000원으로 계산한다. 모바일카드 등록 면제와 두 사람의 별도 환급 신청도 구분하고 해요체 다섯 문장을 쓴다. 스킬 답은 2024년 시범사업 당시 신청할 수 있었던 금액으로 서술한다. 미적용 답은 연도와 시범사업을 생략하고 ‘신청할 수 있어요’ 등 현재형을 써서 현행 제도로 읽힐 수 있다.

</details>
