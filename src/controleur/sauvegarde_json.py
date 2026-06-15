# -----------------------------------------------------------------------------
# --- sauvegarde_json.py -------------------------------------------------------
# -----------------------------------------------------------------------------
# Classe SauvegardeJSON pour le jeu Néonaure.
#
# Cette classe permet de sauvegarder une grille dans un fichier JSON.
#
# Dans le fichier JSON :
#   - chaque motif devient une clé : "motif1", "motif2", ...
#   - chaque case est sauvegardée sous la forme [x, y, valeur]
#
# Exemple :
#   "motif1": [[0, 0, 0], [1, 0, 2], [0, 1, 0]]
# -----------------------------------------------------------------------------

import json

from src.modele.grille import Grille


# -----------------------------------------------------------------------------
# --- classe SauvegardeJSON ----------------------------------------------------
# -----------------------------------------------------------------------------
class SauvegardeJSON:
    """
    Classe permettant de sauvegarder une grille dans un fichier JSON.
    """

    # -------------------------------------------------------------------------
    # --- sauvegarde d'une grille ----------------------------------------------
    # -------------------------------------------------------------------------
    def sauvegarder(self, grille: Grille, chemin: str) -> bool:
        """
        Sauvegarde une grille dans un fichier JSON.
        """

        # dictionnaire qui contiendra toutes les données à écrire dans le JSON
        donnees: dict = {}

        # parcours de tous les motifs de la grille
        for motif in grille.motifs:

            # création du nom du motif dans le fichier JSON
            nom_motif: str = f"motif{motif.identifiant}"

            # création de la liste des cases du motif
            donnees[nom_motif] = []

            # parcours des cases du motif
            for case in motif.cases:

                # ajout de la case sous forme [x, y, valeur]
                donnees[nom_motif].append([
                    case.x,
                    case.y,
                    case.valeur
                ])

        # écriture des données dans le fichier JSON
        with open(chemin, "w", encoding="utf-8") as fichier:
            json.dump(donnees, fichier, indent=4)

        return True


