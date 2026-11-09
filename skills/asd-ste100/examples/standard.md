# When can each Raspberry Pi 4 recovery station be powered down?

[한국어](standard.ko.md)

2026-11-09 · `asd-ste100` 0.1.4 · English · `gpt-6-luna`

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

> ## Bootloader recovery handover
>
> Keep the HDMI displays attached. At each check, observe both the steady flashing pattern on the green activity LED and a green HDMI screen. Disconnect power only after both indications are present. Remove the recovery microSD card only after power is disconnected.
>
> | Station | First check with both indications | Safe action |
> |---|---:|---|
> | North | 30 seconds | Disconnect power, then remove the recovery microSD card. |
> | South | 45 seconds | Disconnect power, then remove the recovery microSD card. |
> | East | None by 60 seconds | Keep power connected and the recovery microSD card installed. |
>
> Elapsed time alone does not authorize removal. At East, the HDMI screen is still not green at 60 seconds, so both required indications are not present.

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Derives North’s first qualifying check as 30 s and South’s as 45 s, using observation times rather than the raw times at which indicators changed. | Met | Met |
| For East at 60 s, withholds disconnect/removal and does not imply that a fixed timeout proves success or establishes hardware failure. | Met | Met |
| States the correct sequence in technician-usable English: observe both signals, disconnect power, then remove the recovery microSD card; calls the card consistently by the same name. | Missed | Met |

**Review.** North qualifies at 30 seconds and South at 45. East stays powered with the recovery microSD card in place. The handover uses the required component name throughout.

Masked reviewer assignment: X was the revised answer. The table retains the original control grades. [Previous pair and scores](https://github.com/hobin01/writing-styles-from-giants/blob/20f24c66c7e89e6ce1007249c83c33932998bf01/skills/asd-ste100/examples/standard.md) · [All attempts and adjudications](https://github.com/hobin01/writing-styles-from-giants/blob/main/evals/runs/2026-11-09-standard/records/asd-ste100.json).

<details>
<summary>Run record</summary>

Baseline generated 2026-11-08. Revised treatment generated independently on 2026-11-09 with Codex CLI 0.167.0, low reasoning, in a fresh read-only session. SHA-256 prefixes (entrypoint / original baseline / revised answer): `441382171a3a` / `9f618db8c88e` / `aba6aa20f2e6`.

</details>
