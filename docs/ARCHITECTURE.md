# Architecture and behavior contracts

Status: proposed, not an implemented API. Read [PROJECT.md](PROJECT.md) first.

## Content and delivery

Future canonical content lives in `skills/<method-id>/`. The entire directory is the portable unit:

```text
skills/<method-id>/
  SKILL.md
  method.json
  locales/en.json
  locales/ko.json
```

`SKILL.md` owns discovery and the short workflow; it references method data instead of duplicating every rule. `method.json` owns language-independent intent, provenance, applicability, rule IDs, and level policies. Locale files own wording, measurement units, and justified deviations. Optional references/scripts are added only when needed. Host-specific metadata stays in adapters or generated bundles.

The [authoring examples](../templates/method/) demonstrate this shape outside the production catalog. They are not installed automatically.

Portable Markdown/JSON content does not need a dedicated product runtime. Start with one real method, the host agent's model, and an evaluation of existing skill installers. Extend the current Python checks when catalog validation is needed. A custom CLI, router runtime, or host adapter is a later proposal only if an observed requirement cannot be met by the existing delivery path. Choose its runtime then; do not scaffold a package in advance.

The repository structure follows the [reference review](REFERENCE.md). A flat `skills/<method-id>/` catalog is sufficient until actual methods justify categories. Plugin manifests are added only for a tested plugin delivery path.

## Selection

Inputs: task purpose, genre, audience, output language, optional selected method, level, and `recommend | auto | off` mode. Only ask for missing context when it materially changes the selection; otherwise disclose a reasonable assumption.

1. `off` disables this project's style application, not host/system instructions.
2. An explicit method selection wins over automatic ranking, subject to compatibility reporting.
3. Filter by applicable task and locale availability, then compare documented purpose. A short host-executed skill workflow can do this first; if a scripted router becomes necessary, use deterministic suitability tags. A model explanation must not fabricate catalog facts.
4. Recommend one best fit with an explanation; offer an alternative when genuinely useful. Do not load the whole catalog.
5. Auto mode applies the selected eligible method within the selected request/project scope. It does not grant file-writing permission or modify global agent instructions.
6. Start with one method. Add an explicitly compatible structural method only when the task needs it. Conflicting rules produce a recorded exception or a choice, not silent averaging.

Selection/audit output records method version, locale variant, level, assumptions, selection reason, skipped rules, and unresolved checks. Keep this visible without inserting implementation metadata into the user's finished prose unless requested.

## Levels and exceptions

| Level | Guideline behavior |
| --- | --- |
| `light` | Apply the high-value subset named by the method; preserve the existing voice; advisory findings |
| `standard` | Apply all ordinary applicable guidelines; suggest changes and explain relevant exceptions |
| `strict` | Apply the full eligible profile; run available checks and account for each unresolved applicable rule |

Semantic invariants apply at every level. A guideline's own justified exception remains valid at `strict`. Hard errors are permitted for reliably checkable violations, not an uncalibrated subjective style score. An unverified requirement is `unverified`, not passed. Strictness is not a percentage of compliance, and it does not turn an adaptation into an official standard.

No numeric readability limit is a global default. A locale-specific limit needs a defined counting method, source or project rationale, and evaluation evidence. See [LOCALIZATION.md](LOCALIZATION.md).

## Configuration

Explicit request choices work without a configuration file. If persistent project configuration or a custom CLI is needed, the proposed precedence is: explicit request/CLI options, nearest project configuration, user configuration, documented defaults. Project-root discovery stops at the chosen repository root; do not read unrelated parent/private files.

Proposed project file: `writing-styles-from-giants.json`. Proposed global file: platform user config directory under `writing-styles-from-giants/config.json`, resolved by the installer. These paths follow the project name; no configuration loader exists yet. Fields start with `schemaVersion`, `mode`, `level`, `locale`, and `method`; no arbitrary command hooks. Locale follows output language when unspecified. Unsupported values fail with a readable error. No automatic persistence of an inferred preference.

This would govern this project's selection settings, not the host's own skill discovery. Verify native precedence for the actual host/version and report conflicts rather than promising to override it.

## Installation contract

Evaluate an existing installer first. Record its version and evidence for the requirements below; expose unsupported behavior and do not claim a supported delivery path before testing it. If a custom CLI is justified, `install`, `list`, `doctor`, `update`, and `uninstall` are possible operations, not currently available commands.

- `install` defaults to project scope. Detection proposes candidates using known paths and host signals; it does not install into every found folder without target selection. Explicit noninteractive targets are supported later.
- Preview resolved roots, target host/surface, method set, scope, storage version, and link/copy changes. In noninteractive use, missing necessary choices fail without writing.
- Materialize complete, versioned skill directories in a durable data directory before linking. Never point a lasting symlink into an `npx` temporary cache.
- Deduplicate aliases/shared paths by resolved destination. Reject paths escaping the selected install roots and symlink traversal into unrelated locations.
- A same installation is idempotent. An unrelated existing path is a conflict. A modified copy or unexpected link is preserved and reported; replacing it requires a concrete user choice.
- If symlinks are unsupported, offer an explicit copy fallback and record its hashes. Do not silently switch behavior.
- An installation manifest records installed version, scope, roots, owned paths, expected link targets or copy hashes, and shared ownership. It contains no document text or credentials.
- Stage and validate updates before switching. A failed update leaves the previous version available. Removing one adapter must not break a shared path used by another.
- Uninstall removes only paths matching the ownership record and current content. Modified/unowned paths remain. Never recursively delete a user skill root.

## Plugins and trust

Portable skills, host plugin bundles, lifecycle hooks, and MCP integrations are distinct capabilities. Add wrappers after a host smoke test proves discovery and application. A host may ignore unknown frontmatter or use different invocation semantics.

The installer must not execute third-party skill scripts, write credential settings, enable network services, or append global instructions as a side effect of installing content. Any later remote service is a separately documented feature with explicit data handling.
