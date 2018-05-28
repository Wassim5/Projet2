# An Efficient Method to count squares between a
# and b
#import numpy as geek
#import numpy as np
import math
from itertools import chain, combinations, product, permutations
import functools
import operator
def CountSquares(a, b):
    return (math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1)


def powerset(iterable):
    """
    powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    """
    xs = list(iterable)
    # note we return an iterator rather than a list
    return chain.from_iterable(combinations(xs,n) for n in range(len(xs)+1))

import math
def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

#1000, 1234)mod1000000007
v1 = 40
v2 = 56
#v1 = 1000
#v2 = 1234
a = list(range(v1, v2))
#print a
b = a
c = []
for i in a:
    #print i, is_prime(i)
    if is_prime(i):
        c.append(i)
        for n in range(i*i, v2, i):
            #print n
            a.remove(n)
        b.remove(i)
#print b
#c = list((powerset(set(b))))
#print c
#print b
cnt = 0
for part in list(powerset(set(b))):
    #print part
    ns = 0
    prod = 1
    if len(part) != 0:
        root = math.sqrt( functools.reduce(operator.mul, part, 1))
        r = int(root + 0.5) ** 2
        if r ==  functools.reduce(operator.mul, part, 1):
            ns += 1
    if ns != 0: cnt += 1
    #print ns
print ("Count of squares is:", cnt)

#b = list(np.prod(powerset(list(range(40, 56)))))
