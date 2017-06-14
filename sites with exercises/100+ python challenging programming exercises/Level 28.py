def createList():
    """line 998"""
    sqrt_list = []
    for i in range(1,21):
        sqrt_list.append(i**2)
    print(sqrt_list[-5:])
    print(sqrt_list[5:])

createList()