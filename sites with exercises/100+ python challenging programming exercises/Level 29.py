def createList():
    """line 1044"""
    sqrt_list = []
    for i in range(1,21):
        sqrt_list.append(i**2)
    return tuple(sqrt_list)

print(createList())