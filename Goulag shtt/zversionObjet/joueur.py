# -*- coding: utf-8 -*-
"""
                           Projet Labyrinthe 
        Projet Python 2019-2020 de 1ere année et AS DUT Informatique Orléans
        
   Module joueur
   ~~~~~~~~~~~~~
   
   Ce module gère un joueur. 
"""
class cl_joueur(object):
    """
    créer un joueur avec une liste de trésors (vide par défaut)
    """
    def __init__(self,nom):
        self._nom = nom
        self._tresors = list()
        self._current_tresor = self._tresors[:1]  
    def __str__(self):
        return "Joueur {0} avec comme trésors : {1}".format(self.get_nom(),self.get_tresors())

    def get_tresors(self):
        """
        retourne le trésor d'un joueur sous la forme d'une liste
        """
        return self._tresors

    def get_nom(self):
        """
        revoie le nom d'un joueur
        """
        return self._nom

    def get_tresor_i(self,i=None):
        """
        renvoie le trésor d'un joueur à l'index i, par défaut c'est le trésor courant
        """
        if i is None:
            i = 0
        if i < len(self.get_tresors()):
            return self.get_tresors()[i]

    def __add__(self,tresor):
        self.get_tresors().append(tresor)
        return self.get_tresors()
    def __len__(self):
        return len(self.get_tresors())
        
    def __eq__(self,joueur):
        return self.get_tresors() == joueur.get_tresors()
        
    def __iter__(self):
        for tresor in self.get_tresors():
            yield tresor

    def next_tr(self):
        """
        passe le prochain trésor d'un joueur en trésor courant et le renvoie
        """
        tresor_actu = (tresor for tresor in self._tresors)   #generator
        self._current_tresor = next(tresor_actu,None)
        return self._current_tresor


    def __sub__(self,i):
        """
        retire le trésor d'un joueur à l'adresse i, par défaut à l'adresse 0
        """
        self.get_tresors().pop(i)

    


def Joueur(nom):
    """
    creer un nouveau joueur portant le nom passé en paramètre. Ce joueur possède une liste de trésors à trouver vide
    paramètre: nom une chaine de caractères
    retourne le joueur ainsi créé
    """
    return cl_joueur(nom)

def ajouterTresor(joueur,tresor):
    """
    ajoute un trésor à trouver à un joueur (ce trésor sera ajouter en fin de liste) Si le trésor est déjà dans la liste des trésors à trouver la fonction ne fait rien
    paramètres:
        joueur le joueur à modifier
        tresor un entier strictement positif
    la fonction ne retourne rien mais modifie le joueur
    """
    joueur + tresor

def prochainTresor(joueur):
    """
    retourne le prochain trésor à trouver d'un joueur, retourne None si aucun trésor n'est à trouver
    paramètre:
        joueur le joueur
    résultat un entier représentant le trésor ou None
    """
    return joueur.next_tr()




def tresorTrouve(joueur):
    """ 
    enlève le premier trésor à trouver car le joueur l'a trouvé
    paramètre:
        joueur le joueur
    la fonction ne retourne rien mais modifie le joueur
    """
    joueur - 0

def getNbTresorsRestants(joueur):
    """
    retourne le nombre de trésors qu'il reste à trouver
    paramètre: joueur le joueur
    résultat: le nombre de trésors attribués au joueur
    """
    return len(joueur)

def getNom(joueur):
    """
    retourne le nom du joueur
    paramètre: joueur le joueur
    résultat: le nom du joueur 
    """
    return joueur.get_nom()

