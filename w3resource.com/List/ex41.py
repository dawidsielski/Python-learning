obj = {}
for i in range(1, 21):
    obj[str(i)] = []
print(obj)

obj["1"].append(1)
print(obj)


multiple_lists = []
for i in range(10):
    multiple_lists.append([])

print(multiple_lists)