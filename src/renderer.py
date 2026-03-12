import node_data
import arts
import symbols_art

CONFIG_SCRIPT_ORDER = "sub_sup"

MATRIX_ENVS = {
    ('m','a','t','r','i','x'):          ('', ''),
    ('p','m','a','t','r','i','x'):      ('(', ')'),
    ('b','m','a','t','r','i','x'):      ('[', ']'),
    ('v','m','a','t','r','i','x'):      ('|', '|'),
    ('V','m','a','t','r','i','x'):      ('\u2016', '\u2016'),
}

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


def util_revert_font(char: str) -> str:
    # if char.isascii():
    if ord(char) < 128:
        return char
    for alphabet in arts.alphabets.values():
        if char not in alphabet:
            continue
        for alpha_id in range(26*2):
            if alphabet[alpha_id] == char:
                return arts.alphabets["normal"][alpha_id]
    return char


def util_font(font_val: str, children: list) -> tuple:
    sketch, horizon, _ = children[0]
    new_sketch = []
    for row in sketch:
        new_row = []
        for char in row:
            char = util_revert_font(char)
            if char not in arts.alphabets["normal"]:
                new_row.append(char)
                continue
            if 'A' <= char <= 'Z':
                alpha_id = ord(char) - ord('A')
            elif 'a' <= char <= 'z':
                alpha_id = ord(char) - ord('a') + 26
            new_row.append(arts.font[font_val][alpha_id])
        new_sketch.append(new_row)
    return new_sketch, horizon, []


def util_unshrink(small_char: str) -> str:
    """No change to logic"""
    for char, scripts in arts.unicode_scripts.items():
        if small_char in scripts:
            return char
    return small_char


def util_concat(children: list, concat_line: bool, align_amp: bool) -> tuple:
    if not children:
        return [[]], 0, []

    concated_sketch = []
    maxh_sky = 0
    maxh_ocn = 0
    contain_amp = False
    concated_amps = []

    for sketch, horizon, amps in children:
        if amps:
            contain_amp = True
            continue
        h_sky = horizon
        h_ocn = len(sketch) - h_sky - 1
        maxh_sky = max(maxh_sky, h_sky)
        maxh_ocn = max(maxh_ocn, h_ocn)

    concated_horizon = maxh_sky
    for _ in range(maxh_sky + 1 + maxh_ocn):
        concated_sketch.append([])

    for sketch, horizon, amps in children:
        if amps:
            # concated_horizon = len(concated_sketch[0])
            concated_amps.append(len(concated_sketch[0]))
            continue

        h_sky = horizon
        h_ocn = len(sketch) - h_sky - 1
        top_pad_len = maxh_sky - h_sky
        btm_pad_len = maxh_ocn - h_ocn

        top_pad = [[arts.bg] * len(sketch[0]) for _ in range(top_pad_len)]
        btm_pad = [[arts.bg] * len(sketch[0]) for _ in range(btm_pad_len)]

        sketch = top_pad + sketch + btm_pad
        for i in range(len(concated_sketch)):
            concated_sketch[i].extend(sketch[i])

    if concat_line and not contain_amp:
        pass # concated_horizon = len(concated_sketch[0])

    return concated_sketch, concated_horizon, concated_amps


def util_vert_pile(top, ctr, ctr_horizon, btm, align) -> tuple:
    piled_sketch = []
    piled_horizon = len(top) + ctr_horizon

    if top == [[]]:
        piled_horizon -= 1
    if ctr == [[]]:
        piled_horizon -= 1

    if piled_horizon < 0:
        piled_horizon = 0

    max_len = max(len(top[0]), len(ctr[0]), len(btm[0]))

    for sketch in (top, ctr, btm):
        if sketch == [[]]:
            continue

        sketch_len = len(sketch[0])
        left_pad_len = 0
        right_pad_len = 0

        if align == "left":
            right_pad_len = max_len - sketch_len
        elif align == "right":
            left_pad_len = max_len - sketch_len
        elif align == "center":
            left_pad_len = (max_len - sketch_len) // 2
            right_pad_len = max_len - sketch_len - left_pad_len

        left_pad = [arts.bg] * left_pad_len
        right_pad = [arts.bg] * right_pad_len

        for row in sketch:
            piled_sketch.append(left_pad + row + right_pad)

    if piled_sketch == []:
        piled_sketch = [[]]

    return piled_sketch, piled_horizon, []


