# Feature: Matrix Environments

## What's Broken

All matrix environments crash with `Unexpected & at positions [0]`.

```bash
python src/main.py '\begin{bmatrix} a & b \\ c & d \end{bmatrix}'
# Output: TeXicode: rendering error: Unexpected & at positions [0]
```

The root cause: `render_begin()` only recognizes `align` and `align*`. Everything
else calls `render_concat_line_no_align_amp()`, which passes `align_amp=False` to
`util_concat()`, which raises ValueError when it encounters `&`.

## What to Implement

Support these environments:

| Environment | Delimiters |
|---|---|
| `matrix` | none |
| `pmatrix` | ( ) |
| `bmatrix` | [ ] |
| `vmatrix` | \| \| |
| `Vmatrix` | ‖ ‖ |

## Expected Behavior

1. Parse `&` as column separator, `\\` as row separator (same as `align`).
2. Render each cell independently (cells can contain fractions, scripts, etc.).
3. Find the widest cell in each column. Pad all cells in that column to match.
4. Center-align cell content within its column.
5. Add single-space gutters between columns.
6. For delimited variants (pmatrix, bmatrix, etc.), wrap the grid in the
   appropriate delimiter pair, scaled to the grid height using `util_delimiter()`.

## Expected Outputs

### Test 1: Basic bmatrix
```bash
python src/main.py '\begin{bmatrix} a & b \\ c & d \end{bmatrix}'
```
```
 ⎡ 𝑎  𝑏 ⎤
 ⎣ 𝑐  𝑑 ⎦
```

### Test 2: Basic pmatrix
```bash
python src/main.py '\begin{pmatrix} a & b \\ c & d \end{pmatrix}'
```
```
 ⎛ 𝑎  𝑏 ⎞
 ⎝ 𝑐  𝑑 ⎠
```

### Test 3: 3x3 matrix
```bash
python src/main.py '\begin{bmatrix} a & b & c \\ d & e & f \\ g & h & i \end{bmatrix}'
```
```
 ⎡ 𝑎  𝑏  𝑐 ⎤
 ⎢ 𝑑  𝑒  𝑓 ⎥
 ⎣ 𝑔  ℎ  𝑖 ⎦
```

### Test 4: Matrix with fractions in cells
```bash
python src/main.py '\begin{pmatrix} \frac{1}{2} & 0 \\ 0 & 1 \end{pmatrix}'
```
The row containing the fraction should be taller. The `0` and `1` cells should
be vertically centered against the fraction's baseline.

### Test 5: Bare matrix (no delimiters)
```bash
python src/main.py '\begin{matrix} a & b \\ c & d \end{matrix}'
```
```
 𝑎  𝑏
 𝑐  𝑑
```

### Test 6: vmatrix (determinant)
```bash
python src/main.py '\begin{vmatrix} a & b \\ c & d \end{vmatrix}'
```
Should use `|` delimiters scaled to height.

### Test 7: Column vector
```bash
python src/main.py '\begin{bmatrix} x \\ y \\ z \end{bmatrix}'
```
```
 ⎡ 𝑥 ⎤
 ⎢ 𝑦 ⎥
 ⎣ 𝑧 ⎦
```

### Test 8: S-parameter matrix (real-world)
```bash
python src/main.py '\begin{bmatrix} b_1 \\ b_2 \end{bmatrix} = \begin{bmatrix} S_{11} & S_{12} \\ S_{21} & S_{22} \end{bmatrix} \begin{bmatrix} a_1 \\ a_2 \end{bmatrix}'
```
Three matrices side by side with `=` between the first two.

## Implementation Approach

1. In `render_begin()`, add name checks for `matrix`, `pmatrix`, `bmatrix`,
   `vmatrix`, `Vmatrix`.

2. Write a new function `render_matrix(children, delim_left, delim_right)` that:
   - Calls `util_concat(children[1:], concat_line=True, align_amp=True)` to get
     the content with amp positions.
   - Splits the rendered rows by `\\` line breaks.
   - For each row, splits by amp positions into cells.
   - Measures cell widths per column, pads to the max.
   - Stacks rows vertically with `util_vert_pile` or manual row assembly.
   - If delimiters are specified, wraps with `util_delimiter()`.

3. The tricky part is that `\\` and `&` interact with the existing line-break
   and concat machinery. Study how `align` does it — the matrix logic is similar
   but needs per-cell padding and delimiter wrapping on top.

## Verification

Run all 8 test inputs above. Paste each output. Then run the regression checks
from common-instructions.md.
