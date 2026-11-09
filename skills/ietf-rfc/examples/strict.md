# Interpreting two different HTTP 429 retry clocks

[한국어](strict.ko.md) · [light](light.md) · [standard](standard.md) · **strict**

### Question

> Two HTTP 429 responses were sent at 09:00:00 UTC and received at 09:00:05 UTC. The first carried Retry-After: 45. The second contained an HTTP date for 09:01:00 UTC that day. The clocks agree. RFC 6585 permits a server to send 429 when a user sends too many requests in a period of time, recommends that the response explain the condition, permits Retry-After and forbids caches to store 429 responses. RFC 9110 allows Retry-After to be an HTTP date or a nonnegative number of seconds after receipt. What should the server, cache and client make of these responses? When would the client try again in each case, and what could still happen?

**Sources** · [IETF RFC 6585 §4, 429 Too Many Requests](https://www.rfc-editor.org/rfc/rfc6585.html#section-4) · [IETF RFC 9110 §10.2.3, Retry-After](https://www.rfc-editor.org/rfc/rfc9110.html#section-10.2.3)

### With the skill

> ## Interpretation of the 429 responses
>
> This interpretation applies RFC 6585’s HTTP 429 behavior and RFC 9110’s `Retry-After` semantics to the two responses. The actors are the server that sends the responses, any cache that handles them, and the client that receives them. The clocks agree.
>
> ### Server
>
> - When a user sends too many requests within a period of time, the server may send a 429 response.
> - When sending a 429 response, the server is recommended to explain the condition.
> - The server may include `Retry-After` in a 429 response.
>
> ### Cache
>
> - A cache is forbidden to store a 429 response.
>
> ### Client
>
> - When `Retry-After` contains a nonnegative number of seconds, the client interprets it as a duration after receipt of the response.
> - When `Retry-After` contains an HTTP date, the client interprets it as the time indicated by that date.
>
> ### Response times and retry times
>
> | Response | Sent | Received | `Retry-After` | Client’s indicated retry time |
> |---|---|---|---|---|
> | First | 09:00:00 UTC | 09:00:05 UTC | `45` seconds | 09:00:50 UTC |
> | Second | 09:00:00 UTC | 09:00:05 UTC | HTTP date: 09:01:00 UTC that day | 09:01:00 UTC |
>
> The first value is relative to receipt, so the client adds 45 seconds to 09:00:05. The second value is an absolute time; the client uses 09:01:00 UTC unchanged. Both indicated times are after the responses were received.
>
> `Retry-After` indicates when to try again; it does not guarantee that a later request will succeed. The server could still send another 429 if the client retries while the rate condition persists.

### Without the skill

> The server has returned two valid indications of when to retry. RFC 9110 allows `Retry-After` to be either a delay in seconds or an HTTP date. The two responses therefore give:
>
> - **First response:** `45` seconds after receipt at 09:00:05 UTC, so the client should wait until **09:00:50 UTC**.
> - **Second response:** the date **09:01:00 UTC**, so the client should wait until that time.
>
> The client should treat each response on its own; the values are not cumulative. A 429 signals rate limiting, and the server should explain the condition when practical. It may use `Retry-After` to guide the client, but the header does not guarantee that a retry will succeed: the client could still be rate limited or receive another 429.
>
> A cache **must not store either 429 response**. That restriction does not prevent the client from receiving the responses or acting on their retry guidance.
