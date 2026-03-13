CORE_TESTS = [
    (r"\frac{1}{2}", ' 1 \n╶─╴\n 2 '),
    (r"\int_0^1 x\,dx = \frac{1}{2}", '⌠          1 \n│₀¹𝑥 𝑑𝑥 = ╶─╴\n⌡          2 '),
    (r"\sum_{i=0}^{n} x_i", '  𝑛    \n ┰─╴   \n ▐╸  𝑥ᵢ\n ┸─╴   \n𝑖 = 0  '),
    (r"\left( \frac{a}{b} \right)", '⎛ 𝑎 ⎞\n⎜╶─╴⎟\n⎝ 𝑏 ⎠'),
    (r"\hat{x} + \bar{y} + \vec{z}", '𝑥̂ + 𝑦̄ + 𝑧⃗'),
    (r"\alpha + \beta = \gamma", 'α + β = γ'),
    (r"E = mc^2", '𝐸 = 𝑚𝑐²'),
    (r"\binom{n}{k}", '⎛𝑛⎞\n⎜ ⎟\n⎝𝑘⎠'),
    (r"\sqrt{\frac{a^2+b^2}{c^2}}", ' ┌─────────╴\n │ 𝑎² + 𝑏²  \n │╶───────╴ \n╰┘   𝑐²     '),
    (r"\lim_{x \to \infty} f(x)", 'lim𝑓(𝑥)\n𝑥→∞    '),
    (r"\begin{align} a &= b + c \\ d &= e + f \end{align}", '𝑎 = 𝑏 + 𝑐\n𝑑 = 𝑒 + 𝑓'),
]

ALIGNMENT_TESTS = [
    (r"\begin{aligned} a &= b + c \\ d &= e + f \end{aligned}", '𝑎 = 𝑏 + 𝑐\n𝑑 = 𝑒 + 𝑓'),
    (r"\begin{cases} x & \text{if } x > 0 \\ -x & \text{otherwise} \end{cases}", '⎧ 𝑥  if 𝑥>0    \n⎨              \n⎩ -𝑥 otherwise \n               '),
    (r"\begin{cases} 1 & x > 0 \\ 0 & x = 0 \\ -1 & x < 0 \end{cases}", '⎧ 1  𝑥>0   \n⎨ 0  𝑥 = 0 \n⎩ -1 𝑥<0   \n           '),
    (r"\begin{aligned} y &= \frac{a}{b} \\ z &= c + d \end{aligned}", '     𝑎   \n𝑦 = ╶─╴  \n     𝑏   \n𝑧 = 𝑐 + 𝑑'),
    (r"\begin{gather} a + b = c \\ x + y = z \end{gather}", '𝑎 + 𝑏 = 𝑐\n𝑥 + 𝑦 = 𝑧'),
    (r"\begin{array}{lcr} \frac{1}{2} & X & a \\ z & Y & bcd \end{array}", ' 1       \n╶─╴ 𝑋   𝑎\n 2       \n𝑧   𝑌 𝑏𝑐𝑑'),
]

