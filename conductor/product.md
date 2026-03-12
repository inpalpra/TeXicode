# Initial Concept
TeX math expressions into Unicode art

# TeXicode Product Guide

## Vision
TeXicode (TeX to Unicode) is a tool that renders TeX math expressions into Unicode art, specifically designed for environments that support code blocks but not native LaTeX (e.g., Reddit, Discord, terminal previews).

## Target Users
- **Social Media Users:** Users of Reddit, Discord, and Teams who want to include math in their posts.
- **Developers:** Developers needing quick math previews in terminals or documentation.
- **General Users:** Anyone looking to insert equations into any text field.
- **Markdown Enthusiasts:** Users who want to render math in markdown files for terminal previews (e.g., using `glow`).
- **Personal Use:** Developed as a personal project.

## Core Goals
- **Command Support:** Support a wide range of LaTeX math commands.
- **Output Quality:** Ensure high-quality Unicode output across platforms, avoiding legacy ASCII art.
- **CLI-First:** Focus on the Python-based CLI as the primary tool.
- **Simplicity:** High-level functions like `render_tex` and `render_tex_web` to orchestrate the rendering.

## Current Features
- Lexer-Parser-Renderer pipeline.
- Unicode focus (italics, box-drawing characters).
- Modular architecture (node-based).
- CLI and Web-based (via Pyodide) interfaces.
- **Markdown Processing:** Render math in markdown files, supporting multiline equations and terminal display (e.g., by piping into a markdown renderer like `glow`).

## Roadmap
- **Overset, Underset & Braces:** support for `\overset`, `\underset`, and large braces.
- **Equation Tags:** numbering and tagging equations.
- **Styling Commands:** `\mathbf`, `\mathcal`, etc.
- **Graceful Degradation:** fallback for unsupported commands.
- **Spacing & Operators:** `\quad`, `\enspace`, and better operator spacing.
- **Markdown Mode:** improvements to markdown file processing.
