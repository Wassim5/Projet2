#F1
#fonction qui vérifie si un entier est premier, en le divisant par tous les entier depuis son milieu jusqu'à 2, et retourne la réponse
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
  
  
  #F
