# Tracking two Linux log files behind the same pathname

[한국어](standard.ko.md)

2026-11-08 · `boring-professor` 0.1.2 · English · `gpt-6-luna`

### Case and sources

- [Linux man-pages 6.19, unlink(2)](https://man7.org/linux/man-pages/man2/unlink.2.html). DESCRIPTION defines the effect of unlinking the last directory link with and without an open descriptor. The filenames, monitor, allocation sizes and event times are illustrative.

### Prompt

> Explain this Linux drill to a systems student. At 09:00 an administrator unlinks the last hard link to /var/log/payments.log. The old file has 20 MiB of allocated data; the writer and a monitor each hold an open descriptor to it. At 09:02 the service creates a separate file at the same pathname, with 5 MiB allocated. At 09:03 the original writer appends 8 MiB through its old descriptor, then closes it at 09:04. The monitor closes its old descriptor at 09:06. Trace which file gets the append, the total allocated data across both files just after 09:04 and just after 09:06, and why the pathname alone is insufficient evidence. Assume no sparse allocation, duplication or other changes; ignore metadata. Keep the explanation literal and concise. Write your answer in English.

### Without the skill

> At 09:00, unlinking the last hard link removes the old file’s name, but the open descriptors keep that file alive. At 09:02, the service creates a new, separate file at `/var/log/payments.log`.
>
> The writer’s append at 09:03 goes to the **old file**, because its descriptor still refers to that file. The old file then has 20 + 8 = **28 MiB** allocated; the new file has **5 MiB**. Total just after 09:04: **33 MiB**.
>
> Closing the writer’s descriptor does not free the old file because the monitor still has it open. When the monitor closes its descriptor at 09:06, the old file is released. The new file remains at **5 MiB**. Total just after 09:06: **5 MiB**.
>
> The pathname alone is insufficient evidence because it names the new file after 09:02. An open descriptor can still refer to the old, unlinked file.

### With the skill at standard

> `unlink` removes a directory entry. An open file descriptor continues to refer to its file even after that file has no pathname.
>
> The 09:00 unlink removes the last hard link to the original file, but the writer’s and monitor’s descriptors keep it accessible. At 09:02, creating `/var/log/payments.log` creates a separate file; the pathname now refers to that file.
>
> The 09:03 append goes to the original file because the writer uses its old descriptor. Its allocated data becomes 20 + 8 = **28 MiB**. The new file remains **5 MiB**, so the total just after the writer closes at 09:04 is **33 MiB**.
>
> At 09:06, the monitor closes the last open descriptor to the original file. The original file is then released, leaving the new file’s **5 MiB** allocated. The total just after 09:06 is **5 MiB**.
>
> The pathname alone is insufficient evidence because, after 09:02, it identifies the new file, while the writer’s descriptor still identifies the unlinked original. These totals assume no sparse allocation, duplication, other changes, or metadata.

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Identifies the append as going to the old, unlinked file through the writer's descriptor, not to the 5 MiB replacement at the reused pathname. | Met | Met |
| Gives 33 MiB just after 09:04 (28 old + 5 new) and 5 MiB just after 09:06; the monitor's descriptor delays release of the old file. | Met | Met |
| Explains the pathname/file-object distinction and the final-descriptor condition using literal technical terms, without implying that unlink disables existing writes. | Met | Met |

**Masked review** (Y = baseline; X = standard). Both identify the old object as the append target, compute 33 MiB at 09:04 and 5 MiB at 09:06, and connect delayed reclamation to the monitor’s descriptor. X defines a directory entry before tracing the events and restates the assumptions; Y gives a shorter event trace. No substantive difference on these checks.

<details>
<summary>Run record</summary>

Each arm was a separate ephemeral read-only Codex CLI 0.167.0 session with low reasoning effort. Neither session was given the other answer or an answer in the other language.

SHA-256 prefixes (entrypoint / baseline answer / standard answer): `7920576bbe50` / `ae415a4a0b15` / `89fd5a38430b`.

</details>
