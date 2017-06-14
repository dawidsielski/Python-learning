import re

def find(s):
    pattern = r'.*z.*'
    print(re.match(pattern, s))


s = input()
find(s)