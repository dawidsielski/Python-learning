import numpy as np

a = np.array([[1,7,3,6],[1,7,4,5]])
print(a)
print(np.sort(a))
print("Sorted axis 0")
print(np.sort(a, axis = 0))
print("Sorted axis 1")
print(np.sort(a, axis = 1))