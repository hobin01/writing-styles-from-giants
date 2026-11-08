# Why the Mars Climate Orbiter’s navigation estimate was wrong

2026-11-08 · `orwell-six-rules` 0.1.2 · English · Codex CLI 0.167.0 / gpt-6.1-sol

### Case and sources

- [Cornelius J. Dennehy / NASA, Best Practices for the Design, Development, and Operation of Robust and Reliable Space Vehicle Guidance, Navigation, and Control Systems (NASA/TP–20230005922, April 2023)](https://ntrs.nasa.gov/api/citations/20230005922/downloads/20230005922.pdf). Appendix A-12, pp. 138–139, and lesson 0641: ground software/interface units, trajectory about 170 km low, and two possible outcomes after loss.

### Prompt

> Rewrite this draft for readers of a museum exhibit in at most 75 words. Draft: In September 1999, the loss of NASA's Mars Climate Orbiter took place. A ground program called SM_FORCES made provision for thruster impulse figures in pound-force seconds. The navigation team proceeded on the assumption that the figures were in newton-seconds as required by the software interface. The mismatch caused errors in the trajectory estimate to accumulate; the spacecraft arrived about 170 km lower than planned. NASA could not determine whether it was destroyed in the atmosphere or left Mars for an orbit around the Sun.

### Without a skill

> In September 1999, NASA lost the Mars Climate Orbiter after a mix-up in units. A ground program reported thruster impulses in pound-force seconds, but navigators treated them as newton-seconds, as the software interface required. Trajectory errors accumulated, bringing the spacecraft about 170 kilometers lower than planned. NASA could not determine whether it broke apart in Mars’s atmosphere or escaped into orbit around the Sun.

### With the skill at standard

> In September 1999, NASA lost the Mars Climate Orbiter. A ground program, SM_FORCES, supplied thruster impulse figures in pound-force seconds. The navigation team assumed they were in newton-seconds, as the software interface required. This mismatch caused errors to build up in the estimated trajectory. The spacecraft arrived about 170 km lower than planned. NASA could not determine whether it was destroyed in Mars’s atmosphere or left Mars to orbit the Sun.

### What changed

**Checks set before the run.** Cut inflated phrasing while accurately attributing the mismatch to ground data, preserving the two impulse units, the approximate 170 km trajectory error and both possible fates. Avoid inventing a collision or blaming a named individual.

Both replace the inflated wording, preserve the units mismatch and describe the two possible fates. The baseline drops the program name and compresses the navigation estimate into 'trajectory errors'. The skill answer keeps SM_FORCES and distinguishes errors accumulating in an estimate from the spacecraft arriving about 170 km lower than planned.

**차이.** 두 답 모두 단위 착오와 탐사선의 두 가지 가능한 최후를 보존합니다. 스킬 답안은 지상 프로그램 이름 SM_FORCES를 남기고, 먼저 오차가 쌓인 것은 궤도 추정값이었다고 정확히 짚습니다.
