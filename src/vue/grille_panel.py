# -----------------------------------------------------------------------------
# --- grille_panel.py ----------------------------------------------------------
# -----------------------------------------------------------------------------
# Classe GrillePanel pour le jeu Néonaure.
#
# Cette classe représente le panneau qui affiche toute la grille.
#
# Elle contient :
#   - un layout en grille
#   - plusieurs objets CaseVue
#
# Important :
#   - cette classe affiche seulement la grille
#   - elle ne vérifie pas les règles du jeu
#   - elle transmet les clics au contrôleur grâce au callback
# -----------------------------------------------------------------------------

from PyQt6.QtWidgets import QWidget, QGridLayout

from src.vue.case_vue import CaseVue


# -----------------------------------------------------------------------------
# --- classe GrillePanel -------------------------------------------------------
# -----------------------------------------------------------------------------
class GrillePanel(QWidget):
    """
    Représente le panneau graphique contenant toutes les cases de la grille.
    """

    # -------------------------------------------------------------------------
    # --- constructeur ---------------------------------------------------------
    # -------------------------------------------------------------------------
    def __init__(self) -> None:

        # appel du constructeur de QWidget
        super().__init__()

        # création du layout en grille
        self.layout = QGridLayout()

        # suppression de l'espace entre les cases
        self.layout.setSpacing(0)

        # suppression des marges autour de la grille
        self.layout.setContentsMargins(0, 0, 0, 0)

        # application du layout au widget
        self.setLayout(self.layout)

        # -------------------------------------------------------------------------
    # --- affichage de la grille ------------------------------------------------
    # -------------------------------------------------------------------------
    def afficher_grille(
        self,
        nb_lignes: int,
        nb_colonnes: int,
        valeurs: list,
        fixes: list,
        motifs: list,
        callback_modification
    ) -> None:
        """
        Affiche une grille à partir des données envoyées par la fenêtre principale.
        """

        # on supprime l'ancienne grille
        self.nettoyer_grille()

        # taille d'une case
        taille_case: int = 48
        self.setFixedSize(nb_colonnes * taille_case, nb_lignes * taille_case)

        # ---------------------------------------------------------------------
        # --- calcul de la taille de chaque motif ------------------------------
        # ---------------------------------------------------------------------
        tailles_motifs: dict = {}

        for y in range(nb_lignes):
            for x in range(nb_colonnes):

                identifiant_motif = motifs[y][x]

                if identifiant_motif not in tailles_motifs:
                    tailles_motifs[identifiant_motif] = 0

                tailles_motifs[identifiant_motif] += 1

        # ---------------------------------------------------------------------
        # --- création des cases graphiques ------------------------------------
        # ---------------------------------------------------------------------
        for y in range(nb_lignes):
            for x in range(nb_colonnes):

                # motif de la case actuelle
                motif_actuel = motifs[y][x]

                # valeur maximale = nombre de cases dans le motif
                valeur_max = tailles_motifs[motif_actuel]

                # création de la case graphique
                case_vue = CaseVue(y, x, valeur_max, callback_modification)

                # affichage de la valeur
                case_vue.set_valeur(valeurs[y][x])

                # état fixe ou modifiable
                case_vue.set_fixe(fixes[y][x])

                # bordure du haut
                if y == 0 or motifs[y - 1][x] != motif_actuel:
                    haut = 3
                else:
                    haut = 1

                # bordure du bas
                if y == nb_lignes - 1 or motifs[y + 1][x] != motif_actuel:
                    bas = 3
                else:
                    bas = 1

                # bordure de gauche
                if x == 0 or motifs[y][x - 1] != motif_actuel:
                    gauche = 3
                else:
                    gauche = 1

                # bordure de droite
                if x == nb_colonnes - 1 or motifs[y][x + 1] != motif_actuel:
                    droite = 3
                else:
                    droite = 1

                # application du style
                case_vue.appliquer_style(haut, droite, bas, gauche)

                # ajout de la case dans le layout
                self.layout.addWidget(case_vue, y, x)

    # -------------------------------------------------------------------------
    # --- nettoyage de la grille -----------------------------------------------
    # -------------------------------------------------------------------------
    def nettoyer_grille(self) -> None:
        """
        Supprime toutes les cases actuellement affichées.
        """

        # tant qu'il reste des éléments dans le layout
        while self.layout.count():

            # on récupère le premier élément
            item = self.layout.takeAt(0)

            # on récupère le widget contenu dans l'élément
            widget = item.widget()

            # si un widget existe, on le supprime
            if widget is not None:
                widget.deleteLater()


