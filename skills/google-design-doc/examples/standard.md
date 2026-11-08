# Should PostgreSQL add the orders index during this shift?

2026-11-08 · `google-design-doc` 0.1.1 at first pass · `gpt-6-luna` · Codex CLI 0.167.0

### Case and sources

- [PostgreSQL 17 documentation, CREATE INDEX](https://www.postgresql.org/docs/17/sql-createindex.html#SQL-CREATEINDEX-CONCURRENTLY). Building Indexes Concurrently explains locking, table scans, waiting for transactions and invalid indexes after failure. The store, schema and decision are illustrative; no production benchmark is quoted.
- [PostgreSQL 17 system catalogs, pg_index](https://www.postgresql.org/docs/17/catalog-pg-index.html). The indisvalid field records whether the index is valid for queries. The rehearsal metrics and release threshold are illustrative.

**Reasoning task.** Apply two independent release constraints to an architectural choice, compute the latency budget and plan a recovery path without converting a rehearsal into production evidence.

### Prompt

> Write a design-review excerpt for an illustrative PostgreSQL 17 store. The team cannot block order INSERTs throughout an index build. Its separate release gate is a rehearsal p95 write latency no more than 20% above the 40 ms baseline. A concurrent-build rehearsal measured 51 ms. Ordinary CREATE INDEX blocks writes; CREATE INDEX CONCURRENTLY lets writes continue, scans the table twice and can wait for transactions. A failed concurrent run can leave an invalid index that planners ignore but writes still maintain. Recommend what to authorize this shift, what to measure before retrying and how to handle an invalid result. The store has not measured production performance. Keep the excerpt under 145 words.

### Without a skill

> ### Index build release decision
>
> Authorize `CREATE INDEX CONCURRENTLY` for this shift: ordinary `CREATE INDEX` blocks writes, which the store cannot accept. The concurrent rehearsal measured 51 ms p95, 27.5% above the 40 ms baseline, so it fails the separate release gate of no more than 20% above baseline (48 ms). Do not treat the rehearsal as evidence of production performance; production has not been measured.
>
> Before retrying, measure rehearsal p95 write latency against the 40 ms baseline and investigate why it exceeded the 48 ms limit. Also check for long-running transactions that could delay the build. Concurrent creation scans the table twice and may wait for transactions.
>
> If a concurrent build fails, inspect the resulting index. If it is invalid, planners ignore it but writes still maintain it. Drop the invalid index before retrying, then verify the new index is valid.

### With the skill at standard

> **Proposal for review — PostgreSQL 17 index build.** Authorize `CREATE INDEX CONCURRENTLY`: order `INSERT`s must continue during the build. Ordinary `CREATE INDEX` blocks writes, so it violates that constraint. Concurrent builds scan the table twice and can wait for transactions. The rehearsal’s p95 write latency was 51 ms, 27.5% above the 40 ms baseline, exceeding the separate release gate of no more than 20% above baseline (48 ms).
>
> Before retrying, measure rehearsal p95 write latency under the same workload and investigate transaction waits; production performance is unmeasured. If the concurrent build fails, check for an invalid index: planners ignore it, but writes still maintain it. Remove the invalid index before retrying, then verify the retry succeeds.
>
> **Review status:** Proposed; authorization is pending.

### First-pass assessment

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Computes the 48 ms gate or the 27.5% increase and recognizes that the 51 ms concurrent rehearsal fails the allowed 20% increase. | Met | Met |
| Rejects an ordinary build during the shift because it blocks required INSERTs and holds the production rollout pending a passing new rehearsal; does not promise production latency. | Missed | Missed |
| Gives a concrete review or recovery plan that checks validity and deals with an invalid index that still imposes write cost (for example, remove it and retry safely). | Met | Met |

Both calculate the 48 ms ceiling and 27.5% increase and describe invalid-index handling. Despite recognizing the failed gate, both recommend authorizing the concurrent build. The skill answer later labels authorization pending, leaving the decision internally inconsistent; the baseline expressly authorizes it for this shift. Neither recommends holding production rollout until a rehearsal passes.

**차이.** 두 답 모두 상한 48 ms와 27.5% 증가율을 계산하고 무효 인덱스 처리 방안도 제시했습니다. 그런데 스킬 답과 미적용 답 모두 기준을 넘긴 빌드를 승인하자고 합니다. 스킬 답은 끝에서 다시 승인 대기라고 적고, 미적용 답은 이번 근무 중 승인하자고 명시합니다. 재시험 통과 전에는 배포를 보류해야 한다는 판단이 빠졌습니다.

<details>
<summary>Developmental retest · version 0.1.2</summary>

Check each independent release gate before authorizing a proposed operation. This retest is excluded from the first-pass counts.

The request and original baseline are unchanged.

**New standard answer**

> **Context and constraints.** The team needs to build an index without blocking order `INSERT`s. Release also requires rehearsal p95 write latency at most 20% above the 40 ms baseline: 48 ms. Production performance is unmeasured.
>
> **Proposal for review: authorize the concurrent build for rehearsal only.** `CREATE INDEX CONCURRENTLY` allows writes to continue, but scans the table twice and can wait for transactions. The rehearsal measured 51 ms, above the 48 ms gate, so this is not authorization to release. Ordinary `CREATE INDEX` blocks writes and fails the operational constraint.
>
> **Before retrying,** measure rehearsal p95 write latency under representative load and investigate transaction waits. Retry only when the rehearsal meets the 48 ms gate.
>
> **Failure handling.** If the concurrent build fails, check for an invalid index: planners ignore it, but writes still maintain it. Remove the invalid index before retrying.
>
> **Status:** Proposed; release approval remains open pending a passing rehearsal.

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Computes the 48 ms gate or the 27.5% increase and recognizes that the 51 ms concurrent rehearsal fails the allowed 20% increase. | Met | Met |
| Rejects an ordinary build during the shift because it blocks required INSERTs and holds the production rollout pending a passing new rehearsal; does not promise production latency. | Missed | Met |
| Gives a concrete review or recovery plan that checks validity and deals with an invalid index that still imposes write cost (for example, remove it and retry safely). | Met | Met |

Both the skill answer and the baseline compute the 48 ms gate, reject a write-blocking ordinary build, and call for inspecting and removing an invalid index. The skill answer permits rehearsal only, with release pending a passing result, but exceeds the under-145-word limit. The baseline correctly calculates the 27.5% increase and then authorizes the concurrent build for this shift without limiting authorization to rehearsal, despite the failed gate.

**차이.** 스킬 답과 미적용 답 모두 허용치를 48ms로 계산하고, 쓰기를 막는 일반 인덱스 생성을 배제하며, 무효 인덱스를 확인해 제거하도록 한다. 스킬 답은 재연습만 허용하고 통과 전까지 배포를 보류하지만 145단어 미만 요건을 넘긴다. 미적용 답은 27.5% 증가를 올바르게 계산하고도 기준에 미달한 상태에서 승인을 연습에 한정하지 않은 채 이번 근무조의 동시 인덱스 생성을 허용한다.

</details>
