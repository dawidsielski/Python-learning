import re

text = "Dawid    work       hard"
print(re.sub(r'\s+', "", text))