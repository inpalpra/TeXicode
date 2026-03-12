# Track Specification: Graceful Degradation

#### Overview
TeXicode currently renders `?` for unrecognized commands or environments. This track implements a graceful degradation system that falls back to raw LaTeX source text instead of producing an uninformative `?`. This ensures that even unsupported or partially supported LaTeX remains readable as source code.

#### Functional Requirements
1.  **Unknown Command Fallback:**
    *   Any command not recognized by the type system must render its literal name (e.g., `\unknowncmd`).
    *   Braced arguments of unknown commands must be rendered and enclosed in literal braces `{` and `}`.
    *   Fallback text must use standard monospace characters (ASCII).
2.  **Unknown Environment Fallback:**
    *   Unrecognized environments (e.g., `\begin{unknown}...\end{unknown}`) must render the `\begin{name}` and `\end{name}` markers around the rendered content.
    *   Within the content, `&` markers must be ignored and `\\` must be treated as line breaks.
3.  **Recursive Rendering in Fallbacks:**
    *   Known commands inside the arguments of an unknown command (e.g., `\unknown{\frac{1}{2}}`) should still be rendered visually if possible.
4.  **Global `?` Elimination:**
    *   Replace all instances of `?` in `src/renderer.py` and `src/node_data.py` with source-based fallbacks.
5.  **No Crash Guarantee:**
    *   Wrap node rendering in error handling to ensure that a bug in a specific renderer falls back to source text rather than crashing the entire process.

#### Non-Functional Requirements
*   **Silent Operation:** No warnings will be printed to `stderr` when degradation occurs.
*   **Performance:** Fallback logic should be lightweight.

#### Acceptance Criteria
*   `python src/main.py '\unknown{x}'` outputs `\unknown{x}`.
*   `python src/main.py '\begin{unknown} x \end{unknown}'` outputs `\begin{unknown} x \end{unknown}`.
*   `python src/main.py 'a + \unknown{b} + c'` renders `a` and `c` normally, and `\unknown{b}` as source.
*   `python src/main.py '\frac{\unknown{x}}{y}'` renders the fraction with `\unknown{x}` in the numerator.
*   No input produces a `?` or a crash.
