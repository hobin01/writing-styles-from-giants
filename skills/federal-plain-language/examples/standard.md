# Federal Plain Language-inspired explanation · A correction without a new deadline

Run on 2026-11-08 • `federal-plain-language` 0.1.1 • English • Codex CLI 0.167.0

### Prompt

> Write a notice for applicants in no more than 65 words. Applications already submitted can be corrected through the portal until 4 p.m. Friday, but only if the status is 'Returned'. A correction does not change the original filing deadline. Paper corrections are not accepted.

### Without a skill

> Notice to Applicants
>
> Applications already submitted may be corrected through the portal until 4 p.m. Friday, but only if their status is “Returned.” A correction does not change the original filing deadline. Paper corrections are not accepted.

### With the skill at standard

> You can correct an application you have already submitted through the portal until 4 p.m. Friday, but only if its status is 'Returned'.
>
> A correction does not change the original filing deadline. Paper corrections are not accepted.

### What changed

**Checks set before the run.** Keep the status restriction, exact portal deadline, unchanged original deadline and paper exclusion. Let an applicant tell whether they can act.

Both retain the status restriction, time, original deadline and paper exclusion. The skill addresses the applicant as “you” and puts the two remaining constraints in a separate paragraph. The baseline adds a notice heading.

**차이.** 두 답 모두 수정 조건과 기한을 보존합니다. 스킬 답안은 신청자에게 직접 말하고, 서면 접수 제한을 따로 모았습니다.
