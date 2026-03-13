# Specification: Operator Spacing Audit (spec.md)

**Overview:**
Audit and document the current spacing around mathematical operators in TeXicode's Unicode output. This investigation will run the existing test suite (`run_tests.py`), analyze the rendered results, and tabulate the findings in `docs/operator_spacing.md` to identify areas where operator spacing can be improved for better visual balance.

**Functional Requirements:**
1.  **Execute Audit:** Run `./run_tests.py` (or a similar script that processes all core and alignment tests) to capture the rendered output of all test cases.
2.  **Analyze Spacing:** For each rendered output, identify common binary operators (`=`, `+`, `-`, `\times`, etc.) and broader TeX operators (`\sum`, `\int`, `\cdot`, etc.).
3.  **Evaluate Visual Balance:** Rate the spacing around each operator as "GOOD" or "BAD" based on the presence and consistency of space characters (U+0020) surrounding the operator glyphs.
4.  **Tabulate Findings:** Create a new document `docs/operator_spacing.md` containing a table with:
    -   **LaTeX String:** The original input expression.
    -   **Rendered Output:** The Unicode grid (art) produced by the renderer.
    -   **Rating:** "GOOD" or "BAD".
    -   **Justification:** A brief explanation of why the spacing was rated as such (e.g., "Missing space after '='", "Properly balanced '+'").

**Non-Functional Requirements:**
-   **Clarity:** The report should be easy to read and provide a clear overview of the current state of operator spacing.
-   **Reproducibility:** The audit should be based on the actual output of the `run_tests.py` script.

**Acceptance Criteria:**
-   `docs/operator_spacing.md` exists and contains a table of findings.
-   The table includes all relevant test cases from the core suite that contain operators.
-   Each entry in the table has a rating and a justification.

**Out of Scope:**
-   Implementing the fix for the spacing issues. This is purely an audit and documentation track.
-   Automating the detection of spacing in code (it will be a manual analysis based on the test output).
