# Proving at most one Raft leader per term in five-member etcd

2026-11-08 · `gtm-formal` 0.1.1 · English · Codex CLI 0.167.0 / gpt-6.1-sol

### Case and sources

- [Ongaro and Ousterhout, In Search of an Understandable Consensus Algorithm, §5.2](https://raft.github.io/raft.pdf). Section 5.2 and Figure 3 distinguish election safety, one vote per term, majority election and split votes.
- [etcd v3.5 FAQ, fault tolerance](https://etcd.io/docs/v3.5/faq/#what-is-failure-tolerance). The fault-tolerance table gives a quorum of three for five etcd members. The split vote is an illustrative configuration.

### Prompt

> For a distributed systems seminar, prove in at most 130 words why two candidates cannot both be elected leader in the same Raft term in a fixed five-voter etcd cluster. Use the illustrative member names etcd-east and etcd-west throughout the proof for the two candidates. Assume a candidate needs at least three distinct votes and each voter grants at most one vote per term. Show the intersection bound for the two voter sets and connect it to the vote rule. Finally explain whether this proof guarantees that a 2–2 split with the fifth voter unreachable elects anyone in that term. This is a worked configuration, not a claim about a live cluster.

### Without a skill

> Suppose etcd-east and etcd-west are both elected in the same term. Let $E$ and $W$ be their respective voter sets. Each requires at least three distinct votes among the five fixed voters, so
>
> $$
> |E\cap W|=|E|+|W|-|E\cup W|\ge 3+3-5=1.
> $$
>
> Thus at least one voter must have voted for both etcd-east and etcd-west in that term, contradicting the rule that each voter grants at most one vote per term. Therefore, both cannot be elected in the same term.
>
> This proves uniqueness, not that an election succeeds. In a 2–2 split between etcd-east and etcd-west with the fifth voter unreachable, neither has the required three votes; if that split persists, neither is elected in that term.

<details>
<summary>Original model text (math delimiters as returned)</summary>

````text
Suppose etcd-east and etcd-west are both elected in the same term. Let \(E\) and \(W\) be their respective voter sets. Each requires at least three distinct votes among the five fixed voters, so
\[
|E\cap W|=|E|+|W|-|E\cup W|\ge 3+3-5=1.
\]
Thus at least one voter must have voted for both etcd-east and etcd-west in that term, contradicting the rule that each voter grants at most one vote per term. Therefore, both cannot be elected in the same term.

This proves uniqueness, not that an election succeeds. In a 2–2 split between etcd-east and etcd-west with the fifth voter unreachable, neither has the required three votes; if that split persists, neither is elected in that term.
````

</details>

### With the skill at standard

> Let $V$ be the fixed voter set, with $|V|=5$, and fix a term $t$. Each voter grants at most one vote in $t$; election requires at least three distinct votes.
>
> Suppose etcd-east and etcd-west are both elected in $t$. Let $E,W\subseteq V$ be their respective voter sets. Then $|E|,|W|\ge3$, so
>
> $$
> |E\cap W|
> =|E|+|W|-|E\cup W|
> \ge3+3-5=1.
> $$
>
> Thus some voter voted for both etcd-east and etcd-west in $t$, contradicting the vote rule. Hence they cannot both be elected in that term.
>
> This proves uniqueness, not guaranteed election. In a 2–2 split between etcd-east and etcd-west, with the fifth voter unreachable, neither has three votes; neither is elected while that split persists.

<details>
<summary>Original model text (math delimiters as returned)</summary>

````text
Let \(V\) be the fixed voter set, with \(|V|=5\), and fix a term \(t\). Each voter grants at most one vote in \(t\); election requires at least three distinct votes.

Suppose etcd-east and etcd-west are both elected in \(t\). Let \(E,W\subseteq V\) be their respective voter sets. Then \(|E|,|W|\ge3\), so
\[
|E\cap W|
=|E|+|W|-|E\cup W|
\ge3+3-5=1.
\]
Thus some voter voted for both etcd-east and etcd-west in \(t\), contradicting the vote rule. Hence they cannot both be elected in that term.

This proves uniqueness, not guaranteed election. In a 2–2 split between etcd-east and etcd-west, with the fifth voter unreachable, neither has three votes; neither is elected while that split persists.
````

</details>

### What changed

**Checks set before the run.** Identify the two vote sets with their named candidates. Prove that two voter sets of at least 3 in a 5-voter universe overlap in at least 1 voter, contradicting one vote per term for distinct candidates. Distinguish election safety from progress: in the stated split neither has a majority; other terms or changing memberships are outside scope.

Both answers identify the candidates as etcd-east and etcd-west, define their vote sets and show why two sets of three among five share at least one voter. Both distinguish a unique possible leader from a guaranteed election in a 2–2 split. The skill starts by explicitly fixing the voter universe and term; the baseline begins directly with the two supposed winners. The earlier symbolic pair is retained below.

**차이.** 두 답 모두 etcd-east와 etcd-west가 각각 3표를 받았다면 5명 중 적어도 한 명이 두 후보에게 투표했다는 모순을 보입니다. 2대 2로 갈리면 승자가 없어도 된다는 점도 같습니다. 스킬 답은 증명 첫 줄에서 투표자 집합과 임기를 먼저 고정합니다.

<details>
<summary>Earlier attempts on this case</summary>

The first pair defined its voters correctly, but still referred to abstract candidates. We named the two example etcd members in the final prompt and reran both arms.

**Attempt 1 — request**

> For a distributed systems seminar, prove in at most 130 words why two candidates cannot both be elected leader in the same Raft term in a fixed five-voter etcd cluster. Assume a candidate needs at least three distinct votes and each voter grants at most one vote per term. Show the intersection bound for the two voter sets and connect it to the vote rule. Finally explain whether this proof guarantees that a 2–2 split with the fifth voter unreachable elects anyone in that term. This is a worked configuration, not a claim about a live cluster.

**Without a skill**

````text
Suppose distinct candidates \(A\) and \(B\) are both elected in term \(t\). Let \(V_A\) and \(V_B\) be their voter sets. Each contains at least three distinct voters from the fixed five-voter cluster, so
\[
|V_A\cap V_B|
=|V_A|+|V_B|-|V_A\cup V_B|
\ge 3+3-5=1.
\]
Thus at least one voter voted for both candidates in term \(t\), contradicting the rule that each voter grants at most one vote per term. Therefore, two candidates cannot both be elected leader in the same term.

This proves uniqueness, not election progress. In a 2–2 split with the fifth voter unreachable, neither candidate has the required three votes. No candidate is elected while that split persists; the proof does not guarantee an election in that term.
````

**With the skill at standard**

````text
Let \(V\) be the fixed set of five voters, and fix a term \(t\). Suppose distinct candidates \(A\) and \(B\) are both elected in \(t\). Let \(S_A,S_B\subseteq V\) be their respective voter sets. By assumption, \(|S_A|,|S_B|\ge3\). Hence
\[
|S_A\cap S_B|
=|S_A|+|S_B|-|S_A\cup S_B|
\ge3+3-5=1.
\]
Thus some voter granted votes to both distinct candidates in term \(t\), contradicting the rule that each voter grants at most one vote per term. Therefore at most one candidate can be elected in any given term.

This proves uniqueness, not guaranteed election. In a 2–2 split with the fifth voter unreachable, neither candidate has the required three votes; if that split persists, no leader is elected in that term.
````

</details>
