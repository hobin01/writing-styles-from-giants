# Can Finland’s basic-income result justify a forecast for 500 workers?

[한국어](standard.ko.md)

2026-11-09 · `socratic-self-questioning` 0.1.6 · English · `gpt-6-luna`

### Case and sources

- [Finnish Ministry of Social Affairs and Health and Kela, Results of the basic income experiment (6 May 2020)](https://valtioneuvosto.fi/en/-/1271139/perustulokokeilun-tulokset-tyollisyysvaikutukset-vahaisia-toimeentulo-ja-psyykkinen-terveys-koettiin-paremmaksi?languageId=en_US). Employment results and experiment design: participating population, €560 payment, November 2017–October 2018 comparison, first-year finding, and asymmetric 2018 activation-policy change.

### Prompt

> A policy brief predicts ‘If we pay 500 local residents, their employment will rise by 3,000 days.’ Evaluate this inference in one concise English paragraph for publication. In Finland's 2017–2018 experiment, 2,000 randomly selected unemployed benefit recipients got €560 per month. During November 2017–October 2018 recipients averaged 78 employment days, six more than the comparison group. Year one showed no group-level employment effect. A 2018 unemployment-benefit reform affected the groups differently, so researchers could not separate that reform's effect from the second-year basic-income effect. Identify the comparison group’s mean employment days, show how the forecast total was derived and explain what would have to be true for it to apply locally.

### Without the skill

> The Finnish results do not support the forecast as a general prediction: recipients averaged 78 employment days from November 2017 to October 2018, six more than the comparison group, whose mean was therefore 72 days. Multiplying that observed difference by 500 gives 3,000 additional employment days, but this is an extrapolation from Finland’s second-year estimate, not evidence that paying 500 local residents would cause the same increase. For the forecast to apply locally, the residents and program would need to be sufficiently comparable to the Finnish participants and experiment, and local conditions would need to produce a similar causal effect. The caveat is substantial: there was no group-level employment effect in year one, and because a 2018 benefit reform affected the groups differently, researchers could not separate its effects from those of basic income in year two.

### With the skill at standard

> The brief predicts 3,000 additional employment days by multiplying 500 residents by six days each. In Finland, unemployed benefit recipients selected for the experiment averaged 78 employment days from November 2017 through October 2018—six more than the comparison group’s 72—but there was no group-level employment effect in year one. The comparison group’s mean was 78 − 6 = 72 days. Because the 2018 benefit reform affected the groups differently, researchers could not isolate its effect from the second-year basic-income effect. The Finnish result therefore does not establish that paying local residents would add six days per person; the forecast applies only if the local recipients and comparison group are comparable and the payment produces the same six-day difference under local conditions.

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Recovers a comparison mean of 72 days and identifies 3,000 as 500 times the six-day observed difference, not an observed local gain. | Met | Met |
| Addresses both the lack of a first-year group-level effect and the asymmetric 2018 reform as a reason the second-year difference does not isolate basic income's effect. | Met | Met |
| Limits the evidence to unemployed benefit recipients and identifies a transfer assumption for 500 local residents, without claiming the experiment proves no effect in any year. | Missed | Met |

**Review.** The comparison mean is 72 days. The 3,000 days are an extrapolation from six days per person. The answer identifies the studied population, the uneven reform exposure and the assumption needed for a local forecast.

Masked reviewer assignment: Y was the revised answer. The table retains the original control grades. [Previous pair and scores](https://github.com/hobin01/writing-styles-from-giants/blob/20f24c66c7e89e6ce1007249c83c33932998bf01/skills/socratic-self-questioning/examples/standard.md) · [All attempts and adjudications](https://github.com/hobin01/writing-styles-from-giants/blob/main/evals/runs/2026-11-09-standard/records/socratic-self-questioning.json).

<details>
<summary>Run record</summary>

Baseline generated 2026-11-08. Revised treatment generated independently on 2026-11-09 with Codex CLI 0.167.0, low reasoning, in a fresh read-only session. SHA-256 prefixes (entrypoint / original baseline / revised answer): `6c4c77094da2` / `b7784aaaace2` / `1af4e026b8f6`.

</details>
