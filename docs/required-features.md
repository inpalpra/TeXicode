# TeXicode: Required Features for Complete Equation Rendering

## Purpose

TeXicode renders LaTeX math as Unicode text art for terminals, chat platforms, and
anywhere monospace text is accepted. This document specifies the features required
to make TeXicode capable of rendering the full range of LaTeX math that appears in
real-world academic and engineering documents — textbooks, papers, technical reports.

The standard of completeness: a user should be able to pipe any LaTeX math from a
published paper through TeXicode and get a legible, structurally correct Unicode
rendering. When a construct truly cannot be represented in Unicode text, TeXicode
should degrade gracefully rather than emit `?` or crash.

---

## Current State Summary

**Working well:** fractions (`\frac`), integrals (`\int`, `\iint`, `\iiint`),
summations (`\sum`), products (`\prod`), square roots (`\sqrt`), limits (`\lim`),
binomial coefficients (`\binom`), Greek letters, subscripts, superscripts,
`\left`/`\right` delimiters, hat/bar/vec/dot/ddot/tilde accents, `\text{}`,
`\mathrm{}`, `\mathbb{}`, `\mathcal{}`, nested fractions, `\substack`, font
variants, the `-f` markdown file mode, inline vs. block detection.

**Broken or missing:** everything listed below.

---

## 1. Matrix and Tabular Environments (Critical)

Matrices are among the most common structures in technical documents. Currently
all matrix environments fail with `Unexpected & at positions [0]` because the
`&` column separator is rejected outside of `align`/`align*`.

### Required environments

| Environment | Delimiters | Example |
|---|---|---|
| `matrix` | none | bare grid of entries |
| `pmatrix` | `( )` | parenthesized matrix |
| `bmatrix` | `[ ]` | bracketed matrix |
| `vmatrix` | `\| \|` | determinant |
| `Vmatrix` | `‖ ‖` | double-bar matrix |
| `smallmatrix` | none, inline-sized | for use inside prose |

### Required behavior

- Parse `&` as column separator and `\\` as row separator within these environments.
- Determine column widths from the widest entry in each column.
- Center-align entries within their columns (LaTeX default for matrices).
- Pad columns with single-space gutters.
- Wrap the grid in the appropriate delimiter pair, scaled to the matrix height
  using the existing `util_delimiter` box-drawing logic.
- Nested content in cells must work: `\frac{1}{2}` in a matrix cell should
  render the fraction vertically and the row height should expand to fit.

### Example expected output

Input: `\begin{bmatrix} a & b \\ c & d \end{bmatrix}`

```
 ⎡ 𝑎  𝑏 ⎤
 ⎣ 𝑐  𝑑 ⎦
```

Input: `\begin{pmatrix} \frac{1}{2} & 0 \\ 0 & 1 \end{pmatrix}`

```
 ⎛  1     ⎞
 ⎜ ╶─╴  0 ⎟
 ⎜  2     ⎟
 ⎜        ⎟
 ⎝  0   1 ⎠
```

---

## 2. Alignment Environments (Critical)

Multi-line aligned equations are standard in derivations and proofs. Currently
`aligned`, `cases`, `array`, and `gather` all fail.

### Required environments

| Environment | Purpose |
|---|---|
| `aligned` | Multi-line equations aligned at `&` (typically at `=`). Used inside `$$`. |
| `align` / `align*` | Top-level multi-line alignment. `align` already works; `align*` should too. |
| `cases` | Piecewise function definition. Left brace delimiter, two columns. |
| `array` | General tabular math with explicit column spec (`{lcr}`). |
| `gather` / `gather*` | Centered multi-line equations, no alignment point. |
| `split` | Like `aligned` but shares equation number with enclosing environment. |

### Required behavior for `aligned`

- Parse `&` as alignment anchor and `\\` as line separator.
- Align all lines at the `&` position (typically placed before `=`).
- Render each line on its own row with the `&` columns vertically aligned.
- No outer delimiters.

