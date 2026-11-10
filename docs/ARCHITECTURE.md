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

The checkout installer can link each selected host’s `skills/wsg` directory to the checkout’s `.agents/skills/wsg` adapter. The adapter follows its real path to read the command guide and methods from the checkout; user inputs and outputs belong to the caller’s project. Keep the clone at the same path for the life of these links.

Copy installation stages the entrypoint, command guide, method directories and rights notices from the checkout or source ZIP. The wheel and dedicated offline ZIP contain that same payload. An installed copy resolves references inside its own directory.

In an interactive terminal, omitting `--host` lists the supported CLI names found on PATH. The user selects the destinations. Explicit `--host` values work independently of detection. Project scope is the default; `--global` selects user scope. A multi-host operation checks all selected destinations for conflicts before writing. Completed installs can be reused on retry. The installer preserves other copies, symlinks and unrelated files. [Host-specific instructions](COMPATIBILITY.md)
