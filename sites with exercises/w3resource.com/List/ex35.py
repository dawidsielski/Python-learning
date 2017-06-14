l = ["p" , "q", "r"]

numbers = [x for x in range(1,3)]

concatenated = []
for element in l:
    for number in numbers:
        concatenated.append(element + str(number))

print(concatenated)
