# from urllib import request
# from operator import add
# shakespeare = request.urlopen('http://inst.eecs.berkeley.edu/~cs61a/fa11/shakespeare.txt')

# words = set(shakespeare.read().decode().split())

# {w for w in words if len(w) >= 5 and w[::-1] in words}
# print(add(2,3))

# Names
from math import pi

from operator import *

radius = 10

area, circ = pi * radius * radius, 2 * pi * radius

def square(x):
    return mul(x, x)

def sum_of_squares(x, y):
    return add(square(x), square(y))

def circ():
    return 2 * pi * radius

