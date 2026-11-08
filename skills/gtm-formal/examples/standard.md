# When does a vote threshold exclude two Raft leaders?

2026-11-08 · `gtm-formal` 0.1.1 at first pass · `gpt-6-luna` · Codex CLI 0.167.0

### Case and sources

- [Ongaro and Ousterhout, In Search of an Understandable Consensus Algorithm, §5.2](https://raft.github.io/raft.pdf). Section 5.2 and Figure 3 distinguish election safety, one vote per term, majority election and split votes.
- [etcd v3.5 FAQ, fault tolerance](https://etcd.io/docs/v3.5/faq/#what-is-failure-tolerance). The fault-tolerance table gives a quorum of three for five etcd members. The varied vote threshold is a mathematical exercise; real Raft uses a majority.

**Reasoning task.** Prove the general intersection criterion in both directions, specialize it to two configurations and separate a safety guarantee from the possibility of an election.

### Prompt

> In a formal note for a distributed-systems seminar, derive a necessary and sufficient inequality on a proposed election threshold q so that any two qualifying voter sets in a fixed cluster of n voters overlap (1 ≤ q ≤ n). Each voter grants at most one vote per term. Use the illustrative etcd-east and etcd-west candidates to connect the bound to election safety. Apply your result to normal majority voting with five voters and to a hypothetical threshold of three in a fixed six-voter cluster. Give a concrete six-voter counterexample if needed. Finally say what election safety alone implies about making progress when voters are unavailable. Keep the proof under 170 words.

### Without a skill

> In a fixed cluster of $n$ voters, any two qualifying sets of size at least $q$ overlap **if and only if**
>
> $$
> 2q>n.
> $$
>
> If $2q\le n$, two disjoint sets of $q$ voters can fit in the cluster; if $2q>n$, two disjoint sets would require more than $n$ voters.
>
> For five voters, normal majority voting requires $q=3$, and $2q=6>5$. Thus, if etcd-east and etcd-west each win with three votes, their voter sets share at least one voter. Since each voter grants at most one vote per term, that shared voter cannot vote for both candidates in the same term. This prevents both candidates from winning in that term.
>
> In a fixed six-voter cluster, a threshold of three does not ensure overlap: etcd-east could receive votes from voters $\{1,2,3\}$, while etcd-west receives votes from $\{4,5,6\}$. The sets are disjoint, so both could qualify without any voter casting two votes.
>
> Election safety alone does not guarantee progress when voters are unavailable. It gives a condition for preventing conflicting elections; if too few voters can participate to form a qualifying set, no election can be completed.

<details>
<summary>Original model text</summary>

````text
In a fixed cluster of \(n\) voters, any two qualifying sets of size at least \(q\) overlap **if and only if**
\[
2q>n.
\]
If \(2q\le n\), two disjoint sets of \(q\) voters can fit in the cluster; if \(2q>n\), two disjoint sets would require more than \(n\) voters.

For five voters, normal majority voting requires \(q=3\), and \(2q=6>5\). Thus, if etcd-east and etcd-west each win with three votes, their voter sets share at least one voter. Since each voter grants at most one vote per term, that shared voter cannot vote for both candidates in the same term. This prevents both candidates from winning in that term.

In a fixed six-voter cluster, a threshold of three does not ensure overlap: etcd-east could receive votes from voters \(\{1,2,3\}\), while etcd-west receives votes from \(\{4,5,6\}\). The sets are disjoint, so both could qualify without any voter casting two votes.

Election safety alone does not guarantee progress when voters are unavailable. It gives a condition for preventing conflicting elections; if too few voters can participate to form a qualifying set, no election can be completed.
````

</details>

### With the skill at standard

> **Method/status:** gtm-formal, standard level (version 0.1.1).
>
> Let $V$ be a fixed cluster of $n$ voters, and let a qualifying set contain at least $q$ distinct voters, where $1\le q\le n$. The condition that each voter grants at most one vote per term means two elections in the same term cannot both be supported by the same voter.
>
> **Claim.** Every two qualifying subsets of $V$ overlap if and only if
>
> $$
> 2q>n.
> $$
>
>
> **Proof.** If $A,B\subseteq V$ are qualifying and disjoint, then $|A\cup B|=|A|+|B|\ge 2q$, while $|A\cup B|\le n$. Thus disjoint qualifying sets are impossible when $2q>n$. Conversely, if $2q\le n$, choose disjoint subsets $A,B$ of size $q$; they are qualifying, so universal overlap fails. Hence the inequality is necessary and sufficient. ∎
>
> For five voters, normal majority requires $q=3$, and $2q=6>5$. Thus two elections in one term cannot both obtain disjoint voter support: in the illustrative case, etcd-east and etcd-west cannot both win under the one-vote-per-term assumption.
>
> For six voters and hypothetical $q=3$, $2q=6$, so overlap is not guaranteed. For example, $\{\text{A,B,C}\}$ and $\{\text{D,E,F}\}$ are disjoint qualifying sets.
>
> Election safety alone does not guarantee progress: unavailable voters may prevent any candidate from obtaining a qualifying set.

<details>
<summary>Original model text</summary>

````text
**Method/status:** gtm-formal, standard level (version 0.1.1).

Let \(V\) be a fixed cluster of \(n\) voters, and let a qualifying set contain at least \(q\) distinct voters, where \(1\le q\le n\). The condition that each voter grants at most one vote per term means two elections in the same term cannot both be supported by the same voter.

**Claim.** Every two qualifying subsets of \(V\) overlap if and only if
\[
2q>n.
\]

**Proof.** If \(A,B\subseteq V\) are qualifying and disjoint, then \(|A\cup B|=|A|+|B|\ge 2q\), while \(|A\cup B|\le n\). Thus disjoint qualifying sets are impossible when \(2q>n\). Conversely, if \(2q\le n\), choose disjoint subsets \(A,B\) of size \(q\); they are qualifying, so universal overlap fails. Hence the inequality is necessary and sufficient. ∎

For five voters, normal majority requires \(q=3\), and \(2q=6>5\). Thus two elections in one term cannot both obtain disjoint voter support: in the illustrative case, etcd-east and etcd-west cannot both win under the one-vote-per-term assumption.

For six voters and hypothetical \(q=3\), \(2q=6\), so overlap is not guaranteed. For example, \(\{\text{A,B,C}\}\) and \(\{\text{D,E,F}\}\) are disjoint qualifying sets.

Election safety alone does not guarantee progress: unavailable voters may prevent any candidate from obtaining a qualifying set.
````

</details>

### First-pass assessment

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Proves the sufficient bound \|E∩W\| ≥ 2q−n for two qualifying sets and connects 2q>n and one vote per term to exclusion of two leaders. | Missed | Missed |
| Establishes necessity when 2q≤n using disjoint sets, computes the five-voter majority of three and illustrates disjoint groups of three in the hypothetical six-voter case. | Met | Met |
| Explicitly distinguishes the hypothetical six-voter threshold from Raft's real majority and states why election safety alone does not guarantee progress when too few votes are available. | Missed | Met |

Both correctly prove the requested iff by ruling out disjoint sets when 2q exceeds n and constructing them otherwise. Neither states the stronger numerical lower bound |E ∩ W| ≥ 2q − n in the first scoring check; this is not a flaw in either proof of overlap. Both give the six-voter split and separate safety from progress. The skill answer calls the threshold of three hypothetical; the baseline does not explicitly distinguish it from the real six-voter majority. The skill answer also inserts an unrequested method/version label. Both exceed 170 whitespace-separated words.

**차이.** 두 증명 모두 두 집합이 겹칠 필요충분조건을 올바르게 보였습니다. 첫 채점 항목은 문제에서 꼭 필요하지 않은 더 강한 교집합 크기 하한까지 요구했고, 둘 다 이를 쓰지 않았습니다. 여섯 명을 3명씩 나눈 반례와 진행 가능성의 한계는 공통입니다. 스킬 답은 3표 기준이 가정임을 밝혔고 미적용 답은 실제 6명 과반수와 명시적으로 구분하지 않았습니다. 스킬 답은 요청하지 않은 스킬 버전도 썼습니다. 두 답 모두 공백 기준으로 170단어를 넘겼습니다.

<details>
<summary>Developmental retest · version 0.1.2</summary>

Clarify the demand for a quantitative lower bound and keep an explicit proof within its requested format. This retest is excluded from the first-pass counts.

**Revised request (both answers regenerated)**

> In a formal note for a distributed-systems seminar, derive a necessary and sufficient inequality on a proposed election threshold q so that any two qualifying voter sets in a fixed cluster of n voters overlap (1 ≤ q ≤ n). Derive a lower bound for the number of voters shared by two qualifying sets in terms of n and q. Each voter grants at most one vote per term. Use the illustrative etcd-east and etcd-west candidates to connect the bound to election safety. Apply your result to normal majority voting with five voters and to a hypothetical threshold of three in a fixed six-voter cluster. Give a concrete six-voter counterexample if needed. Finally say what election safety alone implies about making progress when voters are unavailable. Keep the proof under 170 words.

**New baseline**

> ### Quorum overlap and election safety
>
> Let $A,B\subseteq V$ be qualifying voter sets, each of size at least $q$, where $|V|=n$. Since
>
> $$
> |A\cap B|=|A|+|B|-|A\cup B|\ge 2q-n,
> $$
>
> any two qualifying sets share at least $\max(0,2q-n)$ voters. Thus every pair must overlap exactly when $2q>n$, or equivalently $q>n/2$. This is necessary: if $2q\le n$, the voters can be divided into two disjoint sets of size $q$.
>
> For five voters, majority means $q=3$: any two majorities share at least $2(3)-5=1$ voter. In a fixed six-voter cluster, threshold $q=3$ does not ensure overlap: $\{\text{A},\text{B},\text{C}\}$ and $\{\text{D},\text{E},\text{F}\}$ are disjoint qualifying sets.
>
> For example, if etcd-east and etcd-west each win with three votes in that six-voter cluster, each voter’s one-vote-per-term limit does not prevent the two elections: the disjoint sets can vote for different candidates. A threshold of four would force at least two shared voters; because each can grant at most one vote per term, both candidates cannot receive those shared votes in the same term.
>
> Election safety is about preventing conflicting elections; by itself, it does not guarantee progress when voters are unavailable.

<details>
<summary>Original model text</summary>

````text
### Quorum overlap and election safety

Let \(A,B\subseteq V\) be qualifying voter sets, each of size at least \(q\), where \(|V|=n\). Since
\[
|A\cap B|=|A|+|B|-|A\cup B|\ge 2q-n,
\]
any two qualifying sets share at least \(\max(0,2q-n)\) voters. Thus every pair must overlap exactly when \(2q>n\), or equivalently \(q>n/2\). This is necessary: if \(2q\le n\), the voters can be divided into two disjoint sets of size \(q\).

For five voters, majority means \(q=3\): any two majorities share at least \(2(3)-5=1\) voter. In a fixed six-voter cluster, threshold \(q=3\) does not ensure overlap: \(\{\text{A},\text{B},\text{C}\}\) and \(\{\text{D},\text{E},\text{F}\}\) are disjoint qualifying sets.

For example, if etcd-east and etcd-west each win with three votes in that six-voter cluster, each voter’s one-vote-per-term limit does not prevent the two elections: the disjoint sets can vote for different candidates. A threshold of four would force at least two shared voters; because each can grant at most one vote per term, both candidates cannot receive those shared votes in the same term.

Election safety is about preventing conflicting elections; by itself, it does not guarantee progress when voters are unavailable.
````

</details>

**New standard answer**

> **Claim.** Let $V$ be a fixed set of $n$ voters, and call $A\subseteq V$ qualifying when $|A|\ge q$, where $1\le q\le n$ is an integer. Every two qualifying sets overlap if and only if
>
> $$
> 2q>n.
> $$
>
> Moreover, for all qualifying $A,B\subseteq V$,
>
> $$
> |A\cap B|\ge 2q-n.
> $$
>
>
> **Proof.** Since $|A\cup B|\le n$,
>
> $$
> |A\cap B|=|A|+|B|-|A\cup B|\ge 2q-n.
> $$
>
> Thus $2q>n$ guarantees overlap. Conversely, if $2q\le n$, partition $2q$ voters into disjoint sets $A,B$ of size $q$; any remaining voters lie outside both. These are disjoint qualifying sets, so universal overlap fails. The bound is sharp when $2q>n$: two $q$-element sets can have intersection exactly $2q-n$.
>
> For five voters, majority means $q=3$, so any two qualifying sets share at least $2(3)-5=1$ voter. In a fixed six-voter cluster with threshold $q=3$, the bound is zero: $\{\text{etcd-east-1, etcd-east-2, etcd-east-3}\}$ and $\{\text{etcd-west-1, etcd-west-2, etcd-west-3}\}$ are disjoint qualifying sets. If each voter grants at most one vote per term, overlap prevents two candidates from each receiving $q$ votes in that term, assuming both vote sets are drawn from the same fixed cluster. This is the quorum-intersection basis for election safety. Safety alone does not guarantee progress when voters are unavailable; enough available voters and the system’s other progress conditions are also needed.

<details>
<summary>Original model text</summary>

````text
**Claim.** Let \(V\) be a fixed set of \(n\) voters, and call \(A\subseteq V\) qualifying when \(|A|\ge q\), where \(1\le q\le n\) is an integer. Every two qualifying sets overlap if and only if
\[
2q>n.
\]
Moreover, for all qualifying \(A,B\subseteq V\),
\[
|A\cap B|\ge 2q-n.
\]

**Proof.** Since \(|A\cup B|\le n\),
\[
|A\cap B|=|A|+|B|-|A\cup B|\ge 2q-n.
\]
Thus \(2q>n\) guarantees overlap. Conversely, if \(2q\le n\), partition \(2q\) voters into disjoint sets \(A,B\) of size \(q\); any remaining voters lie outside both. These are disjoint qualifying sets, so universal overlap fails. The bound is sharp when \(2q>n\): two \(q\)-element sets can have intersection exactly \(2q-n\).

For five voters, majority means \(q=3\), so any two qualifying sets share at least \(2(3)-5=1\) voter. In a fixed six-voter cluster with threshold \(q=3\), the bound is zero: \(\{\text{etcd-east-1, etcd-east-2, etcd-east-3}\}\) and \(\{\text{etcd-west-1, etcd-west-2, etcd-west-3}\}\) are disjoint qualifying sets. If each voter grants at most one vote per term, overlap prevents two candidates from each receiving \(q\) votes in that term, assuming both vote sets are drawn from the same fixed cluster. This is the quorum-intersection basis for election safety. Safety alone does not guarantee progress when voters are unavailable; enough available voters and the system’s other progress conditions are also needed.
````

</details>

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Proves the sufficient bound \|E∩W\| ≥ 2q−n for two qualifying sets and connects 2q>n and one vote per term to exclusion of two leaders. | Met | Met |
| Establishes necessity when 2q≤n using disjoint sets, computes the five-voter majority of three and illustrates disjoint groups of three in the hypothetical six-voter case. | Missed | Met |
| Explicitly distinguishes the hypothetical six-voter threshold from Raft's real majority and states why election safety alone does not guarantee progress when too few votes are available. | Missed | Missed |

Both the skill answer and the baseline derive the 2q−n overlap bound and illustrate disjoint triples among six voters. The skill answer proves necessity with 2q chosen voters and explicitly leaves the rest unused. The baseline says all voters can be divided into two q-sized sets when 2q≤n, which fails as a partition if 2q<n. The skill answer names example voters rather than the two candidates; the baseline correctly uses the candidate names and shows why four votes suffice with six voters. Neither explicitly identifies four as Raft’s actual six-voter majority. The skill answer connects unavailable votes to failure to elect; the baseline states only that progress is not guaranteed. Counting the full notes, including headings and one word per formula, gives about 186 and 173 words; the baseline’s body alone is under 170.

**차이.** 스킬 답과 미적용 답 모두 교집합 크기의 하한 2q−n을 유도하고 6명 중 서로 겹치지 않는 3명씩의 예를 든다. 스킬 답은 2q명을 골라 나머지를 제외해 필요성을 보인다. 미적용 답은 2q≤n이면 전체를 크기 q인 두 집합으로 나눌 수 있다고 하는데, 2q<n이면 전원을 그렇게 나눌 수 없다. 스킬 답은 후보 이름 대신 투표자에게 예시 이름을 붙인다. 미적용 답은 후보 이름을 올바르게 쓰고 6명 중 4표면 충분한 이유를 보인다. 둘 다 4표가 실제 Raft의 6인 과반수임을 명시하지 않는다. 스킬 답은 필요한 표가 모자라면 선출할 수 없다고 짚고 미적용 답은 진전이 보장되지 않는다고만 한다. 제목을 포함하고 수식 하나를 한 단어로 세면 전문은 각각 약 186단어와 173단어이며, 미적용 답의 본문만 세면 170단어 미만이다.

</details>
