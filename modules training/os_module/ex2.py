import os

print(os.path.abspath("ex1.py"))

print(os.path.isfile("demo.txt"))


if (os.path.isfile("demo.txt")):
    os.rename("demo.txt", "text.txt")
    print(os.stat("text.txt"))
else:
    os.rename("text.txt", "demo.txt")
    print(os.stat("demo.txt"))

print(os.listdir(os.getcwd()))