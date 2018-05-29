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

def minProd(k)
    
