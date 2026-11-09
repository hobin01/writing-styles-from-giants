# When do two Raft candidates need the same vote?

[한국어](light.ko.md) · [standard](standard.md) · [strict](strict.md)

[Question and sources](standard.md#question)

### Light

> Let $N$ be the number of servers and $q$ the minimum votes required to win. Assume each server can vote for at most one of the two candidates during the term.
>
> Two candidates cannot both win exactly when
> $$
> 2q>N.
> $$
> If both won, they would need $2q$ distinct votes, but only $N$ servers can vote. Conversely, if $2q\le N$, the servers could give each candidate $q$ votes, so two winners are possible.
>
> Thus, a safe threshold is $q>\frac N2$, the majority rule:
>
> - For $N=7$, $q=4$ is safe because $8>7$.
> - For $N=8$, $q=4$ is not safe because $8\not>8$. Each candidate could receive four votes.
>
> A safe threshold prevents two winners but does not guarantee a winner. For example, in a seven-server cluster with threshold four, if the votes split $3$–$3$ and one server abstains, neither candidate reaches four.
