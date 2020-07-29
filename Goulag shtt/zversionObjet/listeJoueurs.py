# -*- coding: utf-8 -*-
"""
                           Projet Labyrinthe 
        Projet Python 2019-2020 de 1ere année et AS DUT Informatique Orléans
        
   Module listeJoueurs
   ~~~~~~~~~~~~~~~~~~~
   
   Ce module gère la liste des joueurs. 
"""
from random import sample
from joueur import *
from itertools import cycle

class listejoueurs(object):
    """
    créer un objet représentant les joueurs d'une partie
    """
    def __init__(self,nomsJoueurs):
        self._listeJ = list()
        #pos = sample(range(len(nomsJoueurs)),len(nomsJoueurs))            #permet de randomiser l'ordre des joueurs.....
        pos = range(len(nomsJoueurs))
        for cpt,j in zip(pos,nomsJoueurs):
            self._listeJ.append((cpt+1,cl_joueur(j)))
        self._listeJ = sorted(self._listeJ,key= lambda x:x[0])
        self._gener = cycle(range(len(nomsJoueurs)))
        self._cur = None

    def get_liste(self):
        """
        renvoie la liste des participants avec leur numéro
        """
        return self._listeJ

    def __str__(self):
        affiche = str()
        for (pos,joueur) in self.get_liste():
            affiche += "Numéro {0}: {1} \n".format(pos,joueur)
        return affiche

    def __add__(self,joueur):
        if len(self) == 0:
            pos_joueur = 1
        else:
            pos_joueur = max(self.get_liste(),key = lambda x:x[0])[0] +1
        self.get_liste().append((pos_joueur,cl_joueur(joueur)))
        self._gener = cycle(range(len(self.get_liste())))


    def __len__(self):
        return len(self._listeJ)

    def __getitem__(self,i):
        if i < len(self):
            return self.get_liste()[i]

    def __iter__(self):
        for (cpt,joueur) in self.get_liste():
            yield cpt,joueur

    def __next__(self):
        self._cur = self[next(self._gener)]
        return self._cur

    def getJoueurCourant(self):
        """
        renvoie le tuple du joueur courant avec son numéro
        """
        if self._cur is None:
            next(self)
        return self._cur

def ListeJoueurs(nomsJoueurs):
    """
    créer une liste de joueurs dont les noms sont dans la liste de noms passés en paramètre
    Attention il s'agit d'une liste de joueurs qui gère la notion de joueur courant
    paramètre: nomsJoueurs une liste de chaines de caractères
    résultat: la liste des joueurs avec un joueur courant mis à 0
    """
    return listejoueurs(nomsJoueurs)


def ajouterJoueur(joueurs, joueur):
    """
    ajoute un nouveau joueur à la fin de la liste
    paramètres: joueurs une liste de joueurs
                joueur le joueur à ajouter
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    joueurs + joueur

def initAleatoireJoueurCourant(joueurs):
    """
    tire au sort le joueur courant
    paramètre: joueurs un liste de joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    return None     #déjà effectué

def distribuerTresors(joueurs,nbTresors=24, nbTresorMax=0):
    """
    distribue de manière aléatoire des trésors entre les joueurs.
    paramètres: joueurs la liste des joueurs
                nbTresors le nombre total de trésors à distribuer (on rappelle 
                        que les trésors sont des entiers de 1 à nbTresors)
                nbTresorsMax un entier fixant le nombre maximum de trésor 
                             qu'un joueur aura après la distribution
                             si ce paramètre vaut 0 on distribue le maximum
                             de trésor possible  
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    nbTresors = int(nbTresors/len(joueurs))*len(joueurs) #assure l'équité de la distribution
    liste_distrib = sample(range(1,nbTresors+1),nbTresors) #assure son côté aléatoire
    for tresor,(_,joueur) in zip(liste_distrib,cycle(joueurs)):
        if nbTresorMax == 0 or len(joueur)< nbTresorMax:
            joueur + tresor

def changerJoueurCourant(joueurs):
    """
    passe au joueur suivant (change le joueur courant donc)
    paramètres: joueurs la liste des joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    next(joueurs)

