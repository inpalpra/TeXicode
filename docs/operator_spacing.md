# Operator Spacing Audit

This document evaluates the current state of operator spacing in TeXicode's output.

## Evaluation: `\hat{x} + \bar{y} + \vec{z}`

**Rendered:**
```
𝑥̂+𝑦̄+𝑧⃗
```

**Rating:** BAD

**Justification:** Missing space after '+'; Missing space before '+'

---

## Evaluation: `\alpha + \beta = \gamma`

**Rendered:**
```
α+β=γ
```

**Rating:** BAD

**Justification:** Missing space after '+'; Missing space after '='; Missing space before '+'; Missing space before '='

---

## Evaluation: `E = mc^2`

**Rendered:**
```
𝐸=𝑚𝑐²
```

**Rating:** BAD

**Justification:** Missing space after '='; Missing space before '='

---

## Evaluation: `\color{red}{x} + y`

**Rendered:**
```
𝑥+𝑦
```

**Rating:** BAD

**Justification:** Missing space after '+'; Missing space before '+'

---

## Evaluation: `\tag{1} E = mc^2`

**Rendered:**
```
𝐸=𝑚𝑐²   (1)
```

**Rating:** BAD

**Justification:** Missing space after '='; Missing space before '='

---

## Evaluation: `\tag*{\dagger} a = b`

**Rendered:**
```
𝑎=𝑏   †
```

**Rating:** BAD

**Justification:** Missing space after '='; Missing space before '='

---

## Evaluation: `\tag{1} \tag{2} a = b`

**Rendered:**
```
𝑎=𝑏   (1) (2)
```

**Rating:** BAD

**Justification:** Missing space after '='; Missing space before '='

---

## Evaluation: `\forall x \exists y`

**Rendered:**
```
∀𝑥∃𝑦
```

**Rating:** GOOD

**Justification:** Spacing appears adequate (or N/A)

---

## Evaluation: `a \approx b \neq c`

**Rendered:**
```
𝑎≈𝑏≠𝑐
```

**Rating:** BAD

**Justification:** Missing space after '≈'; Missing space after '≠'; Missing space before '≈'; Missing space before '≠'

---

## Evaluation: `x \leq y \geq z`

**Rendered:**
```
𝑥≤𝑦≥𝑧
```

**Rating:** BAD

**Justification:** Missing space after '≤'; Missing space after '≥'; Missing space before '≤'; Missing space before '≥'

---

## Evaluation: `S \subset T \supset U`

**Rendered:**
```
𝑆⊂𝑇⊃𝑈
```

**Rating:** BAD

**Justification:** Missing space after '⊂'; Missing space after '⊃'; Missing space before '⊂'; Missing space before '⊃'

---

## Evaluation: `A \subseteq B \supseteq C`

**Rendered:**
```
𝐴⊆𝐵⊇𝐶
```

**Rating:** BAD

**Justification:** Missing space after '⊆'; Missing space after '⊇'; Missing space before '⊆'; Missing space before '⊇'

---

## Evaluation: `x \in X \notin Y`

**Rendered:**
```
𝑥∈𝑋∉𝑌
```

**Rating:** BAD

**Justification:** Missing space after '∈'; Missing space after '∉'; Missing space before '∈'; Missing space before '∉'

---

## Evaluation: `\pm \mp \times \div \cdot`

**Rendered:**
```
±∓×÷⋅
```

**Rating:** BAD

**Justification:** Missing space after '±'; Missing space after '×'; Missing space after '÷'; Missing space after '∓'; Missing space before '×'; Missing space before '÷'; Missing space before '∓'; Missing space before '⋅'

---

## Evaluation: `\nabla \partial \infty`

**Rendered:**
```
∇∂∞
```

**Rating:** GOOD

**Justification:** Spacing appears adequate (or N/A)

---

## Evaluation: `\ldots \cdots \vdots \ddots`

**Rendered:**
```
…⋯⋮⋱
```

**Rating:** BAD

**Justification:** Missing space after '…'; Missing space after '⋮'; Missing space after '⋯'; Missing space before '⋮'; Missing space before '⋯'; Missing space before '⋱'

---

