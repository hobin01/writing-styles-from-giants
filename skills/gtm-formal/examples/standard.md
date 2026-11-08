# GTM-inspired formal mathematical explanation · When preimages preserve intersections

Run on 2026-11-08 • `gtm-formal` 0.1.1 • English • Codex CLI 0.167.0

### Prompt

> For a graduate maths reader, prove in at most 110 words that for any function f:X→Y and any subsets A and B of Y, the inverse image of their intersection equals the intersection of their inverse images. State whether f must be injective and cover empty sets.

### Without a skill

> For every \(x\in X\),
> \[
> \begin{aligned}
> x\in f^{-1}(A\cap B)
> &\iff f(x)\in A\cap B\\
> &\iff f(x)\in A\ \text{and}\ f(x)\in B\\
> &\iff x\in f^{-1}(A)\cap f^{-1}(B).
> \end{aligned}
> \]
> Thus, by extensionality,
> \[
> f^{-1}(A\cap B)=f^{-1}(A)\cap f^{-1}(B).
> \]
> No injectivity assumption is needed. The argument also covers empty sets: \(f^{-1}(\varnothing)=\varnothing\), so if either \(A\) or \(B\) is empty, both sides are empty. If \(X=\varnothing\), both sides are likewise empty.

### With the skill at standard

> For \(S\subseteq Y\), define \(f^{-1}(S)=\{x\in X:f(x)\in S\}\). Let \(A,B\subseteq Y\). For every \(x\in X\),
> \[
> \begin{aligned}
> x\in f^{-1}(A\cap B)
> &\iff f(x)\in A\cap B\\
> &\iff f(x)\in A\ \text{and}\ f(x)\in B\\
> &\iff x\in f^{-1}(A)\cap f^{-1}(B).
> \end{aligned}
> \]
> Thus, by extensionality,
> \[
> f^{-1}(A\cap B)=f^{-1}(A)\cap f^{-1}(B).
> \]
> Injectivity is unnecessary: only the definition of inverse image is used. If \(A=\varnothing\) or \(B=\varnothing\), both sides are empty because \(f^{-1}(\varnothing)=\varnothing\). If \(X=\varnothing\), both sides are likewise empty.

### What changed

**Checks set before the run.** Quantify a general element of X and give equivalences in both directions; do not introduce an inverse function or require injectivity; account for empty sets.

Both prove the identity for each element of X, address empty sets, and explain why injectivity is unnecessary. The skill explicitly defines the inverse image before using it. The mathematical result is the same.

**차이.** 두 증명 모두 공집합과 단사성 조건을 다룹니다. 스킬 답안은 사용하는 기호의 뜻인 역상을 먼저 정의합니다.
