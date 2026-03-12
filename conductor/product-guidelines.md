# TeXicode Product Guidelines

## Prose Style
- **Technical & Concise:** Documentation and error messages should be technical yet easy to understand, focusing on utility.
- **Direct Tone:** Use a senior engineer's professional and direct tone.

## UX Principles
- **Speed-First:** The CLI and web interface must be optimized for fast rendering and minimal user input.
- **Consistency:** Ensure that the Unicode output remains consistent and legible across different terminal fonts and environments.
- **Clarity Over Aesthetics:** Prioritize readability of mathematical expressions (e.g., lengthened square root tails) over purely aesthetic choices.
- **Implicit Math Mode:** Users should be able to input raw TeX without mandatory delimiters (like `\( \)` or `$ $`) while still supporting them.

## Design Principles
- **Unicode Primitives:** Use box-drawing characters for lines and brackets to ensure wide compatibility and consistent spacing.
- **Mathematical Distinction:** Use Unicode italic glyphs to differentiate variables from functions, mimicking LaTeX's visual style.
- **Horizon Alignment:** Maintain a clear horizontal center line for complex, concatenated expressions to improve readability.
- **Connected Glyphs:** Symbols such as sums and square roots must use connecting Unicode characters to form a cohesive visual unit.

## Error Handling
- **Graceful Degradation:** Unsupported LaTeX commands should be rendered as a placeholder (e.g., `?`) rather than causing a system failure.
- **Informative Debugging:** Provide a `-d` debug flag to help users identify parsing or lexing issues.
