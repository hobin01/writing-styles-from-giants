# Interpreting two different HTTP 429 retry clocks

[한국어](light.ko.md) · **light** · [standard](standard.md) · [strict](strict.md)

### Question

> Two HTTP 429 responses were sent at 09:00:00 UTC and received at 09:00:05 UTC. The first carried Retry-After: 45. The second contained an HTTP date for 09:01:00 UTC that day. The clocks agree. RFC 6585 permits a server to send 429 when a user sends too many requests in a period of time, recommends that the response explain the condition, permits Retry-After and forbids caches to store 429 responses. RFC 9110 allows Retry-After to be an HTTP date or a nonnegative number of seconds after receipt. What should the server, cache and client make of these responses? When would the client try again in each case, and what could still happen?

**Sources** · [IETF RFC 6585 §4, 429 Too Many Requests](https://www.rfc-editor.org/rfc/rfc6585.html#section-4) · [IETF RFC 9110 §10.2.3, Retry-After](https://www.rfc-editor.org/rfc/rfc9110.html#section-10.2.3)

### With the skill

> ### Scope and roles
>
> This interpretation covers two HTTP 429 responses sent by a server and received by a client. The clocks agree. The server sent both responses at 09:00:00 UTC; the client received both at 09:00:05 UTC. The first carried `Retry-After: 45`; the second carried an HTTP date of 09:01:00 UTC that day.
>
> ### Server and cache
>
> RFC 6585 permits the server to send 429 when a user has sent too many requests in a period of time. It recommends that the response explain the condition. The server may include `Retry-After`.
>
> A cache must not store a 429 response.
>
> ### Client
>
> RFC 9110 permits `Retry-After` to contain either an HTTP date or a nonnegative number of seconds after receipt. The two values therefore indicate different retry times:
>
> - For `Retry-After: 45`, the client’s retry time is 45 seconds after receipt: 09:00:50 UTC.
> - For the HTTP date `09:01:00 UTC`, the client’s retry time is that stated date and time: 09:01:00 UTC.
>
> These are suggested retry times, not guarantees that a retry will succeed. The client could still receive another 429 or another response.

### Without the skill

> The server has returned two valid indications of when to retry. RFC 9110 allows `Retry-After` to be either a delay in seconds or an HTTP date. The two responses therefore give:
>
> - **First response:** `45` seconds after receipt at 09:00:05 UTC, so the client should wait until **09:00:50 UTC**.
> - **Second response:** the date **09:01:00 UTC**, so the client should wait until that time.
>
> The client should treat each response on its own; the values are not cumulative. A 429 signals rate limiting, and the server should explain the condition when practical. It may use `Retry-After` to guide the client, but the header does not guarantee that a retry will succeed: the client could still be rate limited or receive another 429.
>
> A cache **must not store either 429 response**. That restriction does not prevent the client from receiving the responses or acting on their retry guidance.
