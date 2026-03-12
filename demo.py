import sys
import os

# Ensure the src directory is in the path
sys.path.insert(0, os.path.abspath("src"))

import renderer
from pipeline import render_tex

def demo():
    # tex = r"""\begin{bmatrix} b_{d1} \\ b_{d2} \\ b_{c1} \\ b_{c2} \end{bmatrix} = \begin{bmatrix} S_{dd11} & S_{dd12} & S_{dc11} & S_{dc12} \\ S_{dd21} & S_{dd22} & S_{dc21} & S_{dc22} \\ S_{cd11} & S_{cd12} & S_{cc11} & S_{cc12} \\ S_{cd21} & S_{cd422} & S_{cc21} & S_{cc22} \end{bmatrix} \cdot \begin{bmatrix} a_{d1} \\ a_{c2} \\ a_{c1} \\ a_{c2} \end{bmatrix}"""
    tex = r"""\begin{bmatrix} b_{d1} \\ b_{d2} \\ b_{c1} \\ b_{c2} \end{bmatrix} = \begin{bmatrix} S^{56} & S_{dd12}^{2} & S_{dc11} & S_{dc12} \\ S_{dd21} & S_{dd22} & S_{dc21} & S_{dc22} \\ S_{cd11} & S_{cd12} & S & S_{cc12} \\ S_{cd21} & S_{cd422} & S_{cc21} & S_{cc22} \end{bmatrix} \cdot \begin{bmatrix} a_{d1} \\ a_{c2} \\ a_{c1} \\ a_{c2} \end{bmatrix}"""
    
    options = {"fonts": "normal"}
    
    print("=================== SCRIPT_ORDER = 'sub_sup' ===================")
    renderer.CONFIG_SCRIPT_ORDER = "sub_sup"
    tex_sub_sup = r"S_{dd11}^3"
    print(f"Expression: {tex_sub_sup}")
    print(render_tex(tex_sub_sup, False, False, "raw", options))
    print()
    
    print("Full matrix:")
    print(render_tex(tex, False, False, "raw", options))
    print("\n")

    print("=================== SCRIPT_ORDER = 'sup_sub' ===================")
    renderer.CONFIG_SCRIPT_ORDER = "sup_sub"
    tex_sup_sub = r"S_{dd11}^3"
    print(f"Expression: {tex_sup_sub}")
    print(render_tex(tex_sup_sub, False, False, "raw", options))
    print()

    print("Full matrix:")
    print(render_tex(tex, False, False, "raw", options))
    print("\n")

if __name__ == "__main__":
    demo()
