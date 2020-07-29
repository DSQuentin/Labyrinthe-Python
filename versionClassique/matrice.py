# -*- coding: utf-8 -*-
"""
                           Projet Labyrinthe 
        Projet Python 2019-2020 de 1ere année et AS DUT Informatique Orléans
        
   Module matrice
   ~~~~~~~~~~~~~~~
   
   Ce module gère une matrice. 
"""

# -----------------------------------------
# contructeur et accesseurs pas API2
# -----------------------------------------


def Matrice(nbLignes, nbColonnes, valeurParDefaut=0):
    """
    crée une matrice de nbLignes lignes sur nbColonnes colonnes en mettant 
    valeurParDefaut dans chacune des cases
    paramètres: 
      nbLignes un entier strictement positif qui indique le nombre de lignes
      nbColonnes un entier strictement positif qui indique le nombre de colonnes
      valeurParDefaut la valeur par défaut
    résultat la matrice ayant les bonnes propriétés
    """
    return {"nbLignes": nbLignes,
            "nbColonnes": nbColonnes,
            "tableau": [valeurParDefaut]*nbLignes*nbColonnes
            }


def getNbLignes(matrice):
    """
    retourne le nombre de lignes de la matrice
    paramètre: matrice la matrice considérée
    """
    return matrice["nbLignes"]


def getNbColonnes(matrice):
    """
    retourne le nombre de colonnes de la matrice
    paramètre: matrice la matrice considérée
    """
    return matrice["nbColonnes"]


def getAll(matrice):
    """
    retourne toutes les valeurs de la matrice sous la forme d'une liste
    paramètre: matrice la matrice considérée
    """
    return matrice["tableau"]


def getVal(matrice, ligne, colonne):
    """
    retourne la valeur qui se trouve en (ligne,colonne) dans la matrice
    paramètres: matrice la matrice considérée
                ligne le numéro de la ligne (en commençant par 0)
                colonne le numéro de la colonne (en commençant par 0)
    """

    return matrice["tableau"][ligne * getNbLignes(matrice) + colonne]


def setVal(matrice, ligne, colonne, valeur):
    """
    met la valeur dans la case se trouve en (ligne,colonne) de la matrice
    paramètres: matrice la matrice considérée
                ligne le numéro de la ligne (en commençant par 0)
                colonne le numéro de la colonne (en commençant par 0)
                valeur la valeur à stocker dans la matrice
    cette fonction ne retourne rien mais modifie la matrice
    """
    matrice["tableau"][ligne * getNbLignes(matrice) + colonne] = valeur

# ------------------------------------------
# les decalages
# ------------------------------------------


def decalageLigneAGauche(matrice, numLig, nouvelleValeur=0):
    """
    permet de décaler une ligne vers la gauche en insérant une nouvelle
    valeur pour remplacer la premiere case à droite de cette ligne
    le fonction retourne la valeur qui a été éjectée
    paramèteres: matrice la matrice considérée
                 numLig le numéro de la ligne à décaler
                 nouvelleValeur la valeur à placer
    résultat la valeur qui a été ejectée lors du décalage
    """
    res = getVal(matrice, numLig, 0)

    new_matrice = {"nbLignes": getNbLignes(matrice), "nbColonnes": getNbColonnes(matrice),
                   "tableau": getAll(matrice).copy()}

    setVal(matrice, numLig, getNbLignes(matrice)-1, nouvelleValeur)

    for j in range(0, getNbColonnes(matrice)-1):
        setVal(matrice, numLig, j, getVal(new_matrice, numLig, j+1))

    return res


def decalageLigneADroite(matrice, numLig, nouvelleValeur=0):
    """
    decale la ligne numLig d'une case vers la droite en insérant une nouvelle
    valeur pour remplacer la premiere case à gauche de cette ligne
    paramèteres: matrice la matrice considérée
                 numLig le numéro de la ligne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """
    res = getVal(matrice, numLig, getNbLignes(matrice)-1)

    new_matrice = {"nbLignes": getNbLignes(matrice), "nbColonnes": getNbColonnes(matrice),
                   "tableau": getAll(matrice).copy()}

    setVal(matrice, numLig, 0, nouvelleValeur)

    for j in range(1, getNbColonnes(matrice)):
        setVal(matrice, numLig, j, getVal(new_matrice, numLig, j-1))

    return res


def decalageColonneEnHaut(matrice, numCol, nouvelleValeur=0):
    """
    decale la colonne numCol d'une case vers le haut en insérant une nouvelle
    valeur pour remplacer la premiere case en bas de cette ligne
    paramèteres: matrice la matrice considérée
                 numCol le numéro de la colonne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """
    res = getVal(matrice, 0, numCol)

    new_matrice = {"nbLignes": getNbLignes(matrice), "nbColonnes": getNbColonnes(matrice),
                   "tableau": getAll(matrice).copy()}

    setVal(matrice, getNbColonnes(matrice)-1, numCol, nouvelleValeur)

    for i in range(0, getNbLignes(matrice)-1):
        setVal(matrice, i, numCol, getVal(new_matrice, i+1, numCol))

    return res


def decalageColonneEnBas(matrice, numCol, nouvelleValeur=0):
    """
    decale la colonne numCol d'une case vers le bas en insérant une nouvelle
    valeur pour remplacer la premiere case en haut de cette ligne
    paramèteres: matrice la matrice considérée
                 numCol le numéro de la colonne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """
    res = getVal(matrice, getNbColonnes(matrice)-1, numCol)

    new_matrice = {"nbLignes": getNbLignes(matrice), "nbColonnes": getNbColonnes(matrice),
                   "tableau": getAll(matrice).copy()}

    setVal(matrice, 0, numCol, nouvelleValeur)

    for i in range(1, getNbLignes(matrice)):
        setVal(matrice, i, numCol, getVal(new_matrice, i-1, numCol))

    return res
