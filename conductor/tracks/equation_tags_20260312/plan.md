# Implementation Plan - Equation Tags

## Phase 1: Prototype & Style Selection [checkpoint: 648e6f4]
- [x] Task: Create prototype script in `temp/` to explore `\tag` rendering options. (ee9fc4c)
- [x] Task: Generate multiple stylistic options for tag padding and parentheses. (ee9fc4c)
- [x] Task: Present options to user and get approval for the preferred style. (ee9fc4c)
- [x] Task: Conductor - User Manual Verification 'Phase 1: Prototype & Style Selection' (Protocol in workflow.md) (648e6f4)

## Phase 2: Setup & Testing (Red Phase)
- [ ] Task: Register `\tag` and `\tag*` nodes in `src/node_data.py`.
- [ ] Task: Create `tests/test_tag.py` with failing tests for all acceptance criteria.
- [ ] Task: Verify that tests fail as expected.
- [ ] Task: Conductor - User Manual Verification 'Phase 2: Setup & Testing (Red Phase)' (Protocol in workflow.md)

## Phase 3: Implementation (Green Phase)
- [ ] Task: Implement `render_tag` in `src/renderer.py`.
- [ ] Task: Update `util_concat` or horizontal joining logic to handle the fixed padding for tags.
- [ ] Task: Ensure tags work correctly in `align` and `align*` environments (per-line placement).
- [ ] Task: Verify that all tests in `tests/test_tag.py` pass.
- [ ] Task: Conductor - User Manual Verification 'Phase 3: Implementation (Green Phase)' (Protocol in workflow.md)

## Phase 4: Refinement & Regression Testing
- [ ] Task: Refactor `render_tag` and related logic for clarity.
- [ ] Task: Verify code coverage for new changes (>80%).
- [ ] Task: Update `tests/test_data.py` with new equation tag test cases.
- [ ] Task: Run full regression suite (`run_tests.py` and `pytest`).
- [ ] Task: Verify that all existing features still work (no regressions).
- [ ] Task: Conductor - User Manual Verification 'Phase 4: Refinement & Regression Testing' (Protocol in workflow.md)
