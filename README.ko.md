# writing-styles-from-giants

[English](README.md)

AI한테 “쉽게 설명해 줘”라고 하면, 제가 궁금했던 부분까지 빼고 짧게 끝낼 때가 있어요. 다섯 살 아이에게 자전거 브레이크를 설명하는 것과, 엔지니어에게 브레이크의 작동 원리를 설명하는 건 꽤 다른 일이잖아요. 그래서 **누구에게, 어떤 방식으로 설명할지** 직접 고를 수 있게 만들었습니다. 앞선 사람들의 글쓰기 방식을 제 질문에 빌려 쓴다는 뜻에서 이름도 ‘거인의 어깨 위에 선다’는 말에서 따왔어요.

어떤 차이가 나는지 궁금하다면 [한국어 예제](EXAMPLES.ko.md)나 [영어 예제](EXAMPLES.md)를 열어 보세요. 22개 스킬 모두 GPT-6 Luna에 한국어로 직접 묻고, 영어는 별도 세션에서 다시 물었습니다. [서로 다른 시각에 조회한 두 DNS 서버](skills/feynman-technique/examples/standard.ko.md)는 왜 다른 답을 줄까요? [LIGO의 오경보율](skills/imrad/examples/standard.ko.md)로 관측 한 건이 잡음일 확률을 알 수 있을까요? [서울 지하철 노선도에서 길을 찾는 시간이 줄면](skills/hunminjeongeum/examples/standard.ko.md) 전체 여정에서는 얼마나 절약될까요? 고등학생 이상의 추론을 목표로 만든 각 문제에서 스킬 없이 쓴 답과 `standard` 답을 나란히 볼 수 있습니다.

## Codex에서 써 보기

이 저장소를 프로젝트로 열고, 새 대화에 아래 예제 중 한 줄을 그대로 입력해 보세요. 맨 앞의 `$`도 명령의 일부입니다.

```text
$wsg eli5 자전거 브레이크를 잡으면 왜 바퀴가 느려지는지 설명해 줘.
$wsg asd-ste100 strict Edit this note: The access panel may be opened only after both lamps go out.
$wsg auto 캐시를 넣을지 결정해야 해. DB를 매번 읽는 방식과 비교하는 설계 문서 초안을 써 줘.
$wsg docs ko
```

- **방법을 알고 있으면** `$wsg 스킬-ID [단계] 요청`을 쓰세요. 단계를 생략하면 매번 `standard`입니다. 원문을 가볍게 손보려면 `light`, 해당 방법의 규칙을 하나씩 점검하려면 `strict`를 고르세요. 단계가 달라도 조건이나 수치의 의미는 그대로 보존합니다.
- **고르기 어렵다면** `$wsg auto [단계] 요청`을 쓰세요. 요청의 목적과 독자에 맞는 스킬을 골라 이유를 알려 주고, 그 스킬로 답합니다.
- **목록부터 보려면** `$wsg docs`를 쓰세요. 기본 언어는 영어입니다. `$wsg docs ko`는 한국어로, `$wsg docs en`은 영어로 각 스킬의 용도를 보여 줍니다.

다른 프로젝트에서도 `$wsg`를 쓰려면 [Codex 전역 연결](docs/COMPATIBILITY.md#codex-user-scope)을 한 번 설정하세요. 이 저장소를 직접 가리키므로 스킬이나 명령이 로컬에서 바뀌면 다시 설치할 필요가 없습니다.

Claude Code에서는 이 저장소 안에서 각각 `/wsg`, `/wsg:auto`, `/wsg:docs ko`로 입력합니다. [도구별 확인 범위](docs/COMPATIBILITY.md)

## 어느 스킬을 고르면 될까?

같은 설명 요청이라도 원하는 결과에 따라 선택이 달라집니다. 아이가 손잡이에서 바퀴까지의 움직임을 따라가게 하려면 **ELI5**, 설명에서 빠진 단계를 찾으려면 **Feynman**, 수식으로 주장을 증명하려면 **GTM**이 맞습니다. 각 이름을 누르면 작성 지침과 예제를 볼 수 있어요. 명령에 넣을 정확한 이름은 [스킬 ID와 용도](commands/catalog.ko.md)에서 복사할 수 있습니다. 예를 들어 Feynman의 ID는 `feynman-technique`입니다.

| 하고 싶은 일 | 스킬 |
| --- | --- |
| 설명하기 | [ELI5](skills/eli5/SKILL.md) · [Feynman](skills/feynman-technique/SKILL.md) · [Boring Professor](skills/boring-professor/SKILL.md) · [인터랙티브 HTML](skills/answer-with-html/SKILL.md) · [Jobs 발표](skills/steve-jobs-presentation/SKILL.md) |
| 논리 세우기 | [GTM 증명](skills/gtm-formal/SKILL.md) · [아리스토텔레스 삼단논법](skills/aristotle-syllogism/SKILL.md) · [소크라테스식 질문](skills/socratic-self-questioning/SKILL.md) · [훈민정음](skills/hunminjeongeum/SKILL.md) · [민토 피라미드](skills/minto-pyramid/SKILL.md) |
| 문장 다듬기 | [ASD-STE100 기반 기술 영어](skills/asd-ste100/SKILL.md) · [오웰 6원칙](skills/orwell-six-rules/SKILL.md) · [미국 연방 평문](skills/federal-plain-language/SKILL.md) · [Microsoft 문체](skills/microsoft-writing-style/SKILL.md) · [New Hart’s Rules](skills/new-harts-rules/SKILL.md) · [한국어 평문](skills/korean-plain-language/SKILL.md) |
| 문서 쓰기 | [Diátaxis](skills/diataxis/SKILL.md) · [Google 설계 문서](skills/google-design-doc/SKILL.md) · [Amazon 6-pager](skills/amazon-six-page-narrative/SKILL.md) · [IETF RFC](skills/ietf-rfc/SKILL.md) · [IMRaD](skills/imrad/SKILL.md) · [NIST 기술 보고서](skills/nist-technical-publication/SKILL.md) |

ASD의 `normal`은 `standard`의 별칭입니다. `strict`는 이 프로젝트가 구현한 규칙을 가장 엄격하게 적용하는 단계이며, 공식 ASD-STE100 준수 인증을 뜻하지 않습니다.

방법별 출처는 [참고 자료](docs/REFERENCE.md)에 있습니다. 직접 만든 내용에는 [MIT 라이선스](LICENSE)를 적용합니다. [외부 자료의 권리](THIRD_PARTY_NOTICES.md)와 [기여 방법](CONTRIBUTING.md)도 확인할 수 있습니다.
