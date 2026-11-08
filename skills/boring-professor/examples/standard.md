# Why deleting a Linux log file may not free disk space

2026-11-08 · `boring-professor` 0.1.1 · English · Codex CLI 0.167.0 / gpt-6.1-sol

### Case and sources

- [Linux man-pages 6.19, unlink(2)](https://man7.org/linux/man-pages/man2/unlink.2.html). DESCRIPTION defines the effect of unlinking the last directory link with and without an open descriptor. The log filename and running service are an illustrative Linux scenario.

### Prompt

> Explain the following Linux incident drill for a systems engineer in at most 100 words. An administrator successfully unlinks /var/log/payments.log while a payment service still has it open for writing. Assume this was the file's last hard link and the service holds the only open descriptor. The directory no longer lists the pathname, yet the disk space is still in use. What survived unlink, can the service still write, and what event allows that storage to be reused? The pathname and service describe a drill, not a reported outage.

### Without a skill

> Unlink removes the directory entry for `/var/log/payments.log`, but the inode and its allocated data blocks survive because the service’s open file descriptor still references the file through an open file description. The service can continue writing to it, even though the pathname no longer exists.
>
> When the service closes that last descriptor—or exits, causing it to close—the final open reference disappears. With no hard links or open references remaining, the filesystem can reclaim the inode and data blocks, making the storage available for reuse.

### With the skill at standard

> `unlink` removes the directory entry associating `/var/log/payments.log` with its inode, the filesystem object recording metadata and references to file data. Because this was the last hard link, the inode’s link count becomes zero. The open file description, referenced by the service’s descriptor, still retains the inode and its allocated storage.
>
> The service can continue writing through that descriptor, assuming writes otherwise succeed. When the service closes its only descriptor, explicitly or on process exit, the final open reference is released. The filesystem can then reclaim the unlinked file’s inode and data blocks for reuse.

### What changed

**Checks set before the run.** Distinguish directory entry from open file and file descriptor. Explain continued writes and the last-close condition under the last-hard-link assumption. Do not imply instantaneous recovery of physical bytes or invent an outage.

Both explain why the pathname disappears while the service can still write, and why the space can be reused only after the last open descriptor closes in this drill. The skill answer explicitly identifies the zero link count and defines the inode. The baseline reaches the same conclusion in fewer words.

**차이.** 두 답 모두 로그 이름을 지워도 서비스는 열어 둔 파일에 계속 쓸 수 있고, 마지막 파일 디스크립터가 닫혀야 그 공간을 재사용할 수 있다고 설명합니다. 스킬 답은 이때 하드 링크 수가 0이라는 점과 inode의 역할을 덧붙였습니다.
