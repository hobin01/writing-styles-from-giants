# Clearing a Windows clipboard without losing two keepers

[한국어](standard.ko.md)

2026-11-09 · `microsoft-writing-style` 0.1.11 · English · `gpt-6-luna`

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

> To leave exactly the delivery address and return reference in this PC’s clipboard history, first protect the address, then remove the obsolete access code and both draft notes. **Clear all removes every unpinned entry**, so pin the return reference before you use it.
>
> Press **Windows logo key + V** to open Clipboard history.
>
> | Item | Current state | What to do now |
> |---|---|---|
> | Delivery address | Pinned | Leave it as it is. |
> | Obsolete access code | Pinned | Select **See more (...)**, then **Delete**. |
> | Return reference | Unpinned | Pin it. |
> | First draft note | Unpinned | Leave it for **Clear all**. |
> | Second draft note | Unpinned | Leave it for **Clear all**. |
>
> After those steps, select **Clear all**. Check Clipboard history: the delivery address and return reference should be the only two entries left.

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Uses Windows logo key + V and pins the return reference before Clear all; keeps the already pinned delivery address. | Met | Met |
| Uses See more (...) then Delete for the obsolete pinned access code, or expressly unpins it before Clear all so it is removed; does not imply Clear all alone deletes pinned items. | Missed | Met |
| Gives user-facing steps that end with exactly the address and return reference, remove the two drafts and make no unsupported claim about other devices. | Missed | Met |

**Review.** The sequence protects the unpinned return reference, keeps the pinned address and removes the unwanted pinned code separately. The two drafts go in the bulk clear.

Masked reviewer assignment: Y was the revised answer. The table retains the original control grades. [Previous pair and scores](https://github.com/hobin01/writing-styles-from-giants/blob/20f24c66c7e89e6ce1007249c83c33932998bf01/skills/microsoft-writing-style/examples/standard.md) · [All attempts and adjudications](https://github.com/hobin01/writing-styles-from-giants/blob/main/evals/runs/2026-11-09-standard/records/microsoft-writing-style.json).

<details>
<summary>Run record</summary>

Baseline generated 2026-11-08. Revised treatment generated independently on 2026-11-09 with Codex CLI 0.167.0, low reasoning, in a fresh read-only session. SHA-256 prefixes (entrypoint / original baseline / revised answer): `0478d6d5cc87` / `4df37c28e2f2` / `8db00fcc99c0`.

</details>
