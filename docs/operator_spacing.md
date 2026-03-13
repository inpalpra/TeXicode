# Operator Spacing Audit

| LaTeX String | Rendered Output | Rating | Justification |
|--------------|-----------------|--------|---------------|
| `\int_0^1 x\,dx = \frac{1}{2}` | <pre>⌠        1 
│₀¹𝑥 𝑑𝑥=╶─╴
⌡        2 </pre> | [ ] GOOD <br> [ ] BAD |  |
| `\sum_{i=0}^{n} x_i` | <pre> 𝑛   
┰─╴  
▐╸ 𝑥ᵢ
┸─╴  
𝑖=0  </pre> | [ ] GOOD <br> [ ] BAD |  |
| `\hat{x} + \bar{y} + \vec{z}` | <pre>𝑥̂+𝑦̄+𝑧⃗</pre> | [ ] GOOD <br> [x] BAD | Missing space after '+'; Missing space before '+' |
| `\alpha + \beta = \gamma` | <pre>α+β=γ</pre> | [ ] GOOD <br> [x] BAD | Missing space after '+'; Missing space after '='; Missing space before '+'; Missing space before '=' |
| `E = mc^2` | <pre>𝐸=𝑚𝑐²</pre> | [ ] GOOD <br> [x] BAD | Missing space after '='; Missing space before '=' |
| `\sqrt{\frac{a^2+b^2}{c^2}}` | <pre> ┌───────╴
 │ 𝑎²+𝑏²  
 │╶─────╴ 
╰┘  𝑐²    </pre> | [ ] GOOD <br> [ ] BAD |  |
| `\lim_{x \to \infty} f(x)` | <pre>lim𝑓(𝑥)
𝑥→∞    </pre> | [ ] GOOD <br> [ ] BAD |  |
| `\begin{align} a &= b + c \\ d &= e + f \end{align}` | <pre>𝑎=𝑏+𝑐
𝑑=𝑒+𝑓</pre> | [ ] GOOD <br> [ ] BAD |  |
| `\begin{aligned} a &= b + c \\ d &= e + f \end{aligned}` | <pre>𝑎 =𝑏+𝑐
𝑑 =𝑒+𝑓</pre> | [ ] GOOD <br> [ ] BAD |  |
| `\begin{cases} x & \text{if } x > 0 \\ -x & \text{otherwise} \end{cases}` | <pre>⎧ 𝑥  if 𝑥>0    
⎨              
⎩ -𝑥 otherwise 
               </pre> | [ ] GOOD <br> [ ] BAD |  |
| `\begin{cases} 1 & x > 0 \\ 0 & x = 0 \\ -1 & x < 0 \end{cases}` | <pre>⎧ 1  𝑥>0 
⎨ 0  𝑥=0 
⎩ -1 𝑥<0 
         </pre> | [ ] GOOD <br> [ ] BAD |  |
| `\begin{aligned} y &= \frac{a}{b} \\ z &= c + d \end{aligned}` | <pre>    𝑎 
𝑦 =╶─╴
    𝑏 
𝑧 =𝑐+𝑑</pre> | [ ] GOOD <br> [ ] BAD |  |
| `\begin{gather} a + b = c \\ x + y = z \end{gather}` | <pre>𝑎+𝑏=𝑐
𝑥+𝑦=𝑧</pre> | [ ] GOOD <br> [ ] BAD |  |
| `\begin{bmatrix} b_{d1} \\ b_{d2} \\ b_{c1} \\ b_{c2} \end{bmatrix} = \begin{bmatrix} S_{dd11} & S_{ddpq12} & S_{dc11} & S_{dc12} \\ S_{dd21}^{56} & S & S_{dc21} & S_{dc22} \\ S_{cd11} & S_{cd12} & S_{cc11} & S_{cc12} \\ S_{cd21} & S_{cd422} & S_{cc21} & S_{cc22} \end{bmatrix} \cdot \begin{bmatrix} a_{d1} \\ a_{c2} \\ a_{c1} \\ a_{c2} \end{bmatrix}` | <pre>⎡ 𝑏_𝑑1 ⎤ ⎡  𝑆_𝑑𝑑11  𝑆_𝑑𝑑𝑝𝑞12 𝑆_𝑑𝑐11 𝑆_𝑑𝑐12 ⎤ ⎡ 𝑎_𝑑1 ⎤
⎢ 𝑏_𝑑2 ⎥ ⎢ 𝑆_𝑑𝑑21⁵⁶    𝑆     𝑆_𝑑𝑐21 𝑆_𝑑𝑐22 ⎥ ⎢ 𝑎_𝑐2 ⎥
⎢ 𝑏_𝑐1 ⎥=⎢  𝑆_𝑐𝑑11   𝑆_𝑐𝑑12  𝑆_𝑐𝑐11 𝑆_𝑐𝑐12 ⎥⋅⎢ 𝑎_𝑐1 ⎥
⎣ 𝑏_𝑐2 ⎦ ⎣  𝑆_𝑐𝑑21  𝑆_𝑐𝑑422  𝑆_𝑐𝑐21 𝑆_𝑐𝑐22 ⎦ ⎣ 𝑎_𝑐2 ⎦</pre> | [ ] GOOD <br> [ ] BAD |  |
| `\begin{bmatrix} b_1 \\ b_2 \end{bmatrix} = \begin{bmatrix} S_{11} & S_{12} \\ S_{21} & S_{22} \end{bmatrix} \begin{bmatrix} a_1 \\ a_2 \end{bmatrix}` | <pre>⎡ 𝑏₁ ⎤ ⎡ 𝑆₁₁ 𝑆₁₂ ⎤⎡ 𝑎₁ ⎤
⎣ 𝑏₂ ⎦=⎣ 𝑆₂₁ 𝑆₂₂ ⎦⎣ 𝑎₂ ⎦</pre> | [ ] GOOD <br> [ ] BAD |  |
| `\begin{aligned} b_1 &= S_{11}a_1 + S_{12}a_2 \\ b_2 &= S_{21}a_1 + S_{22}a_2 \end{aligned}` | <pre>𝑏₁ =𝑆₁₁𝑎₁+𝑆₁₂𝑎₂
𝑏₂ =𝑆₂₁𝑎₁+𝑆₂₂𝑎₂</pre> | [ ] GOOD <br> [ ] BAD |  |
| `\begin{vmatrix} a & b \\ c & d \end{vmatrix}` | <pre>│ 𝑎 𝑏 │
│ 𝑐 𝑑 │</pre> | [ ] GOOD <br> [ ] BAD |  |
| `\overset{\text{def}}{=}` | <pre>def
 = </pre> | [ ] GOOD <br> [ ] BAD |  |