MATRIX_TESTS = [
    (r"\begin{bmatrix} b_{d1} \\ b_{d2} \\ b_{c1} \\ b_{c2} \end{bmatrix} = \begin{bmatrix} S_{dd11} & S_{ddpq12} & S_{dc11} & S_{dc12} \\ S_{dd21}^{56} & S & S_{dc21} & S_{dc22} \\ S_{cd11} & S_{cd12} & S_{cc11} & S_{cc12} \\ S_{cd21} & S_{cd422} & S_{cc21} & S_{cc22} \end{bmatrix} \cdot \begin{bmatrix} a_{d1} \\ a_{c2} \\ a_{c1} \\ a_{c2} \end{bmatrix}", '⎡ 𝑏_𝑑1 ⎤   ⎡  𝑆_𝑑𝑑11  𝑆_𝑑𝑑𝑝𝑞12 𝑆_𝑑𝑐11 𝑆_𝑑𝑐12 ⎤   ⎡ 𝑎_𝑑1 ⎤\n⎢ 𝑏_𝑑2 ⎥   ⎢ 𝑆_𝑑𝑑21⁵⁶    𝑆     𝑆_𝑑𝑐21 𝑆_𝑑𝑐22 ⎥   ⎢ 𝑎_𝑐2 ⎥\n⎢ 𝑏_𝑐1 ⎥ = ⎢  𝑆_𝑐𝑑11   𝑆_𝑐𝑑12  𝑆_𝑐𝑐11 𝑆_𝑐𝑐12 ⎥ ⋅ ⎢ 𝑎_𝑐1 ⎥\n⎣ 𝑏_𝑐2 ⎦   ⎣  𝑆_𝑐𝑑21  𝑆_𝑐𝑑422  𝑆_𝑐𝑐21 𝑆_𝑐𝑐22 ⎦   ⎣ 𝑎_𝑐2 ⎦'),
    (r"\begin{bmatrix} b_1 \\ b_2 \end{bmatrix} = \begin{bmatrix} S_{11} & S_{12} \\ S_{21} & S_{22} \end{bmatrix} \begin{bmatrix} a_1 \\ a_2 \end{bmatrix}", '⎡ 𝑏₁ ⎤   ⎡ 𝑆₁₁ 𝑆₁₂ ⎤⎡ 𝑎₁ ⎤\n⎣ 𝑏₂ ⎦ = ⎣ 𝑆₂₁ 𝑆₂₂ ⎦⎣ 𝑎₂ ⎦'),
    (r"\begin{aligned} b_1 &= S_{11}a_1 + S_{12}a_2 \\ b_2 &= S_{21}a_1 + S_{22}a_2 \end{aligned}", '𝑏₁ = 𝑆₁₁𝑎₁ + 𝑆₁₂𝑎₂\n𝑏₂ = 𝑆₂₁𝑎₁ + 𝑆₂₂𝑎₂'),
    (r"\begin{bmatrix} a & b \\ c & d \end{bmatrix}", '⎡ 𝑎 𝑏 ⎤\n⎣ 𝑐 𝑑 ⎦'),
    (r"M = \begin{bmatrix} a & b \\ c & d \end{bmatrix}", '    ⎡ 𝑎 𝑏 ⎤\n𝑀 = ⎣ 𝑐 𝑑 ⎦'),
    (r"\begin{pmatrix} a & b \\ c & d \end{pmatrix}", '⎛ 𝑎 𝑏 ⎞\n⎝ 𝑐 𝑑 ⎠'),
    (r"\begin{bmatrix} a & b & c \\ d & e & f \\ g & h & i \end{bmatrix}", '⎡ 𝑎 𝑏 𝑐 ⎤\n⎢ 𝑑 𝑒 𝑓 ⎥\n⎣ 𝑔 ℎ 𝑖 ⎦'),
    (r"\begin{pmatrix} \frac{1}{2} & 0 \\ 0 & 1 \end{pmatrix}", '⎛  1    ⎞\n⎜ ╶─╴ 0 ⎟\n⎜  2    ⎟\n⎝  0  1 ⎠'),
    (r"\begin{matrix} a & b \\ c & d \end{matrix}", '𝑎 𝑏\n𝑐 𝑑'),
    (r"\begin{vmatrix} a & b \\ c & d \end{vmatrix}", '│ 𝑎 𝑏 │\n│ 𝑐 𝑑 │'),
    (r"\begin{bmatrix} x \\ y \\ z \end{bmatrix}", '⎡ 𝑥 ⎤\n⎢ 𝑦 ⎥\n⎣ 𝑧 ⎦'),
]

