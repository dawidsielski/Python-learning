import re

def find(s):
    pattern = r'^[a-zA-Z_]+$'
    print(re.search(pattern, s))


s = input()
find(s)