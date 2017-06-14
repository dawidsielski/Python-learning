import re

def find(s):
    pattern = r'[A-Z][a-z]+'
    if (re.search(pattern, s)):
        print("Text found")
    else:
        print("Text not found")


s = input()
find(s)