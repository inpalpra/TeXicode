import sys
import os

# Add src to path so we can import renderer/pipeline if needed later
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

def parse_markdown(text):
    """
    Identifies and protects math delimiters in markdown.
    Returns a list of segments: (type, content)
    where type is 'text', 'math_inline', 'math_display', 'code_inline', 'code_fenced'
    """
    segments = []
    i = 0
    n = len(text)
    
    current_text = ""
    
    def flush_text():
        nonlocal current_text
        if current_text:
            segments.append(('text', current_text))
            current_text = ""

    while i < n:
        # Fenced code block check (```)
        if text.startswith('```', i):
            flush_text()
            start = i
            i += 3
            # Find the closing fence
            end_fence = text.find('```', i)
            if end_fence != -1:
                segments.append(('code_fenced', text[start:end_fence+3]))
                i = end_fence + 3
            else:
                # Unclosed fence, treat as text
                current_text += text[start:i]
            continue
            
        # Inline code check (`)
        if text[i] == '`':
            flush_text()
            start = i
            i += 1
            # Find the closing backtick
            end_backtick = text.find('`', i)
            if end_backtick != -1:
                segments.append(('code_inline', text[start:end_backtick+1]))
                i = end_backtick + 1
            else:
                current_text += '`'
            continue
            
        # Escaped dollar (\$ )
        if text.startswith('\\$', i):
            current_text += '\\$'
            i += 2
            continue
            
        # Display math check ($$)
        if text.startswith('$$', i):
            flush_text()
            start = i
            i += 2
            # Find the closing $$
            end_math = text.find('$$', i)
            if end_math != -1:
                segments.append(('math_display', text[start+2:end_math]))
                i = end_math + 2
            else:
                # Unclosed $$, treat as text
                current_text += '$$'
            continue
            
        # Inline math check ($)
        if text[i] == '$':
            flush_text()
            start = i
            i += 1
            # Find the closing $
            # Must NOT be escaped \$
            end_math = -1
            curr = i
            while curr < n:
                if text[curr] == '$' and (curr == 0 or text[curr-1] != '\\'):
                    end_math = curr
                    break
                curr += 1
                
            if end_math != -1:
                segments.append(('math_inline', text[start+1:end_math]))
                i = end_math + 1
            else:
                current_text += '$'
            continue
            
        # Default: accumulate text
        current_text += text[i]
        i += 1
        
    flush_text()
    return segments

import pipeline

def render_segments_with_pipeline(segments, indent_size=4, color=True):
    """
    Renders the segments using the actual TeXicode pipeline.
    """
    output = []
    options = {"fonts": "serif"}
    for type, content in segments:
        if type == 'text':
            output.append(content)
        elif type == 'math_inline':
            # Inline math is rendered in-place
            try:
                # context="raw" to avoid backticks if it's a single line
                rendered = pipeline.render_tex(content, False, color, "raw", options)
                output.append(rendered)
            except Exception as e:
                # Fallback to raw
                print(f"DEBUG: Inline render failed for '{content}': {e}")
                output.append(f"${content}$")
        elif type == 'math_display':
            # Display math is a block
            try:
                rendered = pipeline.render_tex(content, False, color, "raw", options)
                # Indent each line
                indent = " " * indent_size
                indented_lines = [f"{indent}{line}" for line in rendered.splitlines()]
                output.append("\n" + "\n".join(indented_lines) + "\n")
            except Exception as e:
                # Fallback to raw
                print(f"DEBUG: Display render failed for '{content}': {e}")
                output.append(f"\n$$\n{content}\n$$\n")
        elif type == 'code_inline':
            output.append(content)
        elif type == 'code_fenced':
            output.append(content)
    return "".join(output)

if __name__ == "__main__":
    # Test text for stylistic options
    test_math = r"M = \begin{bmatrix} a & b \\ c & d \end{bmatrix}"
    segments = [('math_display', test_math)]
    
    print("\nStylistic Option 1: 2-space indent")
    print(render_segments_with_pipeline(segments, indent_size=2))
    
    print("\nStylistic Option 2: 4-space indent")
    print(render_segments_with_pipeline(segments, indent_size=4))
    
    print("\nStylistic Option 3: 8-space indent")
    print(render_segments_with_pipeline(segments, indent_size=8))
    
    # Test escaped dollars
    test_text = "The price is \\$10 and $x=5$ is math."
    print("Testing escaped dollars...")
    segments = parse_markdown(test_text)
    result = render_segments_with_pipeline(segments)
    print(f"Result: {result}")
    
    test_file = "tests/complex_markdown_test.md"
    if len(sys.argv) > 1:
        test_file = sys.argv[1]
        
    with open(test_file, "r") as f:
        content = f.read()
    
    print(f"Parsing {test_file}...")
    segments = parse_markdown(content)
    # Defaulting to 4-space indent for the full test
    result = render_segments_with_pipeline(segments, indent_size=4)
    
    # Write to a temporary file for inspection
    with open("temp/proto_output.md", "w") as f:
        f.write(result)
    
    print("Parsing complete. Output written to temp/proto_output.md")
