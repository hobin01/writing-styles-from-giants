# Project decisions

## Releases

The first public release is v0.1.0. uv installs the WSG tool from the versioned GitHub Release wheel. The tool installs skills in project scope by default and requires an explicit choice for user-wide installation. Maintainers publish tags under the [release procedure](RELEASING.md).

## Method selection

The user can select a method, request automatic matching or opt out for a single request. Each writing request defaults to `standard`, and the catalog defaults to English. Host adapters share one [command contract](../commands/WSG.md).

## Catalog and attribution

- Attribute documented practices and identify project-original methods. The ASD-inspired profile uses `normal` as an alias for `standard`. Its `strict` level applies the full eligible project profile. Official ASD-STE100 conformity remains unverified. [ASD evidence and scope](../skills/asd-ste100/method.json)
- Keep method instructions primarily in English. Add a separate language-specific skill when the language calls for different rules or measurements. [Language policy](LOCALIZATION.md)
- Retain Minto for SCQA openings, ASD for the controlled-English editing task, and Orwell for the factual prose editing task previously represented by Hemingway. The pre-release catalog migration records retired IDs and the preserved cases. [Migration](CATALOG_CONSOLIDATION.md)
- Publish matched questions and independently generated answers for all three levels in English and Korean. The three comparisons for one method and language share a control answer. [Gallery procedure](METHOD_AUTHORING.md#publish-a-gallery-example)
- License original project content under MIT and keep source-specific rights with each method. [Third-party rights](../THIRD_PARTY_NOTICES.md) · [Bibliography](REFERENCE.md)
