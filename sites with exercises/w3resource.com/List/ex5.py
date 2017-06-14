items = ['abc', 'xyz', 'aba', '1221']

number_of_elements = 0
for element in items:
    if len(element) >= 2 and element[0] == element[len(element) - 1]:
        print(element)
        number_of_elements += 1
print(number_of_elements)