def solution(X):
    result = [0 for x in range(X)]
    for i in range(1, X + 1):
        for dwarf_number in range(1, X + 1):
            x = i * dwarf_number
            if x > X:
                break
            if result[x - 1] == 0:
                result[x - 1] = 1
            else:
                result[x - 1] = 0
    return result