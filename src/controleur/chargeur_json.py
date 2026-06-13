# -----------------------------------------------------------------------------
# --- chargeur_json.py ---------------------------------------------------------
# -----------------------------------------------------------------------------
# Classe ChargeurJSON pour le jeu Néonaure.
#
# Cette classe permet de charger une grille depuis un fichier JSON.
#
# Dans le fichier JSON :
#   - chaque clé correspond à un motif
#   - chaque motif contient une liste de cases
#   - chaque case est représentée par [x, y, valeur]
#
# Exemple :
#   "motif1": [[0, 0, 0], [1, 0, 2], [0, 1, 0]]
#
# x correspond à la colonne.
# y correspond à la ligne.
# valeur vaut 0 si la case est vide.
# -----------------------------------------------------------------------------

import json

from src.modele.grille import Grille
from src.modele.motif import Motif


# -----------------------------------------------------------------------------
# --- classe ChargeurJSON ------------------------------------------------------
# -----------------------------------------------------------------------------
class ChargeurJSON:
    """
    Classe permettant de charger une grille depuis un fichier JSON.
    """

    # -------------------------------------------------------------------------
    # --- chargement d'une grille ----------------------------------------------
    # -------------------------------------------------------------------------
    def charger(self, chemin: str) -> Grille:
        """
        Charge une grille depuis un fichier JSON.
        Renvoie un objet Grille.
        """

        # ouverture du fichier JSON
        with open(chemin, "r", encoding="utf-8") as fichier:
            donnees = json.load(fichier)

        # variables pour trouver la taille de la grille
        max_x: int = 0
        max_y: int = 0

        # parcours des cases pour trouver la plus grande colonne et la plus grande ligne
        for cases_motif in donnees.values():
            for x, y, valeur in cases_motif:
                max_x = max(max_x, x)
                max_y = max(max_y, y)

        # création de la grille
        # max_y + 1 = nombre de lignes
        # max_x + 1 = nombre de colonnes
        grille = Grille(max_y + 1, max_x + 1)

        # identifiant du motif
        identifiant: int = 1

        # parcours des motifs du fichier JSON
        for cases_motif in donnees.values():

            # création d'un motif
            motif = Motif(identifiant)

            # parcours des cases du motif
            for x, y, valeur in cases_motif:

                # récupération de la case déjà présente dans la grille
                case = grille.get_case(x, y)

                # ajout de la valeur dans la case
                case.valeur = valeur

                # si la valeur est différente de 0, la case est donnée au départ
                # donc elle devient fixe
                if valeur != 0:
                    case.rendre_fixe()

                # ajout de la case dans le motif
                motif.ajouter_case(case)

            # ajout du motif dans la grille
            grille.ajouter_motif(motif)

            # passage à l'identifiant suivant
            identifiant += 1

        return grille