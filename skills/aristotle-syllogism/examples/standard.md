# Can new moon and central alignment alone establish a total solar eclipse?

2026-11-08 · `aristotle-syllogism` 0.1.2 at first pass · `gpt-6-luna` · Codex CLI 0.167.0

### Case and sources

- [NASA, Why Do Eclipses Happen?](https://science.nasa.gov/eclipses/geometry/). Geometry, total and annular sections: solar eclipses occur at new moon; totality requires complete coverage, whereas an annular eclipse leaves a ring.
- [NASA, 2023 Annular Eclipse FAQ](https://science.nasa.gov/eclipses/future-eclipses/eclipse-2023/faq/). Eclipse science and the October 14, 2023 path of annularity identify the dated counterexample.

**Reasoning task.** Distinguish a converse from a contrapositive and use the radius difference of centered disks to test which geometry supplies a counterexample.

### Prompt

> A planetarium visitor reasons: 'Every total solar eclipse occurs at new moon; this is a new moon, so it is total.' They also argue that if it were not new moon, there could not be a total solar eclipse. Assess the two inferences separately. For a separate illustrative drawing, suppose an observer sees the two disks exactly centered, the Sun has angular diameter 0.53° and the Moon 0.50°. Calculate the angular width of the exposed rim on one side and infer what the observer would see. Then consider a centered 0.55° Moon instead. Use the actual annular solar eclipse of 14 October 2023 as a factual check, without attributing these invented diameters to it. Keep the answer concise enough to read beside the diagram.

### Without a skill

> **The logic.** “Every total eclipse happens at new moon” means a total eclipse requires a new moon. But it does not mean every new moon produces a total eclipse: the Moon must also pass directly in front of the Sun. The reverse claim is correct: without a new moon, there can be no total solar eclipse.
>
> **Illustrative drawing.** With the disks exactly centered, the 0.53° Sun and 0.50° Moon leave a diameter difference of 0.03°, so the exposed rim is **0.015° wide on each side**. The observer sees a bright ring of sunlight: an **annular eclipse**, not a total one. With a centered 0.55° Moon, it covers the 0.53° Sun completely, so the observer sees a **total eclipse**.
>
> **Factual check.** On 14 October 2023, an actual annular eclipse crossed the Americas: along its path, the Moon appeared too small to cover the Sun, leaving a bright ring. The invented diameters above are only for the drawing.

### With the skill at standard

> **Two inferences**
>
> Let total eclipses be events that occur at new moon. “Every total solar eclipse occurs at new moon” says total eclipses are included among new moons; it does not say every new moon produces a total eclipse. The first inference is invalid: the Moon could be new without a total eclipse occurring. A total eclipse also requires suitable alignment and apparent sizes.
>
> “If it were not new moon, there could not be a total solar eclipse” is the contrapositive of the first premise, so it follows: a total solar eclipse requires new moon. Neither inference establishes that the premise is factually supported; the first conclusion simply reverses its direction.
>
> **Illustrative drawing**
>
> With centered disks, the diameter difference is $0.53° - 0.50° = 0.03°$. The exposed rim on one side is half of that: **0.015°**. The Moon appears slightly smaller, leaving a thin ring of the Sun visible around it: an **annular** appearance, not a total eclipse.
>
> For a centered **0.55° Moon**, it exceeds the Sun’s diameter by $0.02°$, or **0.01° per side**. It would cover the Sun’s disk, producing a total-eclipse appearance, assuming the centers align exactly.
>
> As a factual check, the **14 October 2023** solar eclipse was annular along its path; that does not make the illustrative diameters actual measurements of that eclipse.

<details>
<summary>Original model text</summary>

````text
**Two inferences**

Let total eclipses be events that occur at new moon. “Every total solar eclipse occurs at new moon” says total eclipses are included among new moons; it does not say every new moon produces a total eclipse. The first inference is invalid: the Moon could be new without a total eclipse occurring. A total eclipse also requires suitable alignment and apparent sizes.

“If it were not new moon, there could not be a total solar eclipse” is the contrapositive of the first premise, so it follows: a total solar eclipse requires new moon. Neither inference establishes that the premise is factually supported; the first conclusion simply reverses its direction.

**Illustrative drawing**

With centered disks, the diameter difference is \(0.53° - 0.50° = 0.03°\). The exposed rim on one side is half of that: **0.015°**. The Moon appears slightly smaller, leaving a thin ring of the Sun visible around it: an **annular** appearance, not a total eclipse.

For a centered **0.55° Moon**, it exceeds the Sun’s diameter by \(0.02°\), or **0.01° per side**. It would cover the Sun’s disk, producing a total-eclipse appearance, assuming the centers align exactly.

As a factual check, the **14 October 2023** solar eclipse was annular along its path; that does not make the illustrative diameters actual measurements of that eclipse.
````

</details>

### First-pass assessment

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Explains that new moon is necessary but insufficient, rejects the converse, and accepts the contrapositive about a non-new moon. | Met | Met |
| Computes the one-sided rim as (0.53−0.50)/2 = 0.015°, leading to a ring; with the centered 0.55° Moon the solar disk is fully covered at that observer. | Met | Met |
| Uses the 14 October 2023 annular eclipse as a real counterexample without presenting the classroom drawing’s diameters as measured historical values. | Met | Met |

Both reject the converse, accept the non-new-moon inference, and obtain a 0.015° rim or full coverage for the larger centered Moon. Both keep the 2023 event separate from the drawing. The baseline is shorter for a diagram label. The skill answer explicitly names the contrapositive and states the alignment and apparent-size conditions.

**차이.** 두 답 모두 역은 성립하지 않고 대우는 성립한다는 점, 한쪽 테두리가 0.015°라는 점, 실제 2023년 일식과 가상 그림의 차이를 지킵니다. 미적용 답은 도표 옆에 두기에 짧고, 스킬 답은 대우와 겉보기 크기 조건을 더 분명히 짚습니다.
