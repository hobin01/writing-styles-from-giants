# Why two DNS resolvers disagree after a record is created

2026-11-08 · `feynman-technique` 0.1.2 at first pass · `gpt-6-luna` · Codex CLI 0.167.0

### Case and sources

- [IETF RFC 2308, Negative Caching of DNS Queries](https://www.rfc-editor.org/rfc/rfc2308.html#section-5). Sections 3 and 5 explain the SOA-based lifetime and expiry of negative responses. The hostname, TTL values and clock times are a worked trace, not production DNS records.

**Reasoning task.** Reason from the minimum of two lifetimes and two independent cache insertion times, then change one initial condition while holding the DNS change fixed.

### Prompt

> Two teams query uploads.example.org through independent DNS resolvers. In this illustrative trace, Harbor gets NXDOMAIN at 12:00 and Hill gets NXDOMAIN at 12:03. Both cache the name's absence. The zone's SOA TTL is 900 seconds and its MINIMUM is 300 seconds; RFC 2308 uses the smaller value for a negative answer. At 12:04 the operator creates the A record. At 12:06 both teams query again. In a short incident explanation for a junior developer, predict what each team can see, when the later cache expires, and what would change if Hill had not queried before 12:04. Assume a reachable, updated authority; no evictions, refreshes or local overrides. Do not ask the developer a question.

### Without a skill

> Harbor and Hill can still see the cached NXDOMAIN at 12:06, even though the A record was created at 12:04. Their resolvers cached the name’s absence for the smaller of the SOA TTL (900 seconds) and MINIMUM (300 seconds), so each negative cache entry lasts 300 seconds from its own NXDOMAIN response.
>
> Harbor’s entry expires at 12:05; Hill’s expires at 12:08. At 12:06, Harbor’s resolver can query the updated authority and return the A record, while Hill’s can still return NXDOMAIN. Once Hill’s entry expires at 12:08, its next query can also retrieve the A record.
>
> If Hill had not queried before 12:04, it would have no cached NXDOMAIN. Its first query after the record was created could reach the updated authority and return the A record immediately.

### With the skill at standard

> ### Incident explanation
>
> Harbor and Hill use independent resolvers, so each resolver caches its own answer. Under RFC 2308, the negative-cache TTL is the smaller of the SOA TTL and SOA MINIMUM: **300 seconds** here.
>
> - **Harbor** cached NXDOMAIN at 12:00. Its negative entry expires at **12:05**.
> - **Hill** cached NXDOMAIN at 12:03. Its entry expires at **12:08**.
>
> The operator added the A record at 12:04, but that does not erase either resolver’s cached NXDOMAIN. At 12:06, Harbor’s entry has expired, so—given the reachable, updated authority—it can resolve the new record. Hill’s entry is still valid, so Hill can still get NXDOMAIN until **12:08**. After it expires, Hill can query the authority and see the record.
>
> If Hill had not queried before 12:04, it would have no negative entry to reuse. At 12:06, it could query the updated authority and see the A record immediately. The difference is each resolver’s cache start time: Hill’s pre-change query started its own 300-second negative-cache period.

### First-pass assessment

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Computes the 300-second lifetime and the 12:05 Harbor and 12:08 Hill expirations from their own original queries. | Met | Met |
| At 12:06 Harbor can fetch the new address while Hill can still serve NXDOMAIN; creating the record did not restart or invalidate Hill's cached lifetime. | Missed | Met |
| Explains for a junior developer why Hill with no earlier negative entry could fetch the new address at 12:06 under the stated assumptions, without implying a simultaneous global update. | Met | Met |

Both compute 12:05 and 12:08 and explain the no-prior-query counterfactual. The baseline opens by saying both resolvers can serve cached NXDOMAIN at 12:06, contradicting its own correct Harbor calculation and later explanation. The skill answer consistently says only Hill's negative entry is still valid.

**차이.** 두 답 모두 12:05와 12:08이라는 만료 시각과 사전 조회가 없을 때의 결과를 구했습니다. 미적용 답 첫 문장은 12:06에도 양쪽 모두 캐시된 NXDOMAIN을 볼 수 있다고 써서 뒤의 정확한 계산과 충돌합니다. 스킬 답은 그때 Hill의 음성 캐시만 유효하다고 일관되게 설명합니다.

<details>
<summary>Developmental retest · version 0.1.3</summary>

Keep the mechanism, exception and worked prediction within the requested format. This retest is excluded from the first-pass counts.

The request and original baseline are unchanged.

**New standard answer**

> An NXDOMAIN reply caches that the name does not exist. Under RFC 2308, the negative-cache lifetime here is the smaller of the SOA TTL and MINIMUM: 300 seconds (5 minutes). Harbor’s cache expires at 12:05, five minutes after its 12:00 reply; Hill’s expires at 12:08, five minutes after its 12:03 reply. So at 12:06, Harbor can see the new A record from the updated authority, while Hill can still see its cached NXDOMAIN until 12:08. If Hill had not queried before the record was created, it would have no cached negative answer and could see the A record on its first query after 12:04.
>
> **Method/status:** Feynman-inspired explanation, standard level. This is a prediction from the stated trace and assumptions; no learner response was assessed.

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Computes the 300-second lifetime and the 12:05 Harbor and 12:08 Hill expirations from their own original queries. | Met | Met |
| At 12:06 Harbor can fetch the new address while Hill can still serve NXDOMAIN; creating the record did not restart or invalidate Hill's cached lifetime. | Missed | Met |
| Explains for a junior developer why Hill with no earlier negative entry could fetch the new address at 12:06 under the stated assumptions, without implying a simultaneous global update. | Met | Met |

The skill answer and the baseline derive five-minute negative-cache lifetimes and expiries of 12:05 for Harbor and 12:08 for Hill. Both explain why Hill could fetch the address without an earlier negative entry. The skill answer gives a consistent prediction, then adds a visible Feynman method/level status. The baseline first says both resolvers can still serve cached NXDOMAIN at 12:06, contradicting its own later, correct statement that Harbor’s entry has already expired.

**차이.** 스킬 답과 미적용 답은 모두 음성 캐시 수명을 5분으로 계산하고 Harbor와 Hill의 만료 시각을 각각 12:05와 12:08로 제시한다. Hill이 앞서 부정 응답을 받지 않았다면 새 주소를 조회할 수 있는 이유도 설명한다. 스킬 답의 예측은 일관되지만 끝에 파인만 방법과 적용 수준을 표시한다. 미적용 답은 처음에 12:06에 두 리졸버 모두 캐시된 NXDOMAIN을 반환할 수 있다고 써서, 뒤에서 Harbor의 항목이 이미 만료됐다고 한 설명과 모순된다.

</details>
