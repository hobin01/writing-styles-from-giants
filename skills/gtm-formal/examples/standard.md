# When do two Raft candidates need the same vote?

[한국어](standard.ko.md) · [light](light.md) · [strict](strict.md)

### Question

> Two candidates stand in the same election. The number of servers is fixed, each server can vote for at most one candidate for the term, and each candidate needs a set minimum number of votes to win. Raft normally requires a majority. A team proposes four votes as the minimum for either a seven-server or an eight-server cluster. When does a vote threshold prevent two winners? Is four safe in each cluster, and could an election with a safe threshold still have no winner?

**Sources** · [Ongaro and Ousterhout, In Search of an Understandable Consensus Algorithm, §5.2](https://raft.github.io/raft.pdf) · [etcd v3.5 FAQ, fault tolerance](https://etcd.io/docs/v3.5/faq/#what-is-failure-tolerance)

### Standard

> Let $N$ be the number of servers, and let $T$ be the minimum votes required for a candidate to win. Each server can vote for at most one candidate during the term. Thus, for any two distinct candidates with vote counts $v_1$ and $v_2$,
> $$
> v_1+v_2\le N.
> $$
>
> **Two winners are impossible exactly when $2T>N$.** Indeed, if both candidates win, then $v_1,v_2\ge T$, so $v_1+v_2\ge 2T$. This contradicts $v_1+v_2\le N$ when $2T>N$. Conversely, if $2T\le N$, two candidates can each receive $T$ votes, so the threshold alone does not prevent two winners.
>
> For $T=4$:
>
> - With $N=7$, $2T=8>7$, so **four votes is safe against two winners**.
> - With $N=8$, $2T=8\not>8$, so **four votes is not safe**: four servers can vote for each candidate, producing two winners.
>
> A safe threshold does not guarantee a winner. For example, with seven servers and threshold four, if votes split $3$–$3$ and one server abstains, neither candidate reaches four. Thus a threshold can prevent multiple winners while still allowing no winner.
