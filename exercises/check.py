x = sum([ x for x in [1,2,3,11,22] if (x >= 10 and x <= 99) or (x >= -99 and x <= -10)])
print(x)

def solution(X):
    result = [0 for x in range(X)]
    for i in range(1,X + 1):
        for dwarf_number in range(1, X + 1):
            x = i * dwarf_number
            if x > X:
                break
            if result[x - 1] == 0:
                result[x - 1] = 1
            else:
                result[x - 1] = 0
    return result

print('Solution: ' + str(solution(4)))
