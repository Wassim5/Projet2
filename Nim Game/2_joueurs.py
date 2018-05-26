import string
import random
import time
import sys

def print_rules():
    print ("\n")
    time.sleep(0.1)
    print ("\n")
    time.sleep(0.1)
    print ("                 ___           ___    ")
    time.sleep(0.1)
    print ("    ___         /\__\         /\  \      ")
    time.sleep(0.1)
    print ("   /\__\       /:/ _/_        \:\  \    ")
    time.sleep(0.1)
    print ("  /:/__/      /:/ /\__\        \:\  \       ")
    time.sleep(0.1)
    print (" /::\  \     /:/ /:/ _/_   ___  \:\  \    ")
    time.sleep(0.1)
    print (" \/\:\  \   /:/_/:/ /\__\ /\  \  \:\__\  ")
    time.sleep(0.1)
    print ("    \:\  \  \:\/:/ /:/  / \:\  \ /:/  /  ")
    time.sleep(0.1)
    print ("     \:\__\  \::/_/:/  /   \:\  /:/  /  ")
    time.sleep(0.1)
    print ("     /:/  /   \:\/:/  /     \:\/:/  / ")
    time.sleep(0.1)
    print ("    /:/  /     \::/  /       \::/  /  ")
    time.sleep(0.1)
    print ("    \/__/       \/__/         \/__/   ")
    time.sleep(0.1)
    print ("                         ___      ")
    time.sleep(0.1)
    print ("          _____         /\__\       ")
    time.sleep(0.1)
    print ("         /::\  \       /:/ _/_    ")
    time.sleep(0.1)
    print ("        /:/\:\  \     /:/ /\__\   ")
    time.sleep(0.1)
    print ("       /:/  \:\__\   /:/ /:/ _/_  ")
    time.sleep(0.1)
    print ("      /:/__/ \:|__| /:/_/:/ /\__\ ")
    time.sleep(0.1)
    print ("      \:\  \ /:/  / \:\/:/ /:/  /")
    time.sleep(0.1)
    print ("       \:\  /:/  /   \::/_/:/  / ")
    time.sleep(0.1)
    print ("        \:\/:/  /     \:\/:/  /  ")
    time.sleep(0.1)
    print ("         \::/  /       \::/  /    ")
    time.sleep(0.1)
    print ("          \/__/         \/__/     ")
    time.sleep(0.1)
    print ("                             ")
    time.sleep(0.1)
    print ("                              ")
    time.sleep(0.1)
    print ("      ___                       ___             ")
    time.sleep(0.5)
    print ("     /\  \                     /\  \              ")
    time.sleep(0.1)
    print ("     \:\  \       ___         |::\  \               ")
    time.sleep(0.1)
    print ("      \:\  \     /\__\        |:|:\  \                ")
    time.sleep(0.1)
    print ("  _____\:\  \   /:/__/      __|:|\:\  \             ")
    time.sleep(0.1)
    print (" /::::::::\__\ /::\  \     /::::|_\:\__\              ")
    time.sleep(0.1)
    print (" \:\  \  \/__/ \/\:\  \__  \:\  \  \/__/          ")
    time.sleep(0.5)
    print ("  \:\  \          \:\/\__\  \:\  \                  ")
    time.sleep(0.1)
    print ("   \:\  \          \::/  /   \:\  \                ")
    time.sleep(0.5)
    print ("    \:\__\         /:/  /     \:\__\                 ")
    time.sleep(0.1)
    print ("     \/__/         \/__/       \/__/              ")
    time.sleep(0.5)
    print("\nBienvenue dans le Jeu de NIM\n")
    time.sleep(0.5)
    print("L'objectif est de forcer l adversaire a enlever la derniére pierre de la table\n")
    time.sleep(0.5)
    print("Chacun son tour, Vous pouvez enlevez le nombre que vous voulez d'un seul tas\n")
    time.sleep(0.5)
    print("Le jeu s'arete quand toutes les pierres sont enlevées!\n")
    time.sleep(0.5)
    print ("\n")
    time.sleep(0.1)
print_rules()

