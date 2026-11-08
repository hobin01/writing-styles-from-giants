# 초록색 CI 결과는 어떤 Kubernetes 배포를 확인했을까?

[English](standard.md)

2026-11-08 · `diataxis` 0.1.1 · 한국어 · `gpt-6-luna`

### 사례와 출처

- [Kubernetes command reference, kubectl rollout status](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_rollout/kubectl_rollout_status/)

Kubernetes 문서는 진행 상태를 조회할 때 기본으로 추적하는 리비전과 --revision, --watch 옵션의 동작을 설명합니다. checkout-api의 배포 상황은 예제입니다.

### 질문

> 배포팀을 위한 짧은 한국어 명령 참조 항목을 써 주세요. Deployment checkout-api를 대상으로 CI가 09:00에 별도 플래그 없이 kubectl rollout status를 실행해 리비전 7을 지켜봅니다. 7이 끝나기 전에 리비전 8이 시작되고, 명령은 나중에 성공을 보고합니다. 기본 감시는 최신 롤아웃으로 넘어갑니다. --revision=N을 주면 해당 리비전을 감시하다가 새 리비전에 대체될 때 중단하고, --watch=false는 기다리지 않고 현재 상태를 읽습니다. 이 예에서는 8이 마지막 리비전입니다. CI 성공이 7과 8에 대해 무엇을 입증하고 무엇은 입증하지 않는지 밝히세요. 새 CI 작업에서 리비전 7만 감시할 명령, 운영자가 즉시 현재 상태를 조회할 명령을 각각 정확히 제시하세요. 따라 하는 튜토리얼보다 필요할 때 바로 찾을 수 있는 참조 문서가 필요합니다.

### 스킬 미적용 답안

> ### `kubectl rollout status` 명령 참조
>
> 배포 `checkout-api`의 롤아웃 상태를 확인합니다. 기본 동작은 최신 롤아웃을 감시하므로, 리비전 7을 지켜보던 CI 명령은 리비전 8이 시작되면 새 롤아웃으로 넘어갑니다. 나중에 보고된 성공은 마지막 리비전인 **8이 완료됐음**을 입증하지만, **7이 완료됐음**을 입증하지는 않습니다.
>
> - **새 CI 작업에서 리비전 7만 감시:** `kubectl rollout status deployment/checkout-api --revision=7`
>
>   리비전 7이 새 리비전으로 대체되면 감시를 중단합니다. 성공 여부를 확인하려면 명령의 종료 결과를 확인하세요.
>
> - **운영자가 현재 상태를 즉시 조회:** `kubectl rollout status deployment/checkout-api --watch=false`
>
>   기다리지 않고 현재 롤아웃 상태를 한 번 읽습니다.

### 스킬 적용 답안 · standard

> ### `kubectl rollout status` 참조
>
> 기본 감시는 진행 중인 롤아웃을 따라갑니다. 09:00에 시작한 CI 작업은 별도 플래그 없이 `deployment/checkout-api`의 리비전 7을 감시했지만, 7이 끝나기 전에 8이 시작되어 기본 감시가 최신 롤아웃인 8로 넘어갔습니다. 이후 명령의 성공은 **리비전 8의 롤아웃이 완료됐음**을 입증합니다. 리비전 7의 완료를 입증하지는 않습니다. 이 예에서는 8이 마지막 리비전입니다.
>
> 새 CI 작업에서 리비전 7만 감시하려면:
>
> ```sh
> kubectl rollout status deployment/checkout-api --revision=7
> ```
>
> `--revision=7`은 해당 리비전을 감시하며, 새 리비전으로 대체되면 감시를 중단합니다. 운영자가 기다리지 않고 현재 상태를 즉시 조회하려면:
>
> ```sh
> kubectl rollout status deployment/checkout-api --watch=false
> ```
>
> 이 명령은 현재 상태를 읽고 기다리지 않습니다. 조회 결과만으로 롤아웃 완료를 입증하지는 않습니다.

### 두 답안의 차이

| 실행 전에 정한 기준 | 스킬 미적용 | 스킬 적용 |
| --- | --- | --- |
| 기본 감시가 마지막 리비전 8의 성공을 확인했으나 리비전 7의 성공은 입증하지 못한다고 밝힌다. | 충족 | 충족 |
| deployment/checkout-api에 --revision=7을 주는 실행 가능한 명령을 제시하고, 리비전 7이 대체되면 8을 따라가지 않고 감시가 중단된다고 설명한다. | 충족 | 충족 |
| --watch=false를 쓰는 실행 가능한 현재 상태 조회 명령을 담고, 두 명령의 목적을 간결한 참조 항목에서 쉽게 찾을 수 있다. | 충족 | 충족 |

**블라인드 검토** (Y = 미적용, X = 스킬 적용). 두 답 모두 CI 성공이 리비전 8을 확인한 것이고 리비전 7의 성공은 입증하지 않는다고 설명한다. X 쪽은 명령을 각각 코드 블록에 싣고, Y 쪽은 두 사용 목적을 강조한 목록에 명령을 나란히 배치한다. 둘 다 리비전 고정 감시가 대체 시 중단되는 조건과 즉시 조회 옵션을 정확히 안내한다.

<details>
<summary>실행 기록</summary>

각 답안은 Codex CLI 0.167.0, low 추론 설정의 별도 임시 읽기 전용 세션에서 생성했습니다. 같은 문항의 다른 답안이나 다른 언어의 답안은 입력하지 않았습니다.

SHA-256 앞 12자리 (스킬 지침 / 미적용 원문 / 적용 원문): `1bf8f74acf77` / `ef4253e91603` / `4138d1891549`.

</details>
