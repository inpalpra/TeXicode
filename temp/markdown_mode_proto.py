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

def render_segments(segments):
    """
    Renders the segments into a final string.
    In the prototype, we just wrap math in markers to verify detection.
    """
    output = []
    for type, content in segments:
        if type == 'text':
            output.append(content)
        elif type == 'math_inline':
            output.append(f"[MATH_INLINE: {content}]")
        elif type == 'math_display':
            output.append(f"\n[MATH_DISPLAY_START]\n{content}\n[MATH_DISPLAY_END]\n")
        elif type == 'code_inline':
            output.append(content)
        elif type == 'code_fenced':
            output.append(content)
    return "".join(output)

if __name__ == "__main__":
    test_file = "tests/complex_markdown_test.md"
    if len(sys.argv) > 1:
        test_file = sys.argv[1]
        
    with open(test_file, "r") as f:
        content = f.read()
    
    print(f"Parsing {test_file}...")
    segments = parse_markdown(content)
    result = render_segments(segments)
    
    # Write to a temporary file for inspection
    with open("temp/proto_output.md", "w") as f:
        f.write(result)
    
    print("Parsing complete. Output written to temp/proto_output.md")
    # print(result)
