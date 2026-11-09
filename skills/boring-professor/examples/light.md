# Tracking two Linux log files behind the same pathname

[한국어](light.ko.md) · **light** · [standard](standard.md) · [strict](strict.md)

### Question

> At 18:20 the last hard link to /var/log/jobs.log is removed on Linux. Its file has 24 MiB allocated. A writer and a monitor each still have it open. At 18:22 a new file is created at the same pathname with 7 MiB allocated. At 18:23 the writer appends 4 MiB using its original descriptor and closes it. The monitor closes its original descriptor at 18:25. There are no other changes; ignore metadata and assume allocation equals data length. Which file contains the append, and how much file data remains allocated immediately after each close?

**Sources** · [Linux man-pages 6.19, unlink(2)](https://man7.org/linux/man-pages/man2/unlink.2.html)

### With the skill

> The writer’s descriptor still refers to the original, unlinked file. Creating a new file at the same pathname does not change what existing descriptors refer to. Therefore, the 4 MiB append goes to the original file.
>
> - **18:23, writer closes:** Original file: 24 MiB + 4 MiB = **28 MiB**. New file: **7 MiB**. Total allocated file data: **35 MiB**.
> - **18:25, monitor closes:** The original file has no open descriptors or hard links, so its data is released. New file: **7 MiB**. Total allocated file data: **7 MiB**.

### Without the skill

> The append goes to the original, unlinked file because the writer’s descriptor still refers to that inode. The new `/var/log/jobs.log` is a separate file and remains 7 MiB.
>
> - **18:23, writer closes:** The original file still has a linkless open descriptor held by the monitor, so its 28 MiB remains allocated. The new file has 7 MiB allocated.
> - **18:25, monitor closes:** The original file has no links or open descriptors, so it is deleted and its 28 MiB is freed. The new file’s 7 MiB remains allocated.
