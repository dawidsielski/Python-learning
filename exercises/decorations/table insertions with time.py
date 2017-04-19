def square_list(l):
    result = []
    for element in l:
        result.append(element ** 2)
    return result

def cube_list(l):
    result = []
    for element in l:
        result.append(element ** 3)
    return result


print(square_list(range(10)))
print(cube_list(range(10)))