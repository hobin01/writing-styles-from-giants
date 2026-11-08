# Should PostgreSQL add the orders index during this shift?

[한국어](standard.ko.md)

2026-11-08 · `google-design-doc` 0.1.2 · English · `gpt-6-luna`

### Case and sources

- [PostgreSQL 17 documentation, CREATE INDEX](https://www.postgresql.org/docs/17/sql-createindex.html#SQL-CREATEINDEX-CONCURRENTLY). Building Indexes Concurrently explains locking, table scans, waiting for transactions and invalid indexes after failure. The store, schema and decision are illustrative; no production benchmark is quoted.
- [PostgreSQL 17 system catalogs, pg_index](https://www.postgresql.org/docs/17/catalog-pg-index.html). The indisvalid field records whether the index is valid for queries. The rehearsal metrics and release threshold are illustrative.

### Prompt

> Write a design-review excerpt for an illustrative PostgreSQL 17 store. The team cannot block order INSERTs throughout an index build. Its separate release gate is a rehearsal p95 write latency no more than 20% above the 40 ms baseline. A concurrent-build rehearsal measured 51 ms. Ordinary CREATE INDEX blocks writes; CREATE INDEX CONCURRENTLY lets writes continue, scans the table twice and can wait for transactions. A failed concurrent run can leave an invalid index that planners ignore but writes still maintain. Recommend what to authorize this shift, what to measure before retrying and how to handle an invalid result. The store has not measured production performance. Keep it concise. Write your answer in English.

### Without the skill

> ### Design-review excerpt
>
> Authorize a **concurrent index build**: order INSERTs must continue, and ordinary `CREATE INDEX` blocks writes. `CREATE INDEX CONCURRENTLY` keeps writes running, though it scans the table twice and may wait for transactions.
>
> The rehearsal result **fails the separate latency gate**: 51 ms is 27.5% above the 40 ms baseline, exceeding the 20% limit of 48 ms. Before retrying, measure rehearsal p95 write latency and identify the main contributors, including concurrent write load, transaction duration, and build-related resource use. Production performance is unmeasured, so do not treat the rehearsal as a production estimate.
>
> If a concurrent build fails, check whether it left an invalid index. Planners ignore it, but writes still maintain it; remove the invalid index before retrying, then verify the rebuilt index is valid.

### With the skill at standard

> ## Illustrative PostgreSQL 17 index build
>
> **Proposal for review.** Authorize `CREATE INDEX CONCURRENTLY` for the build, subject to the separate latency gate. The team cannot block order inserts throughout the build. The concurrent-build rehearsal measured 51 ms p95 against a 40 ms baseline: 27.5% higher, above the 20% limit of 48 ms. The rehearsal therefore does not pass the release gate. Production performance has not been measured.
>
> **Behavior and trade-offs.** An ordinary `CREATE INDEX` blocks writes, so it conflicts with the insert constraint. `CREATE INDEX CONCURRENTLY` lets writes continue, but scans the table twice and can wait for transactions. If it fails, it can leave an invalid index: planners ignore it, but writes still maintain it.
>
> **Before retrying.** Measure rehearsal p95 write latency under the same conditions as the 40 ms baseline, and identify what drove the 51 ms result. Retry only when the rehearsal meets the 48 ms limit; the current result does not authorize release.
>
> **Invalid result.** Check the index’s validity after a failed concurrent build. If invalid, account for its write-maintenance cost and remove it before retrying the build.
>
> **Status.** This is a proposal for review. No approval or production-performance evidence is provided.

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Computes the 48 ms gate or the 27.5% increase and recognizes that the 51 ms concurrent rehearsal fails the allowed 20% increase. | Met | Met |
| Rejects an ordinary build during the shift because it blocks required INSERTs and holds the production rollout pending a passing new rehearsal; does not promise production latency. | Missed | Met |
| Gives a concrete review or recovery plan that checks validity and deals with an invalid index that still imposes write cost (for example, remove it and retry safely). | Met | Met |

**Masked review** (Y = baseline; X = standard). Both calculate a 48 ms ceiling and a 27.5% increase, explain why an ordinary build blocks required writes, and plan to inspect and remove an invalid index. X opens with conditional authorization and explicitly withholds production release until a new rehearsal passes. Y acknowledges the breach but opens by authorizing the concurrent build without limiting that authorization to rehearsal.

<details>
<summary>Run record</summary>

Each arm was a separate ephemeral read-only Codex CLI 0.167.0 session with low reasoning effort. Neither session was given the other answer or an answer in the other language.

SHA-256 prefixes (entrypoint / baseline answer / standard answer): `96fbdfc6834c` / `22613968a7c4` / `7e00af2b235a`.

</details>
