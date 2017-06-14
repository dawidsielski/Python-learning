
max_val = 100
l = [x for x in range(2,max_val + 1)]
primes = []

for p in l:
    erase = 2*p
    print(erase)
    while erase <= max_val:
        if erase in l:
            l.remove(erase)
        erase += p
print(l)