### Expected output

Input: `\begin{aligned} a &= b + c \\ d &= e + f \end{aligned}`

```
 𝑎 = 𝑏+𝑐
 𝑑 = 𝑒+𝑓
```

### Required behavior for `cases`

- Render a left curly brace `{` scaled to the number of rows.
- Two columns: the expression and the condition, separated by `&`.
- Conditions are left-aligned.

### Expected output

Input: `\begin{cases} x & \text{if } x > 0 \\ -x & \text{otherwise} \end{cases}`

```
 ⎧ 𝑥    if 𝑥>0    
 ⎨                
 ⎩-𝑥   otherwise  
```

### Required behavior for `array`

- Parse the column specification `{lcr}` for left/center/right alignment per column.
- `|` in the column spec renders vertical rules.
- `\hline` renders horizontal rules using box-drawing characters.

---

## 3. Tag, Label, and Equation Numbering (High)

Equation tags are ubiquitous in textbooks and papers. Currently `\tag{1}` renders
as `?1`.

### Required commands

| Command | Purpose |
|---|---|
| `\tag{...}` | Right-aligned equation number in parentheses: `(1)` |
| `\tag*{...}` | Right-aligned equation number without parentheses |
| `\label{...}` | Silent — should be consumed and ignored (no visible output) |
| `\eqref{...}` | Render as `(ref)` placeholder text |
| `\ref{...}` | Render as `ref` placeholder text |

### Expected output

Input: `E = mc^2 \tag{2.17}`

```
 𝐸 = 𝑚𝑐²                               (2.17)
```

The tag should be right-aligned to the rendering width, separated from the
equation by padding spaces.

---

## 4. Braces: Underbrace and Overbrace (High)

These are commonly used to annotate parts of expressions. Currently both render
the content but emit `?` for the brace itself.

### Required commands

| Command | Purpose |
|---|---|
| `\underbrace{...}_{...}` | Horizontal brace below content, label underneath |
| `\overbrace{...}^{...}` | Horizontal brace above content, label on top |

### Required behavior

- Render the spanned content normally.
- Draw a horizontal curly brace below (or above) using box-drawing or Unicode
  brace characters, sized to match the width of the spanned content.
- Render the label centered below the brace (for underbrace) or above (for
  overbrace).

### Expected output

Input: `\underbrace{a + b + c}_{n \text{ terms}}`

```
 𝑎+𝑏+𝑐  
 ⏟──────╴
 𝑛 terms 
```

Input: `\overbrace{x + y + z}^{\text{sum}}`

```
  sum    
 ⏞──────╴
 𝑥+𝑦+𝑧  
```

---

## 5. Overset and Underset (High)

Common in definitions (`\overset{def}{=}`) and annotated operators.

### Required commands

| Command | Purpose |
|---|---|
| `\overset{top}{base}` | Small text above a symbol |
| `\underset{bottom}{base}` | Small text below a symbol |
| `\stackrel{top}{base}` | Synonym for `\overset` |
| `\xrightarrow{...}` | Extensible arrow with text above |
| `\xleftarrow{...}` | Extensible arrow with text above |

### Expected output

Input: `\overset{\text{def}}{=}`

```
 def
  = 
```

Input: `\xrightarrow{\text{yields}}`

```
  yields  
 ╶───────→
```

---

## 6. Color Support (Medium)

Color is used in educational materials and presentations. Currently `\color{red}{x}`
renders as `?𝑟𝑒𝑑𝑥`.

### Required commands

| Command | Purpose |
|---|---|
| `\color{name}{...}` | Apply named color to content |
| `\textcolor{name}{...}` | Synonym |
| `\colorbox{name}{...}` | Background color (if terminal supports it) |

### Required behavior

- Map standard LaTeX color names (red, blue, green, black, white, cyan, magenta,
  yellow, orange, purple, brown, gray) to ANSI color codes.
