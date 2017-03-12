import re

text = "My 387 name is 8475 Dawid slfsd 987 ldjfh879;lkdj 8976khj 78asd78"

print(re.findall(r'\d+', text))
print(re.findall(r'\b\d+\b', text))