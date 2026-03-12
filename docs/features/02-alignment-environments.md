# Feature: Alignment Environments (aligned, cases, gather)

## What's Broken

`aligned`, `cases`, `array`, and `gather` all crash on `&`:

```bash
python src/main.py '\begin{aligned} a &= b + c \\ d &= e + f \end{aligned}'
# Output: TeXicode: rendering error: Unexpected & at positions [0]

python src/main.py '\begin{cases} x & \text{if } x > 0 \\ -x & \text{otherwise} \end{cases}'
# Output: TeXicode: rendering error: Unexpected & at positions [0]
```

Same root cause as matrices: `render_begin()` doesn't recognize these names.

## What to Implement

| Environment | Behavior |
|---|---|
| `aligned` | Multi-line, aligned at `&`. No delimiters. |
| `cases` | Left curly brace, two columns (expression, condition). |
| `gather` / `gather*` | Multi-line, each line centered, no alignment point. |
| `array` | Column spec `{lcr}`, explicit alignment per column. |
| `split` | Same as `aligned`. |

## Expected Outputs

### Test 1: aligned
```bash
python src/main.py '\begin{aligned} a &= b + c \\ d &= e + f \end{aligned}'
```
```
 𝑎 = 𝑏+𝑐
 𝑑 = 𝑒+𝑓
```
The `=` signs must be vertically aligned.

### Test 2: cases
```bash
python src/main.py '\begin{cases} x & \text{if } x > 0 \\ -x & \text{otherwise} \end{cases}'
```
```
 ⎧ 𝑥   if 𝑥>0   
 ⎨               
 ⎩-𝑥  otherwise  
```
Left curly brace scaled to height. Two columns: math and text condition.

### Test 3: cases with three branches
```bash
python src/main.py '\begin{cases} 1 & x > 0 \\ 0 & x = 0 \\ -1 & x < 0 \end{cases}'
```
Left brace should scale to 3 rows.

### Test 4: aligned with fractions
```bash
python src/main.py '\begin{aligned} y &= \frac{a}{b} \\ z &= c + d \end{aligned}'
```
The `=` signs align. The row with the fraction is taller.

### Test 5: gather (centered, no alignment)
```bash
python src/main.py '\begin{gather} a + b = c \\ x + y = z \end{gather}'
```
```
 𝑎+𝑏 = 𝑐
 𝑥+𝑦 = 𝑧
```
Each line centered independently (no column alignment).

### Test 6: Real-world aligned derivation
```bash
python src/main.py '\begin{aligned} b_1 &= S_{11}a_1 + S_{12}a_2 \\ b_2 &= S_{21}a_1 + S_{22}a_2 \end{aligned}'
```
```
 𝑏₁ = 𝑆₁₁𝑎₁+𝑆₁₂𝑎₂
 𝑏₂ = 𝑆₂₁𝑎₁+𝑆₂₂𝑎₂
```

## Implementation Approach

1. In `render_begin()`, add name checks for `aligned`, `split`, `cases`,
   `gather`, `gather*`, `array`.

2. **For `aligned` and `split`:** These work exactly like `align` — just call
   `util_concat(children[1:], True, True)`. The existing align logic already
   handles `&` alignment and `\\` line breaks.

3. **For `cases`:** Same as `aligned`, but after rendering the grid, wrap
   the left side with a `{` delimiter via `util_delimiter("{", height, horizon)`.

4. **For `gather`:** Call `util_concat(children[1:], True, False)` — line breaks
   enabled, but no `&` alignment. Each line rendered independently, centered.

5. **For `array`:** Parse the column spec from `children[0]`, then render like
   a matrix with per-column alignment (left/center/right) based on the spec.

## Key Insight

`aligned` is literally the same as `align` — the only difference is that `align`
is a top-level environment and `aligned` is meant to be nested inside `$$`. The
rendering logic is identical. The fix for `aligned` is a one-line addition to
`render_begin()`.

`cases` is `aligned` + a left brace delimiter.

## Verification

Run all 6 test inputs above. Paste each output. Then run the regression checks
from common-instructions.md.
