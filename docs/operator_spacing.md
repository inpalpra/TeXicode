# Operator Spacing Audit

| LaTeX String | Rendered Output | Rating | Justification |
|--------------|-----------------|--------|---------------|
| `\int_0^1 x\,dx = \frac{1}{2}` | <pre>⌠        1 <br>│₀¹𝑥 𝑑𝑥=╶─╴<br>⌡        2 </pre> | [ ] GOOD <br> [x] BAD | Missing spaces around '=' |
| `\sum_{i=0}^{n} x_i` | <pre> 𝑛   <br>┰─╴  <br>▐╸ 𝑥ᵢ<br>┸─╴  <br>𝑖=0  </pre> | [ ] GOOD <br> [x] BAD | Missing spaces around '=' in subscript |
| `\hat{x} + \bar{y} + \vec{z}` | <pre>𝑥̂+𝑦̄+𝑧⃗</pre> | [ ] GOOD <br> [x] BAD | Missing spaces around '+' |
| `\alpha + \beta = \gamma` | <pre>α+β=γ</pre> | [ ] GOOD <br> [x] BAD | Missing spaces around '+' and '=' |
| `E = mc^2` | <pre>𝐸=𝑚𝑐²</pre> | [ ] GOOD <br> [x] BAD | Missing spaces around '=' |
| `\sqrt{\frac{a^2+b^2}{c^2}}` | <pre> ┌───────╴<br> │ 𝑎²+𝑏²  <br> │╶─────╴ <br>╰┘  𝑐²    </pre> | [ ] GOOD <br> [x] BAD | Missing spaces around '+' |
| `\begin{align} a &= b + c \\ d &= e + f \end{align}` | <pre>𝑎=𝑏+𝑐<br>𝑑=𝑒+𝑓</pre> | [ ] GOOD <br> [x] BAD | Missing spaces around '=' and '+' |
| `\begin{aligned} a &= b + c \\ d &= e + f \end{aligned}` | <pre>𝑎 =𝑏+𝑐<br>𝑑 =𝑒+𝑓</pre> | [ ] GOOD <br> [x] BAD | Missing space after '=' and around '+' |
| `\begin{cases} 1 & x > 0 \\ 0 & x = 0 \\ -1 & x < 0 \end{cases}` | <pre>⎧ 1  𝑥>0 <br>⎨ 0  𝑥=0 <br>⎩ -1 𝑥<0 <br>         </pre> | [ ] GOOD <br> [x] BAD | Missing spaces around '>' and '=' |
| `\begin{aligned} y &= \frac{a}{b} \\ z &= c + d \end{aligned}` | <pre>    𝑎 <br>𝑦 =╶─╴<br>    𝑏 <br>𝑧 =𝑐+𝑑</pre> | [ ] GOOD <br> [x] BAD | Missing space after '=' in first line, and around '=' and '+' in second |
| `\begin{gather} a + b = c \\ x + y = z \end{gather}` | <pre>𝑎+𝑏=𝑐<br>𝑥+𝑦=𝑧</pre> | [ ] GOOD <br> [x] BAD | Missing spaces around '+' and '=' |
| `\begin{bmatrix} b_1 \\ b_2 \end{bmatrix} = \begin{bmatrix} S_{11} & S_{12} \\ S_{21} & S_{22} \end{bmatrix} \begin{bmatrix} a_1 \\ a_2 \end{bmatrix}` | <pre>⎡ 𝑏₁ ⎤ ⎡ 𝑆₁₁ 𝑆₁₂ ⎤⎡ 𝑎₁ ⎤<br>⎣ 𝑏₂ ⎦=⎣ 𝑆₂₁ 𝑆₂₂ ⎦⎣ 𝑎₂ ⎦</pre> | [ ] GOOD <br> [x] BAD | Missing spaces around '=' |
| `\overset{\text{def}}{=}` | <pre> def <br>  =  </pre> | [ ] GOOD <br> [x] BAD | '=' is correctly centered but the expression as a whole might need padding |
| `\underbrace{a+b+c}_{3\text{ terms}}` | <pre>  𝑎+𝑏+𝑐 <br> ╰──┬──╯<br> 3 terms</pre> | [ ] GOOD <br> [x] BAD | Missing spaces around '+' |
| `A \implies B` | <pre>𝐴⟹𝐵</pre> | [ ] GOOD <br> [x] BAD | Missing spaces around '⟹' |
| `a \approx b \neq c` | <pre>𝑎≈𝑏≠𝑐</pre> | [ ] GOOD <br> [x] BAD | Missing spaces around '≈' and '≠' |
| `x \in X \notin Y` | <pre>𝑥∈𝑋∉𝑌</pre> | [ ] GOOD <br> [x] BAD | Missing spaces around '∈' and '∉' |
| `\pm \mp \times \div \cdot` | <pre>±∓×÷⋅</pre> | [ ] GOOD <br> [x] BAD | No spacing between operators |
| `a \quad b` | <pre>𝑎  𝑏</pre> | [x] GOOD <br> [ ] BAD | Explicit spacing command (\quad) works correctly |
