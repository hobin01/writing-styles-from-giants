# 초록색 CI 결과는 어떤 Kubernetes 배포를 확인했을까?

[English](strict.md) · [light](light.ko.md) · [standard](standard.ko.md)

[질문과 출처](standard.ko.md#질문)

### Strict

> CI는 기본 동작에 따라 최신 롤아웃인 **리비전 8**의 완료를 확인했습니다. 리비전 7이 완료됐는지는 이 결과만으로 알 수 없습니다.
>
> - 리비전 7만 감시: `kubectl rollout status deployment/checkout-api --revision=7`
> - 현재 상태를 한 번만 확인: `kubectl rollout status deployment/checkout-api --watch=false`
