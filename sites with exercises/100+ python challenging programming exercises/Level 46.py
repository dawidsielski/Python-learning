"""line 1602"""

def fibbonaci(n):
    fin = [1,1]
    for i in range(2,n):
        fin.append(fin[i - 1] + fin[i - 2])
    return fin[n - 1]

print(fibbonaci(7))