# -----------------------------------------------------------------------------
# --- case_vue.py --------------------------------------------------------------
# -----------------------------------------------------------------------------
# Classe CaseVue pour le jeu Néonaure.
#
# Cette classe représente une case affichée dans l'interface graphique.
#
# Une case vue est un bouton PyQt6.
# Quand l'utilisateur clique dessus, une fenêtre demande la valeur à entrer.
#
# Important :
#   - la vue ne vérifie pas les règles du jeu
#   - la vue demande seulement une modification
#   - le contrôleur décide si la modification est acceptée ou refusée
# -----------------------------------------------------------------------------

from PyQt6.QtWidgets import QPushButton, QInputDialog
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


# -----------------------------------------------------------------------------
# --- classe CaseVue -----------------------------------------------------------
# -----------------------------------------------------------------------------
class CaseVue(QPushButton):
    """
    Représente une case graphique de la grille.
    """

        # -------------------------------------------------------------------------
    # --- constructeur ---------------------------------------------------------
    # -------------------------------------------------------------------------
    def __init__(self, ligne: int, colonne: int, valeur_max: int, callback_modification=None) -> None:

        super().__init__()

        # position de la case
        self.ligne: int = ligne
        self.colonne: int = colonne

        # valeur maximale possible selon la taille du motif
        self.valeur_max: int = valeur_max

        # état de la case
        self.fixe: bool = False

        # fonction appelée pour modifier une case
        self.callback_modification = callback_modification

        # apparence de la case
        self.setFixedSize(48, 48)
        self.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        self.setCursor(Qt.CursorShape.PointingHandCursor)

        # signal et slot
        self.clicked.connect(self.demander_valeur)
        
        # -------------------------------------------------------------------------
    # --- demande d'une valeur -------------------------------------------------
    # -------------------------------------------------------------------------
    def demander_valeur(self) -> None:
        """
        Demande une valeur au joueur.
        Le choix dépend de la taille du motif.
        """

        # une case fixe ne peut pas être modifiée
        if self.fixe:
            return

        # création de la liste des valeurs possibles
        valeurs_possibles = []

        for valeur in range(1, self.valeur_max + 1):
            valeurs_possibles.append(str(valeur))

        # ouverture d'une liste de choix
        valeur_choisie, ok = QInputDialog.getItem(
            self,
            "Modifier une case",
            f"Choisis un chiffre entre 1 et {self.valeur_max} :",
            valeurs_possibles,
            0,
            False
        )

        # si le joueur valide, on envoie la valeur au contrôleur
        if ok and self.callback_modification is not None:
            self.callback_modification(
                self.colonne,
                self.ligne,
                int(valeur_choisie)
            )

    # -------------------------------------------------------------------------
    # --- modification de l'affichage ------------------------------------------
    # -------------------------------------------------------------------------
    def set_valeur(self, valeur: int) -> None:
        """
        Affiche la valeur dans la case.
        Si la valeur vaut 0, la case est affichée vide.
        """

        if valeur == 0:
            self.setText("")
        else:
            self.setText(str(valeur))

    # -------------------------------------------------------------------------
    # --- état fixe ou modifiable ----------------------------------------------
    # -------------------------------------------------------------------------
    def set_fixe(self, fixe: bool) -> None:
        """
        Indique si la case est fixe ou modifiable.
        """

        self.fixe = fixe

        # si la case est fixe, elle est désactivée
        self.setEnabled(not fixe)

    # -------------------------------------------------------------------------
    # --- style graphique ------------------------------------------------------
    # -------------------------------------------------------------------------
    def appliquer_style(self, haut: int, droite: int, bas: int, gauche: int) -> None:
        """
        Applique le style graphique de la case.

        Les paramètres haut, droite, bas et gauche permettent de modifier
        l'épaisseur des bordures pour mieux voir les motifs.
        """

        # couleur différente selon si la case est fixe ou non
        fond: str = "#D1D5DB" if self.fixe else "#FFFFFF"

        # style CSS du bouton
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {fond};
                color: #000000;
                border-top: {haut}px solid #000000;
                border-right: {droite}px solid #000000;
                border-bottom: {bas}px solid #000000;
                border-left: {gauche}px solid #000000;
                border-radius: 0px;
                font-weight: bold;
            }}

            QPushButton:hover {{
                background-color: #F9A8D4;
            }}
        """)