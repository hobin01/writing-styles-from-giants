# Clearing a Windows clipboard without losing two keepers

2026-11-08 · `microsoft-writing-style` 0.1.1 at first pass · `gpt-6-luna` · Codex CLI 0.167.0

### Case and sources

- [Microsoft Support, Using the clipboard](https://support.microsoft.com/en-us/windows/apps/using-the-clipboard). The Windows 11 sections document opening device history, clearing unpinned entries and deleting one selected item. The clipboard contents are hypothetical.

**Reasoning task.** Plan operations that transform mixed pinned and unpinned entries into an exact target set, recognizing a preservation prerequisite and an exception to a bulk action.

### Prompt

> Write Windows 11 help for a person who wants exactly two entries left in this PC's clipboard history. In this example the delivery address and an obsolete access code are pinned; a return reference and two draft notes are unpinned. Keep the address and the return reference, remove the other three, and avoid retyping either keeper. Windows logo key + V opens Clipboard history. You can pin an entry; Clear all removes the unpinned entries. See more (...) then Delete removes a chosen entry. Give one reliable sequence using Clear all, explain which action must come first and how to tell the goal was met. Use the actual controls. They only asked about this PC. Keep the help under 90 words.

### Without a skill

> 1. Press **Windows logo key + V** to open Clipboard history.
> 2. On the pinned obsolete access code, select **See more (…) > Delete** first. This removes it while keeping the pinned delivery address.
> 3. Select **Clear all** to remove the unpinned return reference and two draft notes.
> 4. To keep the return reference without retyping it, copy it again before clearing, then pin it afterward.
>
> Check that only the delivery address and return reference remain.

### With the skill at standard

> Open Clipboard history with **Windows logo key + V**. Pin the delivery address and return reference first. Then select **Clear all** to remove the obsolete access code and two draft notes; **Clear all** removes unpinned entries. Confirm that only the two keepers remain. If you clear before pinning them, they will be removed too.

### First-pass assessment

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Uses Windows logo key + V and pins the return reference before Clear all; keeps the already pinned delivery address. | Missed | Met |
| Uses See more (...) then Delete for the obsolete pinned access code, or expressly unpins it before Clear all so it is removed; does not imply Clear all alone deletes pinned items. | Met | Missed |
| Gives user-facing steps that end with exactly the address and return reference, remove the two drafts and make no unsupported claim about other devices. | Missed | Missed |

Neither procedure leaves exactly the two desired entries. The baseline correctly targets the pinned access code with Delete but clears the still-unpinned return reference; copying it before clearing and pinning afterward does not protect it. The skill answer pins the return reference first but assumes Clear all will delete the obsolete access code even though it remains pinned. Its instruction to pin the already pinned address is redundant.

**차이.** 두 절차 모두 원하는 두 항목만 남기지 못합니다. 미적용 답은 고정된 접근 코드를 개별 삭제하지만 반품 참조번호를 고정하기 전에 지웁니다. 스킬 답은 참조번호를 먼저 고정하지만 여전히 고정된 접근 코드까지 ‘모두 지우기’로 삭제된다고 잘못 설명합니다. 이미 고정된 주소를 다시 고정하라는 단계도 중복입니다.

<details>
<summary>Developmental retest · version 0.1.2</summary>

Trace the items retained and removed after every operation before writing the final procedure. This retest is excluded from the first-pass counts.

The request and original baseline are unchanged.

**New standard answer**

> 1. Press **Windows logo key + V** to open Clipboard history.
> 2. Pin the delivery address and the return reference. Confirm both show as pinned.
> 3. Select **Clear all**. This removes the unpinned obsolete access code and two draft notes. The pinned entries remain.
> 4. Select **See more (...)** next to the obsolete access code, then select **Delete**.
> 5. Check Clipboard history: the delivery address and return reference should be the only two entries.
>
> Pin both entries before **Clear all**; otherwise, **Clear all** removes them too. These steps affect this PC’s clipboard history.

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Uses Windows logo key + V and pins the return reference before Clear all; keeps the already pinned delivery address. | Missed | Met |
| Uses See more (...) then Delete for the obsolete pinned access code, or expressly unpins it before Clear all so it is removed; does not imply Clear all alone deletes pinned items. | Met | Missed |
| Gives user-facing steps that end with exactly the address and return reference, remove the two drafts and make no unsupported claim about other devices. | Missed | Met |

The baseline explicitly deletes the pinned code, then clears the unpinned return reference before pinning it. Its later instruction to copy the reference again before clearing does not make that sequence reliable. The skill answer instructs the reader to confirm both keepers are pinned, clear the drafts, delete the code individually, and verify the final two entries. Those operations can work, but the skill answer wrongly says the initially pinned code was unpinned and removed by Clear all, immediately before directing the reader to delete it.

**차이.** 미적용 답은 고정된 코드를 개별 삭제하지만 반품 참조를 고정하기 전에 전체 지우기로 지운다. 나중에 지우기 전에 다시 복사하라는 지시로는 이 순서를 신뢰할 수 없다. 스킬 답은 남길 두 항목의 고정을 확인하고 초안을 지운 다음 코드를 개별 삭제하고 최종 두 항목을 확인하도록 한다. 이 조작 순서는 성립하지만, 원래 고정된 코드를 전체 지우기로 이미 지워진 미고정 항목이라고 설명한 직후 그 코드를 삭제하라고 한다.

</details>