MATRIX_BRACE_TESTS = [
    (r"\overbrace{\begin{matrix} x_{11} \end{matrix}}^{top}", '𝑡𝑜𝑝\n╭┴╮\n𝑥₁₁'),
    (r"\underbrace{\begin{matrix} x_{11} \end{matrix}}_{btm}", '𝑥₁₁\n╰┬╯\n𝑏𝑡𝑚'),
    (r"\overbrace{\begin{matrix} x_{11} & x_{12} \end{matrix}}^{top}", '  𝑡𝑜𝑝  \n╭──┴──╮\n𝑥₁₁ 𝑥₁₂'),
    (r"\underbrace{\begin{matrix} x_{11} & x_{12} \end{matrix}}_{btm}", '𝑥₁₁ 𝑥₁₂\n╰──┬──╯\n  𝑏𝑡𝑚  '),
    (r"\overbrace{\begin{matrix} x_{11} & x_{12} \\ x_{21} & x_{22} \end{matrix}}^{top}", '  𝑡𝑜𝑝  \n╭──┴──╮\n𝑥₁₁ 𝑥₁₂\n𝑥₂₁ 𝑥₂₂'),
    (r"\underbrace{\begin{matrix} x_{11} & x_{12} \\ x_{21} & x_{22} \end{matrix}}_{btm}", '𝑥₁₁ 𝑥₁₂\n𝑥₂₁ 𝑥₂₂\n╰──┬──╯\n  𝑏𝑡𝑚  '),
    (r"\overbrace{\begin{matrix} x_{11} \\ x_{21} \end{matrix}}^{top}", '𝑡𝑜𝑝\n╭┴╮\n𝑥₁₁\n𝑥₂₁'),
    (r"\underbrace{\begin{matrix} x_{11} \\ x_{21} \end{matrix}}_{btm}", '𝑥₁₁\n𝑥₂₁\n╰┬╯\n𝑏𝑡𝑚'),
    (r"\overbrace{\begin{matrix} x_{11} & x_{12} & x_{13} \\ x_{21} & x_{22} & x_{23} \end{matrix}}^{top}", '    𝑡𝑜𝑝    \n╭────┴────╮\n𝑥₁₁ 𝑥₁₂ 𝑥₁₃\n𝑥₂₁ 𝑥₂₂ 𝑥₂₃'),
    (r"\underbrace{\begin{matrix} x_{11} & x_{12} & x_{13} \\ x_{21} & x_{22} & x_{23} \end{matrix}}_{btm}", '𝑥₁₁ 𝑥₁₂ 𝑥₁₃\n𝑥₂₁ 𝑥₂₂ 𝑥₂₃\n╰────┬────╯\n    𝑏𝑡𝑚    '),
    (r"\overbrace{\begin{matrix} x_{11} & x_{12} \\ x_{21} & x_{22} \\ x_{31} & x_{32} \end{matrix}}^{top}", '  𝑡𝑜𝑝  \n╭──┴──╮\n𝑥₁₁ 𝑥₁₂\n𝑥₂₁ 𝑥₂₂\n𝑥₃₁ 𝑥₃₂'),
    (r"\underbrace{\begin{matrix} x_{11} & x_{12} \\ x_{21} & x_{22} \\ x_{31} & x_{32} \end{matrix}}_{btm}", '𝑥₁₁ 𝑥₁₂\n𝑥₂₁ 𝑥₂₂\n𝑥₃₁ 𝑥₃₂\n╰──┬──╯\n  𝑏𝑡𝑚  '),
    (r"\overbrace{\begin{matrix} x_{11} & x_{12} & x_{13} & x_{14} \\ x_{21} & x_{22} & x_{23} & x_{24} \\ x_{31} & x_{32} & x_{33} & x_{34} \end{matrix}}^{top}", '      𝑡𝑜𝑝      \n╭──────┴──────╮\n𝑥₁₁ 𝑥₁₂ 𝑥₁₃ 𝑥₁₄\n𝑥₂₁ 𝑥₂₂ 𝑥₂₃ 𝑥₂₄\n𝑥₃₁ 𝑥₃₂ 𝑥₃₃ 𝑥₃₄'),
    (r"\underbrace{\begin{matrix} x_{11} & x_{12} & x_{13} & x_{14} \\ x_{21} & x_{22} & x_{23} & x_{24} \\ x_{31} & x_{32} & x_{33} & x_{34} \end{matrix}}_{btm}", '𝑥₁₁ 𝑥₁₂ 𝑥₁₃ 𝑥₁₄\n𝑥₂₁ 𝑥₂₂ 𝑥₂₃ 𝑥₂₄\n𝑥₃₁ 𝑥₃₂ 𝑥₃₃ 𝑥₃₄\n╰──────┬──────╯\n      𝑏𝑡𝑚      '),
    (r"\overbrace{\begin{matrix} x_{11} & x_{12} & x_{13} \\ x_{21} & x_{22} & x_{23} \\ x_{31} & x_{32} & x_{33} \\ x_{41} & x_{42} & x_{43} \end{matrix}}^{top}", '    𝑡𝑜𝑝    \n╭────┴────╮\n𝑥₁₁ 𝑥₁₂ 𝑥₁₃\n𝑥₂₁ 𝑥₂₂ 𝑥₂₃\n𝑥₃₁ 𝑥₃₂ 𝑥₃₃\n𝑥₄₁ 𝑥₄₂ 𝑥₄₃'),
    (r"\underbrace{\begin{matrix} x_{11} & x_{12} & x_{13} \\ x_{21} & x_{22} & x_{23} \\ x_{31} & x_{32} & x_{33} \\ x_{41} & x_{42} & x_{43} \end{matrix}}_{btm}", '𝑥₁₁ 𝑥₁₂ 𝑥₁₃\n𝑥₂₁ 𝑥₂₂ 𝑥₂₃\n𝑥₃₁ 𝑥₃₂ 𝑥₃₃\n𝑥₄₁ 𝑥₄₂ 𝑥₄₃\n╰────┬────╯\n    𝑏𝑡𝑚    '),
    (r"\overbrace{\begin{matrix} x_{11} & x_{12} & x_{13} & x_{14} & x_{15} \\ x_{21} & x_{22} & x_{23} & x_{24} & x_{25} \end{matrix}}^{top}", '        𝑡𝑜𝑝        \n╭────────┴────────╮\n𝑥₁₁ 𝑥₁₂ 𝑥₁₃ 𝑥₁₄ 𝑥₁₅\n𝑥₂₁ 𝑥₂₂ 𝑥₂₃ 𝑥₂₄ 𝑥₂₅'),
    (r"\underbrace{\begin{matrix} x_{11} & x_{12} & x_{13} & x_{14} & x_{15} \\ x_{21} & x_{22} & x_{23} & x_{24} & x_{25} \end{matrix}}_{btm}", '𝑥₁₁ 𝑥₁₂ 𝑥₁₃ 𝑥₁₄ 𝑥₁₅\n𝑥₂₁ 𝑥₂₂ 𝑥₂₃ 𝑥₂₄ 𝑥₂₅\n╰────────┬────────╯\n        𝑏𝑡𝑚        '),
    (r"\overbrace{\begin{matrix} x_{11} & x_{12} & x_{13} & x_{14} & x_{15} & x_{16} \\ x_{21} & x_{22} & x_{23} & x_{24} & x_{25} & x_{26} \\ x_{31} & x_{32} & x_{33} & x_{34} & x_{35} & x_{36} \end{matrix}}^{top}", '          𝑡𝑜𝑝          \n╭──────────┴──────────╮\n𝑥₁₁ 𝑥₁₂ 𝑥₁₃ 𝑥₁₄ 𝑥₁₅ 𝑥₁₆\n𝑥₂₁ 𝑥₂₂ 𝑥₂₃ 𝑥₂₄ 𝑥₂₅ 𝑥₂₆\n𝑥₃₁ 𝑥₃₂ 𝑥₃₃ 𝑥₃₄ 𝑥₃₅ 𝑥₃₆'),
    (r"\underbrace{\begin{matrix} x_{11} & x_{12} & x_{13} & x_{14} & x_{15} & x_{16} \\ x_{21} & x_{22} & x_{23} & x_{24} & x_{25} & x_{26} \\ x_{31} & x_{32} & x_{33} & x_{34} & x_{35} & x_{36} \end{matrix}}_{btm}", '𝑥₁₁ 𝑥₁₂ 𝑥₁₃ 𝑥₁₄ 𝑥₁₅ 𝑥₁₆\n𝑥₂₁ 𝑥₂₂ 𝑥₂₃ 𝑥₂₄ 𝑥₂₅ 𝑥₂₆\n𝑥₃₁ 𝑥₃₂ 𝑥₃₃ 𝑥₃₄ 𝑥₃₅ 𝑥₃₆\n╰──────────┬──────────╯\n          𝑏𝑡𝑚          '),
]

