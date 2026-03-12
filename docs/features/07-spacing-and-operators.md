# Feature: Additional Spacing and Operators

## What's Broken or Missing

Some spacing commands and operators either produce `?` or incorrect output.

## What to Implement

### Spacing Commands

| Command | Width | Behavior |
|---|---|---|
| `\quad` | 2 spaces | Em space |
| `\qquad` | 4 spaces | Double em space |
| `\,` | thin space | Already works? Verify. |
| `\;` | medium space | Should produce 1 space |
| `\:` | medium space | Same as `\;` |
| `\!` | negative thin space | Reduce gap by 1 (or no-op) |
| `\phantom{x}` | width of x | Invisible, reserves space |
| `\hspace{1em}` | 2 spaces | Fixed horizontal space |

### Operators That May Be Missing

| Command | Symbol |
|---|---|
| `\implies` | ⟹ |
| `\iff` | ⟺ |
| `\therefore` | ∴ |
| `\because` | ∵ |
| `\approx` | ≈ |
| `\neq` or `\ne` | ≠ |
| `\leq` or `\le` | ≤ |
| `\geq` or `\ge` | ≥ |
| `\ll` | ≪ |
| `\gg` | ≫ |
| `\subset` | ⊂ |
| `\supset` | ⊃ |
| `\subseteq` | ⊆ |
| `\supseteq` | ⊇ |
| `\in` | ∈ |
| `\notin` | ∉ |
| `\forall` | ∀ |
| `\exists` | ∃ |
| `\nabla` | ∇ |
| `\partial` | ∂ |
| `\infty` | ∞ |
| `\pm` | ± |
| `\mp` | ∓ |
| `\times` | × |
| `\div` | ÷ |
| `\cdot` | · |
| `\circ` | ∘ |
| `\star` | ⋆ |
| `\dagger` | † |
| `\ddagger` | ‡ |
| `\ldots` | … |
| `\cdots` | ⋯ |
| `\vdots` | ⋮ |
| `\ddots` | ⋱ |

## Verification Approach

1. First, test each operator to see if it already works:
   ```bash
   for cmd in implies iff therefore because approx neq leq geq ll gg subset supset subseteq supseteq notin forall exists nabla partial infty pm mp times div cdot circ star dagger ddagger ldots cdots vdots ddots; do
     echo -n "\\$cmd: "
     python src/main.py "\\$cmd" 2>&1
   done
   ```

2. For any that produce `?` or error, add the symbol to `arts.py` or the
   appropriate lookup table.

3. Test spacing:
   ```bash
   python src/main.py 'a \quad b'
   python src/main.py 'a \qquad b'
   python src/main.py '\phantom{abc} x'
   ```

## Implementation Approach

### Missing operators
Most operators are just character lookups. In `arts.py` or `node_data.py`,
add a mapping from the command name to the Unicode symbol. No new render
functions needed — they use the existing leaf/symbol rendering path.

### Spacing commands
Register each in `node_data.py`. Render function produces a sketch that's
just N space characters wide with horizon=0.

### \phantom
Register with 1 child. Render the child to get its dimensions, then replace
all characters with spaces. Return the invisible sketch.

## Verification

Test every operator above. Verify spacing visually. Run the regression
checks from common-instructions.md.
