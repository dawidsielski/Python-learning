import re

def find(s):
    pattern = r'ab{2,3}'
    if (re.search(pattern, s)):
        print("Text found")
    else:
        print("Text not found")


s = input()
find(s)