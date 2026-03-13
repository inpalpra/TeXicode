# Plan: Spacing and Operators

## Phase 1: Prototyping and Verification of Operators
- [x] Task: Prototyping in `temp/`
    - [x] Create `temp/prototype_operators.py` to test current support for the listed operators.
    - [x] Create `temp/prototype_spacing.py` to test current support for spacing commands.
    - [x] For any operators/spacing commands not working, identify the necessary Unicode characters.
    - [x] Perform visual A/B testing for spacing widths (e.g., `\quad` = 2 vs. 3 spaces).
    - [x] Present stylistic options to the user for approval.
- [x] Task: Conductor - User Manual Verification 'Phase 1' (Protocol in workflow.md)

## Phase 2: Implementation of Mathematical Operators
- [x] Task: Define operator symbols in `src/arts.py` and `src/node_data.py`.
    - [x] Add entries for `\implies`, `\iff`, etc. to the appropriate symbol mapping tables.
    - [x] Ensure that `\ne` is an alias for `\neq`, `\le` for `\leq`, etc.
- [x] Task: Write tests for operators in `tests/test_operators.py`.
    - [x] Create failing tests for new operators.
- [x] Task: Verify that all new operators render correctly.
- [x] Task: Conductor - User Manual Verification 'Phase 2' (Protocol in workflow.md)

## Phase 3: Implementation of Spacing Commands
- [x] Task: Register spacing nodes in `src/node_data.py`.
- [x] Task: Implement `render_spacing` in `src/renderer.py` for `\quad`, `\qquad`, `\hspace`, etc.
- [x] Task: Write tests for spacing commands in `tests/test_spacing.py`.
    - [x] Create failing tests for new spacing commands.
- [x] Task: Verify spacing widths and alignment.
- [x] Task: Conductor - User Manual Verification 'Phase 3' (Protocol in workflow.md)

## Phase 4: Implementation of `\phantom`
- [x] Task: Register `cmd_phantom` node in `src/node_data.py`.
- [x] Task: Implement `render_phantom` in `src/renderer.py`.
    - [x] Render child to a sketch.
    - [x] Replace all non-background characters with background characters (spaces).
- [x] Task: Write tests for `\phantom` in `tests/test_phantom.py`.
    - [x] Create failing tests.
- [x] Task: Verify that `\phantom` correctly reserves space without rendering content.
- [x] Task: Conductor - User Manual Verification 'Phase 4' (Protocol in workflow.md)

## Phase 5: Regression and Final Verification
- [x] Task: Update `tests/test_data.py` with the new test cases.
- [x] Task: Run the full regression test suite (`run_tests.py` and `pytest`).
- [x] Task: Final verification of all listed commands in the feature document.
- [x] Task: Conductor - User Manual Verification 'Phase 5' (Protocol in workflow.md)