# Tracking two Linux log files behind the same pathname

[한국어](strict.ko.md) · [light](light.md) · [standard](standard.md) · **strict**

### Question

> At 18:20 the last hard link to /var/log/jobs.log is removed on Linux. Its file has 24 MiB allocated. A writer and a monitor each still have it open. At 18:22 a new file is created at the same pathname with 7 MiB allocated. At 18:23 the writer appends 4 MiB using its original descriptor and closes it. The monitor closes its original descriptor at 18:25. There are no other changes; ignore metadata and assume allocation equals data length. Which file contains the append, and how much file data remains allocated immediately after each close?

**Sources** · [Linux man-pages 6.19, unlink(2)](https://man7.org/linux/man-pages/man2/unlink.2.html)

### With the skill

> A hard link is a directory entry that refers to a file’s inode. Removing the last hard link removes the pathname reference, but an open file descriptor can keep the original file’s inode and data available. Creating a new file at the same pathname creates a different file. An open descriptor continues to refer to the file it originally opened.
>
> Assume the writer and monitor descriptors refer to the original 24 MiB file. The new file at `/var/log/jobs.log` is a separate file with 7 MiB allocated. The writer’s append changes the original file by +4 MiB, making its allocated data 28 MiB.
>
> - **Immediately after the writer closes at 18:23:** original file: 28 MiB, still held open by the monitor; new file: 7 MiB. **Total: 28 MiB + 7 MiB = 35 MiB.**
> - **Immediately after the monitor closes at 18:25:** original file: 0 MiB, because it has no remaining hard links or open descriptors; new file: 7 MiB. **Total: 0 MiB + 7 MiB = 7 MiB.**
>
> The append is in the **original file**, which no longer has a pathname after 18:20. The total counts file data that remains allocated; it excludes metadata as specified.

### Without the skill

> The append goes to the original, unlinked file because the writer’s descriptor still refers to that inode. The new `/var/log/jobs.log` is a separate file and remains 7 MiB.
>
> - **18:23, writer closes:** The original file still has a linkless open descriptor held by the monitor, so its 28 MiB remains allocated. The new file has 7 MiB allocated.
> - **18:25, monitor closes:** The original file has no links or open descriptors, so it is deleted and its 28 MiB is freed. The new file’s 7 MiB remains allocated.
