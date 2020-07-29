# -*- coding: utf-8 -*-
"""
                           Projet Labyrinthe 
        Projet Python 2019-2020 de 1ere année et AS DUT Informatique Orléans
        
   Module carte
   ~~~~~~~~~~~~
   
   Ce module gère les cartes du labyrinthe. 
"""
from random import sample,randint,choice


"""
la liste des caractères semi-graphiques correspondant aux différentes cartes
l'indice du caractère dans la liste correspond au codage des murs sur la carte
le caractère 'Ø' indique que l'indice ne correspond pas à une carte
"""
listeCartes=['╬','╦','╣','╗','╩','═','╝','Ø','╠','╔','║','Ø','╚','Ø','Ø','Ø']
#ens_dir = {'E':{'╬','╦','╩','═','╠','╔','╚'},'W':{'╬','╦','╩','═','╣','╗','╝'},
 #           'S':{'╬','╦','╠','╣','╔','╗','║'},'N':{'╬','╠','╣','╚','╝','║'}}

class cl_carte(object):
    def __init__(self,nord,est,sud,ouest,tresor=0,pions=[]):
        self.card = dict()
        self.card['N'] = nord
        self.card['E'] = est
        self.card['S'] = sud
        self.card['W'] = ouest
        self.card['T'] = tresor
        self.card['P'] = pions
    def getCard(self):
        """
        renvoie le dictionnaire correspondant à la classe
        """
        return self.card

    def __getitem__(self,i):
        """
        renvoie le boléen pour les cardinalités (N,S,W,E), le trésor contenu avec T et la liste des pions avec P
        """
        return self.getCard()[i]
    def __iter__(self):
        """
        permet de parcourir les boléens de cardinalités (toujours dans l'ordre N -> E -> S -> W)
        """
        for value in self.getCard().values():
            if value is int:
                return
            yield value

    def __add__(self,liste_pions):
        """
        ajoute une liste de pions a la carte (et uniquement une liste)
        """
        for pion in liste_pions:
            if pion not in self:
                self['P'].append(pion)
    def __sub__(self,pion):
        if pion in self:
            self['P'].remove(pion)

    def __len__(self):
        return len(self['P'])

    def __contains__(self,pion):
        return pion in self['P']
    def __setitem__(self,item,value):
        self.getCard()[item] = value

    def __eq__(self,a):
        """
        deux cartes sont égales si elles ont le même dictionnaire
        """
        res = True
        for card in 'SWEN':
            res = res and (self[card] == a[card])
        return res

    def __str__(self):
        affiche = str('\n')
        for key,value in self.getCard().items():
            affiche += 'à {0} on associe {1} \n'.format(key,value)
        return affiche

    



def Carte( nord, est, sud, ouest, tresor=0, pions=[]):
    """
    permet de créer une carte:
    paramètres:
    nord, est, sud et ouest sont des booléens indiquant s'il y a un mur ou non dans chaque direction
    tresor est le numéro du trésor qui se trouve sur la carte (0 s'il n'y a pas de trésor)
    pions est la liste des pions qui sont posés sur la carte (un pion est un entier entre 1 et 4)
    """
    return cl_carte(nord, est, sud, ouest, tresor, pions)


def estValide(c):
    """
    retourne un booléen indiquant si la carte est valide ou non c'est à dire qu'elle a zéro un ou deux murs
    paramètre: c une carte
    """
    return len(list(val for val in c if val is True)) <= 2

def murNord(c):
    """
    retourne un booléen indiquant si la carte possède un mur au nord
    paramètre: c une carte
    """
    return c['N']

def murSud(c):
    """
    retourne un booléen indiquant si la carte possède un mur au sud
    paramètre: c une carte
    """
    return c['S']

def murEst(c):
    """
    retourne un booléen indiquant si la carte possède un mur à l'est
    paramètre: c une carte
    """
    return c['E']

def murOuest(c):
    """
    retourne un booléen indiquant si la carte possède un mur à l'ouest
    paramètre: c une carte
    """
    return c['W']

def getListePions(c):
    """
    retourne la liste des pions se trouvant sur la carte
    paramètre: c une carte
    """
    return c['P']

def setListePions(c,listePions):
    """
    place la liste des pions passées en paramètre sur la carte
    paramètres: c: est une carte
                listePions: la liste des pions à poser
    Cette fonction ne retourne rien mais modifie la carte
    """
    c['P'] = list()
    c + listePions

