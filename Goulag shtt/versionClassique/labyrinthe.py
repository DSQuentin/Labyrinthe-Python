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
from itertools import cycle


def Labyrinthe(nomsJoueurs=["joueur1","joueurs2"],nbTresors=24, nbTresorsMax=0):
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
    laby = dict()
    laby['J'] = ListeJoueurs(nomsJoueurs)
    laby['P'] = Plateau(len(nomsJoueurs),nbTresors)
    distribuerTresors(laby['J'],nbTresors,nbTresorsMax)
    laby['G'] = cycle(p for p in range(1,3))
    laby['Ph'] = next(laby['G'])
    laby['Pl'] = getJoueurCourant(laby['J'])
    laby['C'] = (None,None) #coup précédent
    return laby

def getPlateau(labyrinthe):
    """
    retourne la matrice représentant le plateau de jeu
    paramètre: labyrinthe le labyrinthe considéré
    résultat: la matrice représentant le plateau de ce labyrinthe
    """
    #on va retourner la carte amovible aussi
    return getMatrice(labyrinthe['P'])

def getNbParticipants(labyrinthe):
    """
    retourne le nombre de joueurs engagés dans la partie
    paramètre: labyrinthe le labyrinthe considéré
    résultat: le nombre de joueurs de la partie
    """
    return getNbJoueurs(labyrinthe['J'])

def getNomJoueurCourant(labyrinthe):
    """
    retourne le nom du joueur courant
    paramètre: labyrinthe le labyrinthe considéré
    résultat: le nom du joueurs courant
    """
    return getNom(labyrinthe['Pl'])

def getNumJoueurCourant(labyrinthe):
    """
    retourne le numero du joueur courant
    paramètre: labyrinthe le labyrinthe considéré
    résultat: le numero du joueurs courant
    """
    return numJoueurCourant(labyrinthe['J'])

def getPhase(labyrinthe):
    """
    retourne la phase du jeu courante
    paramètre: labyrinthe le labyrinthe considéré
    résultat: le numéro de la phase de jeu courante
    """   
    return labyrinthe['Ph']


def changerPhase(labyrinthe):
    """
    change de phase de jeu en passant la suivante
    paramètre: labyrinthe le labyrinthe considéré
    la fonction ne retourne rien mais modifie le labyrinthe
    """    
    labyrinthe['Ph'] = next(labyrinthe['G'])
    if labyrinthe['Ph'] == 1:
        changerJoueurCourant(labyrinthe['J'])
        labyrinthe['Pl'] =  getJoueurCourant(labyrinthe['J'])


def getNbTresors(labyrinthe):
    """
    retourne le nombre de trésors qu'il reste sur le labyrinthe
    paramètre: labyrinthe le labyrinthe considéré
    résultat: le nombre de trésors sur le plateau
    """
    somme = 0
    for num in range(getNbParticipants(labyrinthe)):    #les joueurs commencent à 0
        somme += nbTresorsRestantsJoueur(labyrinthe['J'],num)
    return somme



def getListeJoueurs(labyrinthe):
    """
    retourne la liste joueur structures qui gèrent les joueurs et leurs trésors
    paramètre: labyrinthe le labyrinthe considéré
    résultat: les joueurs sous la forme de la structure implémentée dans listeJoueurs.py    
    """
    return labyrinthe['J']


def enleverTresor(labyrinthe,lin,col,numTresor):
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
    pos = getCoordonneesTresor(labyrinthe['P'],num)
    if pos:
        prendreTresorPlateau(labyrinthe['P'],pos[0],pos[1],num)
    

#    for num in range(1,getNbParticipants(labyrinthe)+1):
#            if prochainTresorJoueur(labyrinthe['J'],num) == numTresor:             :(


def prendreJoueurCourant(labyrinthe,lin,col):
    """
    enlève le joueur courant de la carte qui se trouve sur la case lin,col du plateau
    si le joueur ne s'y trouve pas la fonction ne fait rien
    paramètres: labyrinthe: le labyrinthe considéré
                lig: la ligne où se trouve la carte
                col: la colonne où se trouve la carte
    la fonction ne retourne rien mais modifie le labyrinthe    
    """
    num = getNumJoueurCourant(labyrinthe)
    if (lin,col) == getCoordonneesJoueur(labyrinthe['P'],num):
        prendrePionPlateau(labyrinthe['P'],lin,col,num)

def poserJoueurCourant(labyrinthe,lin,col):
    """
    pose le joueur courant sur la case lin,col du plateau
    paramètres: labyrinthe: le labyrinthe considéré
                lig: la ligne où se trouve la carte
                col: la colonne où se trouve la carte
    la fonction ne retourne rien mais modifie le labyrinthe     
    """
    (i,j) = getCoordonneesJoueurCourant(labyrinthe)
    prendreJoueurCourant(labyrinthe,i,j)


