import numpy as np

#Another example of numpy trickery is to construct a leave-one-out matrix of a vector of length k. 
# In the matrix, each row is a vector of length k-1, with a different vector component dropped each time. 
# This can be used for LOOCV to evalaute the out-of-sample accuracy of a predictive model.

N = 5 
print(np.tri(N))

#Create a triangular matrix with N rows, N-1 columns and offset from diagnonal by -1
print(np.tri(N, N-1))

print(np.tri(N, N-1, -1))

# Use broadcasting to create a new index matrix

np.arange(1, N)

print(np.arange(1, N) - np.tri(N, N-1, -1))

index_matrix = (np.arange(1, N) - np.tri(N, N-1, -1)).astype(int)

print(index_matrix)

data = np.array([(1,4), (2,7), (3,11), (4,9), (5,15)])
print(data)

print(data[index_matrix].shape)

print(data[index_matrix])

########## Another example: all but one
def f1(arr, k):
    idx = np.ones_like(arr).astype('bool')
    idx[k]=0
    return arr[idx]

def f2(arr,k):
    return np.r_[arr[:k], arr[k+1:]]


