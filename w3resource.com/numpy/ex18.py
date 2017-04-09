import numpy as np

a = np.array([1,2,3,4])
b = np.array([1,2,3,5,7])
print(a)
print(b)

print(np.intersect1d(a,b))