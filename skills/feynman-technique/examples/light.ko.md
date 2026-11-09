# DNS 응답이 리졸버마다 달라지는 이유

[English](light.md) · [standard](standard.ko.md) · [strict](strict.ko.md)

[질문과 출처](standard.ko.md#질문)

### Light

> NXDOMAIN은 `photos.example.org`에 해당 이름이 없다는 응답이다. 각 리졸버는 NXDOMAIN을 받은 시점부터 SOA TTL 240초와 SOA MINIMUM 600초 중 더 짧은 240초 동안 그 응답을 캐시에 둔다.
>
> Bay는 09:10에 NXDOMAIN을 받아 09:14에 캐시가 만료된다. Ridge는 09:12에 받아 09:16에 만료된다. 운영자가 A 레코드를 추가한 09:13 이후에도 두 캐시의 만료 시각은 바뀌지 않는다. 따라서 09:15 조회에서 Bay는 캐시가 만료되어 권한 서버에 물어보고 새 A 레코드를 받을 수 있지만, Ridge는 아직 캐시된 NXDOMAIN을 돌려줄 수 있다.
>
> Ridge는 09:16부터 새 레코드를 받아올 수 있다. 정확히 그 시각에는 기존 캐시가 만료되어 유효하지 않으며, 이후 도착하는 조회 요청은 갱신된 권한 서버에서 새 레코드를 확인할 수 있다.
