import json

from modele.grille import Grille
from modele.motif import Motif


class ChargeurJSON:
    def charger(self, chemin):
        with open(chemin, "r", encoding="utf-8") as fichier:
            donnees = json.load(fichier)

        max_x = 0
        max_y = 0

        for cases_motif in donnees.values():
            for x, y, valeur in cases_motif:
                max_x = max(max_x, x)
                max_y = max(max_y, y)

        grille = Grille(max_y + 1, max_x + 1)

        identifiant = 1

        for cases_motif in donnees.values():
            motif = Motif(identifiant)

            for x, y, valeur in cases_motif:
                case = grille.get_case(x, y)
                case.valeur = valeur

                if valeur != 0:
                    case.rendre_fixe()

                motif.ajouter_case(case)

            grille.ajouter_motif(motif)
            identifiant += 1

        return grille