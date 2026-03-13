# Implementation Plan: Operator Spacing Fix

## Phase 1: Prototyping (Mandatory)
- [ ] Task: Create prototyping script `temp/operator_spacing_proto.py`
    - [ ] Implement a standalone renderer that adds spaces to target operators.
    - [ ] Create multiple stylistic options (e.g., fixed vs. context-aware spacing).
    - [ ] Verify the prototype against "BAD" cases from `docs/operator_spacing.md`.
- [ ] Task: Conductor - User Manual Verification 'Phase 1: Prototyping' (Protocol in workflow.md)

## Phase 2: Implementation (TDD)
- [ ] Task: Write failing tests for operator spacing
    - [ ] Create `tests/test_operator_spacing.py`.
    - [ ] Add test cases for binary operators (`+`, `-`, `\times`, etc.).
    - [ ] Add test cases for relations (`=`, `\approx`, `\leq`, etc.).
- [ ] Task: Implement context-aware spacing in `src/renderer.py`
    - [ ] Identify `BinOpNode` and `RelNode` (or equivalent) in the parser.
    - [ ] Update `Renderer.render_node` to add spaces around these nodes.
    - [ ] Ensure spaces are ONLY added in appropriate contexts (e.g., between operands).
- [ ] Task: Verify all tests pass (including existing regression tests)
- [ ] Task: Conductor - User Manual Verification 'Phase 2: Implementation' (Protocol in workflow.md)

## Phase 3: Regression & Quality Assurance (Mandatory)
- [ ] Task: Update central regression test data in `tests/test_data.py`
    - [ ] Add new LaTeX strings and their expected visual grids to `CORE_TESTS`.
- [ ] Task: Verify project-wide code quality
    - [ ] Check coverage (>80%).
    - [ ] Run linting and type checks.
- [ ] Task: Conductor - User Manual Verification 'Phase 3: Regression & QA' (Protocol in workflow.md)
