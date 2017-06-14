sequence = input()

sequence = sequence.split()
unique = []
for element in sequence:
    if element not in unique:
        unique.append(element)
print(" ".join(unique))