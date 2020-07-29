#!/usr/bin/python3
import unittest
import sys
import copy
from unittest.mock import patch

from carte import Carte

listeCartes_ = ['╬', '╦', '╣', '╗', '╩', '═', '╝', 'Ø', '╠', '╔', '║', 'Ø', '╚', 'Ø', 'Ø', 'Ø']


class TestCarte(unittest.TestCase):
    def setUp(self):
        self.O = 8
        self.S = 4
        self.E = 2
        self.N = 1
        self.liste_cartes = []
        self.liste_cartes_droite = []
        for i in range(16):
            self.liste_cartes.append(
                Carte(i & self.N == self.N, i & self.E == self.E, i & self.S == self.S, i & self.O == self.O))
            self.liste_cartes_droite.append(
                Carte(i & self.O == self.O, i & self.N == self.N, i & self.E == self.E, i & self.S == self.S))

    def test_estValide(self):
        for i in range(16):
            if i in [7, 11, 13, 14, 15]:
                self.assertFalse(self.liste_cartes[i].estValide(), "la carte " + str(self.liste_cartes[i]) +
                                 "ne devrait pas être valide car elle ne possède qu'une ou 0 ouverture")
            else:
                self.assertTrue(self.liste_cartes[i].estValide(), "la carte " + str(self.liste_cartes[i]) +
                                "devrait être valide car elle possède 2, 3 ou 4 ouvertures")

    def test_murNord(self):
        for i in range(13):
            if i not in (7, 11):
                if i & self.N == self.N:
                    self.assertTrue(self.liste_cartes[i].murNord(),
                                    "la carte " + str(self.liste_cartes[i]) + " devrait posséder un mur au nord")
                else:
                    self.assertFalse(self.liste_cartes[i].murNord(), "la carte " + str(
                        self.liste_cartes[i]) + " ne devrait pas posséder de mur au nord")

    def test_murSud(self):
        for i in range(13):
            if i not in (7, 11):
                if i & self.S == self.S:
                    self.assertTrue(self.liste_cartes[i].murSud(),
                                    "la carte " + str(self.liste_cartes[i]) + " devrait posséder un mur au sud")
                else:
                    self.assertFalse(self.liste_cartes[i].murSud(),
                                     "la carte " + str(self.liste_cartes[i]) + " ne devrait pas posséder de mur au sud")

    def test_murOuest(self):
        for i in range(13):
            if i not in (7, 11):
                if i & self.O == self.O:
                    self.assertTrue(self.liste_cartes[i].murOuest(),
                                    "la carte " + str(self.liste_cartes[i]) + " devrait posséder un mur à l'ouest")
                else:
                    self.assertFalse(self.liste_cartes[i].murOuest(), "la carte " + str(
                        self.liste_cartes[i]) + " ne devrait pas posséder de mur à l'ouest")

    def test_murEst(self):
        for i in range(13):
            if i not in (7, 11):
                if i & self.E == self.E:
                    self.assertTrue(self.liste_cartes[i].murEst(),
                                    "la carte " + str(self.liste_cartes[i]) + " devrait posséder un mur à l'est")
                else:
                    self.assertFalse(self.liste_cartes[i].murEst(), "la carte " + str(
                        self.liste_cartes[i]) + " ne devrait pas posséder de mur à l'est")

    def test_listePions(self):
        c1 = Carte(True, False, True, False)
        c2 = Carte(True, False, True, False, pions=[1, 3])
        self.assertEqual(c1.getListePions(), [],
                         "la carte " + str(c1) + " devrait avoir une liste de pions vide\n" +
                         "Le problème vient sans doute de la fonction Carte")
        self.assertEqual(c2.getListePions(), [1, 3],
                         "la carte " + str(c2) + " devrait avoir une liste de pions égale à [1,3]\n" +
                         "Le problème vient sans doute de la fonction Carte lorsque le paramètre pions est instancié à une liste non vide")
        c1.setListePions([1, 2])
        self.assertEqual(c1.getListePions(), [1, 2],
                         "la carte " + str(c1) + " devrait avoir une liste de pions égale à [1,2]\n" +
                         "Le problème vient sans doute de la fonction setListePions")
        c2.setListePions([])
        self.assertEqual(c2.getListePions(), [],
                         "la carte " + str(c2) + " devrait avoir une liste de pions égale à [1,2]\n" +
                         "Le problème vient sans doute de la fonction setListePions")

    def test_getNbPions(self):
        c1 = Carte(True, False, True, False)
        c2 = Carte(True, False, True, False, pions=[1, 3])
        self.assertEqual(c1.getNbPions(), 0,
                         "la carte " + str(c1) + " devrait avoir un nombre de pions égal à 0\n" +
                         "Le problème vient sans doute de la fonction Carte")
        self.assertEqual(c2.getNbPions(), 2,
                         "la carte " + str(c2) + " devrait avoir un nombre de pions égal à 2\n" +
                         "Le problème vient sans doute de la fonction Carte lorsque le paramètre pions est instancié à une liste non vide")

    def test_possede_Pion(self):
        c1 = Carte(True, False, True, False)
        c2 = Carte(True, False, True, False, pions=[1, 3])
        for i in range(1, 5):
            self.assertFalse(c1.possedePion(i),
                             "la carte " + str(c1) + " ne possède pas le pion " + str(i) + "\n" +
                             "Le problème vient sans doute de la fonction Carte ou de la fonction possedePion")
        for i in range(1, 5):
            if i == 1 or i == 3:
                self.assertTrue(c2.possedePion(i),
                                "la carte " + str(c2) + " possède bien le pion " + str(i) + "\n" +
                                "Le problème vient sans doute de la fonction Carte ou de la fonction possedePion")
            else:
                self.assertFalse(c2.possedePion(i),
                                 "la carte " + str(c2) + " ne possède pas le pion " + str(i) + "\n" +
                                 "Le problème vient sans doute de la fonction Carte ou de la fonction possedePion")

    def test_possede_pendre_Pion(self):
        c1 = Carte(True, False, True, False, pions=[1, 3])
        for nb in range(2):
            c1.prendrePion(3)
            for i in range(1, 5):
                if i == 1:
                    self.assertTrue(c1.possedePion(i),
                                    "la carte " + str(c1) + " possède bien le pion " + str(i) + "\n" +
                                    "Le problème vient sans doute de la fonction prendrePion ou de la fonction possedePion")
                else:
                    self.assertFalse(c1.possedePion(i),
                                     "la carte " + str(c1) + " ne possède pas le pion " + str(i) + "\n" +
                                     "Le problème vient sans doute de la fonction prendrePion ou de la fonction possedePion")

    def test_possede_poser_Pion(self):
        c1 = Carte(True, False, True, False)
        c2 = Carte(True, False, True, False, pions=[1, 3])
        c1.poserPion(2)
        for i in range(1, 5):
            if i == 2:
                self.assertTrue(c1.possedePion(i),
                                "la carte " + str(c1) + " possède bien le pion " + str(i) + "\n" +
                                "Le problème vient sans doute de la fonction poserPion ou de la fonction possedePion")
            else:
                self.assertFalse(c1.possedePion(i),
                                 "la carte " + str(c1) + " ne possède pas le pion " + str(i) + "\n" +
                                 "Le problème vient sans doute de la fonction poserPion ou de la fonction possedePion")
        c2.poserPion(4)
        for i in range(1, 5):
            if i == 1 or i == 3 or i == 4:
                self.assertTrue(c2.possedePion(i),
                                "la carte " + str(c2) + " possède bien le pion " + str(i) + "\n" +
                                "Le problème vient sans doute de la fonction poserPion ou de la fonction possedePion")
            else:
                self.assertFalse(c2.possedePion(2),
                                 "la carte " + str(c2) + " ne possède pas le pion " + str(i) + "\n" +
                                 "Le problème vient sans doute de la fonction poserPion ou de la fonction possedePion")

    def test_tournerHoraire(self):
        for i in range(13):
            if i not in (7, 11):
                c = copy.deepcopy(self.liste_cartes[i])
                c.tournerHoraire()
                self.assertEqual(c.murEst(), self.liste_cartes_droite[i].murEst(),
                                 "problème avec la fonction l'appel tournerHoraire(" +
                                 str(self.liste_cartes[i]) +
                                 "\nRésultat obtenu " + str(c))
                self.assertEqual(c.murOuest(), self.liste_cartes_droite[i].murOuest(),
                                 "problème avec la fonction l'appel tournerHoraire(" +
                                 str(self.liste_cartes[i]) +
                                 "\nRésultat obtenu " + str(c))
                self.assertEqual(c.murSud(), self.liste_cartes_droite[i].murSud(),
                                 "problème avec la fonction l'appel tournerHoraire(" +
                                 str(self.liste_cartes[i]) +
                                 "\nRésultat obtenu " + str(c))
                self.assertEqual(c.murNord(), self.liste_cartes_droite[i].murNord(),
                                 "problème avec la fonction l'appel tournerHoraire(" +
                                 str(self.liste_cartes[i]) +
                                 "\nRésultat obtenu " + str(c))

    def test_tournerAntiHoraire(self):
        for i in range(13):
            if i not in (7, 11):
                c = copy.deepcopy(self.liste_cartes_droite[i])
                c.tournerAntiHoraire()
                self.assertEqual(c.murEst(), self.liste_cartes[i].murEst(),
                                 "problème avec la fonction l'appel tournerAntiHoraire(" +
                                 str(self.liste_cartes_droite[i]) +
                                 "\nRésultat obtenu " + str(c))
                self.assertEqual(c.murOuest(), self.liste_cartes[i].murOuest(),
                                 "problème avec la fonction l'appel tournerAntiHoraire(" +
                                 str(self.liste_cartes_droite[i]) +
                                 "\nRésultat obtenu " + str(c))
                self.assertEqual(c.murSud(), self.liste_cartes[i].murSud(),
                                 "problème avec la fonction l'appel tournerAntiHoraire(" +
                                 str(self.liste_cartes_droite[i]) +
                                 "\nRésultat obtenu " + str(c))
                self.assertEqual(c.murNord(), self.liste_cartes[i].murNord(),
                                 "problème avec la fonction l'appel tournerAntiHoraire(" +
                                 str(self.liste_cartes_droite[i]) +
                                 "\nRésultat obtenu " + str(c))

    def test_getTresor(self):
        c1 = Carte(True, False, True, False)
        c2 = Carte(True, False, True, False, 10)
        self.assertEqual(c1.getTresor(), 0,
                         "la carte " + str(c1) + " ne possède aucun trésor => valeur attendue 0\n" +
                         "Le problème vient sans doute de la fonction Carte ou de la fonction getTresor")
        self.assertEqual(c2.getTresor(), 10,
                         "la carte " + str(c2) + " possède le trésor 10 => valeur attendue 10\n" +
                         "Le problème vient sans doute de la fonction Carte ou de la fonction getTresor")

    def test_getTresor_mettreTresor(self):
        c1 = Carte(True, False, True, False)
        c2 = Carte(True, False, True, False, 10)
        self.assertEqual(c1.mettreTresor(5), 0,
                         "la carte " + str(c1) + " ne possèdait aucun trésor => valeur attendue 0\n" +
                         "Le problème vient sans doute de la fonction Carte ou de la fonction mettreTresor")
        self.assertEqual(c1.getTresor(), 5, "la carte " + str(c1) + " doit posséder le trésor 5\n" +
                         "Le problème vient sans doute de la fonction mettreTresor ou de la fonction getTresor")
        self.assertEqual(c2.mettreTresor(7), 10,
                         "la carte " + str(c2) + " possédait le trésor 10 => valeur attendue 10\n" +
                         "Le problème vient sans doute de la fonction Carte ou de la fonction mettreTresor")
        self.assertEqual(c2.getTresor(), 7, "la carte " + str(c2) + " doit posséder le trésor 7\n" +
                         "Le problème vient sans doute de la fonction mettreTresor ou de la fonction getTresor")

    def test_getTresor_prendreTresor(self):
        c1 = Carte(True, False, True, False)
        c2 = Carte(True, False, True, False, 10)
        self.assertEqual(c1.prendreTresor(), 0,
                         "la carte " + str(c1) + " ne possèdait aucun trésor => valeur attendue 0\n" +
                         "Le problème vient sans doute de la fonction Carte ou de la fonction prendreTresor")
        self.assertEqual(c1.getTresor(), 0, "la carte " + str(c1) + " ne devrait plus posséder de trésor \n" +
                         "Le problème vient sans doute de la fonction prendreTresor ou de la fonction getTresor")
        self.assertEqual(c2.prendreTresor(), 10,
                         "la carte " + str(c2) + " possédait le trésor 10 => valeur attendue 10\n" +
                         "Le problème vient sans doute de la fonction Carte ou de la fonction prendreTresor")
        self.assertEqual(c2.getTresor(), 0, "la carte " + str(c2) + " ne devrait plus posséder de trésor \n" +
                         "Le problème vient sans doute de la fonction prendreTresor ou de la fonction getTresor")

    def test_coderMurs(self):
        for i in range(16):
            res = self.liste_cartes[i].coderMurs()
            self.assertEqual(res, i, "la carte " + str(self.liste_cartes[i]) +
                             " devrait avoir pour code " + str(i) + " mais coderMur a retourné " + str(res))

    def test_decoderMurs(self):
        c = Carte(True, True, True, True)
        for i in range(16):
            c.decoderMurs(i)
            self.assertEqual(c.murNord(), self.liste_cartes[i].murNord(), "le resultat de decoderMur avec le code " + str(i) +
                             " aurait du donner " + str(self.liste_cartes[i]) + " mais on a obtenu " + str(c))
            self.assertEqual(c.murEst(), self.liste_cartes[i].murEst(),
                             "le resultat de decoderMur avec le code " + str(i) +
                             " aurait du donner " + str(self.liste_cartes[i]) + " mais on a obtenu " + str(c))
            self.assertEqual(c.murSud(), self.liste_cartes[i].murSud(),
                             "le resultat de decoderMur avec le code " + str(i) +
                             " aurait du donner " + str(self.liste_cartes[i]) + " mais on a obtenu " + str(c))
            self.assertEqual(c.murOuest(), self.liste_cartes[i].murOuest(),
                             "le resultat de decoderMur avec le code " + str(i) +
                             " aurait du donner " + str(self.liste_cartes[i]) + " mais on a obtenu " + str(c))

    def test_toChar(self):
        for i in range(16):
            carac = self.liste_cartes[i].toChar()
            self.assertEqual(carac, listeCartes_[i], "la carte " + str(self.liste_cartes[i]) +
                             " devrait avoir pour caractère " + listeCartes_[i] + " mais toChar retourne " + str(
                carac))

    def message_passage(self, direction, existe, c1, c2):
        commun = " passage direction " + direction + " entre " + str(c1) + " et " + str(
            c2) + " mais la fonction passage" + \
                 direction + " "
        if existe:
            return "il existe un" + commun + "ne le trouve pas"
        else:
            return "il n'existe pas de" + commun + "en trouve un"

    def test_passageNord(self):
        for i in range(13):
            if i not in (7, 11):
                for j in range(13):
                    if j not in (7, 11):
                        passage = i & self.N == 0 and j & self.S == 0
                        self.assertEqual(self.liste_cartes[i].passageNord(self.liste_cartes[j]), passage,
                                         self.message_passage("Nord", passage, self.liste_cartes[i],
                                                              self.liste_cartes[j]))

    def test_passageSud(self):
        for i in range(13):
            if i not in (7, 11):
                for j in range(13):
                    if j not in (7, 11):
                        passage = i & self.S == 0 and j & self.N == 0
                        self.assertEqual(self.liste_cartes[i].passageSud(self.liste_cartes[j]), passage,
                                         self.message_passage("Sud", passage, self.liste_cartes[i],
                                                              self.liste_cartes[j]))

    def test_passageEst(self):
        for i in range(13):
            if i not in (7, 11):
                for j in range(13):
                    if j not in (7, 11):
                        passage = i & self.E == 0 and j & self.O == 0
                        self.assertEqual(self.liste_cartes[i].passageEst(self.liste_cartes[j]), passage,
                                         self.message_passage("Est", passage, self.liste_cartes[i],
                                                              self.liste_cartes[j]))

    def test_passageOuest(self):
        for i in range(13):
            if i not in (7, 11):
                for j in range(13):
                    if j not in (7, 11):
                        passage = i & self.O == 0 and j & self.E == 0
                        self.assertEqual(self.liste_cartes[i].passageOuest(self.liste_cartes[j]), passage,
                                         self.message_passage("Ouest", passage, self.liste_cartes[i],
                                                              self.liste_cartes[j]))


if __name__ == '__main__':
    unittest.main()
