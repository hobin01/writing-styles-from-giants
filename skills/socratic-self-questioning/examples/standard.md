# Can Finland’s basic-income result justify a forecast for 500 workers?

[한국어](standard.ko.md)

2026-11-08 · `socratic-self-questioning` 0.1.2 · English · `gpt-6-luna`

### Case and sources

- [Finnish Ministry of Social Affairs and Health and Kela, Results of the basic income experiment (6 May 2020)](https://valtioneuvosto.fi/en/-/1271139/perustulokokeilun-tulokset-tyollisyysvaikutukset-vahaisia-toimeentulo-ja-psyykkinen-terveys-koettiin-paremmaksi?languageId=en_US). Employment results and experiment design: participating population, €560 payment, November 2017–October 2018 comparison, first-year finding, and asymmetric 2018 activation-policy change.

### Prompt

> A policy brief predicts ‘If we pay 500 local residents, their employment will rise by 3,000 days.’ Evaluate this inference in one concise English paragraph for publication. In Finland's 2017–2018 experiment, 2,000 randomly selected unemployed benefit recipients got €560 per month. During November 2017–October 2018 recipients averaged 78 employment days, six more than the comparison group. Year one showed no group-level employment effect. A 2018 unemployment-benefit reform affected the groups differently, so researchers could not separate that reform's effect from the second-year basic-income effect. Identify the comparison group’s mean employment days, show how the forecast total was derived and explain what would have to be true for it to apply locally.

### Without the skill

> The Finnish results do not support the forecast as a general prediction: recipients averaged 78 employment days from November 2017 to October 2018, six more than the comparison group, whose mean was therefore 72 days. Multiplying that observed difference by 500 gives 3,000 additional employment days, but this is an extrapolation from Finland’s second-year estimate, not evidence that paying 500 local residents would cause the same increase. For the forecast to apply locally, the residents and program would need to be sufficiently comparable to the Finnish participants and experiment, and local conditions would need to produce a similar causal effect. The caveat is substantial: there was no group-level employment effect in year one, and because a 2018 benefit reform affected the groups differently, researchers could not separate its effects from those of basic income in year two.

### With the skill at standard

> The forecast implies six additional employment days for each of 500 residents, since 3,000 ÷ 500 = 6. In Finland’s experiment, recipients averaged 78 employment days—six more than the comparison group, whose mean was therefore 72 days. But that second-year difference cannot be attributed to basic income alone: a 2018 benefit reform affected the groups differently, and researchers could not separate its effect from the basic-income effect; year one showed no group-level employment effect. The local forecast would apply only if paying these residents produced the same six-day difference against a comparable local comparison group, with relevant conditions and policy effects sufficiently similar.

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Recovers a comparison mean of 72 days and identifies 3,000 as 500 times the six-day observed difference, not an observed local gain. | Met | Met |
| Addresses both the lack of a first-year group-level effect and the asymmetric 2018 reform as a reason the second-year difference does not isolate basic income's effect. | Met | Met |
| Limits the evidence to unemployed benefit recipients and identifies a transfer assumption for 500 local residents, without claiming the experiment proves no effect in any year. | Missed | Missed |

**Masked review** (Y = baseline; X = standard). Both recover the 72-day comparison mean and explain the limitations from the first-year result and the 2018 reform. Both recognize that transferring the six-day difference requires comparable local conditions, but omit that the Finnish participants were unemployed benefit recipients. Y explicitly calls the 3,000 days an extrapolation; X reconstructs it by division.

<details>
<summary>Run record</summary>

Each arm was a separate ephemeral read-only Codex CLI 0.167.0 session with low reasoning effort. Neither session was given the other answer or an answer in the other language.

SHA-256 prefixes (entrypoint / baseline answer / standard answer): `73849e50a54b` / `b7784aaaace2` / `15fcfc0f0a6a`.

</details>
