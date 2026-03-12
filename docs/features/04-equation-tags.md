# Feature: Equation Tags

## What's Broken

```bash
python src/main.py '\tag{1} E = mc^2'
# Output: contains ? for the tag
```

`\tag{n}` should render a right-aligned equation number like `(1)`.

## What to Implement

| Command | Behavior |
|---|---|
| `\tag{text}` | Render `(text)` right-aligned after the equation |
| `\tag*{text}` | Render `text` (no parens) right-aligned after the equation |

## Expected Outputs

### Test 1: Simple tag
```bash
python src/main.py '\tag{1} E = mc^2'
```
```
 𝐸 = 𝑚𝑐²   (1)
```

### Test 2: Tag star (no parens)
```bash
python src/main.py '\tag*{\dagger} a = b'
```
```
 𝑎 = 𝑏   †
```

### Test 3: Tag with text
```bash
python src/main.py '\tag{2.1} \int_0^1 x\,dx = \frac{1}{2}'
```
```
  1        
 ∫  𝑥 𝑑𝑥 = ─   (2.1)
  0        2
```
Tag vertically aligned to baseline of equation.

## Implementation Approach

1. Register `\tag` in `node_data.py` (1 child: the tag content)
2. In `renderer.py`, add `render_tag(children)`:
   - Render the tag content
   - Wrap in `(` and `)` for `\tag` (skip parens for `\tag*`)
   - This produces a sketch
3. The tricky part: `\tag` doesn't just concat — it should appear at the
   right edge. Options:
   - Simplest: treat `\tag` as a concat child that adds padding + `(text)`.
     This means it just appears after the equation naturally with some spaces.
   - More complex: render the equation, measure its width, pad to a fixed
     line width, then place the tag. This requires knowing the terminal width.
   
   **Recommended:** Simple approach. Render `\tag{1}` as `   (1)` — three
   spaces then the parenthesized content. Concat it at the end of the equation.

## Verification

Run all 3 test inputs above. Paste each output. Then run the regression checks
from common-instructions.md.