- Respect the existing `-c` color flag: colors should only emit ANSI codes when
  color mode is enabled.
- When color mode is disabled, render the content normally without color.
- The color argument should be consumed (not rendered as text).

---

## 7. Boxed and Framed Content (Medium)

### Required commands

| Command | Purpose |
|---|---|
| `\boxed{...}` | Box-drawing rectangle around content |
| `\fbox{...}` | Synonym |
| `\cancel{...}` | Diagonal strikethrough (approximate with Unicode combining slash) |
| `\bcancel{...}` | Back-diagonal strikethrough |

### Expected output

Input: `\boxed{E = mc^2}`

```
 ┌─────────┐
 │ 𝐸 = 𝑚𝑐² │
 └─────────┘
```

---

## 8. Spacing Commands (Medium)

LaTeX has explicit spacing commands that affect readability. Some may already work;
all should be handled.

### Required commands

| Command | Width | Behavior |
|---|---|---|
| `\,` | thin space | Render as single space or half-space if possible |
| `\:` or `\>` | medium space | Render as single space |
| `\;` | thick space | Render as single space |
| `\!` | negative thin space | Consume (reduce spacing if adjacent) |
| `\quad` | 1em | Render as 2 spaces |
| `\qquad` | 2em | Render as 4 spaces |
| `\hspace{...}` | explicit | Approximate: render as N spaces |
| `\phantom{...}` | width of content | Render as spaces matching content width |
| `~` | non-breaking space | Render as single space |

---

## 9. Additional Delimiter Sizes (Medium)

`\left`/`\right` work for basic delimiters. The following should also work:

### Required

- `\left\{` / `\right\}` — curly braces (needed for `cases` and sets)
- `\left\langle` / `\right\rangle` — angle brackets
- `\left\lfloor` / `\right\rfloor` — floor
- `\left\lceil` / `\right\rceil` — ceiling
- `\left.` — invisible delimiter (for one-sided matching)
- `\middle|` — middle-sized delimiter in `\left...\right` pairs
- `\big`, `\Big`, `\bigg`, `\Bigg` — manually-sized delimiters

---

## 10. Additional Math Operators and Symbols (Low-Medium)

### Operators with limits

These should render with limits below/above like `\sum` and `\prod`:

| Command | Symbol |
|---|---|
| `\bigcup` | ⋃ |
| `\bigcap` | ⋂ |
| `\bigoplus` | ⨁ |
| `\bigotimes` | ⨂ |
| `\coprod` | ∐ |
| `\sup` | sup (with subscript limit) |
| `\inf` | inf (with subscript limit) |
| `\min` | min (with subscript limit) |
| `\max` | max (with subscript limit) |
| `\arg\min` | arg min (with subscript limit) |
| `\arg\max` | arg max (with subscript limit) |

### Missing relation/binary symbols

Check and add any missing from this commonly-used set:

`\leq`, `\geq`, `\neq`, `\approx`, `\equiv`, `\sim`, `\simeq`, `\cong`,
`\propto`, `\subset`, `\supset`, `\subseteq`, `\supseteq`, `\in`, `\notin`,
`\ni`, `\forall`, `\exists`, `\nexists`, `\nabla`, `\partial`, `\ell`,
`\wp`, `\Re`, `\Im`, `\aleph`, `\hbar`, `\dagger`, `\ddagger`, `\circ`,
`\bullet`, `\star`, `\diamond`, `\triangleleft`, `\triangleright`,
`\vdash`, `\dashv`, `\models`, `\perp`, `\parallel`, `\asymp`,
`\nmid`, `\mid`, `\ll`, `\gg`, `\lll`, `\ggg`, `\prec`, `\succ`,
`\preceq`, `\succeq`.

---

## 11. Multi-line Display in Markdown Mode (Medium)

When processing markdown with `txc -f`, the tool must handle display math blocks
that contain multiple lines and environments correctly.

### Required behavior

