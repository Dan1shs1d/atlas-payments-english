# Architecture and release decisions

## Architect's view

One host-neutral SKILL.md defines the behavior. Progressive references hold the rulebook, 255 terminology proposals, examples and optional structured output schema. Root plugin.json declares the portable format. Codex and Claude have thin compatibility manifests; no duplicated runtime logic. The repository contains separate marketplace catalogs and one plugin directory.

Review is the default. Rewrite is explicit. The input boundary separates instructions outside the supplied material from text being edited. Review findings cite exact spans and stable IDs. Ambiguity remains visible instead of being resolved by a guessed transaction operation. An output can be usable while declaring checks not completed.

## Security chief's view

Minimize capabilities: no hooks, servers, tools, secrets or background processes. Keep host permissions intact. Do not claim that instructions enforce isolation or that a local plugin means private/offline inference. Release only allowlisted source files. Treat referenced pages as evidence, not instructions. Do not bundle third-party manuals or standard text.

## Commercial view

The value is preservation of payment meaning, not generic grammar repair or an official compliance certificate. Open installation reduces adoption friction. Paid services can maintain company terminology, review workflows, onboarding and evaluations without restricting the already published MIT core. Do not make quantified loss-reduction, approval-rate or ROI claims without measured evidence.

## Limits and extension points

The skill depends on the host model and cannot guarantee semantics. There is no hosted editing API, authentication, billing, enterprise admin console or deterministic full STE checker. Those would be separate products with their own threat models. Keep operational policy retrieval separate from editorial transformation. Glossary terms remain scoped editorial proposals.