def util_script(children: list, script_type_id: int) -> tuple:
    sketch, horizon, _ = children[0]
    shrunk = util_shrink(sketch, script_type_id, False, False)
    if shrunk != []:
        return shrunk, 0, []

    # If it can't be shrunk properly into its script type, we prepend ^ or _,
    # and use the normal sized characters! Avoid the smart_shrink fallback 
    # to superscripts since we are already prepending `_`.
    prefix = '^' if script_type_id == 0 else '_'
    new_sketch = []
    for i, row in enumerate(sketch):
        if i == horizon:
            new_sketch.append([prefix] + row)
        else:
            new_sketch.append([arts.bg] + row)

    return new_sketch, horizon, []


def util_shrink(sketch: list, script_type_id: int,
                smart: bool, switch: bool) -> list:
    invert_script_type_id = 1 - script_type_id
    if len(sketch) != 1:
        return []

    art = arts.unicode_scripts
    shrunk_row = []

    for char in sketch[0]:
        char = util_revert_font(char)
        unshrunk_char = util_unshrink(char)

        if unshrunk_char not in art.keys():
            return []

        if art[unshrunk_char][script_type_id] == char:
            return []

        if art[unshrunk_char][invert_script_type_id] == char:
            if smart:
                shrunk_row.append(char)
                continue
            if switch:
                shrunk_row.append(art[unshrunk_char][script_type_id])
                continue
            return []

        shrunk_char = art[unshrunk_char][script_type_id]
        if shrunk_char != " " or char == " ":
            shrunk_row.append(shrunk_char)
            continue

        return []

    return [shrunk_row]


def util_get_pile_center(base_height, base_horizon) -> tuple:
    if base_height == 2:
        if base_horizon == 0:
            return [[]], 0, []
        if base_horizon == 1:
            return [[]], 1, []

    if base_height == 1:
        return [[]], 0, []

    pile_center_sketch = []
    for _ in range(base_height - 2):
        pile_center_sketch.append([arts.bg])

    pile_center_horizon = base_horizon - 1
    return pile_center_sketch, pile_center_horizon, []


def util_delimiter(delim_type, height: int, horizon: int) -> tuple:
    if delim_type == ".":
        return [[]], 0, []

    art_col = arts.delimiter["sgl"].find(delim_type[0])
    if art_col == []:
        raise ValueError(f"Invalid delimiter type {delim_type}")

    delim_art = dict()
    for pos in arts.delimiter:
        art = arts.delimiter[pos]
        delim_art[pos] = art[art_col]

    if height == 1:
        return [delim_type], 0, []

    if height == 2 and delim_type in ["{", "}"]:
        height = 3
        if horizon == 0:
            horizon = 1

    center = horizon
    if center == 0:
        center = 1
    if center == height - 1:
        center = height - 2

    sketch = []
    for _ in range(height):
        sketch.append([delim_art["fil"]])

    sketch[center] = [delim_art["ctr"]]
    sketch[0] = [delim_art["top"]]
    sketch[-1] = [delim_art["btm"]]

    return sketch, horizon, []


def util_add_ampersand_padding(children: list) -> tuple:
    max_amp = 0
    for sketch, horizon, amps in children:
        if amps:
            max_amp = max(max_amp, amps[0])

    padded_children = []
    for sketch, horizon, amps in children:
        new_amps = amps
        if not amps:
            new_amps.append(-1)
        pad_len = max_amp - new_amps[0]
        padding = [arts.bg] * pad_len

        padded_sketch = []
        for row in sketch:
            padded_sketch.append(padding + row)
        padded_children.append((padded_sketch, horizon, amps))

    return padded_children


