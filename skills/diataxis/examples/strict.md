# Which Kubernetes rollout did the green CI job actually observe?

[한국어](strict.ko.md) · [light](light.md) · [standard](standard.md)

[Question and sources](standard.md#question)

### Strict

> CI watched the latest rollout, so it verified **revision 8**. Revision 7 was superseded before the command succeeded.
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
