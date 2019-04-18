import os
import operator
def lire_message(nom):
    """ Fonction qui permet de lire un message
    Elle prend en argument le nom du message : par exemple message1.txt et retourne son contenu"""
    mon_fichier = open(nom,"r",encoding="utf8")
    contenu = mon_fichier.read()
    mon_fichier.close()
    return contenu

def caractere_plus_frequent(texte,n):
    """ Fonction qui permet de retourner le n-ième élements le plus présent dans un texte
    Elle prend 2 argurments : le CONTENU du message et le n-ième élements (0 sort le 1er , 1 le 2nd...)
    Elle retourne le n-ième élement le plus présent dans le texte
    Une protection a été rajouté pour éviter de selectionner un n trop grand"""
    mon_dictionnaire = {}

    for lettre in texte: # On parcourt le texte
        compteur = mon_dictionnaire.get(lettre,0)# Si l'element est présent dans la liste, on récupère sa valeur, sinon on suppose qu'elle vaut 0
        mon_dictionnaire[lettre] = compteur + 1 # On incrémente le nombre de fois ou elle est apparu dans la liste (0+1 = 1 si elle est nouvelle)

    dico_trie = sorted(mon_dictionnaire.items(), reverse=True, key=operator.itemgetter(1)) # On utilise la fonction sorted avec plusieurs arguments
    # pour trier le dictionnaire en ayant les caractères les plus présents qui se trouve en premier
    try:
        return dico_trie[n][0]  # On retourne le n-ième caractère le plus présent
    except:
        print("\n /!\ /!\ /!\ \n Il n'y a pas assez de caractère dans le texte, veuillez sélectionner une autre quantité \n /!\ /!\ /!\ \n")
        return
#caractere_plus_frequent(lire_message("message3.txt"),5000)
def decryptage_cesar(decalage,message):
    """ Fonction qui permet de décrypter le chiffre de césar (à 1 clé) en connaissant la cle
    Elle prend 2 arguments : la clé de cryptage, et le message à decrypter
    Elle retourne le message décodé"""
    contenu = lire_message(message)
    decrypted = ''
    try: # On essaye le décallage
        for lettre in contenu: 
            Chiffre=ord(lettre) # On récupère sa valeur
            decalage_new_lettre = chr(Chiffre-decalage) # On récupère la nouvelle lettre une fois décalé
            decrypted += decalage_new_lettre # On l'ajoute dans le tableau
    except: # Si il ne fonctionne pas, on arrete la fonction
        #print("Le decalage proposé ne fonctionne pas")
        return None
    return decrypted
#decryptage_cesar(293,"message3.txt")

#################################################################################################
#### Le décryptage de césar à 2 décalage représente à codage de vigenère de longueur de clé 2####
#################################################################################################

def decryptage_cesar_2(decalage_1,decalage_2,message):
    """ Fonction qui permet de décrypter le chiffre de césar (à 2 clé) en connaissance la cle
    Elle prend 2 arguments : la clé de cryptage, et le message à decrypter
    Elle affiche le message une fois décodé"""
    contenu = lire_message(message) 
    decrypted = ""
    compteur = 0
    for lettre in contenu:
        Chiffre=ord(lettre)
        if compteur % 2 == 0:
            decalage_new_lettre = chr(int(Chiffre)-decalage_1) # On récupère la nouvelle lettre avec le décallage_1
        else:
            decalage_new_lettre = chr(int(Chiffre)-decalage_2) # On récupère la nouvelle lettre avec le décallage_2
        decrypted += decalage_new_lettre
        compteur += 1
    print(decrypted + "\n")
#decryptage_cesar_2(23,45,"message4.txt")

def deviner_cle_cesar(message):
    """ Fonction qui permet grâce à l'analyse frequentielle de deviner les 4 clés les plus probables du chiffre de césar
    Elle prend en argument le nom du message et retourne une liste de possibilité"""
    contenu = lire_message(message)
    liste_possible=[] # On initialise la liste de clé possible
    fonctionnel = [] # On initialise la liste de clé FONCTIONNEL
    for i in range(1,3):
        analyse = caractere_plus_frequent(contenu,i) # On récupère les 3 caractères les plus fréquents (pour s'assurer d'être fiable) 
        a = ord(analyse) - ord(" ")
        b = ord(analyse) - ord("e")
        liste_possible.append(a)   #Lettre la plus présente : espace et e
        liste_possible.append(b)
        liste_possible.sort()
    for possible in liste_possible: # On vérifie grâce à cette boucle laquelle(lesquelles) de ces clés est (sont) possible(s)
        if ((decryptage_cesar(possible,message)) != None) : # Si la fonction décryptage césar fonctionne sans recontrer de probleme
            fonctionnel.append(possible) # On ajoute la clé au tableau des clé fonctionnelles
    return fonctionnel # On retourne le nombre de clé fonctionnel

########## INTERFACE UTILISATEUR ##########

def interface_utilisateur(message):
    """ Fonction qui permet l'interface avec l'utilisateur
    Elle prend en argument le nom du message, par exemple message.txt
    Elle décrypte le message, et donne les différentes clés et décryptage possible"""

    print("\n ########## Bienvenue dans le décodeur du code césar ########## \n")
    cle = deviner_cle_cesar(message) # Permet de donner l'éventualité des clés
    for key in cle:
        print(decryptage_cesar(key,message))
    print("La/les clé(s) possible(s) est(sont) :",cle)

interface_utilisateur("message3.txt")
############################################