import renderer
import pipeline

MULTI_LINE_ENVS = {
    ('m','a','t','r','i','x'):          ('', ''),
    ('p','m','a','t','r','i','x'):      ('(', ')'),
    ('b','m','a','t','r','i','x'):      ('[', ']'),
    ('v','m','a','t','r','i','x'):      ('|', '|'),
    ('V','m','a','t','r','i','x'):      ('\u2016', '\u2016'),
    ('a','l','i','g','n','e','d'):      ('', ''),
    ('s','p','l','i','t'):              ('', ''),
    ('c','a','s','e','s'):              ('{', '.'),
    ('g','a','t','h','e','r'):          ('', ''),
    ('g','a','t','h','e','r','*'):      ('', ''),
    ('a','r','r','a','y'):              ('', ''),
}

old_render_begin = renderer.render_begin
def patched_render_begin(children: list):
    env_name = children[0][0]
    if env_name in ([['a', 'l', 'i', 'g', 'n']],
                    [['a', 'l', 'i', 'g', 'n', '*']]):
        return renderer.util_concat(children[1:], True, True)
    
    name_tuple = renderer._env_name_to_tuple(env_name)
    if name_tuple in MULTI_LINE_ENVS:
        if name_tuple == ('a','r','r','a','y'):
            return renderer.util_concat(children[2:], True, True)
        if name_tuple in [('g','a','t','h','e','r'), ('g','a','t','h','e','r','*')]:
            return renderer.util_concat(children[1:], True, False)
        return renderer.util_concat(children[1:], True, True)
    return renderer.render_concat_line_no_align_amp(children[1:])

renderer.render_begin = patched_render_begin

def get_delim(delim_char, height, horizon):
    if not delim_char or delim_char == '.':
        return ([[] for _ in range(height)], 0, []) # Fix: return empty list of correct height
    return renderer.util_delimiter(delim_char, height, horizon)

def patched_render_matrix(row_sketches, delim_left, delim_right, align_spec=None):
    all_cells = []
    row_heights = []
    for sketch, horizon, amps in row_sketches:
        cells = renderer._split_row_into_cells(sketch, amps)
        all_cells.append(cells)
        row_heights.append(len(sketch))

    num_cols = max(len(cells) for cells in all_cells) if all_cells else 0

    if not align_spec:
        align_spec = ['c'] * num_cols
    else:
        while len(align_spec) < num_cols:
            align_spec.append(align_spec[-1])

    col_widths = [0] * num_cols
    for cells in all_cells:
        for j, cell in enumerate(cells):
            w = len(cell[0]) if cell[0] else 0
            col_widths[j] = max(col_widths[j], w)

    grid = []
    for row_idx, cells in enumerate(all_cells):
        row_h = row_heights[row_idx]
        row_sketch = None
        for j in range(num_cols):
            cell = cells[j] if j < len(cells) else [[]]
            cell_w = len(cell[0]) if cell[0] else 0
            if not cell[0] and row_h > 1:
                cell = [[] for _ in range(row_h)]
            elif len(cell) < row_h:
                pad_top = (row_h - len(cell)) // 2
                pad_bot = row_h - len(cell) - pad_top
                cell = [[] for _ in range(pad_top)] + cell + [[] for _ in range(pad_bot)]

            target_w = col_widths[j]
            align = align_spec[j] if j < len(align_spec) else 'c'
            
            if align == 'l':
                left_pad = 0
                right_pad = target_w - cell_w
            elif align == 'r':
                left_pad = target_w - cell_w
                right_pad = 0
            else: # 'c'
                left_pad = (target_w - cell_w) // 2
                right_pad = target_w - cell_w - left_pad
                
            padded = []
            for r in cell:
                padded.append([renderer.arts.bg] * left_pad + r + [renderer.arts.bg] * right_pad)
                
            if row_sketch is None:
                row_sketch = padded
            else:
                for r in range(row_h):
                    row_sketch[r] = row_sketch[r] + [renderer.arts.bg] + padded[r]
        grid.extend(row_sketch)

    grid_height = len(grid)
    grid_horizon = grid_height // 2

    if grid_height == 2 and (delim_left in ['{', '}'] or delim_right in ['{', '}']):
        empty_row = [[renderer.arts.bg] * len(grid[0])] if grid[0] else [[]]
        grid = [grid[0]] + empty_row + [grid[1]]
        grid_height = 3
        grid_horizon = 1

    grid_tup = (grid, grid_horizon, [])
    if delim_left or delim_right:
        left_tup = get_delim(delim_left, grid_height, grid_horizon)
        right_tup = get_delim(delim_right, grid_height, grid_horizon)
        
        space_tup = ([[" "]], 0, [])
        elements = []
        if left_tup[0] != [[]]:
            elements.extend([left_tup, space_tup])
        elements.append(grid_tup)
        if right_tup[0] != [[]]:
            elements.extend([space_tup, right_tup])
            
        return renderer.util_concat(elements, False, False)

    return grid_tup