def getNbPions(c):
    """
    retourne le nombre de pions se trouvant sur la carte
    paramètre: c une carte
    """
    return len(c)

def possedePion(c,pion):
    """
    retourne un booléen indiquant si la carte possède le pion passé en paramètre
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    """
    return pion in c


def getTresor(c):
    """
    retourne la valeur du trésor qui se trouve sur la carte (0 si pas de trésor)
    paramètre: c une carte
    """
    return c['T']

def prendreTresor(c):
    """
    enlève le trésor qui se trouve sur la carte et retourne la valeur de ce trésor
    paramètre: c une carte
    résultat l'entier représentant le trésor qui était sur la carte
    """
    tresor = c['T']
    c['T'] = 0
    return tresor

def mettreTresor(c,tresor):
    """
    met le trésor passé en paramètre sur la carte et retourne la valeur de l'ancien trésor
    paramètres: c une carte
                tresor un entier positif
    résultat l'entier représentant le trésor qui était sur la carte
    """
    first_tresor = c['T']
    c['T'] = tresor
    return first_tresor

def prendrePion(c, pion):
    """
    enlève le pion passé en paramètre de la carte. Si le pion n'y était pas ne fait rien
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    Cette fonction modifie la carte mais ne retourne rien
    """
    c - pion

def poserPion(c, pion):
    """
    pose le pion passé en paramètre sur la carte. Si le pion y était déjà ne fait rien
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    Cette fonction modifie la carte mais ne retourne rien
    """
    c + [pion]

def tournerHoraire(c):
    """
    fait tourner la carte dans le sens horaire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien    
    """
    ouest = c['W']
    c['W'] = c['S']
    c['S'] = c['E']
    c['E'] = c['N']
    c['N'] = ouest

def tournerAntiHoraire(c):
    """
    fait tourner la carte dans le sens anti-horaire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien    
    """
    ouest = c['W']
    c['W'] = c['N']
    c['N'] = c['E']
    c['E'] = c['S']
    c['S'] = ouest

def tourneAleatoire(c):
    """
    faire tourner la carte d'un nombre de tours aléatoire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien    
    """
    (tournerHoraire(c) for _ in range(randint(0,3)))

def coderMurs(c):
    """
    code les murs sous la forme d'un entier dont le codage binaire 
    est de la forme bNbEbSbO où bN, bE, bS et bO valent 
       soit 0 s'il n'y a pas de mur dans dans la direction correspondante
       soit 1 s'il y a un mur dans la direction correspondante
    bN est le chiffre des unité, BE des dizaine, etc...
    le code obtenu permet d'obtenir l'indice du caractère semi-graphique
    correspondant à la carte dans la liste listeCartes au début de ce fichier
    paramètre c une carte
    retourne un entier indice du caractère semi-graphique de la carte
    """
    res = b''
    for card in 'NESW':
        if c[card]:
            res += b'1'
        else:
            res += b'0'
    res = int(res[::-1],2)
    return res


def decoderMurs(c,code):
    """
    positionne les murs d'une carte en fonction du code décrit précédemment
    paramètres c une carte
               code un entier codant les murs d'une carte
    Cette fonction modifie la carte mais ne retourne rien
    """    
    for e,card in zip(reversed(range(4)),'WSEN'):
        if 2**e & code:
            code -= 2**e
            c[card] = True
        else:
            c[card] = False


def toChar(c):
    """
    fournit le caractère semi graphique correspondant à la carte (voir la variable listeCartes au début de ce script)
    paramètres c une carte
    """
    return listeCartes[coderMurs(c)]

def passageNord(carte1,carte2):
    """
    suppose que la carte2 est placée au nord de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par le nord
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """
    return not carte2["S"] and not carte1["N"]

def passageSud(carte1,carte2):
    """
    suppose que la carte2 est placée au sud de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par le sud
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """
    return passageNord(carte2,carte1)

def passageOuest(carte1,carte2):
    """
    suppose que la carte2 est placée à l'ouest de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par l'ouest
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """
    return not carte2["E"] and not carte1["W"]

def passageEst(carte1,carte2):
    """
    suppose que la carte2 est placée à l'est de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par l'est
    paramètres carte1 et carte2 deux cartes
    résultat un booléen    
    """
    return passageOuest(carte2,carte1)



if __name__ == "__main__":
    c = Carte(True,False,True,False)
    print(toChar(c))