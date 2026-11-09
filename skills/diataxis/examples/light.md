# Which Kubernetes rollout did the green CI job actually observe?

[한국어](light.ko.md) · **light** · [standard](standard.md) · [strict](strict.md)

### Question

> At 09:00 CI ran kubectl rollout status deployment/checkout-api with no flags while revision 7 was rolling out. Revision 8 started before 7 finished. No later revision started, and the command eventually reported success. By default the watch follows the latest rollout. The --revision=N option pins the watch and aborts if that revision is superseded; --watch=false returns a snapshot. Which revision did CI actually verify? What command would watch only revision 7, and what command would return the current status immediately?

**Sources** · [Kubernetes command reference, kubectl rollout status](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_rollout/kubectl_rollout_status/)

### With the skill

> CI verified **revision 8**, the latest rollout when the watch followed it. The command’s success does not establish that revision 7 finished successfully.
>
> To watch only revision 7:
>
> ```sh
> kubectl rollout status deployment/checkout-api --revision=7
> ```
>
> To return the current status immediately:
>
> ```sh
> kubectl rollout status deployment/checkout-api --watch=false
> ```

### Without the skill

> CI watched the latest rollout, so it verified revision 8.
>
> Watch only revision 7:
>
> ```sh
> kubectl rollout status deployment/checkout-api --revision=7
> ```
>
> Return the current status immediately:
>
> ```sh
> kubectl rollout status deployment/checkout-api --watch=false
> ```
