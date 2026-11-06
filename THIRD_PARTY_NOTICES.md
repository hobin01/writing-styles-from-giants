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
