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
from src.modele.regles_jeu import ReglesJeu
from src.controleur.solveur import Solveur
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

        # grille actuellement utilisée dans le jeu
        self.grille: Grille | None = None

        # outils du contrôleur
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

        # le chargeur lit le fichier JSON et crée une grille
        self.grille = self.chargeur.charger(chemin)

        return self.grille

    # -------------------------------------------------------------------------
    # --- sauvegarde d'une grille ----------------------------------------------
    # -------------------------------------------------------------------------
    def sauvegarder_grille(self, chemin: str) -> bool:
        """
        Sauvegarde la grille actuelle dans un fichier JSON.
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
        Modifie une case de la grille.

        La valeur est toujours affichée si la case n'est pas fixe.
        Ensuite, le contrôleur indique si la valeur est correcte ou non.

        Renvoie :
        - True avec un message si aucune erreur n'est détectée
        - False avec un message si une erreur est détectée
        """

        # aucune grille chargée
        if self.grille is None:
            return False, "Aucune grille n'est chargée."

        # récupération de la case
        case = self.grille.get_case(x, y)

        # une case fixe ne peut pas être modifiée
        if case.fixe:
            return False, "Cette case est fixe, tu ne peux pas la modifier."

        # on place la valeur dans la case
        # même si elle est fausse, pour que le joueur la voie
        case.valeur = valeur

        # si le joueur met 0, on considère qu'il vide la case
        if valeur == 0:
            return True, "Case vidée."

        # recherche du motif de la case
        motif = self.grille.trouver_motif_de_case(case)

        # ---------------------------------------------------------------------
        # --- vérification de la contrainte du motif ---------------------------
        # ---------------------------------------------------------------------
        if motif is not None:

            # la valeur doit être entre 1 et la taille du motif
            if valeur < 1 or valeur > motif.taille():
                return False, f"Erreur : ce motif contient {motif.taille()} cases. Il faut un chiffre entre 1 et {motif.taille()}."

            # on vérifie si la valeur existe déjà dans le motif
            for autre_case in motif.cases:
                if autre_case is not case and autre_case.valeur == valeur:
                    return False, f"Erreur : le chiffre {valeur} est déjà présent dans ce motif."

        # ---------------------------------------------------------------------
        # --- vérification du voisinage direct ---------------------------------
        # ---------------------------------------------------------------------
        for voisin_y in range(y - 1, y + 2):
            for voisin_x in range(x - 1, x + 2):

                # on ignore la case elle-même
                if voisin_x == x and voisin_y == y:
                    continue

                # on vérifie que le voisin est dans la grille
                if 0 <= voisin_x < self.grille.nb_colonnes and 0 <= voisin_y < self.grille.nb_lignes:
                    voisin = self.grille.get_case(voisin_x, voisin_y)

                    if voisin.valeur == valeur:
                        return False, f"Erreur : le chiffre {valeur} est déjà dans le voisinage direct."

        return True, "Bonne valeur : aucune erreur détectée."
    
    # -------------------------------------------------------------------------
    # --- effacement d'une valeur fausse ---------------------------------------
    # -------------------------------------------------------------------------
    def effacer_case_si_valeur(self, x: int, y: int, valeur: int) -> None:
        """
        Efface une case seulement si elle contient encore la valeur donnée.
        Cela évite d'effacer une nouvelle valeur si le joueur a déjà modifié la case.
        """

        # aucune grille chargée
        if self.grille is None:
            return

        # récupération de la case
        case = self.grille.get_case(x, y)

        # on ne modifie jamais une case fixe
        if case.fixe:
            return

        # on efface seulement si la valeur n'a pas changé entre temps
        if case.valeur == valeur:
            case.valeur = 0

    # -------------------------------------------------------------------------
    # --- vérification de la grille --------------------------------------------
    # -------------------------------------------------------------------------
    def verifier_grille(self) -> bool:
        """
        Vérifie si la grille actuelle respecte les règles du jeu.
        """

        # impossible de vérifier si aucune grille n'est chargée
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

        # impossible de résoudre si aucune grille n'est chargée
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


