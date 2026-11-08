# When to remove a Raspberry Pi 4 recovery card

2026-11-08 · `asd-ste100` 0.1.3 · English · Codex CLI 0.167.0 / gpt-6.1-sol

### Case and sources

- [Raspberry Pi, Raspberry Pi computer hardware documentation](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#reflash-the-bootloader). Reflash the bootloader, especially the last step for an HDMI-connected board. The prompt covers only completion of a prepared recovery on the Pi 4 Model B.

### Prompt

> Edit the following service note into a concise instruction for a Raspberry Pi 4 Model B technician with an HDMI display attached. The recovery microSD card has already been prepared and inserted for a bootloader reflash. Before disconnecting power, wait for both indications: a steady flashing pattern from the green activity LED and a green screen on the HDMI display. After the power is disconnected, remove the recovery microSD card. Give only these finishing steps. Use 'recovery microSD card' consistently.

### Without a skill

> 1. Wait for both a steady flashing pattern from the green activity LED and a green screen on the HDMI display.
> 2. Disconnect power.
> 3. Remove the recovery microSD card.

### With the skill at standard

> 1. Wait until both the green activity LED flashes in a steady pattern and the HDMI display shows a green screen.
> 2. Disconnect power.
> 3. Remove the recovery microSD card.

### What changed

**Checks set before the run.** Keep both independent visual completion conditions, then disconnect power, then remove the recovery microSD card. A continuously lit LED, one flash alone or an error screen is insufficient. Do not add a new formatting step or extend these instructions to every Pi model.

Both give the same three finishing steps. Each requires the flashing activity LED and the green HDMI screen before power is disconnected; each removes the recovery microSD card only afterward. The baseline already meets the procedure checks.

**차이.** 두 답 모두 초록색 LED의 점멸과 초록색 HDMI 화면을 함께 확인한 뒤 전원을 끊고 복구용 microSD 카드를 빼라고 안내합니다. 이 절차에서는 적용 전후 차이가 작습니다.
