# What Minneapolis’s I-35W collapse changes about a bridge review

2026-11-08 · `amazon-six-page-narrative` 0.1.1 · English · Codex CLI 0.167.0 / gpt-6.1-sol

### Case and sources

- [NTSB, investigation HWY07MH024, Collapse of I-35W Highway Bridge, Minneapolis, Minnesota](https://www.ntsb.gov/investigations/Pages/HWY07MH024.aspx). What Happened and What We Found: 1 August 2007 collapse, inadequate U10 gusset plate capacity, combined loads, and omission of gusset plates from load-rating analyses. The proposed review by another owner is an exercise.

### Prompt

> Write the opening of a decision memo for a hypothetical public bridge owner reviewing its steel truss bridges after Minneapolis's I-35W bridge collapsed in 2007. Should the owner fund a review of gusset plates in the load ratings or rely on its existing inspection records alone? According to the NTSB, undersized connecting plates at the U10 joints failed under combined loads: earlier modifications had made the bridge heavier, and traffic and concentrated construction loads were present on the day of collapse. Excluding gusset plates from load-rating analyses was a contributing practice. We have no calculations for the hypothetical owner's bridges in this exercise. State what the proposed review would establish; don't declare the owner's bridges safe or unsafe. At most 110 words.

### Without a skill

> The owner should fund a gusset-plate review as part of its steel truss bridge load ratings; existing inspection records alone cannot establish capacity under combined loads. According to the NTSB, undersized U10 connecting plates failed in the 2007 I-35W collapse under loads from earlier modifications, traffic, and concentrated construction activity. Excluding gusset plates from load-rating analyses contributed to the failure. The proposed review would establish whether plate capacities adequately support applicable load combinations, accounting for modifications and construction loading, and identify any needed restrictions, further analysis, or strengthening. Without bridge-specific calculations, this memo makes no finding that the owner’s bridges are safe or unsafe.

### With the skill at standard

> I recommend funding a review of gusset plates in our steel truss bridge load ratings rather than relying on inspection records alone. According to the NTSB, undersized connecting plates at I-35W’s U10 joints failed under combined loads: earlier modifications had increased bridge weight, and traffic and concentrated construction loads were present that day. Excluding gusset plates from load-rating analyses contributed to the collapse. The proposed review would establish whether our ratings account for gusset-plate capacity under applicable combined loads and identify any needed analysis or action. We have no calculations for our bridges in this exercise and cannot conclude whether they are safe or unsafe.

### What changed

**Checks set before the run.** Recommend a specific review and distinguish capacity calculations from records of visible condition. Retain the joint and combined loads identified by the NTSB, and keep the hypothetical owner's bridge capacities unresolved.

Both recommend reviewing gusset plates and leave the hypothetical owner's bridge capacities open. The baseline lists possible follow-up decisions, including restrictions or strengthening. The skill answer spells out why the old bridge carried more weight and makes reviewing the owner's load ratings the immediate decision. Neither treats the Minneapolis finding as a diagnosis of another bridge.

**차이.** 두 답 모두 교량 연결판의 하중 평가를 권하고, 다른 교량의 안전 여부는 판단할 수 없다고 밝힙니다. 스킬 답안은 과거 개조로 교량 자체의 무게가 늘었다는 점을 분명하게 짚습니다.
