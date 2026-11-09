# When can each Raspberry Pi 4 recovery station be powered down?

[한국어](light.ko.md) · **light** · [standard](standard.md) · [strict](strict.md)

### Question

> Three Raspberry Pi 4 Model B boards are finishing bootloader recovery with HDMI displays attached. Disconnect power only after both the green activity LED shows a steady flashing pattern and the HDMI screen is green. Remove the recovery microSD card only after disconnecting power. In this bench exercise the boards are checked at 0, 15, 30, 45 and 60 seconds. Once an indication appears, it stays. On North the LED pattern appears at 16 s and the green screen at 29 s. On South they appear at 41 s and 33 s respectively. On East the LED pattern appears at 21 s and the screen is still not green at 60 s. All three are still powered. At which check can each board be disconnected, and what happens to its recovery microSD card?

**Sources** · [Raspberry Pi, Raspberry Pi computer hardware documentation](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#reflash-the-bootloader)

### With the skill

> - **North:** Disconnect power at the 30-second check. Both indications have appeared by then. After disconnecting power, remove the recovery microSD card.
> - **South:** Disconnect power at the 45-second check. Both indications have appeared by then. After disconnecting power, remove the recovery microSD card.
> - **East:** Do not disconnect power at any listed check. The HDMI screen is still not green at 60 seconds, so both required indications are not present. Keep the recovery microSD card in place.

### Without the skill

> - **North:** Disconnect at the **30-second check**; both indications have appeared by then. After disconnecting power, remove the recovery microSD card.
> - **South:** Disconnect at the **45-second check**; both indications have appeared by then. After disconnecting power, remove the recovery microSD card.
> - **East:** **Do not disconnect at any listed check.** The screen is not green by 60 seconds, so keep the board powered and leave the recovery microSD card in place.
