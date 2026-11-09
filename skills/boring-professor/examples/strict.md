# Tracking two Linux log files behind the same pathname

[한국어](strict.ko.md) · [light](light.md) · [standard](standard.md)

[Question and sources](standard.md#question)

### Strict

> A hard link is a directory entry that refers to a file’s inode. Removing the last hard link removes the pathname reference, but an open file descriptor can keep the original file’s inode and data available. Creating a new file at the same pathname creates a different file. An open descriptor continues to refer to the file it originally opened.
>
> Assume the writer and monitor descriptors refer to the original 24 MiB file. The new file at `/var/log/jobs.log` is a separate file with 7 MiB allocated. The writer’s append changes the original file by +4 MiB, making its allocated data 28 MiB.
>
> - **Immediately after the writer closes at 18:23:** original file: 28 MiB, still held open by the monitor; new file: 7 MiB. **Total: 28 MiB + 7 MiB = 35 MiB.**
> - **Immediately after the monitor closes at 18:25:** original file: 0 MiB, because it has no remaining hard links or open descriptors; new file: 7 MiB. **Total: 0 MiB + 7 MiB = 7 MiB.**
>
> The append is in the **original file**, which no longer has a pathname after 18:20. The total counts file data that remains allocated; it excludes metadata as specified.
