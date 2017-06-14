import re

text = "String \"name\" Dawid"

print(re.findall(r'\"(.*)\"', text))