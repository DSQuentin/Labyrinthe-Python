# -*- coding: utf-8 -*-
"""
                           Projet Labyrinthe 
        Projet Python 2019-2020 de 1ere année et AS DUT Informatique Orléans
        
   Module labyrinthe
   ~~~~~~~~~~~~~~~~~
   
   Ce module gère sur le jeu du labyrinthe (observation et mise à jour du jeu).
"""

from listeJoueurs import *
from plateau import *


class Labyrinthe(object):
    """
    permet de créer un labyrinthe avec nbJoueurs joueurs, nbTresors trésors
    chacun des joueurs aura au plus nbTresorMax à trouver
    si ce dernier paramètre est à 0, on distribuera le maximum de trésors possible 
    à chaque joueur en restant équitable
    un joueur courant est choisi et la phase est initialisée
    paramètres: nomsJoueurs est la liste des noms des joueurs participant à la partie (entre 1 et 4)
                nbTresors le nombre de trésors différents il en faut au moins 12 et au plus 49
                nbTresorMax le nombre de trésors maximum distribué à chaque joueur
    résultat: le labyrinthe crée
    """
    def __init__(self,nomsJoueurs=["joueur1","joueurs2"],nbTresors=24,nbTresorsMax=0):
        self.laby = dict()
        self.laby['J'] = ListeJoueurs(nomsJoueurs)
        self.laby['P'] = Plateau(len(nomsJoueurs),nbTresors)
        self.laby['J'].distribuerTresors(nbTresors,nbTresorsMax)
        self.laby['G'] = (cycle(p for p in range(1,3)))
        self.laby['Ph'] = next(self['G'])
        self.laby['Pl'] = self['J'].getJoueurCourant()
        self.laby['C'] = (None,None) #coup précédent

    def __getitem__(self,item):
        """
        renvoie l'item du dictionnaire qui est demandé
        """
        if item in self.laby:
            return self.laby[item]
        else:
            raise ValueError("Valeur inconnue ou non accessible")
    def __setitem__(self,key,value):
        """
        fonctionne comme les dictionnaires (comme on en manipule un)
        """
        self.laby[key] = value

    def __next__(self):
        """
        passe à la phase suivante et peut-être au joueur suivant
        """
        self['Ph'] = next(self['G'])
        if self['Ph'] == 1:
            self['J'].changerJoueurCourant()
            self['Pl'] =  self['J'].getJoueurCourant()


    def __str__(self):
        """
        donne une représentation du labyrinthes ainsi que des joueurs
        """
        return "{0} {1} \n".format(self['J'],self['P'])
    def getPlateau(self):
        """
        retourne la matrice représentant le plateau de jeu
        paramètre: labyrinthe le labyrinthe considéré
        résultat: la matrice représentant le plateau de ce labyrinthe
        """
        return self['P'][0]

    def getJoueurCourant(self):
        """
        renvoie le joueur courant
        """
        return self['Pl']


    def getNbParticipants(self):
        """
        retourne le nombre de joueurs engagés dans la partie
        paramètre: labyrinthe le labyrinthe considéré
        résultat: le nombre de joueurs de la partie
        """
        return self['P'].get_nb_joueurs()

    def getNomJoueurCourant(self):
        """
        retourne le nom du joueur courant
        paramètre: labyrinthe le labyrinthe considéré
        résultat: le nom du joueurs courant
        """
        return self['Pl'].getNom()

    def getNumJoueurCourant(self):
        """
        retourne le numero du joueur courant
        paramètre: labyrinthe le labyrinthe considéré
        résultat: le numero du joueurs courant
        """
        return self['J'].numJoueurCourant()

    def getPhase(self):
        """
        retourne la phase du jeu courante
        paramètre: labyrinthe le labyrinthe considéré
        résultat: le numéro de la phase de jeu courante
        """   
        return self['Ph']


    def changerPhase(self):
        """
        change de phase de jeu en passant la suivante
        paramètre: labyrinthe le labyrinthe considéré
        la fonction ne retourne rien mais modifie le labyrinthe
        """    
        next(self)

    def getNbTresors(self):
        """
        retourne le nombre de trésors qu'il reste sur le labyrinthe
        paramètre: labyrinthe le labyrinthe considéré
        résultat: le nombre de trésors sur le plateau
        """
        somme = 0
        for num in range(self.getNbParticipants()):
            somme += Labyrinthe['J'].nbTresorsRestantsJoueur(num)
        return somme



    def getListeJoueurs(self):
        """
        retourne la liste joueur structures qui gèrent les joueurs et leurs trésors
        paramètre: labyrinthe le labyrinthe considéré
        résultat: les joueurs sous la forme de la structure implémentée dans listeJoueurs.py    
        """
        return self['J']


    def enleverTresor(self,lin,col,numTresor):
        """
        enleve le trésor numTresor du plateau du labyrinthe. 
        Si l'opération s'est bien passée le nombre total de trésors dans le labyrinthe
        est diminué de 1
        paramètres: labyrinthe: le labyrinthe considéré
                    lig: la ligne où se trouve la carte
                    col: la colonne où se trouve la carte
                    numTresor: le numéro du trésor à prendre sur la carte
        la fonction ne retourne rien mais modifie le labyrinthe
        """
        pos = self['P'].getCoordonneesTresor(num)
        if pos:
            self['P'].prendreTresorPlateau(pos[0],pos[1],num)

    def prendreJoueurCourant(self,lin,col):
        """
        enlève le joueur courant de la carte qui se trouve sur la case lin,col du plateau
        si le joueur ne s'y trouve pas la fonction ne fait rien
        paramètres: labyrinthe: le labyrinthe considéré
                    lig: la ligne où se trouve la carte
                    col: la colonne où se trouve la carte
        la fonction ne retourne rien mais modifie le labyrinthe    
        """
        num = self.getNumJoueurCourant()
        if (lin,col) == self['P'].getCoordonneesJoueur(num):
            self['P'].prendrePionPlateau(lin,col,num)

    def poserJoueurCourant(self,lin,col):
        """
        pose le joueur courant sur la case lin,col du plateau
        paramètres: labyrinthe: le labyrinthe considéré
                    lig: la ligne où se trouve la carte
                    col: la colonne où se trouve la carte
        la fonction ne retourne rien mais modifie le labyrinthe     
        """
        (i,j) = self.getCoordonneesJoueurCourant()
        self.prendreJoueurCourant(i,j)


    def getCarteAJouer(self):
        """
        donne la carte à jouer
        paramètre: labyrinthe: le labyrinthe considéré
        résultat: la carte à jouer      qui est la carte amovible
        """    
        return self['P']['A']

    def coupInterdit(self,direction,rangee):
        """ 
        retourne True si le coup proposé correspond au coup interdit
        elle retourne False sinon
        paramètres: labyrinthe: le labyrinthe considéré
                    direction: un caractère qui indique la direction choisie ('N','S','E','O')
                    rangee: le numéro de la ligne ou de la colonne choisie
        résultat: un booléen indiquant si le coup est interdit ou non
        """


        return (direction,rangee) == self['C']

    def jouerCarte(self,direction,rangee):
        """
        fonction qui joue la carte amovible dans la direction et sur la rangée passées 
        en paramètres. Cette fonction
        - met à jour le plateau du labyrinthe
        - met à jour la carte à jouer
        - met à jour la nouvelle direction interdite
        paramètres: labyrinthe: le labyrinthe considéré
                    direction: un caractère qui indique la direction choisie ('N','S','E','O')
                    rangee: le numéro de la ligne ou de la colonne choisie
        Cette fonction ne retourne pas de résultat mais mais à jour le labyrinthe
        """
        dir_rang = ('decalageColonneEnHaut','S'),('decalageLigneADroite','O'),('decalageLigneAGauche','E'),('decalageColonneEnBas','N')
        mat = self.getPlateau()
        if  direction == 'S':
            Amovible = mat.decalageColonneEnHaut(int(rangee),self["P"]["A"])
        elif direction == 'N':
            Amovible = mat.decalageColonneEnBas(int(rangee),self["P"]["A"])
        elif direction == 'E':
            Amovible = mat.decalageLigneAGauche(int(rangee),self["P"]["A"])
        elif direction == 'O':
            Amovible = mat.decalageLigneADroite(int(rangee),self["P"]["A"])
        else:
            raise ValueError("votre direction n'est pas reconnue")

        self['P'].amovible = Amovible



    def jouerCarte1(self,direction,rangee):
        """
        fonction qui joue la carte amovible dans la direction et sur la rangée passées 
        en paramètres. Cette fonction
        - met à jour le plateau du labyrinthe
        - met à jour la carte à jouer
        - met à jour la nouvelle direction interdite
        paramètres: labyrinthe: le labyrinthe considéré
                    direction: un caractère qui indique la direction choisie ('N','S','E','O')
                    rangee: le numéro de la ligne ou de la colonne choisie
        Cette fonction ne retourne pas de résultat mais mais à jour le labyrinthe
        """
        dir_rang = ('decalageColonneEnHaut','S'),('decalageLigneADroite','O'),('decalageLigneAGauche','E'),('decalageColonneEnBas','N')
        for (func,card) in dir_rang:
            if card == direction:
                mat = self.getPlateau()
                #func = locals()["{0}".format(func)] #sans le callable
                
                commande = eval(""'mat.{0}(int(rangee),self["P"]["A"])'.format(func))
                #Amovible = commande  #comme les décalages sont des méthodes, on est obligés de manipuler les str..
                
                #Amovible =mat.func(int(rangee),self['P']['A'])
                self['P']['A'] = commande



    def tournerCarte(self,sens='H'):
        """
        tourne la carte à jouer dans le sens indiqué en paramètre (H horaire A antihoraire)
        paramètres: labyritnthe: le labyrinthe considéré
                    sens: un caractère indiquant le sens dans lequel tourner la carte
        Cette fonction ne retourne pas de résultat mais mais à jour le labyrinthe    
        """
        carte = self.getCarteAJouer()
        if sens == 'H':
            carte.tournerHoraire()
        elif sens == 'A':
            carte.tournerAntiHoraire()
        else:
            raise ValueError("Sens non reconnu pour tournerCarte")

    def getTresorCourant(self):
        """
        retourne le numéro du trésor que doit cherche le joueur courant
        paramètre: labyritnthe: le labyrinthe considéré 
        resultat: le numéro du trésor recherché par le joueur courant
        """
        return self['J'].tresorCourant()

    def getCoordonneesTresorCourant(self):
        """
        donne les coordonnées du trésor que le joueur courant doit trouver
        paramètre: LABYRINTHE: le labyrinthe considéré 
        resultat: les coordonnées du trésor à chercher ou None si celui-ci 
                n'est pas sur le plateau
        """
        num = self.getTresorCourant()
        return self['P'].getCoordonneesTresor(num)


    def getCoordonneesJoueurCourant(self):
        """
        donne les coordonnées du joueur courant sur le plateau
        paramètre: labyritnthe: le labyrinthe considéré 
        resultat: les coordonnées du joueur courant ou None si celui-ci 
                n'est pas sur le plateau
        """
        num = self.getNumJoueurCourant()
        return self['P'].getCoordonneesJoueur(num)


    def executerActionPhase1(self,action,rangee):
        """
        exécute une action de jeu de la phase 1
        paramètres: labyrinthe: le labyrinthe considéré
                    action: un caractère indiquant l'action à effecter
                            si action vaut 'T' => faire tourner la carte à jouer
                            si action est une des lettres N E S O et rangee est un des chiffre 1,3,5 
                            => insèrer la carte à jouer à la direction action sur la rangée rangee
                            et faire le nécessaire pour passer en phase 2
        résultat: un entier qui vaut
                0 si l'action demandée était valide et demandait de tourner la carte
                1 si l'action demandée était valide et demandait d'insérer la carte
                2 si l'action est interdite car l'opposée de l'action précédente
                3 si action et rangee sont des entiers positifs
                4 dans tous les autres cas
        """
        if action == 'T':
            res = 0
            self.tournerCarte()
        elif action == 'N' or action == 'O' or action == 'S' or action == 'E':
            if not self.coupInterdit(action,rangee):
                self.jouerCarte(action,rangee)
                self.changerPhase()
                res = 1
            else:
                res = 2
        elif action is int and rangee is int and min(action,rangee) >= 0:
            res = 3
        else:
            res = 4
        return res


    def accessibleDistJoueurCourant(self, ligA,colA):
        """
        verifie si le joueur courant peut accéder la case ligA,colA
        si c'est le cas la fonction retourne une liste représentant un chemin possible
        sinon ce n'est pas le cas, la fonction retourne None
        paramètres: labyrinthe le labyrinthe considéré
                    ligA la ligne de la case d'arrivée
                    colA la colonne de la case d'arrivée
        résultat: une liste de couples d'entier représentant un chemin que le joueur
                courant atteigne la case d'arrivée s'il existe None si pas de chemin
        """
        pos = self.getCoordonneesJoueurCourant()
        if pos is not None:
            return self['P'].accessibleDist(pos[0],pos[1],ligA,colA)

    def finirTour(self):
        """
        vérifie si le joueur courant vient de trouver un trésor (si oui fait le nécessaire)
        vérifie si la partie est terminée, si ce n'est pas le cas passe au joueur suivant
        paramètre: labyrinthe le labyrinthe considéré
        résultat: un entier qui vaut :
               - 0 si le joueur courant n'a pas trouvé de trésor
               - 1 si le joueur courant a trouvé un trésor mais la partie n'est pas terminée
               - 2 si le joueur courant a trouvé son dernier trésor (la partie est donc terminée)
        """
        posJ = self.getCoordonneesJoueurCourant()
        posT = self.getCoordonneesTresorCourant()
        if posJ == posT:
            self['P'].prendreTresorPlateau(posT[0],posT[1],self.getTresorCourant())
            self['J'].joueurCourantTrouveTresor()
            if self['J'].joueurCourantAFini():
                res = 2
            else:
                res = 1
        else:
            res = 0
        next(self)
        return res



    

if __name__ == "__main__":
        
    c1 = Labyrinthe()

    print(c1.getTresorCourant())
    print(c1)
    print (c1.getCoordonneesTresorCourant())
    print(c1.getCarteAJouer())
