def comp(array1, array2):
    for element in range(len(array1)):
        index = (len(array1) - 1 + element) % len(array1)
        if array2[element] != array1[index] ** 2:
            return False
    return True


a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
print(comp(a1, a2))