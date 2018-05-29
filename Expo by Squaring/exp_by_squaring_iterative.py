#  fonction qui vérifie d'abord la parité de n, puis calcule x^n 

def expo(x, n):
   
    # on cherche à calculer la valeur de x^n i.e. x**n
    # on suppose que x >= 1 and n >= 0
    # au début on a 0 itération donc on pose s=0 , à la fin de chaque itération, s augment de 1 
   
    s = 0
    r = 1
    while n > 0:
        # si power est pair
        if n % 2 == 0:
            # diviser n par 2
            n = n / 2
            r *= x
            # Multiplier x par soit meme
            x = x * x
        else:
            # on réduit n par 1 
            n = n - 1
            # utiliser le 1 qu'on vient d'enlever
            # on l'enregistre directement dans r
            r = r * x

            # maintenant n est pair, on fait comme la procedure précedante
            n = n / 2
            x = x * x
    s = s+1            

return r,s

# De la meme façon, on met on place une fonction, qui retourne le numéro d'itération pour l'expo x^k
def minProd(k):
   # si n=k alors 0 itérations  
   if k==1 :
        s=0
   # si k=2 alors il faut 1 itération, elle suffit      
    elif k==2:
        s=1
    # sinon 
    else:
        s=2 
        r=3
        while(r<k):
            s=s+1
            r=2*r
        s==s+1
        #retourne la valeur de s à la fin, s indique le nombre d'itération (minimales) pour arriver à x^k  
    return s

# Maintenant on calcule " la somme k allant de 1 à 200 de minProd(k)"
s=0
for k in range (200):
    a=minprod(k)
    s=s+a
   #Afficher le résultat final
print(s)
