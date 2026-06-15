# -----------------------------------------------------------------------------
# --- solveur.py ---------------------------------------------------------------
# -----------------------------------------------------------------------------
# Classe Solveur pour le jeu Néonaure.
#
# Cette classe permet de résoudre automatiquement une grille.
#
# Le solveur utilise une méthode de retour arrière :
#   - il cherche une case vide
#   - il essaye les valeurs possibles
#   - si la valeur respecte les règles, il continue
#   - si ça bloque, il revient en arrière
# -----------------------------------------------------------------------------

from src.modele.regles_jeu import ReglesJeu
from src.modele.grille import Grille
from src.modele.case import Case


# -----------------------------------------------------------------------------
# --- classe Solveur -----------------------------------------------------------
# -----------------------------------------------------------------------------
class Solveur:
    """
    Classe permettant de résoudre une grille de Néonaure.
    """

    # -------------------------------------------------------------------------
    # --- résolution de la grille ----------------------------------------------
    # -------------------------------------------------------------------------
    def resoudre(self, grille: Grille) -> bool:
        """
        Résout la grille avec un algorithme de backtracking.
        Renvoie True si une solution est trouvée.
        Renvoie False sinon.
        """

        # recherche d'une case vide dans la grille
        case_vide = self.trouver_case_vide(grille)

        # s'il n'y a plus de case vide, la grille est résolue
        if case_vide is None:
            return True

        # récupération de la position de la case vide
        x: int = case_vide.x
        y: int = case_vide.y

        # recherche du motif auquel appartient la case
        motif = grille.trouver_motif_de_case(case_vide)

        # si la case n'a pas de motif, on essaye les valeurs de 1 à 8
        if motif is None:
            valeurs_possibles = range(1, 9)

        # sinon, on essaye les valeurs de 1 jusqu'à la taille du motif
        else:
            valeurs_possibles = range(1, motif.taille() + 1)

        # test des valeurs possibles
        for valeur in valeurs_possibles:

            # vérification des règles du jeu
            if ReglesJeu.valeur_possible(grille, x, y, valeur):

                # on place temporairement la valeur
                case_vide.valeur = valeur

                # appel récursif pour continuer à résoudre la grille
                if self.resoudre(grille):
                    return True

                # si la suite ne marche pas, on annule la valeur
                case_vide.valeur = 0

        # aucune valeur ne fonctionne pour cette case
        return False

    # -------------------------------------------------------------------------
    # --- recherche d'une case vide --------------------------------------------
    # -------------------------------------------------------------------------
    def trouver_case_vide(self, grille: Grille) -> Case | None:
        """
        Cherche une case vide et modifiable dans la grille.
        Renvoie la case trouvée.
        Renvoie None si aucune case vide n'est trouvée.
        """

        # parcours de toutes les cases de la grille
        for case in grille.toutes_les_cases():

            # on cherche une case vide qui n'est pas fixe
            if case.est_vide() and not case.fixe:
                return case

        return None

