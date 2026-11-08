# Interpreting two different HTTP 429 retry clocks

2026-11-08 · `ietf-rfc` 0.1.2 at first pass · `gpt-6-luna` · Codex CLI 0.167.0

### Case and sources

- [IETF RFC 6585 §4, 429 Too Many Requests](https://www.rfc-editor.org/rfc/rfc6585.html#section-4). Sections 4 and 7.2 cover explanation, optional Retry-After, cache prohibition, deliberately unspecified counting and a server’s discretion to omit 429.
- [IETF RFC 9110 §10.2.3, Retry-After](https://www.rfc-editor.org/rfc/rfc9110.html#section-10.2.3). The field accepts an HTTP date or nonnegative integer delay in seconds after response receipt. The response times and example header values in the exercise are illustrative.

**Reasoning task.** Distinguish a duration measured from response receipt from an absolute timestamp while preserving separate optional and mandatory actions for servers and caches.

### Prompt

> Write an internal API specification for two illustrative rate-limit responses. Both are sent at 09:00:00 UTC and received by the client at 09:00:05 UTC. The first has Retry-After: 45; the second has an HTTP date equivalent to 09:01:00 UTC that day. Assume synchronized clocks. Under RFC 6585 the server can choose 429, its content should explain the condition, Retry-After is optional, and caches cannot store a 429. RFC 9110 permits either an HTTP date or a nonnegative delay measured after receipt. Declare the BCP 14 keyword convention, give the client’s suggested retry time in each case, and say what neither time promises. Do not add a client obligation absent from the sources. Limit the specification to 125 words.

### Without a skill

> ## Rate-limit responses
>
> This specification uses the BCP 14 keywords **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHALL NOT**, **SHOULD**, **SHOULD NOT**, **RECOMMENDED**, **NOT RECOMMENDED**, **MAY**, and **OPTIONAL** as described in RFC 2119 and RFC 8174, only when they appear in all capitals.
>
> A server **MAY** respond to a rate-limited request with `429 Too Many Requests`. The response content **SHOULD** explain the condition. `Retry-After` is **OPTIONAL**. A `429` response **MUST NOT** be stored by a cache.
>
> `Retry-After` **MAY** contain a nonnegative delay, measured after the client receives the response, or an HTTP date.
>
> For both examples, the response is sent at 09:00:00 UTC and received at 09:00:05 UTC; clocks are synchronized.
>
> - `Retry-After: 45` suggests retrying at **09:00:50 UTC**.
> - An HTTP date of **09:01:00 UTC** suggests retrying at **09:01:00 UTC**.
>
> Neither suggested time promises that retrying then will succeed.

### With the skill at standard

> # Rate-Limit Response Examples
>
> **Status:** Internal illustrative specification. It does not define a new protocol.
>
> ## Abstract
>
> This specification gives two illustrative HTTP 429 responses and the client’s suggested retry times.
>
> ## Specification
>
> The server MAY choose status code 429 (Too Many Requests). Its content SHOULD explain the rate-limit condition. The server MAY include `Retry-After`. A cache MUST NOT store a 429 response.
>
> In this specification, uppercase **MUST**, **MUST NOT**, **SHOULD**, and **MAY** have their BCP 14 meanings (RFC 2119 and RFC 8174).
>
> Assume synchronized clocks. Both responses are sent at 09:00:00 UTC and received at 09:00:05 UTC.
>
> - With `Retry-After: 45`, the suggested retry time is 09:00:50 UTC: 45 seconds after receipt.
> - With `Retry-After` set to an HTTP date equivalent to 09:01:00 UTC that day, the suggested retry time is 09:01:00 UTC.
>
> Neither time promises that a retry will succeed or that the rate limit will have cleared. These examples create no client retry obligation.
>
> ## Security Considerations
>
> These examples do not establish that a retry is safe or successful.
>
> ## IANA Considerations
>
> This internal specification requires no IANA action.
>
> ## References
>
> **Normative:** RFC 6585; RFC 9110; RFC 2119; RFC 8174.

### First-pass assessment

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| States a BCP 14 convention and preserves optional server selection of 429, SHOULD explanatory content, optional Retry-After and the cache's MUST NOT store obligation. | Met | Met |
| Correctly computes 09:00:50 UTC for the 45-second delay after receipt and 09:01:00 UTC for the date value. | Met | Met |
| Frames those times as suggested waits rather than a new client MUST/SHOULD, and states that a retry is not guaranteed to succeed. | Met | Met |

Both get the relative delay and date right (09:00:50 and 09:01:00 UTC), distinguish server choice from cache prohibition, and avoid promising success. Both exceed the requested 125 words by a whitespace count; that length limit is outside the three scored checks. The skill answer adds an abstract, security, IANA and reference sections; the baseline spends part of its budget listing the BCP 14 vocabulary.

**차이.** 두 답 모두 09:00:50과 09:01:00을 구분하고 서버의 선택권과 캐시 저장 금지를 보존합니다. 두 답 모두 세 채점 항목 밖의 125단어 제한은 넘겼습니다. 스킬 답은 초록·보안·IANA·참고문헌 절을 추가했고, 미적용 답은 BCP 14 용어를 길게 나열했습니다.

<details>
<summary>Developmental retest · version 0.1.3</summary>

Use only the structure needed for the requested specification excerpt and its word budget. This retest is excluded from the first-pass counts.

The request and original baseline are unchanged.

**New standard answer**

> ### Internal API specification: Illustrative 429 responses
>
> This internal specification covers two illustrative rate-limit responses. The server may choose status code 429. If it sends 429, its content should explain the condition; it may include `Retry-After`. Caches cannot store a 429.
>
> Uppercase requirement keywords have their BCP 14 meanings (RFC 2119 and RFC 8174).
>
> `Retry-After` may contain an HTTP date or a nonnegative delay in seconds measured after receipt (RFC 9110). With synchronized clocks, for a response sent at 09:00:00 UTC and received at 09:00:05 UTC:
>
> - `Retry-After: 45` suggests 09:00:50 UTC.
> - An HTTP date equivalent to 09:01:00 UTC suggests 09:01:00 UTC.
>
> Neither time promises that a retry will succeed or that the service will be available.
>
> **Security considerations:** No additional security consequences are specified.\
> **IANA:** No IANA action is specified.\
> **References:** Normative: RFC 6585, RFC 9110. BCP 14: RFC 2119, RFC 8174.

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| States a BCP 14 convention and preserves optional server selection of 429, SHOULD explanatory content, optional Retry-After and the cache's MUST NOT store obligation. | Met | Met |
| Correctly computes 09:00:50 UTC for the 45-second delay after receipt and 09:01:00 UTC for the date value. | Met | Met |
| Frames those times as suggested waits rather than a new client MUST/SHOULD, and states that a retry is not guaranteed to succeed. | Met | Met |

The skill answer and the baseline both declare a BCP 14 convention and preserve server choice, recommended explanatory content, an optional header and the prohibition on caching. The skill answer uses lowercase prose for those rules; the baseline applies its uppercase convention directly. Both suggest 09:00:50 UTC from receipt and 09:01:00 UTC from the date, without imposing a retry obligation or promising success. Both exceed 125 words, including the skill answer’s extra end matter and the baseline’s list of keywords.

**차이.** 스킬 답과 미적용 답 모두 BCP 14 표기 규칙을 선언하고, 상태 코드 선택과 헤더는 선택 사항, 사유 설명은 권고 사항, 캐시 저장은 금지 사항으로 전달한다. 스킬 답은 실제 규칙을 소문자 일반 문장으로 쓰고 미적용 답은 선언한 대문자 키워드를 직접 쓴다. 둘 다 수신 시각 기준 09:00:50 UTC와 날짜값 기준 09:01:00 UTC를 권장 시점으로 제시하며 재시도 의무나 성공을 보장하지 않는다. 스킬 답의 부록과 미적용 답의 키워드 목록을 포함해 두 답 모두 125단어를 넘긴다.

</details>
