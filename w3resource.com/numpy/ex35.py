import numpy as np

a = np.arange(12)
print(a)
print(np.reshape(a,(3,4)))
print(np.shape(a))
a.shape = (4,3)
print(a)
print(a.shape)