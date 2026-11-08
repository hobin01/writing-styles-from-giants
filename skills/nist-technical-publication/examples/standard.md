# Which improvement would reduce the uncertainty of NIST-F2 more?

2026-11-08 · `nist-technical-publication` 0.1.2 at first pass · `gpt-6-luna` · Codex CLI 0.167.0

### Case and sources

- [Heavner et al., First Accuracy Evaluation of NIST-F2, Metrologia (2014)](https://www.nist.gov/publications/first-accuracy-evaluation-nist-f2). Authors' abstract, including the July–August 2013 Type A and Type B fractional uncertainties, the 80 K interrogation environment and the reason for the dominant Type B contribution.

**Reasoning task.** Propagate independent uncertainties, compare two counterfactual interventions, and distinguish a reduction in a single physical contribution from a change in the total.

### Prompt

> Prepare a short technical note for a metrology lab deciding which component to improve in NIST-F2. In the July–August 2013 evaluation, Type A statistical fractional frequency uncertainty was 0.44 × 10⁻¹⁵ and Type B systematic uncertainty was 0.11 × 10⁻¹⁵. The 80 K environment reduced the blackbody-radiation uncertainty by more than fiftyfold; microwave-amplitude effects dominated Type B. For this comparison only, assume the two components are independent, combine them by root-sum-square, and compare two equally costly hypothetical upgrades: halve Type A alone or halve Type B alone. Show the present and both projected combined uncertainties, recommend one upgrade on this metric, and state why cooling by itself does not establish a fiftyfold improvement in overall uncertainty.

### Without a skill

> ### NIST-F2 uncertainty improvement
>
> Using the stated independence assumption, combine Type A and Type B uncertainties by root-sum-square:
>
>
> $$
> u_{\text{combined}}=\sqrt{u_A^2+u_B^2}.
> $$
>
>
> | Scenario | Type A | Type B | Combined uncertainty |
> |---|---:|---:|---:|
> | Present | 0.44 | 0.11 | **0.454** |
> | Halve Type A | 0.22 | 0.11 | **0.246** |
> | Halve Type B | 0.44 | 0.055 | **0.443** |
>
> All values are in $10^{-15}$ fractional frequency uncertainty.
>
> For an equally costly upgrade, **halve Type A**: it lowers the combined uncertainty substantially more (to about $0.246\times10^{-15}$, versus $0.443\times10^{-15}$ for halving Type B).
>
> The more-than-fiftyfold reduction from the 80 K environment applies to the blackbody-radiation uncertainty contribution. It does not imply the same reduction in overall uncertainty: other contributions remain, and microwave-amplitude effects dominate Type B.

<details>
<summary>Original model text</summary>

````text
### NIST-F2 uncertainty improvement

Using the stated independence assumption, combine Type A and Type B uncertainties by root-sum-square:

\[
u_{\text{combined}}=\sqrt{u_A^2+u_B^2}.
\]

| Scenario | Type A | Type B | Combined uncertainty |
|---|---:|---:|---:|
| Present | 0.44 | 0.11 | **0.454** |
| Halve Type A | 0.22 | 0.11 | **0.246** |
| Halve Type B | 0.44 | 0.055 | **0.443** |

All values are in \(10^{-15}\) fractional frequency uncertainty.

For an equally costly upgrade, **halve Type A**: it lowers the combined uncertainty substantially more (to about \(0.246\times10^{-15}\), versus \(0.443\times10^{-15}\) for halving Type B).

The more-than-fiftyfold reduction from the 80 K environment applies to the blackbody-radiation uncertainty contribution. It does not imply the same reduction in overall uncertainty: other contributions remain, and microwave-amplitude effects dominate Type B.
````

</details>

### With the skill at standard

> ## Technical note: Upgrade priority for NIST-F2
>
> **Purpose.** Compare two equally costly hypothetical upgrades using combined fractional frequency uncertainty as the decision metric.
>
> **Basis.** In the July–August 2013 evaluation, Type A statistical uncertainty was $0.44 \times 10^{-15}$, and Type B systematic uncertainty was $0.11 \times 10^{-15}$. For this comparison, the components are assumed independent and combined by root-sum-square (RSS):
>
>
> $$
> u_{\mathrm{combined}}=\sqrt{u_A^2+u_B^2}.
> $$
>
>
> **Results.** The present combined uncertainty is $0.454 \times 10^{-15}$. Halving Type A alone gives $0.232 \times 10^{-15}$; halving Type B alone gives $0.427 \times 10^{-15}$. Values are rounded to three significant figures.
>
> | Case | Type A ($\times 10^{-15}$) | Type B ($\times 10^{-15}$) | Combined RSS uncertainty ($\times 10^{-15}$) |
> |---|---:|---:|---:|
> | Present | 0.44 | 0.11 | 0.454 |
> | Halve Type A | 0.22 | 0.11 | 0.232 |
> | Halve Type B | 0.44 | 0.055 | 0.427 |
>
> **Recommendation.** On the combined-uncertainty metric, prioritize halving Type A: it lowers the projected combined uncertainty more than halving Type B.
>
> The 80 K environment reduced the blackbody-radiation uncertainty by more than fiftyfold, while microwave-amplitude effects dominated Type B. That reduction applies to the blackbody-radiation contribution; it does not establish a fiftyfold reduction in overall uncertainty, which also includes Type A and other Type B contributions.
>
> **Method record.** Applied the NIST-inspired technical-publication method, version 0.1.2, at standard level. Assumed the stated independence and RSS combination for this comparison only. No figures or tables were supplied for audit.

<details>
<summary>Original model text</summary>

````text
## Technical note: Upgrade priority for NIST-F2

**Purpose.** Compare two equally costly hypothetical upgrades using combined fractional frequency uncertainty as the decision metric.

**Basis.** In the July–August 2013 evaluation, Type A statistical uncertainty was \(0.44 \times 10^{-15}\), and Type B systematic uncertainty was \(0.11 \times 10^{-15}\). For this comparison, the components are assumed independent and combined by root-sum-square (RSS):

\[
u_{\mathrm{combined}}=\sqrt{u_A^2+u_B^2}.
\]

**Results.** The present combined uncertainty is \(0.454 \times 10^{-15}\). Halving Type A alone gives \(0.232 \times 10^{-15}\); halving Type B alone gives \(0.427 \times 10^{-15}\). Values are rounded to three significant figures.

| Case | Type A (\(\times 10^{-15}\)) | Type B (\(\times 10^{-15}\)) | Combined RSS uncertainty (\(\times 10^{-15}\)) |
|---|---:|---:|---:|
| Present | 0.44 | 0.11 | 0.454 |
| Halve Type A | 0.22 | 0.11 | 0.232 |
| Halve Type B | 0.44 | 0.055 | 0.427 |

**Recommendation.** On the combined-uncertainty metric, prioritize halving Type A: it lowers the projected combined uncertainty more than halving Type B.

The 80 K environment reduced the blackbody-radiation uncertainty by more than fiftyfold, while microwave-amplitude effects dominated Type B. That reduction applies to the blackbody-radiation contribution; it does not establish a fiftyfold reduction in overall uncertainty, which also includes Type A and other Type B contributions.

**Method record.** Applied the NIST-inspired technical-publication method, version 0.1.2, at standard level. Assumed the stated independence and RSS combination for this comparison only. No figures or tables were supplied for audit.
````

</details>

### First-pass assessment

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Reports the Type A/B values with labels and fractional units and derives a current combined value near 0.454 × 10⁻¹⁵ under the stated independence assumption. | Met | Met |
| Correctly calculates both hypothetical totals (about 0.246 × 10⁻¹⁵ if Type A halves and 0.443 × 10⁻¹⁵ if Type B halves) and favors Type A for the larger reduction at equal cost. | Met | Missed |
| Keeps the projections separate from the 2013 observations, bounds the fiftyfold reduction to the blackbody contribution, and identifies microwave amplitude as the dominant Type B effect. | Met | Met |

Both compute the current combined uncertainty and recommend reducing Type A. The baseline’s two projected values are 0.246 and 0.443 (in units of 10⁻¹⁵); the skill answer’s 0.232 and 0.427 do not follow from the RSS formula or from its own table inputs. The skill answer also appends an unrequested method/version record, which makes the condition potentially identifiable. Both correctly limit the fiftyfold improvement to the blackbody contribution.

**차이.** 두 답 모두 현재 합성 불확도와 개선 순위는 맞았습니다. 그러나 스킬 답은 올바른 식과 입력을 적고도 가상 개선 후 두 값을 잘못 계산했습니다. 미적용 답의 0.246과 0.443(각각 × 10⁻¹⁵)이 맞습니다. 스킬 답에는 요청하지 않은 방법명·버전도 드러났습니다.

<details>
<summary>Developmental retest · version 0.1.3</summary>

Recalculate derived values under each counterfactual, verify them against the defining relation and keep audit details out of the report. This retest is excluded from the first-pass counts.

The request and original baseline are unchanged.

**New standard answer**

> ## NIST-F2: uncertainty reduction options
>
> **Basis.** In the July–August 2013 evaluation, Type A statistical fractional frequency uncertainty was $0.44 \times 10^{-15}$, and Type B systematic uncertainty was $0.11 \times 10^{-15}$. The 80 K environment reduced the blackbody-radiation uncertainty by more than fiftyfold; microwave-amplitude effects dominated Type B.
>
> **Comparison.** Assuming the two components are independent, the combined uncertainty is their root-sum-square (RSS):
>
>
> $$
> u_{\mathrm{combined}}=\sqrt{u_A^2+u_B^2}.
> $$
>
>
> | Case | Type A ($\times 10^{-15}$) | Type B ($\times 10^{-15}$) | Combined RSS ($\times 10^{-15}$) |
> |---|---:|---:|---:|
> | Present | 0.44 | 0.11 | 0.454 |
> | Halve Type A | 0.22 | 0.11 | 0.246 |
> | Halve Type B | 0.44 | 0.055 | 0.443 |
>
> Values are rounded to three significant figures after calculation. For example, the present value is $\sqrt{0.44^2+0.11^2}=0.4535\ldots$; squaring the rounded result gives approximately $0.206$, consistent with $0.44^2+0.11^2=0.206$.
>
> **Recommendation.** On combined uncertainty alone, choose the upgrade that halves Type A: it reduces the projected combined uncertainty to $0.246 \times 10^{-15}$, compared with $0.443 \times 10^{-15}$ for halving Type B. This comparison assumes the stated independence and equal upgrade cost.
>
> Cooling alone does not establish a fiftyfold improvement in overall uncertainty. The more-than-fiftyfold reduction applies to the blackbody-radiation uncertainty component; microwave-amplitude effects dominate Type B, and Type A also contributes. The overall result depends on the combined components, not on the blackbody component alone.

<details>
<summary>Original model text</summary>

````text
## NIST-F2: uncertainty reduction options

**Basis.** In the July–August 2013 evaluation, Type A statistical fractional frequency uncertainty was \(0.44 \times 10^{-15}\), and Type B systematic uncertainty was \(0.11 \times 10^{-15}\). The 80 K environment reduced the blackbody-radiation uncertainty by more than fiftyfold; microwave-amplitude effects dominated Type B.

**Comparison.** Assuming the two components are independent, the combined uncertainty is their root-sum-square (RSS):

\[
u_{\mathrm{combined}}=\sqrt{u_A^2+u_B^2}.
\]

| Case | Type A (\(\times 10^{-15}\)) | Type B (\(\times 10^{-15}\)) | Combined RSS (\(\times 10^{-15}\)) |
|---|---:|---:|---:|
| Present | 0.44 | 0.11 | 0.454 |
| Halve Type A | 0.22 | 0.11 | 0.246 |
| Halve Type B | 0.44 | 0.055 | 0.443 |

Values are rounded to three significant figures after calculation. For example, the present value is \(\sqrt{0.44^2+0.11^2}=0.4535\ldots\); squaring the rounded result gives approximately \(0.206\), consistent with \(0.44^2+0.11^2=0.206\).

**Recommendation.** On combined uncertainty alone, choose the upgrade that halves Type A: it reduces the projected combined uncertainty to \(0.246 \times 10^{-15}\), compared with \(0.443 \times 10^{-15}\) for halving Type B. This comparison assumes the stated independence and equal upgrade cost.

Cooling alone does not establish a fiftyfold improvement in overall uncertainty. The more-than-fiftyfold reduction applies to the blackbody-radiation uncertainty component; microwave-amplitude effects dominate Type B, and Type A also contributes. The overall result depends on the combined components, not on the blackbody component alone.
````

</details>

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Reports the Type A/B values with labels and fractional units and derives a current combined value near 0.454 × 10⁻¹⁵ under the stated independence assumption. | Met | Met |
| Correctly calculates both hypothetical totals (about 0.246 × 10⁻¹⁵ if Type A halves and 0.443 × 10⁻¹⁵ if Type B halves) and favors Type A for the larger reduction at equal cost. | Met | Met |
| Keeps the projections separate from the 2013 observations, bounds the fiftyfold reduction to the blackbody contribution, and identifies microwave amplitude as the dominant Type B effect. | Met | Met |

The baseline and the skill answer both apply root-sum-square under independence, give present, A-halved and B-halved fractional uncertainties of 0.454, 0.246 and 0.443 × 10⁻¹⁵, and choose A at equal cost. Both limit the more-than-fiftyfold improvement to blackbody-radiation uncertainty and identify microwave amplitude as the dominant Type B effect. The skill answer identifies the 2013 evaluation explicitly; the baseline distinguishes the scenarios with table labels.

**차이.** 미적용 답과 스킬 답 모두 독립성을 가정해 제곱합의 제곱근을 구한다. 현재와 A 또는 B를 절반으로 줄인 경우의 상대 불확도는 각각 0.454, 0.246, 0.443 × 10⁻¹⁵이며 비용이 같으면 A를 선택한다. 둘 다 50배가 넘는 감소를 흑체복사 불확도에 한정하고, B형의 지배적 요인으로 마이크로파 진폭을 든다. 스킬 답은 2013년 평가임을 명시하고 미적용 답은 표의 행으로 현재와 가상 조건을 구분한다.

</details>
