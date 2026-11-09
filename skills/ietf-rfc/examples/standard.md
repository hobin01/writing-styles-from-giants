# Interpreting two different HTTP 429 retry clocks

[한국어](standard.ko.md) · [light](light.md) · [strict](strict.md)

### Question

> Two HTTP 429 responses were sent at 09:00:00 UTC and received at 09:00:05 UTC. The first carried Retry-After: 45. The second contained an HTTP date for 09:01:00 UTC that day. The clocks agree. RFC 6585 permits a server to send 429 when a user sends too many requests in a period of time, recommends that the response explain the condition, permits Retry-After and forbids caches to store 429 responses. RFC 9110 allows Retry-After to be an HTTP date or a nonnegative number of seconds after receipt. What should the server, cache and client make of these responses? When would the client try again in each case, and what could still happen?

**Sources** · [IETF RFC 6585 §4, 429 Too Many Requests](https://www.rfc-editor.org/rfc/rfc6585.html#section-4) · [IETF RFC 9110 §10.2.3, Retry-After](https://www.rfc-editor.org/rfc/rfc9110.html#section-10.2.3)

### Standard

> ### Interpretation of the 429 responses
>
> RFC 6585 permits a server to send **429 Too Many Requests** when a user has sent too many requests in a period of time. It recommends that the response explain the condition. The server may include `Retry-After`. A cache is forbidden to store a 429 response.
>
> RFC 9110 defines `Retry-After` as either an HTTP date or a nonnegative number of seconds after receipt of the response. The client can use that value to determine when to try again.
>
> | Response | Client’s retry time |
> |---|---|
> | First: `Retry-After: 45`, received at 09:00:05 UTC | 09:00:50 UTC, 45 seconds after receipt |
> | Second: HTTP date 09:01:00 UTC, received at 09:00:05 UTC | 09:01:00 UTC |
>
> These are the times indicated by `Retry-After`; the client may still receive another 429 if the rate limit remains in effect. The second date is later than the first response’s indicated retry time. The two response values do not establish whether they came from the same rate-limit state or which retry time should govern requests other than the one associated with each response.
>
> The cache must not store either 429 response. The stated rules do not specify how a client should reconcile multiple retry instructions beyond interpreting each value according to its form.
>
> IANA applicability: these rules do not request an IANA action.
