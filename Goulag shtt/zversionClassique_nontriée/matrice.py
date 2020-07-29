# -*- coding: utf-8 -*-
"""
                           Projet Labyrinthe 
        Projet Python 2019-2020 de 1ere année et AS DUT Informatique Orléans
        
   Module matrice
   ~~~~~~~~~~~~~~~
   
   Ce module gère une matrice. 
"""

#-----------------------------------------
# contructeur et accesseurs
#-----------------------------------------
'''
   -----------------------------------------
   Une deuxième implémentation des matrices 2D en python
   -----------------------------------------
'''

def Matrice(nbLignes,nbColonnes,valeurParDefaut=0):
    '''
    Crée une matrice de nbLignes lignes et nbColonnes colonnes
    contenant toute la valeur valeurParDefaut
    paramètres:
    résultat:
    '''
    listeValeurs=[valeurParDefaut]*nbLignes
    for i in range(nbLignes):
        listeValeurs[i] = [valeurParDefaut]*nbColonnes
    return listeValeurs

def getNbLignes(matrice):
    '''
    Permet de connaitre le nombre de lignes d'une matrice
    paramètre:
    resultat:
    '''
    return len(matrice)

def getNbColonnes(matrice):
    '''
    Permet de connaitre le nombre de colonnes d'une matrice
    paramètre:
    resultat:    
    '''
    if len(matrice)>0:
        return len(matrice[0])
    return None

def getVal(matrice,lig,col):
    '''
    retourne la valeur qui se trouve à la ligne lig colonne col de la matrice
    paramètres:
    resultat:        
    '''
    return matrice[lig][col]

def setVal(matrice,lig,col,val):
    '''
    place la valeur val à la ligne lig colonne col de la matrice
    paramètres:
    resultat: cette fonction ne retourne rien mais modifie la matrice
    '''
    matrice[lig][col] = val


#------------------------------------------        
# decalages
#------------------------------------------
def decalageLigneAGauche(matrice, numLig, nouvelleValeur):
    """
    permet de décaler une ligne vers la gauche en insérant une nouvelle
    valeur pour remplacer la premiere case à droite de cette ligne
    le fonction retourne la valeur qui a été éjectée
    paramèteres: matrice la matrice considérée
                 numLig le numéro de la ligne à décaler
                 nouvelleValeur la valeur à placer
    résultat la valeur qui a été ejectée lors du décalage
    """
    for j in range(getNbColonnes(matrice)-1):
        res=matrice[numLig][0]
        if j!=getNbColonnes(matrice)-1:
            setVal(matrice,numLig,j,matrice[numLig][j+1])
    setVal(matrice,numLig,j+1,nouvelleValeur)
    return res
    
    


def decalageLigneADroite(matrice,numLig,nouvelleValeur):
    """
    decale la ligne numLig d'une case vers la droite en insérant une nouvelle
    valeur pour remplacer la premiere case à gauche de cette ligne
    paramèteres: matrice la matrice considérée
                 numLig le numéro de la ligne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """
    for j in range(getNbColonnes(matrice)-1,0,-1):
        res=matrice[numLig][getNbColonnes(matrice)-1]
        setVal(matrice,numLig,j,matrice[numLig][j-1])
    setVal(matrice,numLig,0,nouvelleValeur)
    return res
        

def decalageColonneEnHaut(matrice, numCol, nouvelleValeur):
    """
    decale la colonne numCol d'une case vers le haut en insérant une nouvelle
    valeur pour remplacer la premiere case en bas de cette ligne
    paramèteres: matrice la matrice considérée
                 numCol le numéro de la colonne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """
    res=matrice[0][numCol]
    for i in range(getNbLignes(matrice)-1):
        setVal(matrice,i,numCol,matrice[i+1][numCol])
    setVal(matrice,getNbLignes(matrice)-1,numCol,nouvelleValeur)
    return res

def decalageColonneEnBas(matrice, numCol, nouvelleValeur):
    """
    decale la colonne numCol d'une case vers le bas en insérant une nouvelle
    valeur pour remplacer la premiere case en haut de cette ligne
    paramèteres: matrice la matrice considérée
                 numCol le numéro de la colonne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """
    res=matrice[getNbLignes(matrice)-1][numCol]
    for i in range(getNbLignes(matrice)-1,0,-1):
        setVal(matrice,i,numCol,matrice[i-1][numCol])
    setVal(matrice,0,numCol,nouvelleValeur)
    return res
 
