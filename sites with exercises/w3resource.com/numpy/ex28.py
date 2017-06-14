import numpy as np

a = np.arange(6).reshape(2,3)
print(a)
b = np.arange(-1,5).reshape(2,3)
print(b)

print(np.greater(a,b))
print(np.greater_equal(a,b))
print(np.less(a,b))
print(np.less_equal(a,b))