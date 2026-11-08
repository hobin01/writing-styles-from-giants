# Which crossings should receive the pilot first?

2026-11-08 · `minto-pyramid` 0.2.1 at first pass · `gpt-6-luna` · Codex CLI 0.167.0

### Case and sources

- [FHWA, Leading Pedestrian Interval](https://highways.dot.gov/safety/proven-safety-countermeasures/leading-pedestrian-interval). Definition, timing, turning conflicts, visibility, accessibility and applicability at high-turning-volume crossings.
- [FHWA, Safety Evaluation of Protected Left-Turn Phasing and Leading Pedestrian Intervals on Pedestrian Safety (2018), FHWA-HRT-18-044](https://www.fhwa.dot.gov/publications/research/safety/18044/18044.pdf). Executive summary and combined leading-interval evaluation, including the Chicago, New York and Charlotte sites and pedestrian crash modification factor 0.87. The committee decision in the request is hypothetical.

**Reasoning task.** Translate a crash modification factor into absolute expected reductions using two different baselines, then separate the decision forecast from an observed local effect.

### Prompt

> Write a city committee's decision opening in at most 100 words. It can fund one pilot at a group of signalized crossings with heavy turning traffic; either group costs the same and the goal is to avert the larger expected number of vehicle–pedestrian crashes. WALK would begin 3–7 seconds before drivers get green. In FHWA's three-city study the estimated crash modification factor was 0.87. In this hypothetical comparison, without treatment North's crossings are expected to have 20 such crashes and South's 5 over the same period. Estimate what difference applying the study factor would make at each group. Recommend a site and say what comparison the committee should make before treating this forecast as a local result.

### Without a skill

> The committee recommends the North crossings for the pilot. Applying FHWA’s estimated crash modification factor of 0.87 implies a 13% reduction: about 2.6 fewer vehicle–pedestrian crashes in North, compared with 0.65 fewer in South over the same period. These are forecast differences, not local results. Before treating them as local evidence, compare treated crossings with similar untreated crossings over the same period, accounting for baseline crash risk and changes in traffic and pedestrian volumes.

### With the skill at standard

> The committee can fund one pilot at either group of signalized crossings, at the same cost. Which would avert more vehicle–pedestrian crashes, and what should be checked before treating the estimate as a local forecast?
>
> Use the FHWA study factor of 0.87, which implies an estimated 13% reduction: about 2.6 fewer crashes at North (20 × 0.13) versus 0.65 at South (5 × 0.13) over the same period. **Recommend North** to target the larger expected reduction. Before treating this as a local result, compare the study’s three-city sites and conditions with the proposed crossings, especially their traffic and crash patterns.

### First-pass assessment

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Correctly derives expected reductions of 2.6 at North and 0.65 at South (or gives both treated counts and these reductions). | Met | Met |
| Recommends North under the stated equal-cost objective and explains how the early WALK relates to turning vehicles or pedestrian visibility. | Missed | Missed |
| Labels the estimates conditional on transfer from the study and proposes a local treated-versus-credible-without-treatment comparison to test the effect. | Met | Missed |

Both recommend North and correctly forecast 2.6 versus 0.65 fewer crashes; neither explains how starting WALK before drivers get green helps at turning conflicts. The baseline proposes measuring treated crossings against comparable untreated crossings locally. The skill answer checks how similar the city is to the source-study sites, which helps judge transfer but cannot measure the pilot's local effect.

**차이.** 두 답 모두 North를 권고하고 예상 감소량 2.6건과 0.65건을 구했지만, 보행 신호를 먼저 주는 원리는 설명하지 않았습니다. 미적용 답은 시범 교차로와 지역 내 미시행 교차로를 비교하자고 합니다. 스킬 답의 기존 연구 도시와의 비교만으로는 해당 도시의 실제 효과를 측정할 수 없습니다.

<details>
<summary>Developmental retest · version 0.2.2</summary>

Distinguish transfer from an external study from the local comparison needed to test the forecast. The prompt now asks for the mechanism explicitly. This retest is excluded from the first-pass counts.

**Revised request (both answers regenerated)**

> Write a city committee's decision opening in at most 100 words. It can fund one pilot at a group of signalized crossings with heavy turning traffic; either group costs the same and the goal is to avert the larger expected number of vehicle–pedestrian crashes. WALK would begin 3–7 seconds before drivers get green. In FHWA's three-city study the estimated crash modification factor was 0.87. In this hypothetical comparison, without treatment North's crossings are expected to have 20 such crashes and South's 5 over the same period. Estimate what difference applying the study factor would make at each group. Recommend a site, explain why the head start might matter at turns, and specify a local comparison that could measure the effect of the pilot against what would have happened without it.

**New baseline**

> The committee should fund the pilot at North’s crossings. Applying FHWA’s estimated crash modification factor of 0.87 suggests about 2.6 fewer vehicle–pedestrian crashes at North (20 × 13%) over the period, compared with about 0.65 fewer at South (5 × 13%). The 3–7-second WALK head start may give pedestrians time to enter the crossing and become more visible before turning drivers receive green. To assess the pilot, compare North’s post-installation crash experience with its expected no-treatment outcome, using matched untreated crossings and pre-pilot trends to account for changes over time.

**New standard answer**

> **Fund one pilot at North.** Without treatment, North is expected to have 20 vehicle–pedestrian crashes over the period, compared with 5 at South. Applying the study’s estimated crash modification factor of 0.87 implies about 2.6 fewer crashes at North (20 × 0.13), versus 0.65 at South (5 × 0.13). These are estimates, not guaranteed local outcomes.
>
> Starting WALK 3–7 seconds before drivers get green may let pedestrians enter the crossing and become more visible before turning vehicles move.
>
> To measure the pilot’s local effect, compare North’s before-and-after crash change with the change over the same periods at comparable untreated signalized crossings, accounting for traffic and other changes. The study factor estimates expected impact; it does not establish what would have happened locally.

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Correctly derives expected reductions of 2.6 at North and 0.65 at South (or gives both treated counts and these reductions). | Met | Met |
| Recommends North under the stated equal-cost objective and explains how the early WALK relates to turning vehicles or pedestrian visibility. | Met | Met |
| Labels the estimates conditional on transfer from the study and proposes a local treated-versus-credible-without-treatment comparison to test the effect. | Met | Met |

Both the baseline and the skill answer apply the study estimate conditionally and obtain 2.6 fewer expected crashes at North versus 0.65 at South. Both recommend North, explain how the WALK head start can make pedestrians visible to turning drivers, and propose a comparison with untreated crossings over time. The baseline fits 100 words. The skill answer explicitly distinguishes the estimates from local outcomes and describes a before-and-after comparison, but exceeds 100 words.

**차이.** 미적용 답과 스킬 답 모두 연구 추정치를 적용했을 때 예상 사고 감소가 북쪽 2.6건과 남쪽 0.65건이라고 계산한다. 둘 다 북쪽을 권하고, 보행 신호를 먼저 주면 회전 운전자에게 보행자가 잘 보이는 이유와 미시행 횡단보도를 활용한 시기별 비교를 제시한다. 미적용 답은 100단어 이내다. 스킬 답은 추정치와 지역의 실제 결과를 명시적으로 구별하고 전후 비교를 설명하지만 100단어를 넘긴다.

</details>
