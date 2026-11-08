# References

Project-wide bibliography of projects, websites, papers, books, and guides that inform the work.

## Recording references

Add or update a source in the same PR that uses it. Keep one entry per source and include:

- Author or responsible organization, title, and canonical URL or DOI.
- Inspected commit, version, edition, or publication date where available; access date and the pages, sections, or files actually read. Mark unknown details instead of guessing.
- What the source informed, the practices adopted or omitted, and links to affected documents or skills. Distinguish an unread candidate, a consulted reference, and an adopted implementation; reading documentation does not establish tested behavior.

Keep detailed evidence with each method under the [authoring contract](METHOD_AUTHORING.md), and link it from the bibliography entry. Link rights/reuse records in [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md). The bibliography does not replace source-to-rule provenance or required license notices. Add source candidates when relevant, clearly marked as unread until inspected.

## mattpocock/skills

Matt Pocock. [skills, commit 4ae2317](https://github.com/mattpocock/skills/tree/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d). Accessed 2026-11-06; inspected repository structure, README, agent/contributor guidance, and maintainer installation script. Informs documentation and repository organization under [CONTRIBUTING.md](../CONTRIBUTING.md). License evidence is in [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md).

On 2026-11-08 we also read [Writing for Agents](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/productivity/writing-for-agents/SKILL.md) and its skill mechanics notes (installed project version 1.3.2). This informed two choices in the [catalog](../skills/): define a term where it changes a decision, and end a worked example with a check the writer can actually perform.

### Structure and adaptation

| Upstream pattern | This project |
| --- | --- |
| README purpose, installation, and linked skill index | Matching English/Korean sections with honest candidate and installation status |
| Per-skill directories grouped into buckets | Complete method directories; keep a flat catalog until real content needs categories |
| Human docs separate from agent instructions | Short method summaries; steps and source evidence stay with the method |
| Contributor/scope docs and issue forms | Focused issues/PRs; allow future community methods and contributions |
| Version automation and plugin manifests | Existing Python checks and manual source versions; add packaging only when needed |

Upstream AGENTS.md links to CLAUDE.md; we retain a plain CLAUDE.md pointer to shared AGENTS.md. Its maintainer-only global-link script can replace existing directories and is not reused: our installer contract preserves unowned/modified content.

The collaborator-only PR restriction, closed new-skill intake, bucket taxonomy, Changesets dependency, triage bots, and plugin packaging do not fit the current foundation. Use existing installers first and test host behavior before claiming support. This is a structural reference; no upstream implementation or branding is bundled, and no affiliation is implied.

## Anthropic Skill Creator

Anthropic's [Skill Creator](https://github.com/anthropics/skills/blob/2c5958ecac7cee2b583967a2c4981d0f4a75c579/skills/skill-creator/SKILL.md) informed the [paired trials](../evals/runs/2026-11-08-worked-examples.md). We read its guidance on examples, matched tasks, separate agent contexts and revising after failures on 2026-11-08. We wrote our own prompts, grading criteria and examples. The upstream skill has its own [Apache-2.0 license](https://github.com/anthropics/skills/blob/2c5958ecac7cee2b583967a2c4981d0f4a75c579/skills/skill-creator/LICENSE.txt).

## vercel-labs/skills

Vercel. [skills README, commit d3701c1](https://github.com/vercel-labs/skills/blob/d3701c11b1101251af14c9d148f026e1a47ebe17/README.md). Accessed 2026-11-07; scope: README. Identifies an existing installer candidate with project-scoped installation and agent selection, informing the reuse-first delivery plan in [PROJECT.md](PROJECT.md) and the installation contract in [ARCHITECTURE.md](ARCHITECTURE.md). No installer integration or behavior tests have been completed; license evidence is in [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md).

## Agent Skills

For the checkout commands, we read OpenAI's [Build skills](https://learn.chatgpt.com/docs/build-skills) and [Developer commands](https://learn.chatgpt.com/docs/developer-commands), and Anthropic's [Extend Claude with skills](https://code.claude.com/docs/en/skills) on 2026-11-08. The relevant sections describe repository discovery, explicit invocation and slash command names. The project adapters contain original instructions. [Host verification](COMPATIBILITY.md) records the installed versions and what we exercised.

We also inspected [OpenCode 1.16.2 command expansion](https://github.com/anomalyco/opencode/blob/v1.16.2/packages/opencode/src/session/prompt.ts#L1436-L1448) on 2026-11-08. Its handling of shell syntax after argument substitution affects whether arbitrary source text can safely pass through a native command template. That version has no WSG adapter in this checkout.

Agent Skills project. [Repository README, commit 83021e2](https://github.com/agentskills/agentskills/blob/83021e2be457a9b6679148719c1f6074f0ad975e/README.md) and [skills-ref README](https://github.com/agentskills/agentskills/blob/83021e2be457a9b6679148719c1f6074f0ad975e/skills-ref/README.md). Accessed 2026-11-07; scope: those two files. Consulted for portable skill-directory structure and validation references under [ARCHITECTURE.md](ARCHITECTURE.md). The library is explicitly demonstration-only, so it is not adopted as a production dependency. Code and documentation have distinct licenses recorded in [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md). The living [format specification](https://agentskills.io/specification) was read on 2026-11-07 for directory layout, name/description frontmatter, progressive disclosure, and relative references; implementation follows a simple portable subset. No specification prose/code was copied. Host compatibility remains unverified.


## Initial catalog research sources

Accessed 2026-11-07. These entries informed the [24-method assessment](INITIAL_CATALOG_RESEARCH.md) and its experimental implementations. The [initial catalog review](CATALOG_REVIEW.md) pins every original method’s source-to-rule evidence to the initial commit. The [consolidation review](CATALOG_CONSOLIDATION.md) records current representatives and retired scopes; bibliography entries for consulted but retired methods remain historical research, not active skill recommendations. Its corresponding method sections record editions, actual passages read, Korean considerations, and source-access limits. Live pages have no frozen edition unless identified there. No complete-book review is implied. Rights and candidate implementation licenses are recorded in [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md).

| Source owner and work | Consulted source and read scope | Use |
| --- | --- | --- |
| ASD STEMG, ASD-STE100 | [FAQ](https://www.asd-ste100.org/STE_faq.html) and [downloads](https://www.asd-ste100.org/STE_downloads.html), complete public pages; Issue 9, January 2025 selected copyright/writing/counting passages subsequently read; exact PDF pages in [ASD metadata](../skills/asd-ste100/method.json); full dictionary unverified | Controlled English versus principles adoption; FAQ terminology/translation passages reread via direct HTTPS for consolidation; no new full-standard review |
| Andrej Karpathy, X post, 2026-10-02 | [Original](https://x.com/karpathy/status/2105819303471976479); full original post retrieved as public HTML; author/date corroborated through syndication; attached infographic visually inspected | Literal 80% prompting preference, not a compliance measure; exclude HTML/video from ASD scope |
| r/explainlikeimfive community rules | [Community page](https://www.reddit.com/r/explainlikeimfive/), rules 3–5 and 8 | Conventional layperson target versus the owner's explicit age-five adaptation |
| George Orwell, Politics and the English Language, April 1946 | [Estate-authorized Foundation reproduction](https://www.orwellfoundation.com/the-orwell-foundation/orwell/essays-and-other-works/politics-and-the-english-language/), essay and all six rules | Plain prose, qualifications, and the rule allowing exceptions |
| Springer, Graduate Texts in Mathematics | [Series 136](https://link.springer.com/series/136), description and ISSN metadata; no volume read | Series identity; distinguish the owner's original formal-explanation method |
| Barbara Minto, Pyramid Principle and SCQ | [Home](https://www.barbaraminto.com/), [concept](https://www.barbaraminto.com/concept), [course](https://www.barbaraminto.com/course), public pages; 1996 textbook identified, not read | Governing point, grouping, reader question; concept/course pages reread for consolidation; SCQ opening is now part of Minto |
| Apple, iPhone at ten, 2017-01-08 | [Official retrospective](https://www.apple.com/newsroom/2017/01/iphone-at-ten-the-revolution-continues.html), article | Observed presentation framing, not a universal Jobs rulebook |
| Stanford, Jobs commencement address, 2005 | [Prepared address](https://news.stanford.edu/stories/2005/06/youve-got-find-love-jobs-says), retrieved prepared-text passage | Story organization, not full keynote analysis |
| Steve Jobs Archive, Make Something Wonderful, 2023 | [Edited collection](https://book.stevejobsarchive.com/), editorial/copyright statements only | Collection scope and rights; not additional speech analysis |
| George Plimpton and Ernest Hemingway, The Art of Fiction No. 21, Spring 1958 | [Paris Review interview](https://www.theparisreview.org/interviews/4825/the-art-of-fiction-no-21-ernest-hemingway), omission/observation and revision exchanges | Historical source for the retired factual Hemingway adaptation; no book-wide claims |
| UNESCO and Republic of Korea, Hunminjeongeum nomination | [Record](https://www.unesco.org/en/memory-world/hunminjeongum-manuscript) and [nomination PDF](https://media.unesco.org/sites/default/files/webform/mow001/republic_of_korea_hunmin_chongum.pdf), pp. 3–5 and 11–12 | Historical document structure and a proposed explanatory adaptation; original manuscript not fully read |
| National Institute of Korean History, Sejong Annals, volume 113, 1446 lunar 9/29 | [Original and official Korean translation](https://sillok.history.go.kr/id/kda_12809029_004), royal foreword and opening of Jeong Inji foreword | Purpose-first Hunminjeongeum interpretation, with modern structure labeled adaptation |
| David Goodstein, Feynman's Lost Lecture excerpt, 1996 | [Caltech PDF](https://calteches.library.caltech.edu/563/2/Goodstein.pdf), anecdote on PDF p. 6; [1989 teacher-essay record](https://authors.library.caltech.edu/records/gqfj9-g9b59), metadata only | Firsthand freshman-lecture anecdote, not a verified child/grandmother quote |
| Scott Young, Learn Faster, 2011-09-01 | [Article](https://www.scotthyoung.com/blog/2011/09/01/learn-faster/), named-technique discussion | Modern Feynman Technique formulation |
| Scott Young, How Much Do You Understand, 2017-06-13 | [Article](https://www.scotthyoung.com/blog/2017/06/13/how-much-do-you-understand/), technique/depth sections | Limits of explanation as a test of problem-solving ability |
| Farnam Street, Feynman Technique | [Current formulation](https://fs.blog/feynman-technique/), procedural/audience discussion | Modern age-12 variant; not historical evidence |
| Aristotle, Prior Analytics, Jenkinson translation | [Book I](https://classics.mit.edu/Aristotle/prior.1.i.html), parts 1–4 | Premises, quantifiers, and syllogistic validity |
| Plato, Phaedrus, Jowett translation | [Text](https://classics.mit.edu/Plato/phaedrus.html), 229e–230a | Delphic inscription and self-knowledge attribution |
| Plato, Apology, Jowett translation | [Text](https://classics.mit.edu/Plato/apology.html), 21b–23b and 38a | Examination of claimed knowledge; depiction of Socrates |
| Kamprath, Adolphson, Mitamura, Nyberg, Controlled Language for Multilingual Document Production, CLAW 1998 | [Paper](https://aclanthology.org/www.mt-archive.info/90/CLAW-1998-Kamprath.pdf), sections 1–4 through [author-uploaded full text](https://www.researchgate.net/publication/2284766_Controlled_Language_for_Multilingual_Document_Production_Experience_with_Caterpillar_Technical_English) | Historical source for the retired CTE adaptation; not an internal/current Caterpillar manual |
| PLAIN/GSA, Federal Plain Language Guidelines | [Archived source](https://github.com/GSA/plainlanguage.gov/tree/fd7694740f19c0ed20ed71c2dd1dc92699e920fa), introduction/audience/short-sentence/usability pages and LICENSE; commit 2025-09-23 | Audience-centered guidance; full 2011 PDF body unread |
| GSA, Digital.gov plain language | [Current guide](https://digital.gov/guides/plain-language), scope notice/selected adapted material | Current selected adaptation versus full archive |
| Daniele Procida, Diátaxis | [Start here](https://diataxis.fr/start-here/), colophon, translation guidance, and [LICENSE.rst](https://github.com/evildmp/diataxis-documentation-framework/blob/957c09ca40b4a1edc23874f713e01937d50d54d5/LICENSE.rst); revision 957c09c, 2026-08-06 | Four documentation needs and upstream attribution/share-alike boundary |
| Richard Howard, Amazon narrative process, 2019-09-25 | [AWS article](https://aws.amazon.com/blogs/startups/startup-advice-how-to-write-a-narrative/), definition/start guidance/beginning of fictional example | Narrative decision documents and rendered six-page ceiling |
| AWS, Product Management at Amazon | [Working Backwards explanation](https://aws.amazon.com/executive-insights/content/product-management-at-amazon/), PRFAQ discussion | Distinguish PRFAQ from six-page narratives |
| NIST Research Library, Technical Series Publications Author Instructions | [Living instructions](https://www.nist.gov/nist-research-library/nist-technical-series-publications-author-instructions), organization/plain-language/accessibility/measurement sections; updated 2026-11-06 | Owner-selected source; distinguish portable guidance and agency procedures |
| NISTIR 8366, Guidance for NIST Staff on Using Inclusive Language in Documentary Standards | [Official PDF](https://nvlpubs.nist.gov/nistpubs/ir/2021/NIST.IR.8366.pdf), current withdrawal notice only; withdrawn 2025-02-20 | Exclude a narrower withdrawn document as current general author guidance |
| ICMJE, Recommendations, January 2026 | [Manuscript preparation](https://icmje.org/recommendations/browse/manuscript-preparation/preparing-for-submission.html), general principles/reporting guidelines/Introduction–Discussion; index update date | IMRaD and article-format exceptions |
| Flanagan and Ginoza, RFC 7322, September 2014 | [RFC](https://www.rfc-editor.org/rfc/rfc7322.html), philosophy/structure/requirements/references; [live editorial updates](https://www.rfc-editor.org/authors/rfc-style-guide/) through author-choice/XML guidance | RFC editorial structure; informational status and subsequent updates |
| Bradner, RFC 2119, March 1997 | [RFC](https://www.rfc-editor.org/rfc/rfc2119.html), BCP 14 requirement meanings | Normative force of requirement keywords |
| Leiba, RFC 8174, May 2017 | [RFC](https://www.rfc-editor.org/rfc/rfc8174.html), capitalization clarification | Distinguish uppercase BCP 14 words from ordinary prose |
| Malte Ubl, Design Docs at Google, 2020-07-06 | [Firsthand account](https://www.industrialempathy.com/posts/design-docs-at-google/), opening/anatomy/alternatives/review/conclusions | Project-appropriate design reasoning; not a compulsory Google template |
| Google, Documentation Best Practices | [Design-doc discussion](https://google.github.io/styleguide/docguide/best_practices.html) | Feedback proposals and decision archives |
| Google, Developer Documentation Style Guide | [Guide](https://developers.google.com/style), scope/hierarchy/rights only | Distinguish editorial style from design-document method |
| Microsoft, Writing Style Guide | [Welcome](https://learn.microsoft.com/en-us/style-guide/welcome/), [top ten](https://learn.microsoft.com/en-us/style-guide/top-10-tips-style-voice), [global writing](https://learn.microsoft.com/en-us/style-guide/global-communications/writing-tips), and archived source license | Living editorial guide, not older printed manual; page dates/read scope in assessment |
| Anne Waddingham, New Hart's Rules, second edition, OUP 2014 | [Publisher-origin preview](https://api.pageplace.de/preview/DT0400.9780191649134_A23591405/preview-9780191649134_A23591405.pdf), title/copyright/preface/contents/start of chapter 1; OUP catalog blocked | Edition identity and editorial scope; detailed rules not fully reviewed |

## Additional skill implementation references

Each project is recorded once below. All were accessed 2026-11-07; [comparison notes](INITIAL_CATALOG_RESEARCH.md#comparable-projects) identify exact files read, useful patterns, omissions, and whether license text was actually inspected. No implementation was adopted or run.

| Project | Inspected revision | Use |
| --- | --- | --- |
| [QingYunA/answer-me-with-html](https://github.com/QingYunA/answer-me-with-html) | 053619b917c6bf2e17eae5496d05eb08e10fe889 | HTML explanation and adapted STE modes |
| [anthropics/skills](https://github.com/anthropics/skills) | 2c5958ecac7cee2b583967a2c4981d0f4a75c579 | web-artifacts-builder only; artifact delivery |
| [mcollina/skills](https://github.com/mcollina/skills) | c75d70dbfbe991d8cec42aeda0b64ff14fbb9ac7 | Diátaxis documentation skill |
| [Jamfin92/skills](https://github.com/Jamfin92/skills) | 24314eaa5bc63db860f9ec4f41e9f179cfd1e9d4 | STE procedure/description split and rejected certainty-changing example |
| [ashryaagr/karpathy-output-style](https://github.com/ashryaagr/karpathy-output-style) | 4f6c5e974ad8a41fb2ffd628de2ed5271f0b5d88 | Principles versus conformance and secondary 80% interpretation |
| [danyuchn/asd-ste100-skill](https://github.com/danyuchn/asd-ste100-skill) | f38838aee0504fae07ef057667182a7c5af4ffe6 | Strict/flavored and structural/dictionary distinctions |
| [m4vic/socratic](https://github.com/m4vic/socratic) | 3cfaf6e73a8be29d4a8ed5ca80aa03a05f9aad7f | Modern self-questioning and stopping conditions |
| [aws-samples/sample-kiro-cli-prompts-for-product-teams](https://github.com/aws-samples/sample-kiro-cli-prompts-for-product-teams) | 1e1b3491465c2c0f742a92d0072a82454ec5ebb8 | PRFAQ comparison, separate from six-pager |
| [modeled-information-format/mif-docs-plugin](https://github.com/modeled-information-format/mif-docs-plugin) | 3e5725894db37568e41239745d79b2895b05ade0 | Google design-doc and NIST-inspired genre comparisons |
| [docwriter-org/plain-writing-skill](https://github.com/docwriter-org/plain-writing-skill) | f0d3630983ac7a82aa580f1c1509d72df739ee12 | Personal structure-first editing preferences |
| [tamdogood/builder-essential-skills](https://github.com/tamdogood/builder-essential-skills) | 1be9984bdafbb68eaff400bdd82773a1d41ee7ec | Orwell/STE combination contrast; full license notice unread |
| [sysmatt/ste-rules](https://github.com/sysmatt/ste-rules) | c18369e275a6873e09a417ac93219499190a2059 | Condensed STE summary, license unverified |
| [LeadGrowGTM/feynman-skill](https://github.com/LeadGrowGTM/feynman-skill) | Unrecorded; README only | Discovery reference; license claim unverified |

## Korean linguistic companion

National Institute of Korean Language. [쉬운 공문서 쓰기 길잡이](https://korean.go.kr/front/etcData/etcDataView.do?etc_seq=700&mn_id=208&pageIndex=1), 2022, official attachment last revised 2023-07-17; accessed 2026-11-07. Read item description and rights notice, foreword/contents, PDF/printed pp.8,12,15,21–23 visually, and extracted text pp.28–32. Other image-only pages were not reviewed. Informs the independently worded terminology, sentence agreement, and register adaptations in [korean-plain-language/method.json](../skills/korean-plain-language/method.json). Synthetic examples are original; no guide text, transformed examples, or page images are distributed. Its KOGL Type3 attribution/no-derivatives notice is recorded in [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md); independent native-language review is pending.

## Primary sources for the real-world examples

Consulted on 2026-11-08. These sources establish the facts of the writing tasks. Each comparison states what was consulted and which inputs are illustrative. The Luna exercises use these same sources with new worked quantities and decisions. For example, the Windows task uses the documented pinned-item exception and individual deletion control; the PostgreSQL task uses the index validity flag. Only links, facts and original descriptions are included; the sources retain their own terms.

| Comparison | Primary source |
| --- | --- |
| [amazon-six-page-narrative](../skills/amazon-six-page-narrative/examples/standard.md) | [NTSB, investigation HWY07MH024, Collapse of I-35W Highway Bridge, Minneapolis, Minnesota](https://www.ntsb.gov/investigations/Pages/HWY07MH024.aspx) |
| [answer-with-html](../skills/answer-with-html/examples/standard.md) | [NASA/JPL, Speaking Percy's Language: How to Talk so Perseverance Will Listen](https://science.nasa.gov/blog/speaking-percys-language-how-to-talk-so-perseverance-will-listen/) |
| [aristotle-syllogism](../skills/aristotle-syllogism/examples/standard.md) | [NASA, Why Do Eclipses Happen?](https://science.nasa.gov/eclipses/geometry/) · [NASA, 2023 Annular Eclipse FAQ](https://science.nasa.gov/eclipses/future-eclipses/eclipse-2023/faq/) |
| [asd-ste100](../skills/asd-ste100/examples/standard.md) | [Raspberry Pi, Raspberry Pi computer hardware documentation](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#reflash-the-bootloader) |
| [boring-professor](../skills/boring-professor/examples/standard.md) | [Linux man-pages 6.19, unlink(2)](https://man7.org/linux/man-pages/man2/unlink.2.html) |
| [diataxis](../skills/diataxis/examples/standard.md) | [Kubernetes command reference, kubectl rollout status](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_rollout/kubectl_rollout_status/) |
| [eli5](../skills/eli5/examples/standard.md) | [Monterey Bay Aquarium, Life of a rescued sea otter](https://www.montereybayaquarium.org/about-us/stories/life-of-a-rescued-sea-otter) · [Monterey Bay Aquarium, Sea otter](https://www.montereybayaquarium.org/animals-the-ocean/animals-a-to-z/sea-otter) |
| [federal-plain-language](../skills/federal-plain-language/examples/standard.md) | [SSA, U.S. Citizen/Child — Replacement Social Security Card (October 2026)](https://www.ssa.gov/pubs/EN-05-10514.pdf) |
| [feynman-technique](../skills/feynman-technique/examples/standard.md) | [IETF RFC 2308, Negative Caching of DNS Queries](https://www.rfc-editor.org/rfc/rfc2308.html#section-5) |
| [google-design-doc](../skills/google-design-doc/examples/standard.md) | [PostgreSQL 17 documentation, CREATE INDEX](https://www.postgresql.org/docs/17/sql-createindex.html#SQL-CREATEINDEX-CONCURRENTLY) · [PostgreSQL 17 system catalogs, pg_index](https://www.postgresql.org/docs/17/catalog-pg-index.html) |
| [gtm-formal](../skills/gtm-formal/examples/standard.md) | [Ongaro and Ousterhout, In Search of an Understandable Consensus Algorithm, §5.2](https://raft.github.io/raft.pdf) · [etcd v3.5 FAQ, fault tolerance](https://etcd.io/docs/v3.5/faq/#what-is-failure-tolerance) |
| [hunminjeongeum](../skills/hunminjeongeum/examples/standard.md) | [서울특별시, 시민의 발, 디자인을 입다…서울시, 지하철 노선도 40년 만에 변경 (2023-09-13)](https://news.seoul.go.kr/culture/archives/520933) |
| [ietf-rfc](../skills/ietf-rfc/examples/standard.md) | [IETF RFC 6585 §4, 429 Too Many Requests](https://www.rfc-editor.org/rfc/rfc6585.html#section-4) · [IETF RFC 9110 §10.2.3, Retry-After](https://www.rfc-editor.org/rfc/rfc9110.html#section-10.2.3) |
| [imrad](../skills/imrad/examples/standard.md) | [LIGO Scientific Collaboration and Virgo Collaboration, Observation of Gravitational Waves from a Binary Black Hole Merger (2016)](https://dcc.ligo.org/public/0122/P150914/014/LIGO-P150914_Detection_of_GW150914.pdf) |
| [korean-plain-language](../skills/korean-plain-language/examples/standard.md) | [서울특별시 내 손안에 서울, ‘월 5만원대’ 청년 맞춤형 기후동행카드 나온다 (2024-02-21)](https://mediahub.seoul.go.kr/archives/2010350) |
| [microsoft-writing-style](../skills/microsoft-writing-style/examples/standard.md) | [Microsoft Support, Using the clipboard](https://support.microsoft.com/en-us/windows/apps/using-the-clipboard) |
| [minto-pyramid](../skills/minto-pyramid/examples/standard.md) | [FHWA, Leading Pedestrian Interval](https://highways.dot.gov/safety/proven-safety-countermeasures/leading-pedestrian-interval) · [FHWA, Safety Evaluation of Protected Left-Turn Phasing and Leading Pedestrian Intervals on Pedestrian Safety (2018), FHWA-HRT-18-044](https://www.fhwa.dot.gov/publications/research/safety/18044/18044.pdf) |
| [new-harts-rules](../skills/new-harts-rules/examples/standard.md) | [Office for National Statistics, Housing, England and Wales: Census 2021 (5 January 2023)](https://www.ons.gov.uk/peoplepopulationandcommunity/housing/bulletins/housingenglandandwales/census2021) |
| [nist-technical-publication](../skills/nist-technical-publication/examples/standard.md) | [Heavner et al., First Accuracy Evaluation of NIST-F2, Metrologia (2014)](https://www.nist.gov/publications/first-accuracy-evaluation-nist-f2) |
| [orwell-six-rules](../skills/orwell-six-rules/examples/standard.md) | [Cornelius J. Dennehy / NASA, Best Practices for the Design, Development, and Operation of Robust and Reliable Space Vehicle Guidance, Navigation, and Control Systems (NASA/TP–20230005922, April 2023)](https://ntrs.nasa.gov/api/citations/20230005922/downloads/20230005922.pdf) |
| [socratic-self-questioning](../skills/socratic-self-questioning/examples/standard.md) | [Finnish Ministry of Social Affairs and Health and Kela, Results of the basic income experiment (6 May 2020)](https://valtioneuvosto.fi/en/-/1271139/perustulokokeilun-tulokset-tyollisyysvaikutukset-vahaisia-toimeentulo-ja-psyykkinen-terveys-koettiin-paremmaksi?languageId=en_US) |
| [steve-jobs-presentation](../skills/steve-jobs-presentation/examples/standard.md) | [NASA, NASA’s Ingenuity Mars Helicopter Succeeds in Historic First Flight (April 19, 2021)](https://www.nasa.gov/news-release/nasas-ingenuity-mars-helicopter-succeeds-in-historic-first-flight/) |

The inline examples also use the [Python lru_cache reference](https://docs.python.org/3/library/functools.html#functools.lru_cache), [RFC 8259 §§2–3](https://www.rfc-editor.org/rfc/rfc8259#section-3), the [Git branch deletion options](https://git-scm.com/docs/git-branch#Documentation/git-branch.txt--d), [NASA’s initial DART orbit estimate](https://www.nasa.gov/news-release/nasa-confirms-dart-mission-impact-changed-asteroids-motion-in-space/) and the [published NIST-4 measurement, equation 22 and table 1](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=923579). Read scopes and rights notes travel with the method metadata.
