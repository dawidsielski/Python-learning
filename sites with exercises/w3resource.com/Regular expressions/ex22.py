import re

text = "string in which I am going to find another string"

for match in re.finditer("string", text):
    s = match.start()
    e = match.end()
    print('Found "%s" at %d:%d' % (text[s:e], s, e))