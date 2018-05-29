#F1
#fonction qui vérifie si un entier est premier, en le divisant par tous les entier depuis son milieu jusqu'à 2, et retourne la réponse
import math
def prim(x):
	prim=True

	if x!=2:
		for i in range (2, int(x**(1/2)+1)):
			if x%i==0:
				prime=False
				break

	return prim

#F2
# fonction qui recherche les nombre premier, entre deux entier ( départ , arrivée) et les enregistre dans une liste 

def trouv_prims(a, b):
	s = set()
	
	for i in range(a, b+1):
		if trouv_prim(i):
			s.add(i)
	
	return s
  
  
  #F3
from itertools import chain, combinations, product, permutations
import functools
import operator
#CountSquares compte le nombre de carré parfait dans un intervalle donné
def CountSquares(a, b):
    return (math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1)

  #F4
#Powerset forme les sous-ensembles (combinaisons) à partir des elements d'un ensemble donné
def powerset(iterable):
    """
    powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    """
    xs = list(iterable)
    # note: on retourne un itérateur au lieu d'une liste
    return chain.from_iterable(combinations(xs,n) for n in range(len(xs)+1))

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
    if prim(i):
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
print ("Le nombre de carrées est:", cnt)

#b = list(np.prod(powerset(list(range(40, 56)))))