- `$$..$$` blocks should be treated as a single expression, even if they contain
  `\\` line breaks or environments like `aligned`.
- The rendered output should be wrapped in a code fence (` ``` `) in the output
  markdown, preserving the monospace formatting.
- Inline `$...$` that renders to more than one line should automatically be
  promoted to a code block (current behavior — keep it).
- Multiple consecutive display equations should each get their own code block.

---

## 12. Graceful Degradation (High)

Currently, unsupported commands render as `?`. This is confusing because the user
cannot tell what the original command was.

### Required behavior

- **Unsupported commands** should render as their LaTeX source in a visually
  distinct way, for example: `⟨\commandname⟩` or simply the raw LaTeX text.
  This lets the reader know what was intended even if it couldn't be rendered.
- **Unsupported environments** should render their content as-is (without the
  environment wrapper), rather than erroring on `&`.
- **Never crash or print error messages to stdout** when used in pipeline mode
  (`txc -f file.md`). Errors should go to stderr; stdout must always be valid
  markdown.

---

## 13. Accents and Decorations Completeness (Low)

The following accents should work on arbitrary-width content, not just single
characters:

| Command | Decoration |
|---|---|
| `\hat{...}` | Circumflex above |
| `\widehat{...}` | Wide circumflex spanning content width |
| `\bar{...}` | Overline |
| `\overline{...}` | Overline spanning content width (use box-drawing `─`) |
| `\underline{...}` | Underline spanning content width |
| `\vec{...}` | Right arrow above |
| `\widetilde{...}` | Wide tilde spanning content width |
| `\dot{...}` | Single dot above |
| `\ddot{...}` | Double dot above |
| `\acute{...}` | Acute accent |
| `\grave{...}` | Grave accent |
| `\breve{...}` | Breve |
| `\check{...}` | Caron |

For single-character content, Unicode combining marks are fine (current approach).
For multi-character content, use box-drawing characters spanning the width.

---

## 14. Additional Font Commands (Low)

| Command | Style | Status |
|---|---|---|
| `\mathrm{...}` | Roman (upright) | ✓ Works |
| `\mathbf{...}` | Bold | ✓ Works |
| `\mathit{...}` | Italic | ✓ Works |
| `\mathsf{...}` | Sans-serif | ✓ Works |
| `\mathtt{...}` | Monospace | ✓ Works |
| `\mathcal{...}` | Calligraphic | ✓ Works |
| `\mathbb{...}` | Blackboard bold | ✓ Works |
| `\mathfrak{...}` | Fraktur | ✓ Works |
| `\mathscr{...}` | Script | Check coverage |
| `\boldsymbol{...}` | Bold everything | Map to bold Unicode variants |
| `\bm{...}` | Synonym for `\boldsymbol` | Same |

---

## Priority Summary

| Priority | Feature | Impact |
|---|---|---|
| **Critical** | Matrix environments (§1) | Needed for any linear algebra, controls, signal processing |
| **Critical** | Alignment environments — `aligned`, `cases` (§2) | Needed for piecewise functions, derivations |
| **High** | `\tag` and equation numbering (§3) | Standard in every textbook |
| **High** | `\underbrace` / `\overbrace` (§4) | Common in explanatory math |
| **High** | `\overset` / `\underset` / extensible arrows (§5) | Common in definitions and proofs |
| **High** | Graceful degradation (§12) | UX — never emit `?` or crash |
| **Medium** | Color support (§6) | Educational and presentation math |
| **Medium** | `\boxed` (§7) | Highlighting key results |
| **Medium** | Spacing commands (§8) | Readability polish |
| **Medium** | Additional delimiters (§9) | Sets, floor/ceiling notation |
| **Medium** | Limit-style operators (§10) | Union, intersection, argmin |
| **Medium** | Markdown multi-line handling (§11) | Pipeline correctness |
| **Low** | Wide accents (§13) | Completeness |
| **Low** | Additional font commands (§14) | Completeness |
