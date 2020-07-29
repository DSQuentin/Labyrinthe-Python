# -*- coding: utf-8 -*-
"""
                           Projet Labyrinthe 
        Projet Python 2019-2020 de 1ere année et AS DUT Informatique Orléans
        
   Module matrice
   ~~~~~~~~~~~~~~~
   
   Ce module gère une matrice. 
"""

#-----------------------------------------
# contructeur et accesseurs (API2)
#-----------------------------------------

def Matrice(nbLignes,nbColonnes,valeurParDefaut=0):
    """
    crée une matrice de nbLignes lignes sur nbColonnes colonnes en mettant 
    valeurParDefaut dans chacune des cases
    paramètres: 
      nbLignes un entier strictement positif qui indique le nombre de lignes
      nbColonnes un entier strictement positif qui indique le nombre de colonnes
      valeurParDefaut la valeur par défaut
    résultat la matrice ayant les bonnes propriétés
    """
    # return (nbLignes, nbColonnes, [valeurParDefaut]*nbLignes*nbColonnes )
    return {"nbLignes": nbLignes,
    		"nbColonnes": nbColonnes,
    		"values": [valeurParDefaut]*nbLignes*nbColonnes
    		}

def getNbLignes(matrice):
    """
    retourne le nombre de lignes de la matrice
    paramètre: matrice la matrice considérée
    """
    # return matrice[0]
    return matrice["nbLignes"]

def getNbColonnes(matrice):
    """
    retourne le nombre de colonnes de la matrice
    paramètre: matrice la matrice considérée
    """
    # return matrice[1]
    return matrice["nbColonnes"]

def getAllValues(matrice):
	"""
	retourne toutes les valeurs de la matrice sous la forme d'une liste
	paramètre: matrice la matrice considérée
	"""
	# return matrice[2]
	return matrice["values"]

def getVal(matrice,ligne,colonne):
    """
    retourne la valeur qui se trouve en (ligne,colonne) dans la matrice
    paramètres: matrice la matrice considérée
                ligne le numéro de la ligne (en commençant par 0)
                colonne le numéro de la colonne (en commençant par 0)
    """
    # i = ligne * matrice[1] + colonne
    # return matrice[2][i]
    return matrice["values"][ligne * getNbLignes(matrice) + colonne]

def setVal(matrice,ligne,colonne,valeur):
    """
    met la valeur dans la case se trouve en (ligne,colonne) de la matrice
    paramètres: matrice la matrice considérée
                ligne le numéro de la ligne (en commençant par 0)
                colonne le numéro de la colonne (en commençant par 0)
                valeur la valeur à stocker dans la matrice
    cette fonction ne retourne rien mais modifie la matrice
    """
    # i = ligne * matrice[1] + colonne
    # matrice[2][i] = valeur
    i = ligne * getNbLignes(matrice) + colonne
    matrice["values"][i] = valeur

#------------------------------------------        
# decalages
#------------------------------------------
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
    valEject = getVal(matrice, numLig, 0)

    # nouvelleMatrice = (getNbLignes(matrice), getNbColonnes(matrice), getAllValues(matrice).copy())
    copieMatrice = {"nbLignes": getNbLignes(matrice),
    				"nbColonnes": getNbColonnes(matrice),
    				"values": getAllValues(matrice).copy()}
    # print(matrice)

    setVal( matrice, numLig, getNbLignes(matrice)-1, nouvelleValeur)

    for i in range(0, getNbColonnes(matrice)-1):
    	setVal( matrice, numLig, i, getVal(copieMatrice, numLig, i+1))
    	# afficheMatrice(copieMatrice)
    	# afficheMatrice(matrice)
    	# afficheMatrice('*'*20)

    return valEject

