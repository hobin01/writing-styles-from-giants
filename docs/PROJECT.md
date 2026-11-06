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

## Proposed delivery sequence and acceptance

1. **One complete method.** Create a real `skills/<method-id>/` with source/version, read scope, rights notes, stable rules, exceptions, per-level behavior, and reviewed en/ko adaptations. Add ordinary-use, important-exception, and meaning-preservation cases. Follow [METHOD_AUTHORING.md](METHOD_AUTHORING.md); extend existing checks with behavioral tests when catalog validation needs them.
2. **Observed writing behavior.** Verify explicit choice, opt-out, all levels, uncertain/conditional statements, and unavailable locales in a host. Record prompts, outputs, model/host versions, method/locale/level, failures, and judging process. Recommendations must explain fit and respect overrides; add a router only when real choices need one.
3. **Tested distribution.** Evaluate the existing [reuse candidates](../THIRD_PARTY_NOTICES.md) against [ARCHITECTURE.md](ARCHITECTURE.md). Verify complete references, scope, conflicts, durable link/copy behavior, modified files, shared roots, interrupted updates, and removal preservation. Publish installation instructions and support claims only for tested host/version/OS combinations; Windows needs its own evidence.
4. **Source release.** Resolve semantic and ownership failures, inspect archive rights/content, and follow [RELEASING.md](RELEASING.md) for the first `0.0.1` draft. Expand methods and host coverage from evidence.

The proposed initial mode is recommendation at `standard` level, with project-scoped installation. Method review, model evaluations, and host evidence are distinct from repository tests. Public CI requires no model keys; optional model evaluations use bounded cost and sanitized inputs.

## Current state

Present: documentation, authoring/evaluation examples, Python foundation checks, collaboration templates, ignore rules, and CI/draft-release workflow definitions. [Foundation CI has passed on GitHub](RELEASING.md).

Pending: production methods, recommendation/application workflow, installer integration, model evaluations, release workflow verification, host runtime tests, and repository protection settings. The examples are not production skills or model results.

## Boundaries

Reuse host capabilities and existing tools. A custom runtime, CLI, adapter, or plugin needs evidence of a gap first. No dashboard, paid service, remote content upload, model hosting, arbitrary plugin execution, person impersonation, authorship detector, or certified-STE claim is planned. STE-inspired work is a later candidate, with no verified ASD-STE100 compliance claim.
