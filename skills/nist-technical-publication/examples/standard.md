# Which improvement would reduce the uncertainty of NIST-F2 more?

[한국어](standard.ko.md)

2026-11-08 · `nist-technical-publication` 0.1.3 · English · `gpt-6-luna`

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

> ## NIST-F2: upgrade comparison
>
> ### Basis
>
> During the July–August 2013 evaluation, Type A statistical fractional frequency uncertainty was $0.44 \times 10^{-15}$, and Type B systematic uncertainty was $0.11 \times 10^{-15}$. The 80 K environment reduced the blackbody-radiation uncertainty by more than fiftyfold, while microwave-amplitude effects dominated Type B.
>
> For this comparison, the two uncertainty components are assumed independent and combined by root-sum-square:
>
>
> $$
> u_{\mathrm{combined}}=\sqrt{u_A^2+u_B^2}.
> $$
>
>
> ### Results
>
> | Case | Type A ($\times 10^{-15}$) | Type B ($\times 10^{-15}$) | Combined ($\times 10^{-15}$) |
> |---|---:|---:|---:|
> | Present | 0.44 | 0.11 | 0.454 |
> | Halve Type A | 0.22 | 0.11 | 0.246 |
> | Halve Type B | 0.44 | 0.055 | 0.443 |
>
> Values are rounded to three significant figures. For example, the present result is $\sqrt{0.44^2+0.11^2}=0.4536$, in units of $10^{-15}$.
>
> ### Recommendation
>
> On combined uncertainty alone, choose the hypothetical Type A upgrade: it lowers the result to $0.246 \times 10^{-15}$, compared with $0.443 \times 10^{-15}$ for halving Type B. This comparison assumes the upgrades cost the same and affect only the stated component.
>
> Cooling reduced the blackbody-radiation contribution, but that contribution is only one part of Type B, which is dominated by microwave-amplitude effects; Type A also contributes to the combined uncertainty. Therefore, the more-than-fiftyfold reduction in blackbody-radiation uncertainty does not establish a fiftyfold reduction in overall uncertainty.

<details>
<summary>Original math delimiters</summary>

````text
## NIST-F2: upgrade comparison

### Basis

During the July–August 2013 evaluation, Type A statistical fractional frequency uncertainty was \(0.44 \times 10^{-15}\), and Type B systematic uncertainty was \(0.11 \times 10^{-15}\). The 80 K environment reduced the blackbody-radiation uncertainty by more than fiftyfold, while microwave-amplitude effects dominated Type B.

For this comparison, the two uncertainty components are assumed independent and combined by root-sum-square:

\[
u_{\mathrm{combined}}=\sqrt{u_A^2+u_B^2}.
\]

### Results

| Case | Type A (\(\times 10^{-15}\)) | Type B (\(\times 10^{-15}\)) | Combined (\(\times 10^{-15}\)) |
|---|---:|---:|---:|
| Present | 0.44 | 0.11 | 0.454 |
| Halve Type A | 0.22 | 0.11 | 0.246 |
| Halve Type B | 0.44 | 0.055 | 0.443 |

Values are rounded to three significant figures. For example, the present result is \(\sqrt{0.44^2+0.11^2}=0.4536\), in units of \(10^{-15}\).

### Recommendation

On combined uncertainty alone, choose the hypothetical Type A upgrade: it lowers the result to \(0.246 \times 10^{-15}\), compared with \(0.443 \times 10^{-15}\) for halving Type B. This comparison assumes the upgrades cost the same and affect only the stated component.

Cooling reduced the blackbody-radiation contribution, but that contribution is only one part of Type B, which is dominated by microwave-amplitude effects; Type A also contributes to the combined uncertainty. Therefore, the more-than-fiftyfold reduction in blackbody-radiation uncertainty does not establish a fiftyfold reduction in overall uncertainty.
````

</details>

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Reports the Type A/B values with labels and fractional units and derives a current combined value near 0.454 × 10⁻¹⁵ under the stated independence assumption. | Missed | Met |
| Correctly calculates both hypothetical totals (about 0.246 × 10⁻¹⁵ if Type A halves and 0.443 × 10⁻¹⁵ if Type B halves) and favors Type A for the larger reduction at equal cost. | Met | Met |
| Keeps the projections separate from the 2013 observations, bounds the fiftyfold reduction to the blackbody contribution, and identifies microwave amplitude as the dominant Type B effect. | Met | Met |

**Masked review** (X = baseline; Y = standard). Both give the three combined values as 0.454, 0.246 and 0.443 × 10⁻¹⁵, choose Type A, and keep the fiftyfold reduction specific to blackbody radiation. X gives the component values as bare decimals in its table without stating their scale; Y labels all columns and identifies the 2013 measurements. Y's intermediate 0.4536 should be about 0.45354, which still rounds to the stated 0.454.

<details>
<summary>Run record</summary>

Each arm was a separate ephemeral read-only Codex CLI 0.167.0 session with low reasoning effort. Neither session was given the other answer or an answer in the other language.

SHA-256 prefixes (entrypoint / baseline answer / standard answer): `33e35b943513` / `25ee98c46dab` / `97c03562d708`.

</details>
