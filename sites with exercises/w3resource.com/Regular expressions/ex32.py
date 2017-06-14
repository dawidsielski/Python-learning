import re
text = 'Hello world, hello.'
print(re.sub("[ ,.]", ":", text, 2))