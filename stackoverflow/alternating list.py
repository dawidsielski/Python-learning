list_A = ['A1', 'A2', 'A3'] 
list_B = ['B1', 'B2', 'B3', 'B4', 'B5']

zipped = list(zip(list_A,list_B))

concatenated = []
for element in zipped:
    concatenated.append(element[0] + element[1])

print(concatenated)