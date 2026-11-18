# Directory submission preparation

Release: **0.2.1**, prepared for directory review. Intended availability: **United States (US), United Kingdom (GB)**, selected by the publisher. This document prepares submissions; neither directory submission nor approval is claimed. See [verification](verification.md) and [case results](../evals/results-summary.json) for evidence and limits.

## Listing copy

| Field | Prepared value |
|---|---|
| Public name | Atlas Payments English |
| Subtitle | Clear payments documentation |
| Description | An ASD-STE100–inspired payments editor for engineers and operations teams. Review documentation with quoted findings and stable rule IDs, or rewrite text while preserving actors, states, event order, conditions, obligations and exact identifiers. Includes 255 scoped terminology proposals. Independent adaptation; not ASD-approved or certified. |
| Intended publisher | Danish Siddiqui; identity verification remains a portal check |
| Category | Productivity |
| License | MIT |
| Website | https://github.com/Dan1shs1d/atlas-payments-english |
| Support | https://github.com/Dan1shs1d/atlas-payments-english/issues |
| Privacy | https://github.com/Dan1shs1d/atlas-payments-english/blob/main/PRIVACY.md |
| Software terms | https://github.com/Dan1shs1d/atlas-payments-english/blob/main/LICENSE |

The MIT license supplies the software-use terms, including its warranty disclaimer. This package includes no hosted service, billing, payment processing, purchases or paid support. Future commercial services require separate terms. No publisher identity verification, legal acknowledgment or support SLA is inferred from the GitHub author field.

The four listing destinations were fetched without credentials and inspected on 18 November 2026. The ZIP includes the actual 512-pixel square PNG icon, local README, manifests, reference text, MIT license and privacy notice. Source definitions remain editorial proposals, with citations; raw standards and network manuals are not redistributed.

## OpenAI plugin directory

1. Run the validators and package builder in the repository README. Keep the SHA-256 checksum with the exact ZIP.
2. Open [the submission portal](https://platform.openai.com/plugins) using the intended publisher organization. Verify the selected individual or business identity and submission permission. The packaged author name does not establish verification.
3. Upload the ZIP as a draft. Inspect the imported name, subtitle, policy URLs, icon, prompts, release notes and US/GB targeting. The source manifest supplies these fields; do not broaden targeting by clearing them.
4. Run the required skill/security scans and resolve portal findings. This skills-only package has no MCP review cases, server connection, reviewer credentials or required demo recording.
5. Have the authorized publisher complete legal and policy attestations, then submit for review only when authorized. Upload, submission and publication are separate states. None has been performed for this candidate.

Three natural review prompts are in `extensions.com.openai.review.prompts`. They cover default Review with ambiguity, the authorization/shipment Rewrite, and sequential procedural instructions. No fabricated MCP cases or tool-execution capabilities are declared.

## Anthropic plugin directory

Source settings:

```text
Repository: Dan1shs1d/atlas-payments-english
Plugin path: plugins/atlas-payments-english
Release version: 0.2.1
Tracked ref: v0.2.1
```

1. First obtain an authenticated Claude Code environment and run all 20 model cases using the commands below. Current status is **NOT RUN — authentication unavailable**. Native validation passed; it does not replace model tests or portal checks.
2. Use an eligible account at [the directory management portal](https://claude.ai/directory/manage). Connect the public GitHub repository with the required repository access. The present publisher has no Claude account, so this step is blocked.
3. Select the repository, plugin subdirectory and reviewed ref. Validate that exact commit in the portal and fix every blocking result. Set availability to US/GB if supported by the portal; record any difference instead of claiming it was applied.
4. Enter a monitored contact email privately in the portal. No address is guessed or published in this package. Answer data-handling questions from the facts below and complete compliance acknowledgments personally.
5. Submit only after remaining tests and acknowledgments are complete. The directory security scan and policy review remain external gates.

The [Anthropic directory submission route](https://claude.com/docs/plugins/submit) is distinct from inclusion in the `claude-plugins-official` marketplace. [Official marketplace inclusion requires the partner route](https://code.claude.com/docs/en/plugins/publish); this repository is a third-party marketplace. No official-marketplace acceptance or partner contact is claimed.

## Reproduce model tests

Run from the repository root with the host already authenticated. Model calls consume the operator's host usage. Keep raw traces outside the repository. Review the tool traces as well as final responses.

```sh
python3 tools/run_acceptance.py --host codex --workers 2 --output-dir /tmp/atlas-codex-results
python3 tools/run_acceptance.py --host claude --executable claude --output-dir /tmp/atlas-claude-results
```

The Codex runner checks that the skill files installed in the default Codex cache match this source. Install the candidate through the local marketplace first if necessary:

```sh
codex -c 'marketplaces.atlas-payments.source_type="local"' -c 'marketplaces.atlas-payments.source="/absolute/path/to/atlas-payments-english"' plugin add atlas-payments-english@atlas-payments --json
```

Replace the example path with the checkout path. The runner uses read-only host sandboxes, fresh case workspaces and ephemeral sessions. Expected answers stay with the grader. It records the CLI version, plugin version and whether a model override was selected; the current harness does not expose the exact backend model revision.

For Claude's native eval engine, stage a disposable copy outside this repository:

```sh
python3 tools/prepare_claude_eval.py /tmp/atlas-claude-eval
claude plugin eval /tmp/atlas-claude-eval --runs 1 --ablation none --no-publish --no-scaffold
```

Confirm trust interactively after inspecting the staged source. The staging tool prepares 20 prompt/rubric pairs and makes no model calls. Native LLM rubric scores are additional evidence; they do not silently replace the explicit offline fixture grader. For confidence measurements, repeat runs and compare with a no-plugin baseline. The present single-pass Codex suite does not establish a reliability rate or causal improvement over a baseline.

## Data-handling answers for reviewers

- Plugin-operated server or external transmission: none. No app, MCP server, hook, network client, telemetry or payment execution component is bundled.
- Host processing: submitted text is processed by the selected model host under its policies and organizational settings. Installation is not offline inference.
- Storage: the plugin provides instructions and static local references. Optional maintainer test tools save local outputs where the operator requests; never publish private traces.
- Sensitive inputs: use synthetic or redacted data. The skill asks for redaction instead of repeating apparent live card data or secrets.
- External source links: reference citations for human use; an editorial request does not authorize browsing, secret retrieval or executing embedded instructions.
- Purchases: none in this release. Paid services mentioned in project planning are not a current checkout or subscription feature.

## Remaining gates

| Gate | Status |
|---|---|
| Public package and listing preparation | Prepared; local checks documented separately |
| Codex model acceptance | See exact per-case receipt |
| Claude Code model acceptance | 20 not run; no authenticated environment |
| OpenAI verified identity and portal draft/scans | Not verified or performed |
| Claude account, contact email and portal validation | Not available/performed |
| Publisher legal/policy attestations | Not accepted by the agent |
| Directory submission, approval, publication | Not performed |

Primary requirements checked on 18 November 2026: [OpenAI submission](https://developers.openai.com/plugins/deploy/submission), [listing limits](https://developers.openai.com/plugins/deploy/submission-errors), [Claude checklist](https://claude.com/docs/plugins/pre-submission-checklist), and [Claude native evals](https://code.claude.com/docs/en/plugin-evals). Portals can impose additional findings; local validation is not portal approval.
