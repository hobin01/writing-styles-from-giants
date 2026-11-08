# Can new moon and central alignment alone establish a total solar eclipse?

[한국어](standard.ko.md)

2026-11-08 · `aristotle-syllogism` 0.1.2 · English · `gpt-6-luna`

### Case and sources

- [NASA, Why Do Eclipses Happen?](https://science.nasa.gov/eclipses/geometry/). Geometry, total and annular sections: solar eclipses occur at new moon; totality requires complete coverage, whereas an annular eclipse leaves a ring.
- [NASA, 2023 Annular Eclipse FAQ](https://science.nasa.gov/eclipses/future-eclipses/eclipse-2023/faq/). Eclipse science and the October 14, 2023 path of annularity identify the dated counterexample.

### Prompt

> A planetarium visitor reasons: 'Every total solar eclipse occurs at new moon; this is a new moon, so it is total.' They also argue that if it were not new moon, there could not be a total solar eclipse. Assess the two inferences separately. For a separate illustrative drawing, suppose an observer sees the two disks exactly centered, the Sun has angular diameter 0.53° and the Moon 0.50°. Calculate the angular width of the exposed rim on one side and infer what the observer would see. Then consider a centered 0.55° Moon instead. Use the actual annular solar eclipse of 14 October 2023 as a factual check, without attributing these invented diameters to it. Keep the answer concise enough to read beside the diagram. Write the answer in English.

### Without the skill

> The first inference reverses the implication: a total solar eclipse occurs at new moon, but a new moon does not guarantee a total eclipse. The Sun and Moon must also align closely, and the Moon must appear large enough to cover the Sun. The second inference is correct: without a new moon, there is no solar eclipse, total or otherwise.
>
> For the centered disks in the drawing, the 0.53° Sun exceeds the 0.50° Moon by 0.03°, leaving an exposed rim **0.015° wide on each side**. The observer would see an **annular eclipse**: a bright ring of sunlight around the Moon. With a centered 0.55° Moon, the Moon is larger than the Sun and would fully cover it, producing a **total eclipse**.
>
> As a factual check, the eclipse of 14 October 2023 was annular along its path: the Moon appeared too small to cover the Sun completely. The drawing’s invented diameters illustrate the geometry; they are not measurements from that eclipse.

### With the skill at standard

> ### The two inferences
>
> 1. **“Every total solar eclipse occurs at new moon; this is a new moon, so it is total.”**\
>    Premise: All total solar eclipses occur at new moon.\
>    Premise: This is a new moon.\
>    Conclusion: This is a total solar eclipse.
>
>    The conclusion does not follow: the first premise says total eclipses require a new moon, not that every new moon has a total eclipse. A new moon alone does not establish that the Moon is aligned with the Sun or appears large enough to cover it. The stated premise is a necessary condition, not a sufficient one.
>
> 2. **“If it were not new moon, there could not be a total solar eclipse.”**\
>    This is a valid restatement of the first premise: a total solar eclipse entails a new moon. It does not establish that any particular new moon produces a total eclipse. These are logical assessments; the premises’ factual support is separate.
>
> ### Disk drawing
>
> With the disks exactly centered, the 0.53° Sun and 0.50° Moon differ by 0.03° in diameter. The exposed rim on **one side** is half that difference: **0.015°**. In this simplified drawing, sunlight remains visible all around the Moon’s edge: an annular, “ring of fire” appearance.
>
> With a centered 0.55° Moon, the Moon is 0.02° wider than the Sun. It covers the Sun’s disk in the drawing, giving a total-eclipse appearance.
>
> These are illustrative angular diameters, not measurements of the 14 October 2023 eclipse. That event was an **annular solar eclipse**; the Moon did not completely cover the Sun along the path of annularity. The drawing’s exact centering and diameters are assumptions for the illustration, not claims about that event.

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Explains that new moon is necessary but insufficient, rejects the converse, and accepts the contrapositive about a non-new moon. | Met | Met |
| Computes the one-sided rim as (0.53−0.50)/2 = 0.015°, leading to a ring; with the centered 0.55° Moon the solar disk is fully covered at that observer. | Met | Met |
| Uses the 14 October 2023 annular eclipse as a real counterexample without presenting the classroom drawing’s diameters as measured historical values. | Met | Met |

**Masked review** (Y = baseline; X = standard). Both reject the converse, accept the contrapositive and find the 0.015° rim; both distinguish the classroom geometry from the October 2023 eclipse. X separates premises, conclusion and drawing into sections. Y reaches the same results in fewer words, which better fits a diagram label.

<details>
<summary>Run record</summary>

Each arm was a separate ephemeral read-only Codex CLI 0.167.0 session with low reasoning effort. Neither session was given the other answer or an answer in the other language.

SHA-256 prefixes (entrypoint / baseline answer / standard answer): `d69f028ec500` / `12e925d97f7e` / `ab6d3996f923`.

</details>
