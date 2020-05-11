import numpy as np
import timeit

#The base structure in numpy is ndarray, used to represent vectors, matrices and higher-dimensional arrays. Each ndarray has the following attributes:

# dtype = corresponds to data types in C
# shape = dimensions of array
# strides = number of bytes to step in each direction when traversing the array

x = np.array([1,2,3,4,5,6])
print(x)
print('dtype:', x.dtype)
print('shape:', x.shape)
print('strides:', x.strides)

x.shape = (2,3)
print(x)
print('dtype:', x.dtype)
print('shape:', x.shape)
print('strides:', x.strides)

x = x.astype('complex')
print(x)
print('dtype:', x.dtype)
print('shape:', x.shape)
print('strides:', x.strides)

#### Array creation 
print(np.array([1,2,3], np.float64))

print(np.arange(3))

print(np.arange(3,6,0.5))

print(np.ones(3))

print(np.zeros((3,4)))

print(np.eye(4))

print(np.diag([1,2,3,4]))

print(np.fromfunction(lambda i,j: i**2+j**2, (4,5)))


###### Array manipulation
x = np.fromfunction(lambda i,j: i**2+j**2, (4,5))

x = x.astype(np.int64)

print(x)

print(x.T)

print(x.reshape(2, -1))

## Boolean indexing 

print(x >=2)

print(x[x>=2])

##### Calculations and broadcasting

#Broadcasting refers to the set of rules that numpy uses to perfrom operations on arrays with different shapes. 

x = np.fromfunction(lambda i,j: i**2+j**2, (2,3))
print(x)

print(x*5)

print(x+x)

print(np.exp(x))

##The @ symbol denotes matrix multiplication in numpy

print(x @ x.T)

print(x.T @ x)

##### Combining and splitting arrays

np.r_[x,x] #row-wise stack

np.vstack([x,x]) #vertical stack

np.concatenate([x,x], axis = 0) #concatenate row-wise

np.c_[x,x] #column-wise stack

np.hstack([x,x]) # horizontal stack

np.concatenate([x,x], axis=1) # concatenate column-wise

y = np.r_[x,x]

a,b,c=np.hsplit(y,3)

print(c)

####### Reductions
y.sum()

y.sum(0) #column sum

y.sum(1) #row sum

#### Standardize by column mean and standard deviation
z = (y - y.mean(0))/y.std(0)














