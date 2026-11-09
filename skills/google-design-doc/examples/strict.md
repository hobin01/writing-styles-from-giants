# Should PostgreSQL add the orders index during this shift?

[한국어](strict.ko.md) · [light](light.md) · [standard](standard.md) · **strict**

### Question

> A store running PostgreSQL 17 needs an index on its orders table. Order INSERTs must remain available during the build. Production rollout also requires rehearsal p95 write latency at most 20% above the 40 ms baseline. A concurrent-build rehearsal measured 51 ms; production performance has not been measured. Ordinary CREATE INDEX blocks writes. CREATE INDEX CONCURRENTLY permits writes but scans the table twice and can wait for transactions. If it fails, it can leave an invalid index that the planner ignores but writes still maintain. What should the store do on this shift, and what would justify a later production attempt?

**Sources** · [PostgreSQL 17 documentation, CREATE INDEX](https://www.postgresql.org/docs/17/sql-createindex.html#SQL-CREATEINDEX-CONCURRENTLY) · [PostgreSQL 17 system catalogs, pg_index](https://www.postgresql.org/docs/17/catalog-pg-index.html)

### With the skill

> # Index build proposal
>
> **Recommendation for this shift:** Defer the index build. The concurrent build keeps `INSERT`s available, but its rehearsal p95 write latency was 51 ms—27.5% above the 40 ms baseline. The release limit is 20% above baseline, or 48 ms. The rehearsal failed that gate, and production performance has not been measured.
>
> ## Goals and constraints
>
> - Keep order `INSERT`s available during the build.
> - Require rehearsal p95 write latency at most 20% above the 40 ms baseline: **48 ms**.
> - The store runs PostgreSQL 17.
>
> ## Proposed behavior
>
> Use `CREATE INDEX CONCURRENTLY` for a later attempt. It permits writes during the build, scans the table twice, and can wait for transactions.
>
> If the command fails, check whether it left an invalid index. The planner ignores that index, but writes still maintain it. Remove the invalid index before retrying; until it is removed, writes continue to pay its maintenance cost.
>
> ## Alternatives and trade-offs
>
> - **Ordinary `CREATE INDEX`:** Does not meet the requirement to keep `INSERT`s available during the build.
> - **`CREATE INDEX CONCURRENTLY`:** Meets the availability requirement, but the measured rehearsal p95 of 51 ms exceeds the 48 ms limit. It is not ready for production authorization.
>
> ## What would justify a later attempt
>
> Repeat the concurrent-build rehearsal in a representative test setting. Authorize a production attempt only if the rehearsal p95 write latency is **at most 48 ms** and the build keeps `INSERT`s available. Production performance remains unmeasured; observe it during any subsequently approved rollout. No production attempt is approved by this proposal.

### Without the skill

> Do not start the production index build on this shift. A concurrent build keeps INSERTs available, but the rehearsal p95 was 51 ms—27.5% above the 40 ms baseline, exceeding the 20% limit of 48 ms. Production performance is also unknown, and the build can take time or leave an invalid index that still adds write overhead if it fails.
>
> A later production attempt is justified after a rehearsal meets the 48 ms p95 limit and the rollout plan accounts for the two scans, possible waits on transactions, and checking for and removing any invalid index left by a failed build. During the production attempt, monitor write latency and build progress, with a rollback plan if the latency limit is breached.
