# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

TeXicode renders LaTeX math expressions as Unicode text art. It has two interfaces: a Python CLI and a browser-based web app (via Pyodide/WebAssembly).

## Commands

```bash
# Install locally for development
pip install -e .

# Run CLI
python src/main.py "\\frac{1}{2}"
python src/main.py -f example.md        # process markdown file
python src/main.py -c "\\sum_{i=0}^{n}"  # color output
python src/main.py -n "\\alpha"           # normal font (vs default serif)
python src/main.py -d "\\sqrt{x}"         # debug output

# Publish (GitHub Actions)
# Triggered on release creation or manual workflow_dispatch
```

There are no linters or build steps configured.

### Testing
Testing in this repository is data-driven. A visual regression script is available at `run_tests.py`, and an automated assertion suite is available via `pytest tests/`. Both identically read from the central data arrays (like `CORE_TESTS` and `ALIGNMENT_TESTS`) defined in `tests/test_data.py`. As you implement future features (like new environments or symbols), you can simply open up `tests/test_data.py` and add the new LaTeX strings and their expected visual grids to those arrays. This immediately registers them as both an automated regression test and a visual terminal demo!

## Architecture

The core is a 5-stage pipeline in `src/`:

```
Input LaTeX → Lexer → Parser → Renderer → Pipeline → Unicode text output
```

1. **lexer.py** — Tokenizes TeX input into command/number/alphabet/symbol tokens
2. **parser.py** — Builds an AST from tokens using node type metadata from `node_data.py`
3. **node_data.py** — Defines the type system: `type_dict` (token→type), `parent_dependent_type_dict` (context-aware), `type_dependent_type_dict`, and `type_info_dict` (metadata per type: popability, children, rendering behavior)
4. **renderer.py** — Converts AST to 2D character grids ("sketches"). Key concepts:
   - **Sketch**: a list of strings representing lines of rendered output
   - **Horizon**: the baseline reference line index within a sketch, used for vertical alignment during concatenation
   - `util_concat()` — horizontal join with horizon alignment
   - `util_vert_pile()` — vertical stacking
   - `util_script()` / `util_shrink()` — superscript/subscript via Unicode script characters
   - `util_delimiter()` — box-drawing for tall brackets
5. **pipeline.py** — Orchestrates the stages; handles color (ANSI), font selection, and output contexts (raw, md_inline, md_block, web)

Supporting data modules:
- **arts.py** — Unicode character sets (fonts: serif_it, serif_bld, sans, mono, etc.), multi-line operator art (∑, ∏, ∫), delimiter art, and superscript/subscript glyph mappings
- **symbols_art.py** — LaTeX command → Unicode character mappings (Greek letters, operators, arrows, relations, etc.)

**main.py** — CLI entry point with argparse. Processes single expressions or markdown files (regex-based LaTeX block/inline detection).

### Web Interface

- `index.html` / `main.js` / `style.css` — Browser UI using Pyodide 0.29.0
- `main.js` loads Pyodide, fetches all `src/*.py` files into a virtual filesystem, and calls `pipeline.render_tex_web()`
- `pyodide/` contains the Pyodide runtime and wheels

## Key Design Details

- **No external Python dependencies** — everything is pure Python
- Node types drive the entire parse/render flow. To add a new LaTeX command, you typically need to: add token handling in `lexer.py`, define the node type in `node_data.py` (across up to 3 type dicts + `type_info_dict`), and add a rendering function in `renderer.py`
- The renderer works with fixed-width Unicode characters; font support relies on Unicode Mathematical Alphanumeric Symbols blocks
- `setup.py` defines the `txc` CLI entry point
