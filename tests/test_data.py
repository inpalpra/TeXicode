# tests/test_data.py

CORE_TESTS = [
    (
        r'\frac{1}{2}',
        "  1 \n"
        " ╶─╴\n"
        "  2 "
    ),
    (
        r'\int_0^1 x\,dx = \frac{1}{2}',
        " ⌠        1 \n"
        " │₀¹𝑥 𝑑𝑥=╶─╴\n"
        " ⌡        2 "
    ),
    (
        r'\sum_{i=0}^{n} x_i',
        "  ⁿ   \n"
        " ┰─╴  \n"
        " ▐╸ 𝑥ᵢ\n"
        " ┸─╴  \n"
        " ᵢ₌₀  "
    ),
    (
        r'\left( \frac{a}{b} \right)',
        " ⎛ 𝑎 ⎞\n"
        " ⎜╶─╴⎟\n"
        " ⎝ 𝑏 ⎠"
    ),
    (
        r'\hat{x} + \bar{y} + \vec{z}',
        " 𝑥̂+𝑦̄+𝑧⃗"
    ),
    (
        r'\alpha + \beta = \gamma',
        " α+β=γ"
    ),
    (
        r'E = mc^2',
        " 𝐸=𝑚𝑐²"
    ),
    (
        r'\binom{n}{k}',
        " ⎛𝑛⎞\n"
        " ⎜ ⎟\n"
        " ⎝𝑘⎠"
    ),
    (
        r'\sqrt{\frac{a^2+b^2}{c^2}}',
        "  ┌───────╴\n"
        "  │ 𝑎²+𝑏²  \n"
        "  │╶─────╴ \n"
        " ╰┘  𝑐²    "
    ),
    (
        r'\lim_{x \to \infty} f(x)',
        " lim𝑓(𝑥)\n"
        " 𝑥→∞    "
    ),
    (
        r'\begin{align} a &= b + c \\ d &= e + f \end{align}',
        "𝑎=𝑏+𝑐\n"
        "     \n"
        "𝑑=𝑒+𝑓"
    )
]

ALIGNMENT_TESTS = [
    (
        r'\begin{aligned} a &= b + c \\ d &= e + f \end{aligned}',
        " 𝑎 =𝑏+𝑐\n"
        " 𝑑 =𝑒+𝑓"
    ),
    (
        r'\begin{cases} x & \text{if } x > 0 \\ -x & \text{otherwise} \end{cases}',
        " ⎧ 𝑥  if 𝑥>0    \n"
        " ⎨              \n"
        " ⎩ -𝑥 otherwise \n"
        "                "
    ),
    (
        r'\begin{cases} 1 & x > 0 \\ 0 & x = 0 \\ -1 & x < 0 \end{cases}',
        " ⎧ 1  𝑥>0 \n"
        " ⎨ 0  𝑥=0 \n"
        " ⎩ -1 𝑥<0 \n"
        "          "
    ),
    (
        r'\begin{aligned} y &= \frac{a}{b} \\ z &= c + d \end{aligned}',
        "     𝑎 \n"
        " 𝑦 =╶─╴\n"
        "     𝑏 \n"
        " 𝑧 =𝑐+𝑑"
    ),
    (
        r'\begin{gather} a + b = c \\ x + y = z \end{gather}',
        " 𝑎+𝑏=𝑐\n"
        " 𝑥+𝑦=𝑧"
    ),
    (
        r'\begin{array}{lcr} \frac{1}{2} & X & a \\ z & Y & bcd \end{array}',
        "  1       \n"
        " ╶─╴ 𝑋   𝑎\n"
        "  2       \n"
        " 𝑧   𝑌 𝑏𝑐𝑑"
    )
]