def getCarteAJouer(labyrinthe):
    """
    donne la carte à jouer
    paramètre: labyrinthe: le labyrinthe considéré
    résultat: la carte à jouer      qui est la carte amovible
    """    
    return getAmovible(labyrinthe['P'])

def coupInterdit(labyrinthe,direction,rangee):
    """ 
    retourne True si le coup proposé correspond au coup interdit
    elle retourne False sinon
    paramètres: labyrinthe: le labyrinthe considéré
                direction: un caractère qui indique la direction choisie ('N','S','E','O')
                rangee: le numéro de la ligne ou de la colonne choisie
    résultat: un booléen indiquant si le coup est interdit ou non
    """
    return (direction,rangee) == labyrinthe['C']


def jouerCarte(labyrinthe,direction,rangee):
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
    dir_rang = (decalageColonneEnHaut,'S'),(decalageLigneADroite,'O'),(decalageLigneAGauche,'E'),(decalageColonneEnBas,'N')
    for (func,card) in dir_rang:
        if card == direction:
            Amovible = func(getPlateau(labyrinthe),int(rangee), getAmovible(labyrinthe['P']))
            labyrinthe['P'][1] = Amovible





def tournerCarte(labyrinthe,sens='H'):
    """
    tourne la carte à jouer dans le sens indiqué en paramètre (H horaire A antihoraire)
    paramètres: labyritnthe: le labyrinthe considéré
                sens: un caractère indiquant le sens dans lequel tourner la carte
     Cette fonction ne retourne pas de résultat mais mais à jour le labyrinthe    
    """
    carte = getCarteAJouer(labyrinthe)
    if sens == 'H':
        tournerHoraire(carte)
    else:
        tournerAntiHoraire(carte)

def getTresorCourant(labyrinthe):
    """
    retourne le numéro du trésor que doit cherche le joueur courant
    paramètre: labyritnthe: le labyrinthe considéré 
    resultat: le numéro du trésor recherché par le joueur courant
    """
    return tresorCourant(labyrinthe['J'])

def getCoordonneesTresorCourant(labyrinthe):
    """
    donne les coordonnées du trésor que le joueur courant doit trouver
    paramètre: labyritnthe: le labyrinthe considéré 
    resultat: les coordonnées du trésor à chercher ou None si celui-ci 
              n'est pas sur le plateau
    """
    num = getTresorCourant(labyrinthe)
    return getCoordonneesTresor(labyrinthe['P'],num)


def getCoordonneesJoueurCourant(labyrinthe):
    """
    donne les coordonnées du joueur courant sur le plateau
    paramètre: labyritnthe: le labyrinthe considéré 
    resultat: les coordonnées du joueur courant ou None si celui-ci 
              n'est pas sur le plateau
    """
    num = getNumJoueurCourant(labyrinthe)
    return getCoordonneesJoueur(labyrinthe['P'],num)



def executerActionPhase1(labyrinthe,action,rangee):
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
        tournerCarte(labyrinthe)
    elif action == 'N' or action == 'O' or action == 'S' or action == 'E':
        if not coupInterdit(labyrinthe,action,rangee):
            jouerCarte(labyrinthe,action,rangee)
            changerPhase(labyrinthe)
            res = 1
        else:
            res = 2
    elif action is int and rangee is int and min(action,rangee) >= 0:
        res = 3
    else:
        res = 4
    return res

def accessibleDistJoueurCourant(labyrinthe, ligA,colA):
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
    pos = getCoordonneesJoueurCourant(labyrinthe)
    if pos is not None:
        return accessibleDist(labyrinthe['P'],pos[0],pos[1],ligA,colA)

def finirTour(labyrinthe):
    """
    vérifie si le joueur courant vient de trouver un trésor (si oui fait le nécessaire)
    vérifie si la partie est terminée, si ce n'est pas le cas passe au joueur suivant
    paramètre: labyrinthe le labyrinthe considéré
    résultat: un entier qui vaut
              0 si le joueur courant n'a pas trouvé de trésor
              1 si le joueur courant a trouvé un trésor mais la partie n'est pas terminée
              2 si le joueur courant a trouvé son dernier trésor (la partie est donc terminée)
    """
    posJ = getCoordonneesJoueurCourant(labyrinthe)
    posT = getCoordonneesTresorCourant(labyrinthe)
    if posJ == posT:
        prendreTresorPlateau(labyrinthe['P'],posT[0],posT[1],getTresorCourant(labyrinthe))
        joueurCourantTrouveTresor(labyrinthe['J'])
        if joueurCourantAFini(labyrinthe['J']):
            res = 2
        else:
            res = 1
    else:
        res = 0
    changerPhase(labyrinthe)
    return res


    

if __name__ == "__main__":
        
    c1 = Labyrinthe()
    assert getNbTresors(c1) == 24
    assert getPhase(c1) == 1
    changerPhase(c1)
    assert getPhase(c1) == 2

    print(getTresorCourant(c1))
    print(c1)
    print (getCoordonneesTresorCourant(c1))
