import numpy as np

a = np.array([1,2,3])
print(a)
print(type(a))
x = a.shape
print(x)
print(x[0])


b = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(b.shape)
print(b.shape[0])
print(b.shape[1])
print(b[0,1])

a = np.zeros((2,2))
print(a)
a = np.ones((2,2))
print(a)
a = np.eye(2)
print(a)

a = np.random.random((4,4)) * 10
print(a)

print(np.arange(4))


x = np.linspace(10,20,8, endpoint = False) 
print (x)