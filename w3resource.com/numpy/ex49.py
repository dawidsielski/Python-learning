import numpy as np

a = np.eye(3)
print(a)

print(np.ravel(a))
print(np.ravel(a, order='F')) #does throught columns
#in this case both look the same