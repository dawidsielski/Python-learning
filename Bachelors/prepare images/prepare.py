import os
from PIL import Image
import shelve

print(os.getcwd())

path = r'C:\Users\Dawid\Documents\Studies\Programowanie\Python-learning\Bachelors'
trees2_absolute_path = os.path.join(path, 'trees2')

trees2 = open("trees2_paths.txt", "w")


for root, dirname, filenames in os.walk(trees2_absolute_path):
    print(root)
    print("Dirname: ", dirname)
    for name in filenames:
        # print(name)
        # print(os.path.join(root, name))
        trees2.write(os.path.join(root, name))
        trees2.write("\n")

trees2.close()
