import os

for dirpaths, dirnames, filenames in os.walk(os.getcwd()):
    print(dirpaths)
    print(dirnames)
    print(filenames)
    print()