# Feature: Markdown Mode Improvements

## Current State

`txc -f file.md` reads a markdown file, finds LaTeX equations (inline `$...$`
and display `$$...$$`), renders them to Unicode, and replaces them in the output.
The output can be piped to `glow` for terminal markdown rendering.

## What to Verify and Fix

### Test 1: Inline math preserved in flow
```bash
echo 'The energy $E = mc^2$ is fundamental.' > /tmp/test.md
python src/main.py -f /tmp/test.md
```
Expected: `The energy 𝐸 = 𝑚𝑐² is fundamental.`
Inline equation replaced in-place within the sentence.

### Test 2: Display math as block
```bash
echo '$$\frac{a}{b} = c$$' > /tmp/test.md
python src/main.py -f /tmp/test.md
```
Expected: The fraction renders as a multi-line block, properly indented.

### Test 3: Multiple equations in one file
```bash
cat > /tmp/test.md << 'EOF'
# Test Document

Inline: $\alpha + \beta = \gamma$

Display:

$$\int_0^1 x\,dx = \frac{1}{2}$$

More text here with $x^2$ inline.
EOF
python src/main.py -f /tmp/test.md
```
Expected: All three equations rendered. Surrounding markdown untouched.

### Test 4: Escaped dollars not treated as math
```bash
echo 'The price is \$10 and $x = 5$.' > /tmp/test.md
python src/main.py -f /tmp/test.md
```
Expected: `The price is $10 and 𝑥 = 5.`
Escaped `\$` is literal, not math delimiter.

### Test 5: Pipe to glow
```bash
cat > /tmp/test.md << 'EOF'
# Math in Markdown

The formula $E = mc^2$ is famous.

$$\sum_{i=0}^{n} i = \frac{n(n+1)}{2}$$
EOF
python src/main.py -f /tmp/test.md -c | glow
```
Expected: Beautiful terminal output with rendered math and markdown formatting.

### Test 6: Code blocks should NOT have math rendered
```bash
cat > /tmp/test.md << 'EOF'
Here is code:

```python
x = "$not_math$"
```

But $x$ is math here.
EOF
python src/main.py -f /tmp/test.md
```
Expected: The `$not_math$` inside the code block is untouched. Only `$x$`
outside the code block is rendered.

## Potential Issues to Fix

1. **Multi-line display math:** `$$` blocks that span multiple lines in the
   source file need to be collected into a single LaTeX expression before
   rendering.

2. **Indentation of multi-line output:** When a display equation renders as
   multiple lines (e.g., a fraction), all lines should be indented consistently.

3. **Code block protection:** Math delimiters inside `` ` `` or `` ``` `` blocks
   must not be processed.

4. **Nested delimiters:** `$a_{$b$}$` — this is rare but shouldn't crash.

## Implementation Approach

1. Read the markdown file
2. Identify code blocks (``` fenced and indented) — mark as protected regions
3. Outside protected regions, find `$$...$$` (display) and `$...$` (inline)
4. For each match, render the LaTeX content via the pipeline
5. Replace in the output:
   - Inline: single-line replacement
   - Display: multi-line replacement with consistent indentation

## Verification

Run all 6 tests above. Compare output to expected. Then run the regression
checks from common-instructions.md.
