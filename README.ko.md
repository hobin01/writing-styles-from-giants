# writing-styles-from-giants

[English](README.md)

사상가와 역사적 인물, 영향력 있는 책, 기업과 기관의 글쓰기·설명 방식을 AI 에이전트가 활용할 수 있는 스킬로 만드는 프로젝트입니다.

이름에는 **거인들의 어깨에서 세상을 바라보자**는 뜻을 담았습니다. 앞선 이들의 작업에서 배워, 생각을 구성하고 글로 쓰고 설명하는 구체적인 방법을 에이전트에 제공합니다.

**현재 상태:** 문서와 작성 예제만 있으며, 설치 가능한 스킬은 아직 없습니다. 기반 검사 CI는 통과했습니다. 릴리스와 도구별 호환성 검증은 남아 있습니다.

## 이 프로젝트를 시작한 이유

평소 AI에게 “간결하게 써 줘”, “핵심 내용을 정리해 줘”처럼 요구사항을 두루뭉술하게 전달하곤 했습니다. 그 결과 의도와 다른 정리본을 받거나, 읽고 싶지 않은 “AI slop”이 만들어졌습니다.

이 프로젝트는 문서화된 글쓰기 방법과 기관의 가이드를 출처와 적용 기준이 분명한 스킬로 정리합니다. 이를 통해 생각의 구성, 설명 방식, 강조할 내용을 AI에 구체적으로 요구하려 합니다.

## 방법론

아래 후보는 출처·권리 검토, 규칙 작성, 영어·한국어 검토가 필요합니다.

| 후보 | 활용 목적 | 상태 |
| --- | --- | --- |
| Orwell의 원칙을 참고한 평이한 글쓰기 | 명확한 문장 | 제안 단계, 스킬 없음 |
| Federal Plain Language Guidelines | 독자 중심의 설명 | 제안 단계, 스킬 없음 |
| Minto의 원칙을 참고한 구조화 | 제안과 논증 | 제안 단계, 스킬 없음 |

[출처 참고 자료](THIRD_PARTY_NOTICES.md)와 [프로젝트 범위·다음 단계](docs/PROJECT.md)를 확인하세요.

## 설치

실제 스킬 목록을 검증한 뒤 설치 안내를 제공합니다. 자체 설치 도구를 만들기 전에 기존 [skills CLI](https://github.com/vercel-labs/skills)가 [설치 계약](docs/ARCHITECTURE.md)을 충족하는지 확인합니다.

## 계획된 동작

- 명시적인 방법론 선택, 추천 요청, 적용 해제, 사용자가 정한 적용 범위를 존중합니다.
- `light`, `standard`, `strict` 단계를 제공하되 사실, 수치, 단위, 부정, 조건, 예외, 불확실성, 인용문, 출처 표시, 코드를 보존합니다.
- 영어·한국어부터 시작하며, 단어 수를 어절 수로 고정 환산하지 않고 언어별 규칙과 평가를 사용합니다.
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

이 검사는 저장소 기반을 확인하며, 글쓰기 품질이나 도구별 활성화를 검증하지 않습니다. 로컬 작업 이력·크리덴셜·캐시는 Git에서 제외하고, 작업 중 직접 만든 임시 파일은 삭제합니다. 자세한 기준은 [SECURITY.md](SECURITY.md)를 확인하세요.

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
| [templates/method/](templates/method/), [evals/](evals/) | 작성·평가 예제. 배포된 방법론이나 모델 평가 결과가 아닙니다 |
| [scripts/](scripts/), [tests/](tests/) | 저장소 검사와 테스트 |
| [.github/](.github/) | 협업·자동화 설정 |

## 참고 프로젝트

저장소 구성과 기여 안내는 [mattpocock/skills](https://github.com/mattpocock/skills)를 참고합니다. 검토한 구조와 적용 방식은 [참고 저장소 검토](docs/REFERENCE.md)에 기록했습니다.

## 라이선스와 출처

프로젝트에서 직접 작성한 내용은 [MIT 라이선스](LICENSE)로 배포합니다. [재사용 정책](THIRD_PARTY_NOTICES.md)에 따라 기존 MIT·Apache-2.0 구현을 우선 활용하되, 외부 자료의 원래 라이선스와 고지는 유지합니다. 저자나 기관의 승인을 의미하지 않습니다.
