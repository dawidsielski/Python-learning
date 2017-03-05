def fibbonaci(n):
    fin = [1,1]
    for i in range(2,n):
        fin.append(fin[i - 1] + fin[i - 2])
    return fin

fib = fibbonaci(7)
print(",".join([str(x) for x in fib]))