# What Ingenuity’s hover time can and cannot tell an audience

2026-11-08 · `steve-jobs-presentation` 0.1.1 at first pass · `gpt-6-luna` · Codex CLI 0.167.0

### Case and sources

- [NASA, NASA’s Ingenuity Mars Helicopter Succeeds in Historic First Flight (April 19, 2021)](https://www.nasa.gov/news-release/nasas-ingenuity-mars-helicopter-succeeds-in-historic-first-flight/). Flight-day report: onboard control, altimeter-derived height and hover, total time, the airfield name and plans to analyze the data.

**Reasoning task.** Calculate a meaningful time fraction, diagnose an invalid speed estimate that mixes flight phases, and turn a limited observation into a supported presentation decision.

### Prompt

> Write three short speaker beats for a museum briefing as of 19 April 2021. Ingenuity flew autonomously at Wright Brothers Field on Mars to about 3 m, hovered for 30 seconds, and landed 39.1 seconds after takeoff. The flight proves powered, controlled flight on another planet. A proposed slide calls 3 m divided by the whole flight time 'the average climb speed.' Decide whether to use that metric. Give the audience a defensible proportion for time spent hovering and explain why the remaining time does or does not identify climb speed. Close with what the team could decide after reviewing flight data; do not assume a later test succeeded.

### Without a skill

> **What happened:** On 19 April 2021, Ingenuity flew autonomously at Wright Brothers Field on Mars, rose to about 3 m, hovered for 30 seconds, then landed 39.1 seconds after takeoff. It demonstrated powered, controlled flight on another planet.
>
> **How to describe the timing:** I would not call 3 m divided by 39.1 seconds the “average climb speed.” The hover alone was about 77% of the flight (30 ÷ 39.1). The remaining 9.1 seconds include ascent and descent, so they do not tell us how long the climb took or its speed.
>
> **What comes next:** After reviewing the flight data, the team could decide whether to attempt another flight and what changes, if any, to make. The first flight’s success does not establish that a later test succeeded.

### With the skill at standard

> **Museum briefing speaker beats**
>
> 1. **The milestone:** On 19 April 2021, Ingenuity flew autonomously at Wright Brothers Field on Mars. It reached about 3 m, hovered for 30 seconds, and landed 39.1 seconds after takeoff. The flight proved powered, controlled flight on another planet.
>
> 2. **What the timing shows:** Keep the hover proportion: 30 of 39.1 seconds, or about 77% of the flight. Don’t call 3 m divided by 39.1 seconds the “average climb speed.” That calculation spreads the height over the *whole flight*, including the hover and descent. The remaining 9.1 seconds covers ascent and descent together, so it does not tell us how long the climb took or identify climb speed.
>
> 3. **What comes next:** After reviewing the flight data, the team can decide what the measured ascent and descent looked like and whether the evidence supports planning another flight. That decision depends on the data; it does not assume a later test succeeded.

### First-pass assessment

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Reports the first Mars flight as autonomous, powered and controlled, retains about 3 m and distinguishes 30 s of hover from 39.1 s total. | Met | Met |
| Derives roughly 77% hovering and identifies the remaining 9.1 s as non-hover time including ascent and descent; rejects using total time to infer climb speed. | Met | Met |
| Uses three short audience-facing beats and closes on reviewing the flight data to inform the next test, without claiming future success. | Met | Met |

Both give three beats, put about 77% of the flight into hover, and explain why the other 9.1 seconds do not isolate the climb. Both connect the next decision to reviewing the flight data. The baseline compresses the timing objection into a shorter spoken beat; the skill answer explicitly walks through which phases the slide’s denominator includes.

**차이.** 두 답 모두 체공이 비행 시간의 약 77%이고 나머지 9.1초에는 상승과 하강이 함께 들어간다고 설명합니다. 미적용 답은 잘못된 상승 속도 계산을 짧게 풀고, 스킬 답은 슬라이드의 분모에 섞인 각 비행 단계를 설명합니다.
