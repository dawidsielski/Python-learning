user_input = input()
upper, lower = 0, 0
for element in user_input:
    if element.islower():
        lower += 1
    elif element.isupper():
        upper += 1

print("UPPER ", upper, "\nLOWER ", lower)