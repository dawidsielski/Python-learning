def computeSum(n):
    sum = 0
    for i in range(1,n + 1):
        sum += float(i / ( i + 1 ))
    return sum

print(computeSum(5))