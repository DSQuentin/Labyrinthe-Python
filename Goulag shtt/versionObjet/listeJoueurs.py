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


class ListeJoueurs(object):
    """
    créer un objet représentant les joueurs d'une partie
    """
    def __init__(self,nomsJoueurs):
        self._listeJ = list()
        #pos = sample(range(len(nomsJoueurs)),len(nomsJoueurs))            #permet de randomiser l'ordre des joueurs.....
        for cpt,j in enumerate(nomsJoueurs):
            self._listeJ.append((cpt+1,Joueur(j)))
        #self._listeJ = sorted(self._listeJ,key= lambda x:x[0])             #pour randomiser l'ordre des joueurs toujours 
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
        """
        ajoute le joueur à la liste de joueur
        """
        if len(self) == 0:
            pos_joueur = 1
        else:
            pos_joueur = max(self.get_liste(),key = lambda x:x[0])[0] +1
        self.get_liste().append((pos_joueur,Joueur(joueur)))   #comme on a une joueur de plus
        self._gener = cycle(range(len(self.get_liste())))


    def __len__(self):
        """
        retourne le nombre de joueurs
        """
        return len(self._listeJ)

    def __getitem__(self,i):
        """
        renvoie le joueur avec le numéro i
        """
        if i < len(self):
            return self.get_liste()[i]
        else:
            raise ValueError("Ceci n'est pas dans la liste de joueurs")

    def __iter__(self):
        """
        retourne nbJoueurs fois (cpt,joueur)
        """
        for (cpt,joueur) in self._listeJ:
            yield cpt,joueur

    def __next__(self):
        """
        passe au joueur suivant
        """
        self._cur = self[next(self._gener)]
        return self._cur

    def getJoueurNumCourant(self):
        """
        renvoie le tuple du joueur courant avec son numéro
        """
        if self._cur is None:
            next(self)
        return self._cur


    def ajouterJoueur(self, joueur):
        """
        ajoute un nouveau joueur à la fin de la liste
        paramètres: joueurs une liste de joueurs
                    joueur le joueur à ajouter
        cette fonction ne retourne rien mais modifie la liste des joueurs
        """
        self + joueur

    def initAleatoireJoueurCourant(joueurs):
        """
        tire au sort le joueur courant
        paramètre: joueurs un liste de joueurs
        cette fonction ne retourne rien mais modifie la liste des joueurs
        """
        return None     #déjà effectué

    def distribuerTresors(self,nbTresors=24, nbTresorMax=0):
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
        nbTresors = int(nbTresors/len(self))*len(self) #assure l'équité de la distribution
        liste_distrib = sample(range(1,nbTresors+1),nbTresors) #assure son côté aléatoire
        for tresor,(_,joueur) in zip(liste_distrib,cycle(self)):
            if nbTresorMax == 0 or len(joueur)< nbTresorMax:
                joueur + tresor

    def changerJoueurCourant(self):
        """
        passe au joueur suivant (change le joueur courant donc)
        paramètres: joueurs la liste des joueurs
        cette fonction ne retourne rien mais modifie la liste des joueurs
        """
        next(self)

    def getNbJoueurs(self):
        """
        retourne le nombre de joueurs participant à la partie
        paramètre: joueurs la liste des joueurs
        résultat: le nombre de joueurs de la partie
        """
        return len(self)

    def getJoueurCourant(self):
        """
        retourne le joueur courant
        paramètre: joueurs la liste des joueurs
        résultat: le joueur courant
        """
        return self.getJoueurNumCourant()[1]

    def joueurCourantTrouveTresor(self):
        """
        Met à jour le joueur courant lorsqu'il a trouvé un trésor
        c-à-d enlève le trésor de sa liste de trésors à trouver
        paramètre: joueurs la liste des joueurs
        cette fonction ne retourne rien mais modifie la liste des joueurs
        """
        joueur = self.getJoueurCourant()
        joueur.tresorTrouve()

    def nbTresorsRestantsJoueur(self,numJoueur):
        """
        retourne le nombre de trésors restant pour le joueur dont le numéro 
        est donné en paramètre
        paramètres: joueurs la liste des joueurs
                    numJoueur le numéro du joueur
        résultat: le nombre de trésors que joueur numJoueur doit encore trouver
        """
        joueur = self[numJoueur-1][1]
        return joueur.getNbTresorsRestants()

    def numJoueurCourant(self):
        """
        retourne le numéro du joueur courant
        paramètre: joueurs la liste des joueurs
        résultat: le numéro du joueur courant
        """
        return self.getJoueurNumCourant()[0]

    def nomJoueurCourant(self):
        """
        retourne le nom du joueur courant
        paramètre: joueurs la liste des joueurs
        résultat: le nom du joueur courant
        """
        return self.getJoueurCourant().getNom()

    def nomJoueur(self,numJoueur):
        """
        retourne le nom du joueur dont le numero est donné en paramètre
        paramètres: joueurs la liste des joueurs
                    numJoueur le numéro du joueur    
        résultat: le nom du joueur numJoueur
        """
        return self[numJoueur-1][1].getNom()

    def prochainTresorJoueur(self,numJoueur):
        """
        retourne le trésor courant du joueur dont le numero est donné en paramètre
        paramètres: joueurs la liste des joueurs
                    numJoueur le numéro du joueur    
        résultat: le prochain trésor du joueur numJoueur (un entier)
        """
        joueur = joueurs[numJoueur-1][0]
        return prochainTresor(joueur)

    def tresorCourant(self):
        """
        retourne le trésor courant du joueur courant
        paramètre: joueurs la liste des joueurs 
        résultat: le prochain trésor du joueur courant (un entier)
        """
        joueur = self.getJoueurCourant()
        return ~joueur

    def joueurCourantAFini(self):
        """
        indique si le joueur courant a gagné
        paramètre: joueurs la liste des joueurs 
        résultat: un booleen indiquant si le joueur courant a fini
        """
        joueur = self.getJoueurCourant()
        return False if len(joueur) else True



if __name__ == "__main__":
    #hello
    l = ListeJoueurs(['j1','j2'])
    print(l.tresorCourant())

    

