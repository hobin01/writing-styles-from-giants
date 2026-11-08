# Project definition

## Purpose and requirements

Make documented writing and explanation methods usable as AI-agent skills. The [README](../README.md) records the founder's motivation and initial candidates.

- Draw from thinkers, historical figures, books, companies, and institutions, with source evidence and attribution.
- Respect explicit method choice, recommendation requests, opt-out, and selected application scope.
- Provide `light`, `standard`, and `strict` levels without changing facts or qualifications.
- Start with English/Korean adaptations and target the six hosts in [COMPATIBILITY.md](COMPATIBILITY.md).
- Evaluate existing installers for an `npx`-style, project/global delivery path before writing one.
- Use MIT for original content and reuse vetted permissive implementations under the [license policy](../THIRD_PARTY_NOTICES.md).

The repository is private during solo development before stable `0.0.1`, but every commit must be suitable for eventual public release. Follow [CONTRIBUTING.md](../CONTRIBUTING.md) for branch/commit/PR handling and [SECURITY.md](../SECURITY.md) for local history, credentials, caches, and cleanup.

## Delivery sequence and acceptance

1. **Complete method content.** Maintain a real `skills/<method-id>/` with source/version, read scope, rights notes, stable rules, exceptions, per-level behavior, and applicable language rules. English-first instructions and the Korean companion follow the owner’s policy. Add ordinary-use, important-exception, and meaning-preservation cases. Follow [METHOD_AUTHORING.md](METHOD_AUTHORING.md); extend existing checks with behavioral tests when catalog validation needs them.
2. **Observed writing behavior.** Verify explicit choice, opt-out, all levels, uncertain/conditional statements, and unavailable locales in a host. Record prompts, outputs, model/host versions, method/locale/level, failures, and judging process. Recommendations must explain fit and respect overrides; add a router only when real choices need one.
3. **Tested distribution.** Evaluate the existing [reuse candidates](../THIRD_PARTY_NOTICES.md) against [ARCHITECTURE.md](ARCHITECTURE.md). Verify complete references, scope, conflicts, durable link/copy behavior, modified files, shared roots, interrupted updates, and removal preservation. Publish installation instructions and support claims only for tested host/version/OS combinations; Windows needs its own evidence.
4. **Source release.** Resolve semantic and ownership failures, inspect archive rights/content, and follow [RELEASING.md](RELEASING.md) for the first `0.0.1` draft. Expand methods and host coverage from evidence.

The checkout commands default to `standard` on each writing request. Automatic selection is explicit. Method review, model evaluations, and host evidence are distinct from repository tests. Public CI requires no model keys; optional model evaluations use bounded cost and sanitized inputs.

## Current state

Present: 21 experimental methods plus a Korean-specific linguistic companion, source-to-rule metadata, per-level policies, ordinary/exception/meaning-preservation cases, per-skill Ponytail review, and catalog validation with behavioral unit tests. [CATALOG_CONSOLIDATION.md](CATALOG_CONSOLIDATION.md) records three overlap removals, retained distinctions, and migration. [CATALOG_REVIEW.md](CATALOG_REVIEW.md) preserves the initial manual-loading model exercises as historical evidence, separate from verification of the consolidated versions. Existing foundation documentation, CI, and release definitions remain.

All 22 entrypoints now include authored examples. The [four paired writing trials](../evals/runs/2026-11-08-worked-examples.md) preserve outputs, including a failed check and fresh runs after a revision. The HTML example also has a rendered keyboard and no-script check.

The [WSG commands](../commands/WSG.md) expose explicit selection, automatic matching and bilingual help. The [English](../EXAMPLES.md) and [Korean](../EXAMPLES.ko.md) galleries contain GPT-6 Luna’s independent baseline and standard answers to 22 problems designed for high-school reasoning or above, with separate assessments for each language. The [preceding evaluation](https://github.com/hobin01/writing-styles-from-giants/blob/06f7e14e4b9f1e1081e817d7f828278def138742/EXAMPLES.md) preserves the first-pass results and developmental retests. See [host verification](COMPATIBILITY.md) for tested discovery and invocation paths.

Pending: installer lifecycle integration, independent native-language and reader review, repeated comparative evaluations, release workflow verification, and repository protection settings. All methods retain experimental status.

## Boundaries

Reuse host capabilities and existing tools. A custom runtime, CLI, adapter, or plugin needs evidence of a gap first. No dashboard, paid service, remote content upload, model hosting, arbitrary plugin execution, person impersonation, authorship detector, or certified-STE claim is planned. The ASD profile is STE-inspired; full ASD-STE100 compliance remains unverified.
