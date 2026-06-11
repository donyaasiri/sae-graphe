from controleur.chargeur_json import ChargeurJSON
from controleur.sauvegarde_json import SauvegardeJSON
from modele.regles_jeu import ReglesJeu
from controleur.solveur import Solveur


class Controleur:
    def __init__(self):
        self.grille = None
        self.chargeur = ChargeurJSON()
        self.sauvegarde = SauvegardeJSON()
        self.solveur = Solveur()

    def charger_grille(self, chemin):
        self.grille = self.chargeur.charger(chemin)
        return self.grille

    def sauvegarder_grille(self, chemin):
        if self.grille is None:
            return False

        return self.sauvegarde.sauvegarder(self.grille, chemin)

    def modifier_case(self, x, y, valeur):
        if self.grille is None:
            return False

        case = self.grille.get_case(x, y)

        if case.fixe:
            return False

        if not ReglesJeu.valeur_possible(self.grille, x, y, valeur):
            return False

        case.valeur = valeur
        return True

    def verifier_grille(self):
        if self.grille is None:
            return False

        return ReglesJeu.verifier_grille(self.grille)

    def resoudre_grille(self):
        if self.grille is None:
            return False

        return self.solveur.resoudre(self.grille)

    def get_grille(self):
        return self.grille