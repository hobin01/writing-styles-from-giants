# What ten years of LIGO background would imply for GW150914

2026-11-08 · `imrad` 0.1.2 at first pass · `gpt-6-luna` · Codex CLI 0.167.0

### Case and sources

- [LIGO Scientific Collaboration and Virgo Collaboration, Observation of Gravitational Waves from a Binary Black Hole Merger (2016)](https://dcc.ligo.org/public/0122/P150914/014/LIGO-P150914_Detection_of_GW150914.pdf). Abstract and §V.B, binary coalescence search: event date, two detectors, frequency sweep, peak strain, predicted waveform match and upper bound on the false-alarm rate.

**Reasoning task.** Convert a bound on a search rate to a bound on an expected count; distinguish an expectation from a guarantee and from the posterior probability of a specific event.

### Prompt

> Write a museum research abstract of at most 145 words about LIGO’s GW150914. On 14 September 2015 the Livingston and Hanford instruments recorded a signal rising from 35 to 250 Hz with peak dimensionless strain 1.0 × 10⁻²¹. Researchers found that it matched a predicted binary black-hole merger waveform. The search put its rate of noise candidates at least this significant below one per 203,000 years. An editor concludes: “There would be no false alarms in ten years, so the chance this event was noise is zero.” For an illustrative ten years at the same rate, compute an upper bound on the expected number of such noise candidates. Use the result to assess the editor’s reasoning, while keeping instrument readings, analysis, and interpretation distinct.

### Without a skill

> On 14 September 2015, LIGO’s Livingston and Hanford instruments recorded a signal rising from 35 to 250 Hz, with peak dimensionless strain $1.0 \times 10^{-21}$. In the analysis, researchers found that the signal matched a predicted binary black-hole merger waveform. They estimated that noise candidates at least this significant would occur at a rate below one per 203,000 years. At that upper rate, ten years would yield fewer than $10/203{,}000 \approx 4.9 \times 10^{-5}$ expected noise candidates. This is an upper bound on the expected count, not a guarantee of zero candidates: a rare noise event remains possible. Nor does the rate alone give the probability that this particular event was noise. The editor’s conclusion therefore overstates what the rate establishes.

<details>
<summary>Original model text</summary>

````text
On 14 September 2015, LIGO’s Livingston and Hanford instruments recorded a signal rising from 35 to 250 Hz, with peak dimensionless strain \(1.0 \times 10^{-21}\). In the analysis, researchers found that the signal matched a predicted binary black-hole merger waveform. They estimated that noise candidates at least this significant would occur at a rate below one per 203,000 years. At that upper rate, ten years would yield fewer than \(10/203{,}000 \approx 4.9 \times 10^{-5}\) expected noise candidates. This is an upper bound on the expected count, not a guarantee of zero candidates: a rare noise event remains possible. Nor does the rate alone give the probability that this particular event was noise. The editor’s conclusion therefore overstates what the rate establishes.
````

</details>

### With the skill at standard

> **Introduction.** Detecting gravitational waves directly tests predictions of general relativity. We summarize the observation of GW150914 and assess whether a low background rate makes a noise explanation impossible.
>
> **Methods.** On 14 September 2015, the Livingston and Hanford instruments recorded a signal whose frequency rose from 35 to 250 Hz and whose peak dimensionless strain was 1.0 × 10⁻²¹. Researchers compared the signal with a predicted binary black-hole merger waveform and estimated the rate of noise candidates at least this significant.
>
> **Results.** The signal matched the predicted waveform. The estimated noise-candidate rate was below one per 203,000 years. At that upper rate, the expected number in ten years is less than 10/203,000 ≈ 4.9 × 10⁻⁵.
>
> **Discussion.** This bound indicates a very low expected background count, not zero false alarms or zero probability that this event was noise. An expected count is not a guarantee about what occurs in any particular interval.

### First-pass assessment

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Correctly attributes the dated 35–250 Hz, 1.0 × 10⁻²¹ strain signal to both detectors and the waveform comparison to analysis rather than to the detectors. | Met | Met |
| Computes an expected count strictly below 10/203,000 (about 4.93 × 10⁻⁵) over the hypothetical ten years at the stated rate, without labeling it an event probability. | Met | Met |
| Rejects both the guarantee of zero noise candidates and a zero probability for this event; the abstract distinguishes the measured signal from the supported merger interpretation. | Met | Met |

Both distinguish the detectors’ readings from the researchers’ waveform comparison, and give the correct expected-count bound without turning it into a probability for GW150914. The baseline fits the word budget in one paragraph. The skill answer makes the measurement and interpretation easier to find with headings, but exceeds the requested 145 words by whitespace count. The three preregistered checks cover the science rather than the length.

**차이.** 두 답 모두 10년간 기대 오경보 건수가 약 4.93 × 10⁻⁵ 미만임을 구하고, 이를 이 사건이 잡음일 확률과 구분합니다. 미적용 답은 한 문단으로 분량을 지켰고, 스킬 답은 관측과 해석을 제목으로 구분했지만 공백 기준 145단어 제한을 넘겼습니다.

<details>
<summary>Developmental retest · version 0.1.3</summary>

Check the budget for the whole abstract, including section labels. This retest is excluded from the first-pass counts.

The request and original baseline are unchanged.

**New standard answer**

> **Method: IMRaD, standard level**
>
> **Introduction:** Detecting a gravitational-wave signal requires distinguishing a real astrophysical event from noise. This abstract describes the recorded signal and the search’s estimate of noise-candidate frequency.
>
> **Methods:** On 14 September 2015, the Livingston and Hanford instruments recorded the signal. Researchers compared it with a predicted binary black-hole merger waveform and estimated the rate of noise candidates at least this significant.
>
> **Results:** The signal rose from 35 to 250 Hz and had peak dimensionless strain of 1.0 × 10⁻²¹. It matched the predicted waveform. The estimated noise-candidate rate was below one per 203,000 years. At that upper rate, ten years would yield fewer than 10/203,000 ≈ 4.9 × 10⁻⁵ expected candidates.
>
> **Discussion:** This small expected count supports a low noise-candidate rate, not the editor’s claim of zero false alarms or zero probability that the event was noise. An expected count is not a guarantee that none will occur.

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Correctly attributes the dated 35–250 Hz, 1.0 × 10⁻²¹ strain signal to both detectors and the waveform comparison to analysis rather than to the detectors. | Met | Met |
| Computes an expected count strictly below 10/203,000 (about 4.93 × 10⁻⁵) over the hypothetical ten years at the stated rate, without labeling it an event probability. | Met | Met |
| Rejects both the guarantee of zero noise candidates and a zero probability for this event; the abstract distinguishes the measured signal from the supported merger interpretation. | Met | Met |

Both the baseline and the skill answer attribute the dated strain and frequency readings to the two detectors and the merger-waveform match to the analysis. Both bound the expected noise count below 10/203,000 over ten years and reject the editor’s two inferences. The baseline states explicitly that the rate alone cannot determine the probability for this event. The skill answer displays “Method: IMRaD, standard level” before the abstract; including its headings and label puts the delivered text over 145 words.

**차이.** 미적용 답과 스킬 답 모두 두 검출기의 관측 날짜·변형률·주파수를 연구진의 병합 파형 분석과 구분한다. 둘 다 10년간 기대하는 잡음 후보 수가 10/203,000 미만이라고 계산하고 편집자의 두 결론을 부정한다. 미적용 답은 이 비율만으로 개별 사건이 잡음일 확률을 정할 수 없다고 명시한다. 스킬 답에는 초록 앞에 ‘Method: IMRaD, standard level’이 노출되며, 이 표시와 소제목을 포함하면 145단어를 넘는다.

</details>
