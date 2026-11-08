# Google-inspired design document · Choosing an index for a search service

Run on 2026-11-08 • `google-design-doc` 0.1.1 • English • Codex CLI 0.167.0

### Prompt

> Write a design proposal excerpt of at most 115 words. Goal: reduce lookups that currently scan the whole log. Option A adds an index updated during each write. Option B rebuilds the index every 10 minutes. Search must show records within 2 minutes; no latency measurements exist. Changing record format is out of scope.

### Without a skill

> We propose adding an index to reduce lookups that currently scan the whole log, without changing the record format.
>
> Option A updates the index during each write. This supports the two-minute search visibility requirement, provided indexing completes within that window, but adds work to the write path.
>
> Option B rebuilds the index every 10 minutes. As proposed, it cannot meet the two-minute visibility requirement.
>
> Recommend Option A, subject to validation. No latency measurements exist, so performance gains and write overhead remain unverified. Measure lookup latency, write latency, and time to search visibility under representative load before rollout.

### With the skill at standard

> Proposal for review: choose Option A, subject to validation that records become searchable within 2 minutes. The goal is to reduce lookups that currently scan the whole log; record-format changes are out of scope.
>
> On each write, Option A updates an index; searches use that index to locate records. This adds write work. If an index update fails, search visibility may exceed 2 minutes; failure handling remains unresolved.
>
> Option B rebuilds the index every 10 minutes, avoiding per-write index updates but failing the visibility requirement without another mechanism.
>
> No latency measurements exist. Before approval, measure lookup latency, write overhead, and write-to-search visibility, including index-update failures.

### What changed

**Checks set before the run.** Compare the write-path cost with rebuild staleness, honor the two-minute requirement and unchanged record format, avoid invented measurements and identify what to test.

Both recommend A conditionally and reject a 10-minute rebuild as insufficient for a 2-minute deadline. The skill adds a concrete unresolved design question about failed index updates. Neither presents an unmeasured performance gain as observed.

**차이.** 두 답 모두 A를 조건부로 권합니다. 스킬 답안은 인덱스 갱신에 실패해 검색 반영이 늦어지는 경우까지 시험 대상으로 남깁니다.
