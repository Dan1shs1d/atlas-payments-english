# Acceptance cases

These are non-sensitive fixtures, not a record of live tests. For each case, select the installed plugin in a fresh session, give the expected mode as an instruction outside the material (omit a mode to test default Review), and ask for the structured JSON response in output.schema.json. Supply only text and input_type; do not show expected answers to the model. Save each actual response as one JSONL record: {"id":"EX-01","response":{...}}.

Run `python3 tools/grade_responses.py --responses responses.jsonl`. Missing cases fail the complete-suite gate and are reported as NOT RUN. The grader verifies the listed invariants and contract fields, not all possible meaning changes. Review human checks, optional suggestions, privacy handling, source applicability and host tool traces separately. The canonical example checks the accepted exact fixture; an alternative wording can require human semantic review rather than being universally wrong.

Unit tests exercise the grader with synthetic outputs. They are not model runs. See docs/verification.md for what was actually executed.

## Live host runners

`tools/run_acceptance.py` invokes the actual authenticated host CLI in a fresh workspace for each case. No expected answers are included in case prompts. It saves private raw traces and final responses in an explicit output directory. It does not acquire credentials. Run `python3 tools/run_acceptance.py --help` for options. The Codex cache must contain the candidate installed from this local marketplace; the runner verifies every shared skill file against source before testing.

`tools/prepare_claude_eval.py` stages the same 20 cases as native Claude prompt/rubric files in a new external directory. Staging and strict plugin validation make no model calls. See [submission instructions](../docs/directory-submission.md) for authenticated test commands.

Semantic pattern checks accept “greater than,” “more than,” and “exceeds,” and case changes caused by sentence movement. Exact identifiers, amounts and explicit modal words remain protected. Inclusive boundaries, missing negation and reversed events have negative regression tests. This is a finite fixture grader, not a general semantic-equivalence proof.

For EX-10, “only after the customer has returned the goods” preserves the necessary completed-return condition in this specific sentence. The fixture accepts that phrase as well as “only if”; removing “only” fails. This is not permission to replace conditionals with temporal language generally. EX-16 requires clarification of amount, currency, start event and calendar/business-day basis; a deadline-only question fails.
