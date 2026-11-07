# Initial skill catalog research

Research accessed on 2026-11-07 for the owner's 24 initial methods after John von Neumann was withdrawn. This is a pre-authoring assessment, not a released catalog. It distinguishes documented practices, project-original methods, and names whose intended scope needed clarification. Proposed operational steps below are adaptations unless explicitly identified as source summaries.

The original research is preserved below. The later [consolidation](CATALOG_CONSOLIDATION.md) retired standalone SCQA, CTE, and the factual Hemingway adaptation; the current catalog is in [README.md](../README.md). Historical scope decisions below are not active installation choices.

## Authoring decisions

Write skill instructions primarily in English. English instructions can support Korean output; instruction language does not determine output language. Create an additional Korean-specific skill only when a linguistic difference requires its own rules. Structural methods do not need a Korean duplicate merely because their examples are translated. The Korean notes below identify review issues, not a decision to create Korean variants for every method. English controlled vocabularies, word counts, articles, and grammatical-voice rules cannot establish Korean compliance.

Each completed skill must receive a Ponytail review: remove instructions that do not affect the requested behavior, duplicated guidance, speculative options, and unused resources. Keep necessary source attribution, exceptions, meaning-preservation rules, and observable evaluation cases. This document records the pre-authoring research; implementation evidence is in [CATALOG_REVIEW.md](CATALOG_REVIEW.md).

ASD's `normal` aliases `standard`; `strict` applies the full eligible project profile. An informal 80% preference cannot become a measured compliance score. See the implemented [ASD skill](../skills/asd-ste100/SKILL.md) for selected rules.

## Method findings

### ASD-STE100 Simplified Technical English

**Meaning and operational core.** A controlled English standard for technical documentation, maintained by the ASD Simplified Technical English Maintenance Group (STEMG). Its writing rules and controlled dictionary operate together; an ordinary plain-language prompt is insufficient for verified conformity. Use consistent terms, explicit actors, direct instructions, staged information, and unambiguous meanings. Respect procedural/descriptive distinctions and documented exceptions. The official FAQ permits adopting principles for other genres while distinguishing the standard's intended technical-documentation scope. [Official FAQ](https://www.asd-ste100.org/STE_faq.html).

