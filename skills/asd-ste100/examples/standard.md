# When can each Raspberry Pi 4 recovery station be powered down?

2026-11-08 · `asd-ste100` 0.1.3 at first pass · `gpt-6-luna` · Codex CLI 0.167.0

### Case and sources

- [Raspberry Pi, Raspberry Pi computer hardware documentation](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#reflash-the-bootloader). Reflash the bootloader, especially the last step for an HDMI-connected board. The prompt covers only completion of a prepared recovery on the Pi 4 Model B.

**Reasoning task.** Combine two necessary conditions with discrete observation times, handle incomplete evidence at the last check, and preserve the ordered safety prerequisite in a technical handover.

### Prompt

> Write a concise English handover for technicians finishing a Raspberry Pi 4 Model B bootloader recovery with HDMI displays attached. Before disconnecting power they must observe both a steady flashing pattern on the green activity LED and a green HDMI screen. Remove the recovery microSD card only after power is disconnected. In this illustrative bench drill, staff check each board at 0, 15, 30, 45 and 60 seconds. Once an indication appears it persists. At North the LED pattern starts at 16 s and the HDMI screen turns green at 29 s. At South the screen turns green at 33 s and the LED pattern starts at 41 s. At East the LED pattern starts at 21 s and the screen is still not green at 60 s. No power has yet been disconnected. Give the first qualifying check for each station and the safe action there. Explain whether the elapsed time alone can authorize removal. Use one consistent name for the recovery microSD card.

### Without a skill

> ## Bench handover
>
> Keep both HDMI displays attached and leave power connected until each board shows **both** a steady flashing pattern on the green activity LED and a green HDMI screen. Remove the recovery microSD card only after disconnecting power.
>
> Checks are at 0, 15, 30, 45 and 60 seconds. Once an indication appears, it persists.
>
> | Station | First check showing both indications | Safe action |
> |---|---:|---|
> | North | 30 seconds | Disconnect power, then remove the recovery microSD card. |
> | South | 45 seconds | Disconnect power, then remove the recovery microSD card. |
> | East | No qualifying check by 60 seconds | Keep power connected and the card in place; wait for both indications, then disconnect power before removing the card. |
>
> Elapsed time alone does **not** authorize removal. Each board must show both indications first, and power must be disconnected before removing the recovery microSD card.

### With the skill at standard

> North first qualifies at 30 seconds: both indications are present. Disconnect power, then remove the recovery microSD card.
>
> South first qualifies at 45 seconds: both indications are present. Disconnect power, then remove the recovery microSD card.
>
> East does not qualify at any check through 60 seconds because its HDMI screen is not green. Keep power connected and the recovery microSD card in place; continue recovery until both indications are present.
>
> Elapsed time alone does not authorize removal. Disconnect power only after you observe both the steady flashing pattern on the green activity LED and a green HDMI screen. Remove the recovery microSD card only after power is disconnected.

### First-pass assessment

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Derives North’s first qualifying check as 30 s and South’s as 45 s, using observation times rather than the raw times at which indicators changed. | Met | Met |
| For East at 60 s, withholds disconnect/removal and does not imply that a fixed timeout proves success or establishes hardware failure. | Met | Met |
| States the correct sequence in technician-usable English: observe both signals, disconnect power, then remove the recovery microSD card; calls the card consistently by the same name. | Missed | Met |

Both schedule North at 30 s and South at 45 s and keep East powered at 60 s. Both place removal after disconnection. The baseline gives a useful table, but refers to “both HDMI displays” for a three-station drill and shortens the requested recovery microSD card name to “the card” in the East row. The skill answer keeps the specified name in its actions.

**차이.** 두 답 모두 North는 30초, South는 45초에 전원을 끊을 수 있고 East는 60초에도 기다려야 한다고 판단합니다. 미적용 답의 표는 읽기 쉽지만 세 작업대를 두고 ‘두 화면’이라고 쓰고 카드 이름도 한 곳에서 줄였습니다. 스킬 답은 작업 지시에서 지정한 카드 이름을 유지합니다.
