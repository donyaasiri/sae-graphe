from modele.case import Case


class Motif:
    """
    Représente un motif de la grille.

    Un motif est un groupe de cases.
    Si un motif contient N cases, il doit contenir les valeurs de 1 à N.
    """

    def __init__(self, identifiant: int):
        self.__identifiant = identifiant
        self.__cases = []

    @property
    def identifiant(self) -> int:
        return self.__identifiant

    @property
    def cases(self) -> list:
        return self.__cases

    def ajouter_case(self, case: Case) -> None:
        self.__cases.append(case)

    def taille(self) -> int:
        return len(self.__cases)

    def contient_valeur(self, valeur: int) -> bool:
        for case in self.__cases:
            if case.valeur == valeur:
                return True
        return False

    def est_valide(self) -> bool:
        """
        Vérifie que le motif respecte les règles :
        - pas de doublon
        - valeurs entre 1 et N
        - les cases vides, valeur 0, sont acceptées pendant le jeu
        """
        valeurs_vues = set()
        taille = self.taille()

        for case in self.__cases:
            valeur = case.valeur

            if valeur == 0:
                continue

            if valeur < 1 or valeur > taille:
                return False

            if valeur in valeurs_vues:
                return False

            valeurs_vues.add(valeur)

        return True

    def est_complet(self) -> bool:
        if not self.est_valide():
            return False

        for case in self.__cases:
            if case.est_vide():
                return False

        return True

    def __repr__(self) -> str:
        return f"Motif(id={self.__identifiant}, taille={self.taille()})"
