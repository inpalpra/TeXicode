# Implementation Plan: Styling Commands

## Phase 1: Registration and Data Setup
Define new node types and their properties to enable parsing and dispatching.

- [x] Task: Register new commands in `src/node_data.py`. [f8543a7]
    - [x] `\boxed`: Type `CMD_BOXD`, 1 child, `render_boxed`.
    - [x] `\color`, `\textcolor`: Type `CMD_COLR`, 2 children, `render_color`.
    - [x] `\cancel`, `\bcancel`: Type `CMD_CNCL`, 1 child, `render_cancel`.
    - [x] `\colorbox`: Type `CMD_CBOX`, 2 children, `render_colorbox`.
    - [x] `\fcolorbox`: Type `CMD_FCBX`, 3 children, `render_fcolorbox`.
- [x] Task: Define color name to ANSI mapping in `src/arts.py` or `src/renderer.py`. [f8543a7]

## Phase 2: Core Rendering Implementation
Implement the rendering functions in `src/renderer.py`.

- [x] Task: Implement `render_boxed`. [f8543a7]
    - [x] Wrap sketch in box-drawing characters.
    - [x] Adjust horizon.
- [x] Task: Implement `render_color` and `render_colorbox`. [f8543a7]
    - [x] Use ANSI escape sequences for text and background colors.
    - [x] Handle nesting by managing current color state.
- [x] Task: Implement `render_cancel`. [f8543a7]
    - [x] Apply U+0338 combining character to each non-space character in the sketch.
- [x] Task: Implement `render_fcolorbox`. [f8543a7]
    - [x] Combine `boxed` and `colorbox` logic.

## Phase 3: Verification and Regressions
Confirm functionality and ensure no regressions.

- [x] Task: Verify with provided test cases from feature document. [f8543a7]
- [x] Task: Run existing regression tests (`pytest tests/`). [f8543a7] (Note: User opting for manual visual verification)
- [x] Task: Conductor - User Manual Verification 'Styling Commands' (Protocol in workflow.md) [f8543a7]
