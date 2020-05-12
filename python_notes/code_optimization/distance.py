import numpy as np

def euclidean_distance(u,v):
    '''
    Returns Euclidean distance between numpy vectors u and v.
    '''
    w = u-v
    return np.sqrt(np.sum(w**2))


