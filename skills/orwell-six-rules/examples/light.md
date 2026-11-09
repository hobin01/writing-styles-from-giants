# What a unit mix-up did to the Mars Climate Orbiter estimate

[한국어](light.ko.md) · **light** · [standard](standard.md) · [strict](strict.md)

### Question

> A draft about the 1999 Mars Climate Orbiter says, ‘Operational misalignment effectuated a 170-km plunge. SM_FORCES supplied thruster impulses in pound-force seconds, which navigation read as newton-seconds. The craft burned up.’ The trajectory estimate accumulated error and the spacecraft approached Mars about 170 km lower than planned. NASA could not distinguish destruction in the atmosphere from escape into a solar orbit. Suppose SM_FORCES had sent the number 2; this is an illustration, not a flight measurement. Use 1 pound-force second ≈ 4.45 newton-seconds. What should the draft say about the unit error and the spacecraft’s fate?

**Sources** · [Cornelius J. Dennehy / NASA, Best Practices for the Design, Development, and Operation of Robust and Reliable Space Vehicle Guidance, Navigation, and Control Systems (NASA/TP–20230005922, April 2023)](https://ntrs.nasa.gov/api/citations/20230005922/downloads/20230005922.pdf)

### With the skill

> SM_FORCES sent thruster impulses in pound-force seconds, but navigation treated the values as newton-seconds. For example, 2 pound-force seconds is about 8.9 newton-seconds; if navigation read the unchanged numeral as 2 newton-seconds, it undercounted the impulse. The number 2 is illustrative, not a flight measurement.
>
> The trajectory estimate accumulated error, and the spacecraft approached Mars about 170 km lower than planned. NASA could not determine whether it was destroyed in the atmosphere or escaped into a solar orbit.

### Without the skill

> “The navigation system treated SM_FORCES’ thruster impulses as newton-seconds, though they were in pound-force seconds. Thus a value of 2 pound-force seconds corresponds to about 8.9 newton-seconds; 2 is only an illustration, not a flight measurement. The resulting trajectory error brought the spacecraft to Mars about 170 km lower than planned. NASA could not determine whether it was destroyed in the atmosphere or escaped into solar orbit.”
