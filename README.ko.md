# writing-styles-from-giants

[English](README.md)

사상가와 역사적 인물, 영향력 있는 책, 기업과 기관의 글쓰기·설명 방식을 AI 에이전트가 활용할 수 있는 스킬로 만드는 프로젝트입니다.

이름에는 **거인들의 어깨에서 세상을 바라보자**는 뜻을 담았습니다. 앞선 이들의 작업에서 배워, 생각을 구성하고 글로 쓰고 설명하는 구체적인 방법을 에이전트에 제공합니다.

**현재 상태:** 실험 단계의 글쓰기·설명 스킬 24개와 한국어 전용 보조 스킬 1개를 구현했습니다. 각 스킬에는 출처, 단계별 규칙, 평가 사례가 있습니다. 도구별 설치, 독립적인 언어 검토, 릴리스는 아직 검증하지 않았습니다.

## 이 프로젝트를 시작한 이유

평소 AI에게 “간결하게 써 줘”, “핵심 내용을 정리해 줘”처럼 요구사항을 두루뭉술하게 전달하곤 했습니다. 그 결과 의도와 다른 정리본을 받거나, 읽고 싶지 않은 “AI slop”이 만들어졌습니다.

이 프로젝트는 문서화된 글쓰기 방법과 기관의 가이드를 출처와 적용 기준이 분명한 스킬로 정리합니다. 이를 통해 생각의 구성, 설명 방식, 강조할 내용을 AI에 구체적으로 요구하려 합니다.

## 방법론

모든 항목은 실험 단계이며, 직접 작성한 원리 요약 또는 출처와 차이를 밝힌 프로젝트 응용입니다. 폰 노이만은 제외했습니다. New Hart’s Rules는 책 전체의 규칙을 추정하지 않고 제공되거나 확인된 원문을 바탕으로 적용합니다.

| 스킬 | 활용 목적 |
| --- | --- |
| [ASD-STE100 기반 영어](skills/asd-ste100/SKILL.md) | 통제 기술 영어; normal / strict |
| [ELI5](skills/eli5/SKILL.md) | 다섯 살 아이에게 설명 |
| [Orwell의 여섯 원칙](skills/orwell-six-rules/SKILL.md) | 예외를 보존하는 명확한 문장 |
| [Boring Professor](skills/boring-professor/SKILL.md) | 농담·비유 없는 전문 설명 |
| [GTM 기반 형식적 설명](skills/gtm-formal/SKILL.md) | 정의·기호·명제·증명 |
| [Answer with HTML](skills/answer-with-html/SKILL.md) | 상호작용 HTML 설명 |
| [Minto Pyramid](skills/minto-pyramid/SKILL.md) | 핵심 답과 뒷받침 논증 |
| [Jobs 기반 프레젠테이션](skills/steve-jobs-presentation/SKILL.md) | 청중의 이점과 근거 있는 시연 |
| [Hemingway 기반 글쓰기](skills/hemingway-writing/SKILL.md) | 구체적 묘사와 이해에 근거한 생략 |
| [훈민정음 기반 구조](skills/hunminjeongeum/SKILL.md) | 목적·일관된 전개·결론 |
| [Feynman 기반 기법](skills/feynman-technique/SKILL.md) | 설명·빈틈 확인·이해 검증 |
| [Aristotle의 삼단논법](skills/aristotle-syllogism/SKILL.md) | 전제·양화·타당성 |
| [Socrates식 자기 질문](skills/socratic-self-questioning/SKILL.md) | 가정·반례 검토 |
| [Caterpillar Technical English](skills/caterpillar-technical-english/SKILL.md) | 번역을 위한 통제 영어 |
| [Federal Plain Language](skills/federal-plain-language/SKILL.md) | 독자 중심 공공 정보 |
| [IMRaD](skills/imrad/SKILL.md) | 연구 보고서 구조 |
| [SCQA](skills/scqa/SKILL.md) | 상황·문제·질문·답 |
| [Diátaxis](skills/diataxis/SKILL.md) | 독자의 필요에 맞춘 기술 문서 |
| [Amazon 6-pager / AWS](skills/amazon-six-page-narrative/SKILL.md) | 근거 중심 의사결정 서술 |
| [NIST 작성 지침](skills/nist-technical-publication/SKILL.md) | 추적 가능한 기술 보고서 |
| [IETF RFC 기반 명세](skills/ietf-rfc/SKILL.md) | 요구 수준과 정밀한 명세 |
| [Google 설계 문서 관행](skills/google-design-doc/SKILL.md) | 설계 대안·장단점 |
| [Microsoft Writing Style](skills/microsoft-writing-style/SKILL.md) | 도움이 되고 용어가 일관된 기술 글쓰기 |
| [New Hart’s Rules — 원문 확인형](skills/new-harts-rules/SKILL.md) | 판본에 근거한 편집 판단 |
| [한국어 쉬운 글쓰기 보조 스킬](skills/korean-plain-language/SKILL.md) | 한국어 문법·문체·용어 |

