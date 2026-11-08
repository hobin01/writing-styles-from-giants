# Worked examples and paired writing trials

On 2026-11-08 we added a worked example to each of the 22 portable skills. Four skills also have a comparison on a new task. Each link below contains the exact task, checks, full answers and editorial judgment. The examples in other entrypoints are teaching material written by the project.

| Method and level | What happened on this task |
| --- | --- |
| [ASD normal, English](../../skills/asd-ste100/references/observed-trial.md) | Both answers preserved the two-lamp condition, the prohibition and the unknown moisture source. The skill gave the glossary definition a separate sentence. |
| [Minto standard, English](../../skills/minto-pyramid/references/observed-trial.md) | Both answers supported the same decision. The baseline led with the recommendation. The skill framed the decision with the trial evidence and a question before answering. |
| [Feynman strict, English](../../skills/feynman-technique/references/observed-trial.md) | The first treatment gave a worked duplicate scan but left the effect of a reset on the same tag implicit. After revision, both fresh treatments traced that tag within one batch and across the reset. |
| [Korean plain language standard, Korean](../../skills/korean-plain-language/references/observed-trial.md) | Both edits preserved 해요체, the preview condition and the separate save action. The skill used 만 to mark the necessary condition and quoted the UI labels. |

## How to read the results

Each answer came from a newly started Codex desktop subagent with no parent conversation or shared agent history. Each agent was restricted by instruction to its own temporary directory. Both arms used identical task text and the same launch instruction below, apart from the directory path. The baseline directory contained only `TASK.md`. The treatment also contained the portable method directory and `PROFILE.md` specifying the level. We used manual loading and random directory names. The agents shared the underlying host, not the same working files. No agent was given the opposing answer, judging criteria or these trial records. The comparison used the session's default model with no model override; the per-run model build, sampling parameters, and desktop build were not exposed by the subagent interface.

> Answer the task in {directory}. This is a standalone writing request. Inspect only this directory, starting with TASK.md. If it contains a method/ directory, read its SKILL.md, method.json and locale instructions, and apply the level in PROFILE.md. Otherwise answer directly. Do not use any other skills, files, web or previous tasks. Return only the requested writing in your final response, without test commentary.

We fixed the substantive checks before receiving answers. The project authoring agent reviewed the final texts against the source, those checks and the requested format, with the conditions visible to the judge. Each method had one baseline and one initial treatment. Feynman also had two fresh treatments on the same task, one after clarifying the strict instruction and one after making the cache teaching example explicit. The unchanged baseline is shared across these revisions. This is a small set of examples for inspection. It does not estimate an average effect, measure comprehension or test automatic skill discovery.

<details>
<summary>Tested entrypoint versions and fingerprints</summary>

The SHA-256 fingerprints identify the exact `SKILL.md` bytes supplied before the optional trial-record links were appended. Each method directory also contained its version-matched locale, cases and references.

| Method | Method version | SHA-256 of SKILL.md |
| --- | --- | --- |
| ASD | 0.1.2 | `ed07d1434cdeffa44a47c54b51adac81feae0ec11888b23213185dfefc773d81` |
| Minto | 0.2.1 | `c8b9914b3b094d8f8c1df464849daf0790926d443704d73a836d35781d62771f` |
| Korean | 0.1.1 | `8aaa52f09621534634024952b9388f5c3f1bcd4974eb95231d707d6eaee30e4b` |
| Feynman, first draft | 0.1.1 development | `8c042e686baf94a4366c058a73e7ff5295a331053e6b74f9562a077c9dcb34f8` |
| Feynman, revised step | 0.1.1 development | `ebc144a85df1ebd12c7a171e7507e8d2f14f1258c24f1f9d2288c752b06df4df` |
| Feynman, revised example | 0.1.1 | `b8a9373ff0ab74c7201ccdf6cc86c2c8fb2759d3d6467ddaf372a75c46c40863` |

</details>

<details>
<summary>Excluded setup runs</summary>

We initially ran the ASD and Minto tasks using directory paths that named the method and condition. Because a baseline could infer the target style from that path, we repeated both pairs with fresh agents and opaque directory names. We excluded all four earlier answers from the comparison, regardless of their content. Their returned texts follow for inspection.

**ASD, earlier baseline**

> Only a technician may remove the access panel, and only while both lamps are dark. Do not remove the fixed panel.
>
> A sensor detected moisture near the access panel. The source of the moisture is unknown.

**ASD, earlier treatment**

> The access panel is the detachable cover. A technician may remove the access panel only while both lamps are dark. Do not remove the fixed panel.
>
> A sensor detected moisture near the access panel. The source of the moisture is unknown.

**Minto, earlier baseline**

> The lab should keep Reader B and defer a decision on Reader A. Reader B passed all 20 trial runs, while Reader A failed on 3 of 20. The team can fund one replacement, and its reliability has not been tested. If the bench is free next week, the lab can repeat the trial to see whether Reader A’s failures recur.

**Minto, earlier treatment**

> Reader A failed on 3 of 20 trial runs, and Reader B passed all 20. With funding for only one replacement, the lab should keep Reader B and defer the decision on Reader A. Replacement reliability has not been tested. If the bench is free next week, the lab may repeat the trial to see whether A’s failures recur.

</details>

## Other review

The [HTML example](../../skills/answer-with-html/examples/annual-growth.html) is a runnable illustration written for the skill. We rendered the file contents in Chromium 156.0.8078.80. The initial two years showed $121.00. The left arrow selected one year and showed $110.00. Home and End selected zero and four years and showed $100.00 and $146.41. At 320 CSS pixels the page had no horizontal overflow. With JavaScript disabled, its two-year answer remained readable and the inactive control was disabled.

The per-skill Ponytail pass kept the exercise that demonstrates the method's decision and removed repeated instructions where possible. A separate review checked all 22 examples against the underlying cases. It caught a necessary condition in the Federal notice, ambiguous administrator scope in a Microsoft command example, and a percentile expectation that treated “did not improve” as “stayed the same.” The final examples preserve those distinctions.