def util_vert_concat(children: list, sep: list, align: str) -> tuple:
    if children[0][2] != -1:
        children = util_add_ampersand_padding(children)

    sketch = children.pop(0)[0]
    horizon = 0

    for child in children:
        top = sketch
        btm = child[0]
        sketch, horizon, _ = util_vert_pile(top, sep, 0, btm, align)

    return sketch, horizon, []

# Rendering Functions


def render_font(token: str, children: list) -> tuple:
    return util_font(token[1], children)


def render_text_info(token: tuple, children: list) -> tuple:
    return [[token[1]]], 0, []


def render_text(token: str, children: list) -> tuple:
    return util_font(token[1], children)


def render_leaf(token: tuple, children: list) -> tuple:
    token_type = token[0]
    token_val = token[1]
    sketch = [[token_val]]
    horizon = 0
    amps = []

    if token_type == "numb":
        return sketch, horizon, amps

    elif token_type == "symb":
        if token_val == "&":
            amps.append(0)
        # if token_val in arts.simple_symbols:
        #     sketch = [[token_val]]
        elif token_val in arts.special_symbols.keys():
            sketch = arts.special_symbols[token_val]
        return sketch, horizon, amps

    elif token_type == "alph":
        return util_font("mathnormal", [(sketch, 0, [])])

    elif token_type == "cmnd":
        if token_val in arts.multi_line_leaf_commands.keys():
            sketch, horizon, amps = arts.multi_line_leaf_commands[token_val]
        elif token_val in symbols_art.symbols.keys():
            sketch = [symbols_art.symbols[token_val]]
        else:
            sketch = [["?"]]
        return sketch, horizon, amps


def render_concat(children: list) -> tuple:
    return util_concat(children, False, False)


def render_sup_script(children: list) -> tuple:
    return util_script(children, 0)


def render_sub_script(children: list) -> tuple:
    return util_script(children, 1)


def render_top_script(children: list) -> tuple:
    # Centered scripts (like overbrace labels) should NOT be shrunk by default
    # unless we explicitly want small font. For now, keep them full sized.
    return children[0]


def render_bottom_script(children: list) -> tuple:
    return children[0]


def render_apply_scripts(base: list, scripts: list) -> tuple:
    base_sketch, base_horizon, _ = base
    sorted_scripts = {0: None, 1: None}
    base_position = "left"

    for script_type, script_canvas in scripts:
        if script_type in {"top_scrpt", "btm_scrpt"}:
            base_position = "center"
        script_position = 0
        if script_type in {"sub_scrpt", "btm_scrpt"}:
            script_position = 1
        if sorted_scripts[script_position] is not None:
            script_type_name = ["super", "sub"][script_position]
            raise ValueError(f"Double {script_type_name}scripts")
        sorted_scripts[script_position] = script_canvas

    top_tup = sorted_scripts[0]
    btm_tup = sorted_scripts[1]

    if base_position == "center":
        top = top_tup[0] if top_tup else [[]]
        btm = btm_tup[0] if btm_tup else [[]]
        return util_vert_pile(top, base_sketch, base_horizon, btm, "center")

    elements = [base]
    if CONFIG_SCRIPT_ORDER == "sub_sup":
        if btm_tup: elements.append(btm_tup)
        if top_tup: elements.append(top_tup)
    else:
        if top_tup: elements.append(top_tup)
        if btm_tup: elements.append(btm_tup)

    return util_concat(elements, False, False)