OPERATOR_TESTS = [
    (r"A \implies B", '𝐴 ==> 𝐵'),
    (r"A \iff B", '𝐴 <==> 𝐵'),
    (r"\therefore \because", '∴∵'),
    (r"\forall x \exists y", '∀ 𝑥 ∃ 𝑦'),
    (r"a \approx b \neq c", '𝑎 ≈ 𝑏 ≠ 𝑐'),
    (r"x \leq y \geq z", '𝑥 ≤ 𝑦 ≥ 𝑧'),
    (r"S \subset T \supset U", '𝑆 ⊂ 𝑇 ⊃ 𝑈'),
    (r"A \subseteq B \supseteq C", '𝐴 ⊆ 𝐵 ⊇ 𝐶'),
    (r"x \in X \notin Y", '𝑥 ∈ 𝑋 ∉ 𝑌'),
    (r"\pm \mp \times \div \cdot", '± ∓ × ÷ ⋅'),
    (r"\nabla \partial \infty", '∇∂∞'),
    (r"\ldots \cdots \vdots \ddots", '…⋯⋮⋱'),
]

OVERSET_TESTS = [
    (r"\overset{\text{def}}{=}", 'def\n = '),
    (r"\underset{x \to 0}{\lim}", 'lim\n𝑥→0'),
    (r"\underbrace{a+b+c}_{3\text{ terms}}", '𝑎 + 𝑏 + 𝑐\n╰───┬───╯\n 3 terms '),
    (r"\overbrace{x+y}^{2}", '  2  \n╭─┴─╮\n𝑥 + 𝑦'),
    (r"\xrightarrow{\text{yields}}", ' yields \n───────>'),
    (r"\xrightarrow[below]{above}", ' 𝑎𝑏𝑜𝑣𝑒 \n──────>\n 𝑏𝑒𝑙𝑜𝑤 '),
    (r"\overbrace{\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}}^{I_3}", '   𝐼₃    \n╭───┴───╮\n⎡ 1 0 0 ⎤\n⎢ 0 1 0 ⎥\n⎣ 0 0 1 ⎦'),
    (r"\underbrace{\begin{matrix} a & b & c \\ d & e & f \\ g & h & i \end{matrix}}_{M}", '𝑎 𝑏 𝑐\n𝑑 𝑒 𝑓\n𝑔 ℎ 𝑖\n╰─┬─╯\n  𝑀  '),
]

