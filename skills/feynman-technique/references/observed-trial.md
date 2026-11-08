# Feynman strict · predicting what a counter remembers

Recorded on 2026-11-08 with one fresh Codex agent per answer. The baseline received the task. Each treatment agent also received this skill at `strict` level. These are the returned texts, including paragraph breaks.

## Request

Explain this counter to a new operator in a short paragraph. Give a finished explanation without asking the reader questions. A valid scan increases the stored count by one unless that same tag was already scanned in the current batch. Starting a new batch clears the stored count and the list of seen tags. A rejected scan changes neither. The notes do not specify how a scan is classified as valid.

## Checks set before the runs

Explain the seen-tag list and reset. Show how the same tag behaves within and across batches, that rejection leaves both states unchanged, and that validity criteria are unknown. Give a finished prediction without quizzing the operator.

## Without this skill

Starting a new batch resets the count to zero and clears the list of seen tags. A valid scan adds one to the count and records the tag on the list. If the tag is already on the list, the count stays the same. A rejected scan leaves both the count and the list unchanged. The notes do not specify what makes a scan valid.

## With the first draft

Starting a new batch resets the count to zero and clears the list of tags already seen. The first valid scan of tag A adds one to the count and puts A on the list, so scanning A again in the same batch adds nothing. A rejected scan changes neither the count nor the list. If the first scan of tag B is rejected, a later valid scan of B still adds one. The notes do not say how the scanner decides whether a scan is valid.

The strict step originally asked for any new application. We clarified how to choose a revealing one for mechanisms with memory: hold the input fixed and cross a stated change of state. A fresh agent received the same request and the revised skill.

## After revising the strict step

The counter remembers which tags it has counted in the current batch. A valid scan adds one if the tag is new to that batch. For example, if tag A is the first tag you scan and the scan is valid, the count goes to one. Scan A again and the count stays at one. Starting a new batch resets the count to zero and clears the tag list, so a valid scan of A now brings the count to one again. A rejected scan leaves both the count and the list unchanged. The notes do not say how the counter decides whether a scan is valid.

## After making the teaching example explicit

Review of the separate cache illustration found it still left the reader to infer the hit and miss. We wrote out both outcomes, then repeated the held-out counter request in one more fresh context.

The counter adds one the first time you make a valid scan of a tag in each batch. For example, if tag A is the first valid scan, the count goes from zero to one. A second valid scan of A leaves the count at one because A is already on the list of seen tags. Starting a new batch resets the count to zero and clears the list, so scanning A again raises the count to one if the scan is valid. A rejected scan leaves both the count and the list unchanged. The notes do not say how the counter decides whether a scan is valid.

## Review

The baseline describes all four rules, but leaves the reader to work out the repeated tag. The first skill answer predicts a rejected scan followed by a valid one and a duplicate in one batch. It mentions the reset without tracing the same tag across it, so it misses one of the checks. Both revised answers trace A through both batches and keep the rejected-scan rule and the unknown classification criterion. The extra sentences serve the requested prediction. No learner took a test.
