# How Seoul’s 2024 youth Climate Card refunds differed for physical and mobile cards

2026-11-08 · `korean-plain-language` 0.1.1 · Korean · Codex CLI 0.167.0 / gpt-6.1-sol

### Case and sources

- [서울특별시 내 손안에 서울, ‘월 5만원대’ 청년 맞춤형 기후동행카드 나온다 (2024-02-21)](https://mediahub.seoul.go.kr/archives/2010350). City's February 2024 announcement, especially the retrospective refund, separate registration rule and monthly eligibility conditions under the original pilot.

### Prompt

> 2024년 서울 기후동행카드 시범사업을 소개하는 기록용 글이에요. 당시 청년 할인 대상자에게 실물카드와 모바일카드의 차이를 알려 주는 해요체 문구로, 아래 내용을 네 문장 이내로 다듬어 주세요. 실물카드는 티머니 홈페이지에 등록한 이후의 이용분만 환급 대상이었어요. 모바일카드는 환급을 위한 별도 카드 등록이 필요 없었어요. 둘 다 환불 없이 30일권을 끝까지 사용한 달에만 7,000원을 돌려받을 수 있었고, 환급은 자동 지급이 아니라 별도로 신청해야 했어요. 지금 신청할 수 있다는 뜻이 되면 안 돼요.

### Without a skill

> 2024년 서울 기후동행카드 시범사업 당시 청년 할인 대상자의 실물카드는 티머니 홈페이지에 등록한 이후의 이용분만 환급 대상이었어요. 모바일카드는 환급을 위한 별도 카드 등록이 필요 없었어요. 두 카드 모두 환불 없이 30일권을 끝까지 사용한 달에만 7,000원을 돌려받을 수 있었어요. 환급금은 자동으로 지급되지 않았고, 당시 별도로 환급 신청을 해야 했어요.

### With the skill at standard

> 2024년 서울 기후동행카드 시범사업 당시 청년 할인 대상자는 실물카드를 티머니 홈페이지에 등록한 이후의 이용분에 대해서만 환급받을 수 있었어요. 모바일카드는 환급을 위한 별도의 카드 등록이 필요 없었어요. 두 카드 모두 환불 없이 30일권을 끝까지 사용한 달에만 7,000원을 돌려받을 수 있었어요. 환급금은 자동으로 지급되지 않았고, 당시 별도로 환급을 신청해야 했어요.

### What changed

**Checks set before the run.** Keep the 2024 pilot in the past; distinguish mobile registration from the refund application required in both cases. Retain physical-card registration timing, full 30-day use without refund, the 7,000-won amount per qualifying month and 해요체.

Both distinguish registering the physical card from applying for the refund, and both keep the notice in the past. The baseline makes the physical card the topic of its first sentence. The skill answer makes the eligible rider the subject. Both preserve the four-sentence limit, full 30-day use, the monthly 7,000 won and 해요체.

**차이.** 첫 문장의 중심이 미적용 답안에서는 ‘실물카드’, 스킬 답안에서는 ‘청년 할인 대상자’입니다. 두 답 모두 실물카드 등록과 환급 신청을 구분하며, 30일 만기·월 7,000원·과거 시점이라는 조건을 지켰습니다.
