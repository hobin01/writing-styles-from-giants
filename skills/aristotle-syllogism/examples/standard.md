# Does a new moon guarantee a total solar eclipse?

2026-11-08 · `aristotle-syllogism` 0.1.2 · English · Codex CLI 0.167.0 / gpt-6.1-sol

### Case and sources

- [NASA, Why Do Eclipses Happen?](https://science.nasa.gov/eclipses/geometry/). Geometry, total and annular sections: solar eclipses occur at new moon; totality requires complete coverage, whereas an annular eclipse leaves a ring.
- [NASA, 2023 Annular Eclipse FAQ](https://science.nasa.gov/eclipses/future-eclipses/eclipse-2023/faq/). Eclipse science and the October 14, 2023 path of annularity identify the dated counterexample.

### Prompt

> Assess this planetarium visitor's argument in under 85 words: Every total solar eclipse on Earth occurs at new moon. On 14 October 2023 there was a new moon. Therefore there was a total solar eclipse on Earth that day. For the factual check, NASA identifies that day's eclipse as annular: even along the central path a ring of the Sun remained visible. Tell the visitor whether the inference follows and whether the actual event supplies a counterexample.

### Without a skill

> The inference does not follow: it affirms the consequent. Every total solar eclipse occurs at new moon, but not every new moon brings a total solar eclipse. NASA identifies the 14 October 2023 eclipse as annular: even along the central path, a ring of the Sun remained visible. Thus, that day is a counterexample to the converse claim that every new moon brings a total solar eclipse, not to the original claim that every total solar eclipse occurs at new moon.

### With the skill at standard

> The inference does not follow. The premises say every total solar eclipse on Earth occurs at new moon and that 14 October 2023 had a new moon. They do not say every new moon brings a total solar eclipse; that would be an extra premise. No existence follows from the universal premise alone.
>
> Factually, NASA identifies that day’s eclipse as annular: a ring remained visible even along the central path. Thus the actual event supplies a counterexample: both premises hold, but the conclusion fails.

### What changed

**Checks set before the run.** Keep both premises true while showing the conclusion was false on that date. Distinguish the direction of implication from the independent annular observation. Do not describe that eclipse as absent everywhere, or confuse the ring seen along the central path with totality.

Both keep the true premise and use the ring visible on 14 October 2023 to refute the converse. The baseline names the fallacy; the skill separates the inference from the dated observation. Its extra point about existence is logically correct, but the question already supplies a particular new moon.

**차이.** 두 답 모두 금환일식 때 태양의 고리가 남았다는 사실을 반례로 씁니다. 미적용 답은 오류의 이름을, 적용 답은 빠진 전제를 짚습니다.
