import re

def find(s):
    pattern = r'^[a-z]+'
    print(re.match(pattern, s))



s = input()
find(s)