import sys
import os

# Add src to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import pipeline

def print_rows(rows):
    for row in rows:
        print(row)

def prototype_tag(eq_tex, tag_text, is_starred=False, padding=3):
    print(f"\n--- Prototype: {eq_tex} with tag '{tag_text}' (starred={is_starred}, padding={padding}) ---")
    
    # Use simple joining for visual demo
    eq_rows = pipeline.render_tex_rows(eq_tex, False)
    # Clean up empty lines from pipeline output for demo purposes
    eq_rows = [r for r in eq_rows if r.strip()]
    
    tag_content_rows = pipeline.render_tex_rows(tag_text, False)
    tag_content_rows = [r for r in tag_content_rows if r.strip()]
    
    tag_baseline_idx = len(tag_content_rows) // 2
    
    if not is_starred:
        tag_rows = []
        for i in range(len(tag_content_rows)):
            prefix = "(" if i == tag_baseline_idx else " "
            suffix = ")" if i == tag_baseline_idx else " "
            tag_rows.append(prefix + tag_content_rows[i] + suffix)
    else:
        tag_rows = tag_content_rows
        
    eq_baseline_idx = len(eq_rows) // 2
    
    above = max(eq_baseline_idx, tag_baseline_idx)
    below = max(len(eq_rows) - eq_baseline_idx - 1, len(tag_rows) - tag_baseline_idx - 1)
    
    total_rows = above + 1 + below
    
    final_rows = []
    for i in range(total_rows):
        eq_row_idx = i - (above - eq_baseline_idx)
        if 0 <= eq_row_idx < len(eq_rows):
            line = eq_rows[eq_row_idx]
        else:
            line = " " * len(eq_rows[0]) if eq_rows else ""
            
        line += " " * padding
        
        tag_row_idx = i - (above - tag_baseline_idx)
        if 0 <= tag_row_idx < len(tag_rows):
            line += tag_rows[tag_row_idx]
            
        final_rows.append(line)
        
    print_rows(final_rows)

if __name__ == "__main__":
    print("================ VISUAL OPTIONS FOR EQUATION TAGS ================")
    
    # Option 1: Standard 3-space padding
    prototype_tag(r"E = mc^2", "1", padding=3)
    
    # Option 2: Compact 1-space padding
    prototype_tag(r"E = mc^2", "1", padding=1)
    
    # Option 3: Starred tag (no parens)
    prototype_tag(r"a = b", r"\dagger", is_starred=True, padding=3)
    
    # Option 4: Complex equation baseline alignment
    prototype_tag(r"\int_0^1 x\,dx = \frac{1}{2}", "2.1", padding=3)
    
    # Option 5: Multi-tag concatenation
    print("\n--- Prototype: Multi-Tag Concatenation (\tag{1} \tag{2}) ---")
    eq = "a = b"
    tags = ["(1)", "(2)"]
    combined_tag = " ".join(tags)
    print(f"{eq}   {combined_tag}")
