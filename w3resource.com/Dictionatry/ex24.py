s = "w3resource"
d = {}
for element in s:
    if element in d.keys():
        d[element] += 1
    else:
        d[element] = 1

print(d)
