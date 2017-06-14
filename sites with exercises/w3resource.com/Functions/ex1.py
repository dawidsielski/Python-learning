def max_of_two(a,b):
    if a > b:
        return a
    return b


def max_of_three(a,b,c):
    max_two = max(a,b)
    return max_of_two(max_two,c)

print(max_of_three(1,4,7))