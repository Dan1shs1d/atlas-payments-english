# Verification and release scope

Public release: 0.2.1, 18 November 2026. Neither directory submission nor approval is claimed.

## Executed checks

| Check | Result | Evidence scope |
|---|---|---|
| Codex model acceptance | **20/20 passed** | One genuine host run per fixture; final answers and tool traces reviewed |
| Claude Code model acceptance | **0 run; 20 not run** | No authenticated account or alternative provider; no Claude model results inferred |
| Python regression/unit tests | 27 passed | Packaging and grader regressions using synthetic responses; separate from model tests |
| Release boundary and manifest checks | Passed | Selected identity, metadata, reference, privacy and containment constraints |
| Skill Creator validator | Passed | Frontmatter and scaffold checks |
| Claude Code strict plugin and marketplace validation | Passed | Version 2.1.327, no warnings or advice on final source |
| Deterministic archive and inventory | Passed | Allowlisted 15-file ZIP, 67,693 bytes, 512×512 PNG icon |
| Four public listing destinations | Passed | Unauthenticated HTTP fetch and content inspection on 18 November 2026 |
| Portal scans, policy review and publisher verification | Not performed | External directory gates remain |

## Actual model evidence

See the [per-case receipt](../evals/results-summary.json) and [actual synthetic-fixture responses](../evals/codex-responses-0.2.1.jsonl). Raw traces remain private because they include local paths and host context. The receipt includes their hashes, the source hashes and the CLI version.

Codex CLI: 0.167.0-alpha.4.1. Final run: 19:16:18–19:18:17 UTC on 18 November 2026. The host default model was used with no explicit override; the exact backend model revision was not exposed by this harness. Tests ran in fresh, read-only, ephemeral host workspaces using the actually installed candidate skill. The runner verified the installed skill files against source. Only the source text and requested mode/purpose were supplied; expected answers stayed with the grader. The central example also exists legitimately among the plugin's shipped examples, so this is a regression suite, not a held-out benchmark.

Manual review confirmed preservation of actors, conditions, states, event order, identifiers and modal words across these fixtures. EX-09 only read/searched local plugin references; no link fetch, secret retrieval, upload or source-command execution was observed. EX-16 asked for amount, currency, deadline start event, day basis and timezone when material. No MCP or web tool calls were observed in the final suite.

## Failures corrected

Earlier iterations are recorded in the receipt. An explicit “must not” became an imperative prohibition; the skill now preserves the modal wording. Manual review found a refund clarification that asked about days but missed amount/currency; the skill and grader now check both. Overly literal grading also rejected valid equivalents such as “exceeds,” “more than,” sentence-initial “After”/“No,” and the necessary completed-return condition expressed with “only after.” Narrow fixture patterns accept those forms while negative regression tests still reject inclusive boundaries, lost negation, omitted necessary conditions and reversed event order.

The final suite was rerun after both skill fixes. Failed intermediate runs were not silently reported as successful model runs. A final passing run is not a measured reliability rate, a claim that earlier runs always passed, or evidence that the plugin outperforms a no-plugin baseline.

## Claude and directory limits

The genuine Claude Code binary reported loggedIn=false and authMethod=none. The publisher confirmed no Claude account. Twenty native prompt/rubric fixtures can be staged with `tools/prepare_claude_eval.py`; staging and strict validation did not run a model. Complete all 20 Claude cases in an authenticated environment before calling cross-host acceptance complete.

See the [directory preparation guide](directory-submission.md). The package supplies listing fields, policy links, prompts, release notes and US/GB targeting. The authorized publisher must still complete portal identity checks, scans, contact details and acknowledgments. Anthropic's directory route differs from its official marketplace partner route. No review approval, listing or publication is implied by a valid ZIP.

## Adoption limits

This finite regression suite does not establish exhaustive ASD-STE100 Issue 9 conformance, source currency, network authorization, legal correctness, security certification or accuracy over all 255 terminology records. Review consequential edits with a domain owner and validate applicable source editions. Repeat meaningful tests after rule, glossary, model or host changes. The package is an editorial aid; a passing format check is not operational approval.
