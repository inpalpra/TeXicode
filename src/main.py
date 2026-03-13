# TeXicode, a cli script that renders TeX math into Unicode
# Author: Darcy Zhang
# Project url: https://github.com/dxddxx/TeXicode

import sys
import argparse
import re
from pipeline import render_tex


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


def process_markdown(content, debug, color, options):
    segments = parse_markdown(content)
    output = []
    indent_size = 0  # As per user preference
    
    for seg_type, seg_content in segments:
        if seg_type == 'text':
            output.append(seg_content)
        elif seg_type == 'math_inline':
            try:
                # context="raw" to get pure unicode art without markdown code blocks
                rendered = render_tex(seg_content, debug, color, "raw", options, raise_errors=True)
                output.append(rendered)
            except Exception:
                # Fallback to raw LaTeX
                output.append(f"${seg_content}$")
        elif seg_type == 'math_display':
            try:
                rendered = render_tex(seg_content, debug, color, "raw", options, raise_errors=True)
                indent = " " * indent_size
                indented_lines = [f"{indent}{line}" for line in rendered.splitlines()]
                output.append("\n" + "\n".join(indented_lines) + "\n")
            except Exception:
                # Fallback to raw LaTeX
                output.append(f"\n$$\n{seg_content}\n$$\n")
        elif seg_type in ('code_inline', 'code_fenced'):
            output.append(seg_content)
            
    print("".join(output))


def main():
    help_description = \
            "TeXicode - render TeX strings or process markdown math\
             (https://github.com/dxddxx/TeXicode)"

    input_parser = argparse.ArgumentParser(description=help_description)
    input_parser.add_argument('-d', '--debug',
                              action='store_true',
                              help='enable debug')
    input_parser.add_argument('-f', '--file',
                              help='input Markdown file')
    input_parser.add_argument('-c', '--color',
                              action='store_true',
                              help='enable color (black on white)')
    input_parser.add_argument('latex_string',
                              nargs='?',
                              help='raw TeX string (if not using -f)')
    input_parser.add_argument('-n', '--normal-font',
                              action='store_true',
                              help='use normal font instead of serif')
    args = input_parser.parse_args()
    debug = args.debug
    color = args.color
    file_path = args.file
    latex_string = args.latex_string

    options = {}
    options["fonts"] = "normal" if args.normal_font else "serif"

    if file_path:
        try:
            with open(file_path, "r") as f:
                content = f.read()
            process_markdown(content, debug, color, options)
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
            sys.exit(1)
    elif latex_string:
        try:
            # For direct CLI usage, we use "raw" context to show it in the terminal
            print(render_tex(latex_string, debug, color, "raw", options))
        except Exception as e:
            if debug:
                raise e
            print(f"Error: Rendering failed. Use --debug for details.")
            sys.exit(1)
    else:
        input_parser.print_help()


if __name__ == "__main__":
    main()
