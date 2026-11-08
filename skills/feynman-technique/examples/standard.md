# Why a new DNS name can still return NXDOMAIN

2026-11-08 · `feynman-technique` 0.1.2 · English · Codex CLI 0.167.0 / gpt-6.1-sol

### Case and sources

- [IETF RFC 2308, Negative Caching of DNS Queries](https://www.rfc-editor.org/rfc/rfc2308.html#section-5). Sections 3 and 5 explain the SOA-based lifetime and expiry of negative responses. The hostname, TTL values and clock times are a worked trace, not production DNS records.

### Prompt

> Explain this DNS rollout to a developer in one short paragraph. In this worked example a recursive resolver looks up uploads.example.org at 12:00:00, receives NXDOMAIN (the name does not exist), and caches it. In the zone, the SOA record has a TTL of 900 seconds and a MINIMUM of 300 seconds; RFC 2308 uses the smaller value for the negative cache lifetime. At 12:01:00 the operator creates an A record for that name. What can the same resolver return at 12:02:00, and when does this cached answer expire? Assume no early eviction, refresh or local override; the authoritative server remains reachable. The clock times and record are illustrative.

### Without a skill

> The resolver caches the NXDOMAIN response for 300 seconds—the smaller of the SOA TTL (900 seconds) and MINIMUM (300 seconds). Creating the A record at 12:01:00 does not invalidate that cached response, so at 12:02:00 the same resolver can still return NXDOMAIN. The cached negative answer expires at 12:05:00, after which a new lookup can retrieve the A record from the authoritative server.

### With the skill at standard

> A recursive resolver caches DNS answers, including NXDOMAIN (“the name does not exist”). Here, RFC 2308 sets the negative cache lifetime to the smaller of the SOA TTL (900 seconds) and MINIMUM (300 seconds), so the NXDOMAIN cached at 12:00:00 lasts until 12:05:00. Creating the A record at 12:01:00 does not invalidate that resolver’s cached answer: at 12:02:00 it can still return NXDOMAIN, with 180 seconds remaining. Under the stated assumptions, the cached answer expires at 12:05:00; a subsequent lookup can query the reachable authoritative server and obtain the new A record.

### What changed

**Checks set before the run.** Compute a 300-second lifetime starting at 12:00, not at the record change. A cached NXDOMAIN can persist at 12:02; it expires at 12:05. Expiration permits a fresh lookup rather than proving that all resolvers update simultaneously.

Both answers start the 300-second lifetime when the resolver receives NXDOMAIN, retain the 12:02 negative response and calculate the 12:05 expiry. The skill answer also gives the 180 seconds left at 12:02. Both describe a later lookup rather than promising that all resolvers change together.

**차이.** 두 답 모두 12시 1분에 레코드를 추가해도 12시 2분에는 이전 NXDOMAIN을 돌려줄 수 있고, 캐시는 12시 5분에 만료된다고 설명합니다. 스킬 답은 12시 2분에 남은 시간이 180초라는 계산까지 보여 줍니다.
