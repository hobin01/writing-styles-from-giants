# Why two DNS resolvers disagree after a record is created

[한국어](standard.ko.md)

2026-11-09 · `feynman-technique` 0.1.8 · English · `gpt-6-luna`

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

> **Incident explanation (junior developer):** RFC 2308 sets the negative-cache lifetime to the smaller of the SOA TTL (900 seconds) and SOA MINIMUM (300 seconds), so each resolver can keep its own NXDOMAIN result for 300 seconds from when it received that answer. Harbor received NXDOMAIN at 12:00, so its entry expires at **12:05**. Hill received NXDOMAIN at 12:03, so its entry expires at **12:08**. The A record was created at 12:04, but that does not erase either resolver’s cached result. At 12:06, Harbor’s entry has expired and, with the authority reachable and updated, Harbor can see the A record; Hill’s entry is still valid, so Hill can still see NXDOMAIN until 12:08. If Hill had not queried before 12:04, it would have no negative entry to serve at 12:06 and could query the authority and see the A record. The two resolvers’ cache timers start independently when each receives NXDOMAIN.

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Computes the 300-second lifetime and the 12:05 Harbor and 12:08 Hill expirations from their own original queries. | Met | Met |
| At 12:06 Harbor can fetch the new address while Hill can still serve NXDOMAIN; creating the record did not restart or invalidate Hill's cached lifetime. | Missed | Met |
| Explains for a junior developer why Hill with no earlier negative entry could fetch the new address at 12:06 under the stated assumptions, without implying a simultaneous global update. | Met | Met |

**Review.** The two expirations come from different first queries. At 12:06 only Hill can still reuse its negative entry; without that earlier query, Hill could fetch the new address.

Masked reviewer assignment: X was the revised answer. The table retains the original control grades. [Previous pair and scores](https://github.com/hobin01/writing-styles-from-giants/blob/20f24c66c7e89e6ce1007249c83c33932998bf01/skills/feynman-technique/examples/standard.md) · [All attempts and adjudications](https://github.com/hobin01/writing-styles-from-giants/blob/main/evals/runs/2026-11-09-standard/records/feynman-technique.json).

<details>
<summary>Run record</summary>

Baseline generated 2026-11-08. Revised treatment generated independently on 2026-11-09 with Codex CLI 0.167.0, low reasoning, in a fresh read-only session. SHA-256 prefixes (entrypoint / original baseline / revised answer): `5527bddea967` / `dae944fee0be` / `e3260298686a`.

</details>
