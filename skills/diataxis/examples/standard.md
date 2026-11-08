# Which Kubernetes rollout did the green CI job actually observe?

2026-11-08 · `diataxis` 0.1.1 at first pass · `gpt-6-luna` · Codex CLI 0.167.0

### Case and sources

- [Kubernetes command reference, kubectl rollout status](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_rollout/kubectl_rollout_status/). Synopsis and flags document default revision tracking, --revision and --watch. checkout-api and revisions 7/8 are an illustrative release, not historical cluster telemetry.

**Reasoning task.** Infer what an apparently successful deployment monitor actually witnessed after its target changed, and distinguish that evidence from a nonblocking snapshot.

### Prompt

> Write a short lookup entry for the release team using kubectl rollout status on Deployment checkout-api. CI starts watching revision 7 without flags at 09:00. Before 7 finishes, revision 8 starts; the command later reports success. A default watch follows the latest rollout across revisions; a watch pinned with --revision=N aborts if superseded, and --watch=false reads a snapshot without waiting. Explain what the green job does and does not establish about 7 and 8. Give the exact commands for a new CI job that must monitor revision 7 specifically and for an operator who wants the current status immediately. Assume 8 is the last revision during this example. Make this useful for lookup, not a tutorial.

### Without a skill

> `kubectl rollout status deployment/checkout-api` watches the latest rollout by default. If revision 8 starts before revision 7 finishes, the watch follows 8; a green job establishes that the latest rollout (revision 8 here) succeeded. It does **not** establish that revision 7 completed successfully.
>
> To monitor revision 7 specifically, pin the watch:
>
> ```sh
> kubectl rollout status deployment/checkout-api --revision=7
> ```
>
> If revision 8 supersedes it, that command aborts rather than reporting success for 8.
>
> To read the current status immediately, without waiting:
>
> ```sh
> kubectl rollout status deployment/checkout-api --watch=false
> ```

### With the skill at standard

> ## `kubectl rollout status` for `checkout-api`
>
> A watch without flags follows the latest rollout. If revision 8 starts while the command is watching revision 7, the command follows revision 8. Assuming 8 is the last revision in this example, a successful exit means revision 8 completed; it does **not** establish that revision 7 completed.
>
> | Need | Command | Behavior |
> |---|---|---|
> | CI job must monitor revision 7 specifically | `kubectl rollout status deployment/checkout-api --revision=7` | Watches revision 7; aborts if a newer rollout supersedes it. |
> | Operator wants the current status immediately | `kubectl rollout status deployment/checkout-api --watch=false` | Reads a status snapshot and exits without waiting. |
>
> **Example:** CI starts an unpinned watch at 09:00 while revision 7 is running. Revision 8 starts before 7 finishes, and the command later reports success. The green job establishes that the latest rollout it followed—revision 8—completed. It does not establish that revision 7 completed.

### First-pass assessment

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Attributes the successful default watch to latest revision 8 and says that its success does not establish success for revision 7. | Met | Met |
| Gives an executable kubectl rollout status command for deployment/checkout-api with --revision=7, and states that supersession causes the pinned watch to abort rather than follow 8. | Met | Met |
| Gives an executable command with --watch=false for a current snapshot, with purpose and commands easy to find in a compact lookup entry. | Met | Met |

Both say the successful watch refers to revision 8 and cannot certify revision 7; both give usable pinned-watch and snapshot commands. The skill answer puts the commands and effects in a lookup table but repeats the green-job explanation. The baseline uses two shorter command blocks.

**차이.** 두 답 모두 성공이 revision 8을 가리키므로 revision 7의 성공은 확정할 수 없다고 설명하며, 고정 감시와 즉시 조회에 맞는 명령을 제공합니다. 스킬 답은 목적별 표를 썼지만 성공의 의미를 반복했고, 미적용 답은 두 코드 블록으로 더 짧게 정리했습니다.
