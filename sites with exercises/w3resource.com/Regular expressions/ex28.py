import re

text = "ala ma kota elementarz afrodyzjak"

result = re.findall(r'\b[ae][a-z]+\b', text)
print(result)

for element in re.finditer(r'\b[ae][a-z]+\b', text):
    s = int(element.start())
    e = int(element.end())
    print("Start " + str(s) + " ending " + str(e) + " string: " + text[s: e])