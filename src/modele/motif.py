# -----------------------------------------------------------------------------
# --- import -------------------------------------------------------------------
# -----------------------------------------------------------------------------
# La classe Motif utilise la classe Case.
# Un motif est composé de plusieurs cases.
# -----------------------------------------------------------------------------

from src.modele.case import Case


# -----------------------------------------------------------------------------
# --- classe Motif -------------------------------------------------------------
# -----------------------------------------------------------------------------
# Un motif représente une zone de la grille.
# Si un motif contient N cases, alors les valeurs possibles sont de 1 à N.
# -----------------------------------------------------------------------------

class Motif:
    """
    Représente un motif de la grille.

    Un motif est un groupe de cases.
    Si un motif contient N cases, il doit contenir les valeurs de 1 à N.
    """

    # -------------------------------------------------------------------------
    # --- constructeur ---------------------------------------------------------
    # -------------------------------------------------------------------------
    def __init__(self, identifiant: int) -> None:
        # identifiant du motif
        self.__identifiant: int = identifiant

        # liste des cases appartenant au motif
        self.__cases: list[Case] = []

    # -------------------------------------------------------------------------
    # --- accesseurs -----------------------------------------------------------
    # -------------------------------------------------------------------------

    # retourne l'identifiant du motif
    @property
    def identifiant(self) -> int:
        return self.__identifiant

    # retourne la liste des cases du motif
    @property
    def cases(self) -> list:
        return self.__cases

    # -------------------------------------------------------------------------
    # --- méthodes -------------------------------------------------------------
    # -------------------------------------------------------------------------

    # ajoute une case dans le motif
    def ajouter_case(self, case: Case) -> None:
        self.__cases.append(case)

    # retourne le nombre de cases dans le motif
    def taille(self) -> int:
        return len(self.__cases)

    # vérifie si une valeur est déjà présente dans le motif
    def contient_valeur(self, valeur: int) -> bool:
        for case in self.__cases:
            if case.valeur == valeur:
                return True

        return False

    # vérifie que le motif respecte les règles
    def est_valide(self) -> bool:
        """
        Vérifie que le motif respecte les règles :
        - pas de doublon
        - valeurs entre 1 et N
        - les cases vides, valeur 0, sont acceptées pendant le jeu
        """

        # ensemble des valeurs déjà rencontrées dans le motif
        valeurs_vues = set()

        # taille du motif : si taille = N, les valeurs doivent aller de 1 à N
        taille = self.taille()

        # parcours de toutes les cases du motif
        for case in self.__cases:
            valeur = case.valeur

            # une case vide est autorisée pendant la partie
            if valeur == 0:
                continue

            # la valeur doit être comprise entre 1 et la taille du motif
            if valeur < 1 or valeur > taille:
                return False

            # la valeur ne doit pas déjà être présente dans le motif
            if valeur in valeurs_vues:
                return False

            # on mémorise la valeur
            valeurs_vues.add(valeur)

        return True

    # vérifie si le motif est complet
    def est_complet(self) -> bool:

        # si le motif n'est pas valide, il ne peut pas être complet
        if not self.est_valide():
            return False

        # toutes les cases doivent être remplies
        for case in self.__cases:
            if case.est_vide():
                return False

        return True

    # affichage de l'objet dans la console
    def __repr__(self) -> str:
        return f"Motif(id={self.__identifiant}, taille={self.taille()})"


# -----------------------------------------------------------------------------
# --- main de test -------------------------------------------------------------
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    # création de quelques cases
    case0 = Case(0, 0, 1, True)
    case1 = Case(1, 0, 2, True)
    case2 = Case(2, 0, 0, False)

    # création d'un motif
    motif0 = Motif(1)

    # ajout des cases dans le motif
    motif0.ajouter_case(case0)
    motif0.ajouter_case(case1)
    motif0.ajouter_case(case2)

    # affichage du motif
    print(motif0)

    # vérification des règles du motif
    print(motif0.est_valide())

    # vérification si le motif est complet
    print(motif0.est_complet())

    # modification de la case vide
    case2.valeur = 3

    # nouvelle vérification
    print(motif0.est_valide())
    print(motif0.est_complet())