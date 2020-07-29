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
class Matrice(object):
    """
    crée une matrice de nbLignes lignes sur nbColonnes colonnes en mettant 
    valeurParDefaut dans chacune des cases
    paramètres: 
      nbLignes un entier strictement positif qui indique le nombre de lignes
      nbColonnes un entier strictement positif qui indique le nombre de colonnes
      valeurParDefaut la valeur par défaut
    résultat la matrice ayant les bonnes propriétés
    """
    def __init__(self,nbLignes, nbColonnes, valeurParDefaut=0):
        self.nbLignes = nbLignes
        self.nbColonnes = nbColonnes
        self.tableau = [valeurParDefaut]*nbColonnes*nbLignes

    def exec_moi_rotation(self,card):
        dic = {'S' : self.decalageColonneEnHaut,'N':self.decalageColonneEnBas,'O':self.decalageLigneADroite,'E':self.decalageLigneAGauche}
        return dic[card]

    def getNbLignes(self):
        """
        retourne le nombre de lignes de la matrice
        paramètre: 
        """
        return self.nbLignes

    def getNbColonnes(self):
        """
        retourne le nombre de colonnes de la matrice
        paramètre: 
        """
        return self.nbColonnes

    def __getitem__(self,pos):
        """
        retourne la valeur qui se trouve en (ligne,colonne) dans la matrice
        paramètres: 
                   pos un tuple avec :
                     - ligne le numéro de la ligne (en commençant par 0)
                     - colonne le numéro de la colonne (en commençant par 0)
        """
        return self.tableau[pos[0]*self.getNbLignes() + pos[1]]

    def __setitem__(self,pos,value):
        """
        met la valeur dans la case se trouve en (ligne,colonne) de la matrice
        paramètres: 
                   pos un tuple avec :
                       -  ligne le numéro de la ligne (en commençant par 0)
                       - colonne le numéro de la colonne (en commençant par 0)
                    valeur la valeur à stocker dans la matrice
        cette fonction ne retourne rien mais modifie la matrice
        """
        self.tableau[pos[0]*self.nbLignes + pos[1]] = value

    def getVal(self,lig,col):
        '''
        retourne la valeur qui se trouve à la ligne lig colonne col de la matrice
        paramètres:
        resultat:        
        '''
        return self[(lig,col)]

    def setVal(self,lig,col,val):
        """
        met la valeur dans la case se trouve en (ligne,colonne) de la matrice
        paramètres: 
                   -  ligne le numéro de la ligne (en commençant par 0)
                   -  colonne le numéro de la colonne (en commençant par 0)
                    valeur la valeur à stocker dans la matrice
        cette fonction ne retourne rien mais modifie la matrice
        """
        self[(lig,col)] = val


    #------------------------------------------        
    # decalages
    #------------------------------------------

    def decalageLigneAGauche(self, numLig, nouvelleValeur):
        """
        permet de décaler une ligne vers la gauche en insérant une nouvelle
        valeur pour remplacer la premiere case à droite de cette ligne
        le fonction retourne la valeur qui a été éjectée
        paramèteres: 
                    - numLig le numéro de la ligne à décaler
                    - nouvelleValeur la valeur à placer
        résultat la valeur qui a été ejectée lors du décalage
        """
        res = self[(numLig,0)]

        new_matrice = Matrice(self.getNbLignes(),self.getNbColonnes())
        new_matrice.tableau = self.tableau.copy()

        self[numLig,self.nbLignes-1] = nouvelleValeur

        for j in range(0,self.getNbColonnes()-1):
            self[(numLig,j)] = new_matrice[(numLig,j+1)]

        return res
        
        


    def decalageLigneADroite(self,numLig,nouvelleValeur):
        """
        decale la ligne numLig d'une case vers la droite en insérant une nouvelle
        valeur pour remplacer la premiere case à gauche de cette ligne
        paramèteres: 
                    - numLig le numéro de la ligne à décaler
                    - nouvelleValeur la valeur à placer
        résultat: la valeur de la case "ejectée" par le décalage
        """
        res = self[(numLig,self.getNbLignes()-1)]

        new_matrice = Matrice(self.getNbLignes(),self.getNbColonnes())
        new_matrice.tableau = self.tableau.copy()
        self[numLig,0] = nouvelleValeur

        for j in range(1,self.getNbColonnes()):
            self[(numLig,j)] = new_matrice[(numLig,j-1)]

        return res
            

    def decalageColonneEnHaut(self, numCol, nouvelleValeur):
        """
        decale la colonne numCol d'une case vers le haut en insérant une nouvelle
        valeur pour remplacer la premiere case en bas de cette ligne
        paramèteres: 
                    - numCol le numéro de la colonne à décaler
                    - nouvelleValeur la valeur à placer
        résultat: la valeur de la case "ejectée" par le décalage
        """
        res = self[(0,numCol)]

        new_matrice = Matrice(self.getNbLignes(),self.getNbColonnes())
        new_matrice.tableau = self.tableau.copy()

        self[(self.getNbColonnes()-1,numCol)] = nouvelleValeur

        for i in range(0, self.getNbLignes()-1):
            self[(i,numCol)] = new_matrice[(i+1,numCol)]

        return res

    def decalageColonneEnBas(self, numCol, nouvelleValeur):
        """
        decale la colonne numCol d'une case vers le bas en insérant une nouvelle
        valeur pour remplacer la premiere case en haut de cette ligne
        paramèteres: 
                    - numCol le numéro de la colonne à décaler
                    - nouvelleValeur la valeur à placer
        résultat: la valeur de la case "ejectée" par le décalage
        """
        res = self[(self.getNbColonnes()-1,numCol)]

        new_matrice = Matrice(self.getNbLignes(),self.getNbColonnes())
        new_matrice.tableau = self.tableau.copy()
    
        self[(0,numCol)] = nouvelleValeur
        for i in range(1, self.getNbLignes()):
            self[(i,numCol)] = new_matrice[(i-1,numCol)]

        return res

if __name__ == '__main__':
    m = Matrice(7,7)