# 초록색 CI 결과는 어떤 Kubernetes 배포를 확인했을까?

[English](light.md) · [standard](standard.ko.md) · [strict](strict.ko.md)

[질문과 출처](standard.ko.md#질문)

### Light

> CI가 확인한 것은 리비전 8입니다. 기본 동작이 최신 롤아웃을 따라가므로 리비전 7이 끝나기 전에 8이 시작된 뒤, 명령은 8의 완료를 기다려 성공을 보고했습니다.
>
> - 리비전 7만 감시: `kubectl rollout status deployment/checkout-api --revision=7`
> - 기다리지 않고 현재 상태 한 번 읽기: `kubectl rollout status deployment/checkout-api --watch=false`
