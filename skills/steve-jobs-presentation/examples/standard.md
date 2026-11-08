# What Ingenuity’s hover time can and cannot tell an audience

[한국어](standard.ko.md)

2026-11-08 · `steve-jobs-presentation` 0.1.1 · English · `gpt-6-luna`

### Case and sources

- [NASA, NASA’s Ingenuity Mars Helicopter Succeeds in Historic First Flight (April 19, 2021)](https://www.nasa.gov/news-release/nasas-ingenuity-mars-helicopter-succeeds-in-historic-first-flight/). Flight-day report: onboard control, altimeter-derived height and hover, total time, the airfield name and plans to analyze the data.

### Prompt

> Write three short speaker beats for a museum briefing as of 19 April 2021. Ingenuity flew autonomously at Wright Brothers Field on Mars to about 3 m, hovered for 30 seconds, and landed 39.1 seconds after takeoff. The flight proves powered, controlled flight on another planet. A proposed slide calls 3 m divided by the whole flight time 'the average climb speed.' Decide whether to use that metric. Give the audience a defensible proportion for time spent hovering and explain why the remaining time does or does not identify climb speed. Close with what the team could decide after reviewing flight data; do not assume a later test succeeded. Write the answer in English.

### Without the skill

> 1. Ingenuity’s first flight at Wright Brothers Field was autonomous: it climbed to about 3 metres, hovered for 30 seconds, and landed 39.1 seconds after takeoff. It demonstrated powered, controlled flight on another planet.
>
> 2. I would not call 3 metres divided by the full 39.1 seconds the “average climb speed.” The hover alone was 30 of 39.1 seconds—about 77% of the flight. The remaining 9.1 seconds include both ascent and descent, so they do not tell us how long the climb took or establish a climb speed.
>
> 3. After reviewing the flight data, the team could assess how the helicopter and its systems performed and decide whether to attempt another flight. That decision would depend on the data; it does not mean a later test had succeeded.

### With the skill at standard

> **Method status:** Jobs-inspired presentation structure · standard
>
> 1. **The milestone:** “On 19 April 2021, Ingenuity flew autonomously at Wright Brothers Field on Mars. It reached about 3 metres, hovered for 30 seconds, and landed 39.1 seconds after takeoff. The flight demonstrated powered, controlled flight on another planet.”
>
> 2. **What the timing tells us:** “The hover took about 77% of the flight: 30 divided by 39.1. I would not label 3 metres divided by the whole flight time—about 0.077 metres per second—as the average climb speed. The total includes the 30-second hover and time spent descending, so the remaining 9.1 seconds cannot tell us how long the climb took.”
>
> 3. **What comes next:** “The flight establishes the milestone; the timing alone does not establish climb speed. After reviewing the flight data, the team could decide whether it supports a climb-speed estimate and what, if anything, to investigate in a later flight. That would be a decision based on the data, not a claim that a later test succeeded.”

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Reports the first Mars flight as autonomous, powered and controlled, retains about 3 m and distinguishes 30 s of hover from 39.1 s total. | Met | Met |
| Derives roughly 77% hovering and identifies the remaining 9.1 s as non-hover time including ascent and descent; rejects using total time to infer climb speed. | Met | Met |
| Uses three short audience-facing beats and closes on reviewing the flight data to inform the next test, without claiming future success. | Met | Missed |

**Masked review** (X = baseline; Y = standard). Both give the roughly 77% hover share, separate the 9.1 seconds of ascent and descent, and decline to infer climb speed. X gives three brief, speakable beats. Y's second beat is longer and the visible method status is additional material outside the requested three beats; its closing decision is still conditional on the data.

<details>
<summary>Run record</summary>

Each arm was a separate ephemeral read-only Codex CLI 0.167.0 session with low reasoning effort. Neither session was given the other answer or an answer in the other language.

SHA-256 prefixes (entrypoint / baseline answer / standard answer): `172a5e6964a7` / `7cd7cfac8849` / `b1d810da602d`.

</details>
