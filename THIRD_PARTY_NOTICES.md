# License and reuse policy

Original project code and documentation are [MIT licensed](LICENSE), as chosen by the owner. Reuse existing implementations before writing equivalents.

## Allowed reuse

- Prefer MIT and Apache-2.0 components after checking the exact version, relevant files, and dependencies. Other permissive licenses need the same review.
- Preserve upstream copyright, license text, and required notices. Apache-2.0 reuse also requires change notices on modified files and applicable upstream NOTICE attributions. Third-party files retain their licenses; the project's MIT license does not replace them.
- Do not copy, vendor, or ship GPL/AGPL-covered code, or other material whose terms would prevent this project's MIT distribution. Unknown licensing is not permission to reuse.
- Record actual reuse here with upstream/version, files, license, required notices, and modifications. Preserve those notices in source and release archives.

See the original [MIT terms](https://opensource.org/license/mit) and [Apache-2.0 redistribution conditions](https://www.apache.org/licenses/LICENSE-2.0#redistribution).

## License-checked reuse candidates

License/README review only; these are not installed dependencies or runtime compatibility claims.

| Project and inspected revision | License evidence | Intended use and limit |
| --- | --- | --- |
| [vercel-labs/skills, d3701c1](https://github.com/vercel-labs/skills/tree/d3701c11b1101251af14c9d148f026e1a47ebe17) | [MIT](https://github.com/vercel-labs/skills/blob/d3701c11b1101251af14c9d148f026e1a47ebe17/LICENSE) | First installer candidate; verify complete references, scope, conflicts, update/removal, and host behavior before adoption |
| [agentskills/agentskills, 83021e2](https://github.com/agentskills/agentskills/tree/83021e2be457a9b6679148719c1f6074f0ad975e) | [Apache-2.0](https://github.com/agentskills/agentskills/blob/83021e2be457a9b6679148719c1f6074f0ad975e/LICENSE) for code; [CC BY 4.0](https://github.com/agentskills/agentskills/blob/83021e2be457a9b6679148719c1f6074f0ad975e/README.md#license) for documentation, subject to directory-specific notices | Format/validation reference; [skills-ref](https://github.com/agentskills/agentskills/blob/83021e2be457a9b6679148719c1f6074f0ad975e/skills-ref/README.md) explicitly says it is demonstration-only, not a production dependency |
| [mattpocock/skills, 4ae2317](https://github.com/mattpocock/skills/tree/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d) | [MIT](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/LICENSE) | Repository organization and contributor guidance; see [REFERENCE.md](docs/REFERENCE.md) |

No upstream implementation is currently bundled. The foundation checker validates this project's public-file boundary and authoring examples; it does not replace a standard-format validator.

## Writing-method sources

Candidates include [Orwell's essay](https://www.orwellfoundation.com/the-orwell-foundation/orwell/essays-and-other-works/politics-and-the-english-language/), [GSA Plain Language materials](https://github.com/GSA/plainlanguage.gov), and [Barbara Minto's site](https://www.barbaraminto.com/). These links establish neither reuse permission nor completed source review.

Books, standards, dictionaries, quotations, images, and linked references keep their own rights. An upstream code license does not relicense its sources. Author original operational summaries, attribute adaptations, and resolve rights before bundling external material. The template rules are project-original examples. Names identify sources and targets without implying endorsement or affiliation.


## Initial catalog research and additional candidates

The [initial assessment](docs/INITIAL_CATALOG_RESEARCH.md) and [bibliography](docs/REFERENCE.md#initial-catalog-research-sources) record original summaries and links, not redistributed source documents or adopted implementations. The following license texts were inspected on 2026-11-07 at the listed revisions. These are reference candidates only; before copying files, review their file-specific notices, referenced sources, assets, and dependencies and record the actual reuse here.

| Candidate and revision | Inspected license evidence | Scope |
| --- | --- | --- |
| QingYunA/answer-me-with-html, 053619b | [MIT](https://github.com/QingYunA/answer-me-with-html/blob/053619b917c6bf2e17eae5496d05eb08e10fe889/LICENSE) | README and skill reference; no CLI/assets copied; repository rights do not relicense ASD material or embedded fonts |
| anthropics/skills web-artifacts-builder, 2c5958e | [Skill-specific Apache-2.0](https://github.com/anthropics/skills/blob/2c5958ecac7cee2b583967a2c4981d0f4a75c579/skills/web-artifacts-builder/LICENSE.txt) | This skill's license only; no blanket license assertion for all Anthropic skills |
| mcollina/skills, c75d70d | [MIT](https://github.com/mcollina/skills/blob/c75d70dbfbe991d8cec42aeda0b64ff14fbb9ac7/LICENSE) | Documentation skill reference; upstream Diátaxis text has separate terms |
| ashryaagr/karpathy-output-style, 4f6c5e9 | [MIT](https://github.com/ashryaagr/karpathy-output-style/blob/4f6c5e974ad8a41fb2ffd628de2ed5271f0b5d88/LICENSE) | README/selected STE reference, not rights to the official standard or social-media content |
| danyuchn/asd-ste100-skill, f38838a | [MIT](https://github.com/danyuchn/asd-ste100-skill/blob/f38838aee0504fae07ef057667182a7c5af4ffe6/LICENSE) | Skill-reference comparison; underlying standard rights remain separate |
| m4vic/socratic, 3cfaf6e | [MIT](https://github.com/m4vic/socratic/blob/3cfaf6e73a8be29d4a8ed5ca80aa03a05f9aad7f/LICENSE) | README and skill; no question packs or cited books reviewed for reuse |
| AWS product-team prompts, 1e1b349 | [MIT-0](https://github.com/aws-samples/sample-kiro-cli-prompts-for-product-teams/blob/1e1b3491465c2c0f742a92d0072a82454ec5ebb8/LICENSE) | PRFAQ sample/reference only; no external Amazon content bundled |
| MIF documentation plugin, 3e57258 | [MIT](https://github.com/modeled-information-format/mif-docs-plugin/blob/3e5725894db37568e41239745d79b2895b05ade0/LICENSE) | google-design-doc and nist-sp skills as comparisons; no dependency/schema adoption |
| docwriter-org/plain-writing-skill, f0d3630 | [MIT](https://github.com/docwriter-org/plain-writing-skill/blob/f0d3630983ac7a82aa580f1c1509d72df739ee12/LICENSE) | Personal editing preferences, not official Federal guidance |

No reuse permission was established for Jamfin92/skills, sysmatt/ste-rules, or LeadGrowGTM/feynman-skill. Tamdogood's license endpoint reported MIT, but the full notice text was not read. These remain reference-only sources.

### Underlying method sources

- **ASD-STE100:** official public FAQ/download notices were read; Selected Issue 9 copyright/writing/counting passages were subsequently read during implementation (exact pages in `skills/asd-ste100/method.json`); the complete rule set and dictionary remain unverified. The standard/dictionary is not bundled. A candidate implementation's MIT license cannot authorize its redistribution or establish conformity.
- **Federal Plain Language archive:** [GSA license](https://github.com/GSA/plainlanguage.gov/blob/fd7694740f19c0ed20ed71c2dd1dc92699e920fa/LICENSE.md) states US public-domain status and a worldwide CC0 dedication. Check third-party content separately before copying.
- **Diátaxis:** [upstream CC BY-SA 4.0](https://github.com/evildmp/diataxis-documentation-framework/blob/957c09ca40b4a1edc23874f713e01937d50d54d5/LICENSE.rst). Its text, translations, and diagrams must not be imported and relabeled MIT. No licensed expression was copied; future reuse needs an explicit license record.
- **Microsoft:** archived [documentation license](https://github.com/MicrosoftDocs/microsoft-style-guide/blob/c6945c32294e845a84b192a094fb1b7c2c452a6a/LICENSE) identifies CC BY 4.0; current Learn pages and code have their own applicable notices. The archived license's heading/start was inspected, not every condition.
- **Google:** the inspected Developers style page identifies CC BY 4.0 text and Apache-2.0 code. This does not cover Malte Ubl's separate article. No Google or Ubl prose/templates were copied.
- **RFCs:** document rights follow their IETF Trust/BCP 78 notices. Code-component provisions are not a blanket MIT license for RFC prose. No RFC boilerplate or document text is bundled.
- **Other historical and book-based candidates:** no permissive redistribution rights were established for the inspected Orwell reproduction, Minto materials, Jobs speeches/archive, Hemingway interview, CTE paper/manuals, New Hart's Rules, or Feynman sources. Ancient originals, modern translations, photographs, and institutional website prose have separate rights. Use original operational summaries with source attribution; review any proposed excerpts or assets before distribution.

## Initial implementation rights

All skill instructions, operational summaries, metadata, and synthetic cases are newly written project content under MIT. No upstream skill implementation, standard, dictionary, book passage, speech, diagram, translation, or proprietary checklist is bundled. Source names identify the documented practice and do not imply affiliation or certification. Detailed source and read-scope records travel inside each skill’s `method.json`.

The Korean companion consults NIKL’s [2022 guide](https://korean.go.kr/front/etcData/etcDataView.do?etc_seq=700&mn_id=208&pageIndex=1), whose item-specific notice is KOGL Type3 (attribution/no derivatives). The project supplies independently worded language principles and original synthetic examples; it does not redistribute or translate the guide’s expression, substitution tables, or page images. Further reuse requires checking that notice; the project MIT license cannot grant rights to the source.
