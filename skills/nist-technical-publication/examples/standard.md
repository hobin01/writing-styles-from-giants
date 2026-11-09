# Which improvement would reduce the uncertainty of NIST-F2 more?

[한국어](standard.ko.md) · [light](light.md) · [strict](strict.md)

### Question

> The July–August 2013 NIST-F2 evaluation reported fractional frequency uncertainty components of 0.44 × 10⁻¹⁵ (Type A, statistical) and 0.11 × 10⁻¹⁵ (Type B, systematic). Its 80 K environment reduced blackbody-radiation uncertainty by more than a factor of 50. Microwave-amplitude effects dominated Type B. Suppose we can halve either component for the same cost, leaving the other unchanged. Assume the two components are independent and combine in quadrature. Which upgrade would reduce combined uncertainty more? Does the fiftyfold figure tell us how much the clock’s overall uncertainty improved?

**Sources** · [Heavner et al., First Accuracy Evaluation of NIST-F2, Metrologia (2014)](https://www.nist.gov/publications/first-accuracy-evaluation-nist-f2)

### Standard

> ## Comparison of the two upgrades
>
> Assuming the Type A and Type B components are independent, the combined fractional frequency uncertainty is their root-sum-square:
>
> $$
> u=\sqrt{u_A^2+u_B^2}.
> $$
>
> If the Type A component is halved:
>
> $$
> u_A'=\sqrt{(0.22\times10^{-15})^2+(0.11\times10^{-15})^2}
> =\sqrt{0.0605}\times10^{-15}.
> $$
>
> If the Type B component is halved:
>
> $$
> u_B'=\sqrt{(0.44\times10^{-15})^2+(0.055\times10^{-15})^2}
> =\sqrt{0.196625}\times10^{-15}.
> $$
>
> The Type A upgrade yields the lower combined uncertainty, so halving Type A would reduce the combined uncertainty more.
>
> ## What the fiftyfold figure means
>
> No. The statement that the 80 K environment reduced blackbody-radiation uncertainty by more than a factor of 50 applies to that uncertainty contribution. It does not give the clock’s overall uncertainty improvement. That would require the blackbody contribution before and after cooling, along with the other uncertainty components and how they combine.
