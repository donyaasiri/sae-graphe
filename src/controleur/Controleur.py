# -----------------------------------------------------------------------------
# --- controleur.py ------------------------------------------------------------
# -----------------------------------------------------------------------------
# Classe Controleur pour le jeu Néonaure.
#
# Le contrôleur fait le lien entre :
#   - la vue
#   - le modèle
#   - le chargement JSON
#   - la sauvegarde JSON
#   - le solveur
#
# La vue ne doit pas modifier directement la grille.
# Elle passe par le contrôleur.
# -----------------------------------------------------------------------------

from src.controleur.chargeur_json import ChargeurJSON
from src.controleur.sauvegarde_json import SauvegardeJSON
from src.controleur.solveur import Solveur
from src.modele.regles_jeu import ReglesJeu
from src.modele.grille import Grille


# -----------------------------------------------------------------------------
# --- classe Controleur --------------------------------------------------------
# -----------------------------------------------------------------------------
class Controleur:
    """
    Classe qui relie la vue avec le modèle.
    """

    # -------------------------------------------------------------------------
    # --- constructeur ---------------------------------------------------------
    # -------------------------------------------------------------------------
    def __init__(self) -> None:

        # grille actuellement utilisée
        self.grille: Grille | None = None

        # outils utilisés par le contrôleur
        self.chargeur: ChargeurJSON = ChargeurJSON()
        self.sauvegarde: SauvegardeJSON = SauvegardeJSON()
        self.solveur: Solveur = Solveur()

    # -------------------------------------------------------------------------
    # --- chargement d'une grille ----------------------------------------------
    # -------------------------------------------------------------------------
    def charger_grille(self, chemin: str) -> Grille:
        """
        Charge une grille depuis un fichier JSON.
        """

        self.grille = self.chargeur.charger(chemin)

        return self.grille

    # -------------------------------------------------------------------------
    # --- sauvegarde d'une grille ----------------------------------------------
    # -------------------------------------------------------------------------
    def sauvegarder_grille(self, chemin: str) -> bool:
        """
        Sauvegarde la grille actuelle.
        """

        # impossible de sauvegarder si aucune grille n'est chargée
        if self.grille is None:
            return False

        return self.sauvegarde.sauvegarder(self.grille, chemin)

    # -------------------------------------------------------------------------
    # --- modification d'une case ----------------------------------------------
    # -------------------------------------------------------------------------
    def modifier_case(self, x: int, y: int, valeur: int) -> tuple[bool, str]:
        """
        Demande la modification d'une case.

        Renvoie :
        - True avec un message si la valeur est acceptée
        - False avec un message si la valeur est refusée
        """

        # aucune grille chargée
        if self.grille is None:
            return False, "Aucune grille n'est chargée."

        # récupération de la case
        case = self.grille.get_case(x, y)

        # une case fixe ne peut pas être modifiée
        if case.fixe:
            return False, "Cette case est fixe, tu ne peux pas la modifier."

        # vérification simple avec les règles du modèle
        if not ReglesJeu.valeur_possible(self.grille, x, y, valeur):
            return False, "Valeur refusée : elle ne respecte pas les règles du jeu."

        # si la valeur est acceptée, on la place
        case.valeur = valeur

        return True, "Bonne valeur : la case a été modifiée."

    # -------------------------------------------------------------------------
    # --- vérification de la grille --------------------------------------------
    # -------------------------------------------------------------------------
    def verifier_grille(self) -> bool:
        """
        Vérifie si la grille actuelle respecte les règles.
        """

        if self.grille is None:
            return False

        return ReglesJeu.verifier_grille(self.grille)

    # -------------------------------------------------------------------------
    # --- résolution de la grille ----------------------------------------------
    # -------------------------------------------------------------------------
    def resoudre_grille(self) -> bool:
        """
        Lance le solveur sur la grille actuelle.
        """

        if self.grille is None:
            return False

        return self.solveur.resoudre(self.grille)

    # -------------------------------------------------------------------------
    # --- accès à la grille -----------------------------------------------------
    # -------------------------------------------------------------------------
    def get_grille(self) -> Grille | None:
        """
        Renvoie la grille actuelle.
        """

        return self.grille