from chain import *
import os

file_path = os.path.dirname(os.path.abspath(__file__))
# print(file_path)
images_path = os.path.join(file_path, "Testing database")
# print(images_path)
os.chdir(images_path)

files_in_dir = os.listdir()
# print(files_in_dir)
paths = [os.path.join(images_path, x) for x in files_in_dir]

for element in paths[2:-1]:
    tree = Image.open(element)
    imfile = tree.convert("1", dither = Image.NONE)
    c = Chain(imfile)
    print(element)
    c.print_information()