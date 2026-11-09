# Which improvement would reduce the uncertainty of NIST-F2 more?

[한국어](standard.ko.md)

2026-11-09 · `nist-technical-publication` 0.1.4 · English · `gpt-6-luna`

### Case and sources

- [Heavner et al., First Accuracy Evaluation of NIST-F2, Metrologia (2014)](https://www.nist.gov/publications/first-accuracy-evaluation-nist-f2). Authors' abstract, including the July–August 2013 Type A and Type B fractional uncertainties, the 80 K interrogation environment and the reason for the dominant Type B contribution.

### Prompt

> Prepare a short technical note for a metrology lab deciding which component to improve in NIST-F2. In the July–August 2013 evaluation, Type A statistical fractional frequency uncertainty was 0.44 × 10⁻¹⁵ and Type B systematic uncertainty was 0.11 × 10⁻¹⁵. The 80 K environment reduced the blackbody-radiation uncertainty by more than fiftyfold; microwave-amplitude effects dominated Type B. For this comparison only, assume the two components are independent, combine them by root-sum-square, and compare two equally costly hypothetical upgrades: halve Type A alone or halve Type B alone. Show the present and both projected combined uncertainties, recommend one upgrade on this metric, and state why cooling by itself does not establish a fiftyfold improvement in overall uncertainty. Write the answer in English.

### Without the skill

> ### NIST-F2 upgrade comparison
>
> Assuming independent Type A and Type B components, the combined fractional frequency uncertainty is their root-sum-square:
>
> | Scenario | Type A | Type B | Combined uncertainty |
> |---|---:|---:|---:|
> | Present | 0.44 | 0.11 | **0.454 × 10⁻¹⁵** |
> | Halve Type A | 0.22 | 0.11 | **0.246 × 10⁻¹⁵** |
> | Halve Type B | 0.44 | 0.055 | **0.443 × 10⁻¹⁵** |
>
> On this metric, **halving Type A is the better upgrade**: it lowers the combined uncertainty substantially, while halving Type B produces only a small change because Type A is much larger.
>
> Cooling to 80 K reduced the blackbody-radiation uncertainty by more than fiftyfold, but that is a reduction in one systematic contribution, not in total uncertainty. Microwave-amplitude effects dominated Type B, and the overall uncertainty also includes Type A; therefore, cooling alone does not imply a fiftyfold improvement in the combined uncertainty.

### With the skill at standard

> ## NIST-F2 uncertainty improvement note
>
> The July–August 2013 evaluation reported a Type A statistical fractional frequency uncertainty of **0.44 × 10⁻¹⁵** and a Type B systematic uncertainty of **0.11 × 10⁻¹⁵**. Microwave-amplitude effects dominated Type B; the 80 K environment reduced the blackbody-radiation uncertainty by more than fiftyfold.
>
> For this comparison, assume the Type A and Type B components are independent and combine them by root-sum-square:
>
> $$
> u_{\mathrm{combined}}=\sqrt{u_A^2+u_B^2}.
> $$
>
> | Scenario | Type A uncertainty (× 10⁻¹⁵) | Type B uncertainty (× 10⁻¹⁵) | Combined uncertainty (× 10⁻¹⁵) |
> |---|---:|---:|---:|
> | Present | 0.44 | 0.11 | 0.454 |
> | Halve Type A | 0.22 | 0.11 | 0.246 |
> | Halve Type B | 0.44 | 0.055 | 0.443 |
>
> The table values are coefficients on the stated common scale; for example, the present combined uncertainty is **0.454 × 10⁻¹⁵**. On this metric, choose the Type A upgrade: it lowers the combined uncertainty more than halving Type B.
>
> Cooling alone does not establish a fiftyfold improvement in overall uncertainty. The reported reduction applies to the blackbody-radiation component, while other uncertainty sources remain; microwave-amplitude effects dominated Type B, and Type A was larger than Type B in this evaluation.

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Reports the Type A/B values with labels and fractional units and derives a current combined value near 0.454 × 10⁻¹⁵ under the stated independence assumption. | Missed | Met |
| Correctly calculates both hypothetical totals (about 0.246 × 10⁻¹⁵ if Type A halves and 0.443 × 10⁻¹⁵ if Type B halves) and favors Type A for the larger reduction at equal cost. | Met | Met |
| Keeps the projections separate from the 2013 observations, bounds the fiftyfold reduction to the blackbody contribution, and identifies microwave amplitude as the dominant Type B effect. | Met | Met |

**Review.** With independent components, the current combined fractional uncertainty is about 0.454 × 10⁻¹⁵. Halving Type A gives 0.246 × 10⁻¹⁵ versus 0.443 × 10⁻¹⁵ for Type B. The fiftyfold change belongs to the blackbody contribution.

Masked reviewer assignment: X was the revised answer. The table retains the original control grades. [Previous pair and scores](https://github.com/hobin01/writing-styles-from-giants/blob/20f24c66c7e89e6ce1007249c83c33932998bf01/skills/nist-technical-publication/examples/standard.md) · [All attempts and adjudications](https://github.com/hobin01/writing-styles-from-giants/blob/main/evals/runs/2026-11-09-standard/records/nist-technical-publication.json).

<details>
<summary>Run record</summary>

Baseline generated 2026-11-08. Revised treatment generated independently on 2026-11-09 with Codex CLI 0.167.0, low reasoning, in a fresh read-only session. SHA-256 prefixes (entrypoint / original baseline / revised answer): `d936b66143cd` / `25ee98c46dab` / `2e5b1c8bcbd6`.

</details>