MATRIX_TESTS = [
    (
        r'\begin{bmatrix} b_{d1} \\ b_{d2} \\ b_{c1} \\ b_{c2} \end{bmatrix} = \begin{bmatrix} S_{dd11} & S_{ddpq12} & S_{dc11} & S_{dc12} \\ S_{dd21}^{56} & S & S_{dc21} & S_{dc22} \\ S_{cd11} & S_{cd12} & S_{cc11} & S_{cc12} \\ S_{cd21} & S_{cd422} & S_{cc21} & S_{cc22} \end{bmatrix} \cdot \begin{bmatrix} a_{d1} \\ a_{c2} \\ a_{c1} \\ a_{c2} \end{bmatrix}',
        "⎡ 𝑏_𝑑1 ⎤ ⎡  𝑆_𝑑𝑑11  𝑆_𝑑𝑑𝑝𝑞12 𝑆_𝑑𝑐11 𝑆_𝑑𝑐12 ⎤ ⎡ 𝑎_𝑑1 ⎤\n"
        "⎢ 𝑏_𝑑2 ⎥ ⎢ 𝑆_𝑑𝑑21⁵⁶    𝑆     𝑆_𝑑𝑐21 𝑆_𝑑𝑐22 ⎥ ⎢ 𝑎_𝑐2 ⎥\n"
        "⎢ 𝑏_𝑐1 ⎥=⎢  𝑆_𝑐𝑑11   𝑆_𝑐𝑑12  𝑆_𝑐𝑐11 𝑆_𝑐𝑐12 ⎥⋅⎢ 𝑎_𝑐1 ⎥\n"
        "⎣ 𝑏_𝑐2 ⎦ ⎣  𝑆_𝑐𝑑21  𝑆_𝑐𝑑422  𝑆_𝑐𝑐21 𝑆_𝑐𝑐22 ⎦ ⎣ 𝑎_𝑐2 ⎦"
    ),
    (
        r'\begin{bmatrix} b_1 \\ b_2 \end{bmatrix} = \begin{bmatrix} S_{11} & S_{12} \\ S_{21} & S_{22} \end{bmatrix} \begin{bmatrix} a_1 \\ a_2 \end{bmatrix}',
        "⎡ 𝑏₁ ⎤ ⎡ 𝑆₁₁ 𝑆₁₂ ⎤⎡ 𝑎₁ ⎤\n"
        "⎣ 𝑏₂ ⎦=⎣ 𝑆₂₁ 𝑆₂₂ ⎦⎣ 𝑎₂ ⎦"
    ),
    (
        r'\begin{aligned} b_1 &= S_{11}a_1 + S_{12}a_2 \\ b_2 &= S_{21}a_1 + S_{22}a_2 \end{aligned}',
        " 𝑏₁ =𝑆₁₁𝑎₁+𝑆₁₂𝑎₂\n"
        " 𝑏₂ =𝑆₂₁𝑎₁+𝑆₂₂𝑎₂"
    ),
    (
        r'\begin{bmatrix} a & b \\ c & d \end{bmatrix}',
        " ⎡ 𝑎 𝑏 ⎤\n"
        " ⎣ 𝑐 𝑑 ⎦"
    ),
    (
        r'\begin{pmatrix} a & b \\ c & d \end{pmatrix}',
        " ⎛ 𝑎 𝑏 ⎞\n"
        " ⎝ 𝑐 𝑑 ⎠"
    ),
    (
        r'\begin{bmatrix} a & b & c \\ d & e & f \\ g & h & i \end{bmatrix}',
        " ⎡ 𝑎 𝑏 𝑐 ⎤\n"
        " ⎢ 𝑑 𝑒 𝑓 ⎥\n"
        " ⎣ 𝑔 ℎ 𝑖 ⎦"
    ),
    (
        r'\begin{pmatrix} \frac{1}{2} & 0 \\ 0 & 1 \end{pmatrix}',
        " ⎛  1    ⎞\n"
        " ⎜ ╶─╴ 0 ⎟\n"
        " ⎜  2    ⎟\n"
        " ⎝  0  1 ⎠"
    ),
    (
        r'\begin{matrix} a & b \\ c & d \end{matrix}',
        " 𝑎 𝑏\n"
        " 𝑐 𝑑"
    ),
    (
        r'\begin{vmatrix} a & b \\ c & d \end{vmatrix}',
        " │ 𝑎 𝑏 │\n"
        " │ 𝑐 𝑑 │"
    ),
    (
        r'\begin{bmatrix} x \\ y \\ z \end{bmatrix}',
        " ⎡ 𝑥 ⎤\n"
        " ⎢ 𝑦 ⎥\n"
        " ⎣ 𝑧 ⎦"
    )
]

