# -----------------------------------------------------------------------------
# --- grille.py ----------------------------------------------------------------
# -----------------------------------------------------------------------------
# Classe Grille pour le jeu Néonaure.
# La grille contient :
#   - un nombre de lignes
#   - un nombre de colonnes
#   - des cases
#   - des motifs
# -----------------------------------------------------------------------------

from src.modele.case import Case
from src.modele.motif import Motif


# -----------------------------------------------------------------------------
# --- classe Grille -------------------------------------------------------------
# -----------------------------------------------------------------------------
class Grille:
    """
    Représente la grille complète du jeu.
    Elle contient les cases et les motifs.
    """

    # -------------------------------------------------------------------------
    # --- constructeur ---------------------------------------------------------
    # -------------------------------------------------------------------------
    def __init__(self, nb_lignes: int, nb_colonnes: int) -> None:
        # dimensions de la grille
        self.__nb_lignes: int = nb_lignes
        self.__nb_colonnes: int = nb_colonnes

        # liste des cases sous forme de tableau à deux dimensions
        self.__cases: list = []

        # liste des motifs de la grille
        self.__motifs: list = []

        # création des cases vides
        for y in range(nb_lignes):
            ligne = []

            for x in range(nb_colonnes):
                ligne.append(Case(x, y, 0, False))

            self.__cases.append(ligne)

    # -------------------------------------------------------------------------
    # --- accesseurs -----------------------------------------------------------
    # -------------------------------------------------------------------------
    @property
    def nb_lignes(self) -> int:
        return self.__nb_lignes

    @property
    def nb_colonnes(self) -> int:
        return self.__nb_colonnes

    @property
    def motifs(self) -> list:
        return self.__motifs

    # -------------------------------------------------------------------------
    # --- accès aux cases -------------------------------------------------------
    # -------------------------------------------------------------------------
    def get_case(self, x: int, y: int) -> Case:
        """
        Renvoie la case située à la colonne x et à la ligne y.
        """
        return self.__cases[y][x]

    def set_case(self, x: int, y: int, case: Case) -> None:
        """
        Remplace la case située à la colonne x et à la ligne y.
        """
        self.__cases[y][x] = case

    def set_valeur(self, x: int, y: int, valeur: int) -> None:
        """
        Modifie la valeur d'une case.
        """
        self.get_case(x, y).valeur = valeur

    # -------------------------------------------------------------------------
    # --- gestion des motifs ---------------------------------------------------
    # -------------------------------------------------------------------------
    def ajouter_motif(self, motif: Motif) -> None:
        """
        Ajoute un motif à la grille.
        """
        self.__motifs.append(motif)

    def trouver_motif_de_case(self, case_recherchee: Case):
        """
        Renvoie le motif auquel appartient une case.
        Renvoie None si la case n'est dans aucun motif.
        """
        for motif in self.__motifs:
            for case in motif.cases:
                if case is case_recherchee:
                    return motif

        return None

    # -------------------------------------------------------------------------
    # --- vérifications simples ------------------------------------------------
    # -------------------------------------------------------------------------
    def est_complete(self) -> bool:
        """
        Vérifie si toutes les cases de la grille sont remplies.
        """
        for y in range(self.__nb_lignes):
            for x in range(self.__nb_colonnes):
                if self.get_case(x, y).est_vide():
                    return False

        return True

    def toutes_les_cases(self) -> list:
        """
        Renvoie toutes les cases de la grille dans une seule liste.
        """
        resultat = []

        for y in range(self.__nb_lignes):
            for x in range(self.__nb_colonnes):
                resultat.append(self.get_case(x, y))

        return resultat

    # -------------------------------------------------------------------------
    # --- représentation -------------------------------------------------------
    # -------------------------------------------------------------------------
    def __repr__(self) -> str:
        return f"Grille({self.__nb_lignes}x{self.__nb_colonnes})"


# -----------------------------------------------------------------------------
# --- test rapide --------------------------------------------------------------
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    print("--- test de la classe Grille ---")

    # création d'une grille 3 x 3
    grille = Grille(3, 3)

    # modification d'une case
    grille.set_valeur(0, 0, 1)

    # affichage
    print(grille)
    print(grille.get_case(0, 0))
    print("Grille complète :", grille.est_complete())