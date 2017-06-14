"""line 1089"""

def evenElementsTuple(tup):
    evens = []
    for element in tup:
        if element % 2 == 0:
            evens.append(element)
    return tuple(evens)




t = (1,2,3,4,5,6,7,8,9,10)
print(evenElementsTuple(t))