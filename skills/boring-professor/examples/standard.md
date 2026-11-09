# Tracking two Linux log files behind the same pathname

[한국어](standard.ko.md) · [light](light.md) · **standard** · [strict](strict.md)

### Question

> At 18:20 the last hard link to /var/log/jobs.log is removed on Linux. Its file has 24 MiB allocated. A writer and a monitor each still have it open. At 18:22 a new file is created at the same pathname with 7 MiB allocated. At 18:23 the writer appends 4 MiB using its original descriptor and closes it. The monitor closes its original descriptor at 18:25. There are no other changes; ignore metadata and assume allocation equals data length. Which file contains the append, and how much file data remains allocated immediately after each close?

**Sources** · [Linux man-pages 6.19, unlink(2)](https://man7.org/linux/man-pages/man2/unlink.2.html)

### With the skill

> A file descriptor refers to an open file independently of the pathname used to open it. Removing the last hard link removes the pathname reference; the file’s data remains allocated while an open descriptor still refers to it. Creating a new file at that pathname creates a separate file.
>
> The append at 18:23 goes to the original file, because the writer uses its original descriptor. The new file at `/var/log/jobs.log` remains 7 MiB.
>
> - **18:23, after the writer closes:** Original file: 24 MiB + 4 MiB = 28 MiB. New file: 7 MiB. **Total allocated file data: 28 MiB + 7 MiB = 35 MiB.**
> - **18:25, after the monitor closes:** The original file has no remaining open descriptors and no pathname, so its data is released. New file: 7 MiB. **Total allocated file data: 7 MiB.**
>
> These totals count the two files’ data and exclude metadata, as specified.

### Without the skill

> The append goes to the original, unlinked file because the writer’s descriptor still refers to that inode. The new `/var/log/jobs.log` is a separate file and remains 7 MiB.
>
> - **18:23, writer closes:** The original file still has a linkless open descriptor held by the monitor, so its 28 MiB remains allocated. The new file has 7 MiB allocated.
> - **18:25, monitor closes:** The original file has no links or open descriptors, so it is deleted and its 28 MiB is freed. The new file’s 7 MiB remains allocated.
