# 어떤 스킬을 쓰면 될까?

Codex에서는 아래 표에서 ID를 골라 `$wsg ID 요청`으로 써 보세요. 기본값은 `standard`입니다. 필요한 부분만 가볍게 손볼 때는 `light`, 적용할 수 있는 규칙을 모두 점검할 때는 `strict`를 붙이세요. 원하는 결과는 알겠는데 방법을 고르기 어렵다면 `$wsg auto 요청`으로 시작하면 됩니다.

Claude Code에서는 `/wsg ID 요청`, `/wsg:auto 요청`, `/wsg:docs ko`로 쓸 수 있습니다.

### 개념을 설명하거나 주장을 따져 보고 싶을 때

| ID | 이런 글에 쓰세요 |
| --- | --- |
| [`eli5`](../skills/eli5/SKILL.md) | 다섯 살 아이에게 읽어 줄 설명. 아이가 떠올릴 수 있는 행동부터 한 단계씩 설명합니다. |
| [`feynman-technique`](../skills/feynman-technique/SKILL.md) | 원리를 남에게 가르쳐 보면서, 그 설명만으로는 다음 일을 예측할 수 없는 지점을 찾습니다. |
| [`boring-professor`](../skills/boring-professor/SKILL.md) | 이미 분야를 아는 독자를 위해, 농담이나 비유 없이 정확한 용어로 기술적 관계를 풀어냅니다. |
| [`gtm-formal`](../skills/gtm-formal/SKILL.md) | 수학 명제의 대상과 정의, ‘모든’과 ‘어떤’의 범위를 밝히고 증명을 쓰거나 검토합니다. |
| [`aristotle-syllogism`](../skills/aristotle-syllogism/SKILL.md) | ‘모든 A는 B다’, ‘일부 B는 C다’ 같은 전제로부터 결론이 실제로 따라오는지 따져 봅니다. |
| [`socratic-self-questioning`](../skills/socratic-self-questioning/SKILL.md) | 질문이나 반례로 숨은 가정을 점검한 뒤, 근거가 뒷받침하는 만큼만 주장합니다. |
| [`hunminjeongeum`](../skills/hunminjeongeum/SKILL.md) | 독자가 어떤 어려움을 겪는지 먼저 밝히고, 제안이 그 문제를 어떻게 푸는지 결론까지 이어 갑니다. |
| [`answer-with-html`](../skills/answer-with-html/SKILL.md) | 도식이나 직접 조작할 수 있는 예제가 담긴 HTML 답안을 만듭니다. |

### 결정하거나 발표할 때

| ID | 이런 글에 쓰세요 |
| --- | --- |
| [`minto-pyramid`](../skills/minto-pyramid/SKILL.md) | 추천을 먼저 쓰고 그 아래에 근거를 묶습니다. 도입부만 필요하면 독자가 결정해야 할 질문을 중심으로 씁니다. |
| [`amazon-six-page-narrative`](../skills/amazon-six-page-narrative/SKILL.md) | 팀이 함께 읽고 결정할 수 있도록 배경, 선택지, 근거, 남은 위험을 하나의 문서에 담습니다. |
| [`steve-jobs-presentation`](../skills/steve-jobs-presentation/SKILL.md) | 제품의 결과나 시연이 청중에게 어떤 도움이 되는지 실제 발표에서 말할 문장으로 씁니다. |

### 기술 문서를 작성할 때

| ID | 이런 글에 쓰세요 |
| --- | --- |
| [`google-design-doc`](../skills/google-design-doc/SKILL.md) | 엔지니어링 리뷰를 받을 설계안을 작성하고, 대안별 장단점과 제약을 비교합니다. |
| [`ietf-rfc`](../skills/ietf-rfc/SKILL.md) | 구현자가 무엇을 반드시 해야 하고 무엇을 선택할 수 있는지 구분해 명세를 씁니다. |
| [`nist-technical-publication`](../skills/nist-technical-publication/SKILL.md) | 측정 방법, 단위, 불확실성, 한계를 밝혀서 독자가 수치의 근거를 확인할 수 있게 합니다. |
| [`imrad`](../skills/imrad/SKILL.md) | 직접 수행한 연구의 질문, 방법, 관찰 결과, 해석이 구별되도록 논문을 구성합니다. |
| [`diataxis`](../skills/diataxis/SKILL.md) | 독자에게 필요한 것이 따라 해 볼 튜토리얼인지, 특정 작업의 절차인지, 찾아볼 정보인지, 원리 설명인지에 맞춰 문서를 씁니다. |

### 문장을 다듬을 때

| ID | 이런 글에 쓰세요 |
| --- | --- |
| [`asd-ste100`](../skills/asd-ste100/SKILL.md) | 기술 영어에서 용어를 통일하고 작업과 조건을 명확히 씁니다. `strict`는 프로젝트가 다루는 규칙을 모두 점검하며, 공식 표준 준수 여부는 검증하지 않습니다. |
| [`orwell-six-rules`](../skills/orwell-six-rules/SKILL.md) | 논픽션에서 진부한 표현과 불필요한 단어를 덜어 내면서 원래 뜻을 살립니다. |
| [`federal-plain-language`](../skills/federal-plain-language/SKILL.md) | 공공 안내문에서 독자가 무엇을 언제까지 해야 하고 어떤 조건이 붙는지 찾기 쉽게 정리합니다. |
| [`microsoft-writing-style`](../skills/microsoft-writing-style/SKILL.md) | 제품 안내문에서 실제 화면의 버튼 이름과 명령어를 그대로 쓰고, 먼저 필요한 조건을 알려 줍니다. |
| [`new-harts-rules`](../skills/new-harts-rules/SKILL.md) | 영어 출판물을 편집할 때 제공된 사내 지침이나 해당 판본의 구절을 근거로 표기 방식을 정합니다. |
| [`korean-plain-language`](../skills/korean-plain-language/SKILL.md) | 한국어 문장의 조사, 지시 대상, 종결 표현을 다듬되 말투와 ‘해도 된다’와 ‘해야 한다’의 차이를 지킵니다. |
