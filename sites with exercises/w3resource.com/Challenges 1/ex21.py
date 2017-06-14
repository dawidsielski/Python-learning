l = [2,6,18,54]
k = [2,4,8,16,32,63]

def if_aritmetic_progression(l):
    difference = l[1] / l[0]
    for element in range(2, len(l)):
        if difference != l[element] / l[element - 1]:
            return False
    return True


print("List: " + str(l) + " " + str(if_aritmetic_progression(l)))
print("List: " + str(k) + " " + str(if_aritmetic_progression(k)))