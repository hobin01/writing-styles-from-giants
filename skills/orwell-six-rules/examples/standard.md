# What a unit mix-up did to the Mars Climate Orbiter estimate

[한국어](standard.ko.md) · [light](light.md) · [strict](strict.md)

### Question

> A draft about the 1999 Mars Climate Orbiter says, ‘Operational misalignment effectuated a 170-km plunge. SM_FORCES supplied thruster impulses in pound-force seconds, which navigation read as newton-seconds. The craft burned up.’ The trajectory estimate accumulated error and the spacecraft approached Mars about 170 km lower than planned. NASA could not distinguish destruction in the atmosphere from escape into a solar orbit. Suppose SM_FORCES had sent the number 2; this is an illustration, not a flight measurement. Use 1 pound-force second ≈ 4.45 newton-seconds. What should the draft say about the unit error and the spacecraft’s fate?

**Sources** · [Cornelius J. Dennehy / NASA, Best Practices for the Design, Development, and Operation of Robust and Reliable Space Vehicle Guidance, Navigation, and Control Systems (NASA/TP–20230005922, April 2023)](https://ntrs.nasa.gov/api/citations/20230005922/downloads/20230005922.pdf)

### Standard

> The SM_FORCES component sent thruster impulses in pound-force seconds, but navigation read the values as newton-seconds. For example, 2 pound-force seconds × 4.45 newton-seconds per pound-force second ≈ 8.9 newton-seconds. If navigation treated the unchanged numeral 2 as newton-seconds, it read an impulse of 2 newton-seconds. The 2 is illustrative, not a flight measurement.
>
> The trajectory estimate accumulated error, and the spacecraft approached Mars about 170 km lower than planned. NASA could not determine whether it was destroyed in the atmosphere or escaped into a solar orbit. Its fate remains unknown.
