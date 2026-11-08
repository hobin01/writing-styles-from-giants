# Why two DNS resolvers disagree after a record is created

[한국어](standard.ko.md)

2026-11-08 · `feynman-technique` 0.1.3 · English · `gpt-6-luna`

### Case and sources

- [IETF RFC 2308, Negative Caching of DNS Queries](https://www.rfc-editor.org/rfc/rfc2308.html#section-5). Sections 3 and 5 explain the SOA-based lifetime and expiry of negative responses. The hostname, TTL values and clock times are a worked trace, not production DNS records.

### Prompt

> Two teams query uploads.example.org through independent DNS resolvers. In this illustrative trace, Harbor gets NXDOMAIN at 12:00 and Hill gets NXDOMAIN at 12:03. Both cache the name's absence. The zone's SOA TTL is 900 seconds and its MINIMUM is 300 seconds; RFC 2308 uses the smaller value for a negative answer. At 12:04 the operator creates the A record. At 12:06 both teams query again. In a short incident explanation for a junior developer, predict what each team can see, when the later cache expires, and what would change if Hill had not queried before 12:04. Assume a reachable, updated authority; no evictions, refreshes or local overrides. Do not ask the developer a question. Write your answer in English.

### Without the skill

> Harbor and Hill can both still see `NXDOMAIN` at 12:06. Under RFC 2308, the negative cache lifetime is the smaller of the SOA TTL (900 seconds) and SOA MINIMUM (300 seconds), so each resolver can cache the absence for 300 seconds from its own NXDOMAIN response.
>
> Harbor’s entry expires at **12:05**, and Hill’s at **12:08**. At 12:06, Harbor’s cache has expired, so its next query can reach the updated authority and return the A record. Hill’s cache is still valid, so Hill can still receive NXDOMAIN until 12:08; after that, its next query can return the A record.
>
> If Hill had not queried before 12:04, it would have no cached negative answer. Its first query after the A record was created could reach the authority and return the A record immediately.

### With the skill at standard

> Harbor’s NXDOMAIN at 12:00 is cached for 300 seconds: RFC 2308 uses the smaller of the SOA TTL (900 seconds) and MINIMUM (300 seconds). The cache stores that the name does not exist, so at 12:06 Harbor can still receive NXDOMAIN even though the operator added the A record at 12:04. Harbor’s negative cache expires at 12:05.
>
> Hill’s independent resolver starts its own 300-second timer from its NXDOMAIN at 12:03, so it can also receive NXDOMAIN at 12:06; that cache expires at 12:08. After each cache expires, a query can reach the updated authority and see the A record. If Hill had not queried before 12:04, it would have no cached NXDOMAIN, so its first query at 12:06 could reach the authority and return the A record.

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Computes the 300-second lifetime and the 12:05 Harbor and 12:08 Hill expirations from their own original queries. | Met | Met |
| At 12:06 Harbor can fetch the new address while Hill can still serve NXDOMAIN; creating the record did not restart or invalidate Hill's cached lifetime. | Missed | Missed |
| Explains for a junior developer why Hill with no earlier negative entry could fetch the new address at 12:06 under the stated assumptions, without implying a simultaneous global update. | Met | Met |

**Masked review** (X = baseline; Y = standard). Both derive 300 seconds, the 12:05 and 12:08 expirations, and Hill’s counterfactual. X initially says both resolvers can still return the cached negative answer at 12:06, then corrects itself for Harbor. Y says Harbor can still see NXDOMAIN at 12:06 even though it gives Harbor’s earlier expiration. Only Hill can reuse that negative entry.

<details>
<summary>Run record</summary>

Each arm was a separate ephemeral read-only Codex CLI 0.167.0 session with low reasoning effort. Neither session was given the other answer or an answer in the other language.

SHA-256 prefixes (entrypoint / baseline answer / standard answer): `9249d0cc1aa8` / `dae944fee0be` / `1f151137eb92`.

</details>
