# TeXicode Technology Stack

## Core Technologies
- **Programming Language:** Python (>= 3.8)
- **Runtime:** Standard Python Interpreter for CLI; Pyodide for Web browser runtime.
- **Build System:** `setuptools` with `pyproject.toml`.

## CLI Component
- **Implementation:** Python-based command-line tool.

## Web Component
- **Frontend Framework:** Vanilla JavaScript (main.js).
- **Runtime Environment:** Pyodide (v0.25.0+) for on-device Python execution in the browser.
- **Styling:** Vanilla CSS (style.css).
- **Template:** HTML5 (index.html).

## Architecture
- **Pipeline:** Modular Lexer -> Parser -> Renderer architecture.
- **API Orchestration:** High-level `pipeline.py` provides uniform interface for both CLI and Web.
- **Data-Driven Testing:** Visual regression and assertion-based testing using `pytest` and shared test data.
