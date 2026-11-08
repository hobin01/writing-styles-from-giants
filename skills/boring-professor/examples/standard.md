# Tracking two Linux log files behind the same pathname

2026-11-08 · `boring-professor` 0.1.1 at first pass · `gpt-6-luna` · Codex CLI 0.167.0

### Case and sources

- [Linux man-pages 6.19, unlink(2)](https://man7.org/linux/man-pages/man2/unlink.2.html). DESCRIPTION defines the effect of unlinking the last directory link with and without an open descriptor. The filenames, monitor, allocation sizes and event times are illustrative.

**Reasoning task.** Track two distinct file objects, two references to the unlinked file and allocated bytes at successive times instead of inferring storage from the visible pathname.

### Prompt

> Explain this Linux drill to a systems student. At 09:00 an administrator unlinks the last hard link to /var/log/payments.log. The old file has 20 MiB of allocated data; the writer and a monitor each hold an open descriptor to it. At 09:02 the service creates a separate file at the same pathname, with 5 MiB allocated. At 09:03 the original writer appends 8 MiB through its old descriptor, then closes it at 09:04. The monitor closes its old descriptor at 09:06. Trace which file gets the append, how much allocated data belongs to the two files just after 09:04 and just after 09:06, and why the pathname alone is insufficient evidence. Assume no sparse allocation, duplication or other changes; ignore metadata. Keep the explanation literal and under 120 words.

### Without a skill

> The 8 MiB append goes to the original file: the writer’s open descriptor still refers to its inode, even after the last hard link is unlinked. The new file created at `/var/log/payments.log` is separate and receives none of that append.
>
> Just after 09:04, the original has 28 MiB allocated but is unlinked; the new pathname file has 5 MiB. Just after 09:06, the original’s last open descriptor has closed, so it is deleted and has no allocated data remaining; the new file still has 5 MiB.
>
> The pathname alone cannot identify the file held by an open descriptor: after 09:02 it names the new file, while the old descriptors still refer to the original inode.

### With the skill at standard

> `unlink` removes a directory entry. An open file description can still refer to the old file after its last hard link is removed.
>
> The writer’s descriptor still refers to the original file, so its 8 MiB append goes there. The new file at `/var/log/payments.log` is separate.
>
> Just after 09:04, the original file has 28 MiB allocated (20 + 8); the new file has 5 MiB. The monitor’s descriptor still keeps the original file alive. Just after 09:06, when the monitor closes it, the original file is released, leaving 0 MiB allocated to it; the new file remains at 5 MiB.
>
> The pathname identifies the new file after 09:02. It does not identify the original file still held by open descriptors.

### First-pass assessment

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Identifies the append as going to the old, unlinked file through the writer's descriptor, not to the 5 MiB replacement at the reused pathname. | Met | Met |
| Gives 33 MiB just after 09:04 (28 old + 5 new) and 5 MiB just after 09:06; the monitor's descriptor delays release of the old file. | Missed | Missed |
| Explains the pathname/file-object distinction and the final-descriptor condition using literal technical terms, without implying that unlink disables existing writes. | Met | Met |

Both assign the 8 MiB append to the old file and explain why the pathname now names its replacement. Both give the 09:04 components as 28 MiB and 5 MiB but leave the requested total of 33 MiB to the reader. Both leave 5 MiB after the final close. The skill answer specifically names the monitor as the reason storage survives 09:04.

**차이.** 두 답 모두 8 MiB는 이전 파일에 기록되며 현재 경로는 새 파일을 가리킨다고 설명합니다. 09:04의 28 MiB와 5 MiB를 제시했지만 합계 33 MiB는 독자가 직접 계산해야 합니다. 마지막에 남는 5 MiB는 두 답 모두 맞았습니다. 스킬 답은 모니터의 디스크립터가 이전 파일을 붙잡고 있다고 명시합니다.

<details>
<summary>Developmental retest · version 0.1.2</summary>

Calculate requested totals from their components and account for each state change. This retest is excluded from the first-pass counts.

The request and original baseline are unchanged.

**New standard answer**

> At 09:00, unlinking removes the old file’s last directory entry. An open descriptor still refers to that file, so the writer’s 8 MiB append goes to the old file, not the new file created at the same pathname.
>
> Just after 09:04, the old file has 28 MiB allocated (20 + 8); the new file has 5 MiB. The old file remains allocated because the monitor still has it open.
>
> Just after 09:06, the old file’s final open descriptor is closed, so its 28 MiB is released. The new file still has 5 MiB allocated.
>
> The pathname identifies the new file after 09:02. It does not identify the old file referenced by the open descriptors, so pathname alone cannot establish which file received the append.

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Identifies the append as going to the old, unlinked file through the writer's descriptor, not to the 5 MiB replacement at the reused pathname. | Met | Met |
| Gives 33 MiB just after 09:04 (28 old + 5 new) and 5 MiB just after 09:06; the monitor's descriptor delays release of the old file. | Missed | Missed |
| Explains the pathname/file-object distinction and the final-descriptor condition using literal technical terms, without implying that unlink disables existing writes. | Met | Met |

The baseline and the skill answer correctly trace the 8 MiB append to the unlinked file. Both give the 09:04 amounts separately as 28 MiB old and 5 MiB new. Neither states the required combined total of 33 MiB, so both miss the second criterion. Both correctly leave only the new file’s 5 MiB after the last descriptor closes at 09:06. The skill answer identifies the monitor as the remaining descriptor holder and exceeds the under-120-word limit.

**차이.** 미적용 답과 스킬 답 모두 링크가 제거된 기존 파일에 8 MiB가 추가된다고 정확히 설명한다. 둘 다 09:04의 기존 파일 28 MiB와 새 파일 5 MiB를 각각 제시하지만, 요구한 합계 33 MiB를 명시하지 않아 두 번째 기준을 충족하지 못한다. 09:06에 마지막 파일 디스크립터가 닫힌 뒤 새 파일의 5 MiB만 남는다는 설명은 둘 다 맞다. 스킬 답은 남은 디스크립터를 모니터가 보유한다고 명시하지만, 120단어 미만 요건을 넘긴다.

</details>
