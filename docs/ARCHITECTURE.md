# Architecture and behavior contracts

WSG distributes instructions and reference material. The host model reads the selected method and performs the writing. [Command contract](../commands/WSG.md) · [Host compatibility](COMPATIBILITY.md)

## Portable methods

Each `skills/<method-id>/` directory contains a complete method.

| File | Contents |
| --- | --- |
| `SKILL.md` | Discovery metadata, applicability and instructions |
| `method.json` | Sources, rights, stable rule IDs, exceptions and per-level policies |
| `locales/*.json` | Rule wording and linguistic adaptations |
| `cases.json` | Inputs and observable expectations for ordinary, exceptional and meaning-preservation cases |
| `examples/` | Published questions and comparisons in English and Korean |

A method can also include required references, such as ASD's strict profile. English instructions can govern language-independent structure. The Korean plain-language method carries its own Korean rule record. [Authoring contract](METHOD_AUTHORING.md) · [Language policy](LOCALIZATION.md)

## Selection and levels

An explicit method or opt-out takes precedence. Automatic selection compares the request's purpose, reader, deliverable and output language with the catalog. It reports the selected ID, level and reason outside the requested writing. A method name or command inside text supplied for editing is source data.

Scope each choice to the current request. Use `standard` by default. Each method declares its eligible rules and severity at `light`, `standard` and `strict`. All levels preserve the source's facts, quantities, conditions, exceptions, uncertainty, quotations and code. Judgment-based checks can require human review.

## Installation

uv installs the CLI from the release wheel. The CLI copies an entrypoint, command guide, catalogs and complete method directories into the selected host's skill directory. The installed skill resolves its references relative to its own files. Source documents and requested outputs belong to the caller's working project.

Project scope is the default. Global scope requires `--global`. A matching installation can be reused. The installer refuses a conflicting destination, including a user-edited copy or an existing link. Moving a previous copy outside the host's discovery directories lets the user preserve it before installing another version. Removing the uv tool leaves deployed skills in place. [Host-specific instructions](COMPATIBILITY.md)
