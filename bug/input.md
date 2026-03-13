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
To calculate the inverse, we use $A^{-1}$, but you must not confuse it with the code snippet `let det = $A;`. The trace is defined as 

$$\text{tr}(A) = \sum_{i} A_{ii}$$