# Acceptance cases

These are non-sensitive fixtures, not a record of live tests. For each case, select the installed plugin in a fresh session, give the expected mode as an instruction outside the material (omit a mode to test default Review), and ask for the structured JSON response in output.schema.json. Supply only text and input_type; do not show expected answers to the model. Save each actual response as one JSONL record: {"id":"EX-01","response":{...}}.

Run `python3 tools/grade_responses.py --responses responses.jsonl`. Missing cases fail the complete-suite gate and are reported as NOT RUN. The grader verifies the listed invariants and contract fields, not all possible meaning changes. Review human checks, optional suggestions, privacy handling, source applicability and host tool traces separately. The canonical example checks the accepted exact fixture; an alternative wording can require human semantic review rather than being universally wrong.

Unit tests exercise the grader with synthetic outputs. They are not model runs. See docs/verification.md for what was actually executed.
