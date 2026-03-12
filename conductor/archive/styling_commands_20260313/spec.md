# Specification: Styling Commands (color, boxed, cancel)

## Overview
Implement LaTeX styling commands in TeXicode to allow for visual modifications like framing, coloring, and striking through text in the terminal.

## Functional Requirements
- **`\boxed{content}`**: Draw a Unicode box around the content using standard box-drawing characters (`┌`, `┐`, `└`, `┘`, `─`, `│`).
- **`\color{name}{content}`** and **`\textcolor{name}{content}`**: Apply ANSI terminal colors (if enabled). Supports standard 8 ANSI colors (red, blue, green, etc.).
- **`\cancel{content}`** and **`\bcancel{content}`**: Strikethrough using the combining character U+0336 on each non-space character.
- **`\colorbox{name}{content}`**: Apply ANSI background colors.
- **`\fcolorbox{border}{bg}{content}`**: Draw a box and apply a background color.

## Non-Functional Requirements
- **Graceful Fallback**: If color mode is disabled (no `-c` flag) or an invalid color name is provided, the styling should be ignored silently, and the content rendered normally.
- **Nesting**: Styling commands should support nesting (e.g., `\color{red}{A \color{blue}{B} C}`).
- **Performance**: Styling should not significantly impact rendering time.

## Acceptance Criteria
- `\boxed{\frac{a}{b}}` renders with a correctly sized box.
- `\color{red}{x}` renders `x` in red if `-c` is used, and just `x` otherwise.
- `\cancel{x}` renders as `x` with a strike-through.
- `\colorbox{yellow}{x^2}` applies a yellow background in color mode.
- `\fcolorbox{red}{blue}{x}` renders a red box with a blue background.
- Existing features (fractions, sums, integrals) are NOT broken by these additions.

## Out of Scope
- Support for arbitrary hex/RGB colors (unless easily supported by terminal ANSI).
- Complex `\cancel` variants (like diagonal lines crossing multiple rows) that cannot be represented by simple combining characters.
