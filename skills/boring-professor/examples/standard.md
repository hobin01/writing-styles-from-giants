# Boring Professor: literal technical explanation · Why one lock is insufficient

Run on 2026-11-08 • `boring-professor` 0.1.1 • English • Codex CLI 0.167.0

### Prompt

> Explain to a systems student, in at most 90 words, why locking only the final write cannot guarantee unique ticket numbers. Two workers can both read 17 before either writes. Each increments its local value and writes 18 under the write lock. Assume the counter starts at 17 and both operations succeed.

### Without a skill

> Locking only the final write prevents simultaneous writes, but it does not protect the full read–increment–write operation. Both workers can read 17, independently compute 18, then take turns acquiring the write lock and writing 18. Both operations succeed, yet both issue ticket 18, and the counter ends at 18 instead of 19. To guarantee unique ticket numbers, protect the entire read–increment–write sequence with one lock or use an atomic increment that returns a distinct value to each worker.

### With the skill at standard

> A lock provides mutual exclusion: only one worker can execute the protected code at a time. If it protects only the final write, both workers can read the initial counter value, 17, before either writes. Each independently computes 18. The lock then serializes two successful writes of 18, so both workers obtain the same ticket number.
>
> Uniqueness requires protecting the entire read–increment–write operation with the same lock, or using an atomic increment that returns a distinct value for each operation.

### What changed

**Checks set before the run.** Name the protected operation and the unprotected read–modify–write sequence. Trace both workers to 18. Keep the stated assumptions and avoid a metaphor.

Both trace two reads of 17 and two writes of 18, and suggest protecting the full operation. The skill defines mutual exclusion first; the baseline spells out that the counter ends at 18 instead of 19. Both are usable literal explanations.

**차이.** 두 답 모두 18번이 두 번 발급되는 과정을 설명합니다. 스킬 답안은 먼저 상호 배제를 정의하고, 미적용 답안은 최종 값이 19가 아닌 18임을 강조합니다.
