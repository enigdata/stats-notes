import numpy as np
from numpy.testing import assert_almost_equal
from distance import euclidean_distance

def test_non_negative():
    for i in range(10):
        u = np.random.normal(3)
        v = np.random.normal(3)
        assert euclidean_distance(u,v) >= 0

def test_when_zero():
    u = np.zeros(3)
    v = np.zeros(3)
    assert euclidean_distance(u,v) == 0

def test_when_not_zero():
    for i in range(10):
        u = np.random.random(3)
        v = np.zeros(3)
        assert euclidean_distance(u, v) != 0

def test_symmetry():
    for i in range(10):
        u = np.random.random(3)
        v = np.random.random(3)
        assert euclidean_distance(u, v) == euclidean_distance(v, u)

def test_triangle():
    u = np.random.random(3)
    v = np.random.random(3)
    w = np.random.random(3)
    assert euclidean_distance(u, w) <= euclidean_distance(u, v) + euclidean_distance(v, w)

def test_known1():
    u = np.array([0])
    v = np.array([3])
    assert_almost_equal(euclidean_distance(u, v), 3)

def test_known2():
    u = np.array([0,0])
    v = np.array([3,4])
    assert_almost_equal(euclidean_distance(u, v), 5)

def test_known3():
    u = np.array([0,0])
    v = np.array([-3, -4])
    assert_almost_equal(euclidean_distance(u, v), 5)

