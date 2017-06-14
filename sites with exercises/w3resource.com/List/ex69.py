list_of_lists =  [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]

result = []

for element in list_of_lists:
    if element not in result:
        result.append(element)

print(result)