# Should PostgreSQL add the orders index during this shift?

[한국어](standard.ko.md) · [light](light.md) · [strict](strict.md)

### Question

> A store running PostgreSQL 17 needs an index on its orders table. Order INSERTs must remain available during the build. Production rollout also requires rehearsal p95 write latency at most 20% above the 40 ms baseline. A concurrent-build rehearsal measured 51 ms; production performance has not been measured. Ordinary CREATE INDEX blocks writes. CREATE INDEX CONCURRENTLY permits writes but scans the table twice and can wait for transactions. If it fails, it can leave an invalid index that the planner ignores but writes still maintain. What should the store do on this shift, and what would justify a later production attempt?

**Sources** · [PostgreSQL 17 documentation, CREATE INDEX](https://www.postgresql.org/docs/17/sql-createindex.html#SQL-CREATEINDEX-CONCURRENTLY) · [PostgreSQL 17 system catalogs, pg_index](https://www.postgresql.org/docs/17/catalog-pg-index.html)

### Standard

> ## Proposal for this shift
>
> Do not attempt the index build on this shift. The store’s rehearsal p95 write latency limit is 48 ms: 20% above the 40 ms baseline. The concurrent-build rehearsal measured 51 ms, so it failed the release gate by 3 ms. Production performance has not been measured.
>
> ## Proposed design
>
> Use `CREATE INDEX CONCURRENTLY` for a later attempt. It permits order inserts during the build, meeting the availability constraint. It scans the table twice and may wait for transactions.
>
> If the build fails, check whether it left an invalid index. The planner ignores that index, but writes still maintain it. Drop the invalid index before retrying, accounting for its ongoing write cost until it is removed.
>
> ## Alternative
>
> Ordinary `CREATE INDEX` does not meet the availability constraint because it blocks writes during the build. It is therefore not a viable option for this rollout.
>
> ## What would justify a later production attempt
>
> First, repeat the concurrent-build rehearsal in a representative test setting and measure p95 write latency. A result at or below 48 ms would pass the latency gate; a result above 48 ms would not. Also assess transaction waits and the expected impact of the two table scans. Production performance remains unknown until a rollout is approved and observed.
>
> If the representative rehearsal passes and the store can preserve insert availability, reviewers can consider authorizing a production attempt. Approval has not been given.
