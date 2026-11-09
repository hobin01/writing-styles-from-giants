# What Ingenuity’s hover time can and cannot tell an audience

[한국어](standard.ko.md)

2026-11-09 · `steve-jobs-presentation` 0.1.8 · English · `gpt-6-luna`

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

> 1. “On 19 April 2021, Ingenuity flew autonomously at Wright Brothers Field on Mars, reaching about 3 meters. The flight demonstrated powered, controlled flight on another planet.”
>
> 2. “It hovered for 30 seconds of its 39.1-second flight—about 77 percent. I would not label 3 meters divided by total flight time as average climb speed: the remaining 9.1 seconds include ascent and descent, so they do not tell us how long the climb took.”
>
> 3. “After reviewing the flight data, the team can decide what to change or measure in a future flight; that review alone cannot tell us whether a later test will succeed.”

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Reports the first Mars flight as autonomous, powered and controlled, retains about 3 m and distinguishes 30 s of hover from 39.1 s total. | Met | Met |
| Derives roughly 77% hovering and identifies the remaining 9.1 s as non-hover time including ascent and descent; rejects using total time to infer climb speed. | Met | Met |
| Uses three short audience-facing beats and closes on reviewing the flight data to inform the next test, without claiming future success. | Met | Met |

**Review.** The three spoken beats distinguish the 30-second hover from the whole flight. Ascent and descent share the remaining 9.1 seconds; reviewing the flight data informs the next test.

Masked reviewer assignment: X was the revised answer. The table retains the original control grades. [Previous pair and scores](https://github.com/hobin01/writing-styles-from-giants/blob/20f24c66c7e89e6ce1007249c83c33932998bf01/skills/steve-jobs-presentation/examples/standard.md) · [All attempts and adjudications](https://github.com/hobin01/writing-styles-from-giants/blob/main/evals/runs/2026-11-09-standard/records/steve-jobs-presentation.json).

<details>
<summary>Run record</summary>

Baseline generated 2026-11-08. Revised treatment generated independently on 2026-11-09 with Codex CLI 0.167.0, low reasoning, in a fresh read-only session. SHA-256 prefixes (entrypoint / original baseline / revised answer): `24a22d2a3e7c` / `7cd7cfac8849` / `5e0194f544ea`.

</details>
