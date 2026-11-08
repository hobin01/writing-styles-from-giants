# Architecture and behavior contracts

The experimental catalog works from this checkout. One project command chooses and loads a portable method; the host model performs the writing. See [the command contract](../commands/WSG.md), [verified host surfaces](COMPATIBILITY.md) and [project scope](PROJECT.md).

## Portable content

The complete `skills/<method-id>/` directory is the distribution unit:

```text
skills/<method-id>/
  SKILL.md
  method.json
  locales/en.json          # canonical English rule wording for most methods
  cases.json               # synthetic observable expectations
```

`SKILL.md` owns discovery and concise agent steps. `method.json` owns intent, sources, applicability, stable rule IDs, and level policies. Locale records own rule wording, measurements, and justified linguistic adaptations. Only the Korean companion requires `locales/ko.json`; an English-written language-independent rule does not need a Korean clone. Include references/scripts only when needed; host metadata stays outside the portable core. The [templates](../templates/method/) are authoring examples; [skills](../skills/) contains the experimental implementations. Each skill directory is self-contained, including its evidence and cases.

Use the host's model and existing installers/validators from the [reuse review](../THIRD_PARTY_NOTICES.md). Add custom runtime, adapters, categories, or plugins only for a demonstrated gap. Extend the Python foundation checks for project-specific rules rather than duplicating a standard-format validator.

## Selection

Inputs are purpose, genre, audience, output language, optional method/level, and `recommend | auto | off`. Ask only for missing information that changes the choice; otherwise disclose assumptions.

Codex exposes one project-local entrypoint, `$wsg`. A method ID selects a method explicitly, `auto` selects a method by the request, and `docs` shows the English or Korean catalog. Slash-capable adapters forward their command spellings to the same contract. The dispatcher reads method instructions and applicable references; comparison outputs are for readers browsing examples.

1. `off` disables this project's method application, not host/system instructions.
2. Explicit selection wins. Explain incompatibility rather than silently substituting a method.
3. Compare documented applicability and locale availability. Start with a short skill workflow; use deterministic suitability tags if a scripted router becomes necessary. Do not invent catalog facts.
4. Recommend one fit with reasons and limitations. Start with one method; combine only explicitly compatible methods when needed. Record conflicts as exceptions or choices.
5. Auto mode applies within selected scope; it grants no file-writing permission or global instruction changes.

Audit output records method/version, locale, level, assumptions, fit, skipped rules, and unresolved checks. Keep it out of finished prose unless requested. Explicit application does not require a separate audit; automatic selection must expose at least the method and level in a status or audit view.

## Levels

| Level | Guideline behavior |
| --- | --- |
| `light` | Named high-value subset; preserve existing voice; advisory findings |
| `standard` | Ordinary applicable guidelines; explain relevant exceptions |
| `strict` | Full eligible profile; run available checks and account for unresolved applicable rules |

Meaning-preservation invariants and justified exceptions apply at every level. Selected skills default to `standard` without a level; ASD `normal` is an alias for `standard`. Its 80%/100% descriptions are intensity labels, not scores. Use hard errors only for reliably checkable violations. Unverified checks stay unverified; strictness is neither a compliance percentage nor official certification. Numeric readability limits require locale-specific evidence under [LOCALIZATION.md](LOCALIZATION.md).

Explicit choices work without configuration files. If persistent settings become necessary, proposed precedence is request/CLI, nearest project settings, user settings, then defaults. Follow output language when locale is unspecified; reject unsupported values, expose host discovery conflicts, and never persist inferred preferences or search unrelated parent/private files. Arbitrary command hooks are excluded.

## Installation and host trust

Evaluate an existing installer against these requirements before publishing commands or support claims:

- Default to project scope. Detect candidates, then select targets; preview roots, hosts, methods, versions, and link/copy changes. Incomplete noninteractive requests fail without writing.
- Retain complete directories in durable versioned storage before linking; never leave lasting links into an ephemeral `npx` cache.
- Deduplicate shared destinations and reject paths escaping selected roots or traversing into unrelated locations.
- Repeated installation is idempotent. Preserve unrelated paths, modified copies, and unexpected links; replacement needs a concrete choice. Disclose copy fallback and record hashes when symlinks are unavailable.
- Record owned paths, versions, link targets or hashes, and shared ownership without document text or credentials. Validate updates before switching, retain the previous version on failure, and preserve shared destinations during removal.
- Remove only owned, unchanged installation content; never recursively delete a user skill root.

Verify discovery, invocation, references, and lifecycle behavior for each host/version/OS under [COMPATIBILITY.md](COMPATIBILITY.md). Portable skills, plugins, hooks, and MCP integrations are separate capabilities. Installation must not execute third-party scripts, edit credentials, enable services, or append global instructions as a side effect. Any future remote service needs its own data-handling contract.
