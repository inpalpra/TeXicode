# Implementation Plan: Markdown Mode Improvements

## Phase 1: Prototyping & Verification (temp/) [checkpoint: 0c79604]
- [x] Task: Create a prototype script `temp/markdown_mode_proto.py` to test regex-based or manual parsing of markdown for math. 82d564e
- [x] Task: Implement a state machine in the prototype to handle:
    - Escaped `\$`.
    - Inline code backticks.
    - Fenced code blocks.
    - Multiline `$$` blocks. 049afe4
- [x] Task: Test the prototype against `tests/complex_markdown_test.md` and verify all scenarios are correctly identified and replaced. 1de919f
- [x] Task: Conductor - User Manual Verification 'Prototyping' (Protocol in workflow.md) 0c79604

## Phase 2: Implementation (src/) [checkpoint: a2e24ad]
- [x] Task: Update `src/main.py` or `src/pipeline.py` to integrate the improved markdown parsing logic. a2e24ad
- [x] Task: Ensure that display math output is indented with a fixed (e.g., 4 spaces) padding. a2e24ad
- [x] Task: Verify that error handling falls back to raw LaTeX when rendering fails. a2e24ad
- [x] Task: Conductor - User Manual Verification 'Implementation' (Protocol in workflow.md) a2e24ad


## Phase 3: Regression Testing & Finalization
- [~] Task: Run `run_tests.py` and ensure no regressions.
- [ ] Task: Run `txc -f tests/complex_markdown_test.md` and verify the final terminal output visually.
- [ ] Task: Conductor - User Manual Verification 'Regression Testing' (Protocol in workflow.md)
