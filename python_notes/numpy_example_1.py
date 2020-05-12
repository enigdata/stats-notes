import numpy as np
##### Example: Calculating pairwise distance matrix using broadcasting and vectorization

# Calculate the pairwise distance matrix between the following points

# (0,0)
# (4,0)
# (4,3)
# (0,3)

def distance_matrix(pts):
    '''
    returns matrix of pairwise Euclidean distances. Pure Python version.
    '''
    n = len(pts)
    p = len(pts[0])
    m = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            s = 0 
            for k in range(p):
                s += (pts[i, k] - pts[j, k]) ** 2 

            m[i, j] = s ** 0.5 
    return m 

def distance_matrix_np(pts):
    '''
    returns matrix of pairwise Euclidean distances. Vectorized numpy version.
    '''
    return np.sum((pts[None, :] - pts[:, None])**2, -1)**0.5

pts = np.array([(0,0), (4,0), (4,3), (0,3)])
print(pts)

print(pts[None, :])
print(pts[None, :].shape)
print(pts[:, None])
print(pts[:, None].shape)

m = pts[None, :] - pts[:, None]
print(m)
print(m.shape) # (4,4,2)

m ** 2

#We want to end up with a 4 by 4 matrix, so sum over the axis with dimension 2. This is axis=2, or axis=-1 since it is the first axis from the end.

# timeit results
#Python version: best of 3: 3.26 s per loop
#Numpy version: best of 3: 77.3 ms per loop

#### But don't give up on loops yet
from numba import njit 

@njit
def distance_matrix_numba(pts):
    n = pts.shape[0]
    p = pts.shape[1]
    dist = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            s = 0 
            for k in range(p):
                s += (pts[i, k] - pts[j,k])**2 
            dist[i, j] = s 

    return np.sqrt(dist)

# The slowest run took 27.17 times longer than the fastest. This could mean that an intermediate result is being cached
# best of 3: 16.1 ms per loop








        





