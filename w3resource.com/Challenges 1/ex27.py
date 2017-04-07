l = [0,1,2,3,0,4,5,6]

n_zeros = l.count(0)
l = list(filter(lambda x : x != 0, l))
for n in range(n_zeros):
    l.append(0)

print(l)