**Evidence and read scope.** Read the complete public FAQ and downloads notice using direct HTTPS retrieval after the browser fetch returned 403. Current issue: Issue 9, January 2025. The [official Issue 9 PDF](https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf) was located and fetched temporarily, but its contents were not read in the research-only change. During implementation, selected writing/counting and copyright passages were read; see [the exact ASD evidence record](../skills/asd-ste100/method.json). The complete dictionary and every writing rule were not reviewed. This assessment does not independently verify every numbered writing rule or dictionary entry. [Official downloads](https://www.asd-ste100.org/STE_downloads.html).

**80% / 100%.** Neither is an established compliance measure in the official pages read. Treat them as the user's intended intensity labels until concrete project rules are selected. `strict` can mean the project's strongest supported checks, with a review record; it cannot promise 100% ASD conformity from a prompt. `normal` can adopt selected principles without inventing a mathematical denominator. All levels preserve meaning.

**Karpathy attribution and confirmed scope.** Read the complete [original public X post](https://x.com/karpathy/status/2105819303471976479), published 2026-10-02 at 00:37 UTC. Direct public HTML retrieval succeeded after earlier browser 403 responses and truncated syndication responses. Karpathy reports that requesting ASD-STE100 explanations makes LLM writing easier for him to read and sometimes softens the stringent specification by asking for “80% of the way to ASD-STE100.” This is personal prompting advice, not a defined rule subset, percentage formula, or conformance guarantee. The owner confirmed this is the intended inspiration for `normal`; the post's later diagram, HTML, and video suggestions are outside the ASD skill's scope.

The post's [attached infographic](https://pbs.twimg.com/media/HTlaHqgbwAAS1lv.png?name=orig) was visually inspected. Its substitution of *about* for approximate quantities conflicts with the official FAQ's restriction of *about* to the concerned-with sense. Do not adopt the image as an authoritative dictionary or bundle it.

**Rights and Korean.** The downloads notice reserves rights and disclaims tool endorsement; the current edition's copyright statement controls. No standard/dictionary redistribution is authorized by this review. Korean output needs a separately labeled STE-inspired adaptation: the English dictionary, parts of speech, word counting, and grammar cannot become Korean compliance rules through translation.

### ELI5, with the user's literal age-five target

**Meaning.** The conventional subreddit method addresses laypeople rather than actual five-year-olds. Its public rules assume typical secondary-school knowledge unless the requester specifies otherwise; explanations must clarify a mechanism rather than merely supply a short answer. Avoid unexplained terms and condescension. [r/explainlikeimfive rules on the community page](https://www.reddit.com/r/explainlikeimfive/).

**Proposed project adaptation.** The user explicitly intends a five-year-old reader. Record that as an adaptation, not the subreddit definition: establish familiar prerequisites; introduce one unfamiliar idea at a time; use concrete, observable examples; explain required terms; identify where a simplifying model stops being accurate. An analogy is optional, never evidence that two systems behave identically. Retain necessary uncertainty and conditions; do not claim developmental suitability without reader review.

**Evidence, rights, Korean.** Read the community page's rules, especially rules 3–5 and 8. The older wiki/rules page merely redirects to newer rules. These are community rules, not a licensed pedagogical standard; no reuse license was verified. Korean needs decisions about familiar vocabulary, sentence endings, and whether an adult reads the explanation aloud. Do not infer a Korean age-five reading level from English word counts or a readability score.

### George Orwell's six rules

**Meaning and core.** A documented method for clear, honest expression, particularly nonfiction and political language, rather than imitation of Orwell's identity. Faithful operational summaries: inspect stock imagery; prefer shorter equally accurate words; remove unnecessary words; prefer active voice when it works; replace needless specialized or foreign expressions with familiar equivalents; preserve the final permission to break the preceding rules when their application damages expression. The essay distinguishes fresh useful imagery from worn-out figures; it does not ban all metaphor.

**Evidence and read scope.** Read the essay, including the surrounding qualifications and all six rules: George Orwell, *Politics and the English Language*, *Horizon*, April 1946, reproduced with estate permission by [The Orwell Foundation](https://www.orwellfoundation.com/the-orwell-foundation/orwell/essays-and-other-works/politics-and-the-english-language/). Rule 6 must survive every strictness level; a mechanical ban on passive voice or technical terminology would erase its exceptions.

**Rights and Korean.** The Foundation explicitly warns that the material remains copyrighted in some jurisdictions, including the US. Write original operational summaries, not a bundled essay. Korean needs reviewed adaptations for passive constructions, jargon, and stock expressions. Word length and the essay's English etymological preferences do not transfer literally; necessary Korean technical terms remain intact.

### Boring Professor — user-original method

**Meaning and core.** The user's specification, not an established named school: explain technically and logically, without jokes or metaphors. Proposed project-original sequence: define the problem and terms; state assumptions; describe the mechanism or derivation in dependency order; distinguish evidence, inference, and uncertainty; work through a literal example when helpful; state scope and exceptions. “Boring” should not become permission for needless length or inaccessible language.

**Evidence and questions.** Primary specification: the user's request in this conversation. No invented professor, publication, or external certification is needed. Literal diagrams and worked numerical examples can support technical explanation without adding metaphor.

**Rights and Korean.** Original project instructions can be authored without borrowing a proprietary checklist. Korean requires stable technical terminology and a chosen explanatory register. Do not remove subjects or connective relations if that would obscure the logical dependencies. No English sentence cap is justified by this specification.

### GTM / Graduate Texts in Mathematics — user-original formal method

**Meaning.** [Springer's official GTM series page](https://link.springer.com/series/136) describes graduate introductions intended to develop active understanding and support teaching and self-study. A book series is not itself a uniform formal-writing standard. The user's requested symbolic/formal mode therefore needs to be recorded as project-original, with GTM identified as an inspiration rather than an official source of rules.

**Operational core.** Define objects and notation before use; state assumptions and domains; distinguish definitions, propositions, proofs, and examples; make quantifiers and implication direction explicit; justify each nontrivial step; preserve boundary cases and counterexamples. Use symbolic notation where it increases precision, accompanied by enough prose to identify its meaning. Do not manufacture a theorem or proof for an empirical claim.

**Evidence and limits.** Read the official series description and metadata, ISSNs 0072-5285 and 2197-5612. No individual GTM volume or formal authoring specification was reviewed. A future claim of faithfulness to a particular book requires selecting and reading that book's relevant passages.

**Rights and Korean.** No permissive book license was verified. Korean review should cover mathematical vocabulary, quantifier scope, symbols in prose, and theorem/proof conventions; English source sentences are not a Korean style specification.

### Answer with HTML — user-original delivery method

**Meaning and operational core.** Deliver an explanation as an HTML artifact with CSS, diagrams, mathematical notation, or JavaScript interaction when these help the reader understand. This is a delivery method, not a fixed prose style. Proposed project-original behavior: choose the explanatory question; present a usable initial state; connect each control to a visible conceptual change; keep displayed formulas, labels, assumptions, and computed values consistent; provide accessible labels and a readable static fallback. Use the smallest artifact that answers the question; a framework, renderer CLI, or video system is not implied.

**Evidence and scope.** The owner's description defines the requested method. The closest located project is [QingYunA/answer-me-with-html](https://github.com/QingYunA/answer-me-with-html/tree/053619b917c6bf2e17eae5496d05eb08e10fe889), rather than the supplied spelling `answer-with-me-html`. Its README and skill were read; the current implementation delegates Markdown-to-HTML rendering to a bundled CLI. Anthropic's web-artifacts-builder is another artifact-delivery reference. Neither implementation was run or adopted.

**Korean and rights.** An English-authored skill can produce Korean labels, prose, and diagrams without a duplicate skill. Review fonts, line wrapping, accessible names, and mathematical terminology for the chosen output language. Upstream MIT/Apache license evidence and reuse boundaries are listed below; no source code or assets were copied.

### Barbara Minto's Pyramid Principle

**Meaning and core.** Structure a business argument around one governing point, with grouped supporting insights and facts below it. First identify the reader's question, then supply the answer and the logically related support. Check that each grouping actually supports the insight claimed above it; a count of reasons is not itself the insight. These are faithful summaries of the official public explanations, not a reproduction of the entire book. [Concept](https://www.barbaraminto.com/concept), [course outline](https://www.barbaraminto.com/course).

**Evidence and read scope.** Read the complete public concept and course pages, plus the home page's textbook description. The site identifies the 1996 *The Minto Pyramid Principle: Logic in Writing, Thinking and Problem Solving* edition and distinguishes the older 1987 book and unchanged 2002 reissue. The book and paid course were **not read**. Therefore do not attribute every popular consulting checklist, an exact fixed number of supporting points, or a complete MECE implementation to this review. [Official home/textbook description](https://www.barbaraminto.com/).

**Rights and Korean.** Official pages carry an all-rights-reserved notice and mark the named framework; no permissive redistribution license was verified. Author original questions and examples. Korean needs review of conclusion-first structure and explicit links between grouped evidence and claims. A cultural claim that all Korean readers prefer a different structure would need evidence.

### Steve Jobs presentations — observed practice, not a canonical rulebook

**Meaning and evidence.** The source is observed presentation structure, not Jobs impersonation or an assumed endorsement. Apple documents the 2007 iPhone introduction's three-functions-to-one-product framing in its [official retrospective, 2017-01-08](https://www.apple.com/newsroom/2017/01/iphone-at-ten-the-revolution-continues.html). Stanford publishes Jobs's [prepared 2005 commencement address](https://news.stanford.edu/stories/2005/06/youve-got-find-love-jobs-says), explicitly organized around three personal stories. Read the Apple article and Stanford's retrieved prepared-text passage; neither constitutes a full keynote/video analysis.

**Operational adaptation.** Identify the central audience benefit; use a small, signposted sequence; present a concrete change or demonstration when the subject supports it; connect each section to the central message. These are project adaptations inferred from the cited examples, not universally prescribed Jobs rules. A fixed three-part mandate is unjustified. Keep real supporting evidence and limitations; never fabricate experiences, live demonstrations, reactions, or product performance.

**Rights and Korean.** No permissive license for speeches, slides, footage, or images was verified. The [Steve Jobs Archive's edited collection](https://book.stevejobsarchive.com/) was located and its editorial/copyright statements inspected; it is © 2023, all rights reserved, and explicitly excerpted. Korean requires attention to spoken cadence, register, and audience knowledge; sparse English slide text is not a Korean word-count rule. Carmine Gallo's separate later framework was not reviewed or substituted.

### Ernest Hemingway — documented literary practice

**Meaning and core.** Hemingway describes deliberate omission based on knowledge, concrete observed detail, and revision to convey experience. Omission caused by ignorance leaves a gap rather than a stronger story. For this project's factual tasks, any extension is an adaptation: remove unnecessary exposition while retaining information the reader needs to interpret or act correctly. Required facts, conditions, uncertainty, citations, and warnings cannot disappear under an “iceberg” label.

**Evidence and read scope.** Read the omission/observation discussion and revision exchange in George Plimpton's interview, *The Art of Fiction No. 21*, *The Paris Review* 18, Spring 1958, available on [the original publication's site](https://www.theparisreview.org/interviews/4825/the-art-of-fiction-no-21-ernest-hemingway). The interview gives evidence for these practices, not a universal ban on adverbs or a numerical sentence-length rule. No Hemingway book was read for this task.

**Rights and Korean.** No permissive interview license was verified; use original summaries and synthetic examples. Korean needs review for natural sentence rhythm, explicit referents, and how omitted context affects comprehension. The user means the author, not the separate Hemingway Editor product, so product readability scoring is outside this candidate's source basis.

### Hunminjeongeum: explanation from purpose through principles to examples

**English meaning:** a historical explanatory document about a newly created writing system; a promising model for explaining a designed system, rather than a generic plain-language style.

The [UNESCO record](https://www.unesco.org/en/memory-world/hunminjeongum-manuscript) establishes the 1446 Haerye edition, Sejong's main text, scholarly explanations/examples, and Jeong Inji's postface. The [Republic of Korea nomination](https://media.unesco.org/sites/default/files/webform/mow001/republic_of_korea_hunmin_chongum.pdf), especially PDF pp. 3–5 and 11–12, describes purpose, creation principles, component explanations, combination rules, and usage examples. It also explicitly praises the document's logical development and independent learnability. Those assessments are the nominator's claims, not this project's measured results.

**Confirmed intent and adaptation:** open with the problem, intended reader, and benefit; develop principles, analysis, and examples that answer that problem; conclude with the supported result and its limits. Suitable for specifications and educational explanations. The owner clarified that the primary goal is to explain why the document is needed and make its introduction, body, and conclusion cohere. This is not a request to reconstruct all Haerye chapters or equate the historical work with IMRaD.

The [National Institute of Korean History's Sejong Annals entry](https://sillok.history.go.kr/id/kda_12809029_004), volume 113, Sejong 28, lunar 9/29 (1446), was also read for the royal foreword and beginning of Jeong Inji's foreword in the original and official Korean translation. The foreword identifies difficulty expressing the language through the existing writing system and states the intended ease and everyday usefulness of the new letters. It does not merely claim that language difference made learning impossible. Summarizing the stated purpose is source-faithful; using modern introduction/body/conclusion headings is a project adaptation.

**Korean need:** review Classical Chinese/modern translations and historical terminology; do not convert historical orthographic prescriptions into current Korean writing rules.

**Read/rights:** UNESCO live record, selected nomination passages, and the identified Annals foreword passages, not the full 1446 original. Ancient text, modern translations, photographs, and website prose require separate rights treatment; no images/translations bundled.

### Feynman-inspired explanation and the modern Feynman Technique

**English meaning:** explaining a concept to reveal gaps, checking sources, and refining the explanation for a specified audience.

Goodstein's firsthand anecdote in [*Feynman's Lost Lecture*, excerpt, 1996, PDF p. 6](https://calteches.library.caltech.edu/563/2/Goodstein.pdf) concerns failure to reduce spin/statistics to a **freshman** lecture. The [1989 article record](https://authors.library.caltech.edu/records/gqfj9-g9b59) establishes its earlier teacher essay, but its PDF download failed. Neither source verifies a child/grandmother quotation. Do not claim those popular wordings are authentic Feynman quotations.

[Scott Young, September 2011](https://www.scotthyoung.com/blog/2011/09/01/learn-faster/) documents his named technique; [Young, June 2017, technique/depth sections](https://www.scotthyoung.com/blog/2017/06/13/how-much-do-you-understand/) identifies his adaptation and warns that feeling able to explain does not imply being able to solve problems. [Farnam Street's current formulation](https://fs.blog/feynman-technique/) specifies a 12-year-old audience; it is a modern formulation, not historical proof.

**Operational adaptation:** set audience/prerequisites; explain mechanism; mark gaps; verify them; revise; test a transfer task. Preserve necessary technical terms and analogy limits. No universal child-reading target.

**Korean need:** assess audience vocabulary and culturally intelligible examples, not English grade or word-count substitutions.

**Read/rights:** cited HTML sections and anecdote, not Feynman's whole books. Caltech excerpt, Young, and Farnam Street retain copyright; write original questions and examples.

### Aristotelian syllogistic argument checking

**English meaning:** making premises and terms explicit and checking whether a conclusion necessarily follows.

[Aristotle, *Prior Analytics*, Book I, parts 1–4, A. J. Jenkinson translation](https://classics.mit.edu/Aristotle/prior.1.i.html) defines premises, universal/particular statements, syllogism, and valid/invalid first-figure relations. This supports a real reasoning method, not simply a three-paragraph writing pattern.

**Operational adaptation:** extract premises and conclusion; normalize repeated terms; preserve quantifiers, negation, modality, and existence assumptions; test validity separately from factual support; expose a missing premise instead of inventing one. Use for deductive arguments. Probabilistic evidence and causal explanations must not be promoted into necessary deduction. Traditional syllogistic and modern predicate logic differ on existential assumptions.

**Korean need:** preserve 모두/일부/어떤, scope of negation, omitted subjects, and consistent term reference.

**Read/rights:** specified opening parts only, not all Aristotle or modal syllogistic. Ancient original and this translation/site edition have distinct rights; no source-text bundling or MIT claim about translations.

### Socratic examination and self-questioning

**English meaning:** testing one's claims, definitions, and assumptions through questions and attempted refutation.

In [Plato, *Phaedrus*, 229e–230a, Jowett translation](https://classics.mit.edu/Plato/phaedrus.html), Socrates refers to self-knowledge as a **Delphic inscription**. It does not establish that Socrates coined “Know thyself.” [*Apology*, especially 21b–23b and 38a](https://classics.mit.edu/Plato/apology.html), depicts examination of claimed knowledge and of oneself/others. These are Plato's depictions, not surviving writing by Socrates.

**Operational adaptation:** clarify a claim; identify reasons/assumptions; seek counterexamples and alternative explanations; revise or retain uncertainty; stop when further questions cannot materially change the answer. Self-review and an interactive teaching dialogue are different products; do not force an interview on a writing request.

**Korean need:** questions must be respectful without weakening logical challenge; resolve omitted referents and implied agreement.

**Read/rights:** identified passages in hosted translations, not all dialogues. Attribute the historical practice via Plato; review translation rights before redistribution.

### Caterpillar Technical English (CTE)

**English meaning:** controlled source English for consistent technical documentation and translation.

[Kamprath, Adolphson, Mitamura, Nyberg, CLAW 1998](https://aclanthology.org/www.mt-archive.info/90/CLAW-1998-Kamprath.pdf), read through its [author-uploaded full text, sections 1–4](https://www.researchgate.net/publication/2284766_Controlled_Language_for_Multilingual_Document_Production_Experience_with_Caterpillar_Technical_English), distinguishes CTE from earlier **Caterpillar Fundamental English (CFE)**. CFE sought to avoid translation; CTE supports translation using controlled terminology, permitted grammar, interactive disambiguation, reusable information elements, and review. CTE can retain grammatical complexity needed by the domain. The paper even gives a term with multiple approved domain senses; “one word, one meaning” is too absolute.

**Operational adaptation:** use the supplied project glossary; resolve ambiguous references/senses; preserve procedural conditions, warnings, and markup. Do not invent an official approved vocabulary, full grammar, current Caterpillar implementation, or compliance certificate.

**Korean need:** controlled-English input and Korean translation/review are separate; Korean authoring requires its own terminology and grammar rules.

**Read/rights:** 1998 historical report, not internal CTE manual or current standard. No dictionary/tool reuse or permissive license verified.

### Federal Plain Language Guidelines

**Meaning:** Audience-centered public information that readers can find, understand, and use. **Core behavior:** Establish the reader’s knowledge and task; organize around their questions; simplify expression while retaining conditions; test whether intended readers find and understand the answer. Plain language does not prescribe one school reading grade for every audience. Splitting a conditional sentence must retain its logical relationship.

**Evidence/scope:** PLAIN/GSA’s archived [guideline introduction](https://github.com/GSA/plainlanguage.gov/blob/fd7694740f19c0ed20ed71c2dd1dc92699e920fa/_pages/guidelines/index.md), [audience](https://github.com/GSA/plainlanguage.gov/blob/fd7694740f19c0ed20ed71c2dd1dc92699e920fa/_pages/guidelines/audience/index.md), [short sentences](https://github.com/GSA/plainlanguage.gov/blob/fd7694740f19c0ed20ed71c2dd1dc92699e920fa/_pages/guidelines/concise/write-short-sentences.md), and [usability testing](https://github.com/GSA/plainlanguage.gov/blob/fd7694740f19c0ed20ed71c2dd1dc92699e920fa/_pages/guidelines/test/usability-testing.md) were read. Pin: `fd7694740f19c0ed20ed71c2dd1dc92699e920fa` (2025-09-23). The March 2011/May 2011 revision PDF was identified, but its body was not successfully extracted here. [Digital.gov](https://digital.gov/guides/plain-language) now carries selected adapted material, explicitly distinct from the full archive.

**Scope:** Use the named Federal Guidelines archive as the initial evidence base; current Digital.gov adaptations are supplementary and must remain identified. Full-PDF coverage is still unverified. Avoid treating a heuristic count as verified quality. **Korean:** A separate application layer is necessary for sentence endings, omitted subjects, bureaucratic Sino-Korean terms, and condition placement; English word counts are not eojeol counts. **Rights:** Read [repository license](https://github.com/GSA/plainlanguage.gov/blob/fd7694740f19c0ed20ed71c2dd1dc92699e920fa/LICENSE.md): US public domain plus worldwide CC0 dedication; third-party quotations still need individual checking.

### IMRaD research-report structure

**English meaning:** Introduction, Methods, Results, and Discussion for reporting original research.

[ICMJE manuscript preparation](https://icmje.org/recommendations/browse/manuscript-preparation/preparing-for-submission.html), read General Principles, Reporting Guidelines, and Introduction–Discussion; [recommendations index](https://www.icmje.org/recommendations/) identifies the January 2026 update. The guidance expressly allows other article formats.

**Operational adaptation:** state question/context; describe reproducible methods; report findings separately from interpretation; discuss limitations and bounded conclusions; check abstract/body consistency. Follow the target journal and study-design reporting guideline. Never fabricate methods, participants, approval, data, or results to fill headings.

**Korean need:** journal-specific Korean section labels, technical terminology, and uncertainty/causality review; no universal paragraph count.

**Read/rights:** selected current guidance sections, not every linked reporting standard. ICMJE website states all rights reserved; summarize originally, do not bundle its checklist as MIT content.

### SCQA and its relationship with Minto

**English meaning:** Situation–Complication–Question–Answer, a possible opening structure for decision documents.

[Minto's home](https://www.barbaraminto.com/), [concept](https://www.barbaraminto.com/concept), and [course](https://www.barbaraminto.com/course) pages explain a single governing point, grouped supporting ideas, and identifying the reader's question. Minto's site explicitly calls it the **SCQ Framework**, and the site describes the 1996 textbook as superseding the earlier book. These pages alone do not establish all rules of an official four-part SCQA implementation.

**Operational adaptation:** establish relevant shared context; show the change/tension; identify the decision question; state a supported answer. Avoid manufacturing conflict or presenting an unproven recommendation as a fact. The initial separate SCQA candidate focused on the opening; consolidation now keeps that optional framing inside Minto. Share provenance and avoid duplicating the whole Pyramid workflow.

**Korean need:** natural context and conclusion placement, explicit distinction between fact and proposal; no English sentence quotas.

**Read/rights:** three public pages, not paid course/textbook. Copyright and marks remain with Minto; original summaries only, no affiliation claim.

### Diátaxis

**Meaning:** Match documentation to four reader needs: learning, accomplishing a task, consulting facts, and developing understanding. **Core behavior:** Classify by action versus knowledge and acquisition versus application; write tutorials, how-to guides, reference, and explanation accordingly; connect related content without mixing their purposes.

**Evidence/scope:** Daniele Procida’s official [Start here](https://diataxis.fr/start-here/) was read in full through its compass table; [colophon](https://diataxis.fr/colophon/) and [translation guidance](https://diataxis.fr/translation/) were inspected. Living framework; repository revision identified as `957c09ca40b4a1edc23874f713e01937d50d54d5` (2026-08-06). This is document architecture and workflow, not primarily sentence editing.

**Scope:** Support selecting/drafting a requested type and classifying/restructuring an existing document set when requested. Do not require four folders or an inflexible reader sequence. **Korean:** The four needs transfer well; consistent Korean labels and realistic Korean examples need review. Upstream says Korean translation is in progress, not published as a completed locale. **Rights:** [LICENSE.rst](https://github.com/evildmp/diataxis-documentation-framework/blob/957c09ca40b4a1edc23874f713e01937d50d54d5/LICENSE.rst) is CC BY-SA 4.0. Do not import text, translated text, or diagrams and relabel them MIT; original operational summaries need careful provenance separation.

### Amazon six-page narrative / AWS

**Meaning:** A reasoned narrative for planning and decisions, constrained to readable length. **Core behavior:** Explain purpose and background for colleagues outside the immediate team; support claims with evidence; develop plans and accountability in prose. The six-page ceiling permits appendices and is a rendered-document constraint, not a fixed word count.

**Evidence/scope:** Richard Howard, AWS Startup Business Development, [“How to Use Amazon’s Narrative Process…”](https://aws.amazon.com/blogs/startups/startup-advice-how-to-write-a-narrative/), 2019-09-25: introduction, definition, starting guidance, and beginning of fictional example read. [AWS product-management explanation](https://aws.amazon.com/executive-insights/content/product-management-at-amazon/) inspected for the distinct Working Backwards process: a proposed future customer benefit expressed in a press release, expanded by FAQs.

**Scope:** Use `amazon-six-page-narrative` as the six-pager interpretation. AWS service documentation, internal narratives, and PRFAQ are separate methods; do not merge their rules. Howard’s instruction to support claims must not cause uncertainty to be deleted. **Korean:** The reasoning structure transfers; a six-page Korean version requires specified typography and page size, not English-to-Korean count conversion. **Rights:** Public explanatory pages are not permissively licensed templates. Attribute original summaries; do not reproduce fictional examples or imply Amazon approval.

### NIST Technical Series Publications Author Instructions

**Meaning:** Preparation of a traceable, accessible scientific/technical report. **Core behavior:** Appropriate report components, consistent headings/references, accessible figures/tables, and preserved SI units and measurement uncertainty.

**Evidence/scope:** The initial label did not identify an exact publication; the owner subsequently selected the linked official instructions. Read relevant organization, plain-language, accessibility, and measurement sections of NIST Research Library’s [NIST Technical Series Publications Author Instructions](https://www.nist.gov/nist-research-library/nist-technical-series-publications-author-instructions), created 2021-02-16; page footer shows an update dated 2026-11-06 (figures section 2026-06-05). Its plain-language guidance explicitly preserves the usefulness of agreed technical terminology and is contextual advice. Agency publication identifiers, seals, internal clearance, and templates are institutional requirements, not portable writing rules.

**Confirmed scope:** The owner selected the linked Technical Series Publications Author Instructions. Extract transferable scientific/technical authoring guidance, keeping NIST submission procedures separate. NISTIR 8366 is a different, narrower source, *Guidance for NIST Staff on Using Inclusive Language in Documentary Standards*. Its [official PDF](https://nvlpubs.nist.gov/nistpubs/ir/2021/NIST.IR.8366.pdf) currently contains a withdrawal notice: original release 2021-04-29, withdrawn 2025-02-20. Do not represent it as current general author guidance. **Korean:** Preserve technical terms, symbols, units, uncertainty, and citation identity; apply Korean terminology/accessibility conventions separately. **Rights:** Check individual NIST/third-party rights; government authorship does not license copied standards, marks, or external examples.

### IETF / RFC writing

**Meaning:** Precise technical specifications with explicit scope, terminology, references, and requirement strength. **Core behavior:** Preserve technical meaning above editorial preferences; separate normative and informative references; supply appropriate abstract, introduction, security and IANA considerations; use requirement keywords only with their declared meaning.

**Evidence/scope:** Heather Flanagan and Sandy Ginoza, [RFC 7322](https://www.rfc-editor.org/rfc/rfc7322.html), September 2014: status, introduction/philosophy, style/structure overview, and requirement/reference sections read. It is **Informational**, not an Internet Standard. [Current RFC Editor style updates](https://www.rfc-editor.org/authors/rfc-style-guide/) were read through author-choice/XML guidance. [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119.html), March 1997, and [RFC 8174](https://www.rfc-editor.org/rfc/rfc8174.html), May 2017, were read for BCP 14 semantics. Normative text need not use uppercase keywords.

**Scope:** Interpret the requested writing style as an internal RFC adaptation; actual RFC submission requires separately requested submission work. RFC 7322 has updates, including RFC 7997; do not enforce its historical English-only/ASCII presentation without current context. **Korean:** An internal Korean adaptation must preserve MUST/SHOULD/MAY distinctions explicitly; Korean text is not official RFC submission compliance. **Rights:** IETF Trust/BCP 78 provisions apply; do not call RFC prose MIT or confuse code-component rights with document rights.

### Design Docs at Google

**Meaning:** Write down a consequential software design and its trade-offs before implementation and review. **Core behavior:** Establish context, goals/non-goals, proposed design, alternatives, and relevant cross-cutting concerns; explain why the approach fits the constraints; use detail that supports decisions.

**Evidence/scope:** Malte Ubl’s firsthand [Design Docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/), 2020-07-06: opening, anatomy through alternatives, review/conclusions inspected. This is an experienced practitioner’s account, not an official compulsory Google template. He explicitly allows project-appropriate forms. Google’s [Documentation Best Practices](https://google.github.io/styleguide/docguide/best_practices.html) independently describes design documents as proposals for feedback and later decision archives. [Google developer documentation style](https://developers.google.com/style) is a separate editorial reference, inspected only for scope/hierarchy/rights.

**Scope:** Do not force complete schemas/code into the design doc or fabricate resolved decisions. **Korean:** Structure transfers; Korean engineering terminology and review etiquette need examples, not a separate theory. **Rights:** No permissive license was verified for Ubl’s article; summarize independently. Google Developers page is CC BY 4.0 (code Apache 2.0), which does not extend to Ubl’s site.

### Microsoft Writing Style Guide

**Meaning:** Clear, helpful technology communication with consistent terminology and usable instructions. **Core behavior:** Lead with reader needs and next steps; keep wording concise; use consistent UI/technical terms; write for global audiences without losing precision.

**Evidence/scope:** Microsoft’s [welcome](https://learn.microsoft.com/en-us/style-guide/welcome/) (updated 2025-01-08), [top ten tips](https://learn.microsoft.com/en-us/style-guide/top-10-tips-style-voice) (2026-07-06), and [global writing tips](https://learn.microsoft.com/en-us/style-guide/global-communications/writing-tips) (2023-06-14) read. This is the living online guide, not the older printed *Microsoft Manual of Style*.

**Scope:** Separate generally useful guidance from Microsoft product/interface conventions. Never apply “shorter is always better” above project meaning-preservation invariants. **Korean:** English contractions, articles, capitalization, and serial commas do not transfer literally; speech level, UI labels, particles, and terminology require locale rules. **Rights:** Archived source repository `c6945c32294e845a84b192a094fb1b7c2c452a6a` has [CC BY 4.0 documentation license](https://github.com/MicrosoftDocs/microsoft-style-guide/blob/c6945c32294e845a84b192a094fb1b7c2c452a6a/LICENSE) (heading/start inspected), separate code license; the archive may lag current Learn pages. No copying done.

### New Hart’s Rules

**Meaning:** An English editorial and publication reference for consistent presentation. **Potential behavior:** Resolve selected spelling, punctuation, capitalization, quotations, numbers, and reference decisions using an identified edition and declared house style.

**Evidence/scope:** OUP’s catalog page was blocked by a browser challenge. An [OUP-origin preview hosted by a bookseller](https://api.pageplace.de/preview/DT0400.9780191649134_A23591405/preview-9780191649134_A23591405.pdf) was inspected: title/copyright pages, preface, contents, and beginning of chapter 1. Verified **second edition, 2014**, Anne Waddingham, print ISBN 9780199570027. The complete book and most operational rules were **not read**. No full-book method should be claimed from this preview.

**Scope:** Start with an edition-specific UK English editorial reference; a complete operational checklist remains source-limited until its relevant passages can be read. This is not Oxford’s unrelated public university communications guide. **Korean:** English copyediting conventions largely need separate Korean equivalents; the main reuse is consistent house-style decision making and handling embedded English. **Rights:** Copyright OUP 2005/2014, all rights reserved. Use a lawfully obtained edition for detailed evidence; do not bundle the preview, book, dictionary entries, or reproduced checklists.

## Comparable projects

These are implementation references, not evidence that their attributed methods are correct. Reading their source does not establish host compatibility or output quality. No upstream code, dictionary, template, or image is bundled.

| Project and inspected revision | Read scope and rights evidence | Useful reference and boundary |
| --- | --- | --- |
| [QingYunA/answer-me-with-html](https://github.com/QingYunA/answer-me-with-html/tree/053619b917c6bf2e17eae5496d05eb08e10fe889) | README, `skills/answer-me-with-html/SKILL.md`, root LICENSE; MIT. | Closest match to Answer with HTML. A bundled CLI converts an extended Markdown draft into a page. Reference its content/rendering separation; do not automatically inherit its CLI, global settings, video mode, broad activation, or language thresholds. Its adapted STE warning/blocking modes do not prove ASD conformance. |
| [anthropics/skills web-artifacts-builder](https://github.com/anthropics/skills/tree/2c5958ecac7cee2b583967a2c4981d0f4a75c579/skills/web-artifacts-builder) | `SKILL.md` and its own `LICENSE.txt`; Apache-2.0 for this skill, not a blanket claim about the repository. | Bundles complex React artifacts into one HTML file. Its framework/toolchain is unnecessary for a small explanation page; retain only the idea of a shareable artifact when it serves the task. |
| [mcollina/skills documentation](https://github.com/mcollina/skills/tree/c75d70dbfbe991d8cec42aeda0b64ff14fbb9ac7/skills/documentation) | `SKILL.md`, root LICENSE; MIT. | Direct Diátaxis skill reference: select a documentation type before writing. Do not inherit mandatory clarification on every task or the unevaluated 30-second reference-lookup target. The implementation's MIT license does not relicense upstream Diátaxis text. |
| [Jamfin92/skills ste](https://github.com/Jamfin92/skills/tree/24314eaa5bc63db860f9ec4f41e9f179cfd1e9d4/ste) | `SKILL.md` version 0.1.0; root license retrieval did not establish a license. Reference only. | Separates procedures and descriptions. Reject its example that turns a possible timeout cause into a certain one: this violates this project's meaning-preservation invariant. Do not adopt its compliance or rights claims as authoritative. |
| [ashryaagr/karpathy-output-style](https://github.com/ashryaagr/karpathy-output-style/tree/4f6c5e974ad8a41fb2ffd628de2ed5271f0b5d88) | README, selected `skills/clear-writing/references/asd-ste100.md`, root LICENSE; MIT. | Separates STE-inspired drafting from conformity. Its interpretation of the 80% phrase is secondary to the original post, now read in full. |
| [danyuchn/asd-ste100-skill](https://github.com/danyuchn/asd-ste100-skill/tree/f38838aee0504fae07ef057667182a7c5af4ffe6) | Root `SKILL.md` through workflow/output, version 0.4.0, root LICENSE; MIT. | Useful strict/flavored and structural/dictionary distinctions. Do not inherit hidden mode selection or assume its source-standard claims were independently verified. |
| [m4vic/socratic](https://github.com/m4vic/socratic/tree/3cfaf6e73a8be29d4a8ed5ca80aa03a05f9aad7f) | README, `SKILL.md`, root LICENSE; MIT. Question packs were not read. | Modern self-interrogation and stopping-rule reference. Self-review defaults fit the user's request better than a compulsory interview. It is not historical evidence about Socrates. |
| [AWS product-team prompts](https://github.com/aws-samples/sample-kiro-cli-prompts-for-product-teams/tree/1e1b3491465c2c0f742a92d0072a82454ec5ebb8) | `.claude/skills/product-prfaq/SKILL.md`, `prompts/PRFAQ_Guide.md`, LICENSE; MIT-0. | Customer questions and skeptical FAQ are useful PRFAQ references, not six-pager rules. Omit host orchestration, hardcoded paths, handoff schemas, arbitrary limits, and invented quotations. |
| [MIF documentation plugin](https://github.com/modeled-information-format/mif-docs-plugin/tree/3e5725894db37568e41239745d79b2895b05ade0) | `skills/google-design-doc/SKILL.md`, `skills/nist-sp/SKILL.md`, LICENSE; MIT. | Compare design alternatives and separate design/decision/requirements documents. Omit MIF/JSON-LD machinery and mandatory sections not supported by the intended source. Its NIST-inspired genre cannot establish agency authority. |
| [docwriter-org/plain-writing-skill](https://github.com/docwriter-org/plain-writing-skill/tree/f0d3630983ac7a82aa580f1c1509d72df739ee12) | `skills/plain-writing/SKILL.md`, LICENSE; MIT. | Structure-first editing reference, not an official Federal Guidelines implementation. Omit universal analogy/dash bans and arbitrary clause/list limits. |

Other inspected references were not advanced for reuse: [tamdogood's Orwell skill](https://github.com/tamdogood/builder-essential-skills/blob/1be9984bdafbb68eaff400bdd82773a1d41ee7ec/skills/orwell-writing/SKILL.md) mixes Orwell and STE (skill read; root license text unread); [sysmatt's STE summary](https://github.com/sysmatt/ste-rules/blob/c18369e275a6873e09a417ac93219499190a2059/STE100-writing-rules.md) has no verified license (summary read); [LeadGrowGTM/feynman-skill](https://github.com/LeadGrowGTM/feynman-skill) had an MIT marketing claim but no verified license text in the inspected listing (README only, revision unrecorded).

## Implementation boundaries

The owner selected CTE rather than CFE and the NIST Author Instructions linked above. Hunminjeongeum means purpose-first writing with a clear introduction, body, and conclusion. The named Karpathy post, now read in full, is the intended source for the informal 80% intensity, with HTML/video outside the ASD skill's scope. These clarify scope without approving unverified historical claims or compliance percentages.

The initial implementation selects explicit ASD-inspired profiles and maps `normal` to `standard`. Full standard/dictionary checks, book-wide coverage, rights to bundle source material, and Korean-specific adaptations remain unverified wherever marked. Ask only when a missing choice materially changes the method; ordinary task parameters and the bounded interpretations stated above do not require another interview.

Keep methods distinct even where they overlap: ELI5 targets audience knowledge; Feynman-inspired explanation tests explanatory completeness; Minto organizes an argument and can frame its opening; IMRaD organizes a research report; Diátaxis selects documentation types; HTML determines delivery. Combine them only through an explicit compatible request.

The initial catalog uses English-first instructions and one separately justified Korean companion, with source-linked cases. Routing and installation machinery remain outside this implementation. Preserve the entire method directory when distribution is tested.
