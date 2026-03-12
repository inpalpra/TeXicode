# Implementation Plan: Styling Commands

## Phase 1: Registration and Data Setup
Define new node types and their properties to enable parsing and dispatching.

- [ ] Task: Register new commands in `src/node_data.py`.
    - [ ] `\boxed`: Type `CMD_BOXD`, 1 child, `render_boxed`.
    - [ ] `\color`, `\textcolor`: Type `CMD_COLR`, 2 children, `render_color`.
    - [ ] `\cancel`, `\bcancel`: Type `CMD_CNCL`, 1 child, `render_cancel`.
    - [ ] `\colorbox`: Type `CMD_CBOX`, 2 children, `render_colorbox`.
    - [ ] `\fcolorbox`: Type `CMD_FCBX`, 3 children, `render_fcolorbox`.
- [ ] Task: Define color name to ANSI mapping in `src/arts.py` or `src/renderer.py`.

## Phase 2: Core Rendering Implementation
Implement the rendering functions in `src/renderer.py`.

- [ ] Task: Implement `render_boxed`.
    - [ ] Wrap sketch in box-drawing characters.
    - [ ] Adjust horizon.
- [ ] Task: Implement `render_color` and `render_colorbox`.
    - [ ] Use ANSI escape sequences for text and background colors.
    - [ ] Handle nesting by managing current color state.
- [ ] Task: Implement `render_cancel`.
    - [ ] Apply U+0336 combining character to each non-space character in the sketch.
- [ ] Task: Implement `render_fcolorbox`.
    - [ ] Combine `boxed` and `colorbox` logic.

## Phase 3: Verification and Regressions
Confirm functionality and ensure no regressions.

- [ ] Task: Verify with provided test cases from feature document.
- [ ] Task: Run existing regression tests (`pytest tests/`).
- [ ] Task: Conductor - User Manual Verification 'Styling Commands' (Protocol in workflow.md)
