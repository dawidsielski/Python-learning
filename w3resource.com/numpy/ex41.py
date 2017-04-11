import numpy as np

x = np.arange(4, dtype=np.float)
print(x)
y = np.full(x.shape,10,dtype = x.dtype)
print(y)