# Interpreting two different HTTP 429 retry clocks

[한국어](standard.ko.md)

2026-11-09 · `ietf-rfc` 0.1.10 · English · `gpt-6-luna`

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

> # Rate-Limit Response Examples
>
> **Status:** Internal illustrative specification.
>
> ## Scope and terminology
>
> This specification covers two illustrative HTTP 429 responses and the client’s suggested retry times. “Receipt” means receipt by the client. Clocks are assumed synchronized.
>
> ## Requirements
>
> The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** are to be interpreted as described in BCP 14 (RFC 2119 and RFC 8174) when, and only when, they appear in uppercase.
>
> | Actor | BCP 14 | Behavior and condition |
> |---|---|---|
> | Server | MAY | Choose status code 429 to indicate that the client has sent too many requests in a given amount of time. |
> | Server | SHOULD | Include a response representation that explains the condition. |
> | Server | MAY | Include `Retry-After` in a 429 response. |
> | Cache | MUST NOT | Store a 429 response. |
>
> ## Suggested retry times
>
> RFC 9110 allows `Retry-After` to contain either an HTTP date or a nonnegative delay in seconds measured after receipt. In both examples, the response is sent at 09:00:00 UTC and received at 09:00:05 UTC.
>
> - With `Retry-After: 45`, the suggested retry time is **09:00:50 UTC** (45 seconds after receipt).
> - With `Retry-After` set to an HTTP date equivalent to **09:01:00 UTC** that day, the suggested retry time is **09:01:00 UTC**.
>
> Neither time promises that the rate limit will have cleared or that a subsequent request will succeed. The client has no retry obligation specified here.
>
> ## References
>
> **Normative:** RFC 6585 (429 responses); RFC 9110 (`Retry-After` formats). RFC 2119 and RFC 8174 define BCP 14 keyword meanings.
>
> **IANA:** No IANA action applies to these examples.

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| States a BCP 14 convention and preserves optional server selection of 429, SHOULD explanatory content, optional Retry-After and the cache's MUST NOT store obligation. | Met | Met |
| Correctly computes 09:00:50 UTC for the 45-second delay after receipt and 09:01:00 UTC for the date value. | Met | Met |
| Frames those times as suggested waits rather than a new client MUST/SHOULD, and states that a retry is not guaranteed to succeed. | Met | Met |

**Review.** The specification keeps each requirement with its actor. The two retry times are 09:00:50 and 09:01:00 UTC; neither obliges the client to retry or promises success.

Masked reviewer assignment: Y was the revised answer. The table retains the original control grades. [Previous pair and scores](https://github.com/hobin01/writing-styles-from-giants/blob/20f24c66c7e89e6ce1007249c83c33932998bf01/skills/ietf-rfc/examples/standard.md) · [All attempts and adjudications](https://github.com/hobin01/writing-styles-from-giants/blob/main/evals/runs/2026-11-09-standard/records/ietf-rfc.json).

<details>
<summary>Run record</summary>

Baseline generated 2026-11-08. Revised treatment generated independently on 2026-11-09 with Codex CLI 0.167.0, low reasoning, in a fresh read-only session. SHA-256 prefixes (entrypoint / original baseline / revised answer): `a03848dad0d2` / `0e16e6d9aec6` / `18eb49ccc918`.

</details>
