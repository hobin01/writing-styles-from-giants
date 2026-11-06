# Localization and language adaptation

English and Korean are the first target languages. English contributor documentation is canonical; keep the Korean README aligned. This choice does not make English writing rules authoritative for other languages.

## README parity

Keep README.md and README.ko.md aligned in heading hierarchy and section order, table rows, link destinations, commands, candidate status, and limitations. Translate meaning rather than English sentence order. Add material clarifications to both versions in the same change. A structural check cannot establish translation accuracy; compare the prose as well.

Only the README currently has a full Korean counterpart. Contributor/design documents remain canonical English. Locale rule files intentionally differ when a language needs an adaptation; their stable rule IDs and declared coverage must still agree.

## Separate the language layers

- Method intent and stable rule IDs are language-independent where possible.
- Instruction language is the language used to explain the skill to the agent.
- Output language is the language requested for the finished text.
- Linguistic rules and evaluation belong to the output locale. Translating instructions alone does not validate a locale.

Use BCP 47 locale identifiers. An exact reviewed variant is preferred. A parent-language fallback is allowed only when the method declares it suitable; disclose it. If no adequate variant exists, report the limitation or use recommendation-only mode. Never silently use English word limits for Korean output.

## Measurement

English words, Korean eojeol, characters, syllables, and model tokens measure different things. Do not adopt an English-10/Korean-5 conversion. An eojeol count does not measure syntax or comprehension by itself.

A numeric rule must specify unit, segmentation, normalization, punctuation/code/quotation treatment, scope, threshold, rationale, and evidence status. Mark uncalibrated thresholds experimental. Mixed-language text requires an explicit measurement policy, not a guessed language ratio. Preserve technical names, units, and code.

## Language review

Add an original-language rule explanation, a faithful example and counterexample, an exception, and a meaning-preservation case. Korean review includes particles/endings, subject omission, passive/causative nuance, honorifics/register, and translated terminology where relevant. English review includes articles, modality, grammatical voice, and reader knowledge where relevant. These are review prompts, not universal prohibitions.

Keep common rule IDs and mark intentionally inapplicable rules. A locale-only rule gets its own ID and rationale. Changing register, such as 해요체 to 합니다체, requires a user/genre choice rather than automatic normalization.

Report evaluation separately by locale, genre, and level. Track semantic changes, false positives, justified exceptions, reader understanding, and reviewer disagreement. A native-language reviewer checks adaptations before `reviewed` status. Adding more languages must not mean translating every English threshold.

## Relevant sources

- [BCP 47 language tags](https://www.rfc-editor.org/rfc/bcp/bcp47.txt)
- [국립국어원 쉬운 공문서 쓰기 길잡이](https://korean.go.kr/front/etcData/etcDataView.do?etc_seq=700&mn_id=208&pageIndex=1): consult its item-specific reuse notice before copying.
- [CDC CCI usage](https://www.cdc.gov/ccindex/tool/how-to-use.html): reader-oriented assessment is distinct from a readability formula.
