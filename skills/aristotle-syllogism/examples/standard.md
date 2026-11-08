# Aristotelian syllogistic argument checking · Following a hold rule backwards

Run on 2026-11-08 • `aristotle-syllogism` 0.1.1 • English • Codex CLI 0.167.0

### Prompt

> Assess this argument in a few sentences. Every sealed canister is on hold. Item D is on hold. Therefore D is sealed. Assume the two premises are true. Say whether the conclusion follows and give a small example if useful.

### Without a skill

> The conclusion does not follow. The premises say that being sealed guarantees being on hold, but they do not say that only sealed canisters are on hold. For example, D could be an unsealed canister placed on hold for inspection, while every sealed canister is also on hold. Both premises would be true, but the conclusion would be false.

### With the skill at standard

> The premises say that all sealed canisters are on hold and that D is on hold; the conclusion says D is sealed. The conclusion does not follow: being on hold does not establish that an item is sealed or even that it is a canister. For example, a sealed canister and an unsealed item D could both be on hold, satisfying both premises while D remains unsealed. The premises are assumed true; whether D is actually sealed requires additional evidence.

### What changed

**Checks set before the run.** Separate the truth of the premises from whether D must be sealed. A counterexample must keep both premises true while D is on hold but unsealed.

Both give a counterexample that makes the premises true and the conclusion false. The skill also notices that the premises never say D is a canister and that D's actual condition requires evidence. Either answer settles validity.

**차이.** 두 답 모두 반례로 결론이 따라오지 않음을 보입니다. 스킬을 쓴 답은 D가 통이라는 전제조차 없다는 점까지 짚습니다.
