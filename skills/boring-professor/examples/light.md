# Tracking two Linux log files behind the same pathname

[한국어](light.ko.md) · [standard](standard.md) · [strict](strict.md)

[Question and sources](standard.md#question)

### Light

> The writer’s descriptor still refers to the original, unlinked file. Creating a new file at the same pathname does not change what existing descriptors refer to. Therefore, the 4 MiB append goes to the original file.
>
> - **18:23, writer closes:** Original file: 24 MiB + 4 MiB = **28 MiB**. New file: **7 MiB**. Total allocated file data: **35 MiB**.
> - **18:25, monitor closes:** The original file has no open descriptors or hard links, so its data is released. New file: **7 MiB**. Total allocated file data: **7 MiB**.
