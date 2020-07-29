from matrice import *
from carte import *
from random import choice


class Plateau(object):
    def __init__(self,nbJoueurs,nbTresors):
        """
        créer un nouveau plateau contenant nbJoueurs et nbTrésors
        paramètres: nbJoueurs le nombre de joueurs (un nombre entre 1 et 4)
                    nbTresors le nombre de trésor à placer (un nombre entre 1 et 49)
        resultat: un couple contenant
                  - une matrice de taille 7x7 représentant un plateau de labyrinthe où les cartes
                    ont été placée de manière aléatoire
                  - la carte amovible qui n'a pas été placée sur le plateau
        """
        self._nbJoueurs = nbJoueurs
        self._nbTresors = nbTresors

        #fonctions auxiliaire pour le codage des murs

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
        

        
        def code_jonction():
            """
            renvoie le code d'une jonction de manière aléatoire
            """
            return choice((1,2,4,8))

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
            carte.decoderMurs(code)
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
            liste_fixes =  [9, 1, 1, 3, 8, 8, 1, 2, 8, 4, 12, 2, 12, 4, 4, 6] # on sait que les fixes on des coordonnées pairs
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
                        carte.decoderMurs(liste_fixes[0])
                        liste_fixes.pop(0)
                        if (i,j) in list_coord:
                            carte.mettreTresor(next(num_tresor,0)) #un trésor sur chaque carte fixe sauf les coins
                            list_coord.remove((i,j))

                    laby[(i,j)] = carte

            #repartition trésors, ils ne peuvent pas être sur la première tuile amovible (ça pourrait favoriser le premier joueur

            for num_tresor in range(next(num_tresor,50),nbTresors):
                i,j = choice(list_coord)
                carte = laby[(i,j)]
                carte.mettreTresor(num_tresor)
                list_coord.remove((i,j))  #permet de mettre un seul tresor a chaque endroit
            return laby,amovible


        self.laby,self.amovible = creerCartesAmovibles(0,nbTresors)
        print(self)  #donne l'appercu attendu

        #placement des joueurs de manière aléatoire

        for (i,j),joueur in zip(((0, 0), (0, 6), (6, 0),(6,6)),range(1,nbJoueurs + 1)):
            carte = self.laby[(i,j)]
            carte['P'] = [joueur]
            self.laby[(i,j)] = carte


    def __len__(self):
        """
        retourne le nombre de trésors initial
        """
        return self._nbTresors

    def get_nb_joueurs(self):
        """
        retourne le nombre de joueurs
        """
        return self._nbJoueurs

    def __iter__(self):
        """
        renvoie toutes les cartes du plateau avec leur coordonnées sans la carte amovible"
        """
        for i in range(7):
            for j in range(7):
                yield ((i,j),getVal(self.laby,i,j))
        #yield ((None,None),self.amovible) #c'était la carte amovible
    
    def __setitem__(self,item,value):
        """
        met à l'attribut item de la classe Labyrinthe la valeur value...
        """
        self.item = value

    def __getitem__(self,a):
        """
        renvoie l'objet demandé (0 ou 'P pour le laby et 1 ou 'A' pour carte Amovible)
        """
        if a in {0,'P'}:
            return self.laby
        elif a in {1,'A'}:
            return self.amovible
        else:
            raise ValueError("Cet objet n'est pas accessible")
    def __str__(self):
        """
        permet d'avoir une très représentation du plateau en texte 
        sans les trésors  et sans les coordonnées bien évidemment
        """
        affiche = "\n carte amovible : {0} \n ".format(self['A'].toChar())
        for i in range(7):
            affiche += "\n"
            for j in range(7):
                card = self['P'][(i,j)]
                code = card.toChar()
                affiche += "{0} ".format(code)
        return affiche





    def prendreTresorPlateau(self,lig,col,numTresor):
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
        carte = self['P'].getVal(lig,col)
        if carte.getTresor() == numTresor:
            carte.prendreTresor()
            res = True
        else:
            res = False
        return res
    
    def getCoordonneesTresor(self,numTresor):
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
                carte = self['P'].getVal(i,j)
                if carte.getTresor() == numTresor:
                    return (i,j)
    
    def getCoordonneesJoueur(self,numJoueur):
        """
        retourne les coordonnées sous la forme (lig,col) du joueur passé en paramètre
        paramètres: plateau: le plateau considéré
                    numJoueur: le numéro du joueur à trouver
        resultat: un couple d'entier donnant les coordonnées du joueur ou None si
                  le joueur n'est pas sur le plateau
        """
        terrain = self['P']
        for i in range(7):
            for j in range(7):
                carte = terrain[(i,j)]
                if numJoueur in carte.getListePions():
                    return (i,j)
    
    def prendrePionPlateau(self,lig,col,numJoueur):
        """
        prend le pion du joueur sur la carte qui se trouve en (lig,col) du plateau
        paramètres: plateau:le plateau considéré
                    lin: numéro de la ligne où se trouve le pion
                    col: numéro de la colonne où se trouve le pion
                    numJoueur: le numéro du joueur qui correspond au pion
        Cette fonction ne retourne rien mais elle modifie le plateau
        """
        carte = self['P'].getVal(lig,col)
        carte - numJoueur
    
    def poserPionPlateau(self,lig,col,numJoueur):
        """
        met le pion du joueur sur la carte qui se trouve en (lig,col) du plateau
        paramètres: plateau:le plateau considéré
                    lin: numéro de la ligne où se trouve le pion
                    col: numéro de la colonne où se trouve le pion
                    numJoueur: le numéro du joueur qui correspond au pion
        Cette fonction ne retourne rien mais elle modifie le plateau
        """
        carte = self['P'].getVal(lig,col)
        carte + [numJoueur]
    
        
    def check_voisins(self,carte,i,j,voisins = [('N',(-1,0)),('O',(0,-1)),('E',(0,1)),('S',(1,0))]):
        """
        renvoie tous les voisins possibles pour une position donnée 
        """
        possible = set()
        for e,(card,(i2,j2)) in enumerate(voisins):
            if not carte[card]:
                i1,j1 = i2 + i , j2 + j
                carte2 = self['P'][(i1,j1)]
                card_opposee = voisins[3-e][0] #cardinalité opposée à celle actuelle

                if not carte2[card_opposee]:
                    if 7 > i1 >= 0 and 7 > j1 >= 0:
                        possible.add((i1,j1))
        return possible


    def tous_les_chemins(self,ligD,colD,ligA,colA,visited=None):
        """
        renvoie les chemins possibles pour aller à la liste d'arrivée
        """
        if visited is None:
            visited = [(ligD,colD)]

        if (ligD,colD) == (ligA,colA):
            yield visited
        else:
            carte = self['P'].getVal(ligD,colD)

            for i1,j1 in self.check_voisins(carte,ligD,colD):
                if (i1,j1) not in set(visited):
                    for chemin in self.tous_les_chemins(i1,j1,ligA,colA, visited + [(i1,j1)]):
                        if chemin is not None and chemin[-1] == (ligA,colA):
                            yield chemin


    def accessibleDist(self,ligD,colD,ligA,colA,visited=None):
        """
        indique si il y a un chemin entre la case ligD,colD et la case ligA,colA du plateau
        mais la valeur de retour est None s'il n'y a pas de chemin, 
        sinon c'est un chemin possible entre ces deux cases sous la forme d'une liste
        de coordonées (couple de (lig,col))
        paramètres: - ligD: la ligne de la case de départ
                    - colD: la colonne de la case de départ
                    - ligA: la ligne de la case d'arrivée
                    - colA: la colonne de la case d'arrivée
        résultat: une liste de coordonées indiquant un chemin possible entre la case
                de départ et la case d'arrivée
        """
        if (ligD,colD) == (ligA,colA) :
            return [(ligD,colD)]
        chemins = self.tous_les_chemins(ligD,colD,ligA,colA,None)
        for chemin in chemins:
            if chemin is not None:
                return chemin

    def accessible(self,ligD,colD,ligA,colA,visited = None):
        """
        indique si il y a un chemin entre la case ligD,colD et la case ligA,colA du labyrinthe
        paramètres: 
                    - ligD: la ligne de la case de départ
                    - colD: la colonne de la case de départ
                    - ligA: la ligne de la case d'arrivée
                    - colA: la colonne de la case d'arrivée
        résultat: un boolean indiquant s'il existe un chemin entre la case de départ
                et la case d'arrivée
        """
        if (ligD,colD) == (ligA,colA):
            return True
        return self.accessibleDist(ligD,colD,ligA,colA,None) is not None

if __name__== '__main__':
    # bien le bonjour
    p = Plateau(4,12)
    print(p)
    print(p.accessibleDist(0,0,1,1))