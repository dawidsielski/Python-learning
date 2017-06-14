for element in range(5):
    print(element)
else:
    print("It will be printed because no brake statement called")

print()

for element in range(5):
    if element == 3:
        break
    print(element)
else:
    print("not printed")