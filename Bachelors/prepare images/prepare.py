import os
from PIL import Image
import shelve

print(os.getcwd())

path = r'C:\Users\Dawid\Documents\Studies\Programowanie\Python-learning\Bachelors'
trees2_absolute_path = os.path.join(path, 'trees2')


for root, dirname, filenames in os.walk(trees2_absolute_path):
    print(root)
    print("Dirname: ", dirname)
    for name in filenames:
        # print(name)
        image_path = os.path.join(root, name)
        img = Image.open(image_path)