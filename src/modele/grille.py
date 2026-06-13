from modele.case import Case
from modele.motif import Motif


class Grille:
    """
    Représente la grille complète du jeu.
    Elle contient les cases et les motifs.
    """

    def __init__(self, nb_lignes: int, nb_colonnes: int):
        self.__nb_lignes = nb_lignes
        self.__nb_colonnes = nb_colonnes
        self.__cases = []
        self.__motifs = []

        for y in range(nb_lignes):
            ligne = []
            for x in range(nb_colonnes):
                ligne.append(Case(x, y, 0, False))
            self.__cases.append(ligne)

    @property
    def nb_lignes(self) -> int:
        return self.__nb_lignes

    @property
    def nb_colonnes(self) -> int:
        return self.__nb_colonnes

    @property
    def motifs(self) -> list:
        return self.__motifs

    def get_case(self, x: int, y: int) -> Case:
        return self.__cases[y][x]

    def set_case(self, x: int, y: int, case: Case) -> None:
        self.__cases[y][x] = case

    def set_valeur(self, x: int, y: int, valeur: int) -> None:
        self.get_case(x, y).valeur = valeur

    def ajouter_motif(self, motif: Motif) -> None:
        self.__motifs.append(motif)

    def est_complete(self) -> bool:
        for y in range(self.__nb_lignes):
            for x in range(self.__nb_colonnes):
                if self.get_case(x, y).est_vide():
                    return False
        return True

    def trouver_motif_de_case(self, case_recherchee: Case):
        for motif in self.__motifs:
            for case in motif.cases:
                if case is case_recherchee:
                    return motif
        return None

    def toutes_les_cases(self) -> list:
        resultat = []

        for y in range(self.__nb_lignes):
            for x in range(self.__nb_colonnes):
                resultat.append(self.get_case(x, y))

        return resultat

    def __repr__(self) -> str:
        return f"Grille({self.__nb_lignes}x{self.__nb_colonnes})"