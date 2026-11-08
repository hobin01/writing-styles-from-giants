# What a unit mix-up did to the Mars Climate Orbiter estimate

2026-11-08 · `orwell-six-rules` 0.1.2 at first pass · `gpt-6-luna` · Codex CLI 0.167.0

### Case and sources

- [Cornelius J. Dennehy / NASA, Best Practices for the Design, Development, and Operation of Robust and Reliable Space Vehicle Guidance, Navigation, and Control Systems (NASA/TP–20230005922, April 2023)](https://ntrs.nasa.gov/api/citations/20230005922/downloads/20230005922.pdf). Appendix A-12, pp. 138–139, and lesson 0641: ground software/interface units, trajectory about 170 km low, and two possible outcomes after loss.

**Reasoning task.** Translate an impulse into the interface's units, compare the mistaken and correct readings, and distinguish an error in an estimate from a proved spacecraft fate.

### Prompt

> Rewrite this museum label in at most 95 words. Draft: ‘Operational misalignment effectuated a 170-km plunge. SM_FORCES supplied thruster impulses in pound-force seconds, which navigation read as newton-seconds. The craft burned up.’ The real 1999 navigation estimate accumulated error and the spacecraft approached Mars about 170 km lower than planned. NASA could not distinguish destruction in the atmosphere from escape into a solar orbit. To make the unit error concrete, use a clearly labelled illustrative impulse of 2 pound-force seconds. For this exercise use 1 pound-force second ≈ 4.45 newton-seconds. Work out what the number should have meant to navigation and how far its reading was off. Keep the illustration separate from the reported mission outcome.

### Without a skill

> A 1999 navigation estimate accumulated error, bringing the spacecraft about 170 km lower over Mars than planned. NASA could not tell whether it burned up in the atmosphere or escaped into solar orbit.
>
> **Illustrative unit error:** A thruster impulse of 2 pound-force seconds should have meant about 8.9 newton-seconds to navigation. Read as only 2 newton-seconds, it was off by 6.9 newton-seconds.

### With the skill at standard

> A 1999 navigation estimate accumulated error, bringing the spacecraft about 170 km lower over Mars than planned. NASA could not tell whether it was destroyed in the atmosphere or escaped into solar orbit.
>
> **Illustrative unit error:** An impulse of 2 pound-force seconds equals about 8.9 newton-seconds. Navigation read it as 2 newton-seconds—about 6.9 newton-seconds too low. This example illustrates the unit mismatch; it does not establish what happened to the spacecraft.

### First-pass assessment

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| For the illustrative impulse, gives about 8.9 newton-seconds rather than the 2 read by navigation, with an understatement of about 6.9 newton-seconds or a factor of about 4.45. | Met | Met |
| Keeps the hypothetical impulse distinct from the mission record and attributes the roughly 170 km difference to the accumulated trajectory-estimate error/low approach rather than to a known plunge. | Met | Met |
| Retains both possible fates and makes the causal sequence understandable to a museum visitor in no more than 95 words. | Met | Met |

Both correctly convert the illustrative 2 pound-force seconds to about 8.9 newton-seconds, give the 6.9 newton-second understatement and preserve the low approach and two possible fates. The skill answer adds an explicit sentence separating the example from the spacecraft's fate. Neither identifies SM_FORCES as the ground program in the supplied draft.

**차이.** 두 답 모두 예시의 올바른 값 8.9뉴턴초와 과소평가분 6.9뉴턴초를 구하고 탐사선의 두 가능한 최후를 보존합니다. 스킬 답은 예시로 실제 최후를 판정할 수 없다고 한 번 더 밝힙니다. 둘 다 원문의 지상 프로그램 이름은 생략했습니다.

<details>
<summary>Developmental retest · version 0.1.3</summary>

Retain identifiers that a reader needs to locate the relevant program, object or source. This retest is excluded from the first-pass counts.

The request and original baseline are unchanged.

**New standard answer**

> The 1999 Mars mission’s navigation estimate accumulated error, bringing the spacecraft about 170 km lower than planned. NASA could not tell whether it burned up in the atmosphere or escaped into solar orbit.
>
> **Illustration, not a mission measurement:** An impulse of 2 pound-force seconds should have meant about 8.9 newton-seconds to navigation. If read as 2 newton-seconds, it was short by about 6.9 newton-seconds.

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| For the illustrative impulse, gives about 8.9 newton-seconds rather than the 2 read by navigation, with an understatement of about 6.9 newton-seconds or a factor of about 4.45. | Met | Met |
| Keeps the hypothetical impulse distinct from the mission record and attributes the roughly 170 km difference to the accumulated trajectory-estimate error/low approach rather than to a known plunge. | Met | Met |
| Retains both possible fates and makes the causal sequence understandable to a museum visitor in no more than 95 words. | Missed | Missed |

Both the skill answer and the baseline separate the illustrative impulse from the mission, calculate 8.9 newton-seconds and a 6.9 newton-second shortfall, give the low approach of about 170 km, and retain both possible fates within 95 words. Neither says that the actual mission supplied impulses in pound-force seconds and navigation interpreted those numbers as newton-seconds. The reader must infer what caused the real estimate to drift from a separately marked illustration.

**차이.** 스킬 답과 미적용 답 모두 가상 충격량과 실제 임무를 구분하고, 올바른 값 8.9뉴턴초와 부족분 6.9뉴턴초를 계산한다. 실제 접근 고도가 계획보다 약 170km 낮았다는 점과 두 가지 가능한 최후도 95단어 안에 담는다. 그러나 둘 다 실제 임무에서 파운드힘초로 전달한 수치를 항법 측이 뉴턴초로 해석했다고 밝히지 않는다. 독자가 별도로 표시한 예시에서 실제 궤도 추정 오차의 원인을 유추해야 한다.

</details>
