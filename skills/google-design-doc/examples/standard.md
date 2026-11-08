# Adding a PostgreSQL index while orders are still arriving

2026-11-08 · `google-design-doc` 0.1.1 · English · Codex CLI 0.167.0 / gpt-6.1-sol

### Case and sources

- [PostgreSQL 17 documentation, CREATE INDEX](https://www.postgresql.org/docs/17/sql-createindex.html#SQL-CREATEINDEX-CONCURRENTLY). Building Indexes Concurrently explains locking, table scans, waiting for transactions and invalid indexes after failure. The store, schema and decision are illustrative; no production benchmark is quoted.
- [PostgreSQL 17 system catalogs, pg_index](https://www.postgresql.org/docs/17/catalog-pg-index.html). The indisvalid field confirms the baseline’s suggested validity check. This catalog reference was checked after the runs.

### Prompt

> Write a design-review excerpt of at most 130 words for an illustrative online store on PostgreSQL 17. Its unpartitioned orders table keeps receiving INSERTs; the requirement is that an index build must not block those writes for the duration of the build. Compare ordinary CREATE INDEX on customer_id with CREATE INDEX CONCURRENTLY. The ordinary build blocks table writes; the concurrent build permits them but scans the table twice and waits for relevant transactions. Failure can leave an invalid index that queries ignore but writes still maintain. Recommend one path and name a rollout check. The store has measured neither build time nor order-write latency.

### Without a skill

> For this illustrative store on PostgreSQL 17, ordinary `CREATE INDEX ON orders (customer_id)` blocks table writes during the build, violating the requirement to keep accepting order INSERTs.
>
> Recommend `CREATE INDEX CONCURRENTLY ON orders (customer_id)`. It permits writes during construction, but scans the table twice and waits for relevant transactions. It can still increase resource use and affect write latency; the store has measured neither build time nor order-write latency, so neither should be promised.
>
> A failed concurrent build can leave an invalid index that queries ignore but writes still maintain. As a rollout check, verify `pg_index.indisvalid` before declaring success, and monitor order-write latency during the build.

### With the skill at standard

> Proposal for review: use `CREATE INDEX CONCURRENTLY` on `orders(customer_id)` in PostgreSQL 17. The requirement is to keep accepting INSERTs throughout the build.
>
> Ordinary `CREATE INDEX` blocks table writes for the build’s duration, so it fails this requirement. The concurrent build permits INSERTs but scans the table twice and waits for relevant transactions. An incoming order can therefore be inserted while the index builds, although its write latency has not been measured.
>
> If the concurrent build fails, it can leave an invalid index: queries ignore it, but writes still maintain it. Before rollout completion, verify index validity and investigate any invalid index.
>
> Approval remains pending. The store has measured neither build time nor order-write latency; measure both during a representative trial to assess rollout impact.

### What changed

**Checks set before the run.** Tie the recommendation to the write-availability requirement; explain scans/waits and invalid-index maintenance. Include an operational check without claiming zero overhead, no locks of any kind, or measured latency for this store.

Both recommend a concurrent build, explain its extra scans and waits, and keep latency unmeasured. The baseline gives the most actionable validity check, pg_index.indisvalid. The skill answer walks one incoming order through the design and proposes a representative trial. Its statement that approval is pending is plausible in a review draft, but the hypothetical store supplied no approval record.

**차이.** 두 답 모두 쓰기를 허용하는 동시 인덱스 생성을 권합니다. 미적용 답은 확인할 열인 pg_index.indisvalid까지 지정하고, 스킬 답은 주문 한 건이 들어올 때의 동작과 측정할 항목을 짚습니다. 실제 승인 상태는 예제에 주어지지 않았습니다.
