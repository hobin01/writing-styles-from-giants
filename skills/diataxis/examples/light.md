# Which Kubernetes rollout did the green CI job actually observe?

[한국어](light.ko.md) · [standard](standard.md) · [strict](strict.md)

[Question and sources](standard.md#question)

### Light

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
