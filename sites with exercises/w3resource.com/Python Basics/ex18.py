def sum(a,b,c):
    sum = a + b + c
    if a == b == c:
        sum = sum * 3
    return sum


print(sum(1,2,3))
print(sum(3,3,3))