renderer.render_matrix = patched_render_matrix

def patched_render_opn_root(children_ids, nodes, canvas):
    matrix_bgin_ids = set()
    for cid in children_ids:
        cnode = nodes[cid]
        if cnode[0] == "cmd_bgin":
            env_sketch = canvas[cnode[2][0]]
            name_tuple = renderer._env_name_to_tuple(env_sketch[0])
            if name_tuple in MULTI_LINE_ENVS:
                matrix_bgin_ids.add(cid)

    if not matrix_bgin_ids:
        children = [canvas[cid] for cid in children_ids]
        return renderer.render_root(children)

    grouped = []
    i = 0
    while i < len(children_ids):
        cid = children_ids[i]
        if cid in matrix_bgin_ids:
            cnode = nodes[cid]
            env_name_node = canvas[cnode[2][0]]
            name_tuple = renderer._env_name_to_tuple(env_name_node[0])
            delim_l, delim_r = MULTI_LINE_ENVS[name_tuple]
            
            align_spec = None
            if name_tuple == ('a','r','r','a','y'):
                spec_sketch, _, _ = canvas[cnode[2][1]]
                align_spec = spec_sketch[0]
            elif name_tuple in [('a','l','i','g','n','e','d'), ('s','p','l','i','t')]:
                align_spec = ['r', 'l'] * 10
            elif name_tuple == ('c','a','s','e','s'):
                align_spec = ['l', 'l']
            elif name_tuple in [('g','a','t','h','e','r'), ('g','a','t','h','e','r','*')]:
                align_spec = ['c']

            matrix_rows = [canvas[cid]]
            j = i + 1
            while j < len(children_ids):
                next_cid = children_ids[j]
                if nodes[next_cid][0] == "cmd_lbrk":
                    matrix_rows.append(canvas[next_cid])
                    j += 1
                else:
                    break
            i = j
            assembled = patched_render_matrix(matrix_rows, delim_l, delim_r, align_spec)
            grouped.append(assembled)
        else:
            grouped.append(canvas[cid])
            i += 1

    remaining_has_lbrk = False
    i = 0
    while i < len(children_ids):
        cid = children_ids[i]
        if cid in matrix_bgin_ids:
            j = i + 1
            while j < len(children_ids):
                if nodes[children_ids[j]][0] == "cmd_lbrk":
                    j += 1
                else:
                    break
            i = j
        else:
            if nodes[cid][0] == "cmd_lbrk":
                remaining_has_lbrk = True
                break
            i += 1

    if remaining_has_lbrk or len(grouped) == 1:
        return renderer.render_root(grouped)
    else:
        return renderer.util_concat(grouped, False, False)

renderer._render_opn_root = patched_render_opn_root

if __name__ == "__main__":
    def print_demo(title, tex):
        print(f"=== {title} ===")
        print(f"[{tex}]")
        print("-" * 20)
        try:
            print(pipeline.render_tex(tex, False, False, "raw", {"fonts": "normal"}))
        except Exception as e:
            import traceback
            traceback.print_exc()
            print(f"ERROR: {e}")
        print("\n")

    print_demo("1. aligned", 
               r'\begin{aligned} a &= b + c \\ d &= e + f \end{aligned}')
    
    print_demo("2. cases", 
               r'\begin{cases} x & \text{if } x > 0 \\ -x & \text{otherwise} \end{cases}')
    
    print_demo("3. cases with three branches", 
               r'\begin{cases} 1 & x > 0 \\ 0 & x = 0 \\ -1 & x < 0 \end{cases}')
    
    print_demo("4. aligned with fractions", 
               r'\begin{aligned} y &= \frac{a}{b} \\ z &= c + d \end{aligned}')

    print_demo("5. gather", 
               r'\begin{gather} a + b = c \\ x + y = z \end{gather}')
    
    print_demo("6. array", 
               r'\begin{array}{lcr} 1 & X & a \\ z & Y & bcd \end{array}')
