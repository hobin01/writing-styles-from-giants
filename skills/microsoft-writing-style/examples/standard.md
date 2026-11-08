# Clearing a Windows clipboard without losing two keepers

[한국어](standard.ko.md)

2026-11-08 · `microsoft-writing-style` 0.1.2 · English · `gpt-6-luna`

### Case and sources

- [Microsoft Support, Using the clipboard](https://support.microsoft.com/en-us/windows/apps/using-the-clipboard). The Windows 11 sections document opening device history, clearing unpinned entries and deleting one selected item. The clipboard contents are hypothetical.

**Language scope.** This English example applies the English technology-writing profile to an English Windows interface.

### Prompt

> Write Windows 11 help for a person who wants exactly two entries left in this PC's clipboard history. The Windows interface is in English. In this example the delivery address and an obsolete access code are pinned; a return reference and two draft notes are unpinned. Keep the address and the return reference, remove the other three, and avoid retyping either keeper. Windows logo key + V opens Clipboard history. You can pin an entry; Clear all removes the unpinned entries. See more (...) then Delete removes a chosen entry. Give one reliable sequence using Clear all, explain which action must come first and how to tell the goal was met. Use the actual controls. They only asked about this PC. Keep it concise. Write your answer in English.

### Without the skill

> 1. Press **Windows logo key + V** to open Clipboard history.
> 2. Find the **delivery address** and **return reference**. For each one, select **See more (…) > Pin**. Do this **before** clearing anything, so both keepers survive.
> 3. Select **Clear all**. This removes the unpinned **obsolete access code** and **two draft notes**.
> 4. Check the history: it should show exactly the **delivery address** and **return reference**, both pinned. No retyping is needed.
>
> This changes clipboard history on this PC only.

### With the skill at standard

> Open Clipboard history with **Windows logo key + V**. To keep the delivery address and return reference without retyping either:
>
> 1. If the return reference is not pinned, select **See more (...)** next to it, then **Pin**.
> 2. Select **Clear all**. This removes the unpinned obsolete access code and both draft notes. The address and return reference stay because they’re pinned.
> 3. Check Clipboard history. Exactly two entries should remain: the delivery address and return reference. Both should show as pinned.
>
> Pin the return reference before selecting **Clear all**; otherwise, Clear all removes it. These steps affect clipboard history on this PC.

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Uses Windows logo key + V and pins the return reference before Clear all; keeps the already pinned delivery address. | Met | Met |
| Uses See more (...) then Delete for the obsolete pinned access code, or expressly unpins it before Clear all so it is removed; does not imply Clear all alone deletes pinned items. | Missed | Missed |
| Gives user-facing steps that end with exactly the address and return reference, remove the two drafts and make no unsupported claim about other devices. | Missed | Missed |

**Masked review** (X = baseline; Y = standard). Both tell the reader to pin the return reference before Clear all. X unnecessarily asks the reader to pin the already pinned address as well. Both incorrectly describe the obsolete access code as unpinned: it survives Clear all, and neither answer deletes or unpins it. Their checks for a final two-item history cannot repair that missing step.

<details>
<summary>Run record</summary>

Each arm was a separate ephemeral read-only Codex CLI 0.167.0 session with low reasoning effort. Neither session was given the other answer or an answer in the other language.

SHA-256 prefixes (entrypoint / baseline answer / standard answer): `fe6a3443c596` / `4df37c28e2f2` / `3db328b316a7`.

</details>
