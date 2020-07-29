# -*- coding: utf-8 -*-
"""
                           Projet Labyrinthe 
        Projet Python 2019-2020 de 1ere année et AS DUT Informatique Orléans
        
   Module joueur
   ~~~~~~~~~~~~~
   
   Ce module gère un joueur. 
"""
from random import sample


class Joueur(object):
    """
    créer un joueur avec une liste de trésors (vide par défaut)
    """

    def __init__(self, nom):
        self._nom = nom
        self._tresors = [].copy()
        self._current_tresor = self._tresors[:1]

    def __str__(self):
        """
        pour l'affichage du joueur
        """
        return "Joueur '{0}' avec comme trésors : {1}".format(self.getNom(), self.get_tresors())

    def get_tresors(self):
        """
        retourne le trésor d'un joueur sous la forme d'un ensemble
        """
        return self._tresors

    def __invert__(self):
        """
        le ~self retourne le trésor courant
        """
        return self.prochainTresor()

    def getNom(self):
        """
        retourne le nom du joueur
        paramètre: joueur le joueur
        résultat: le nom du joueur 
        """
        return self._nom

    def __add__(self, tresor):
        """
        ajoute un trésor au joueur
        """
        if tresor not in self.get_tresors():
            self.get_tresors().append(tresor)

    def __sub__(self, i):
        """
        retire le trésor au joueur
        """
        self.get_tresors().pop(i)

    def __len__(self):
        """
        retourne le nombre de trésors restants
        """
        return len(self.get_tresors())

    def __eq__(self, joueur):
        """
        deux joueurs sont égaux seulement si ils ont les mêmes trésors
        """
        return self.get_tresors() == joueur.get_tresors()

    def __iter__(self):
        """
        renvoie tous les trésors tous joueurs un à un
        """
        for tresor in self.get_tresors():
            yield tresor

    def ajouterTresor(self, tresor):
        """
        ajoute un trésor à trouver à un joueur (ce trésor sera ajouter en fin de liste) Si le trésor est déjà dans la liste des trésors à trouver la fonction ne fait rien
        paramètres:
            joueur le joueur à modifier
            tresor un entier strictement positif
        la fonction ne retourne rien mais modifie le joueur
        """
        self + tresor

    def prochainTresor(self):
        """
        retourne le prochain trésor à trouver d'un joueur, retourne None si aucun trésor n'est à trouver
        paramètre:
            joueur le joueur
        résultat un entier représentant le trésor ou None
        """
        tresor_actu = (tresor for tresor in self._tresors)  # generator
        self._current_tresor = next(tresor_actu, None)
        return self._current_tresor

    def tresorTrouve(self):
        """ 
        enlève le premier trésor à trouver car le joueur l'a trouvé
        paramètre:
            joueur le joueur
        la fonction ne retourne rien mais modifie le joueur
        """
        self - 0

    def getNbTresorsRestants(self):
        """
        retourne le nombre de trésors qu'il reste à trouver
        paramètre: joueur le joueur 
        résultat: le nombre de trésors attribués au joueur
        """
        return len(self)


if __name__ == '__main__':
    j = Joueur('david')
    print(j)
    print(~j)
