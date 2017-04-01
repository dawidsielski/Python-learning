def facto(number):
    result = 1
    for element in range(1,number + 1):
        result *= element
    return result

print(facto(5))