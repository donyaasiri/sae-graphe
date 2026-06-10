class Case:
    """
    Représente une case de la grille.

    Une case possède :
    - une position : x colonne, y ligne
    - une valeur : 0 si vide
    - un état fixe : True si la case est donnée au départ
    """

    def __init__(self, x: int, y: int, valeur: int = 0, fixe: bool = False):
        self.__x = x
        self.__y = y
        self.__valeur = valeur
        self.__fixe = fixe

    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y

    @property
    def valeur(self) -> int:
        return self.__valeur

    @valeur.setter
    def valeur(self, nouvelle_valeur: int) -> None:
        if not self.__fixe:
            self.__valeur = nouvelle_valeur

    @property
    def fixe(self) -> bool:
        return self.__fixe

    def est_vide(self) -> bool:
        return self.__valeur == 0

    def rendre_fixe(self) -> None:
        self.__fixe = True

    def rendre_modifiable(self) -> None:
        self.__fixe = False

    def __repr__(self) -> str:
        return f"Case(x={self.__x}, y={self.__y}, valeur={self.__valeur}, fixe={self.__fixe})"