def main():
    # Definir une table(listPierres) vide, puis lui affecter des pierres, appeler la fonction "random" 
    listPierres = []
    randTas = random.randint(3, 7)
    randPierres = random.randint(5, 23)
    nom1, nom2 = nom_joueurs()

    joueur = nom1 # Fixer joueur a 1 (ça changera plus tard au cours du jeu)
    
    avoir_table(listPierres, randTas, randPierres, joueur) # Table initial

    jouer_encore(listPierres, randTas, randPierres, nom1, nom2, joueur) 

# Entrer et enregistrer le nom des 2 joueurs            
def nom_joueurs():
    return input("Entrer nom joueur1: "), input("Entrer nom joueur2: ")

# Accepter la table vide et le nom des joueurs
#Modifier la table, en ajoutant des tas et pierres aleatoirement par "random", puis afficher la table initiale 
def avoir_table(listPierres, randTas, randPierres, joueur):

    # Avoir table initiale
    print("Voici la table.")
    print("-" * 25)
    for i in range(0, randTas):
        randPierres = random.randint(5, 23)
        _e = 23 - randPierres
        print('Pile {}: {}'.format(i + 1, 'O' * randPierres, ' ' * _e),'(',randPierres,')')
        listPierres.append(randPierres)
    print("-" * 25)

    # la somme des pierres sur la table
    somme_nim(listPierres, randTas)

# retourne un message string quand inserer valeur invalide, met a jour la table pour le tour suivant
def avoir_valid_input(listPierres, randTas, joueur):

    # Commencer une boucle pour verifier si valeurs valides - si valid, break loop - sinon, continuer de demander
    while True:
        Tas = input('{}, Choisissez un tas: '.format(joueur))
        Pierres = input(' Combien de pierres a enlever depuis ce tas? ')

        # si toutes les conditions sont CORRECTES, break loop
        if (Pierres and Tas) and (Pierres.isdigit()) and (Pierres.isdigit()):
            if (int(Pierres) > 0) and (int(Tas) <= len(listPierres)) and (int(Tas) > 0):
                if (int(Pierres) <= listPierres[int(Tas) - 1]):
                    if (int(Pierres) != 0) and (int(Tas) != 0):
                        break
        
        # sinon, afficher ce message
        print("Hmmm. Vous avez entrer un valeur fausse. Essayez encore, {}.".format(joueur))
        
    # Mettre a jour
    listPierres[int(Tas) - 1] -= int(Pierres)

    # Continuer à jouer
    continuer_jeu(listPierres, randTas, joueur)

# accepter les changements apporté sur les pierres, tas et le nom des joueurs
# afficher nouvelles table mis a jour
def continuer_jeu(listPierres, randTas, joueur): 
    print("Regardons la table.")
    print("-" * 25)
    for i in range(0, randTas):
        print("Tas {}: {}".format(i + 1, 'O' * listPierres[i]),'(',listPierres[i],')')

    print("-" * 25)

    # somme des pierres sur la table
    if listPierres != [0] * len(listPierres):
        somme_nim(listPierres, randTas)


# accepter les changements apporté sur les pierres, tas et le nom des joueurs
# afficher le nom du perdant, et demande si il veulent jouer encore une fois
def jouer_encore(listPierres, randTas, randPierres, nom1, nom2, joueur):

    # Commencer la boucle pour changer de joueur ( le tour)
    while True:
        avoir_valid_input(listPierres, randTas, joueur)
        
        # Pour determiner le perdant, verifier si la liste des pierres est à 0 au tour de ce joueur
        if listPierres == [0] * len(listPierres):
            print("{} a perdu cette partie".format(joueur))
            util = input("Voulez vous jouer encore une fois? Entrez o pour oui, nimporte autre pour non: ")

            if util.lower() == 'o':
                # réinitialiser les données du jeu pour une nouvelle partie
                ListPierres = []
                randTas = random.randint(3, 7)
                nom1, nom2 = avoir_joueurs()
                joueur = nom1
                avoir_table(listPierres, randTas, randPierres, joueur)
                avoir_valid_input(listPierres, randTas, joueur)
                
            else:
                break
            
        # Tour des joueurs 2->1, 1->2 
        if joueur == nom1:
            joueur = nom2

        else:
            joueur = nom1
def somme_nim(listPierres, randTas):
    nim = 0

    # Calculer somme des pierres pour chaque liste des Pierres
    for i in listPierres:
        nim = nim ^ i
        

    
main()