OVERSET_TESTS = [
    (
        r'\overset{\text{def}}{=}',
        " def \n"
        "  =  "
    ),
    (
        r'\underset{x \to 0}{\lim}',
        " lim \n"
        " 𝑥→0 "
    ),
    (
        r'\underbrace{a+b+c}_{3\text{ terms}}',
        "  𝑎+𝑏+𝑐 \n"
        " ╰──┬──╯\n"
        " 3 terms"
    ),
    (
        r'\overbrace{x+y}^{2}',
        "   ²  \n"
        " ╭─┴─╮\n"
        "  𝑥+𝑦 "
    ),
    (
        r'\xrightarrow{\text{yields}}',
        "  yields \n"
        " ───────>"
    ),
    (
        r'\xrightarrow[below]{above}',
        "  above \n"
        " ──────>\n"
        "  below "
    ),
    (
        r'\overbrace{\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}}^{I_3}',
        "     ᴵ₃    \n"
        " ╭───┴────╮\n"
        "  ⎡ 1 0 0 ⎤\n"
        "  ⎢ 0 1 0 ⎥\n"
        "  ⎣ 0 0 1 ⎦"
    ),
    (
        r'\underbrace{\begin{matrix} a & b & c \\ d & e & f \\ g & h & i \end{matrix}}_{M}',
        "  𝑎 𝑏 𝑐\n"
        "  𝑑 𝑒 𝑓\n"
        "  𝑔 ℎ 𝑖\n"
        " ╰─┬──╯\n"
        "   𝑀   "
    )
]

