import re

text = "ala ma kota 50 5 elementarz afrodyzjak"

for m in re.finditer("\d+", text):  
    print(m.group(0))  
    print("Index position:", m.start())  