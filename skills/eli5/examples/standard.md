# Which model coat loses warmth faster, and what does that tell a child about pup 696?

[한국어](standard.ko.md)

2026-11-09 · `eli5` 0.1.18 · English · `gpt-6-luna`

### Case and sources

- [Monterey Bay Aquarium, Life of a rescued sea otter](https://www.montereybayaquarium.org/about-us/stories/life-of-a-rescued-sea-otter). Pup 696's rescue and grooming sections describe the role of air in the fur in warmth and buoyancy.
- [Monterey Bay Aquarium, Sea otter](https://www.montereybayaquarium.org/animals-the-ocean/animals-a-to-z/sea-otter). Species account, Adaptations and Grooming: unlike many marine mammals, a sea otter relies on fur in cold water and lacks a thick layer of blubber.

### Prompt

> At Monterey Bay Aquarium, a five-year-old asks why caregivers groomed rescued sea otter pup 696. In a classroom demonstration invented for this question, two equally warm jars have identical model coats in the same cold bath. With air trapped in the fluffy coat, one jar cools 4 degrees in 20 minutes. With the coat wet and flat, the other cools 3 degrees in 10 minutes. A child says the fluffy jar lost warmth faster because four is more than three. Neither jar was tested for floating. Real sea otters lack thick blubber; grooming traps air in their fur, which helps them stay warm and float. Answer the child in at most five short sentences: use a fair comparison, explain whether air makes heat, and say what the jars can and cannot show about floating. Write the answer in English.

### Without the skill

> That comparison isn’t fair yet: the jars were measured for different lengths of time. Air doesn’t make heat; trapped air slows heat loss, so compare both coats over the same time. These jars can show how coats affect cooling, but they can’t tell us which coat floats better because floating wasn’t tested. Sea otters groom to trap air in their fur, which helps them stay warm and float.

### With the skill at standard

> The caregivers groomed pup 696 to help keep him warm.\
> The air trapped in his fluffy fur slows heat from escaping; it doesn’t make heat.\
> The flat wet coat cooled faster: on average, it lost 6 degrees in 20 minutes, while the fluffy coat lost 4.\
> The jars didn’t test floating.\
> In real sea otters, air trapped in their fur helps them float.

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Uses an equal-time comparison to explain the apparent reversal (2 degrees versus 3 per 10 minutes, or equivalent rates) and identifies the fluffy coat as slower to cool on average. | Missed | Met |
| Connects grooming to trapped air keeping warmth from leaving as fast, without claiming that air creates heat or substituting an invented biological mechanism. | Met | Met |
| In at most five short child-facing sentences, separates the jars’ untested floating behavior from the fact that trapped air also helps real otters float. | Met | Met |

**Review.** The answer compares average losses of 6 and 4 degrees per 20 minutes (3 and 2 per 10). This rescales the wet jar’s 10-minute measurement. It tells the child why grooming matters, why air slows heat loss and why the jar test cannot establish buoyancy.

Masked reviewer assignment: X was the revised answer. The table retains the original control grades. [Previous pair and scores](https://github.com/hobin01/writing-styles-from-giants/blob/20f24c66c7e89e6ce1007249c83c33932998bf01/skills/eli5/examples/standard.md) · [All attempts and adjudications](https://github.com/hobin01/writing-styles-from-giants/blob/main/evals/runs/2026-11-09-standard/records/eli5.json).

<details>
<summary>Run record</summary>

Baseline generated 2026-11-08. Revised treatment generated independently on 2026-11-09 with Codex CLI 0.167.0, low reasoning, in a fresh read-only session. SHA-256 prefixes (entrypoint / original baseline / revised answer): `fdd792c71803` / `b13daecf86ad` / `66f424b317e0`.

</details>
