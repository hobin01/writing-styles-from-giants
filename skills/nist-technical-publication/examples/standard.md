# Which improvement would reduce the uncertainty of NIST-F2 more?

[한국어](standard.ko.md) · [light](light.md) · **standard** · [strict](strict.md)

### Question

> The July–August 2013 NIST-F2 evaluation reported fractional frequency uncertainty components of 0.44 × 10⁻¹⁵ (Type A, statistical) and 0.11 × 10⁻¹⁵ (Type B, systematic). Its 80 K environment reduced blackbody-radiation uncertainty by more than a factor of 50. Microwave-amplitude effects dominated Type B. Suppose we can halve either component for the same cost, leaving the other unchanged. Assume the two components are independent and combine in quadrature. Which upgrade would reduce combined uncertainty more? Does the fiftyfold figure tell us how much the clock’s overall uncertainty improved?

**Sources** · [Heavner et al., First Accuracy Evaluation of NIST-F2, Metrologia (2014)](https://www.nist.gov/publications/first-accuracy-evaluation-nist-f2)

### With the skill

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

### Without the skill

> Halving the Type A component reduces combined uncertainty from $\sqrt{0.44^2+0.11^2}\approx0.454$ to $\sqrt{0.22^2+0.11^2}\approx0.246$, in units of $10^{-15}$.
>
> Halving Type B gives $\sqrt{0.44^2+0.055^2}\approx0.443$. So halving Type A reduces the combined uncertainty more.
>
> The factor of more than 50 applies to the blackbody-radiation uncertainty, not to the clock’s overall uncertainty. Without the other uncertainty contributions and the blackbody term’s size before the reduction, it does not tell us how much overall uncertainty improved.
