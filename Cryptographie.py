import os
import math

def decryptage_scytale():
    mon_fichier = open("Message.txt","r")
    contenu = mon_fichier.read()
    cle = 3
    num_col = int(math.ceil(len(contenu) / float(cle)))
    num_rows = cle
    num_empty = (num_col*num_rows) - len(contenu)
    decrypted = [''] * num_col
    col = 0
    row = 0
    for car in contenu:
        decrypted[col] += car
        col += 1
        if (col == num_col) or (col == num_col - 1 and row >= num_rows - num_empty):
            col = 0
            row += 1    

    print(''.join(decrypted) + "\n")

def decryptage_cesar(decalage,message):
    mon_fichier = open(message,"r",encoding="utf8")
    contenu = mon_fichier.read()
    decrypted = [''] * len(contenu)

    for i in contenu:
        Chiffre=ord(i)
        decalage_new_lettre = chr(int(Chiffre)-decalage)
        decrypted += decalage_new_lettre
    print(''.join(decrypted) + "\n")
decryptage_cesar(-83,"message3.txt")
import operator
def init_caract(texte):
    mon_dictionnaire = {}
    for lettre in texte:
        compteur = mon_dictionnaire.get(lettre,0)
        mon_dictionnaire[lettre] = compteur + 1
    valeur=0
    cle_f = ""
    return mon_dictionnaire,valeur,cle_f

def caractere_plus_frequent(texte,n):
    mon_dictionnaire,valeur,cle_f = init_caract(texte)
    for cle,valeur_lettre in mon_dictionnaire.items():
        if (valeur_lettre > valeur):
            valeur = valeur_lettre
            cle_f = cle
    dico_trie = sorted(mon_dictionnaire.items(), reverse=True, key=operator.itemgetter(1))
    return dico_trie[n][0] 

def deviner_cle_cesar(message):
    liste_possible=[]
    for i in range(1,5):
        analyse = caractere_plus_frequent(message,i)
        décalage_Maj = ord(analyse) - ord("E")
        décalage_Min = ord(analyse) - ord("e")
        liste_possible.append(décalage_Maj)
        liste_possible.append(décalage_Min)
        liste_possible.sort()
    #Lettre la plus présente : espace
    return liste_possible
    
"""mon_fichier = open("message3.txt","r",encoding="utf8")
contenu = mon_fichier.read()
print(deviner_cle_cesar(contenu))"""
def decryptage_cesar_2():
    decalage_1 = 23
    decalage_2 = 45
    mon_fichier = open("message4.txt","r",encoding="utf8")
    contenu = mon_fichier.read()
    decrypted = [''] * len(contenu)
    compteur = 0
    for i in contenu:
        Chiffre=ord(i)
        if compteur % 2 == 0:
            decalage_new_lettre = chr(int(Chiffre)-decalage_1)
        else:
            decalage_new_lettre = chr(int(Chiffre)-decalage_2)
        decrypted += decalage_new_lettre
        compteur = compteur+1
    print(''.join(decrypted) + "\n")

def PGCD (m,n) :
    if m <= 0 or n <= 0 : raise Exception("Pas possible de calculer le PGCD")
    if m == 1 or n == 1 : return 1
    if m == n : return m
    if m < n : return PGCD (m, n-m)
    return PGCD (n, m-n)


def code_vigenere(cle) :
    mon_fichier = open("message5.txt","r",encoding="utf8")
    contenu = mon_fichier.read()
    decrypted = [''] * len(contenu)
    compteur = 0
    for i in contenu:
        Chiffre_lettre=ord(i)
        decalage_new_lettre=chr(Chiffre_lettre - int(cle[compteur]))
        compteur+=1
        if (compteur == len(cle)):
            compteur=0
        decrypted += decalage_new_lettre
    print(''.join(decrypted) + "\n")
#code_vigenere([2,9,3])

def trouver_taille_cle():
    mon_fichier = open("message6.txt","r",encoding="utf8")
    contenu = mon_fichier.read()
    possibilite = []
    compteur = 0
    compteur_position = 0
    Total_rep = {}
    liste_tempo= ""
    distance = []
    for i in range(2,8):
        if ((len(contenu) % i) ==0):
            possibilite.append(i)

    for i in contenu:
        liste_tempo = liste_tempo + i
        compteur += 1
        compteur_position +=1
        if (compteur == possibilite[0]):
            compteur_2 = Total_rep.get(liste_tempo,0)

            if (compteur_2 != 0): 
                distance.append(compteur_position - compteur_2)
            else: 
                Total_rep[liste_tempo] = compteur_position-possibilite[0]
            liste_tempo= ""
            compteur = 0
    oui=0
    non=0
    dic_validation ={}
    for i in possibilite:
        print(i)
        for z in distance:
            if (z%i == 0):
                oui += 1
            else:
                non += 1
        dic_validation = dic_validation.get(possibilite,0)
        dic_validation[possibilite] = non
    return dic_validation

print(trouver_taille_cle())





    


    