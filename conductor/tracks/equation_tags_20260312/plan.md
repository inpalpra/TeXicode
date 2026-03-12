# Implementation Plan - Equation Tags

## Phase 1: Prototype & Style Selection [checkpoint: 648e6f4]
- [x] Task: Create prototype script in `temp/` to explore `\tag` rendering options. (ee9fc4c)
- [x] Task: Generate multiple stylistic options for tag padding and parentheses. (ee9fc4c)
- [x] Task: Present options to user and get approval for the preferred style. (ee9fc4c)
- [x] Task: Conductor - User Manual Verification 'Phase 1: Prototype & Style Selection' (Protocol in workflow.md) (648e6f4)

## Phase 2: Setup & Testing (Red Phase) [checkpoint: 9960c6f]
- [x] Task: Register `\tag` and `\tag*` nodes in `src/node_data.py`. (f15827d)
- [x] Task: Create `tests/test_tag.py` with failing tests for all acceptance criteria. (d244780)
- [x] Task: Verify that tests fail as expected. (d244780)
- [x] Task: Conductor - User Manual Verification 'Phase 2: Setup & Testing (Red Phase)' (Protocol in workflow.md) (9960c6f)

## Phase 3: Implementation (AST Pre-processing Strategy) [checkpoint: b6fcdc1]
- [x] Task: Implement `preprocess_ast_for_tags(nodes)` in `src/renderer.py` to reorder tags to the end of lines.
- [x] Task: Integrate `preprocess_ast_for_tags` into the `render` function.
- [x] Task: Implement `render_tag` in `src/renderer.py` with 3-space padding and automatic parentheses.
- [x] Task: Adjust `tests/test_data.py` to match the finalized rendering output (no leading spaces).
- [x] Task: Verify that all tests in `tests/test_tag.py` pass.
- [x] Task: Conductor - User Manual Verification 'Phase 3: Implementation' (Protocol in workflow.md)

## Phase 4: Refinement & Regression Testing
- [ ] Task: Verify code coverage for new changes (>80%).
- [ ] Task: Run full regression suite (`run_tests.py` and `pytest`).
- [ ] Task: Verify that all existing features still work (no regressions).
- [ ] Task: Conductor - User Manual Verification 'Phase 4: Refinement & Regression Testing' (Protocol in workflow.md)
