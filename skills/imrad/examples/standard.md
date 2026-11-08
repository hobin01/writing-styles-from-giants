# How LIGO recognized GW150914

2026-11-08 · `imrad` 0.1.2 · English · Codex CLI 0.167.0 / gpt-6.1-sol

### Case and sources

- [LIGO Scientific Collaboration and Virgo Collaboration, Observation of Gravitational Waves from a Binary Black Hole Merger (2016)](https://dcc.ligo.org/public/0122/P150914/014/LIGO-P150914_Detection_of_GW150914.pdf). Abstract and §V.B, binary coalescence search: event date, two detectors, frequency sweep, peak strain, predicted waveform match and upper bound on the false-alarm rate.

### Prompt

> Write a research abstract of at most 110 words for a museum's science page about GW150914, keeping the measurement and its interpretation distinct. On 14 September 2015 both Advanced LIGO detectors, at Livingston and Hanford, recorded a transient signal. Its frequency rose from 35 to 250 Hz and its peak strain was 1.0 × 10⁻²¹. The signal matched the waveform predicted for two black holes spiraling together, merging and settling into one remnant. The paper estimated a false-alarm rate of less than one event per 203,000 years for its search. Explain what that rate measures.

### Without a skill

> On 14 September 2015, Advanced LIGO’s detectors at Livingston and Hanford recorded a transient signal whose frequency rose from 35 to 250 Hz, with a peak strain of 1.0 × 10⁻²¹. These measurements matched the predicted gravitational-wave signature of two black holes spiraling together, merging and settling into one remnant, supporting that interpretation of GW150914. The paper estimated a search false-alarm rate below one event per 203,000 years: how often detector noise would produce a candidate at least as significant under that search procedure. This rate is not the probability that this particular signal was noise.

### With the skill at standard

> **Introduction:** GW150914 tested whether gravitational-wave observations matched predictions for merging black holes.
>
> **Methods:** On 14 September 2015, the Advanced LIGO detectors at Livingston and Hanford recorded a transient signal.
>
> **Results:** Its frequency rose from 35 to 250 Hz, with a peak strain of 1.0 × 10⁻²¹. The paper estimated a false-alarm rate below one event per 203,000 years: how often noise would produce a candidate at least as significant in that search, not the probability this event was noise.
>
> **Discussion:** The waveform matched predictions for two black holes spiraling together, merging and settling into one remnant, supporting that interpretation.

### What changed

**Checks set before the run.** Keep the event date, both instruments, 35–250 Hz and the dimensionless peak strain. Distinguish the observed waveform from the black-hole-merger interpretation and the search's noise false-alarm rate from the rate of mergers.

Both final answers give the date, sites, frequency sweep, peak strain and the search-specific false-alarm rate. Both distinguish a noise-candidate rate from the probability that GW150914 was noise. The revised skill answer puts the detector reading in Methods and the merger interpretation in Discussion; the baseline makes the same distinction in one paragraph. The first skill answer assigned the waveform comparison to the detectors. After the instruction was clarified, the new answer no longer does so.

**차이.** 두 최종 답 모두 오경보율을 ‘이 신호가 잡음일 확률’과 구분합니다. 첫 적용 답은 검출기가 파형까지 비교한 것처럼 썼습니다. 재실행한 답은 검출기가 기록한 신호와 그 신호를 블랙홀 병합으로 해석한 근거를 따로 보여 줍니다.

<details>
<summary>Earlier attempts on this case</summary>

The first treatment assigned waveform comparison to the detectors. The revised method distinguishes the recording instrument from the analysis. We reran the same request with that change.

**Attempt 1 — request**

> Write a research abstract of at most 110 words for a museum's science page about GW150914, keeping the measurement and its interpretation distinct. On 14 September 2015 both Advanced LIGO detectors, at Livingston and Hanford, recorded a transient signal. Its frequency rose from 35 to 250 Hz and its peak strain was 1.0 × 10⁻²¹. The signal matched the waveform predicted for two black holes spiraling together, merging and settling into one remnant. The paper estimated a false-alarm rate of less than one event per 203,000 years for its search. Explain what that rate measures.

**With the skill at standard**

> **Introduction:** GW150914 tested predictions of gravitational waves from merging black holes.
>
> **Methods:** On 14 September 2015, both Advanced LIGO detectors, at Livingston and Hanford, recorded a transient signal and compared it with predicted waveforms.
>
> **Results:** Its frequency rose from 35 to 250 Hz, with peak strain 1.0 × 10⁻²¹. It matched the predicted waveform of two black holes spiraling together, merging and settling into one remnant. The search’s estimated false-alarm rate was less than one event per 203,000 years: how often noise would produce a candidate at least as significant.
>
> **Discussion:** This agreement supports interpreting GW150914 as gravitational waves from a black-hole merger.

</details>
