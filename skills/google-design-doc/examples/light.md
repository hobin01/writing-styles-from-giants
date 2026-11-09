# Should PostgreSQL add the orders index during this shift?

[한국어](light.ko.md) · **light** · [standard](standard.md) · [strict](strict.md)

### Question

> A store running PostgreSQL 17 needs an index on its orders table. Order INSERTs must remain available during the build. Production rollout also requires rehearsal p95 write latency at most 20% above the 40 ms baseline. A concurrent-build rehearsal measured 51 ms; production performance has not been measured. Ordinary CREATE INDEX blocks writes. CREATE INDEX CONCURRENTLY permits writes but scans the table twice and can wait for transactions. If it fails, it can leave an invalid index that the planner ignores but writes still maintain. What should the store do on this shift, and what would justify a later production attempt?

**Sources** · [PostgreSQL 17 documentation, CREATE INDEX](https://www.postgresql.org/docs/17/sql-createindex.html#SQL-CREATEINDEX-CONCURRENTLY) · [PostgreSQL 17 system catalogs, pg_index](https://www.postgresql.org/docs/17/catalog-pg-index.html)

### With the skill

> ## Shift decision
>
> **Do not start the index build on this shift.** Ordinary `CREATE INDEX` violates the requirement that order inserts remain available. `CREATE INDEX CONCURRENTLY` permits writes, but its rehearsal p95 write latency was 51 ms.
>
> The rollout limit is 20% above the 40 ms baseline: at most **48 ms p95**. The rehearsal exceeded that limit by 3 ms, so concurrent build has not passed the release gate. Production performance is also unmeasured.
>
> ## Later production attempt
>
> A production attempt would be justified after a representative rehearsal of the concurrent build measures p95 write latency at or below **48 ms**, while confirming order inserts remain available. The rehearsal should account for the build’s two table scans and possible waits for transactions.
>
> If a concurrent build fails, check whether it left an invalid index. The planner ignores that index, but writes still maintain it; remove the invalid index before retrying. Production performance should be observed during any later approved rollout.

### Without the skill

> Do not start the production index build on this shift. A concurrent build keeps INSERTs available, but the rehearsal p95 was 51 ms—27.5% above the 40 ms baseline, exceeding the 20% limit of 48 ms. Production performance is also unknown, and the build can take time or leave an invalid index that still adds write overhead if it fails.
>
> A later production attempt is justified after a rehearsal meets the 48 ms p95 limit and the rollout plan accounts for the two scans, possible waits on transactions, and checking for and removing any invalid index left by a failed build. During the production attempt, monitor write latency and build progress, with a rollback plan if the latency limit is breached.
