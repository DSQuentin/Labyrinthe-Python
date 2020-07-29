from matrice import *
from carte import *
from random import choice, sample


def Plateau(nbJoueurs, nbTresors):
    """
    créer un nouveau plateau contenant nbJoueurs et nbTrésors
    paramètres: nbJoueurs le nombre de joueurs (un nombre entre 1 et 4)
                nbTresors le nombre de trésor à placer (un nombre entre 1 et 49)
    resultat: un couple contenant
              - une matrice de taille 7x7 représentant un plateau de labyrinthe où les cartes
                ont été placée de manière aléatoire
              - la carte amovible qui n'a pas été placée sur le plateau
    """
    laby = dict()
    l_bool = [True,False]
    laby = Matrice(7,7,None)
    amovible = Carte(choice(l_bool),choice(l_bool),choice(l_bool),choice(l_bool),0,[])
    for i in range(7):
        for j in range(7):
            carte = Carte(choice(l_bool),choice(l_bool),choice(l_bool),choice(l_bool),0,[])
            setVal(laby,i,j,carte)
    del l_bool
    r7_i,r7_j = list(range(7)),list(range(7))

    #répartition des trésors
    for num_tresor in range(nbTresors):
        i,j = choice(r7_i),choice(r7_j)
        carte = getVal(laby,i,j)
        mettreTresor(carte,num_tresor)
        r7_i.remove(i)
        r7_j.remove(j)   #permet de mettre un seul tresor a chaque endroit
        
    #placement des joueurs de manière aléatoire et des coins
    N,E,S,O = False,True,True,False
    
    for (i,j),joueur in zip(((0, 0), (6, 6), (0, 6),(6,0)),sample(range(nbJoueurs),nbJoueurs)):
        carte1 = getVal(laby,int(i),int(j))
        carte = Carte(N,E,S,O,getTresor(carte1),carte1['P'].copy())
        tournerHoraire(carte)
        N,E,S,O = murNord(carte),murEst(carte),murSud(carte),murOuest(carte)
        poserPion(carte,joueur)
        setVal(laby,i,j,carte)
    return (laby, amovible)
