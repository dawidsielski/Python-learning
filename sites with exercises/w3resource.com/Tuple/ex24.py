l = [1,2,3,4,(1,2,3)]

count = 0
for element in l:
    if isinstance(element, tuple):
        break
    count += 1

print(count)