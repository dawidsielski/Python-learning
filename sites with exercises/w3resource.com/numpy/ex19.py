import numpy as np

a = np.array([1,1,2,3,4,5,6,6,6])
print(np.unique(a))
print(np.unique(a, return_index = True))