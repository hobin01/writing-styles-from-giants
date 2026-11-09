# Which crossings should receive the pilot first?

[한국어](standard.ko.md)

2026-11-09 · `minto-pyramid` 0.2.6 · English · `gpt-6-luna`

### Case and sources

- [FHWA, Leading Pedestrian Interval](https://highways.dot.gov/safety/proven-safety-countermeasures/leading-pedestrian-interval). Definition, timing, turning conflicts, visibility, accessibility and applicability at high-turning-volume crossings.
- [FHWA, Safety Evaluation of Protected Left-Turn Phasing and Leading Pedestrian Intervals on Pedestrian Safety (2018), FHWA-HRT-18-044](https://www.fhwa.dot.gov/publications/research/safety/18044/18044.pdf). Executive summary and combined leading-interval evaluation, including the Chicago, New York and Charlotte sites and pedestrian crash modification factor 0.87. The committee decision in the request is hypothetical.

### Prompt

> Write one concise decision-opening paragraph in English for a city committee. It can fund one pilot at a group of signalized crossings with heavy turning traffic; either group costs the same and the goal is to avert the larger expected number of vehicle–pedestrian crashes. WALK would begin 3–7 seconds before drivers get green. In FHWA's three-city study the estimated crash modification factor was 0.87. In this hypothetical comparison, without treatment North's crossings are expected to have 20 such crashes and South's 5 over the same period. Estimate what difference applying the study factor would make at each group. Recommend a site, explain why the head start might matter at turns, and specify a local comparison that could measure the effect of the pilot against what would have happened without it.

### Without the skill

> Fund one pilot at **North’s signalized crossings**, where heavy turning traffic and an expected 20 vehicle–pedestrian crashes make the potential benefit larger: applying FHWA’s estimated crash modification factor of 0.87 implies about 2.6 fewer crashes over the comparison period, versus about 0.65 fewer at South’s crossings, which are expected to have 5. The 3–7 second WALK head start may give pedestrians time to enter the crosswalk and become more visible to turning drivers before those drivers receive green. To measure the pilot’s effect, compare North’s before-and-after crash rate with the change over the same period at similar untreated crossings, accounting for pedestrian and vehicle volumes and other relevant changes.

### With the skill at standard

> Cities face vehicle–pedestrian crash risks at both groups of signalized crossings, and the committee can fund one pilot at either site. Which should it choose to avert more crashes, and how can it assess the pilot’s effect? Apply FHWA’s three-city study factor of 0.87 as an estimate: North’s expected 20 crashes would fall to 17.4, or about 2.6 fewer; South’s 5 would fall to 4.35, or about 0.65 fewer. I recommend North because the same estimated proportional reduction yields a larger absolute decrease there. The 3–7 second WALK head start could give pedestrians time to enter the crossing before turning drivers get green, making them more visible to drivers turning through the intersection. To measure the local effect, compare the change in vehicle–pedestrian crashes at North before and after the pilot with the change over the same periods at comparable untreated signalized crossings; matching traffic, turning patterns, and crash trends would make that comparison more credible. The estimates transfer the study factor to North and South, so they are not guaranteed local results.

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Correctly derives expected reductions of 2.6 at North and 0.65 at South (or gives both treated counts and these reductions). | Met | Met |
| Recommends North under the stated equal-cost objective and explains how the early WALK relates to turning vehicles or pedestrian visibility. | Met | Met |
| Labels the estimates conditional on transfer from the study and proposes a local treated-versus-credible-without-treatment comparison to test the effect. | Met | Met |

**Review.** The recommendation rests on 2.6 versus 0.65 expected crashes prevented at equal cost, conditional on local transfer. Comparable untreated intersections give the city a way to test that forecast.

Masked reviewer assignment: Y was the revised answer. The table retains the original control grades. [Previous pair and scores](https://github.com/hobin01/writing-styles-from-giants/blob/20f24c66c7e89e6ce1007249c83c33932998bf01/skills/minto-pyramid/examples/standard.md) · [All attempts and adjudications](https://github.com/hobin01/writing-styles-from-giants/blob/main/evals/runs/2026-11-09-standard/records/minto-pyramid.json).

<details>
<summary>Run record</summary>

Baseline generated 2026-11-08. Revised treatment generated independently on 2026-11-09 with Codex CLI 0.167.0, low reasoning, in a fresh read-only session. SHA-256 prefixes (entrypoint / original baseline / revised answer): `8063d7e2ee16` / `447627226ac3` / `e506e806dc95`.

</details>
