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

def decryptage_cesar():
    decalage=293
    mon_fichier = open("Message.txt","r",encoding="utf8")
    contenu = mon_fichier.read()
    decrypted = [''] * len(contenu)

    for i in contenu:
        Chiffre=ord(i)
        decalage_new_lettre = chr(int(Chiffre)-decalage)
        decrypted += decalage_new_lettre
    print(''.join(decrypted) + "\n")

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
decryptage_cesar_2()
