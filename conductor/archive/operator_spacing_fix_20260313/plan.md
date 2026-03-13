# Implementation Plan: Operator Spacing Fix

## Phase 1: Prototyping (Mandatory)
- [x] Task: Create prototyping script `temp/operator_spacing_proto.py`
    - [x] Implement a standalone renderer that adds spaces to target operators.
    - [x] Create multiple stylistic options (e.g., fixed vs. context-aware spacing).
    - [x] Verify the prototype against "BAD" cases from `docs/operator_spacing.md`.
- [x] Task: Conductor - User Manual Verification 'Phase 1: Prototyping' (Protocol in workflow.md)

## Phase 2: Implementation (TDD)
- [x] Task: Write failing tests for operator spacing
    - [x] Create `tests/test_operator_spacing.py`.
    - [x] Add test cases for binary operators (`+`, `-`, `\times`, etc.).
    - [x] Add test cases for relations (`=`, `\approx`, `\leq`, etc.).
- [x] Task: Implement context-aware spacing in `src/renderer.py`
    - [x] Identify `BinOpNode` and `RelNode` (or equivalent) in the parser.
    - [x] Update `Renderer.render_node` to add spaces around these nodes.
    - [x] Ensure spaces are ONLY added in appropriate contexts (e.g., between operands).
- [x] Task: Verify all tests pass (including existing regression tests)
- [x] Task: Conductor - User Manual Verification 'Phase 2: Implementation' (Protocol in workflow.md)

## Phase 3: Regression & Quality Assurance (Mandatory)
- [x] Task: Update central regression test data in `tests/test_data.py`
    - [x] Add new LaTeX strings and their expected visual grids to `CORE_TESTS`.
- [x] Task: Verify project-wide code quality
    - [x] Check coverage (>80%).
    - [x] Run linting and type checks.
- [x] Task: Conductor - User Manual Verification 'Phase 3: Regression & QA' (Protocol in workflow.md)
