import os

print(os.path.basename('/tmp/basename.txt'))
print(os.getcwd())
print(os.path.abspath(os.getcwd()))
print(os.path.dirname(os.getcwd()))
print("Absolute path to file: ", os.path.dirname(os.path.abspath(__file__)))
print(os.path.abspath(__file__))

# print(dir(os.path))

print(os.path.split(os.path.dirname(os.path.abspath(__file__))))
print(os.path.realpath(os.path.dirname(os.path.abspath(__file__))))