# Standard example repairs · 9 November 2026

Thirteen of the 22 methods had missed at least one published standard check in English or Korean. In the [previous English gallery](https://github.com/hobin01/writing-styles-from-giants/blob/20f24c66c7e89e6ce1007249c83c33932998bf01/EXAMPLES.md) and [previous Korean gallery](https://github.com/hobin01/writing-styles-from-giants/blob/20f24c66c7e89e6ce1007249c83c33932998bf01/EXAMPLES.ko.md), 23 of the 132 standard checks were missed. This run kept both public prompts, all six checks per method, and both original controls. It reran both languages after each change to a method, including the language that had previously passed. Nine unchanged methods retain their original assessments.

## What was run

- Writer and masked reviewer both used GPT-6 Luna on Codex CLI 0.167.0 with low reasoning effort. The backend did not report a model build identifier. Each accepted answer came from a fresh read-only session in a unique directory outside the checkout. The [existing runner](../../../scripts/run_writing_pair.py) rejected tool activity, incomplete sessions and inconsistent final messages. Neither answers nor rubrics were supplied to the writer.
- The standard treatment received exactly the request plus the portable SKILL.md, method.json and locale JSON files. It did not receive cases.json, other answers, reviewer feedback or the gallery. Each language was generated directly. The original controls and their published scores are unchanged.
- Two superseded arms (the speaker script 0.1.6 in Korean and Minto 0.2.5 in English) repeatedly invoked web search and were rejected. Their records contain the failures, not scored answers. The final versions have valid answers in both languages.
- Each revised method also received a third question in another setting, with three checks fixed before any new generation. These 13 transfer questions have independently generated Luna controls. After a transfer failure, that question became part of the development loop; it is useful evidence about that example and does not estimate unseen-task performance.
- A separate Luna session graded each pair as X/Y in random order. The records keep both the initial masked verdict and the final adjudication. Some answers contain a method label, so full masking cannot be guaranteed. The final adjudication checked the actual words, numbers and actions; it could reverse a preliminary pass or fail. HTML decisions also used Chrome 156.0.8078.80: a script-disabled default and the ArrowRight, Home and End states of the labeled control. The records include the observed values and any contradictory prose.
- Earlier valid answers remain in the records, including failed intermediate revisions. Infrastructure retries did not substitute a different task or model. An incomplete writer session or an input-snapshot error yielded no accepted text; an invalid grader response was retried against the same answers. The published result is the first valid answer for that task on the final revision, not the best of several samples on that revision.

## Results

268 revised standard answers and 13 new transfer controls were generated. All 78 fixed gallery checks for the revised methods and all 39 transfer checks passed on their final versions. The other 54 gallery checks passed in the original assessments. Each final profile contributed one answer per question. Multiple versions were developed against these same checks; the scores describe the recorded outputs and are not an independent estimate of reliability. The experiment does not establish a pass rate on future requests.

| Method and raw record | Procedure revised | Final version (revisions tested) | Previously missed gallery checks | Final English / Korean / transfer |
| --- | --- | ---: | ---: | --- |
| [answer-with-html](records/answer-with-html.json) | Generate values and explanations from the same model. Render a useful script-free initial state. | 0.1.8 (5) | 2 | 3/3 · 3/3 · 3/3 |
| [asd-ste100](records/asd-ste100.json) | Keep prescribed component names throughout the procedure, including warnings. | 0.1.4 (1) | 1 | 3/3 · 3/3 · 3/3 |
| [eli5](records/eli5.json) | Separate a demonstration’s findings from known facts about the real subject. Compare rates on a common basis in short spoken sentences. | 0.1.18 (16) | 2 | 3/3 · 3/3 · 3/3 |
| [federal-plain-language](records/federal-plain-language.json) | Keep each eligible option with its owner and form. Check that the selected combination fits the original limit before recommending it. | 0.1.22 (20) | 3 | 3/3 · 3/3 · 3/3 |
| [feynman-technique](records/feynman-technique.json) | Trace each independent instance to its own boundary, and recompute the affected instance in a counterfactual. | 0.1.8 (5) | 3 | 3/3 · 3/3 · 3/3 |
| [ietf-rfc](records/ietf-rfc.json) | Bind each normative clause to the source actor and force, including in translated prose. Distinguish retry advice from a guarantee. | 0.1.10 (7) | 1 | 3/3 · 3/3 · 3/3 |
| [korean-plain-language](records/korean-plain-language.json) | Keep the scope of 만 and 모두 accurate in both the memo and the standalone replacement. Preserve each group’s amount and exemption. | 0.1.9 (7) | 1 | 3/3 · 3/3 · 3/3 |
| [microsoft-writing-style](records/microsoft-writing-style.json) | Cross each item’s starting state with its intended outcome, then use the documented control before the bulk action. | 0.1.11 (9) | 4 | 3/3 · 3/3 · 3/3 |
| [minto-pyramid](records/minto-pyramid.json) | Check forecast arithmetic and attach external estimates to the conditions and local comparison that would support them. | 0.2.6 (4) | 1 | 3/3 · 3/3 · 3/3 |
| [new-harts-rules](records/new-harts-rules.json) | Carry the counted unit into the final copy, normalize house forms across editable spans, and keep protected titles intact. | 0.1.6 (4) | 1 | 3/3 · 3/3 · 3/3 |
| [nist-technical-publication](records/nist-technical-publication.json) | Declare a common numerical scale and keep units consistent across inputs, equations and summary values. | 0.1.4 (1) | 1 | 3/3 · 3/3 · 3/3 |
| [socratic-self-questioning](records/socratic-self-questioning.json) | Reconstruct comparison values, name the original population and specify the assumption needed to transfer its result. | 0.1.6 (4) | 1 | 3/3 · 3/3 · 3/3 |
| [steve-jobs-presentation](records/steve-jobs-presentation.json) | Separate the measured parts of a demonstration and close with the decision the existing evidence can inform. | 0.1.8 (7) | 2 | 3/3 · 3/3 · 3/3 |

## Reading a record

Each file contains the fixed prompts and checks in their original language, the new transfer control, every accepted treatment answer and its raw SHA-256 digest. `masked_review` preserves the reviewer's original X/Y scores, notes and the condition key. `adjudicated_standard` is the final verdict in rubric order. A note explains review corrections. The table in each gallery keeps the control scores assigned in the original evaluation; rescoring a fixed control does not replace those scores.

To reconstruct a method input, concatenate the tagged SKILL.md, method.json and locale files exactly as in the [pair runner](../../../scripts/run_writing_pair.py). For patching only, append one newline to the concatenated final profile. Apply the patch and remove that terminal newline again before hashing. Use the final profile as the base for any `input_patch_from_final`, and compare its SHA-256 with `method_input_sha256`. Older official gallery pages remain available at their original commit, including earlier ELI5 wording and HTML retests.

For a fresh pair, pass a record’s `cases.en.prompt`, `cases.ko.prompt` or `cases.transfer.prompt` to the runner on stdin. CI verifies the archive and gallery without calling a model.
