text = input()

first = text[0]
text = text.replace(first, "$")

# text[0] = first
print(first + text[1:])