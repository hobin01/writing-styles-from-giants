# Can Finland’s basic-income result justify a forecast for 500 workers?

2026-11-08 · `socratic-self-questioning` 0.1.1 at first pass · `gpt-6-luna` · Codex CLI 0.167.0

### Case and sources

- [Finnish Ministry of Social Affairs and Health and Kela, Results of the basic income experiment (6 May 2020)](https://valtioneuvosto.fi/en/-/1271139/perustulokokeilun-tulokset-tyollisyysvaikutukset-vahaisia-toimeentulo-ja-psyykkinen-terveys-koettiin-paremmaksi?languageId=en_US). Employment results and experiment design: participating population, €560 payment, November 2017–October 2018 comparison, first-year finding, and asymmetric 2018 activation-policy change.

**Reasoning task.** Recover the comparison mean and extrapolated total, then distinguish statistical arithmetic, causal identification and transfer to a different population.

### Prompt

> A policy brief predicts ‘If we pay 500 local residents, their employment will rise by 3,000 days.’ Evaluate this inference in a finished paragraph of at most 110 words. In Finland's 2017–2018 experiment, 2,000 randomly selected unemployed benefit recipients got €560 per month. During November 2017–October 2018 recipients averaged 78 employment days, six more than the comparison group. Year one showed no group-level employment effect. A 2018 unemployment-benefit reform affected the groups differently, so researchers could not separate that reform's effect from the second-year basic-income effect. Reconstruct the arithmetic behind the forecast and explain what would have to be true for it to apply locally.

### Without a skill

> The forecast likely multiplies Finland’s second-year difference—six additional employment days per recipient—by 500 residents, yielding 3,000 days. But that arithmetic is not a local prediction: Finland’s first year showed no group-level employment effect, and the second-year estimate cannot be separated from the 2018 benefit reform, which affected the groups differently. Applying it locally would require the six-day difference to represent a causal basic-income effect, and for local recipients, benefit rules, labor markets, payment levels, and follow-up period to be sufficiently comparable. Without that evidence, 3,000 days is an extrapolation, not an established expected gain.

### With the skill at standard

> The forecast appears to scale Finland’s second-year difference of six employment days per recipient to 500 residents: 500 × 6 = 3,000 days. But “six more” was an average difference from the comparison group, not proof that basic income caused six extra days for each recipient. Year one showed no group-level employment effect, and in year two a benefit reform affected the groups differently, so researchers could not isolate the basic-income effect. The local forecast would require the six-day difference to represent a causal effect that transfers to these residents under a comparable payment, population, period, and policy context. The Finnish results alone do not establish that.

### First-pass assessment

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Recovers a comparison mean of 72 days and identifies 3,000 as 500 times the six-day observed difference, not an observed local gain. | Missed | Missed |
| Addresses both the lack of a first-year group-level effect and the asymmetric 2018 reform as a reason the second-year difference does not isolate basic income's effect. | Met | Met |
| Limits the evidence to unemployed benefit recipients and identifies a transfer assumption for 500 local residents, without claiming the experiment proves no effect in any year. | Missed | Missed |

Both recover 500 × 6 = 3,000, reject a guaranteed local gain, and explain the null first-year result and the asymmetric benefit reform. Neither gives the comparison mean of 72 days required by the rubric, although it isn't necessary to reconstruct the forecast itself. Both mention transfer assumptions but leave out that the Finnish participants were unemployed benefit recipients. The skill answer specifies a comparable payment, population and period; the baseline also mentions labour markets.

**차이.** 두 답 모두 500×6=3,000을 복원하고 1년 차 결과와 2년 차 제도 변경을 설명합니다. 다만 채점 기준에 있던 비교집단 평균 72일은 그 곱셈에 직접 필요하지 않아 둘 다 쓰지 않았습니다. 지역으로 일반화하려면 집단이 비슷해야 한다고 말하면서, 핀란드 참여자가 실업급여 수급자였다는 점도 명시하지 않았습니다.

<details>
<summary>Developmental retest · version 0.1.2</summary>

Identify who was studied before transferring the finding to a new population. The clarified prompt explicitly requests the comparison-group mean. This retest is excluded from the first-pass counts.

**Revised request (both answers regenerated)**

> A policy brief predicts ‘If we pay 500 local residents, their employment will rise by 3,000 days.’ Evaluate this inference in a finished paragraph of at most 110 words. In Finland's 2017–2018 experiment, 2,000 randomly selected unemployed benefit recipients got €560 per month. During November 2017–October 2018 recipients averaged 78 employment days, six more than the comparison group. Year one showed no group-level employment effect. A 2018 unemployment-benefit reform affected the groups differently, so researchers could not separate that reform's effect from the second-year basic-income effect. Identify the comparison group’s mean employment days, show how the forecast total was derived and explain what would have to be true for it to apply locally.

**New baseline**

> The comparison group averaged 72 employment days (78 minus six). The forecast appears to apply the estimated six-day difference to 500 people: 500 × 6 = 3,000 additional employment days. But Finland’s first year showed no group-level employment effect, and the second-year estimate cannot be separated from the effect of a benefit reform that affected the groups differently. The forecast therefore treats an uncertain, context-specific estimate as causal and transferable. For it to apply locally, paying 500 residents would need to produce the same six-day average increase there, under comparable conditions, with no offsetting effects.

**New standard answer**

> The forecast assumes a gain of six employment days per person: 500 residents × 6 days = 3,000 days. In Finland’s 2017–2018 experiment, recipients averaged 78 employment days, six more than the comparison group, whose mean was therefore 72 days. But year one showed no group-level employment effect, and in year two a benefit reform affected the groups differently, so researchers could not isolate basic income’s effect. The six-day difference is an observed comparison, not a settled causal effect. Applying it locally would require the local residents and program to be comparable to the Finnish participants and conditions, and the difference to reflect the payment rather than other factors.

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Recovers a comparison mean of 72 days and identifies 3,000 as 500 times the six-day observed difference, not an observed local gain. | Met | Met |
| Addresses both the lack of a first-year group-level effect and the asymmetric 2018 reform as a reason the second-year difference does not isolate basic income's effect. | Met | Met |
| Limits the evidence to unemployed benefit recipients and identifies a transfer assumption for 500 local residents, without claiming the experiment proves no effect in any year. | Missed | Missed |

The baseline and the skill answer both recover the 72-day comparison mean, derive 3,000 as 500 times the six-day observed difference, and explain the null first-year group result and differential second-year reform. Both describe conditions for local transfer, but neither identifies the original population as unemployed benefit recipients. The skill answer’s sentence giving the 78-day mean names the experiment’s full 2017–2018 span without specifying the November 2017–October 2018 measurement period.

**차이.** 미적용 답과 스킬 답 모두 비교집단 평균 72일을 구하고, 3,000일이 관측 차이 6일에 500명을 곱한 외삽임을 밝힌다. 첫해 집단 수준 효과가 관찰되지 않은 점과 둘째 해 제도 개편의 집단별 영향도 설명한다. 둘 다 지역 적용 조건은 제시하지만 원래 모집단이 실업급여 수급자였다고 밝히지 않는다. 스킬 답은 평균 78일을 설명하는 문장에서 실험 전체인 2017~2018년을 언급하면서 측정 기간인 2017년 11월~2018년 10월은 명시하지 않는다.

</details>
