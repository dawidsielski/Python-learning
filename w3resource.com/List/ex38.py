items = [0,1,2,3,4,5]

for x in range(0, len(items), 2):
    hold = items[x]
    items[x] = items[x + 1]
    items[x + 1] = hold

print(items)