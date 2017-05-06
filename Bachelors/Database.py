import os
import shelve
from PIL import Image
from Chain import *
import sys

sys.setrecursionlimit(5000)


script_dir = os.path.dirname(os.path.abspath(__file__))
# print(script_dir)
absolute_path_trees = os.path.join(script_dir, "trees")
trees_content = os.listdir(absolute_path_trees)
# print(len(trees_content))

for element in trees_content[:4]:
    print(element)
    path = os.path.join(absolute_path_trees, element)
    tree = Image.open(path)
    imfile = tree.convert("1", dither = Image.NONE)
    c = Chain(imfile)
    print(c.chain_code)