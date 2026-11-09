# Which Kubernetes rollout did the green CI job actually observe?

[한국어](standard.ko.md) · [light](light.md) · [strict](strict.md)

### Question

> At 09:00 CI ran kubectl rollout status deployment/checkout-api with no flags while revision 7 was rolling out. Revision 8 started before 7 finished. No later revision started, and the command eventually reported success. By default the watch follows the latest rollout. The --revision=N option pins the watch and aborts if that revision is superseded; --watch=false returns a snapshot. Which revision did CI actually verify? What command would watch only revision 7, and what command would return the current status immediately?

**Sources** · [Kubernetes command reference, kubectl rollout status](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_rollout/kubectl_rollout_status/)

### Standard

> CI followed the latest rollout, so it verified revision 8. The command’s success does not show that revision 7 completed.
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
