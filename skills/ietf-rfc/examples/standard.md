# Interpreting two different HTTP 429 retry clocks

[한국어](standard.ko.md)

2026-11-08 · `ietf-rfc` 0.1.3 · English · `gpt-6-luna`

### Case and sources

- [IETF RFC 6585 §4, 429 Too Many Requests](https://www.rfc-editor.org/rfc/rfc6585.html#section-4). Sections 4 and 7.2 cover explanation, optional Retry-After, cache prohibition, deliberately unspecified counting and a server’s discretion to omit 429.
- [IETF RFC 9110 §10.2.3, Retry-After](https://www.rfc-editor.org/rfc/rfc9110.html#section-10.2.3). The field accepts an HTTP date or nonnegative integer delay in seconds after response receipt. The response times and example header values in the exercise are illustrative.

### Prompt

> Write an internal API specification for two illustrative rate-limit responses. Both are sent at 09:00:00 UTC and received by the client at 09:00:05 UTC. The first has Retry-After: 45; the second has an HTTP date equivalent to 09:01:00 UTC that day. Assume synchronized clocks. Under RFC 6585 the server can choose 429, its content should explain the condition, Retry-After is optional, and caches cannot store a 429. RFC 9110 permits either an HTTP date or a nonnegative delay measured after receipt. Declare the BCP 14 keyword convention, give the client’s suggested retry time in each case, and say what neither time promises. Do not add a client obligation absent from the sources. Keep it concise. Write your answer in English.

### Without the skill

> ## Rate-limit responses
>
> This illustrative API may return **429 Too Many Requests** when a client exceeds its rate limit. The response content should explain the condition. The server may include `Retry-After`; it is optional. Caches **MUST NOT** store a 429 response.
>
> **BCP 14 convention:** The key words **MUST**, **MUST NOT**, **SHOULD**, and **MAY** are to be interpreted as described in BCP 14 only when they appear in all capitals.
>
> Both responses are sent at **09:00:00 UTC** and received at **09:00:05 UTC**. Assume synchronized clocks.
>
> | `Retry-After` value | Suggested retry time |
> |---|---|
> | `45` | **09:00:50 UTC** — 45 seconds after receipt |
> | HTTP date equivalent to **09:01:00 UTC** | **09:01:00 UTC** |
>
> Neither time promises that a retry will succeed or that the server will be available then.

### With the skill at standard

> ## Retry timing for illustrative rate-limit responses
>
> This internal specification covers the client’s suggested retry time for two illustrative HTTP 429 responses. The server chooses whether to send a 429 response; if it does, RFC 6585 says its content should explain the condition, `Retry-After` is optional, and caches cannot store the response. The examples assume synchronized clocks.
>
> In this specification, uppercase requirement keywords have their BCP 14 meanings (RFC 2119 and RFC 8174). **MUST** and **MAY** describe requirements and permissions; they do not add client behavior beyond the cited sources.
>
> In both examples, the server sends the response at 09:00:00 UTC and the client receives it at 09:00:05 UTC.
>
> - With `Retry-After: 45`, the value is a nonnegative delay measured after receipt. The client’s suggested retry time is **09:00:50 UTC**.
> - With `Retry-After` set to an HTTP date equivalent to **09:01:00 UTC** that day, the client’s suggested retry time is **09:01:00 UTC**.
>
> Neither time promises that a retry will succeed or that the rate limit will have cleared.
>
> **References.** RFC 6585 and RFC 9110 are normative for this behavior; RFC 2119 and RFC 8174 define the stated keyword convention. No IANA action is required.

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| States a BCP 14 convention and preserves optional server selection of 429, SHOULD explanatory content, optional Retry-After and the cache's MUST NOT store obligation. | Met | Met |
| Correctly computes 09:00:50 UTC for the 45-second delay after receipt and 09:01:00 UTC for the date value. | Met | Met |
| Frames those times as suggested waits rather than a new client MUST/SHOULD, and states that a retry is not guaranteed to succeed. | Met | Met |

**Masked review** (X = baseline; Y = standard). Both give the two times (09:00:50 and 09:01:00 UTC), preserve the server’s choice and retry semantics, and withhold any guarantee of success. X uses a table and an explicit cache MUST NOT. Y explains the cache prohibition in prose and supplies references. Both convey the content recommendation using lowercase “should,” rather than an uppercase BCP 14 keyword.

<details>
<summary>Run record</summary>

Each arm was a separate ephemeral read-only Codex CLI 0.167.0 session with low reasoning effort. Neither session was given the other answer or an answer in the other language.

SHA-256 prefixes (entrypoint / baseline answer / standard answer): `1613a9080cdb` / `0e16e6d9aec6` / `db3dd8aedeae`.

</details>
