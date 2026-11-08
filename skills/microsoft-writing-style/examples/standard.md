# Clearing Windows 11 Clipboard history without deleting a pinned entry

2026-11-08 · `microsoft-writing-style` 0.1.1 · English · Codex CLI 0.167.0 / gpt-6.1-sol

### Case and sources

- [Microsoft Support, Using the clipboard](https://support.microsoft.com/en-us/windows/apps/using-the-clipboard). Windows 11 section on clearing clipboard history gives the local shortcut, Clear all control and pinned-item exception. The delivery address describes an illustrative user task.

### Prompt

> Write brief Windows 11 help for a person with Clipboard history enabled on their PC. They pinned a frequently used delivery address and want to clear the other entries. Microsoft documents the Windows logo key + V shortcut to open Clipboard history and Clear all at the top of the panel to clear device history except pinned items. Tell the reader what to select and what will happen to the address. Write only the user-facing instructions, using the actual shortcut and control label; do not make a claim about synced devices.

### Without a skill

> Press **Windows logo key + V** to open Clipboard history, then select **Clear all** at the top of the panel. The other entries will be cleared, and your pinned delivery address will remain.

### With the skill at standard

> Press **Windows logo key + V** to open Clipboard history, then select **Clear all** at the top of the panel. This clears your device’s Clipboard history except pinned items. Your pinned delivery address will remain.

### What changed

**Checks set before the run.** Preserve the shortcut, the literal Clear all label and the pinned-address exception. Keep the answer scoped to this PC; no unrequested account, cloud deletion, or settings steps.

Both give the same Windows shortcut and Clear all label and correctly say the pinned address remains. The skill answer explicitly scopes the cleanup to this device and makes the general exception for pinned items clear. Both are usable here.

**차이.** 두 답 모두 Windows 로고 키 + V에서 Clear all을 누르면 고정한 주소가 남는다고 안내합니다. 스킬 답은 ‘이 장치’와 ‘고정 항목 제외’라는 범위를 한 번 더 명확히 합니다.
