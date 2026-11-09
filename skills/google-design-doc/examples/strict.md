# Should PostgreSQL add the orders index during this shift?

[한국어](strict.ko.md) · [light](light.md) · [standard](standard.md)

[Question and sources](standard.md#question)

### Strict

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
