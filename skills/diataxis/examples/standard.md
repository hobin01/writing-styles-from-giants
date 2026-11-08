# Which Kubernetes rollout did the green CI job actually observe?

[한국어](standard.ko.md)

2026-11-08 · `diataxis` 0.1.1 · English · `gpt-6-luna`

### Case and sources

- [Kubernetes command reference, kubectl rollout status](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_rollout/kubectl_rollout_status/). Synopsis and flags document default revision tracking, --revision and --watch. checkout-api and revisions 7/8 are an illustrative release, not historical cluster telemetry.

### Prompt

> Write a short lookup entry for the release team using kubectl rollout status on Deployment checkout-api. CI starts watching revision 7 without flags at 09:00. Before 7 finishes, revision 8 starts; the command later reports success. A default watch follows the latest rollout across revisions; a watch pinned with --revision=N aborts if superseded, and --watch=false reads a snapshot without waiting. Explain what the green job does and does not establish about 7 and 8. Give the exact commands for a new CI job that must monitor revision 7 specifically and for an operator who wants the current status immediately. Assume 8 is the last revision during this example. Make this useful for lookup, not a tutorial. Write your answer in English.

### Without the skill

> ### `kubectl rollout status` — `checkout-api`
>
> At 09:00, CI runs `kubectl rollout status deployment/checkout-api` without flags while revision 7 is in progress. Revision 8 starts before 7 finishes, and the command later reports success. By default, the watch follows the latest rollout, so that green job establishes that **revision 8 completed**. It does **not** establish that revision 7 completed successfully.
>
> For a new CI job that must monitor revision 7 specifically, pin the watch:
>
> ```sh
> kubectl rollout status deployment/checkout-api --revision=7
> ```
>
> If revision 7 is superseded before the watch completes, the command aborts rather than switching to revision 8.
>
> For an immediate status snapshot without waiting:
>
> ```sh
> kubectl rollout status deployment/checkout-api --watch=false
> ```
>
> This reports the current rollout status; it does not establish that the rollout will finish successfully.

### With the skill at standard

> ## `kubectl rollout status` for `checkout-api`
>
> **Default behavior:** `kubectl rollout status deployment/checkout-api` follows the latest rollout. If revision 8 starts while the command is watching revision 7, the watch follows revision 8.
>
> In this example, the green CI job establishes that the latest rollout it followed—revision 8, assumed to be the last revision—completed successfully. It does **not** establish that revision 7 completed successfully: the command may have switched to watching revision 8 before 7 finished.
>
> | Need | Command | Behavior |
> |---|---|---|
> | CI job must monitor revision 7 specifically | `kubectl rollout status deployment/checkout-api --revision=7` | Watches revision 7; aborts if it is superseded. |
> | Operator wants the current status immediately | `kubectl rollout status deployment/checkout-api --watch=false` | Reads a snapshot and returns without waiting. |

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Attributes the successful default watch to latest revision 8 and says that its success does not establish success for revision 7. | Met | Met |
| Gives an executable kubectl rollout status command for deployment/checkout-api with --revision=7, and states that supersession causes the pinned watch to abort rather than follow 8. | Met | Met |
| Gives an executable command with --watch=false for a current snapshot, with purpose and commands easy to find in a compact lookup entry. | Met | Met |

**Masked review** (X = baseline; Y = standard). Both identify revision 8 as the successful rollout, give the two executable commands and explain why the unpinned watch cannot certify revision 7. X places the commands in separate code blocks and distinguishes a current snapshot from future success. Y groups each command and its behavior in a lookup table.

<details>
<summary>Run record</summary>

Each arm was a separate ephemeral read-only Codex CLI 0.167.0 session with low reasoning effort. Neither session was given the other answer or an answer in the other language.

SHA-256 prefixes (entrypoint / baseline answer / standard answer): `1bf8f74acf77` / `80606212012a` / `67a7105766a3`.

</details>
