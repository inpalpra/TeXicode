# Plan: Spacing and Operators

## Phase 1: Prototyping and Verification of Operators
- [ ] Task: Prototyping in `temp/`
    - [ ] Create `temp/prototype_operators.py` to test current support for the listed operators.
    - [ ] Create `temp/prototype_spacing.py` to test current support for spacing commands.
    - [ ] For any operators/spacing commands not working, identify the necessary Unicode characters.
    - [ ] Perform visual A/B testing for spacing widths (e.g., `\quad` = 2 vs. 3 spaces).
    - [ ] Present stylistic options to the user for approval.
- [ ] Task: Conductor - User Manual Verification 'Phase 1' (Protocol in workflow.md)

## Phase 2: Implementation of Mathematical Operators
- [ ] Task: Define operator symbols in `src/arts.py` and `src/node_data.py`.
    - [ ] Add entries for `\implies`, `\iff`, etc. to the appropriate symbol mapping tables.
    - [ ] Ensure that `\ne` is an alias for `\neq`, `\le` for `\leq`, etc.
- [ ] Task: Write tests for operators in `tests/test_operators.py`.
    - [ ] Create failing tests for new operators.
- [ ] Task: Verify that all new operators render correctly.
- [ ] Task: Conductor - User Manual Verification 'Phase 2' (Protocol in workflow.md)

## Phase 3: Implementation of Spacing Commands
- [ ] Task: Register spacing nodes in `src/node_data.py`.
- [ ] Task: Implement `render_spacing` in `src/renderer.py` for `\quad`, `\qquad`, `\hspace`, etc.
- [ ] Task: Write tests for spacing commands in `tests/test_spacing.py`.
    - [ ] Create failing tests for new spacing commands.
- [ ] Task: Verify spacing widths and alignment.
- [ ] Task: Conductor - User Manual Verification 'Phase 3' (Protocol in workflow.md)

## Phase 4: Implementation of `\phantom`
- [ ] Task: Register `cmd_phantom` node in `src/node_data.py`.
- [ ] Task: Implement `render_phantom` in `src/renderer.py`.
    - [ ] Render child to a sketch.
    - [ ] Replace all non-background characters with background characters (spaces).
- [ ] Task: Write tests for `\phantom` in `tests/test_phantom.py`.
    - [ ] Create failing tests.
- [ ] Task: Verify that `\phantom` correctly reserves space without rendering content.
- [ ] Task: Conductor - User Manual Verification 'Phase 4' (Protocol in workflow.md)

## Phase 5: Regression and Final Verification
- [ ] Task: Update `tests/test_data.py` with the new test cases.
- [ ] Task: Run the full regression test suite (`run_tests.py` and `pytest`).
- [ ] Task: Final verification of all listed commands in the feature document.
- [ ] Task: Conductor - User Manual Verification 'Phase 5' (Protocol in workflow.md)