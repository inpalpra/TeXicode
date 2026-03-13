# Track: Spacing and Operators Spec

## Overview
This track implements missing LaTeX spacing commands and a wide range of mathematical operators to improve the quality of Unicode math rendering in TeXicode.

## Functional Requirements
### 1. Spacing Commands
- `\quad`: Render as 2 spaces.
- `\qquad`: Render as 4 spaces.
- `\,`: Render as thin space (1/3 or 1/4 of a space). Already works? Verify.
- `\;` and `\:`: Render as medium space (1 space).
- `\!`: Render as negative thin space.
- `\phantom{content}`: Render as invisible space with the exact width, height, and depth of the `content`.
- `\hspace{1em}`: Render as 2 fixed spaces. (Only fixed values like `{1em}` supported for now).

### 2. Mathematical Operators
Implement the following symbols:
- Arrows: `\implies` (⟹), `\iff` (⟺).
- Logical: `\therefore` (∴), `\because` (∵), `\forall` (∀), `\exists` (∃).
- Relations: `\approx` (≈), `\neq` (≠), `\ne` (≠), `\leq` (≤), `\le` (≤), `\geq` (≥), `\ge` (≥), `\ll` (≪), `\gg` (≫), `\subset` (⊂), `\supset` (⊃), `\subseteq` (⊆), `\supseteq` (⊇), `\in` (∈), `\notin` (∉).
- Operators: `\pm` (±), `\mp` (∓), `\times` (×), `\div` (÷), `\cdot` (·), `\circ` (∘), `\star` (⋆), `\dagger` (†), `\ddagger` (‡).
- Analysis/Calculus: `\nabla` (∇), `\partial` (∂), `\infty` (∞).
- Dots: `\ldots` (…), `\cdots` (⋯), `\vdots` (⋮), `\ddots` (⋱).

## Acceptance Criteria
- All listed spacing commands correctly modify the horizontal layout without crashing.
- `\phantom{x}` takes up the same space as `x` but shows no characters.
- All listed operators render their corresponding Unicode symbols when used in a TeX string.
- Existing tests and basic rendering commands (like `\frac`, `\sum`) still work correctly.

## Out of Scope
- Support for arbitrary `\hspace` units (e.g., `10pt`, `5cm`).
- Advanced kerning or sub-pixel character positioning.