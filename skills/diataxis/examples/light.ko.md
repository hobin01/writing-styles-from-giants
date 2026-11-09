# 초록색 CI 결과는 어떤 Kubernetes 배포를 확인했을까?

[English](light.md) · **light** · [standard](standard.ko.md) · [strict](strict.ko.md)

### 질문

> 09:00에 checkout-api의 리비전 7 배포가 진행되는 동안 CI가 별도 옵션 없이 kubectl rollout status deployment/checkout-api를 실행했다. 7이 끝나기 전에 리비전 8이 시작됐고 이후 더 새 리비전은 없었다. 명령은 나중에 성공을 보고했다. 기본값은 최신 롤아웃을 따라간다. --revision=N은 지정한 리비전을 감시하다가 다른 리비전으로 대체되면 중단하고, --watch=false는 현재 상태를 한 번 읽는다. CI가 실제로 확인한 리비전은 어느 것인가? 7만 감시하려면 어떤 명령을 쓰고, 지금 상태를 기다리지 않고 보려면 어떤 명령을 쓰는가?

**출처** · [Kubernetes command reference, kubectl rollout status](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_rollout/kubectl_rollout_status/)

### 스킬 적용

> CI가 확인한 것은 리비전 8입니다. 기본 동작이 최신 롤아웃을 따라가므로 리비전 7이 끝나기 전에 8이 시작된 뒤, 명령은 8의 완료를 기다려 성공을 보고했습니다.
>
> - 리비전 7만 감시: `kubectl rollout status deployment/checkout-api --revision=7`
> - 기다리지 않고 현재 상태 한 번 읽기: `kubectl rollout status deployment/checkout-api --watch=false`

### 스킬 미적용

> CI는 기본 동작에 따라 최신 롤아웃인 **리비전 8**의 완료를 확인했습니다.
>
> - 리비전 7만 감시: `kubectl rollout status deployment/checkout-api --revision=7`
> - 기다리지 않고 현재 상태 확인: `kubectl rollout status deployment/checkout-api --watch=false`
