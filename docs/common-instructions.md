# TeXicode: Common Instructions for All Feature Work

Feed this document to every agent alongside the specific feature document.

---

## What This Project Is

TeXicode converts LaTeX math to Unicode text art for terminals. The CLI is `txc`.
The source is in `src/`. There are no existing tests.

## Architecture (5-Minute Version)

```
Input LaTeX → lexer.py → parser.py → renderer.py → 2D character grid
```

**Core data structure — the Sketch:**
- A sketch is a `list[list[str]]` — a 2D grid of single characters.
- Each row is one line of output. Each cell is one character.
- A sketch has a **horizon** — the baseline row index (like the line you write on).
- A sketch has **amps** — a list of column positions where `&` alignment markers appeared.
- Everything in the renderer returns `(sketch, horizon, amps)`.

**How rendering works:**
- `renderer.py` processes the AST bottom-up (children rendered before parents).
- `render_node()` dispatches to a specific `render_*` function based on node type.
- The function name is defined in `node_data.py` → `type_info_dict[node_type][4][1]`.

**Key utility functions in `renderer.py`:**
- `util_concat(children, concat_line, align_amp)` — horizontal join. Aligns children
  by their horizon (baseline). If `align_amp=True`, tracks `&` column positions.
  If `align_amp=False` and an `&` is encountered, it **raises ValueError**.
- `util_vert_pile(top, ctr, ctr_horizon, btm, align)` — vertical stack with
  left/center/right alignment. Used for fractions, limits, etc.
- `util_delimiter(delim_type, height, horizon)` — builds a scaled bracket column
  (parens, brackets, braces) from box-drawing characters in `arts.py`.

**How environments work:**
- `\begin{name}...\end{name}` is parsed into a `cmd_bgin` node with children:
  - child[0]: the environment name (as character nodes)
  - child[1:]: the content between \begin and \end
- `render_begin(children)` dispatches based on `children[0][0]` (the name).
- Currently only `align` and `align*` are recognized. Everything else falls
  through to `render_concat_line_no_align_amp()` which crashes on `&`.

**How `&` and `\\` work:**
- `&` is rendered as a zero-width marker. `util_concat` records its column position
  in the amps list (when `align_amp=True`).
- `\\` creates a `cmd_lbrk` node that splits content into separate lines.
  After `\\`, each line is rendered independently, then lines are stacked vertically.

**Character art in `arts.py`:**
- `arts.delimiter` — dictionary of delimiter art by position (`sgl`, `top`, `ctr`,
  `fil`, `btm`). Index into each string by finding the delimiter in `sgl`.
- `arts.bg` — the background character (space).
- Font lookups: `arts.serif_it`, `arts.serif_bld`, `arts.mathbb`, etc.

## How to Run and Verify

```bash
cd ~/repos/TeXicode

# Run a single expression:
python src/main.py '\frac{1}{2}'

# Run from a markdown file:
python src/main.py -f input.md

# With color:
python src/main.py -c '\sum_{i=0}^{n} x_i'
```

**The verification standard:** Run the exact input shown in the feature document.
Paste the terminal output. Compare visually to the expected output. If it doesn't
match, the feature is not done.

## Rules for Implementation

1. **Reproduce the failure first.** Before writing any code, run the broken input
   and confirm it fails. Paste the error or broken output.

2. **One feature at a time.** The feature document describes one capability. Implement
   it fully before moving on.

3. **Test at the CLI level.** After every code change, run `python src/main.py '<input>'`
   and paste the output. Do not write unit tests unless the feature document asks for them.

4. **Never break existing features.** After your change, verify these still work:
   ```bash
   python src/main.py '\frac{1}{2}'
   python src/main.py '\int_0^1 x\,dx = \frac{1}{2}'
   python src/main.py '\sum_{i=0}^{n} x_i'
   python src/main.py '\left( \frac{a}{b} \right)'
   python src/main.py '\hat{x} + \bar{y} + \vec{z}'
   python src/main.py '\alpha + \beta = \gamma'
   python src/main.py 'E = mc^2'
   python src/main.py '\binom{n}{k}'
   python src/main.py '\sqrt{\frac{a^2+b^2}{c^2}}'
   python src/main.py '\lim_{x \to \infty} f(x)'
   ```
   If any of these change, your implementation has a regression. Fix it before
   declaring done.

5. **Touch only the files you need.** The core files are:
   - `src/renderer.py` — rendering logic
   - `src/node_data.py` — type system and dispatch tables
   - `src/arts.py` — character art
   - `src/parser.py` — only if parsing changes are needed
   - `src/lexer.py` — only if new token types are needed

6. **Unsupported constructs should never produce `?`.** If you can't render
   something, fall back to the raw LaTeX source text. `?` is never acceptable.

## Where to Find Things

| What | Where |
|---|---|
| Environment dispatch | `src/renderer.py`, `render_begin()` (~line 541) |
| Horizontal concat | `src/renderer.py`, `util_concat()` (~line 46) |
| Vertical stack | `src/renderer.py`, `util_vert_pile()` (~line 95) |
| Delimiter scaling | `src/renderer.py`, `util_delimiter()` (~line 214) |
| Node type config | `src/node_data.py`, `type_info_dict` (~line 102) |
| Token→type mapping | `src/node_data.py`, `type_dict` (~line 34) |
| Delimiter art | `src/arts.py`, `delimiter` dict (~line 170) |
| CLI entry point | `src/main.py` |
| Pipeline orchestration | `src/pipeline.py` |
