# When do two Raft candidates need the same vote?

[한국어](strict.ko.md) · [light](light.md) · [standard](standard.md)

[Question and sources](standard.md#question)

### Strict

> Let $N\in\{7,8\}$ be the number of servers, and let $T$ be the minimum number of votes each candidate needs to win. Assume each server casts at most one vote in the term, and both candidates win exactly when each receives at least $T$ votes.
>
> Two winners would require at least $2T$ votes in total. Since at most $N$ votes can be cast, two winners are impossible exactly when
> $$
> 2T>N,
> $$
> or, for integer $T$, when $T>\lfloor N/2\rfloor$. If $2T\le N$, two winners are possible: assign $T$ distinct servers to each candidate, leaving any remaining servers unassigned. Thus the condition is both necessary and sufficient.
>
> For $N=7$, four is safe because $2\cdot4=8>7$. For $N=8$, four is not safe: $2\cdot4=8$, and assigning four servers to each candidate gives both candidates the minimum required votes. A threshold of five would prevent two winners in an eight-server cluster.
>
> A safe threshold does not guarantee a winner. For example, in the seven-server cluster with threshold four, if no server votes, neither candidate reaches four votes. More generally, votes may be split so that each candidate receives fewer than $T$.
