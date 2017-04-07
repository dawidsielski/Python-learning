n = int(input("Please enter number: "))

result = 0
n = str(n)
while len(n) >= 2:
    n = str(n)
    for element in n:
        result += int(element)
    n = str(result)
    result = 0

print((n))
