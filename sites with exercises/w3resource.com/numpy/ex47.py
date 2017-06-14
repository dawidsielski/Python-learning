import numpy as np

a = np.tri(5,5)
print(a)
print()
print(a.T)
print()

a = np.tri(5,5, -1)
print(a)
print()

a = np.tri(5,5, 1)
print(a)
print()