def getNbJoueurs(joueurs):
    """
    retourne le nombre de joueurs participant à la partie
    paramètre: joueurs la liste des joueurs
    résultat: le nombre de joueurs de la partie
    """
    return len(joueurs)

def getJoueurCourant(joueurs):
    """
    retourne le joueur courant
    paramètre: joueurs la liste des joueurs
    résultat: le joueur courant
    """
    return joueurs.getJoueurCourant()[1]

def joueurCourantTrouveTresor(joueurs):
    """
    Met à jour le joueur courant lorsqu'il a trouvé un trésor
    c-à-d enlève le trésor de sa liste de trésors à trouver
    paramètre: joueurs la liste des joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    joueur = getJoueurCourant(joueurs)
    tresorTrouve(joueur)

def nbTresorsRestantsJoueur(joueurs,numJoueur):
    """
    retourne le nombre de trésors restant pour le joueur dont le numéro 
    est donné en paramètre
    paramètres: joueurs la liste des joueurs
                numJoueur le numéro du joueur
    résultat: le nombre de trésors que joueur numJoueur doit encore trouver
    """
    joueur = joueurs[numJoueur-1][1]
    return len(joueur)

def numJoueurCourant(joueurs):
    """
    retourne le numéro du joueur courant
    paramètre: joueurs la liste des joueurs
    résultat: le numéro du joueur courant
    """
    return joueurs.getJoueurCourant()[0]

def nomJoueurCourant(joueurs):
    """
    retourne le nom du joueur courant
    paramètre: joueurs la liste des joueurs
    résultat: le nom du joueur courant
    """
    return joueurs.getJoueurCourant()[1].get_nom()

def nomJoueur(joueurs,numJoueur):
    """
    retourne le nom du joueur dont le numero est donné en paramètre
    paramètres: joueurs la liste des joueurs
                numJoueur le numéro du joueur    
    résultat: le nom du joueur numJoueur
    """
    return joueurs[numJoueur-1][1].get_nom()

def prochainTresorJoueur(joueurs,numJoueur):
    """
    retourne le trésor courant du joueur dont le numero est donné en paramètre
    paramètres: joueurs la liste des joueurs
                numJoueur le numéro du joueur    
    résultat: le prochain trésor du joueur numJoueur (un entier)
    """
    joueur = joueurs[numJoueur-1][0]
    return prochainTresor(joueur)

def tresorCourant(joueurs):
    """
    retourne le trésor courant du joueur courant
    paramètre: joueurs la liste des joueurs 
    résultat: le prochain trésor du joueur courant (un entier)
    """
    joueur = getJoueurCourant(joueurs)
    return joueur.get_tresor_i()

def joueurCourantAFini(joueurs):
    """
    indique si le joueur courant a gagné
    paramètre: joueurs la liste des joueurs 
    résultat: un booleen indiquant si le joueur courant a fini
    """
    joueur = getJoueurCourant(joueurs)
    return True if len(joueur)==0 else False



if __name__ == "__main__":
    l1 = ListeJoueurs(["Batman","Robin"])
    print(l1)
    print(getNbJoueurs(l1))

    l1 + "Monsieur"
    distribuerTresors(l1,10)
    print (l1)
    # assert nbTresorsRestantsJoueur(l1,0) == 2
    # joueurCourantTrouveTresor(l1)
    # assert nbTresorsRestantsJoueur(l1,0) == 1
    # assert numJoueurCourant(l1) == 1
    # changerJoueurCourant(l1)
    # assert numJoueurCourant(l1) == 2
    # changerJoueurCourant(l1)
    # changerJoueurCourant(l1)
    # assert numJoueurCourant(l1) == 1
    # assert nomJoueur(l1,0) == l1[0][1].get_nom()


    

