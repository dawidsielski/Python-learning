import re

text = "hello java python testx"
print(re.findall(r'\b[a-z]{5}\b', text))