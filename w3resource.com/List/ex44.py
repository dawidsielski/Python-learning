items = []

for i in range(5):
    l = []
    for j in range(5):
        l.append(i * 5 + j + 1)
    items.append(l)

print(items)


print([ [x * 5 + y + 1 for y in range(5) ] for x in range(5)])