def decalageLigneADroite(matrice, numLig, nouvelleValeur=0):
    """
    decale la ligne numLig d'une case vers la droite en insérant une nouvelle
    valeur pour remplacer la premiere case à gauche de cette ligne
    paramèteres: matrice la matrice considérée
                 numLig le numéro de la ligne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """
    valEject = getVal(matrice, numLig, getNbLignes(matrice)-1)

    # nouvelleMatrice = (getNbLignes(matrice), getNbColonnes(matrice), getAllValues(matrice).copy())
    copieMatrice = {"nbLignes": getNbLignes(matrice),
    				"nbColonnes": getNbColonnes(matrice),
    				"values": getAllValues(matrice).copy()}
    # print(matrice)

    setVal(matrice, numLig, 0, nouvelleValeur)

    for i in range(1,getNbColonnes(matrice)):
    	setVal( matrice, numLig, i, getVal(copieMatrice, numLig, i-1))
    	# afficheMatrice(copieMatrice)
    	# afficheMatrice(matrice)
    	# print('*'*20)

    return valEject

def decalageColonneEnHaut(matrice, numCol, nouvelleValeur=0):
    """
    decale la colonne numCol d'une case vers le haut en insérant une nouvelle
    valeur pour remplacer la premiere case en bas de cette ligne
    paramèteres: matrice la matrice considérée
                 numCol le numéro de la colonne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """
    valEject = getVal(matrice, 0, numCol)

    # nouvelleMatrice = (getNbLignes(matrice), getNbColonnes(matrice), getAllValues(matrice).copy())
    copieMatrice = {"nbLignes": getNbLignes(matrice),
    				"nbColonnes": getNbColonnes(matrice),
    				"values": getAllValues(matrice).copy()}
    # print(matrice)

    setVal( matrice, getNbColonnes(matrice)-1, numCol, nouvelleValeur)

    for i in range(0, getNbLignes(matrice)-1):
    	setVal( matrice, i, numCol, getVal(copieMatrice, i+1, numCol))
    	# afficheMatrice(copieMatrice)
    	# afficheMatrice(matrice)
    	# print('*'*20)

    return valEject

def decalageColonneEnBas(matrice, numCol, nouvelleValeur=0):
    """
    decale la colonne numCol d'une case vers le bas en insérant une nouvelle
    valeur pour remplacer la premiere case en haut de cette ligne
    paramèteres: matrice la matrice considérée
                 numCol le numéro de la colonne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """
    valEject = getVal(matrice, getNbColonnes(matrice)-1, numCol)

    # nouvelleMatrice = (getNbLignes(matrice), getNbColonnes(matrice), getAllValues(matrice).copy())
    copieMatrice = {"nbLignes": getNbLignes(matrice),
    				"nbColonnes": getNbColonnes(matrice),
    				"values": getAllValues(matrice).copy()}

    setVal(matrice, 0, numCol, nouvelleValeur)

    for i in range(1, getNbLignes(matrice)):
    	setVal( matrice, i, numCol, getVal(copieMatrice, i-1, numCol))
    	# afficheMatrice(copieMatrice)
    	# afficheMatrice(matrice)
    	# print('*'*20)

    return valEject

#------------------------------------------        
# asserts
#------------------------------------------

if __name__=='__main__':
	m1 = Matrice(7, 7)
	for numLig in range(7):
		for numCol in range(7):
			setVal(m1, numLig, numCol, (numLig,numCol) )

	# afficheMatrice(m1)
	assert(getVal(m1, 4, 6))==(4,6)
	assert(getVal(m1, getNbLignes(m1)-1, getNbColonnes(m1)-1))==(6,6)

	afficheMatrice(m1)

	print("### VERS LA DROITE ###")
	assert(decalageLigneADroite(m1, 4, 'D'))==(4,6)
	afficheMatrice(m1,8)

	print("### VERS LA GAUCHE ###")
	assert(decalageLigneAGauche(m1, 1, 'G'))==(1,0)
	afficheMatrice(m1,8)

	print("### VERS LE BAS ###")
	assert(decalageColonneEnBas(m1, 6, 'B'))==(6,6)
	afficheMatrice(m1,8)

	print("### VERS LE HAUT ###")
	assert(decalageColonneEnHaut(m1, 5, 'H'))==(0,5)
	afficheMatrice(m1,8)

