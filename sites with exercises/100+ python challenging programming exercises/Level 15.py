def compute_value(n):
    result = 0
    for times in range(4):
        result += int(str(n) * (times + 1))
    return result


print(compute_value(9))