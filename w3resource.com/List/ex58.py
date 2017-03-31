l1 = [1, 3, 5, 7, 9, 10]
l2 = [2, 4, 6, 8]

import itertools as it
l1.pop()
print(list(it.chain(l1,l2)))