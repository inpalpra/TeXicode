# Feature: Styling Commands (color, boxed, cancel)

## What's Broken

```bash
python src/main.py '\boxed{a + b}'
# Output: ?

python src/main.py '\color{red}{x}'
# Output: renders "red" as visible text alongside x

python src/main.py '\cancel{x}'
# Output: ?

python src/main.py '\colorbox{yellow}{x^2}'
# Output: ? or crash
```

## What to Implement

| Command | Behavior |
|---|---|
| `\boxed{content}` | Draw a Unicode box around the content |
| `\color{name}{content}` | Apply ANSI terminal color to content |
| `\textcolor{name}{content}` | Same as `\color` |
| `\cancel{content}` | Strikethrough using combining char U+0336 |
| `\bcancel{content}` | Same as cancel (backslash direction not possible in terminal) |
| `\colorbox{name}{content}` | Apply ANSI background color |
| `\fcolorbox{border}{bg}{content}` | Box + background (render as boxed with bg color) |

## Expected Outputs

### Test 1: boxed
```bash
python src/main.py '\boxed{a + b}'
```
```
 ┌─────┐
 │𝑎+𝑏  │
 └─────┘
```
Box drawn with Unicode box-drawing characters.

### Test 2: color (with -c flag for color mode)
```bash
python src/main.py -c '\color{red}{x} + \color{blue}{y}'
```
`x` in red ANSI, `y` in blue ANSI, `+` in default color.

### Test 3: color without -c flag
```bash
python src/main.py '\color{red}{x} + y'
```
Just renders `𝑥+𝑦` — color ignored silently when color mode is off.
The color name (`red`) must NOT appear in output.

### Test 4: cancel
```bash
python src/main.py '\cancel{x}'
```
```
 x̶
```
Strikethrough using combining long stroke overlay (U+0336).

### Test 5: boxed fraction
```bash
python src/main.py '\boxed{\frac{a}{b}}'
```
```
 ┌───┐
 │ 𝑎 │
 │ ─ │
 │ 𝑏 │
 └───┘
```

## Implementation Approach

### boxed
1. Register `\boxed` in `node_data.py` (1 child)
2. Render the content, then wrap the sketch:
   - Add `│` on left and right of every row
   - Add `┌─…─┐` on top
   - Add `└─…─┘` on bottom
   - Horizon = original horizon + 1 (shifted down by top border)

### color / textcolor
1. Register in `node_data.py` (2 children: color name and content)
2. In render function:
   - If color mode is enabled (check global state or flag), wrap the content
     sketch characters with ANSI color escape sequences
   - If color mode is off, just render the content and discard the color name
   - **Critical:** The color name child (`{red}`) must be consumed and NOT
     rendered as visible text
3. Supported color names: red, blue, green, cyan, magenta, yellow, black, white

### cancel
1. Register in `node_data.py` (1 child)
2. Render the content, then apply combining character U+0336 to each non-space
   character in the sketch

## Verification

Run all 5 test inputs above. Paste each output. Then run the regression checks
from common-instructions.md.
