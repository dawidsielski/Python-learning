import collections

l = [1,2,3,1,2,3,1,2,4,1,1,1,1]
ctr = collections.Counter(l)

min_val = 1
max_val = 3
for i in range(min_val,max_val):
    print(str(i) + " is " + str(ctr[i]) + " times in: " + str(l))