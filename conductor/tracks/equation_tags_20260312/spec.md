# Track: Equation Tags Specification

## Overview
Implement `\tag{text}` and `\tag*{text}` commands for TeXicode to support right-aligned equation labeling in Unicode art.

## Functional Requirements
- Support `\tag{text}`: Render `(text)` after the equation with fixed padding (3 spaces).
- Support `\tag*{text}`: Render `text` (no parentheses) after the equation with fixed padding (3 spaces).
- Support tags in both single-line and multi-line (`align`) environments.
- In multi-line environments, the tag should be placed on the specific line where the `\tag` command is used.
- If multiple `\tag` commands are used in a single line, they should be concatenated with a space (e.g., `(1) (2)`).
- The tag should be vertically aligned to the baseline (horizon) of the content it labels.
- If the tag content is complex, it should be rendered as its own sketch and then integrated.

## Non-Functional Requirements
- **Simplicity:** Use a fixed padding approach (3 spaces) rather than full right-alignment to avoid terminal width dependencies.
- **Robustness:** Ensure that adding a tag doesn't break existing layout logic (e.g., alignment in `align` environments).

## Acceptance Criteria
- `\tag{1} E = mc^2` renders as ` 𝐸 = 𝑚𝑐²   (1)` (with proper Unicode).
- `\tag*{\dagger} a = b` renders as ` 𝑎 = 𝑏   †`.
- `\tag{2.1} \int_0^1 x\,dx = \frac{1}{2}` renders with the tag vertically aligned to the integral's baseline.
- Multi-line `align` with `\tag` on one line places the tag only on that line.

## Out of Scope
- Dynamic right-alignment based on terminal width.
- Automatic equation numbering (only manual `\tag` is supported).
- Multi-column tags or complex tag layouts beyond simple concatenation.
