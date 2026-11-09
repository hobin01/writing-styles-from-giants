# Interpreting two different HTTP 429 retry clocks

[한국어](light.ko.md) · [standard](standard.md) · [strict](strict.md)

[Question and sources](standard.md#question)

### Light

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
