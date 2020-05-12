# pip install --pre line-profiler
# pip install psutil
# pip install memory_profiler

#### Timing Code
# 1s = 1000 ms
# 1 ms = 1000 us
# 1 us = 1000 ns

#### Simple approach
import time 
import timeit

def f(nsec = 1.0):
    '''
    Function sleeps for nsec seconds.
    '''
    time.sleep(nsec)

start = timeit.default_timer()
f()
elapsed = timeit.default_timer() - start

print(elapsed)

#### we can make a decorator for convenience
def process_time(f, *args, **kwargs):
    def func(*args, **kwargs):
        import timeit
        start = timeit.default_timer()
        f(*args, **kwargs)
        elapsed = timeit.default_timer() - start
        print(elapsed)
    return func

@process_time
def f1(nsec = 1.0):
    '''
    function sleeps for nsec seconds.
    '''
    time.sleep(nsec)

f1()