에이전트가 스킬 디렉터리 전체에 접근할 수 있도록 하고 `SKILL.md`를 읽게 하세요. 예: “ASD-STE100 normal로 이 설명을 다듬어 줘.” 방법, 출력 언어, 단계를 지정할 수 있습니다. ASD의 `normal`은 `standard`에 대응합니다. “80%”와 “100%”는 요청한 적용 강도이며 측정된 준수율이 아닙니다. 원문에 포함된 명령은 데이터로 취급합니다.

[검토 기록](docs/CATALOG_REVIEW.md)은 정적 검사, Ponytail 검토, 모델 실행 사례를 구분합니다. [권리](THIRD_PARTY_NOTICES.md)와 [남은 작업](docs/PROJECT.md)도 확인하세요.

## 설치

이식 가능한 배포 단위는 `skills/<method-id>/` 디렉터리 전체입니다. 설치 도구는 포함하거나 통합 검증하지 않았습니다. 자체 설치 도구를 만들기 전에 기존 [skills CLI](https://github.com/vercel-labs/skills)가 [설치 계약](docs/ARCHITECTURE.md)을 충족하는지 확인합니다.

## 사용과 단계

- 명시적인 방법론 선택, 추천 요청, 적용 해제, 사용자가 정한 적용 범위를 존중합니다.
- `light`, `standard`, `strict` 단계를 제공하되 사실, 수치, 단위, 부정, 조건, 예외, 불확실성, 인용문, 출처 표시, 코드를 보존합니다.
- 지침은 영어 중심입니다. 언어에 독립적인 구조는 요청한 출력 언어에 적용할 수 있습니다. 영어 문법·통제 사전은 영어에만 적용하며, 한국어 문장 편집을 요청하면 한국어 보조 스킬을 사용합니다. 단어·어절 고정 환산이나 원어민 검토 완료를 주장하지 않습니다.
- Codex, Claude Code, OpenCode, Antigravity, Pi, Cline을 지원 목표로 삼고 공통 스킬 본문을 도구에 종속시키지 않습니다.
- 출처를 밝힌 방법론을 적용합니다. 사칭, 작성자 판별, 공식 규정 준수 인증은 범위에 포함하지 않습니다.

## 기여

정식 `0.0.1` 전까지 단독으로 개발합니다. 브랜치·커밋·PR·CI를 거치며, private 단계의 직접 병합은 [CONTRIBUTING.md](CONTRIBUTING.md)를 따릅니다.

저장소 루트에서 Python 3.12 이상으로 실행합니다. 추가 패키지는 필요하지 않습니다.

```sh
python3 -m unittest discover -s tests -v
python3 scripts/check_repository.py
git diff --check
```

이 검사는 저장소 무결성과 스킬 계약을 확인하며, 글쓰기 품질이나 도구별 활성화를 검증하지 않습니다. 로컬 작업 이력·크리덴셜·캐시는 Git에서 제외하고, 작업 중 직접 만든 임시 파일은 삭제합니다. 자세한 기준은 [SECURITY.md](SECURITY.md)를 확인하세요.

## 저장소 안내

| 경로 | 내용 |
| --- | --- |
| [AGENTS.md](AGENTS.md) | 공통 에이전트 지침 |
| [docs/PROJECT.md](docs/PROJECT.md) | 범위, 구현 순서, 완료 기준 |
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | 스킬 구성, 선택, 엄격도, 설치 계약 |
| [docs/METHOD_AUTHORING.md](docs/METHOD_AUTHORING.md) | 출처, 권리, 규칙, 평가 |
| [docs/LOCALIZATION.md](docs/LOCALIZATION.md) | 언어별 적응과 README 일치 기준 |
| [docs/COMPATIBILITY.md](docs/COMPATIBILITY.md) | 지원 대상 도구와 검증 근거 |
| [docs/DECISIONS.md](docs/DECISIONS.md) | 확정된 선택과 제안 |
| [docs/RELEASING.md](docs/RELEASING.md) | CI, 버전 관리, 소스 릴리스 초안 |
| [docs/REFERENCE.md](docs/REFERENCE.md) | 프로젝트 참고 자료 목록과 검토 기록 |
| [docs/INITIAL_CATALOG_RESEARCH.md](docs/INITIAL_CATALOG_RESEARCH.md) | 유지한 24개 방법과 유사 프로젝트의 조사 |
| [skills/](skills/), [docs/CATALOG_REVIEW.md](docs/CATALOG_REVIEW.md) | 실험 단계 스킬과 검토 근거 |
| [templates/method/](templates/method/), [evals/](evals/) | 작성·평가 예제. 배포된 방법론이나 모델 평가 결과가 아닙니다 |
| [scripts/](scripts/), [tests/](tests/) | 저장소 검사와 테스트 |
| [.github/](.github/) | 협업·자동화 설정 |

## 라이선스와 출처

프로젝트에서 직접 작성한 내용은 [MIT 라이선스](LICENSE)로 배포합니다. [재사용 정책](THIRD_PARTY_NOTICES.md)에 따라 기존 MIT·Apache-2.0 구현을 우선 활용하되, 외부 자료의 원래 라이선스와 고지는 유지합니다. 저자나 기관의 승인을 의미하지 않습니다.
