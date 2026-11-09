# When do two Raft candidates need the same vote?

[한국어](strict.ko.md) · [light](light.md) · [standard](standard.md) · **strict**

### Question

> Two candidates stand in the same election. The number of servers is fixed, each server can vote for at most one candidate for the term, and each candidate needs a set minimum number of votes to win. Raft normally requires a majority. A team proposes four votes as the minimum for either a seven-server or an eight-server cluster. When does a vote threshold prevent two winners? Is four safe in each cluster, and could an election with a safe threshold still have no winner?

**Sources** · [Ongaro and Ousterhout, In Search of an Understandable Consensus Algorithm, §5.2](https://raft.github.io/raft.pdf) · [etcd v3.5 FAQ, fault tolerance](https://etcd.io/docs/v3.5/faq/#what-is-failure-tolerance)

### With the skill

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

### Without the skill

> To prevent two candidates from winning the same term, the minimum vote threshold must be **more than half the servers**. If two candidates each reached that threshold, their vote sets would overlap, which is impossible when each server votes for at most one candidate.
>
> - **Seven servers:** Four votes is safe. Two sets of four would require eight votes, but only seven servers can vote.
> - **Eight servers:** Four votes is not safe. The votes could split four to each candidate, giving both a win. The threshold must be at least five.
>
> A safe threshold does not guarantee a winner. Votes might split among candidates so that none reaches the minimum—for example, in a seven-server cluster with a four-vote threshold, a 3–2–2 split leaves no winner.
