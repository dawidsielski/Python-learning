import re

text = "this-is cat "

text = re.sub("\s","_",text)
print(text)
