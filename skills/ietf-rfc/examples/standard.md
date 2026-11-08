# Specifying HTTP 429 for a rate-limited API

2026-11-08 · `ietf-rfc` 0.1.2 · English · Codex CLI 0.167.0 / gpt-6.1-sol

### Case and sources

- [IETF RFC 6585 §4, 429 Too Many Requests](https://www.rfc-editor.org/rfc/rfc6585.html#section-4). Sections 4 and 7.2 cover explanation, optional Retry-After, cache prohibition, deliberately unspecified counting and a server’s discretion to omit 429.
- [IETF RFC 9110 §10.2.3, Retry-After](https://www.rfc-editor.org/rfc/rfc9110.html#section-10.2.3). The field accepts an HTTP date or nonnegative integer delay in seconds after response receipt. The 120-second header is an illustration.

### Prompt

> Draft a short internal HTTP API specification (at most 95 words) using BCP 14 keywords. Explain how a client interprets the worked header Retry-After: 120 and whether a subsequent request is guaranteed to succeed. Under RFC 6585 §§4 and 7.2 a server can choose 429 for too many requests in a time interval. If sent, its content should explain the condition and it may include Retry-After. A cache must not store a 429 response. RFC 9110 §10.2.3 permits an HTTP date or a nonnegative delay in seconds measured after receipt of the response. State the keyword convention and distinguish server, client and cache roles. No identity scheme or rate-limiting algorithm is specified.

### Without a skill

> The keywords MUST, MUST NOT, SHOULD, and MAY are interpreted as described in BCP 14 (RFC 2119 and RFC 8174) when capitalized.
>
> A server MAY return 429 for too many requests within a time interval. Its content SHOULD explain the condition; it MAY include Retry-After.
>
> Retry-After accepts an HTTP date or nonnegative delay in seconds. For `Retry-After: 120`, the client SHOULD wait at least 120 seconds after receiving the response before retrying. Success is not guaranteed.
>
> A cache MUST NOT store a 429 response.
>
> No identity scheme or rate-limiting algorithm is specified.

### With the skill at standard

> Internal draft: HTTP rate limiting
>
> Uppercase keywords use BCP 14 meanings (RFC 2119; RFC 8174).
>
> A server MAY send 429 for too many requests within a time interval. Its content SHOULD explain the condition; it MAY include Retry-After. A cache MUST NOT store 429 responses.
>
> Clients interpret `Retry-After: 120` as a suggested 120-second delay after response receipt; subsequent success is not guaranteed. An HTTP date is also permitted.
>
> Security: identity and rate-limiting algorithms remain unspecified.
> IANA: no action.
>
> Normative references: RFC 6585 §§4, 7.2; RFC 9110 §10.2.3.

### What changed

**Checks set before the run.** Keep explanatory details at SHOULD, Retry-After optional (MAY), and cache storage prohibited (MUST NOT). Interpret 120 as seconds after receipt and do not guarantee that the subsequent request succeeds. Do not invent per-user counting rules.

Both final answers keep sending HTTP 429 optional, prohibit cache storage and count 120 seconds from receipt, without promising a successful retry. The baseline makes waiting a client SHOULD under BCP 14. The skill describes the suggested wait without adding that normative client requirement. The first treatment had incorrectly made sending 429 mandatory.

**차이.** 두 최종 답 모두 서버의 429 전송은 선택 사항이고 캐시는 응답을 저장하면 안 된다는 점을 지킵니다. 응답 수신 후 120초를 세되 재시도 성공을 보장하지도 않습니다. 미적용 답은 클라이언트 대기에 대문자 SHOULD를 추가했고, 스킬 답은 이를 권장 대기 시간으로 설명했습니다.

<details>
<summary>Earlier attempts on this case</summary>

The first treatment made sending a 429 mandatory. We clarified that choosing to send a message differs from the obligations on its contents. The new treatment preserved that condition but left the timer origin implicit. We then supplied the receipt-time fact in the final prompt and reran both arms.

**Attempt 1 — request**

> Draft an internal HTTP API specification of at most 95 words using BCP 14 keywords. Adopt RFC 6585 section 4: a 429 response reports too many requests in a time interval; its content should explain the condition, it may include Retry-After, and a cache must not store the response. RFC 9110 section 10.2.3 permits either an HTTP date or a nonnegative delay in seconds. For a worked header, use Retry-After: 120. Do not prescribe an identity scheme or rate-limiting algorithm. State the keyword convention and distinguish the server, client and cache roles.

**With the skill at standard**

> # Internal HTTP API Draft
>
> This specification defines rate-limit responses. Uppercase keywords use BCP 14 meanings (RFC 2119; RFC 8174).
>
> The server MUST use 429 to report too many requests in a time interval. Response content SHOULD explain the condition; the server MAY include `Retry-After`.
>
> Clients can interpret `Retry-After` as an HTTP date or nonnegative delay in seconds.
>
> Example: `Retry-After: 120`
>
> A cache MUST NOT store the response.
>
> Identity schemes and rate-limiting algorithms remain unspecified; abuse resistance remains unresolved.
>
> IANA: no action.
>
> Normative references: RFC 6585 §4; RFC 9110 §10.2.3.

**Attempt 2 — request**

> Draft an internal HTTP API specification of at most 95 words using BCP 14 keywords. Adopt RFC 6585 section 4: a 429 response reports too many requests in a time interval; its content should explain the condition, it may include Retry-After, and a cache must not store the response. RFC 9110 section 10.2.3 permits either an HTTP date or a nonnegative delay in seconds. For a worked header, use Retry-After: 120. Do not prescribe an identity scheme or rate-limiting algorithm. State the keyword convention and distinguish the server, client and cache roles.

**Without a skill**

> The keywords MUST, MUST NOT, SHOULD, and MAY are interpreted as described in BCP 14 when, and only when, they appear in uppercase.
>
> Server: A 429 (Too Many Requests) response indicates too many requests in a time interval. Its content SHOULD explain the condition. The server MAY include Retry-After, using either an HTTP date or a nonnegative delay in seconds.
>
> Worked header:
> ```http
> Retry-After: 120
> ```
>
> Client: The client SHOULD wait for the indicated interval before retrying.
>
> Cache: A cache MUST NOT store a 429 response.

**With the skill at standard**

> Internal draft: HTTP rate-limit responses.
>
> Uppercase keywords use BCP 14 meanings (RFC 2119; RFC 8174).
>
> A server MAY send 429 to report too many client requests within a time interval. Its content SHOULD explain the condition; it MAY include Retry-After. A cache MUST NOT store the response.
>
> Retry-After permits an HTTP date or nonnegative delay in seconds, interpreted by the client. Example:
> ```http
> Retry-After: 120
> ```
>
> Identity schemes and limiting algorithms remain unspecified.
> Security: abuse resistance remains unresolved.
> IANA: no action.
>
> Normative references: RFC 6585 §4; RFC 9110 §10.2.3.

</details>
