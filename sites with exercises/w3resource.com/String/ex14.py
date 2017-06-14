text = "red, white, black, red, green, black".split()

print(text)

unique = []
for element in text:
    if element not in unique:
        print(element)
        unique.append(element)

print(unique)