# Complex Markdown Mode Tests

## Scenario 1: Complex Multiline Matrix with Overset and Underset
Here is a complex state transition matrix:

$$
M = \begin{bmatrix}
  \overset{\alpha}{a} & b \\
  c & \underset{\beta}{d}
\end{bmatrix}
$$

The transition is complete.

## Scenario 2: Inline Math Interspersed with Inline Code Fences
To calculate the inverse, we use $A^{-1}$, but you must not confuse it with the code snippet `let det = $A;`. The trace is defined as $$\text{tr}(A) = \sum_{i} A_{ii}$$

## Scenario 3: Math Code Block Protection (Multiline Fences)
The following LaTeX code generates our target equation:

```latex
\begin{align}
  \hat{H} \Psi &= E \Psi \\
  \Psi(x, t) &= \sum_{n} c_n \phi_n(x) e^{-i E_n t / \hbar}
\end{align}
```

But when rendered outside the block:
$$ \hat{H} \Psi = E \Psi $$

## Scenario 4: Alignment Environments Inside Markdown Display Math
The system of equations is given by:

$$
\begin{align}
  2x + 3y &= 5 \tag{1} \\
  4x - y &= 11 \tag{2}
\end{align}
$$

We can solve this using substitution.

## Scenario 5: Nested Matrices with Complex Symbols (Fractions + Overset)
Consider the block matrix transformation:

$$
T = \begin{pmatrix}
  \frac{\overset{\rightarrow}{v}}{c} & 0 \\
  0 & I_3
\end{pmatrix}
$$

Where $I_3$ is the identity matrix.

## Scenario 6: Complex Multiline Matrix with Overset and Underset
Here is a complex state transition matrix:

$$
M = \begin{bmatrix}
  \overset{\alpha}{a} & b \\
  c & \underset{\beta}{d}
\end{bmatrix}
$$

The transition is complete.

## Scenario 7: Inline Math Interspersed with Inline Code Fences
To calculate the inverse, we use $A^{-1}$, but you must not confuse it with the code snippet `let det = $A;`. The trace is defined as $\text{tr}(A) = \sum_{i} A_{ii}$.

## Scenario 8: Math Code Block Protection (Multiline Fences)
The following LaTeX code generates our target equation:

```latex
\begin{align}
  \hat{H} \Psi &= E \Psi \\
  \Psi(x, t) &= \sum_{n} c_n \phi_n(x) e^{-i E_n t / \hbar}
\end{align}
```

But when rendered outside the block:
$$ \hat{H} \Psi = E \Psi $$

## Scenario 9: Alignment Environments Inside Markdown Display Math
The system of equations is given by:

$$
\begin{align}
  2x + 3y &= 5 \tag{1} \\
  4x - y &= 11 \tag{2}
\end{align}
$$

We can solve this using substitution.

## Scenario 10: Nested Matrices with Complex Symbols (Fractions + Overset)
Consider the block matrix transformation:

$$
T = \begin{pmatrix}
  \frac{\overset{\rightarrow}{v}}{c} & 0 \\
  0 & I_3
\end{pmatrix}
$$

Where $I_3$ is the identity matrix.

## Scenario 11: Colored Math with Inline Code
The equation $\color{red}{E = mc^2}$ is famous, but don't confuse it with the code snippet `let energy = $E;`.

## Sceraio 12: Colored Math in Matrix

$$
\begin{bmatrix}
  \color{blue}{a} & \color{green}{b} \\
  \color{red}{c} & \color{yellow}{d}
\end{bmatrix}
$$

## Scenario 13: Use three dots in a big matrix

$$
\begin{bmatrix}
  a & b & \cdots & c \\
  d & e & \cdots & f \\
  \vdots & \vdots & \ddots & \vdots \\
  g & h & \cdots & i
\end{bmatrix}
$$

# Sample Text from Paper

Q: show me some matrix equations for s-parameters
A:

Based on the provided documents, here are several matrix equations for S-parameters:

**1. General Two-Port Network Equations**
The relationship between incident waves ($a$) and reflected/transmitted waves ($b$) for a two-port network is defined by:
$$
\begin{aligned}
b_1 &= S_{11}a_1 + S_{12}a_2 \\
b_2 &= S_{21}a_1 + S_{22}a_2
\end{aligned}
$$
This can be written in matrix form as:
$$
\begin{bmatrix} b_1 \\ b_2 \end{bmatrix} = \begin{bmatrix} S_{11} & S_{12} \\ S_{21} & S_{22} \end{bmatrix} \begin{bmatrix} a_1 \\ a_2 \end{bmatrix}
$$
[@TechnologiesEmbedding]

**2. General n-Port Network Equation**
For an $n$-port network, the relationship is expressed as:
$$
\mathbf{b}_n = [S] \mathbf{a}_n
$$
Where $\mathbf{b}_n$ is the column vector of reflected waves and $[S]$ is the scattering matrix.
[@TechnologiesEmbedding]

**3. Mixed-Mode S-Parameters (4-Port Network)**
To fully describe a 4-port network, the mixed-mode S-parameters are arranged in matrix form:
$$
\begin{bmatrix} b_{d1} \\ b_{d2} \\ b_{c1} \\ b_{c2} \end{bmatrix} = \begin{bmatrix} S_{dd11} & S_{dd12} & S_{dc11} & S_{dc12} \\ S_{dd21} & S_{dd22} & S_{dc21} & S_{dc22} \\ S_{cd11} & S_{cd12} & S_{cc11} & S_{cc12} \\ S_{cd21} & S_{cd422} & S_{cc21} & S_{cc22} \end{bmatrix} \cdot \begin{bmatrix} a_{d1} \\ a_{c2} \\ a_{c1} \\ a_{c2} \end{bmatrix}
$$
[@Dunsmore2020Handbook]

**4. Impedance Transformation Matrix Equation**
To transform S-parameters from one reference impedance to another, the following matrix transformation is used:
$$
[S'] = [X]^{-1}([S] - [\Gamma])([I] - [\Gamma][S])^{-1}[X] \tag{2.17}
$$
[@Dunsmore2020Handbook]

**5. Two-Port Bilinear Matrix Equation (Calibration)**
For the 12-term calibration method, the measured S-parameters formulation results in a bilinear matrix equation. Expanding this for the two-port case yields 4 linear equations involving measured S-parameters, actual S-parameters, and error terms.
[unknown source]