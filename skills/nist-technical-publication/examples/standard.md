# The uncertainty budget of the NIST-F2 cesium fountain

2026-11-08 · `nist-technical-publication` 0.1.2 · English · Codex CLI 0.167.0 / gpt-6.1-sol

### Case and sources

- [Heavner et al., First Accuracy Evaluation of NIST-F2, Metrologia (2014)](https://www.nist.gov/publications/first-accuracy-evaluation-nist-f2). Authors' abstract, including the July–August 2013 Type A and Type B fractional uncertainties, the 80 K interrogation environment and the reason for the dominant Type B contribution.

### Prompt

> For a metrology lab, summarize the July–August 2013 evaluation of NIST-F2 in at most 85 words. This cesium fountain interrogated atoms in an 80 K environment. Cooling cut the uncertainty from the blackbody-radiation shift by more than a factor of 50. The reported statistical (Type A) fractional frequency uncertainty was 0.44 × 10⁻¹⁵; the systematic (Type B) component was 0.11 × 10⁻¹⁵. Microwave-amplitude effects dominated the Type B component. Explain what the smaller number represents without presenting it as the clock's total uncertainty.

### Without a skill

> During its July–August 2013 evaluation, NIST-F2 interrogated cesium atoms in an 80 K environment, reducing uncertainty from the blackbody-radiation shift by more than a factor of 50. Its statistical (Type A) fractional frequency uncertainty was 0.44 × 10⁻¹⁵. The smaller value, 0.11 × 10⁻¹⁵, represents the systematic (Type B) uncertainty component, dominated by microwave-amplitude effects; it is not the clock’s total uncertainty.

### With the skill at standard

> The July–August 2013 evaluation of the NIST-F2 cesium fountain interrogated atoms in an 80 K environment, reducing uncertainty from the blackbody-radiation shift by more than a factor of 50. The reported statistical (Type A) fractional frequency uncertainty was 0.44 × 10⁻¹⁵. The smaller value, 0.11 × 10⁻¹⁵, represents the systematic (Type B) fractional frequency uncertainty component, dominated by microwave-amplitude effects; it is not the clock’s total uncertainty.

### What changed

**Checks set before the run.** Keep July–August 2013, 80 K and the factor greater than 50 attached only to uncertainty from the blackbody-radiation shift. Preserve each numeric fractional uncertainty with its correct component and keep microwave-amplitude effects tied to Type B; neither component alone is the total.

Both keep the 80 K setting, the time interval and the two numerical components. Both attach the factor above 50 to the blackbody-radiation contribution only. The skill spells out that the smaller component is a fractional frequency uncertainty; the baseline is already sufficient to keep it separate from the clock’s total uncertainty.

**차이.** 두 답 모두 50배 넘게 줄어든 것은 흑체복사에 따른 불확도라고 밝힙니다. 둘 다 0.11 × 10⁻¹⁵를 전체 불확도로 바꾸지 않았습니다.