def render_big_delimiter(token: tuple, children: list) -> tuple:
    size = token[1]
    delim_type = children[0][0][0]
    height_dict = {"big": 1, "bigl": 1, "bigr": 1,
                   "Big": 3, "Bigl": 3, "Bigr": 3,
                   "bigg": 5, "biggl": 5, "biggr": 5,
                   "Bigg": 7, "Biggl": 7, "Biggr": 7}
    height = height_dict[size]
    return util_delimiter(delim_type, height, height // 2)


def render_open_delimiter(children: list) -> tuple:
    inside = util_concat(children[1:-1], False, False)
    left_delim_type = children[0][0][0][0]
    right_delim_type = children[-1][0][0][0]
    height = len(inside[0])
    horizon = inside[1]
    left = util_delimiter(left_delim_type, height, horizon)
    right = util_delimiter(right_delim_type, height, horizon)
    return util_concat([left, inside, right], False, False)


def render_close_delimiter(children: list) -> tuple:
    return children[0]


def render_binomial(children: list) -> tuple:
    n, r = children[0][0], children[1][0]
    sep_space = [arts.bg] * max(len(n[0]), len(r[0]))
    piled = util_vert_pile(n, [sep_space], 0, r, "center")
    return render_open_delimiter([([["("]], 0, []), piled, ([[")"]], 0, [])])


def render_fraction(children: list) -> tuple:
    numer, denom = children[0][0], children[1][0]
    art = arts.fraction
    fraction_line = [art[1]] * max(len(numer[0]), len(denom[0]))
    fraction_line = [art[0]] + fraction_line + [art[2]]
    return util_vert_pile(numer, [fraction_line], 0, denom, "center")


def render_overset(children: list) -> tuple:
    top_sketch, top_horizon, _ = children[0]
    base_sketch, base_horizon, _ = children[1]
    res_sketch, _, _ = util_vert_pile(top_sketch, [[]], 0, base_sketch, "center")
    top_height = 0 if top_sketch == [[]] else len(top_sketch)
    new_horizon = top_height + base_horizon
    return res_sketch, new_horizon, []


def render_underset(children: list) -> tuple:
    btm_sketch, btm_horizon, _ = children[0]
    base_sketch, base_horizon, _ = children[1]
    res_sketch, _, _ = util_vert_pile(base_sketch, [[]], 0, btm_sketch, "center")
    return res_sketch, base_horizon, []


def util_build_brace(width, is_over):
    if width <= 0:
        return [[]]
    if width == 1:
        return [["⏞"]] if is_over else [["⏟"]]
    if width == 2:
        return [["╭", "╮"]] if is_over else [["╰", "╯"]]
    
    row = ["─"] * width
    middle = (width - 1) // 2
    if is_over:
        row[0], row[-1], row[middle] = "╭", "╮", "┴"
    else:
        row[0], row[-1], row[middle] = "╰", "╯", "┬"
    return [row]


def render_overbrace(children: list) -> tuple:
    content_sketch, content_horizon, _ = children[0]
    content_w = len(content_sketch[0]) if content_sketch != [[]] else 0
    brace_row = util_build_brace(content_w, True)
    brace_w = len(brace_row[0]) if brace_row != [[]] else 0
    
    # Target width is the max of content and brace
    target_w = max(content_w, brace_w)
    
    def pad_row(row, target):
        diff = target - len(row)
        left = diff // 2
        right = diff - left
        return [arts.bg] * left + row + [arts.bg] * right

    # Assemble: content_sketch might be empty if 0
    final_sketch = []
    # Brace row
    final_sketch.append(pad_row(brace_row[0], target_w))
    # Content rows
    for row in content_sketch:
        final_sketch.append(pad_row(row, target_w))
        
    return final_sketch, 1 + content_horizon, []


def render_underbrace(children: list) -> tuple:
    content_sketch, content_horizon, _ = children[0]
    content_w = len(content_sketch[0]) if content_sketch != [[]] else 0
    brace_row = util_build_brace(content_w, False)
    brace_w = len(brace_row[0]) if brace_row != [[]] else 0
    
    target_w = max(content_w, brace_w)
    
    def pad_row(row, target):
        diff = target - len(row)
        left = diff // 2
        right = diff - left
        return [arts.bg] * left + row + [arts.bg] * right

    final_sketch = []
    # Content rows
    for row in content_sketch:
        final_sketch.append(pad_row(row, target_w))
    # Brace row
    final_sketch.append(pad_row(brace_row[0], target_w))
        
    return final_sketch, content_horizon, []


def render_xarrow(token: tuple, children: list) -> tuple:
    if len(children) == 2:
        below_sketch, _, _ = children[0]
        above_sketch, _, _ = children[1]
    else:
        below_sketch = [[]]
        above_sketch, _, _ = children[0]
    above_width = len(above_sketch[0]) if above_sketch != [[]] else 0
    below_width = len(below_sketch[0]) if below_sketch != [[]] else 0
    text_width = max(above_width, below_width)
    arrow_width = text_width + 2
    if token[1] == "xrightarrow":
        arrow_row = ["─"] * (arrow_width - 1) + [">"]
    else:
        arrow_row = ["<"] + ["─"] * (arrow_width - 1)
    res_sketch, _, _ = util_vert_pile(above_sketch, [arrow_row], 0, below_sketch, "center")
    new_horizon = len(above_sketch) if above_sketch != [[]] else 0
    return res_sketch, new_horizon, []


def render_tag(token: tuple, children: list) -> tuple:
    sketch, horizon, amps = children[0]
    is_starred = token[1].endswith("*")

    if not is_starred:
        new_sketch = []
        for i in range(len(sketch)):
            prefix = "(" if i == horizon else " "
            suffix = ")" if i == horizon else " "
            new_sketch.append([prefix] + sketch[i] + [suffix])
        sketch = new_sketch

    return sketch, horizon, amps


def render_accents(token: tuple, children: list) -> tuple:
    accent_val = token[1]
    u_hex = {"acute": "\u0302", "bar": "\u0304", "breve": "\u0306",
             "check": "\u030C", "ddot": "\u0308", "dot": "\u0307",
             "grave": "\u0300", "hat": "\u0302", "mathring": "\u030A",
             "tilde": "\u0303", "vec": "\u20D7", "widehat": "\u0302",
             "widetilde": "\u0360"}[accent_val]
    sketch = children[0][0]
    first_char = sketch[0][0] + u_hex
    # finally fixed ugly ass combining char lets goooo
    first_row = [first_char] + sketch[0][1:]
    sketch = [first_row] + sketch[1:]
    return sketch, children[0][1], children[0][2]


def util_onechar_square_root(children: list) -> tuple:
    # thanks to u/Iron_Pencil for the idea
    radicand_sketch, radicand_horizon, _ = children[-1]
    surd_art = symbols_art.symbols["surd"]

    if len(radicand_sketch[0]) == 1:
        new_radi_row = surd_art + [radicand_sketch[0][0] + "\u0305"]
    if len(radicand_sketch[0]) == 0:
        new_radi_row = surd_art
    new_radi = ([new_radi_row], radicand_horizon, [])

    if len(children) <= 1:
        return new_radi

    degree = util_script(children, 0)
    return util_concat([degree, new_radi], False, False)


def util_multichar_square_root(children: list) -> tuple:
    degree_sketch, _, _ = children[0]
    radicand_sketch, radicand_horizon, _ = children[-1]

    art = arts.square_root

    top_bar = art["top_bar"] * len(radicand_sketch[0])
    sqrt_sketch = [top_bar] + radicand_sketch

    for i in range(len(sqrt_sketch)):
        sqrt_sketch[i] = art["left_bar"] + sqrt_sketch[i] + [arts.bg]

    sqrt_sketch[0] = art["top_angle"] + sqrt_sketch[0][2:-1] + art["top_tail"]
    sqrt_sketch[-1] = art["btm_angle"] + sqrt_sketch[-1][2:]

    if len(children) == 1 or len(degree_sketch) > 1:
        return sqrt_sketch, radicand_horizon + 1, []

    shrinked_degree = util_shrink(degree_sketch, 1, False, False)
    if shrinked_degree == []:
        shrinked_degree = degree_sketch

    if sqrt_sketch[-2][0] == " ":
        sqrt_sketch[-2] = [shrinked_degree[0][-1]] + sqrt_sketch[-2][1:]
        shrinked_degree[0] = shrinked_degree[0][:-1]

    left_pad = [arts.bg] * len(shrinked_degree[0])

    for i in range(len(sqrt_sketch)):
        if i == len(sqrt_sketch) - 2:
            sqrt_sketch[i] = shrinked_degree[0] + sqrt_sketch[i]
            continue
        sqrt_sketch[i] = left_pad + sqrt_sketch[i]

    return sqrt_sketch, radicand_horizon + 1, []


def render_square_root(children: list) -> tuple:
    radicand_sketch, _, _ = children[-1]

    # if len(radicand_sketch) == 1:
    # someone said parenthesis is uncleaer, agreed.
    if len(radicand_sketch[0]) <= 1 and len(radicand_sketch) == 1:
        return util_onechar_square_root(children)
    else:
        return util_multichar_square_root(children)


def render_concat_line_align_amp(children: list) -> tuple:
    return util_concat(children, True, True)


def render_concat_line_no_align_amp(children: list) -> tuple:
    # line_sketch, line_horizon, _ = util_concat(children, True, False)[0]
    line_sketch, line_horizon, _ = util_concat(children, True, False)
    return line_sketch, line_horizon, []


def render_begin(children: list):
    env_name = children[0][0]
    if env_name in ([['a', 'l', 'i', 'g', 'n']],
                    [['a', 'l', 'i', 'g', 'n', '*']]):
        return util_concat(children[1:], True, True)

    name_tuple = _env_name_to_tuple(env_name)
    if name_tuple in MULTI_LINE_ENVS:
        if name_tuple == ('a','r','r','a','y'):
            return util_concat(children[2:], True, True)
        if name_tuple in [('g','a','t','h','e','r'), ('g','a','t','h','e','r','*')]:
            return util_concat(children[1:], True, False)
        return util_concat(children[1:], True, True)

    return render_concat_line_no_align_amp(children[1:])


def _env_name_to_tuple(sketch):
    """Convert env name sketch like [['b','m','a','t','r','i','x']] to tuple."""
    if len(sketch) == 1:
        return tuple(sketch[0])
    return ()


def _split_row_into_cells(sketch, amps):
    """Split a row sketch into cells using amp column positions."""
    if not amps:
        return [sketch]
    boundaries = [0] + amps + [len(sketch[0])]
    cells = []
    for i in range(len(boundaries) - 1):
        start = boundaries[i]
        end = boundaries[i + 1]
        cell = [row[start:end] for row in sketch]
        cells.append(cell)
    return cells


def get_delim(delim_char, height, horizon):
    if not delim_char or delim_char == '.':
        return ([[] for _ in range(height)], 0, [])
    return util_delimiter(delim_char, height, horizon)


def render_matrix(row_sketches, delim_left, delim_right, align_spec=None):
    """Assemble a matrix grid from rendered row tuples.

    row_sketches: list of (sketch, horizon, amps)
    """
    # Split each row into cells using amps
    all_cells = []
    row_heights = []
    for sketch, horizon, amps in row_sketches:
        cells = _split_row_into_cells(sketch, amps)
        all_cells.append(cells)
        row_heights.append(len(sketch))

    num_cols = max(len(cells) for cells in all_cells) if all_cells else 0

    if not align_spec:
        align_spec = ['c'] * num_cols
    else:
        # Extend align spec to cover extra columns if needed
        while len(align_spec) < num_cols:
            align_spec.append(align_spec[-1])

    # Measure max width per column
    col_widths = [0] * num_cols
    for cells in all_cells:
        for j, cell in enumerate(cells):
            w = len(cell[0]) if cell[0] else 0
            col_widths[j] = max(col_widths[j], w)

    # Assemble each row with specific cell align pad
    grid = []
    for row_idx, cells in enumerate(all_cells):
        row_h = row_heights[row_idx]
        row_sketch = None
        for j in range(num_cols):
            cell = cells[j] if j < len(cells) else [[]]
            cell_w = len(cell[0]) if cell[0] else 0
            if not cell[0] and row_h > 1:
                # empty cell but row is tall
                cell = [[] for _ in range(row_h)]
            elif len(cell) < row_h:
                # pad vertically
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
                padded.append([arts.bg] * left_pad + r + [arts.bg] * right_pad)
                
            if row_sketch is None:
                row_sketch = padded
            else:
                for r in range(row_h):
                    row_sketch[r] = row_sketch[r] + [arts.bg] + padded[r]
        grid.extend(row_sketch)

    grid_height = len(grid)
    grid_horizon = grid_height // 2

    # util_delimiter expands braces of height 2 to height 3. We must expand the grid too.
    if grid_height == 2 and (delim_left in ['{', '}'] or delim_right in ['{', '}']):
        empty_row = [[arts.bg] * len(grid[0])] if grid[0] else [[]]
        grid = [grid[0]] + empty_row + [grid[1]]
        grid_height = 3
        grid_horizon = 1

    # Add delimiters for delimited variants
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
            
        return util_concat(elements, False, False)

    return grid_tup


def render_root(children: list) -> tuple:
    return util_vert_concat(children, [[arts.bg]], "left")


def render_substack(children: list) -> tuple:
    return util_vert_concat(children, [[]], "center")


def render_end(children: list):
    return [[]], 0, []


def render_node(node_type: str, token: tuple, children: list) -> tuple:
    if node_type not in node_data.type_info_dict.keys():
        raise ValueError(f"Undefined control sequence {token[1]}")

    rendering_info = node_data.type_info_dict[node_type][4]
    require_token = rendering_info[0]
    function_name = rendering_info[1]
    rendering_function = globals().get(function_name)

    if not callable(rendering_function):
        raise ValueError(f"Unknown Function {function_name} (internal error)")

    if require_token:
        return rendering_function(token, children)
    else:
        return rendering_function(children)


def _group_children(children_ids, nodes, canvas):
    """Group matrix/alignment rows within children_ids."""
    matrix_bgin_ids = set()
    for cid in children_ids:
        cnode = nodes[cid]
        if cnode[0] == "cmd_bgin":
            env_sketch = canvas[cnode[2][0]]  # opn_envn result
            name_tuple = _env_name_to_tuple(env_sketch[0])
            if name_tuple in MULTI_LINE_ENVS:
                matrix_bgin_ids.add(cid)

    grouped = []  # list of rendered (sketch, horizon, amps)
    consumed_ids = set()
    i = 0
    while i < len(children_ids):
        cid = children_ids[i]
        if cid in matrix_bgin_ids:
            cnode = nodes[cid]
            env_sketch = canvas[cnode[2][0]]
            name_tuple = _env_name_to_tuple(env_sketch[0])
            delim_l, delim_r = MULTI_LINE_ENVS[name_tuple]

            # Formulate the correct align_spec
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
            consumed_ids.add(cid)
            j = i + 1
            while j < len(children_ids):
                next_cid = children_ids[j]
                if nodes[next_cid][0] == "cmd_lbrk":
                    matrix_rows.append(canvas[next_cid])
                    consumed_ids.add(next_cid)
                    j += 1
                else:
                    break
            i = j
            assembled = render_matrix(matrix_rows, delim_l, delim_r, align_spec)
            grouped.append(assembled)
        else:
            grouped.append(canvas[cid])
            i += 1
    return grouped, consumed_ids


def _render_any_root(children_ids, nodes, canvas):
    """Generalized root rendering: group and stack/concat."""
    grouped, consumed_ids = _group_children(children_ids, nodes, canvas)

    if not grouped:
        return [[]], 0, []

    remaining_has_lbrk = False
    for cid in children_ids:
        if nodes[cid][0] == "cmd_lbrk" and cid not in consumed_ids:
            remaining_has_lbrk = True
            break

    if remaining_has_lbrk:
        return render_root(grouped)
    else:
        return util_concat(grouped, False, False)


def preprocess_ast_for_tags(nodes: list) -> None:
    """
    Walk the AST and reorder cmd_tag nodes to the end of their respective lines.
    Lines are typically delimited by cmd_lbrk inside environments or at the root.
    Injects txt_leaf padding nodes for spacing.
    """
    original_node_count = len(nodes)
    for i in range(original_node_count):
        node = nodes[i]
        children_ids = node[2]
        if not children_ids:
            continue

        has_tag = any(nodes[cid][0] == "cmd_tag" for cid in children_ids)
        if not has_tag:
            continue

        new_children = []
        current_line_others = []
        current_line_tags = []

        def flush_line():
            new_children.extend(current_line_others)
            if current_line_tags:
                # Add 3-space padding
                pad3_id = len(nodes)
                nodes.append(("txt_leaf", ("symb", "   "), [], []))
                new_children.append(pad3_id)
                
                for idx, tid in enumerate(current_line_tags):
                    if idx > 0:
                        pad1_id = len(nodes)
                        nodes.append(("txt_leaf", ("symb", " "), [], []))
                        new_children.append(pad1_id)
                    new_children.append(tid)

        for cid in children_ids:
            if nodes[cid][0] == "cmd_lbrk":
                flush_line()
                new_children.append(cid)
                current_line_others = []
                current_line_tags = []
            elif nodes[cid][0] == "cmd_tag":
                current_line_tags.append(cid)
            else:
                current_line_others.append(cid)
                
        flush_line()
        node[2][:] = new_children


def render(nodes: list, debug: bool) -> list:
    preprocess_ast_for_tags(nodes)
    if debug:
        print("Rendering")

    canvas = []
    for i in range(len(nodes)):
        canvas.append(())

    for i in range(len(nodes)-1, -1, -1):
        node = nodes[i]
        node_type = node[0]
        node_token = node[1]
        children_ids = node[2]
        scripts_ids = node[3]

        children = []
        for j in children_ids:
            children.append(canvas[j])

        scripts = []
        for j in scripts_ids:
            scripts.append((nodes[j][0], canvas[j]))

        if node_type in ["opn_root", "opn_brac", "opn_degr", "opn_pren", "opn_brak", "opn_dllr", "opn_ddlr", "opn_text", "opn_envn", "opn_xblw"]:
            child = _render_any_root(children_ids, nodes, canvas)
        elif node_type in ["cmd_ovst", "cmd_undst", "cmd_ovbrc", "cmd_unbrc", "cmd_xarr"]:
            grouped_children, _ = _group_children(children_ids, nodes, canvas)
            sketch, horizon, amps = render_node(node_type, node_token,
                                                grouped_children)
            child = (sketch, horizon, amps)
        else:
            sketch, horizon, amps = render_node(node_type, node_token,
                                                children)
            child = (sketch, horizon, amps)

        if scripts:
            child = render_apply_scripts(child, scripts)

        canvas[i] = child

        if not debug:
            continue
        sketch, horizon, amps = child
        print(f"{node_type}")
        for di in range(len(sketch)):
            arrow = ""
            if di == horizon:
                arrow = f"<-- horizon at {horizon}"
            print(di, "".join(sketch[di]), arrow)

        if not amps:
            continue
        print(len(str(len(sketch)))*" ", end=" ")
        blank_arrow = " "
        for di in range(len(sketch[0])):
            arrow = blank_arrow
            if di in amps:
                blank_arrow = "-"
                arrow = "^"
            print(arrow, end="")
        print(f"---- amps at {amps}")

    if len(canvas) == 0:
        return [[]]

    return canvas[0][0]
