# TeXicode

## Build, test, and lint commands

```bash
# Install the CLI locally
pip install -e .

# Run the CLI directly on a single TeX expression
python src/main.py '\frac{a}{b}'

# Process a Markdown file with embedded math
python src/main.py -f example.md

# Useful targeted validation runs
python src/main.py -c '\sum_{i=0}^{n} i'
python src/main.py -n '\alpha'
python src/main.py -d '\sqrt{x}'

# Validate Python syntax across the core modules
python -m py_compile src/*.py

# Build release artifacts (same packaging path used in GitHub Actions)
python -m pip install build
python -m build

# Run the browser app locally
python -m http.server 8000
```

There is no automated CI test suite or lint configuration in this repository. For single-case validation, run `python src/main.py '<expression>'` against the exact expression or markdown file affected by your change.

For regression testing, the repository uses a data-driven architecture. A visual regression script is available at `run_tests.py`, and an automated assertion suite is available via `pytest tests/`. Both identically read from the central data arrays (like `CORE_TESTS` and `ALIGNMENT_TESTS`) defined in `tests/test_data.py`. As you implement future features (like new environments or symbols), you can simply open up `tests/test_data.py` and add the new LaTeX strings and their expected visual grids to those arrays. This immediately registers them as both an automated regression test and a visual terminal demo!

## High-level architecture

TeXicode has one rendering core used in two interfaces:

- The Python CLI in `src/main.py`
- The web app in `index.html` + `main.js`, which loads the same `src/*.py` files into Pyodide and calls `pipeline.render_tex_web(...)`

The core pipeline is:

```text
TeX input -> lexer.py -> parser.py -> renderer.py -> pipeline.py -> rendered Unicode art
```

- `lexer.py` tokenizes TeX into command/alphabet/number/symbol tokens and injects `meta` start/end markers for parsing.
- `parser.py` builds the node tree from those tokens. It does not hardcode TeX behavior; it relies on the type metadata in `node_data.py`.
- `node_data.py` is the central grammar/render metadata table. `type_dict`, `parent_dependent_type_dict`, and `type_dependent_type_dict` decide node types; `type_info_dict` controls stack behavior, children, and which renderer function to call.
- `renderer.py` turns parsed nodes into "sketches" (2D character grids) and aligns them using a `horizon` baseline. Rendering dispatch is data-driven through function names stored in `node_data.type_info_dict`.
- `pipeline.py` orchestrates lexing/parsing/rendering, chooses the active font in `arts.py`, and formats output for raw CLI text, markdown inline/block output, and the web UI.
- `arts.py` and `symbols_art.py` are the glyph databases: fonts, delimiter art, script glyphs, large operators, and TeX-command-to-Unicode mappings.

## Key conventions

- Most feature work is metadata-driven. When adding or changing TeX support, start with `node_data.py` and then update `renderer.py`; only touch `lexer.py` when tokenization rules themselves must change.
- Renderer values are passed around as `(sketch, horizon, amps)` tuples. A sketch is a list of character rows, and `horizon` is the alignment baseline used by helpers like `util_concat()` and `util_vert_pile()`.
- Script handling is split between parse time and render time: `parser.py` reclassifies scripts based on the base node (`sup_scrpt`/`sub_scrpt` vs. `top_scrpt`/`btm_scrpt`), and `renderer.py` applies them afterward with `render_apply_scripts()`.
- `\begin{align}` and `\begin{align*}` are special-cased in `renderer.py` to align columns using ampersand positions. Keep ampersand handling consistent with `util_add_ampersand_padding()` and `render_begin()`.
- Unknown commands are usually surfaced visually as `?` in `render_leaf()`, while structural/internal failures raise `ValueError` and are wrapped in `pipeline.py` as stage-specific TeXicode errors.
- Font selection is global state in `arts.py`. `pipeline.init_arts()` switches between serif and normal fonts before rendering, and the web app mirrors that through the "Normal font" toggle.
- `main.js` has an explicit list of Python files copied into the Pyodide filesystem. If a new Python module becomes part of the runtime path, update that list as well as the packaging metadata in `setup.py`.