MATRIX_BRACE_TESTS = [
    (r"\overbrace{\begin{matrix} x_{11} \end{matrix}}^{top}", " top \n ╭┴╮ \n x₁₁\n"),
    (r"\underbrace{\begin{matrix} x_{11} \end{matrix}}_{btm}", " x₁₁ \n ╰┬╯ \n btm\n"),
    (r"\overbrace{\begin{matrix} x_{11} & x_{12} \end{matrix}}^{top}", "   top   \n ╭──┴──╮ \n x₁₁ x₁₂\n"),
    (r"\underbrace{\begin{matrix} x_{11} & x_{12} \end{matrix}}_{btm}", " x₁₁ x₁₂ \n ╰──┬──╯ \n   btm  \n"),
    (r"\overbrace{\begin{matrix} x_{11} & x_{12} \\ x_{21} & x_{22} \end{matrix}}^{top}", "   top    \n ╭──┴───╮ \n  x₁₁ x₁₂ \n  x₂₁ x₂₂ \n"),
    (r"\underbrace{\begin{matrix} x_{11} & x_{12} \\ x_{21} & x_{22} \end{matrix}}_{btm}", "  x₁₁ x₁₂ \n  x₂₁ x₂₂ \n ╰──┬───╯ \n   btm    \n"),
    (r"\overbrace{\begin{matrix} x_{11} \\ x_{21} \end{matrix}}^{top}", " top  \n ╭┴─╮  \n  x₁₁ \n  x₂₁ \n"),
    (r"\underbrace{\begin{matrix} x_{11} \\ x_{21} \end{matrix}}_{btm}", "  x₁₁ \n  x₂₁ \n ╰┬─╯  \n btm  \n"),
    (r"\overbrace{\begin{matrix} x_{11} & x_{12} & x_{13} \\ x_{21} & x_{22} & x_{23} \end{matrix}}^{top}", "     top      \n ╭────┴─────╮ \n  x₁₁ x₁₂ x₁₃ \n  x₂₁ x₂₂ x₂₃ \n"),
    (r"\underbrace{\begin{matrix} x_{11} & x_{12} & x_{13} \\ x_{21} & x_{22} & x_{23} \end{matrix}}_{btm}", "  x₁₁ x₁₂ x₁₃ \n  x₂₁ x₂₂ x₂₃ \n ╰────┬─────╯ \n     btm      \n"),
    (r"\overbrace{\begin{matrix} x_{11} & x_{12} \\ x_{21} & x_{22} \\ x_{31} & x_{32} \end{matrix}}^{top}", "   top    \n ╭──┴───╮ \n  x₁₁ x₁₂ \n  x₂₁ x₂₂ \n  x₃₁ x₃₂ \n"),
    (r"\underbrace{\begin{matrix} x_{11} & x_{12} \\ x_{21} & x_{22} \\ x_{31} & x_{32} \end{matrix}}_{btm}", "  x₁₁ x₁₂ \n  x₂₁ x₂₂ \n  x₃₁ x₃₂ \n ╰──┬───╯ \n   btm    \n"),
    (r"\overbrace{\begin{matrix} x_{11} & x_{12} & x_{13} & x_{14} \\ x_{21} & x_{22} & x_{23} & x_{24} \\ x_{31} & x_{32} & x_{33} & x_{34} \end{matrix}}^{top}", "       top        \n ╭──────┴───────╮ \n  x₁₁ x₁₂ x₁₃ x₁₄ \n  x₂₁ x₂₂ x₂₃ x₂₄ \n  x₃₁ x₃₂ x₃₃ x₃₄ \n"),
    (r"\underbrace{\begin{matrix} x_{11} & x_{12} & x_{13} & x_{14} \\ x_{21} & x_{22} & x_{23} & x_{24} \\ x_{31} & x_{32} & x_{33} & x_{34} \end{matrix}}_{btm}", "  x₁₁ x₁₂ x₁₃ x₁₄ \n  x₂₁ x₂₂ x₂₃ x₂₄ \n  x₃₁ x₃₂ x₃₃ x₃₄ \n ╰──────┬───────╯ \n       btm        \n"),
    (r"\overbrace{\begin{matrix} x_{11} & x_{12} & x_{13} \\ x_{21} & x_{22} & x_{23} \\ x_{31} & x_{32} & x_{33} \\ x_{41} & x_{42} & x_{43} \end{matrix}}^{top}", "     top      \n ╭────┴─────╮ \n  x₁₁ x₁₂ x₁₃ \n  x₂₁ x₂₂ x₂₃ \n  x₃₁ x₃₂ x₃₃ \n  x₄₁ x₄₂ x₄₃ \n"),
    (r"\underbrace{\begin{matrix} x_{11} & x_{12} & x_{13} \\ x_{21} & x_{22} & x_{23} \\ x_{31} & x_{32} & x_{33} \\ x_{41} & x_{42} & x_{43} \end{matrix}}_{btm}", "  x₁₁ x₁₂ x₁₃ \n  x₂₁ x₂₂ x₂₃ \n  x₃₁ x₃₂ x₃₃ \n  x₄₁ x₄₂ x₄₃ \n ╰────┬─────╯ \n     btm      \n"),
    (r"\overbrace{\begin{matrix} x_{11} & x_{12} & x_{13} & x_{14} & x_{15} \\ x_{21} & x_{22} & x_{23} & x_{24} & x_{25} \end{matrix}}^{top}", "         top          \n ╭────────┴─────────╮ \n  x₁₁ x₁₂ x₁₃ x₁₄ x₁₅ \n  x₂₁ x₂₂ x₂₃ x₂₄ x₂₅ \n"),
    (r"\underbrace{\begin{matrix} x_{11} & x_{12} & x_{13} & x_{14} & x_{15} \\ x_{21} & x_{22} & x_{23} & x_{24} & x_{25} \end{matrix}}_{btm}", "  x₁₁ x₁₂ x₁₃ x₁₄ x₁₅ \n  x₂₁ x₂₂ x₂₃ x₂₄ x₂₅ \n ╰────────┬─────────╯ \n         btm          \n"),
    (r"\overbrace{\begin{matrix} x_{11} & x_{12} & x_{13} & x_{14} & x_{15} & x_{16} \\ x_{21} & x_{22} & x_{23} & x_{24} & x_{25} & x_{26} \\ x_{31} & x_{32} & x_{33} & x_{34} & x_{35} & x_{36} \end{matrix}}^{top}", "           top            \n ╭──────────┴───────────╮ \n  x₁₁ x₁₂ x₁₃ x₁₄ x₁₅ x₁₆ \n  x₂₁ x₂₂ x₂₃ x₂₄ x₂₅ x₂₆ \n  x₃₁ x₃₂ x₃₃ x₃₄ x₃₅ x₃₆ \n"),
    (r"\underbrace{\begin{matrix} x_{11} & x_{12} & x_{13} & x_{14} & x_{15} & x_{16} \\ x_{21} & x_{22} & x_{23} & x_{24} & x_{25} & x_{26} \\ x_{31} & x_{32} & x_{33} & x_{34} & x_{35} & x_{36} \end{matrix}}_{btm}", "  x₁₁ x₁₂ x₁₃ x₁₄ x₁₅ x₁₆ \n  x₂₁ x₂₂ x₂₃ x₂₄ x₂₅ x₂₆ \n  x₃₁ x₃₂ x₃₃ x₃₄ x₃₅ x₃₆ \n ╰──────────┬───────────╯ \n           btm            \n"),
]

ALL_TESTS = CORE_TESTS + ALIGNMENT_TESTS + MATRIX_TESTS + OVERSET_TESTS + MATRIX_BRACE_TESTS
