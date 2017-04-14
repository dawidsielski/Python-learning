import os
from datetime import datetime

print(os.getcwd())
os.chdir("C:/Users/Dawid/Documents/Studies/Programowanie/Python-learning")
print(os.getcwd())

# os.mkdir("mkdir_training_folder")
# os.rmdir("mkdir_training_folder")

# os.makedirs("makedirs/dawid/")
# os.removedirs("makedirs/dawid/")

print(os.listdir())

# os.rename('text.txt', 'demo.txt')
print(os.stat('demo.txt'))
print(datetime.fromtimestamp(os.stat('demo.txt').st_mtime))

for dirpath, dirnames, filenames in os.walk("C:/Users/Dawid/Desktop"):
    print(dirpath)
    print(dirnames)
    print(filenames)

print(os.getcwd())
print(os.path.isdir("google-python-exercises"))
print(os.path.isfile("text.txt"))