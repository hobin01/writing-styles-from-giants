# When does a vote threshold exclude two Raft leaders?

[한국어](standard.ko.md)

2026-11-08 · `gtm-formal` 0.1.2 · English · `gpt-6-luna`

### Case and sources

- [Ongaro and Ousterhout, In Search of an Understandable Consensus Algorithm, §5.2](https://raft.github.io/raft.pdf). Section 5.2 and Figure 3 distinguish election safety, one vote per term, majority election and split votes.
- [etcd v3.5 FAQ, fault tolerance](https://etcd.io/docs/v3.5/faq/#what-is-failure-tolerance). The fault-tolerance table gives a quorum of three for five etcd members. The varied vote threshold is a mathematical exercise; real Raft uses a majority.

### Prompt

> In a formal note for a distributed-systems seminar, derive a necessary and sufficient inequality on a proposed election threshold q so that any two qualifying voter sets in a fixed cluster of n voters overlap (1 ≤ q ≤ n). Derive a lower bound for the number of voters shared by two qualifying sets in terms of n and q. Each voter grants at most one vote per term. Use the illustrative etcd-east and etcd-west candidates to connect the bound to election safety. Apply your result to normal majority voting with five voters and to a hypothetical threshold of three in a fixed six-voter cluster. Give a concrete six-voter counterexample if needed. Finally say what election safety alone implies about making progress when voters are unavailable. Keep it concise. Write your answer in English.

### Without the skill

> Let $A$ and $B$ be any two qualifying voter sets in a fixed cluster of $n$ voters, each containing at least $q$ voters, where $1\le q\le n$. Since $A\cup B$ has at most $n$ voters,
>
> $$
> |A\cap B|=|A|+|B|-|A\cup B|\ge 2q-n.
> $$
>
> This bound is tight. Thus every two qualifying sets overlap **if and only if**
>
> $$
> 2q-n\ge1,\qquad\text{equivalently}\qquad q>\frac n2.
> $$
>
> When they overlap, they share at least $2q-n$ voters.
>
> For five voters, a majority threshold is $q=3$. Any two qualifying sets share at least $2(3)-5=1$ voter. If etcd-east and etcd-west each win an election using a majority, their voter sets therefore share a voter. Because each voter grants at most one vote per term, that shared voter cannot vote for both candidates in the same term; this prevents both candidates from winning that term.
>
> In a fixed six-voter cluster, threshold $q=3$ does not ensure overlap: the qualifying sets $\{1,2,3\}$ and $\{4,5,6\}$ are disjoint. A threshold of $q=4$ is needed to guarantee overlap, with at least $2(4)-6=2$ shared voters.
>
> Election safety alone does not guarantee progress: if too many voters are unavailable to form a qualifying set, no candidate can be elected.

<details>
<summary>Original math delimiters</summary>

````text
Let \(A\) and \(B\) be any two qualifying voter sets in a fixed cluster of \(n\) voters, each containing at least \(q\) voters, where \(1\le q\le n\). Since \(A\cup B\) has at most \(n\) voters,
\[
|A\cap B|=|A|+|B|-|A\cup B|\ge 2q-n.
\]
This bound is tight. Thus every two qualifying sets overlap **if and only if**
\[
2q-n\ge1,\qquad\text{equivalently}\qquad q>\frac n2.
\]
When they overlap, they share at least \(2q-n\) voters.

For five voters, a majority threshold is \(q=3\). Any two qualifying sets share at least \(2(3)-5=1\) voter. If etcd-east and etcd-west each win an election using a majority, their voter sets therefore share a voter. Because each voter grants at most one vote per term, that shared voter cannot vote for both candidates in the same term; this prevents both candidates from winning that term.

In a fixed six-voter cluster, threshold \(q=3\) does not ensure overlap: the qualifying sets \(\{1,2,3\}\) and \(\{4,5,6\}\) are disjoint. A threshold of \(q=4\) is needed to guarantee overlap, with at least \(2(4)-6=2\) shared voters.

Election safety alone does not guarantee progress: if too many voters are unavailable to form a qualifying set, no candidate can be elected.
````

</details>

### With the skill at standard

> Fix a cluster of $n\ge 1$ voters. A qualifying set is a subset of at least $q$ voters, where $q$ is an integer with $1\le q\le n$. For any two qualifying sets $A,B\subseteq V$, inclusion–exclusion gives
>
> $$
> |A\cap B|=|A|+|B|-|A\cup B|\ge 2q-n,
> $$
>
> since $|A\cup B|\le n$. Thus every pair overlaps if and only if
>
> $$
> \boxed{2q>n}\qquad\text{or, equivalently,}\qquad q>\frac n2.
> $$
>
> The bound on the overlap is $\max(0,2q-n)$. If $2q\le n$, two disjoint qualifying sets of size $q$ can be chosen, so overlap is not guaranteed.
>
> For example, with five voters, normal majority voting uses $q=3$. Any two qualifying sets share at least $2(3)-5=1$ voter. In a fixed six-voter cluster with hypothetical threshold $q=3$, the bound is zero: $\{\text{A},\text{B},\text{C}\}$ and $\{\text{D},\text{E},\text{F}\}$ are disjoint qualifying sets.
>
> Apply this to two candidates, etcd-east and etcd-west, each winning by collecting votes from a qualifying set. With a threshold satisfying $2q>n$, their voter sets intersect. Because each voter grants at most one vote per term, the shared voter cannot vote for both candidates in that term; hence both cannot win. With six voters and threshold three, disjoint winning sets are possible, so this overlap argument alone does not guarantee election safety.
>
> Election safety is a safety property: it rules out conflicting wins under its assumptions, but by itself guarantees no progress when voters are unavailable. Progress depends on whether enough voters remain available to form a qualifying set and on the election protocol’s other conditions.

<details>
<summary>Original math delimiters</summary>

````text
Fix a cluster of \(n\ge 1\) voters. A qualifying set is a subset of at least \(q\) voters, where \(q\) is an integer with \(1\le q\le n\). For any two qualifying sets \(A,B\subseteq V\), inclusion–exclusion gives
\[
|A\cap B|=|A|+|B|-|A\cup B|\ge 2q-n,
\]
since \(|A\cup B|\le n\). Thus every pair overlaps if and only if
\[
\boxed{2q>n}\qquad\text{or, equivalently,}\qquad q>\frac n2.
\]
The bound on the overlap is \(\max(0,2q-n)\). If \(2q\le n\), two disjoint qualifying sets of size \(q\) can be chosen, so overlap is not guaranteed.

For example, with five voters, normal majority voting uses \(q=3\). Any two qualifying sets share at least \(2(3)-5=1\) voter. In a fixed six-voter cluster with hypothetical threshold \(q=3\), the bound is zero: \(\{\text{A},\text{B},\text{C}\}\) and \(\{\text{D},\text{E},\text{F}\}\) are disjoint qualifying sets.

Apply this to two candidates, etcd-east and etcd-west, each winning by collecting votes from a qualifying set. With a threshold satisfying \(2q>n\), their voter sets intersect. Because each voter grants at most one vote per term, the shared voter cannot vote for both candidates in that term; hence both cannot win. With six voters and threshold three, disjoint winning sets are possible, so this overlap argument alone does not guarantee election safety.

Election safety is a safety property: it rules out conflicting wins under its assumptions, but by itself guarantees no progress when voters are unavailable. Progress depends on whether enough voters remain available to form a qualifying set and on the election protocol’s other conditions.
````

</details>

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Proves the sufficient bound \|E∩W\| ≥ 2q−n for two qualifying sets and connects 2q>n and one vote per term to exclusion of two leaders. | Met | Met |
| Establishes necessity when 2q≤n using disjoint sets, computes the five-voter majority of three and illustrates disjoint groups of three in the hypothetical six-voter case. | Missed | Met |
| Explicitly distinguishes the hypothetical six-voter threshold from Raft's real majority and states why election safety alone does not guarantee progress when too few votes are available. | Met | Met |

**Masked review** (Y = baseline; X = standard). Both derive the inclusion–exclusion bound, apply one vote per term and distinguish safety from election progress. X explicitly constructs disjoint sets for the general case 2q ≤ n and gives the sharp nonnegative bound. Y demonstrates the six-voter split but does not establish general necessity and calls 2q−n tight without the lower limit of zero. Y explicitly computes the safe six-voter threshold of four.

<details>
<summary>Run record</summary>

Each arm was a separate ephemeral read-only Codex CLI 0.167.0 session with low reasoning effort. Neither session was given the other answer or an answer in the other language.

SHA-256 prefixes (entrypoint / baseline answer / standard answer): `b351e00329c8` / `40b121481c1f` / `8b4494337284`.

</details>
