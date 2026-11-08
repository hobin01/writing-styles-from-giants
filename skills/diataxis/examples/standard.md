# Watching a specific Kubernetes Deployment revision

2026-11-08 · `diataxis` 0.1.1 · English · Codex CLI 0.167.0 / gpt-6.1-sol

### Case and sources

- [Kubernetes command reference, kubectl rollout status](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_rollout/kubectl_rollout_status/). Synopsis and flags document default revision tracking, --revision and --watch. checkout-api and revisions 7/8 are an illustrative release, not historical cluster telemetry.

### Prompt

> Write a compact lookup entry for a Kubernetes release engineer who uses kubectl rollout status. An illustrative Deployment named checkout-api is rolling out revision 7; revision 8 might start before 7 finishes. Without --revision, the command watches the latest rollout and follows a newer revision if one starts. With --revision=7, it monitors that particular revision and aborts if it is superseded. With --watch=false, it returns the current status without waiting. Supply the exact command to watch revision 7 and the two flag meanings. Do not claim either rollout actually succeeded.

### Without a skill

> `kubectl rollout status deployment/checkout-api --revision=7`
>
> - `--revision=7`: Watch revision 7; abort if a newer revision supersedes it. Without this flag, the command watches the latest rollout and follows newer revisions.
> - `--watch=false`: Return the current status immediately, without waiting for the rollout to finish.

### With the skill at standard

> Watch revision 7 of `checkout-api`:
>
> ```sh
> kubectl rollout status deployment/checkout-api --revision=7
> ```
>
> | Flag | Meaning |
> | --- | --- |
> | `--revision=7` | Monitors revision 7 and aborts if it is superseded, such as when revision 8 starts. Without `--revision`, the command watches the latest rollout and follows a newer revision if one starts. |
> | `--watch=false` | Returns the current status without waiting. |
>
> This example does not establish that either rollout succeeded.

### What changed

**Checks set before the run.** Use kubectl rollout status deployment/checkout-api --revision=7 (or equivalent); distinguish monitoring from starting or rolling back the Deployment, pinning from following the latest, and one-time status from waiting. The revision numbers are example inputs.

Both give a correct command for revision 7 and explain when --watch=false returns. The baseline is a short lookup list. The skill uses a table and names the concrete failure condition: revision 8 superseding revision 7. Neither reports a successful deployment.

**차이.** 두 답 모두 revision 7을 지정하는 명령과 기다리지 않고 상태만 읽는 옵션을 정확히 제시합니다. 스킬 답은 revision 8이 시작되면 revision 7을 지켜보던 명령이 중단된다는 상황을 표에서 보여 줍니다.
