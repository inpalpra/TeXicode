# Feature: Graceful Degradation

## What's Broken

Any unrecognized command renders as `?`:

```bash
python src/main.py '\underbrace{x}_{y}'
# Output: ?

python src/main.py '\tag{1}'
# Output: ?
```

A `?` is never useful. The raw LaTeX is always more informative.

## The Rule

If TeXicode cannot render a LaTeX command, it must fall back to rendering
the raw LaTeX source text as plain Unicode characters. No `?`. No crash.
No silent omission.

## What to Implement

1. **Unknown commands render as source text.** If a `\command` is not in the
   type system, render the literal string `\command` (plus its braced arguments
   if any).

2. **Unknown environments render content.** If `\begin{unknown}...\end{unknown}`
   is not recognized, render the content between begin/end as if the environment
   wrapper wasn't there. Ignore `&` and treat `\\` as line breaks.

3. **Never produce `?`.** Search the entire codebase for anywhere `?` is
   returned as output. Replace every instance with raw-source fallback.

4. **Never crash on valid LaTeX.** Any input that `pdflatex` would accept
   should produce some output, even if degraded.

## Expected Outputs

### Test 1: Unknown command
```bash
python src/main.py '\phantomcommand{abc}'
```
```
 \phantomcommand{abc}
```
Raw source, not `?`, not crash.

### Test 2: Unknown environment
```bash
python src/main.py '\begin{tikzpicture} x \end{tikzpicture}'
```
```
 x
```
Content is rendered; environment wrapper is ignored.

### Test 3: Currently broken commands produce source
```bash
python src/main.py '\tag{1}'
```
Before the tag feature is implemented, this should produce:
```
 \tag{1}
```
Not `?`.

### Test 4: Partial failure doesn't break the whole expression
```bash
python src/main.py 'a + \unknowncmd{b} + c'
```
```
 𝑎+\unknowncmd{b}+𝑐
```
The known parts render normally. The unknown part becomes source text.

### Test 5: Deeply nested unknown
```bash
python src/main.py '\frac{\unknowncmd{x}}{y}'
```
```
 \unknowncmd{x}
 ───────────────
       𝑦
```
The fraction renders. The unknown command in the numerator becomes source text.

## Implementation Approach

### Find all `?` sources

Search for `?` in the rendering path:
```bash
grep -n "'?'" src/renderer.py src/node_data.py src/arts.py
grep -n '"?"' src/renderer.py src/node_data.py src/arts.py
```

Each `?` site needs a fallback that reconstructs the source text.

### Fallback rendering function

Create `render_fallback(token, children)` in `renderer.py`:
- Reconstruct the source: `\commandname` + `{` + child source + `}`
- Render each character of the source text as a single-row sketch
- Return the sketch with horizon=0, amps=[]

### Error catching

Wrap `render_node()` in a try/except. If any render function raises, call
`render_fallback()` with the node's token and children.

This ensures that even if a recognized command has a bug in its render
function, the output is degraded but not broken.

### Unknown environments

In `render_begin()`, the `else` clause currently falls through to
`render_concat_line_no_align_amp()` which crashes on `&`. Change this:
- If the environment name is unrecognized, strip `&` from the children
  and render the content as plain concatenation.
- Alternatively, render with `align_amp=True` and just ignore the
  alignment (don't pad columns).

## Verification

Run all 5 test inputs above. Also deliberately test edge cases:
- Empty braces: `\unknowncmd{}`
- Nested unknown: `\cmd1{\cmd2{x}}`
- Unknown in subscript: `a_{\unknowncmd{1}}`

Then run the regression checks from common-instructions.md.
