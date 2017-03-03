binary_sequence = input()
binary_sequence = binary_sequence.split(",")
# print(binary_sequence)

for element in binary_sequence:
    if int(element, 2) % 5 == 0:
        print(element, end = " ")