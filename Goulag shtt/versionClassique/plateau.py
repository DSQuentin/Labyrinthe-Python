from matrice import *
from carte import *
from random import choice, sample,shuffle


def codeangle():
    """
    renvoie le code d'un angle de manière aléatoire
    """
    return choice((1,2)) + choice((4,8))

def tout_droit():
    """
    renvoie le code d'un tout droit
    """
    return sum(choice(((1,4),(2,8))))

def rand_del(liste):
    """
    choisi un élément aléatoire d'une liste, le renvoie et le retire de cette liste
    """
    num = choice(liste)
    liste.remove(num)
    return num

def code_jonction():
    """
    renvoie le code d'une jonction de manière aléatoire
    """
    num1 = choice((1,2,4,8))

    return num1

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
    laby,amovible = creerCartesAmovibles(0,nbTresors)

    #placement des joueurs de manière aléatoire
    
    for (i,j),joueur in zip(((0, 0),(0,6),(6, 0),(6, 6)),range(1,nbJoueurs+1)):
        carte = getVal(laby,i,j)
        carte['P'] = [joueur]
        setVal(laby,i,j,carte)
    return [laby, amovible]

def getMatrice(plateau):
    """
    retourne la matrice représentant le plateau de jeu
    paramètre: plateau le plateau considéré
    résultat: la matrice représentant le plateau
    """
    return plateau[0]

def getAmovible(plateau):
    """
    retourne la carte amovible du plateau de jeu
    paramètre: plateau le plateau considéré
    résultat: la carte amovible du plateau
    """
    return plateau[1]



