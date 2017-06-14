import re

def find(s):
    pattern = r'a.+b'
    if (re.search(pattern, s)):
        print("Text found")
    else:
        print("Text not found")


s = input()
find(s)