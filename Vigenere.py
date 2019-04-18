import os
import operator
def lire_message(nom):
    """ Fonction qui permet de lire un message
    Elle prend en argument le nom du message : par exemple message1.txt et retourne son contenu"""
    mon_fichier = open(nom,"r",encoding="utf8")
    contenu = mon_fichier.read()
    mon_fichier.close()
    return contenu

def code_vigenere(cle,message) :
    """ Fonction qui permet de décoder le code de vigenère en connaissant la clé
    Elle prend en argument la clé sous forme de tableau et le nom du fichier (message.txt par exemple), et retourne le message décodé"""
    contenu = lire_message(message)
    decrypted = ""
    compteur = 0
    try:
        for i in contenu:
            Chiffre_lettre=ord(i)
            decalage_new_lettre=chr(Chiffre_lettre - int(cle[compteur]))
            compteur+=1
            if (compteur == len(cle)): # Tant que le compteur n'est pas égale à la clé, on ne remet pas a 0 le compteur
                compteur=0
            decrypted += decalage_new_lettre
    except:
        return None
    return decrypted
#code_vigenere([2,9,3])
#rint(code_vigenere([7,2,9,3,1,3,5,11,10,4,3],"message6.txt"))

def pgcd(a,b):
    """ Fonction du plus grand diviseur commun entre 2 arguments"""
    if b==0:
        return a
    else:
        r=a%b
        return pgcd(b,r)

def Longueur_cle_vigenere(message,precision):
    """ Fonction qui permet de déterminer la longueur de la clé de vigenère en utilisant la distance entre chaque élement et le PGCD
    Elle prend en argument le nom du fichier et la précision : il s'agit de retourner les n possibilité de longueur de clé """
    contenu = lire_message(message)
    dico = {}
    for i in range (0, len(contenu)-2) :
        t = contenu [i:i+2] #On découpe les mots 2 par deux
        if t in dico : 
            dico [t].append(i) # Si la séquence est déjà dans le dictionnaire, on rajoute la position
        else : 
            dico [t] = [i] #Sinon on la créer
    distance = {}
    for cle,valeur in dico.items():
        premiere_fois = 1
        for element in valeur:
            if (premiere_fois == 1): #Si c'est le premier caractère de l'ensemble (par exemple 1,500,1000)
                tmp = element # on l'inclut dans tmp (temporaire)
                premiere_fois = 0
            if (tmp != element): # On verifie qu'il n'est pas identique à celui de départ (on commence alors obligatoirement par comparer le 1 et le 2nd)
                a = pgcd(tmp,element) # On détermine le pgcd entre les deux élements
                if a not in distance :  # Si la distance n'existe pas encore, alors on la créer
                    distance[a] = 1
                else: #sinon, on récupère sa valeur et on l'incrémente
                    compteur = distance.get(a)
                    distance[a] = compteur+1
    dico_trie = sorted(distance.items(), reverse=True, key=operator.itemgetter(1)) # On trie dans le sens décroissant
    selection =[]
    for i in range(0,precision):
        selection.append(dico_trie[i] [0])
    return selection
#print(Longueur_cle_vigenere("message6.txt",5))

def Determine_cle_vigenere(message,longueur):
    """ Fonction qui permet de déterminer les différentes clé de vigenere, 
    elle prend en argument la longueur de la clé, et nom du fichier
    elle renvoit différentes possibilités de clé"""
    contenu = lire_message(message)
    compteur=0
    dico=[{}for i in range(longueur)] #On créer une liste de n dictionnaire (avec n la longueur de la clé)

    ### Dans la partie suivante, on va faire une analyse de fréquence sur CHACUN des éléments en faisant intervernir la longueur de la clé
    ### exemple sur un vigenere de longueur 3, texte = abcdefabc , en faisant l'analyse de fréquence, 
    # on obtient le dictionnaire {{"a" : 2,"d":1},{"b":2,"e":2},{"c":2,"f":1}}
    # On supposera dans la suite, que l'élément le plus présent dans chacun des dictionnaires est soit un "e" soit un espace
    # On pourra déterminer de cette façon la clé de vigenère car l'analyse fréquentielle est fiable sur de grand texte
    for i in range(len(contenu)):
        if contenu[i] in dico[compteur]: # Si on a déjà le caractère dans le dictionnaire
            incrementation = dico[compteur].get(contenu[i]) # on récupère sa valeur
            dico[compteur][contenu[i]] = incrementation +1 # et on l'incrémente de 1
        else:
            dico[compteur][contenu[i]] = 1 # Sinon, on créer le caractère dans le dictionnaire
        compteur=compteur+1 
        if (compteur == longueur): # Si le compteur atteint la longueur, alors on remet à 0
            compteur=0
    lettre_plus_frequente =[]
    decalage_1 = [] # On créer une première liste pour le décalage avec l'espace
    for n in range(longueur):
        dico_trie = sorted(dico[n].items(), reverse=True, key=operator.itemgetter(1)) # Permet de sortir le n-ième dictionnaire sous forme de liste
        lettre_plus_frequente.append(dico_trie[0])
        decalage_1.append(ord(lettre_plus_frequente[n][0]) - ord(" "))
    return decalage_1
#Determine_cle_vigenere("message6.txt",11)
#Determine_cle_vigenere("message4.txt",2)

########## INTERFACE UTILISATEUR ##########

def interface_utilisateur(message):
    """ Fonction qui permet l'interface avec l'utilisateur
    Elle prend en argument le nom du message, par exemple message.txt
    Elle décrypte le message, et donne les différentes clés et décryptage possible"""
    print("\n###########################################################################")
    print("########## Bienvenue dans le décodeur du code de vigenère #################")
    print("###########################################################################\n")
    precision = int(input("Quelle précision voulez vous pour le décodage ? (5 est suffisant dans 99% des cas) :"))
    liste_longueur = Longueur_cle_vigenere(message,precision)
    for longueur in liste_longueur:
        a = Determine_cle_vigenere(message,longueur)
        if (code_vigenere(a,message) != None):
            print(code_vigenere(a,message))
            print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
            print("\nDécryptage obtenu pour une longueur de :",longueur,"et une clé de",a)
            print("\n")
interface_utilisateur("message6.txt")
############################################