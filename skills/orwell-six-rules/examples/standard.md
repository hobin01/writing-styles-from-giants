# What a unit mix-up did to the Mars Climate Orbiter estimate

[한국어](standard.ko.md)

2026-11-08 · `orwell-six-rules` 0.1.3 · English · `gpt-6-luna`

### Case and sources

- [Cornelius J. Dennehy / NASA, Best Practices for the Design, Development, and Operation of Robust and Reliable Space Vehicle Guidance, Navigation, and Control Systems (NASA/TP–20230005922, April 2023)](https://ntrs.nasa.gov/api/citations/20230005922/downloads/20230005922.pdf). Appendix A-12, pp. 138–139, and lesson 0641: ground software/interface units, trajectory about 170 km low, and two possible outcomes after loss.

### Prompt

> Rewrite this museum label as one concise English paragraph. Draft: ‘Operational misalignment effectuated a 170-km plunge. SM_FORCES supplied thruster impulses in pound-force seconds, which navigation read as newton-seconds. The craft burned up.’ The real 1999 navigation estimate accumulated error and the spacecraft approached Mars about 170 km lower than planned. NASA could not distinguish destruction in the atmosphere from escape into a solar orbit. To make the unit error concrete, use a clearly labelled illustrative impulse of 2 pound-force seconds. For this exercise use 1 pound-force second ≈ 4.45 newton-seconds. Work out what the number should have meant to navigation and how far its reading was off. Keep the illustration separate from the reported mission outcome.

### Without the skill

> A 1999 navigation error accumulated over time, bringing the spacecraft to Mars about 170 km lower than planned. NASA could not determine whether it was destroyed in the atmosphere or escaped into solar orbit. **Illustrative impulse, not a mission measurement:** 2 pound-force seconds should have meant about 8.9 newton-seconds to navigation; reading it as 2 newton-seconds was off by 6.9 newton-seconds.

### With the skill at standard

> Navigation errors accumulated during the 1999 mission, bringing the spacecraft to Mars about 170 km lower than planned. SM_FORCES supplied thruster impulses in pound-force seconds, but navigation read them as newton-seconds. **Illustrative example:** an impulse of 2 pound-force seconds should have meant about 8.9 newton-seconds to navigation; reading it as 2 meant the value was about 6.9 newton-seconds too low. NASA could not determine whether the spacecraft was destroyed in the atmosphere or escaped into solar orbit.

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| For the illustrative impulse, gives about 8.9 newton-seconds rather than the 2 read by navigation, with an understatement of about 6.9 newton-seconds or a factor of about 4.45. | Met | Met |
| Keeps the hypothetical impulse distinct from the mission record and attributes the roughly 170 km difference to the accumulated trajectory-estimate error/low approach rather than to a known plunge. | Met | Met |
| Retains both possible fates and makes the causal sequence understandable to a museum visitor in a concise paragraph. | Missed | Met |

**Masked review** (Y = baseline; X = standard). Both calculate 8.9 newton-seconds and an understatement of 6.9 for the illustration, preserve the low approach and leave both fates open. X explicitly names SM_FORCES and says which units it sent and navigation read. Y gives the mismatch only as an illustrative calculation, leaving the connection to the real accumulated error implicit.

<details>
<summary>Run record</summary>

Each arm was a separate ephemeral read-only Codex CLI 0.167.0 session with low reasoning effort. Neither session was given the other answer or an answer in the other language.

SHA-256 prefixes (entrypoint / baseline answer / standard answer): `90ee273da21c` / `38676238d03e` / `0d49ca5b7959`.

</details>
