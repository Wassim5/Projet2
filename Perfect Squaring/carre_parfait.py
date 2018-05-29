# An Efficient Method to count squares between a
# and b
#import numpy as geek
#import numpy as np
import math
from itertools import chain, combinations, product, permutations
import functools
import operator
#compter le nombre de carrés parfaits entre deux bornes a et b
def CountSquares(a, b):
    return (math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1)

#former les sous-ensembles (combinaisons) des éléments d'une liste
def powerset(iterable):
    """
    powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    """
    xs = list(iterable)
    return chain.from_iterable(combinations(xs,n) for n in range(len(xs)+1))

#verifier si un nombre n est premier
def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

#définir les bornes inférieure v1 et supérieure b de la liste
v1 = 40
v2 = 56
#construire la liste selon les bornes v1 et v2
a = list(range(v1, v2))
#print a
#utiliser une autre liste de travail b qui contient les éléments de la liste a
b = a
for i in a:
    #print i, is_prime(i)
    #enlever les nombres premiers et ses multiples
    if is_prime(i):
        for n in range(i*i, v2, i):
            #print n
            a.remove(n)
        b.remove(i)
#print b
#variable qui compte le nombre de sous-ensembles non vides dans lesquels le produit de tous les éléments est un carré parfait.
cnt = 0
for part in list(powerset(set(b))):
    #print part
    ns = 0
    prod = 1
    #exclure le sous-ensemble vide du test
    if len(part) != 0:
        #calculer la racine carrée du produit des éléments d'un sous-ensemble part
        root = math.sqrt( functools.reduce(operator.mul, part, 1))
        r = int(root + 0.5) ** 2
        #verifier que la racine carrée est entière afin de mettre le nombre de carrés parfaits ns à 1
        if r ==  functools.reduce(operator.mul, part, 1):
            ns += 1
    #incrémenter cnt quand le produit des éléments du sous-ensemble part en cours est un carée parfait (ns==1)
    if ns != 0: cnt += 1
    #print ns
print ("Le nombre de ous-ensembles où le produit de ses éléments est un carré parfait est:", cnt)

#b = list(np.prod(powerset(list(range(40, 56)))))
