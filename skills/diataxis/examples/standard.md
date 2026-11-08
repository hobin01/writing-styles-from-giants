# Diátaxis documentation · A lookup entry for snapshot retention

Run on 2026-11-08 • `diataxis` 0.1.1 • English • Codex CLI 0.167.0

### Prompt

> Write a short entry for people who already use our backup CLI and want to look up the flag `--keep N`. It accepts integers 1 through 14, defaults to 3, and applies only to completed snapshots. Pending snapshots stay untouched. No installation steps are needed.

### Without a skill

> `--keep N`
>
> Keep the N most recent completed snapshots. Accepts integers from 1 to 14; defaults to 3. Pending snapshots remain untouched.

### With the skill at standard

> ### `--keep N`
>
> Sets how many completed snapshots to keep.
>
> | Value | Constraint |
> | --- | --- |
> | Type | Integer |
> | Allowed range | 1–14 |
> | Default | 3 |
> | Applies to | Completed snapshots only |
>
> Pending snapshots stay untouched.

### What changed

**Checks set before the run.** Serve lookup readers with the flag's exact spelling, range, default and completed-only scope. Leave pending snapshots untouched and avoid unsupported CLI commands.

Both give the correct range, default and scope. The baseline adds “most recent,” an ordering the supplied specification does not promise. The skill uses a small lookup table and leaves the ordering unspecified.

**차이.** 미적용 답안은 명세에 없는 ‘가장 최근’이라는 순서를 덧붙였습니다. 스킬 답안은 조회에 필요한 범위·기본값·적용 대상을 표로 보여 줍니다.
