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


class Carte(object):
    def __init__(self,nord,est,sud,ouest,tresor=0,pions=[]):
        """
        permet de créer une carte:
        paramètres:
        nord, est, sud et ouest sont des booléens indiquant s'il y a un mur ou non dans chaque direction
        tresor est le numéro du trésor qui se trouve sur la carte (0 s'il n'y a pas de trésor)
        pions est la liste des pions qui sont posés sur la carte (un pion est un entier entre 1 et 4)
        """
        self.card = dict()
        self['N'] = nord
        self['E'] = est
        self['S'] = sud
        self['O'] = ouest
        self['T'] = tresor
        self['P'] = pions.copy()

    def getCard(self):
        """
        renvoie le dictionnaire correspondant à la classe
        """
        return self.card

    def __getitem__(self,i):
        """
        renvoie le boléen pour les cardinalités (N,S,W,E), le trésor contenu avec T et la liste des pions avec P
        """
        return self.card[i]
    def _setitem__(self,key,value):
        """
        dans le dictionnaire card, met à key la valeur value
        """
        self.card[key] = value


    def __iter__(self):
        """
        permet de parcourir les boléens de cardinalités (toujours dans l'ordre N -> E -> S -> W)
        """
        for value in self.card.values():
            if value is int:
                return
            yield value

    def __add__(self,liste_pions):
        """
        ajoute une liste de pions a la carte (et uniquement une liste)
        """
        if self['P'] is None:
            self['P'] = []
        for pion in liste_pions:
            if pion not in self:
                self['P'].append(pion)
    def __sub__(self,pion):
        """
        enlève le pion de la liste
        """
        if pion in self:
            self['P'].remove(pion)

    def __len__(self):
        """
        renvoie le nombre de pions
        """
        return len(self['P'])

    def __contains__(self,pion):
        """
        indique si le pion est dans la carte
        """
        return pion in self['P']

    def __setitem__(self,item,value):
        self.card[item] = value

    def __eq__(self,a):
        """
        deux cartes sont égales si elles ont le même dictionnaire
        """
        return self.card == a.card

    def __str__(self):
        affiche = str('\n')
        for key,value in self.card.items():
            affiche += 'à {0} on associe {1} \n'.format(key,value)
        return affiche

        


    def estValide(self):
        """
        retourne un booléen indiquant si la carte est valide ou non c'est à dire qu'elle a zéro un ou deux murs
        paramètre: une carte
        """
        return len(list(card for card in 'NSEO' if self[card]is True)) <= 2

    def murNord(self):
        """
        retourne un booléen indiquant si la carte possède un mur au nord
        paramètre: une carte
        """
        return self['N']

    def murSud(self):
        """
        retourne un booléen indiquant si la carte possède un mur au sud
        paramètre: une carte
        """
        return self['S']

    def murEst(self):
        """
        retourne un booléen indiquant si la carte possède un mur à l'est
        paramètre: une carte
        """
        return self['E']

    def murOuest(self):
        """
        retourne un booléen indiquant si la carte possède un mur à l'ouest
        paramètre: une carte
        """
        return self['O']

    def getListePions(self):
        """
        retourne la liste des pions se trouvant sur la carte
        paramètre: une carte
        """
        return self['P']

    def setListePions(self,listePions):
        """
        place la liste des pions passées en paramètre sur la carte
        paramètres:
            - listePions: la liste des pions à poser
        Cette fonction ne retourne rien mais modifie la carte
        """
        self['P'] = []
        self + listePions

    def getNbPions(self):
        """
        retourne le nombre de pions se trouvant sur la carte
        paramètre: la carte
        résultat:le nb de pions sur la carte (int)
        """
        return len(self)

    def possedePion(self,pion):
        """
        retourne un booléen indiquant si la carte possède le pion passé en paramètre
        paramètres:
                   - pion un entier compris entre 1 et 4
        résultat: un boléen
        """
        return pion in self


    def getTresor(self):
        """
        retourne la valeur du trésor qui se trouve sur la carte (0 si pas de trésor)
        paramètre: la carte
        résultat: le trésor sur la carte (int)
        """
        return self['T']

    def prendreTresor(self):
        """
        enlève le trésor qui se trouve sur la carte et retourne la valeur de ce trésor
        paramètre: la carte
        résultat l'entier représentant le trésor qui était sur la carte
        """
        tresor = self['T']
        self['T'] = 0
        return tresor

    def mettreTresor(self,tresor):
        """
        met le trésor passé en paramètre sur la carte et retourne la valeur de l'ancien trésor
        paramètres: la carte
                    tresor un entier positif
        résultat l'entier représentant le trésor qui était sur la carte
        """
        first_tresor = self['T']
        self['T'] = tresor
        return first_tresor

    def prendrePion(self, pion):
        """
        enlève le pion passé en paramètre de la carte. Si le pion n'y était pas ne fait rien
        paramètres: la carte
                    pion un entier compris entre 1 et 4
        Cette fonction modifie la carte mais ne retourne rien
        """
        self - pion

    def poserPion(self, pion):
        """
        pose le pion passé en paramètre sur la carte. Si le pion y était déjà ne fait rien
        paramètres: la carte
                    pion un entier compris entre 1 et 4
        Cette fonction modifie la carte mais ne retourne rien
        """
        self + [pion]

    def tournerHoraire(self):
        """
        fait tourner la carte dans le sens horaire
        paramètres: la carte
        Cette fonction modifie la carte mais ne retourne rien    
        """
        ouest = self['O']
        self['O'] = self['S']
        self['S'] = self['E']
        self['E'] = self['N']
        self['N'] = ouest

    def tournerAntiHoraire(self):
        """
        fait tourner la carte dans le sens anti-horaire
        paramètres: la carte
        Cette fonction modifie la carte mais ne retourne rien    
        """
        ouest = self['O']
        self['O'] = self['N']
        self['N'] = self['E']
        self['E'] = self['S']
        self['S'] = ouest

    def tourneAleatoire(self):
        """
        faire tourner la carte d'un nombre de tours aléatoire
        paramètres: la carte
        Cette fonction modifie la carte mais ne retourne rien    
        """
        (self.tournerHoraire() for _ in range(randint(0,3)))

    def coderMurs(self):
        """
        code les murs sous la forme d'un entier dont le codage binaire 
        est de la forme bNbEbSbO où bN, bE, bS et bO valent 
        soit 0 s'il n'y a pas de mur dans dans la direction correspondante
        soit 1 s'il y a un mur dans la direction correspondante
        bN est le chiffre des unité, BE des dizaine, etc...
        le code obtenu permet d'obtenir l'indice du caractère semi-graphique
        correspondant à la carte dans la liste listeCartes au début de ce fichier
        paramètre la carte
        retourne un entier indice du caractère semi-graphique de la carte
        """
        res = b''
        for card in 'OSEN':
            if self[card]:
                res += b'1'
            else:
                res += b'0'
        res = int(res,2)
        return res


    def decoderMurs(self,code):
        """
        positionne les murs d'une carte en fonction du code décrit précédemment
        paramètres la carte
                code un entier codant les murs d'une carte
        Cette fonction modifie la carte mais ne retourne rien
        """    
        for e,card in zip(reversed(range(4)),'OSEN'):
            if 2**e & code:
                code -= 2**e
                self[card] = True
            else:
                self[card] = False


    def toChar(self):
        """
        fournit le caractère semi graphique correspondant à la carte (voir la variable listeCartes au début de ce script)
        paramètres la carte
        """
        return listeCartes[self.coderMurs()]


    def passageNord(self,carte2):
        """
        On suppose que la carte2 est placée au nord de la carte1 et indique
        s'il y a un passage entre ces deux cartes en passant par le nord
        paramètres carte1 et carte2 deux cartes
        résultat un booléen
        """
        return not carte2["S"] and not self["N"]

    def passageSud(self,carte2):
        """
        On suppose que la carte2 est placée au sud de la carte1 et indique
        s'il y a un passage entre ces deux cartes en passant par le sud
        paramètres carte1 et carte2 deux cartes
        résultat un booléen
        """
        return carte2.passageNord(self)

    def passageOuest(self,carte2):
        """
        On suppose que la carte2 est placée à l'ouest de la carte1 et indique
        s'il y a un passage entre ces deux cartes en passant par l'ouest
        paramètres carte1 et carte2 deux cartes
        résultat un booléen
        """
        return not carte2["E"] and not self["O"]

    def passageEst(self,carte2):
        """
        suppose que la carte2 est placée à l'est de la carte1 et indique
        s'il y a un passage entre ces deux cartes en passant par l'est
        paramètres carte1 et carte2 deux cartes
        résultat un booléen    
        """
        return carte2.passageOuest(self)

    



def checkangle(code):
    """
    retourne un boléen qui indique si le code indiqué correspond à un angle
    fonction faite pour le plaisir
    """
    return not (code & 1 and code & 2) and not(code & 4 and code & 8) 


if __name__ == "__main__":
    c = Carte(False,True,False,True)
    cpt = 0
    print(c) # :)
    c.decoderMurs(14)

#6,14,14,12,7,7,14,13,7,11,13,13,3,11,11,9
