# Which model coat loses warmth faster, and what does that tell a child about pup 696?

[한국어](standard.ko.md)

2026-11-08 · `eli5` 0.1.2 · English · `gpt-6-luna`

### Case and sources

- [Monterey Bay Aquarium, Life of a rescued sea otter](https://www.montereybayaquarium.org/about-us/stories/life-of-a-rescued-sea-otter). Pup 696's rescue and grooming sections describe the role of air in the fur in warmth and buoyancy.
- [Monterey Bay Aquarium, Sea otter](https://www.montereybayaquarium.org/animals-the-ocean/animals-a-to-z/sea-otter). Species account, Adaptations and Grooming: unlike many marine mammals, a sea otter relies on fur in cold water and lacks a thick layer of blubber.

### Prompt

> At Monterey Bay Aquarium, a five-year-old asks why caregivers groomed rescued sea otter pup 696. In a classroom demonstration invented for this question, two equally warm jars have identical model coats in the same cold bath. With air trapped in the fluffy coat, one jar cools 4 degrees in 20 minutes. With the coat wet and flat, the other cools 3 degrees in 10 minutes. A child says the fluffy jar lost warmth faster because four is more than three. Neither jar was tested for floating. Real sea otters lack thick blubber; grooming traps air in their fur, which helps them stay warm and float. Answer the child in at most five short sentences: use a fair comparison, explain whether air makes heat, and say what the jars can and cannot show about floating. Write the answer in English.

### Without the skill

> That comparison isn’t fair yet: the jars were measured for different lengths of time. Air doesn’t make heat; trapped air slows heat loss, so compare both coats over the same time. These jars can show how coats affect cooling, but they can’t tell us which coat floats better because floating wasn’t tested. Sea otters groom to trap air in their fur, which helps them stay warm and float.

### With the skill at standard

> When you fluff a blanket, it traps air in its little spaces. The air does not make heat; it slows heat from leaving, so let’s compare the jars over the same 10 minutes: the fluffy jar lost 2 degrees, and the wet, flat one lost 3. So the fluffy jar cooled more slowly. These jars show how coat air can help keep an otter warm, but they were not tested for floating, so they cannot show that. Real sea otters groom their fur to trap air, which helps them stay warm and float.

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Uses an equal-time comparison to explain the apparent reversal (2 degrees versus 3 per 10 minutes, or equivalent rates) and identifies the fluffy coat as slower to cool on average. | Missed | Met |
| Connects grooming to trapped air keeping warmth from leaving as fast, without claiming that air creates heat or substituting an invented biological mechanism. | Met | Met |
| In at most five short child-facing sentences, separates the jars’ untested floating behavior from the fact that trapped air also helps real otters float. | Met | Missed |

**Masked review** (Y = baseline; X = standard). X computes 2 versus 3 degrees per ten minutes; Y notices the unequal observation times but leaves the normalized comparison for the child to calculate. Both explain that air slows heat loss, that the jars were not tested for floating, and that trapped air helps actual otters float. X fits five sentences but packs the calculation, a semicolon and a colon into one long sentence for a five-year-old; Y fits the shorter, child-facing format better. The 2 degrees per ten minutes is a normalized average. The demonstration did not measure the fluffy jar's drop in its first ten minutes.

<details>
<summary>Earlier wording and both returned answers</summary>

The initial prompt compared total heat loss in unequal intervals. We clarified that the child was comparing cooling rates and reran both English arms. Only the final pair is scored above.

**Earlier prompt**

> At Monterey Bay Aquarium, a five-year-old asks why caregivers groomed rescued sea otter pup 696. In a classroom demonstration invented for this question, two equally warm jars have identical model coats in the same cold bath. With air trapped in the fluffy coat, one jar cools 4 degrees in 20 minutes. With the coat wet and flat, the other cools 3 degrees in 10 minutes. A child says the fluffy jar lost more warmth because four is more than three. Neither jar was tested for floating. Real sea otters lack thick blubber; grooming traps air in their fur, which helps them stay warm and float. Answer the child in at most five short sentences: use a fair comparison, explain whether air makes heat, and say what the jars can and cannot show about floating. Write the answer in English.

**Earlier baseline**

> You’re right that 4 is more than 3, but the jars were checked for different lengths of time, so that isn’t a fair comparison. Air doesn’t make heat; trapped air slows heat from escaping, like a blanket. The jars suggest that fluffy fur can help keep warmth in. They weren’t tested for floating, so they can’t show whether the fur helps otters float.

**Earlier standard answer**

> Sea otters groom their fur to keep it fluffy, with tiny pockets of air inside. The jars cooled at different speeds: the fluffy jar lost 2 degrees in 10 minutes, while the wet jar lost 3 degrees in 10 minutes, so the wet one cooled faster. The air does not make heat; it helps the otter keep its body heat. The jars show how the coats slow cooling, but they cannot show whether air helps an otter float because neither jar was tested for floating.

</details>

<details>
<summary>Run record</summary>

Each arm was a separate ephemeral read-only Codex CLI 0.167.0 session with low reasoning effort. Neither session was given the other answer or an answer in the other language.

SHA-256 prefixes (entrypoint / baseline answer / standard answer): `10536a49c052` / `b13daecf86ad` / `a8ba35d193a1`.

</details>
