#!/usr/bin/python3
import unittest
import sys
import copy
from unittest.mock import patch

from listeJoueurs import ListeJoueurs
from joueur import Joueur


class TestListeJoueurs(unittest.TestCase):
    def setUp(self):
        self.liste_noms = [["test1", "test2", "test3", "test4"],
                           ["essai2", "essai4"]]

    def test_Joueur(self):
        for noms in self.liste_noms:
            liste_joueurs = ListeJoueurs(noms)
            jo = Joueur(noms[0])
            nbj = liste_joueurs.getNbJoueurs()
            self.assertEqual(nbj, len(noms), "La liste de joueur crée à partir de " + str(noms) + " devrait contenir " +
                             str(len(noms)) + " joueurs mais la fonction getNbJoueurs retourne " + str(nbj) +
                             "\nCela peut provenir des fonctions ListeJoueurs ou getNbJoueurs")
            jc = liste_joueurs.getJoueurCourant()
            self.assertEqual(jc.getNom(), noms[0], "La liste de joueur crée à partir de " + str(
                noms) + " devrait avoir pour joueur courant " +
                             str(noms[0]) + " mais la fonction getJoueurCourant retourne " + str(jc.getNom()) +
                             "\nCela peut provenir des fonctions ListeJoueurs ou getJoueurCourant")

    def test_ajouterJoueur(self):
        for noms in self.liste_noms:
            liste_joueurs = ListeJoueurs([])
            cpt = 0
            nbj = liste_joueurs.getNbJoueurs()
            self.assertEqual(nbj, cpt, "La liste de joueur crée à partir de [] devrait contenir aucun joueur mais " +
                             "la fonction getNbJoueurs retourne " + str(nbj) +
                             "\nCela peut provenir des fonctions ListeJoueurs ou getNbJoueurs")
            for nom in noms:
                cpt += 1
                liste_joueurs.ajouterJoueur(Joueur(nom))
                nbj = liste_joueurs.getNbJoueurs()
                self.assertEqual(nbj, cpt, "La liste de joueur devrait contenir " + str(cpt) + " joueur(s) mais " +
                                 "la fonction getNbJoueurs retourne " + str(nbj) +
                                 "\nCela peut provenir des fonctions  ajouterJoueur ou getNbJoueurs")

    def test_changerJoueurCourant(self):
        for noms in self.liste_noms:
            liste_joueurs = ListeJoueurs(noms)
            taille = len(noms)
            for i in range(6):
                jca = Joueur(noms[i % taille])
                jc = liste_joueurs.getJoueurCourant()
                self.assertEqual(jc.getNom(), noms[i % taille],
                                 "Le joueur courant de la liste joueur créée à partir de " + str(
                                     noms) + " au bout de " + str(i) +
                                 " tour(s) devrait être " + str(
                                     noms[i % taille]) + " mais la fonction getJoueurCourant retourne " + str(
                                     jc.getNom()) +
                                 "\nCela peut provenir des fonctions ListeJoueurs, getJoueurCourant ou changerJoueurCourant")
                liste_joueurs.changerJoueurCourant()

    def test_numJoueurCourant(self):
        for noms in self.liste_noms:
            liste_joueurs = ListeJoueurs(noms)
            taille = len(noms)
            for i in range(6):
                njc = liste_joueurs.numJoueurCourant()
                self.assertEqual(njc, i % taille + 1,
                                 "Le numero du joueur courant de la liste joueur créée à partir de " + str(
                                     noms) + " au bout de " + str(i) +
                                 " tour(s) devrait être " + str(
                                     i % taille + 1) + " mais la fonction getJoueurCourant retourne " + str(njc) +
                                 "\nCela peut provenir des fonctions ListeJoueurs, numJoueurCourant ou changerJoueurCourant")
                liste_joueurs.changerJoueurCourant()

    def test_nomJoueurCourant(self):
        for noms in self.liste_noms:
            liste_joueurs = ListeJoueurs(noms)
            taille = len(noms)
            for i in range(6):
                njc = liste_joueurs.nomJoueurCourant()
                self.assertEqual(njc, noms[i % taille],
                                 "Le nom du joueur courant de la liste joueur créée à partir de " + str(
                                     noms) + " au bout de " + str(i) +
                                 " tour(s) devrait être " + str(
                                     noms[i % taille]) + " mais la fonction getJoueurCourant retourne " + str(njc) +
                                 "\nCela peut provenir des fonctions ListeJoueurs, nomJoueurCourant ou changerJoueurCourant")
                liste_joueurs.changerJoueurCourant()

    def test_distribuerTresors(self):
        def recolter_tresor(jo):
            j = copy.deepcopy(jo)
            res = []
            while j.getNbTresorsRestants() != 0:
                res.append(j.prochainTresor())
                j.tresorTrouve()
            return res

        for noms in self.liste_noms:
            liste_joueurs = ListeJoueurs(noms)
            liste_joueurs.distribuerTresors(12, 3)
            recolte = []
            for i in range(len(noms)):
                tresors = recolter_tresor(liste_joueurs.getJoueurCourant())
                self.assertEqual(len(tresors), 3,
                                 "La distribution de 3 trésors compris entre 1 et 12 pour une liste de joueur créée à partir " +
                                 str(
                                     noms) + " devrait donner 3 trésors à chaque joueur or votre fonction a donné " + str(
                                     len(tresors)) +
                                 " au joueur " + str(i + 1) +
                                 "\nCela peut provenir des fonctions ListeJoueurs, distribuerTresors ou getJoueurCourant")
                recolte.extend(tresors)
                liste_joueurs.changerJoueurCourant()
            recolte.sort()
            for i in range(len(recolte) - 1):
                self.assertIn(recolte[i], list(range(1, 13)),
                              "La distribution de 3 trésors compris entre 1 et 12 pour une liste de joueur créée à partir " +
                              str(noms) + " a distribué un trésor inconnu " + str(recolte[i]))
                self.assertTrue(recolte[i] != recolte[i + 1],
                                "La distribution de 3 trésors compris entre 1 et 12 pour une liste de joueur créée à partir " +
                                str(noms) + " a distribué deux fois le même trésor " + str(recolte[i]))
            self.assertIn(recolte[len(recolte) - 1], list(range(1, 13)),
                          "La distribution de 3 trésors compris entre 1 et 12 pour une liste de joueur créée à partir " +
                          str(noms) + " a distribué un trésor inconnu " + str(recolte[len(recolte) - 1]))

    def test_joueurCourantTrouveTresor(self):
        for noms in self.liste_noms:
            liste_joueurs = ListeJoueurs(noms)
            liste_joueurs.distribuerTresors(16, 4)
            cpt = 4
            for i in range(4):
                cpt -= 1
                for j in range(len(noms)):
                    jo = copy.deepcopy(liste_joueurs.getJoueurCourant())
                    jo.tresorTrouve()
                    liste_joueurs.joueurCourantTrouveTresor()
                    jo_res = liste_joueurs.getJoueurCourant()
                    nbt = jo_res.getNbTresorsRestants()
                    self.assertEqual(nbt, cpt, "Un joueur qui a trouvé " + str(i + 1) +
                                     " trésor(s) sur 4 devrait en avoir " + str(cpt) +
                                     " à trouver mais la fonction getNbTresorsRestants retourne " + str(nbt) +
                                     "\nCela peut provenir des fonctions ListeJoueurs, changerJoueurCourant, distribuerTresors ou joueurCourantTrouveTresor")
                    # self.assertEqual(jo.nom, jo_res.nom,
                    #                  "Il y a une incohérence entre les fonctions tresorTrouve et joueurCourantTrouveTresor")
                    # self.assertEqual(jo.tresors, jo_res.tresors,
                    #                  "Il y a une incohérence entre les fonctions tresorTrouve et joueurCourantTrouveTresor")
                    liste_joueurs.changerJoueurCourant()

    def test_nbTresorsRestantsJoueur(self):
        for noms in self.liste_noms:
            liste_joueurs = ListeJoueurs(noms)
            liste_joueurs.distribuerTresors(16, 4)
            for i in range(1, len(noms) + 1):
                nbt = liste_joueurs.nbTresorsRestantsJoueur(i)
                self.assertEqual(nbt, 4, "Après avoir distribué 4 trésor à chaque joueur," +
                                 " nbTresorsRestantsJoueur devrait retourner 4 mais elle retourne " + str(nbt) +
                                 " le joueur " + str(i) +
                                 "\nCela peut provenir des fonctions ListeJoueurs, distribuerTresors ou nbTresorsRestantsJoueur")

    def test_joueurCourantAFini(self):
        for noms in self.liste_noms:
            liste_joueurs = ListeJoueurs(noms)
            for i in range(1, len(noms) + 1):
                self.assertTrue(liste_joueurs.joueurCourantAFini(), "Le joueur courant de la liste " +
                                str(
                                    liste_joueurs) + " n'a aucun trésor la fonction joueurCourantAFini devrait retourner True" +
                                "\nCela peut provenir des fonctions ListeJoueurs ou joueurCourantAFini")
                liste_joueurs.changerJoueurCourant()

            liste_joueurs.distribuerTresors(16, 4)
            for i in range(1, len(noms) + 1):
                self.assertFalse(liste_joueurs.joueurCourantAFini(), "Le joueur courant de la liste " +
                                 str(
                                     liste_joueurs) + " a 4 trésors la fonction joueurCourantAFini devrait retourner True" +
                                 "\nCela peut provenir des fonctions distribuerTresors ou joueurCourantAFini")
                liste_joueurs.changerJoueurCourant()


if __name__ == '__main__':
    print("*" * 50)
    print("* ATTENTION! Note importante".ljust(48), "*")
    print("* les tests ne peuvent s'effectuer avant".ljust(48), "*")
    print("* d'avoir implémenté les fonctions ".ljust(48), "*")
    print("*", " " * 10, "- ListeJoueurs".ljust(35), "*")
    print("*", " " * 10, "- getNbJoueurs".ljust(35), "*")
    print("*", " " * 10, "- getJoueurCourant".ljust(35), "*")
    print("*" * 50)
    unittest.main()