def genere_Liste_coords(i,j):
    """
    genere une liste de tuples avec toutes les possibilités réalisables 
    en omettant les coins
    """
    list_coord = list()
    for val in range(i*j):
        if val == 0 or val == i-1 or val == i*j-1 or val == i*(j-1):
            continue
        list_coord.append((val//7,val%7))
    return list_coord
    

def choisi_carte(cpt_murs):
    """
    choisi aléatoirement une parmi les cartes restantes
    cpt_murs est une dictionnaire qui associe à chaque type de carte la fonction pour la coder ainsi que la quantité restante
    retourne la carte et modifie cpt_murs avec un compteur -1 et si le cpt==0 alors on supprime la clé
    """
    type_C = choice(list(cpt_murs))
    func_code,cpt = cpt_murs[type_C]
    code = func_code()
    carte = Carte(False,False,False,False)
    decoderMurs(carte,code)
    if cpt == 1:
        del cpt_murs[type_C]
    else:
        cpt_murs[type_C][1] -= 1
    return carte

def creerCartesAmovibles(tresorDebut,nbTresors):
    """
    fonction utilitaire qui permet de créer les cartes amovibles du jeu en y positionnant
    aléatoirement nbTresor trésors
    la fonction retourne la liste, mélangée aléatoirement, des cartes ainsi créées
    paramètres: tresorDebut: le numéro du premier trésor à créer
                nbTresors: le nombre total de trésor à créer
    résultat: la liste mélangée aléatoirement des cartes amovibles créees
    """
    #creation plateau
    liste_fixes = [9, 1, 1, 3, 8, 8, 1, 2, 8, 4, 12, 2, 12, 4, 4, 6] # on sait que les fixes on des coordonnées pairs
    cpt_murs = {'D':[tout_droit,12],'J':[code_jonction,18-12],'A':[codeangle,20-4]} #on enlève les cartes fixes aux compteurs
    laby = Matrice(7,7,None)
    list_coord = genere_Liste_coords(7,7) # sert pour la répartition des trésors
    num_tresor = (num for num in range(tresorDebut,nbTresors))
    amovible = choisi_carte(cpt_murs)
    for i in range(7):
        for j in range(7):
            if i%2 or j%2: # si un seul des deux est impair
                carte = choisi_carte(cpt_murs)
                
            else:
                carte = Carte(False,False,False,False)
                decoderMurs(carte,liste_fixes[0])
                liste_fixes.pop(0)
                if (i,j) in list_coord:
                    mettreTresor(carte,next(num_tresor,0)) #un trésor sur chaque carte fixe sauf les coins
                    list_coord.remove((i,j))

            setVal(laby,i,j,carte)

    #repartition trésors, ils ne peuvent pas être sur la première tuile amovible (ça pourrait favoriser le premier joueur)
    
    for num_tresor in range(next(num_tresor,50),nbTresors):
        i,j = choice(list_coord)
        carte = getVal(laby,i,j)
        mettreTresor(carte,num_tresor)
        list_coord.remove((i,j))  #permet de mettre un seul tresor a chaque endroit

    return laby,amovible

def prendreTresorPlateau(plateau,lig,col,numTresor):
    """
    prend le tresor numTresor qui se trouve sur la carte en lin,col du plateau
    retourne True si l'opération s'est bien passée (le trésor était vraiment sur
    la carte
    paramètres: plateau: le plateau considéré
                lig: la ligne où se trouve la carte
                col: la colonne où se trouve la carte
                numTresor: le numéro du trésor à prendre sur la carte
    resultat: un booléen indiquant si le trésor était bien sur la carte considérée
    """
    carte = getVal(plateau[0],lig,col)
    if getTresor(carte):
        prendreTresor(carte)
        res = True
    else:
        res = False
    return res

def getCoordonneesTresor(plateau,numTresor):
    """
    retourne les coordonnées sous la forme (lig,col) du trésor passé en paramètre
    paramètres: plateau: le plateau considéré
                numTresor: le numéro du trésor à trouver
    resultat: un couple d'entier donnant les coordonnées du trésor ou None si
              le trésor n'est pas sur le plateau
    """
    # renvoie None si le trésor est sur la carte amovible
    for i in range(7):
        for j in range(7):
            carte = getVal(plateau[0],i,j)
            if getTresor(carte) == numTresor:
                return (i,j)

def getCoordonneesJoueur(plateau,numJoueur):
    """
    retourne les coordonnées sous la forme (lig,col) du joueur passé en paramètre
    paramètres: plateau: le plateau considéré
                numJoueur: le numéro du joueur à trouver
    resultat: un couple d'entier donnant les coordonnées du joueur ou None si
              le joueur n'est pas sur le plateau
    """
    try:
        terrain = getMatrice(plateau)
    except:
        terrain = plateau
    for i in range(7):
        for j in range(7):
            carte = getVal(terrain,i,j)
            if numJoueur in getListePions(carte):
                return (i,j)


def prendrePionPlateau(plateau,lig,col,numJoueur):
    """
    prend le pion du joueur sur la carte qui se trouve en (lig,col) du plateau
    paramètres: plateau:le plateau considéré
                lin: numéro de la ligne où se trouve le pion
                col: numéro de la colonne où se trouve le pion
                numJoueur: le numéro du joueur qui correspond au pion
    Cette fonction ne retourne rien mais elle modifie le plateau
    """
    try:
        carte = getVal(plateau,lig,col)
    except:
        carte = getVal(plateau[0],lig,col)
    prendrePion(carte,numJoueur)

def poserPionPlateau(plateau,lin,col,numJoueur):
    """
    met le pion du joueur sur la carte qui se trouve en (lig,col) du plateau
    paramètres: plateau:le plateau considéré
                lin: numéro de la ligne où se trouve le pion
                col: numéro de la colonne où se trouve le pion
                numJoueur: le numéro du joueur qui correspond au pion
    Cette fonction ne retourne rien mais elle modifie le plateau
    """
    try:
        carte = getVal(plateau,lin,col)
    except:
        carte = getVal(plateau[0],lin,col)
    poserPion(carte,numJoueur)

def check_voisins(plateau,carte,i,j,voisins = [('N',(-1,0)),('O',(0,-1)),('E',(0,1)),('S',(1,0))]):
    """
    renvoie tous les voisins possibles pour une position donnée 
    """
    possible = set()
    for e,(card,(i2,j2)) in enumerate(voisins):
        if not carte[card]:
            i1,j1 = i2 + i , j2 + j
            try:
                carte2 = getVal(plateau,i1,j1)
            except:
                carte2 = getVal(plateau[0],i1,j1)

            if not carte2[voisins[3-e][0]]:
                if 7 > i1 >= 0 and 7 > j1 >= 0:
                    possible.add((i1,j1))
    return possible

def check_none(func):
    """
    on s'assure que visited est bel est bien à None
    """
    if 'visited' in globals():
        visited = None
    return func

@check_none
def tous_les_chemins(plateau,ligD,colD,ligA,colA,visited=None):
    """
    renvoie les chemins possibles pour aller à la liste d'arrivée
    """
    if visited is None:
        visited = [(ligD,colD)]

    if (ligD,colD) == (ligA,colA):
        yield visited
    else:
        try:
            carte = getVal(plateau,ligD,colD)
        except:
            carte = getVal(plateau[0],ligD,colD)

        for i1,j1 in check_voisins(plateau,carte,ligD,colD):
            if (i1,j1) not in set(visited):
                for chemin in tous_les_chemins(plateau,i1,j1,ligA,colA, visited + [(i1,j1)]):
                    if chemin is not None and chemin[-1] == (ligA,colA):
                        yield chemin


@check_none
def accessibleDist(plateau,ligD,colD,ligA,colA,visited=None):
    """
    indique si il y a un chemin entre la case ligD,colD et la case ligA,colA du plateau
    mais la valeur de retour est None s'il n'y a pas de chemin, 
    sinon c'est un chemin possible entre ces deux cases sous la forme d'une liste
    de coordonées (couple de (lig,col))
    paramètres: plateau: le plateau considéré
                ligD: la ligne de la case de départ
                colD: la colonne de la case de départ
                ligA: la ligne de la case d'arrivée
                colA: la colonne de la case d'arrivée
    résultat: une liste de coordonées indiquant un chemin possible entre la case
              de départ et la case d'arrivée
    """
    if (ligD,colD) == (ligA,colA) :
        return [(ligD,colD)]
    chemins = tous_les_chemins(plateau,ligD,colD,ligA,colA,None)
    best = None
    for chemin in chemins:
        if chemin is not None:
            return chemin

def accessible(plateau,ligD,colD,ligA,colA,visited = None):
    """
    indique si il y a un chemin entre la case ligD,colD et la case ligA,colA du labyrinthe
    paramètres: plateau: le plateau considéré
                ligD: la ligne de la case de départ
                colD: la colonne de la case de départ
                ligA: la ligne de la case d'arrivée
                colA: la colonne de la case d'arrivée
    résultat: un boolean indiquant s'il existe un chemin entre la case de départ
              et la case d'arrivée
    """
    if (ligD,colD) == (ligA,colA):
        return True
    return accessibleDist(plateau,ligD,colD,ligA,colA,None) is not None


if __name__ == "__main__":
    p = Plateau(4,14)
    print((accessibleDist(p,0,0,2,2,None)))
