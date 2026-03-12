# Feature: Overset, Underset, Overbrace, Underbrace

## What's Broken

These commands all produce `?` output:

```bash
python src/main.py '\underbrace{a + b + c}_{3 \text{ terms}}'
# Output: ?

python src/main.py '\overbrace{x + y}^{2 \text{ terms}}'
# Output: ?

python src/main.py '\overset{\text{def}}{=}'
# Output: ?

python src/main.py '\underset{x}{f}'
# Output: ?
```

These commands are not registered in `node_data.py` and have no render functions.

## What to Implement

| Command | Behavior |
|---|---|
| `\overset{top}{base}` | Place `top` centered above `base` |
| `\underset{bottom}{base}` | Place `bottom` centered below `base` |
| `\overbrace{content}^{label}` | Horizontal brace above content, label above brace |
| `\underbrace{content}_{label}` | Horizontal brace below content, label below brace |
| `\stackrel{top}{base}` | Same as `\overset` |
| `\xleftarrow[below]{above}` | Extensible left arrow with labels |
| `\xrightarrow[below]{above}` | Extensible right arrow with labels |

## Expected Outputs

### Test 1: overset
```bash
python src/main.py '\overset{\text{def}}{=}'
```

$$
\overset{\text{def}}{=}
$$

```
 def
  =
```
The text "def" centered above the `=` sign.

### Test 2: underset
```bash
python src/main.py '\underset{x \to 0}{\lim}'
```

$$
\underset{x \to 0}{\lim}
$$

```
 lim
 𝑥→0
```
The limit annotation below `lim`.

### Test 3: underbrace
```bash
python src/main.py '\underbrace{a + b + c}_{3 \text{ terms}}'
```

$$
\underbrace{a + b + c}_{3 \text{ terms}}
$$


```
 𝑎+𝑏+𝑐
 ⏟─────⏟
 3 terms
```
Horizontal brace spanning the content width, label centered below.
The exact brace character can be `⏟` (U+23DF) or built from box-drawing chars.

### Test 4: overbrace
```bash
python src/main.py '\overbrace{x + y}^{2}'
```

$$
\overbrace{x + y}^{2}
$$

```
   2
 ⏞───⏞
 𝑥+𝑦
```
Horizontal brace above, label above the brace.

### Test 5: stackrel (alias for overset)
```bash
python src/main.py '\stackrel{*}{\longrightarrow}'
```

$$
\stackrel{*}{\longrightarrow}
$$

`*` centered above a long right arrow.

### Test 6: xrightarrow
```bash
python src/main.py '\xrightarrow{\text{yields}}'
```

$$
\xrightarrow{\text{yields}}
$$

A right arrow that stretches to fit the text "yields" above it.

## Implementation Approach

### overset / underset / stackrel

These are vertical stacks — `util_vert_pile` is the tool.

1. Register `\overset`, `\underset`, `\stackrel` in `node_data.py`:
   - `type_dict`: map token to a node type (e.g., `cmd_ovst`)
   - `type_info_dict`: 2 children, render function `render_overset`
2. In `renderer.py`, add `render_overset(children)`:
   - Render child[0] (top) and child[1] (base)
   - Use `util_vert_pile(top_sketch, None, None, base_sketch, "center")`
   - Set horizon = base's horizon + top's height
3. `render_underset` is the same but reversed: base on top, annotation below.

### overbrace / underbrace

1. Register in `node_data.py` (2 children: content and label)
2. In `renderer.py`, add `render_underbrace(children)`:
   - Render child[0] (content)
   - Build a horizontal brace of `content_width` using `⏟` or box-drawing chars
   - Render child[1] (label)
   - Stack: content → brace → label (top to bottom)
3. `render_overbrace` is the reverse: label → brace → content

### Horizontal brace construction

Build a row like: `⎩` + `─` × (width - 2) + `⎭` for underbrace,
or use Unicode `⏟` (U+23DF BOTTOM CURLY BRACKET) if a single-char solution works.
For multi-width, use `⏞` (U+23DE TOP CURLY BRACKET) or `﹄﹃` etc.

A practical approach: one row of `─` with `⏟` or `⎨` in the center.

### xrightarrow / xleftarrow

1. Render the label text
2. Create an arrow `─→` or `←─` stretched to label width + 2
3. Stack label above arrow (or below for optional `[below]` argument)

## Verification

Run all 6 test inputs above. Paste each output. Then run the regression checks
from common-instructions.md.
