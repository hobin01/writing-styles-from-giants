# Should a city pilot an earlier WALK signal?

2026-11-08 · `minto-pyramid` 0.2.1 · English · Codex CLI 0.167.0 / gpt-6.1-sol

### Case and sources

- [FHWA, Leading Pedestrian Interval](https://highways.dot.gov/safety/proven-safety-countermeasures/leading-pedestrian-interval). Definition, timing, turning conflicts, visibility, accessibility and applicability at high-turning-volume crossings.
- [FHWA, Safety Evaluation of Protected Left-Turn Phasing and Leading Pedestrian Intervals on Pedestrian Safety (2018), FHWA-HRT-18-044](https://www.fhwa.dot.gov/publications/research/safety/18044/18044.pdf). Executive summary and combined leading-interval evaluation, including the Chicago, New York and Charlotte sites and pedestrian crash modification factor 0.87. The committee decision in the request is hypothetical.

### Prompt

> For a hypothetical city traffic committee, write an opening paragraph recommending whether to pilot a leading pedestrian interval at signalized crossings with many turning vehicles. In this arrangement WALK begins 3–7 seconds before drivers get green, so someone crossing can become visible before drivers turn. A 2018 FHWA evaluation across treated sites in Chicago, New York City and Charlotte estimated about 13% fewer vehicle–pedestrian crashes than expected without the treatment. This committee has not measured outcomes at its own crossings. Give a concrete next step and keep the opening under 90 words.

### Without a skill

> The committee should pilot a leading pedestrian interval at signalized crossings with many turning vehicles, giving pedestrians a 3–7-second head start to become visible before drivers turn. A 2018 FHWA evaluation of treated sites in Chicago, New York City and Charlotte estimated about 13% fewer vehicle–pedestrian crashes than expected without the treatment, though local results remain unmeasured. Next, select pilot crossings and establish baseline crash, turning-conflict and delay measures to compare with outcomes after installation.

### With the skill at standard

> At signalized crossings with many turning vehicles, a leading pedestrian interval starts WALK 3–7 seconds before drivers get green, helping pedestrians become visible before drivers turn. Should the city pilot it? A 2018 FHWA evaluation across treated sites in Chicago, New York City and Charlotte estimated about 13% fewer vehicle–pedestrian crashes than expected without treatment, but local outcomes remain unmeasured. Recommend a pilot at selected crossings, beginning with baseline crash and turning-conflict measurements and a plan to compare outcomes after implementation.

### What changed

**Checks set before the run.** Give the pilot decision, the 3–7-second mechanism, the three-city estimate and its vehicle–pedestrian crash outcome. Distinguish a proposed local check from an already measured local effect.

Both propose a pilot, give the three-city estimate and call for baseline measurements at the new sites. The baseline leads with the recommendation and includes delay among its suggested measures. The skill answer explains the WALK interval, asks the decision question, then gives its recommendation. Both keep the 13% estimate distinct from the local outcome.

**차이.** 두 답 모두 13%를 세 도시의 추정치로 남겨 두고, 새 교차로에서는 별도로 측정하자고 합니다. 미적용 답안은 시범 도입을 먼저 권하고, 스킬 답안은 신호의 원리와 결정할 질문을 제시한 뒤 권고합니다.
