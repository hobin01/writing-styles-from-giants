# 초록색 CI 결과는 어떤 Kubernetes 배포를 확인했을까?

[English](standard.md) · [light](light.ko.md) · [strict](strict.ko.md)

### 질문

> 09:00에 checkout-api의 리비전 7 배포가 진행되는 동안 CI가 별도 옵션 없이 kubectl rollout status deployment/checkout-api를 실행했다. 7이 끝나기 전에 리비전 8이 시작됐고 이후 더 새 리비전은 없었다. 명령은 나중에 성공을 보고했다. 기본값은 최신 롤아웃을 따라간다. --revision=N은 지정한 리비전을 감시하다가 다른 리비전으로 대체되면 중단하고, --watch=false는 현재 상태를 한 번 읽는다. CI가 실제로 확인한 리비전은 어느 것인가? 7만 감시하려면 어떤 명령을 쓰고, 지금 상태를 기다리지 않고 보려면 어떤 명령을 쓰는가?

**출처** · [Kubernetes command reference, kubectl rollout status](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_rollout/kubectl_rollout_status/)

### Standard

> CI는 최신 롤아웃을 따라가므로 리비전 8의 성공을 확인했습니다. 리비전 7만 감시하려면 `kubectl rollout status deployment/checkout-api --revision=7`을 쓰고, 현재 상태만 한 번 확인하려면 `kubectl rollout status deployment/checkout-api --watch=false`를 쓰면 됩니다.