SPACING_TESTS = [
    (r"a \quad b", '𝑎  𝑏'),
    (r"a \qquad b", '𝑎    𝑏'),
    (r"a\,b", '𝑎 𝑏'),
    (r"a\;b", '𝑎 𝑏'),
    (r"a\:b", '𝑎 𝑏'),
    (r"a\!b", '𝑎𝑏'),
    (r"a\hspace{1em}b", '𝑎  𝑏'),
    (r"a\hspace{2em}b", '𝑎    𝑏'),
    (r"a\phantom{xxx}b", '𝑎   𝑏'),
    (r"\frac{a}{\phantom{b}}", ' 𝑎 \n╶─╴\n   '),
]

TAG_TESTS = [
    (r"\tag{1} E = mc^2", '𝐸 = 𝑚𝑐²   (1)'),
    (r"\tag*{\dagger} a = b", '𝑎 = 𝑏   †'),
    (r"\tag{2.1} \int_0^1 x\,dx = \frac{1}{2}", '⌠          1       \n│₀¹𝑥 𝑑𝑥 = ╶─╴   (2.1)\n⌡          2       '),
    (r"\begin{align} a &= b \tag{1} \\ c &= d \end{align}", '𝑎 = 𝑏   (1)\n𝑐 = 𝑑    '),
    (r"\tag{1} \tag{2} a = b", '𝑎 = 𝑏   (1) (2)'),
]

STYLING_TESTS = [
    (r"\boxed{a + b}", '┏━━━━━┓\n┃𝑎 + 𝑏┃\n┗━━━━━┛'),
    (r"\boxed{\frac{a}{b}}", '┏━━━┓\n┃ 𝑎 ┃\n┃╶─╴┃\n┃ 𝑏 ┃\n┗━━━┛'),
    (r"\cancel{x}", '𝑥̶'),
    (r"\color{red}{x} + y", '𝑥 + 𝑦'),
    (r"\colorbox{yellow}{x^2}", '𝑥²'),
    (r"\fcolorbox{red}{blue}{x}", '┏━┓\n┃𝑥┃\n┗━┛'),
    (r"\frac{\cancel{(x-1)}(x+2)}{(x-3)\cancel{(x-1)}}", ' (̶𝑥̶ -̶ 1̶)̶(𝑥 + 2) \n╶──────────────╴\n (𝑥 - 3)(̶𝑥̶ -̶ 1̶)̶ '),
]

GRACEFUL_DEGRADATION_TESTS = [
    (r"\unknown{x}", '\\unknown{𝑥}'),
    (r"\unknown{\frac{1}{2}}", '          1  \n\\unknown{╶─╴}\n          2  '),
    (r"\begin{myfile} x \end{myfile}", '\\begin{myfile}\n𝑥             \n\\end{myfile}  '),
]

COLOR_TESTS = [
    (r"\color{red}{x} + y", '\x1b[31m𝑥\x1b[39m + 𝑦'),
    (r"\colorbox{yellow}{x}", '\x1b[43m𝑥\x1b[49m'),
]
