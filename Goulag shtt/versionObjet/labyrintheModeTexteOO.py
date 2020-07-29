#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
                           Projet Labyrinthe 
        Projet Python 2019-2020 de 1ere année et AS DUT Informatique Orléans
        
   Programme principal du labyrinthe en mode texte
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

from labyrinthe import *
from ansiColor import *
import sys
import time

class LabyrintheModeTexte(object):
    def __init__(self,labyrinthe):
        """
        création d'une vue de labyrinthe en mode texte
        paramètre: labyrinthe le labyrinthe à afficher
        résultat: une vue texte du labyrinthe
        """
        self.labyrinthe= labyrinthe
        
    def setLabyrinthe(self,labyrinthe):
        """
        association d'un jeu de labyrinthe à la vue mode texte
        paramètres: 
                    labyrinthe le labyrinthe à afficher
        La fonction ne retourne pas de résultat mais modifie lmt    
        """
        self.labyrinthe=labyrinthe

    def getLabyrinthe(self):
        """
        retourne le labyrinthe associé à la vue mode texte
        paramètre: lmnt  une vue de labyrinthe mode texte
        resultat le labyrinthe associé
        """
        return self.labyrinthe
        
    def afficheCarte(self, carte,pion=1,tresor=-1):
        """
        affiche une carte
        paramètres: lmt: une vue de labyrinthe mode texte
                    carte: la carte à afficher
                    pion: numéro du pion à afficher en priorité si plusieurs disponibles
                    tresor: numero du trésor à afficher (le trésor recherché
        Le fonction ne retourne rien mais affiche à l'écran la carte
        """
        coulFond=NORMAL
        coulCar=NORMAL
        style=AUCUN
        if carte.getTresor()==tresor:
            coulFond=GRIS
            coulCar=NOIR
        lesPions=carte.getListePions()
        if len(lesPions)>0:
            if len(lesPions)>1:
                style=GRAS
            if carte.possedePion(pion):
                coulCar=pion
            else:  
                coulCar=lesPions[0]
        pcouleur(carte.toChar(),coulCar,coulFond,style)
     
    def afficheLabyrinthe(self,message="",sauts=0):
        """
        affiche un jeu de labyrinthe
        paramètres: lmt: une vue de labyrinthe mode texte
                    message: une chaine de caractères contenant un message à afficher
                    sauts: nombre de lignes à sauter à la fin de l'affichage
        Le fonction ne retourne rien mais affiche le labyrinthe à l'écran
        """
        clearscreen();
        print(message)
        labyrinthe=self.getLabyrinthe()
        liste_J=labyrinthe.getListeJoueurs()
        print('Cartes restantes : ')
        for i in range(1,labyrinthe.getNbParticipants()+1):
            pcouleur(liste_J.nomJoueur(i).ljust(10)+' '+str(liste_J.nbTresorsRestantsJoueur(i))+' ',i)
            print()
        print()
        print("C'est au tour de ",end='')
        pcouleur(liste_J.nomJoueurCourant(),liste_J.numJoueurCourant())
        print(" de jouer")
        tresor=liste_J.tresorCourant()
        print("Le trésor recherché est :",tresor, "caché ",end='')
        coord=labyrinthe.getCoordonneesTresorCourant()
        if coord==None:
            print("sur la carte à jouer")
        else:
            print("en",coord)
        print()
        print(' ',sep='',end='')
        plateau=labyrinthe.getPlateau()
        remplissage=' '*30
        print(remplissage,end='')
        for i in range(1,7,2):
            print(" "+str(i),sep='',end='')
        print()
        for i in range(plateau.getNbLignes()):
            print(remplissage,end='')            
            if i%2==0:
                print(' ',sep='',end='')
            else:
                print(str(i),sep='',end='')
            for j in range(plateau.getNbColonnes()):
                self.afficheCarte(plateau.getVal(i,j),liste_J.numJoueurCourant(),tresor)
            if i%2==0:
                print(' ',sep='',end='')
            else:
                print(str(i),sep='',end='')            
            print()
        print(' ',sep='',end='')
        print(remplissage,end='')        
        for i in range(1,7,2):
            print(" "+str(i),sep='',end='')
        print()
        print("Carte à jouer: ",end='')
        self.afficheCarte(labyrinthe.getCarteAJouer(),tresor=tresor)
        for i in range(sauts):
            print()
        print()

    def animationChemin(self,chemin, joueur,pause=0.1):
        """
        affiche le déplacement du joueur courant vers sa destination
        paramètres: lmt: la vue texte du labyrinthe
                    chemin: une liste de coordonnées indiquant le chemin suivi
                    joueur: numéro du joueur qui se déplace
                    pause: temporisation entre l'affichage de deux étapes
        """
        (xp,yp)=chemin.pop(0)
        plateau = self.labyrinthe['P']
        for (x,y) in chemin:
            plateau.prendrePionPlateau(xp,yp,joueur)
            plateau.poserPionPlateau(x,y,joueur)
            self.afficheLabyrinthe(sauts=1)
            time.sleep(pause)
            xp,yp=x,y
        return xp,yp

    # -------------------------------------------
    # fonctions de saisie des actions des joueurs
    # -------------------------------------------
    
    def saisirOrdre(self):
        """
        permet de saisir soit l'ordre de tourner la carte à jouer
                        soit l'ordre d'insérer la carte à jouer
        la fonction vérifie la validité de l'ordre. On ne sort de la fonction que si
        l'ordre est valide.
        paramètre: lmt: une vue texte de labyrinthe
        résultat: l'ordre saisi sous la forme d'un couple (x,y)
                où x est un caractère valant un des cinq caractères 'T','N','E','S','O'
                dans le cas où x vaut 'T' la valeur de y n'est pas utilisée,
                dans le cas où x vaut une des quatre autres valeurs, y doit valoir 1, 3 ou 5
                c'est à dire le numéro de la ligne ou de la colonne où insérer la carte
                si l'ordre saisi n'est pas valide la focntion retourne (-1,-1)
        """
        valide = False
        while not valide :
            (x,y) = input("\n -T si vous souhaitez prendre le tresor \n Saisissez une cardinalité (N S E O) suivie de la colonne/ligne (1,3,5) désirée, exemple : 'N 5' .\n \n Veuillez saisir votre ordre :   ").split()
            if x == 'T':
                y = 'T'
            else:
                valide = True
        return (x,y)



    def saisirDeplacement(self):
        """
        permet de saisir les coordonnées du point d'arrivée visé par le joueur courant
        paramètre: lmt: une vue texte de labyrinthe
        résultat: un couple d'entier (lin,col) indiquant les coordonnées de la case destination. Si l'utilisateur a entré des coordonnées incorrecte la fonction retourne (-1,-1)
        """ 
        try:
            (x,y) = tuple(map(int,input("Sous la forme num_lig num_col (5 4 par exemple), \n saisir votre déplacement : ").split()))
            if min(x,y) < 0 and max(x,y) > 6 :
                (x,y) = (-1,-1)
        except: #il a mal indiqué les coordonées
            (x,y) = (-1,-1)
        return (x,y)
            



            
    # demarre la partie en mode texte
    def demarrer(self):
        """
        lance le jeu du labyrinte en mode texte, il faut que le labyrinthe et 
        les joueurs aient été créés avant ce lancement
        paramètre: lmt: une vue texte de labyrinthe
        la fonction ne retourne rien mais effectue une partie de labyrinthe
        """
        # premier affichage du jeu
        self.afficheLabyrinthe()
        labyrinthe=self.getLabyrinthe()
        plateau=labyrinthe.getPlateau()
        fini=False
        while not fini: # tant qu'aucun joueur n'a gagné
            while(labyrinthe.getPhase()==1):  # tant qu'on est dans la phase 1
                x,y=self.saisirOrdre() # on saisit une ordre de phase 1
                res=labyrinthe.executerActionPhase1(x,y) # on effectue les actions liées à cet ordre
                # traitement du résultat de l'ordre pour afficher le bon message à l'utilisateur
                if res==0: 
                    message="La carte a été tournée"
                elif res==1:
                    message="La carte a bien été insérée"
                elif res==2:
                    message="Ce coup est interdit car l'opposé du précédent"
                elif res==3:
                    message="Vous devez insérer la carte avant de vous déplacer"
                else:
                    message="Veuillez soit tourner la carte soit l'insérer"
                self.afficheLabyrinthe(message)
                
            # la première phase est terminée, on va demander au joueur sa case destination
            chemin=None
            xDep,yDep=labyrinthe.getCoordonneesJoueurCourant()
            nomJC=labyrinthe.getNomJoueurCourant()
            pionJC=labyrinthe.getNumJoueurCourant()
            while chemin==None: # tant que la case destination n'est pas valide
                xA,yA=self.saisirDeplacement() # saisie de la destination
                if xA==-1 or yA==-1: # coordonées incorrectes
                    self.afficheLabyrinthe("Veuillez choisir une case du labyrinthe")
                else: # coordonées correctes 
                      #=> on va verifier l'accessibilité de la case destination pour le joueur courant 
                    chemin=labyrinthe['P'].accessibleDist(xDep,yDep,xA,yA)
                    if chemin==None:
                        self.afficheLabyrinthe("Cette case n'est pas accessible au joueur "+nomJC)
            # le joueur a saisi une destination correcte et accessible
            # on déplace le joueur sur sa case destination
            self.animationChemin(chemin,pionJC)
            # sauvegarde du numéro de trésor à trouver pour l'affichage
            t=labyrinthe.getTresorCourant()
            # action finalisant le tour
            res2=labyrinthe.finirTour()
            message=""
            # traitement du résultat de la fonction finirTour pour afficher le bon message
            if res2==2:
                message="Le joueur "+nomJC+" a gagné"
                fini=True
            elif res2==1:
                message="Le joueur "+nomJC+" vient de trouver le trésor "+str(t)
            self.afficheLabyrinthe(message)
        # la partie est terminer
        print("Merci au revoir")

            
if __name__ == "__main__":
    #entrée des joueurs à la partie
    liste_J = []
    continuer = True
    i = 1
    while continuer:
        liste_J.append(input("Joueur numéro {0},\nVeuillez insérer son nom  : ".format(i)))
        i += 1
        print('\n')
        if i == 5:
            continuer = False
        rep = input("Un autre joueur veut-il se joindre à cette partie ma foi déjantée ? (o/N)")
        print('\n')
        if rep == 'o' or rep == 'O':
            continue
        else:
            continuer = False
    #nous passons à la saisie du nombre de trésors/joueur
    ok = False
    while not ok:
        try:
            nbTresors = int(input("Combien de trésors est-ce que les joueurs devront trouver (0 pour le maximum) ? "))
            ok = True
        except:
            print("Allez faites-un effort, il nous faut un nombre s'il vous plait")
    print("Félicitaions vous y êtes parvenu ! bon jeu à vous")
    

    print("Bienvenue dans le très réputé du labyrinthe (vous avez raison, c'est un classique)")
    l = Labyrinthe(liste_J,nbTresorsMax=nbTresors)

    g=LabyrintheModeTexte(l)

    g.demarrer()
            

