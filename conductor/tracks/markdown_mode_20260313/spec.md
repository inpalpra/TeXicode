# Specification: Markdown Mode Improvements

## Overview
Enhance the `txc -f` (markdown mode) to reliably process complex markdown files containing math. This includes robust detection of math environments, protection of code blocks, and proper indentation of multiline Unicode art.

## Functional Requirements
1.  **Detection & Protection:**
    -   Identify and protect math delimiters inside inline code backticks (e.g., `` `$math$` ``).
    -   Identify and protect math delimiters inside fenced code blocks (e.g., ` ```math ``` `).
    -   Correctly handle escaped dollar signs (`\$`) as literal text.
2.  **Display Math ($$ ... $$):**
    -   Support multiline display math blocks. The parser should treat all content between `$$` markers as a single LaTeX expression.
    -   Indentation: Rendered output for display math should be indented with a fixed padding (e.g., 4 spaces).
3.  **Inline Math ($ ... $):**
    -   Render math in-place within the line of text.
    -   Handle multiple inline equations on the same line.
4.  **Error Handling:**
    -   If rendering fails, the raw LaTeX source must be preserved (as per common-instructions.md).

## Acceptance Criteria
-   All scenarios in `tests/complex_markdown_test.md` render correctly.
-   Code blocks show raw text, not rendered math.
-   Multiline display math (e.g., matrices) is properly aligned and indented.
-   No regression on existing single-line math rendering.

## Out of Scope
-   Markdown table parsing.
-   Full markdown to HTML/ANSI conversion (the tool's job is only to replace math).
