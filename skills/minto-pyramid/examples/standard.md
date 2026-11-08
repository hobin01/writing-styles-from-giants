# Which crossings should receive the pilot first?

[한국어](standard.ko.md)

2026-11-08 · `minto-pyramid` 0.2.2 · English · `gpt-6-luna`

### Case and sources

- [FHWA, Leading Pedestrian Interval](https://highways.dot.gov/safety/proven-safety-countermeasures/leading-pedestrian-interval). Definition, timing, turning conflicts, visibility, accessibility and applicability at high-turning-volume crossings.
- [FHWA, Safety Evaluation of Protected Left-Turn Phasing and Leading Pedestrian Intervals on Pedestrian Safety (2018), FHWA-HRT-18-044](https://www.fhwa.dot.gov/publications/research/safety/18044/18044.pdf). Executive summary and combined leading-interval evaluation, including the Chicago, New York and Charlotte sites and pedestrian crash modification factor 0.87. The committee decision in the request is hypothetical.

### Prompt

> Write one concise decision-opening paragraph in English for a city committee. It can fund one pilot at a group of signalized crossings with heavy turning traffic; either group costs the same and the goal is to avert the larger expected number of vehicle–pedestrian crashes. WALK would begin 3–7 seconds before drivers get green. In FHWA's three-city study the estimated crash modification factor was 0.87. In this hypothetical comparison, without treatment North's crossings are expected to have 20 such crashes and South's 5 over the same period. Estimate what difference applying the study factor would make at each group. Recommend a site, explain why the head start might matter at turns, and specify a local comparison that could measure the effect of the pilot against what would have happened without it.

### Without the skill

> Fund one pilot at **North’s signalized crossings**, where heavy turning traffic and an expected 20 vehicle–pedestrian crashes make the potential benefit larger: applying FHWA’s estimated crash modification factor of 0.87 implies about 2.6 fewer crashes over the comparison period, versus about 0.65 fewer at South’s crossings, which are expected to have 5. The 3–7 second WALK head start may give pedestrians time to enter the crosswalk and become more visible to turning drivers before those drivers receive green. To measure the pilot’s effect, compare North’s before-and-after crash rate with the change over the same period at similar untreated crossings, accounting for pedestrian and vehicle volumes and other relevant changes.

### With the skill at standard

> North is the stronger pilot choice: applying FHWA’s estimated crash modification factor of 0.87 to the expected counts implies about 2.6 fewer vehicle–pedestrian crashes at North’s crossings (20 × 0.13), compared with 0.65 fewer at South’s (5 × 0.13). The 3–7 second WALK head start may give pedestrians time to enter the crossing before turning drivers receive green, making them more visible and reducing conflicts. To measure the pilot’s local effect, compare crash changes at the treated crossings before and after installation with changes over the same periods at similar untreated crossings, accounting for differences in baseline crash trends and exposure.

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Correctly derives expected reductions of 2.6 at North and 0.65 at South (or gives both treated counts and these reductions). | Met | Met |
| Recommends North under the stated equal-cost objective and explains how the early WALK relates to turning vehicles or pedestrian visibility. | Met | Met |
| Labels the estimates conditional on transfer from the study and proposes a local treated-versus-credible-without-treatment comparison to test the effect. | Met | Met |

**Masked review** (Y = baseline; X = standard). Both recommend North, project reductions of 2.6 versus 0.65, explain the visibility mechanism and propose comparing changes with similar untreated crossings over the same periods. X mentions baseline trends and exposure; Y names pedestrian and vehicle volumes. Neither presents the forecast as a measured local benefit.

<details>
<summary>Run record</summary>

Each arm was a separate ephemeral read-only Codex CLI 0.167.0 session with low reasoning effort. Neither session was given the other answer or an answer in the other language.

SHA-256 prefixes (entrypoint / baseline answer / standard answer): `1c5f170eb9d4` / `447627226ac3` / `60b342fd8bcc`.

</details>
