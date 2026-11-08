# Which model coat loses warmth faster, and what does that tell a child about pup 696?

2026-11-08 · `eli5` 0.1.1 at first pass · `gpt-6-luna` · Codex CLI 0.167.0

### Case and sources

- [Monterey Bay Aquarium, Life of a rescued sea otter](https://www.montereybayaquarium.org/about-us/stories/life-of-a-rescued-sea-otter). Pup 696's rescue and grooming sections describe the role of air in the fur in warmth and buoyancy.
- [Monterey Bay Aquarium, Sea otter](https://www.montereybayaquarium.org/animals-the-ocean/animals-a-to-z/sea-otter). Species account, Adaptations and Grooming: unlike many marine mammals, a sea otter relies on fur in cold water and lacks a thick layer of blubber.

**Reasoning task.** Normalize temperature changes by unequal exposure times and distinguish experimental evidence for insulation from the separate biological buoyancy claim, in language a child can follow.

### Prompt

> At Monterey Bay Aquarium, a five-year-old asks why caregivers groomed rescued sea otter pup 696. In a classroom demonstration invented for this question, two equally warm jars have identical model coats in the same cold bath. With air trapped in the fluffy coat, one jar cools 4 degrees in 20 minutes. With the coat wet and flat, the other cools 3 degrees in 10 minutes. A child says the fluffy jar lost more warmth because four is more than three. Neither jar was tested for floating. Real sea otters lack thick blubber; grooming traps air in their fur, which helps them stay warm and float. Answer the child in at most five short sentences: use a fair comparison, explain whether air makes heat, and say what the jars can and cannot show about floating.

### Without a skill

> The jars were in the same cold bath, but they were watched for different amounts of time, so we can’t fairly compare 4 degrees with 3 degrees. The fluffy coat cooled 4 degrees in 20 minutes; the wet, flat coat cooled 3 degrees in 10 minutes. Trapped air doesn’t make heat; it slows heat from escaping. The jars can show how coats may help keep warmth in, but they weren’t tested for floating. In real sea otters, grooming traps air in their fur, helping them stay warm and float.

### With the skill at standard

> These jars have not had a fair test: one cooled for 20 minutes, and the other for 10. Air does not make heat; when it is trapped in fluffy fur, it slows heat from escaping. The jars can show how coats may help keep warmth, but they do not show whether a coat helps an otter float because neither jar was tested for floating. Sea otters have little blubber, so grooming helps keep their fur fluffy and full of air.

### First-pass assessment

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Uses an equal-time comparison to explain the apparent reversal (2 degrees versus 3 per 10 minutes, or equivalent rates) and identifies the fluffy coat as slower to cool on average. | Missed | Missed |
| Connects grooming to trapped air keeping warmth from leaving as fast, without claiming that air creates heat or substituting an invented biological mechanism. | Met | Met |
| In at most five short child-facing sentences, separates the jars’ untested floating behavior from the fact that trapped air also helps real otters float. | Met | Missed |

Both notice the unequal times and explain that trapped air slows heat loss, but neither compares the rates: the fluffy coat lost 2 degrees per 10 minutes on average, the flat coat 3. The baseline distinguishes the jars’ untested buoyancy from real grooming that helps an otter float. The skill answer states the jars were not tested for floating but leaves out the known benefit to the animal. The baseline’s first sentence would still be long to read to a five-year-old.

**차이.** 두 답 모두 시간 차이를 알아채고 공기가 열을 만들지 않는다고 설명하지만, 같은 10분당 평균 2도와 3도로 비교하지는 못했습니다. 미적용 답은 병의 실험과 실제 수달이 뜨는 데 도움이 되는 효과를 구분했습니다. 스킬 답은 부력을 시험하지 않았다고만 하고 실제 효과를 빠뜨렸습니다.

<details>
<summary>Developmental retest · version 0.1.2</summary>

Resolve unequal bases before simplifying; distinguish what an example measures from what it leaves untested. This retest is excluded from the first-pass counts.

The request and original baseline are unchanged.

**New standard answer**

> Imagine the two jars are boats in a cold bath: the fluffy coat jar cooled 4 degrees in 20 minutes, or 2 degrees in 10 minutes, while the wet, flat coat jar cooled 3 degrees in 10 minutes. So, over the same 10 minutes, the wet, flat coat jar lost more warmth. Air in a sea otter’s fur doesn’t make heat; it gets trapped and helps slow heat from leaving. The jars show how the coats slowed cooling in this classroom demonstration, but they weren’t tested for floating, so they can’t tell us which coat floats better. Sea otters groom their fur to trap air, which helps them stay warm and float.

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Uses an equal-time comparison to explain the apparent reversal (2 degrees versus 3 per 10 minutes, or equivalent rates) and identifies the fluffy coat as slower to cool on average. | Missed | Met |
| Connects grooming to trapped air keeping warmth from leaving as fast, without claiming that air creates heat or substituting an invented biological mechanism. | Met | Met |
| In at most five short child-facing sentences, separates the jars’ untested floating behavior from the fact that trapped air also helps real otters float. | Missed | Missed |

The skill answer compares the average drops over ten minutes, 2 degrees for fluffy fur and 3 for flat fur. The baseline notices the unequal observation times but never works out which coat cooled faster. Both explain that trapped air slows heat loss and distinguish what the jars showed from what helps an otter float. Both use five sentences, but their opening sentences run to 38 and 27 words, respectively, a poor fit for a five-year-old.

**차이.** 스킬 답은 10분당 평균 하락 폭이 보송한 털에서 2도, 납작한 털에서 3도라고 비교한다. 미적용 답은 관찰 시간이 다르다는 점만 짚고 어느 쪽이 더 빨리 식는지는 말하지 않는다. 둘 다 공기가 열 손실을 늦춘다는 점과, 병 실험에서 확인한 사실과 실제 수달의 부력을 구분한다. 각각 다섯 문장이지만 첫 문장이 스킬 답은 38단어, 미적용 답은 27단어로 다섯 살 아이에게 길다.

</details>
