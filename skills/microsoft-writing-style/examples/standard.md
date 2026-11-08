# Microsoft-inspired technology writing · Restoring a workspace from an archive

Run on 2026-11-08 • `microsoft-writing-style` 0.1.1 • English • Codex CLI 0.167.0

### Prompt

> Rewrite this help text for someone using the app. Keep it under 70 words. Only workspace owners may select the button labelled 'Restore copy'. They may do so only after the archive has been verified. The action creates a separate copy; it does not change the current workspace. A storage quota might block creation.

### Without a skill

> After the archive has been verified, workspace owners can select **Restore copy** to create a separate copy. The current workspace stays unchanged. If there isn’t enough available storage within your quota, the copy can’t be created.

### With the skill at standard

> Only workspace owners may select **Restore copy**, and only after the archive has been verified. This action creates a separate copy without changing the current workspace. A storage quota might prevent the copy from being created.

### What changed

**Checks set before the run.** Keep the exact UI label, owner restriction, verified archive prerequisite, separate copy and unchanged workspace. Preserve quota as a possibility.

Both preserve the label and separate-copy behavior. The baseline omits the explicit ‘only’ on the owner restriction and gives a more specific interpretation of the quota than the source. The skill keeps both restrictions and the possibility of a block visible.

**차이.** 미적용 답안에서는 소유자만 가능하다는 제한이 약해졌습니다. 스킬 답안은 권한·검증 조건을 버튼 이름 바로 앞에 놓습니다.
