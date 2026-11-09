# DNS 응답이 리졸버마다 달라지는 이유

[English](standard.md) · [light](light.ko.md) · [strict](strict.ko.md)

### 질문

> 서로 독립적으로 동작하는 DNS 리졸버 두 대가 photos.example.org를 조회했다. Bay는 09:10에, Ridge는 09:12에 NXDOMAIN 응답을 받았다. 각 리졸버는 SOA TTL(240초)과 SOA MINIMUM(600초) 중 작은 값만큼 그 응답을 캐시에 보관한다. 운영자는 09:13에 A 레코드를 추가했다. 09:15에 두 리졸버가 다시 조회 요청을 받았다. 갱신된 권한 서버에 접속할 수 있고, 조기 삭제나 갱신 또는 로컬 설정에 의한 응답 대체는 없다. 두 클라이언트가 왜 다른 응답을 받을 수 있고, Ridge는 언제부터 새 레코드를 받아올 수 있을까?

**출처** · [IETF RFC 2308, Negative Caching of DNS Queries](https://www.rfc-editor.org/rfc/rfc2308.html#section-5)

### Standard

> NXDOMAIN은 **`photos.example.org`라는 이름 자체가 존재하지 않는다**는 응답이다. 두 리졸버는 각자 받은 부정 응답을 독립적으로 캐시에 보관하므로, 만료 시각도 다르다. 보관 시간은 SOA TTL 240초와 SOA MINIMUM 600초 중 작은 값인 240초다.
>
> Bay는 09:10에 응답을 받아 09:14에 캐시가 만료된다. Ridge는 09:12에 받아 09:16에 만료된다. 운영자가 09:13에 A 레코드를 추가해 권한 서버가 갱신됐더라도, 이미 받은 응답의 캐시 시간은 바뀌지 않는다. 따라서 09:15 요청에서 Bay는 만료된 캐시를 버리고 권한 서버를 조회해 새 레코드를 받을 수 있지만, Ridge는 아직 유효한 NXDOMAIN 캐시를 사용해 이름이 없다고 답할 수 있다.
>
> Ridge의 기존 NXDOMAIN 캐시는 09:16에 만료된다. 그 시각 이후 새 조회가 권한 서버에 도달하면 A 레코드를 받아올 수 있다. 09:16보다 앞선 요청은 여전히 캐시된 NXDOMAIN을 받을 수 있고, 정확히 09:16에는 캐시가 만료된 상태다.
