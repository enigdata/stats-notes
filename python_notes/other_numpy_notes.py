import numpy as np
from numpy.core.umath_tests import matrix_multiply

print(matrix_multiply.signature)

us = np.random.random((5, 2, 3)) # 5 2x3 matrics
vs = np.random.random((5, 3, 4)) # 5 3x4 matrices

print(us)
print(vs)

# perform matrix multiplication for each of the 5 sets of matrices

ws = matrix_multiply(us, vs)
print(ws.shape)
print(ws)

#### Saving and loading NDArrays
x1 = np.arange(1, 10).reshape(3,3)
print(x1)

np.savetxt('./x1.txt', x1)

x2 = np.loadtxt('./x1.txt')

print(x2) #data type was not preserved

##Saving to and loading from binary files (much faster and also preserves dtype)

np.save('./x1.npy', x1)
x3 = np.load('./x1.npy')

print(x3)


