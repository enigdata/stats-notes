import numpy as np 

xs = np.random.randint(0, 1000, 100)
ys = np.random.randint(0, 1000, 100)

#### Using lists
def get_common(xs, ys):
    '''
    Using lists
    '''
    common = set()
    for x in xs:
        for y in ys:
            if x==y:
                common.add(x)
    return zs 

### 3 loops, best of 3: 872 µs per loop

#### Using sets
set(xs) & set(ys)

### 3 loops, best of 3: 27.2 µs per loop

#### Python idioms for speed
# string concatenation
def concat1(alist):
    '''
    Using string concatenation
    '''
    s = alist[0]
    for item in alist[1:]:
        s += " " + item 
    return s 

def concat2(alist):
    '''
    Using join
    '''
    return " ".join(alist)

alist = ['abcde', 'fg'] * 1000000

#concat1 3 loops, best of 3: 170 ms per loop
#concat2 3 loops, best of 3: 11.9 ms per loop

#### Avoiding loops
import math 

def loop1(n):
    '''
    using for loop with function call
    '''
    z = []
    for i in range(n):
        z.append(math.sin(i))
    return z 

def loop2(n):
    '''
    using local version of function.
    '''
    z = []
    sin = math.sin 
    for i in range(n):
        z.append(sin(i))
    return z 

def loop3(n):
    '''
    using list comprehension
    '''
    sin = math.sin 
    return [sin(i) for i in range(n)]

def loop4(n):
    '''
    using map
    '''
    sin = math.sin 
    return list(map(sin, range(n)))

def loop5(n):
    '''
    using numpy
    '''
    return np.sin(np.arange(n)).tolist() 

n = 1000000

# 1 loop, best of 1: 323 ms per loop
# 1 loop, best of 1: 276 ms per loop
# 1 loop, best of 1: 234 ms per loop
# 1 loop, best of 1: 234 ms per loop
# 1 loop, best of 1: 77.6 ms per loop

#### Using in-place operations
a = np.arange(1e6)

%timeit global a; a = a * 0
%timeit global a; a *= 0

# 1000 loops, best of 3: 677 µs per loop
# 1000 loops, best of 3: 484 µs per loop

#### Using appropriate indexing
def idx1(xs):
    '''
    using loops
    '''
    s = 0
    for x in xs:
        if (x>10) and (x<20):
            s += x 
    return s 

def idx2(xs):
    '''
    using logical indexing
    '''
    return np.sum(xs[(xs>10) & (xs<20)])

n = 1000000
xs = np.random.randint(0, 100, n)

# 3 loops, best of 3: 253 ms per loop
# 3 loops, best of 3: 3.64 ms per loop

##### Using generalized universal functions 
xs = np.random.random((1000, 10))
print(xs)

ys = np.random.random((1000, 10))

from numpy.core.umath_tests import inner1d

%timeit -n3 -r3 np.array([x @ y for x, y in zip(xs, ys)])
%timeit -n3 -r3 inner1d(xs, ys)

# 3 loops, best of 3: 945 µs per loop
# 3 loops, best of 3: 14 µs per loop

###### Memoization
from functools import lru_cache

def fib(n):
    if n <= 2:
        return 1 
    else:
        return fib(n-1) + fib(n-2)

# A simple example of memoization - in practice, use `lru_cache` from functools
def memoize(f):
    store = {}
    def func(n):
        if n not in store:
            store[n] = f(n)
        return store[n]

    return func     

@memoize
def mfib(n):
    return fib(n)

@lru_cache
def lfib(n):
    return fib(n)

assert(fib(10) == mfib(10))
assert(fib(10) == lfib(10))

# 10 loops, best of 1: 263 ms per loop
# 10 loops, best of 1: 25.9 ms per loop
# 10 loops, best of 1: 26.3 ms per loop