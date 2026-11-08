# Feynman-inspired explanation and gap checking · Why a full buffer overwrites an item

Run on 2026-11-08 • `feynman-technique` 0.1.1 • English • Codex CLI 0.167.0

### Prompt

> Explain a two-slot buffer to a new operator in a short paragraph, without asking them a question. Each arrival writes to the next slot; after the second slot, writing returns to the first. Starting empty, A, B and C arrive in that order. The policy for simultaneous arrivals is unknown.

### Without a skill

> A two-slot buffer stores items in two positions, writing to each slot in turn. Starting empty, A goes into the first slot and B into the second. Writing then returns to the first slot, so C replaces A, leaving C in the first slot and B in the second. How simultaneous arrivals are handled is unknown.

### With the skill at standard

> A two-slot buffer has two places to hold items. Each arrival writes to the next slot, returning to the first after the second and replacing anything already there. Starting empty, A goes into slot 1, B into slot 2, and C into slot 1, replacing A. The buffer then holds C in slot 1 and B in slot 2; the next arrival will write to slot 2. The policy for simultaneous arrivals is unknown, so we cannot say how those arrivals would be ordered or stored.

### What changed

**Checks set before the run.** Explain where A, B and C go and why C overwrites A; leave simultaneous arrivals unresolved. At standard a learner quiz is unnecessary.

Both trace A, B and C correctly and leave simultaneous arrivals unresolved. The skill goes one step further and predicts which slot the next arrival will use. A learner’s response was not observed.

**차이.** 두 답 모두 C가 왜 A를 덮어쓰는지 설명합니다. 스킬 답안은 다음 항목이 어느 칸에 들어갈지도 예측합니다.
