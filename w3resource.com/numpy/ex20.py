import numpy as np

a = np.array([0, 10, 20, 40, 60, 80], dtype = float)
print(a)
b = np.array([10, 30, 40, 50, 70, 90], dtype = float)
print(b)

print(np.setdiff1d(a,b))
