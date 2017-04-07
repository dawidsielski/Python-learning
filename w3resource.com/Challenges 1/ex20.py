l = [3,5,7,9,11]
k = [3,5,6,7,9]

def if_aritmetic_progression(l):
    difference = l[1] - l[0]
    for element in range(2, len(l)):
        if difference != l[element] - l[element - 1]:
            return False
    return True


print("List: " + str(l) + " " + str(if_aritmetic_progression(l)))
print("List: " + str(k) + " " + str(if_aritmetic_progression(k)))