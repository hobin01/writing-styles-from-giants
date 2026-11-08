# When can each Raspberry Pi 4 recovery station be powered down?

[한국어](standard.ko.md)

2026-11-08 · `asd-ste100` 0.1.3 · English · `gpt-6-luna`

### Case and sources

- [Raspberry Pi, Raspberry Pi computer hardware documentation](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#reflash-the-bootloader). Reflash the bootloader, especially the last step for an HDMI-connected board. The prompt covers only completion of a prepared recovery on the Pi 4 Model B.

**Language scope.** This English handover uses the project’s STE-inspired standard profile. It does not verify official ASD-STE100 compliance.

### Prompt

> Write a concise English handover for technicians finishing a Raspberry Pi 4 Model B bootloader recovery with HDMI displays attached. Before disconnecting power they must observe both a steady flashing pattern on the green activity LED and a green HDMI screen. Remove the recovery microSD card only after power is disconnected. In this illustrative bench drill, staff check each board at 0, 15, 30, 45 and 60 seconds. Once an indication appears it persists. At North the LED pattern starts at 16 s and the HDMI screen turns green at 29 s. At South the screen turns green at 33 s and the LED pattern starts at 41 s. At East the LED pattern starts at 21 s and the screen is still not green at 60 s. No power has yet been disconnected. Give the first qualifying check for each station and the safe action there. Explain whether the elapsed time alone can authorize removal. Use one consistent name for the recovery microSD card.

### Without the skill

> **Bench drill handover — Raspberry Pi 4 Model B**
>
> Keep power connected until both the steady flashing green activity LED pattern and a green HDMI screen are visible. Then disconnect power before removing the recovery microSD card.
>
> | Station | First check showing both indications | Safe action |
> |---|---:|---|
> | North | 30 s | Disconnect power, then remove the recovery microSD card. |
> | South | 45 s | Disconnect power, then remove the recovery microSD card. |
> | East | None by 60 s | Keep power connected; do not remove the card. |
>
> Elapsed time alone does not authorize removal. At each check, confirm both indications are present; if either is absent, keep power connected and continue checking.

### With the skill at standard

> ## Recovery handover
>
> Keep power connected until both indications are present: a steady flashing pattern on the green activity LED and a green HDMI screen. Disconnect power only after you observe both indications. Remove the recovery microSD card only after power is disconnected.
>
> In this bench drill, staff check each board at 0, 15, 30, 45, and 60 seconds. Once an indication appears, it persists.
>
> | Station | First check with both indications | Safe action |
> |---|---:|---|
> | North | 30 seconds | Both indications are present. Disconnect power, then remove the recovery microSD card. |
> | South | 45 seconds | Both indications are present. Disconnect power, then remove the recovery microSD card. |
> | East | None by 60 seconds | Keep power connected. Do not remove the recovery microSD card; wait until both indications are present. |
>
> Elapsed time alone does not authorize removal. North and South qualify at their first listed check when both indications are present. East does not qualify at 60 seconds because its HDMI screen is not green.

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Derives North’s first qualifying check as 30 s and South’s as 45 s, using observation times rather than the raw times at which indicators changed. | Met | Met |
| For East at 60 s, withholds disconnect/removal and does not imply that a fixed timeout proves success or establishes hardware failure. | Met | Met |
| States the correct sequence in technician-usable English: observe both signals, disconnect power, then remove the recovery microSD card; calls the card consistently by the same name. | Missed | Met |

**Masked review** (Y = baseline; X = standard). Both give 30 s for North, 45 s for South and no qualifying observation for East by 60 s. Both keep East powered and put disconnection before removal. X repeats “recovery microSD card” in each station row; Y shortens it to “the card” in the East row. The safety decisions agree.

<details>
<summary>Run record</summary>

Each arm was a separate ephemeral read-only Codex CLI 0.167.0 session with low reasoning effort. Neither session was given the other answer or an answer in the other language.

SHA-256 prefixes (entrypoint / baseline answer / standard answer): `6600af844428` / `9f618db8c88e` / `369141520448`.

</details>
