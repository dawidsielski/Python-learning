import numpy as np

a = np.eye(4,4)
print(a.size)
print(a.itemsize)

print("Amount of memory: %d" % (a.size * a.itemsize))