def checkio(data):
    non_unique = []
    for element in data:
        if data.count(element) > 1:
            non_unique.append(element)  
    return non_unique


print(checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3])
print(checkio([1, 2, 3, 4, 5]) == [])
print(checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5])
print(checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9])