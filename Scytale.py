import os
import math
def lire_message(nom):
    """ Fonction qui permet de lire un message
    Elle prend en argument le nom du message : par exemple message1.txt et retourne son contenu"""
    mon_fichier = open(nom,"r",encoding="utf8")
    contenu = mon_fichier.read()
    mon_fichier.close()
    return contenu

def decryptage_scytale(cle,message):
    """ Fonction qui permet de décrypter le chiffrage spartiate de la scytale en connaissance la cle
    Elle prend 2 arguments : la clé de cryptage, et le message à decrypter
    Elle affiche le message une fois décodé"""
    contenu = lire_message(message)
    nbr_colonne = int(math.ceil(len(contenu) / float(cle))) # Le nombre de colonne est la longueur du message divisé par la clé
    nbr_ligne = cle # Le nombre de ligne correspond à la longueur de la clé
    num_empty = (nbr_colonne*nbr_ligne) - len(contenu)
    Message_au_clair = [''] * nbr_colonne # on clé un tableau de [""] fois le nombre de colonne
    colonne = 0 # On initialise les variables
    ligne = 0
    for car in contenu:
        Message_au_clair[colonne] += car
        colonne += 1
        if (colonne == nbr_colonne) or (colonne == nbr_colonne - 1 and ligne >= nbr_ligne - num_empty):
            colonne = 0
            ligne += 1    
    print(''.join(Message_au_clair) + "\n")
        
decryptage_scytale(3,"Message.txt")