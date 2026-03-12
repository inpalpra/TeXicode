# Track Specification: Overset, Underset, and Braces

## Goal
Implement support for LaTeX math commands that involve vertical stacking and horizontal braces, specifically `\overset`, `\underset`, `\overbrace`, `\underbrace`, `\stackrel`, `\xleftarrow`, and `\xrightarrow`.

## Requirements
- **Vertical Stacking:** `\overset`, `\underset`, and `\stackrel` must correctly stack children vertically using `util_vert_pile`.
- **Horizontal Braces:** `\overbrace` and `\underbrace` must generate horizontal braces spanning the content width and correctly stack the label.
- **Extensible Arrows:** `\xleftarrow` and `\xrightarrow` must stretch to fit the label width and stack label(s) correctly.
- **Strict Adherence:** Follow `docs/common-instructions.md` and `docs/features/03-overset-underset-braces.md`.
- **No `?` Fallback:** Fall back to raw LaTeX source if rendering is impossible, never use `?`.

## Reference Materials
- `docs/common-instructions.md`
- `docs/features/03-overset-underset-braces.md`
- `src/renderer.py`
- `src/node_data.py`
- `src/arts.py`
