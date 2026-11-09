# Should PostgreSQL add the orders index during this shift?

[한국어](light.ko.md) · [standard](standard.md) · [strict](strict.md)

[Question and sources](standard.md#question)

### Light

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
