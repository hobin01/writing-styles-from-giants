# Interpreting two different HTTP 429 retry clocks

[한국어](strict.ko.md) · [light](light.md) · [standard](standard.md)

[Question and sources](standard.md#question)

### Strict

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
