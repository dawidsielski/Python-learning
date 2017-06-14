import re

s = "Exercises number 1, 12, 13, and 345 are important"

print(re.findall(r'[0-9]{1,3}', s))