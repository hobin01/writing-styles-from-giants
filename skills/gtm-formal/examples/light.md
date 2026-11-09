# When do two Raft candidates need the same vote?

[한국어](light.ko.md) · **light** · [standard](standard.md) · [strict](strict.md)

### Question

> Two candidates stand in the same election. The number of servers is fixed, each server can vote for at most one candidate for the term, and each candidate needs a set minimum number of votes to win. Raft normally requires a majority. A team proposes four votes as the minimum for either a seven-server or an eight-server cluster. When does a vote threshold prevent two winners? Is four safe in each cluster, and could an election with a safe threshold still have no winner?

**Sources** · [Ongaro and Ousterhout, In Search of an Understandable Consensus Algorithm, §5.2](https://raft.github.io/raft.pdf) · [etcd v3.5 FAQ, fault tolerance](https://etcd.io/docs/v3.5/faq/#what-is-failure-tolerance)

### With the skill

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

### Without the skill

> To prevent two candidates from winning the same term, the minimum vote threshold must be **more than half the servers**. If two candidates each reached that threshold, their vote sets would overlap, which is impossible when each server votes for at most one candidate.
>
> - **Seven servers:** Four votes is safe. Two sets of four would require eight votes, but only seven servers can vote.
> - **Eight servers:** Four votes is not safe. The votes could split four to each candidate, giving both a win. The threshold must be at least five.
>
> A safe threshold does not guarantee a winner. Votes might split among candidates so that none reaches the minimum—for example, in a seven-server cluster with a four-vote threshold, a 3–2–2 split leaves no winner.
