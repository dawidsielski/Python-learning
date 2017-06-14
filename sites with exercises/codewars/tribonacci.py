def tribonacci(signature,n):
    if n < 3:
        return signature[:n]
    result = signature
    while len(result) < n:
        result.append(result[-1] + result[-2] + result[-3])
    return result


print(tribonacci([1,1,1],10))