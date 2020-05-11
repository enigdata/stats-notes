##### Functions can be passed in as arguments

def grad(x, f, h=0.01):
    return (f(x+h) - f(x-h))/(2*h)

def f(x):
    return x*x**2 + 5*x + 3

print(grad(0, f))

##### Functions can also be returned by functions
import time 
def timer(f):
    def g(*args, **kwargs):
        start = time.time()
        res = f(*args, **kwargs)
        elapsed = time.time() - start
        return res, elapsed
    return g 

def f(n=1000000):
    s = sum([x*x for x in range(n)])
    return s 

timed_func = timer(f)
print(timed_func())

###### Decorators
@timer
def g(n = 1000000):
    s = sum([x*x for x in range(n)])
    return s 

print(g())

print(map(lambda x:x*x, [1,2,3,4]))
print(list(map(lambda x: x*x, [1,2,3,4])))

print(list(filter(lambda x: x%2==0, [1,2,3,4])))

from functools import reduce

reduce(lambda x, y: x*y, [1,2,3,4], 10)
#result is 240

###### List Comprehension
[x*x for x in [1,2,3,4]]
[x for x in [1,2,3,4] if x%2==0]

####### Set and dictionary comprehension

{i%3 for i in range(10)}
{i: i%3 for i in range(10)}

##### Generator Expression
(i**2 for i in range(10,15))

# Generator expressions return a potentially infinite stream, but one at a time thus sparing memory. 
# They are ubiquitous in Python 3, allowing us to handle arbitrarily large data sets.

#Note that count can generate an infinite stream
def count(i=0):
    while True:
        yield i
        i += 1

c = count()
print(next(c))
print(next(c))
print(next(c))

print(list(zip('abcde', count(10))))

#returns [('a', 10), ('b', 11), ('c', 12), ('d', 13), ('e', 14)]

def palindrome_numbers(n):
    yield from range(1, n+1)
    yield from range(n, 0, -1)

print(list(palindrome_numbers(5)))

# [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]

##### Itertools
import itertools as it 

for i in it.islice(count(), 5, 10):
    print(i)

## takewhile()
# take the element from the sequence while the predicate is True
for i in it.takewhile(lambda i: i<5, count()):
    print(i)

import operator as op 

[i for i in it.starmap(op.add, [(1,2), (2,3), (3,4)])]

#returns [3,5,7]

fruits = ['appple', 'banana', 'cherry', 'durain', 'eggplant',  'fig']

for k, group in it.groupby(sorted(fruits, key=len), len):
    print(k, list(group))

import functools as fn 
import numpy as np

rng1 = fn.partial(np.random.normal, 2, 0.3)
rng2 = fn.partial(np.random.normal, 10, 1)

rng1(10)
rng2(10)

print(fn.reduce(op.add, rng2(10)))







