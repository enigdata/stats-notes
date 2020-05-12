import time 
from numpy.testing import assert_almost_equal

def timer(f, *args, **kwargs):
    start = time.clock()
    ans = f(*args, **kwargs)
    return ans, time.clock() - start

##### Using numespr

#One of the simplest approaches is to use `numexpr <https://github.com/pydata/numexpr>`__ which takes a numpy expression and compiles a more efficient version of the numpy expression written as a string. 
# If there is a simple expression that is taking too long, this is a good choice due to its simplicity. However, it is quite limited.

import numpy as np 

a = np.random.random(int(1e6))
b = np.random.random(int(1e6))
c = np.random.random(int(1e6))

b**2 - 4*a*c

#3 loops, best of 3: 9.94 ms per loop

import numexpr as ne 

ne.evaluate('b**2 - 4*a*c')

#3 loops, best of 3: 1.87 ms per loop

###### Using numba
#When it works, the JIT numba can speed up Python code tremendously with minimal effort.


#Example
import numba 
from numba import jit 

def matrix_multiplication(A, B):
    m, n = A.shape 
    n, p = B.shape
    C = np.zeros((m,p))
    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i,j] += A[i,k]*B[k,j]
    return C 

A = np.random.random((30,50))
B = np.random.random((50, 40))

@jit 
def matrix_multiplication_numba(A, B):
    m, n = A.shape 
    n, p = B.shape
    C = np.zeros((m,p))
    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i,j] += A[i,k]*B[k,j]
    return C 

## numpy version
def matrix_multiplication_numpy(A,B):
    return A.dot(B)

## using nopython
def mc_pi(n):
    x = np.random.uniform(-1, 1, (n,2))
    return 4*np.sum((x**2).sum(1) < 1)/n 

# 10 loops, best of 3: 54.9 ms per loop

@jit 
def mc_pi_numba(n):
    x = np.random.uniform(-1, 1, (n,2))
    return 4*np.sum((x**2).sum(1) < 1)/n 

#10 loops, best of 3: 50.4 ms per loop

@jit(nopython=True)
def mc_pi_nopython(n):
    x = np.random.uniform(-1, 1, (n,2))
    return 4*np.sum((x**2).sum(1) < 1)/n

from numba.errors import TypingError

try:
    mc_pi_nopython(n)
except TypingError:
    print('Unable to convert to pure C code.')

##Using cache=True




