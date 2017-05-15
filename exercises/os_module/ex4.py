import os

print(os.path.basename('/tmp/basename.txt'))
print(os.path.abspath(os.getcwd()))
print(os.path.abspath())
print(os.path.dirname(os.getcwd()))
print(os.path.dirname(os.path.abspath(__file__)))

print(dir(os.path))

