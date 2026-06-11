# -----------------------------------------------------------------------------
# --- classe Case --------------------------------------------------------------
# -----------------------------------------------------------------------------
# Une case représente une cellule de la grille.
# Elle possède une position, une valeur et un état fixe ou modifiable.
# -----------------------------------------------------------------------------

class Case:
    """
    Représente une case de la grille.

    Une case possède :
    - une position : x colonne, y ligne
    - une valeur : 0 si vide
    - un état fixe : True si la case est donnée au départ
    """

    # -------------------------------------------------------------------------
    # --- constructeur ---------------------------------------------------------
    # -------------------------------------------------------------------------
    def __init__(self, x: int, y: int, valeur: int = 0, fixe: bool = False) -> None:
        # position de la case dans la grille
        self.__x: int = x
        self.__y: int = y

        # valeur de la case : 0 signifie que la case est vide
        self.__valeur: int = valeur

        # indique si la case est fixe ou modifiable
        self.__fixe: bool = fixe

    # -------------------------------------------------------------------------
    # --- accesseurs -----------------------------------------------------------
    # -------------------------------------------------------------------------

    # retourne la colonne de la case
    @property
    def x(self) -> int:
        return self.__x

    # retourne la ligne de la case
    @property
    def y(self) -> int:
        return self.__y

    # retourne la valeur de la case
    @property
    def valeur(self) -> int:
        return self.__valeur

    # modifie la valeur seulement si la case n'est pas fixe
    @valeur.setter
    def valeur(self, nouvelle_valeur: int) -> None:
        if not self.__fixe:
            self.__valeur = nouvelle_valeur

    # retourne True si la case est fixe
    @property
    def fixe(self) -> bool:
        return self.__fixe

    # -------------------------------------------------------------------------
    # --- méthodes -------------------------------------------------------------
    # -------------------------------------------------------------------------

    # vérifie si la case est vide
    def est_vide(self) -> bool:
        return self.__valeur == 0

    # rend la case fixe
    def rendre_fixe(self) -> None:
        self.__fixe = True

    # rend la case modifiable
    def rendre_modifiable(self) -> None:
        self.__fixe = False

    # affichage de l'objet dans la console
    def __repr__(self) -> str:
        return f"Case(x={self.__x}, y={self.__y}, valeur={self.__valeur}, fixe={self.__fixe})"


# -----------------------------------------------------------------------------
# --- main de test -------------------------------------------------------------
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    # création d'une case vide et modifiable
    case0 = Case(0, 0)

    # affichage de la case
    print(case0)

    # modification de la valeur
    case0.valeur = 3
    print(case0)

    # rendre la case fixe
    case0.rendre_fixe()

    # cette modification ne sera pas prise en compte car la case est fixe
    case0.valeur = 5
    print(case0)

    # vérification si la case est vide
    print(case0.est_vide())