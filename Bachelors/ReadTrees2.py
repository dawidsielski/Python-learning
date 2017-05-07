import os
from PIL import Image
from Chain import *
import shelve

# print(os.path.dirname())

script_path = os.path.dirname(os.path.realpath(__file__))
trees2_absolute_path = os.path.join(script_path, 'trees2')

trees2_chain_code = shelve.open('trees2_database')

for root, dirname, filenames in os.walk(trees2_absolute_path):
    print(root)
    print("Dirname: ", dirname)
    for name in filenames:
        print(name)

        path = os.path.join(root, name)
        tree = Image.open(path)
        imfile = tree.convert("1", dither = Image.NONE)
        c = Chain(imfile)
        information = {'Code' : c.chain_code, "Border pixel" : c.points, "Perimeter" : c.perimeter, \
                        "Shape height" : c.shape_height, "Shape width" : c.shape_width, "First black" : c.begin, "Last black" : c.end}
        trees2_chain_code[name] = information
        print(c.chain_code)

trees2_absolute_path.close()