| `\underset{x \to 0}{\lim}` | <pre>lim
𝑥→0</pre> | [ ] GOOD <br> [ ] BAD |  |
| `\underbrace{a+b+c}_{3\text{ terms}}` | <pre> 𝑎+𝑏+𝑐 
 ╰─┬─╯ 
3 terms</pre> | [ ] GOOD <br> [ ] BAD |  |
| `\overbrace{x+y}^{2}` | <pre> 2 
╭┴╮
𝑥+𝑦</pre> | [ ] GOOD <br> [ ] BAD |  |
| `\boxed{a + b}` | <pre>┏━━━┓
┃𝑎+𝑏┃
┗━━━┛</pre> | [ ] GOOD <br> [ ] BAD |  |
| `\color{red}{x} + y` | <pre>𝑥+𝑦</pre> | [ ] GOOD <br> [x] BAD | Missing space after '+'; Missing space before '+' |
| `\frac{\cancel{(x-1)}(x+2)}{(x-3)\cancel{(x-1)}}` | <pre> (̶𝑥̶-̶1̶)̶(𝑥+2) 
╶──────────╴
 (𝑥-3)(̶𝑥̶-̶1̶)̶ </pre> | [ ] GOOD <br> [ ] BAD |  |
| `\tag{1} E = mc^2` | <pre>𝐸=𝑚𝑐²   (1)</pre> | [ ] GOOD <br> [x] BAD | Missing space after '='; Missing space before '=' |
| `\tag*{\dagger} a = b` | <pre>𝑎=𝑏   †</pre> | [ ] GOOD <br> [x] BAD | Missing space after '='; Missing space before '=' |
| `\tag{2.1} \int_0^1 x\,dx = \frac{1}{2}` | <pre>⌠        1       
│₀¹𝑥 𝑑𝑥=╶─╴   (2.1)
⌡        2       </pre> | [ ] GOOD <br> [ ] BAD |  |
| `\begin{align} a &= b \tag{1} \\ c &= d \end{align}` | <pre>𝑎=𝑏   (1)
𝑐=𝑑    </pre> | [ ] GOOD <br> [ ] BAD |  |
| `\tag{1} \tag{2} a = b` | <pre>𝑎=𝑏   (1) (2)</pre> | [ ] GOOD <br> [x] BAD | Missing space after '='; Missing space before '=' |
| `\forall x \exists y` | <pre>∀𝑥∃𝑦</pre> | [x] GOOD <br> [ ] BAD | Spacing appears adequate (or N/A) |
| `a \approx b \neq c` | <pre>𝑎≈𝑏≠𝑐</pre> | [ ] GOOD <br> [x] BAD | Missing space after '≈'; Missing space after '≠'; Missing space before '≈'; Missing space before '≠' |
| `x \leq y \geq z` | <pre>𝑥≤𝑦≥𝑧</pre> | [ ] GOOD <br> [x] BAD | Missing space after '≤'; Missing space after '≥'; Missing space before '≤'; Missing space before '≥' |
| `S \subset T \supset U` | <pre>𝑆⊂𝑇⊃𝑈</pre> | [ ] GOOD <br> [x] BAD | Missing space after '⊂'; Missing space after '⊃'; Missing space before '⊂'; Missing space before '⊃' |
| `A \subseteq B \supseteq C` | <pre>𝐴⊆𝐵⊇𝐶</pre> | [ ] GOOD <br> [x] BAD | Missing space after '⊆'; Missing space after '⊇'; Missing space before '⊆'; Missing space before '⊇' |
| `x \in X \notin Y` | <pre>𝑥∈𝑋∉𝑌</pre> | [ ] GOOD <br> [x] BAD | Missing space after '∈'; Missing space after '∉'; Missing space before '∈'; Missing space before '∉' |
| `\pm \mp \times \div \cdot` | <pre>±∓×÷⋅</pre> | [ ] GOOD <br> [x] BAD | Missing space after '±'; Missing space after '×'; Missing space after '÷'; Missing space after '∓'; Missing space before '×'; Missing space before '÷'; Missing space before '∓'; Missing space before '⋅' |
| `\nabla \partial \infty` | <pre>∇∂∞</pre> | [x] GOOD <br> [ ] BAD | Spacing appears adequate (or N/A) |
| `\ldots \cdots \vdots \ddots` | <pre>…⋯⋮⋱</pre> | [ ] GOOD <br> [x] BAD | Missing space after '…'; Missing space after '⋮'; Missing space after '⋯'; Missing space before '⋮'; Missing space before '⋯'; Missing space before '⋱' |
