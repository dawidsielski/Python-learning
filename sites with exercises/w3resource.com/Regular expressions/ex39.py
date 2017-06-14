import re

text = "Dawid   hello   abroad names"
print(re.sub(r' +', " ", text))