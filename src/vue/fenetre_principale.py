from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt

from vue.grille_panel import GrillePanel
from modele.grille import Grille


class FenetrePrincipale(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Jeu Néonaure")
        self.resize(850, 700)

        self.setStyleSheet("""
            QMainWindow {
                background-color: #111827;
                color: white;
            }

            QLabel {
                color: white;
            }

            QMenuBar {
                background-color: #1F2937;
                color: white;
                padding: 6px;
                font-size: 14px;
            }

            QMenuBar::item:selected {
                background-color: #374151;
                border-radius: 6px;
            }

            QMenu {
                background-color: #1F2937;
                color: white;
                border: 1px solid #374151;
            }

            QMenu::item:selected {
                background-color: #2563EB;
            }
        """)

        self.creer_menu()

        widget_central = QWidget()
        layout = QVBoxLayout()

        titre = QLabel("Jeu Néonaure")
        titre.setStyleSheet("font-size: 28px; font-weight: bold; margin: 15px;")
        layout.addWidget(titre)

        self.grille_panel = GrillePanel()
        layout.addWidget(self.grille_panel, alignment=Qt.AlignmentFlag.AlignCenter)

        self.message = QLabel("Bienvenue dans le jeu Néonaure.")
        self.message.setStyleSheet("font-size: 14px; margin: 12px;")
        layout.addWidget(self.message)

        widget_central.setLayout(layout)
        self.setCentralWidget(widget_central)

        self.grille_modele = self.creer_grille_test()
        self.afficher_grille_modele()

    def creer_menu(self):
        menu_bar = self.menuBar()

        menu_fichier = menu_bar.addMenu("Fichier")
        menu_fichier.addAction("Charger une grille")
        menu_fichier.addAction("Sauvegarder")
        menu_fichier.addSeparator()
        menu_fichier.addAction("Quitter")

        menu_jeu = menu_bar.addMenu("Jeu")
        menu_jeu.addAction("Vérifier")
        menu_jeu.addAction("Résoudre")
        menu_jeu.addAction("Réinitialiser")

    def creer_grille_test(self):
        grille = Grille(8, 8)

        valeurs = [
            [0, 4, 0, 0, 0, 4, 0, 0],
            [5, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 3],
            [3, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 5, 0, 5, 0],
            [2, 0, 3, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 4, 0, 0, 0],
            [0, 4, 0, 0, 0, 0, 0, 0],
        ]

        for y in range(8):
            for x in range(8):
                valeur = valeurs[y][x]
                if valeur != 0:
                    grille.set_valeur(x, y, valeur)
                    grille.get_case(x, y).rendre_fixe()
        grille.set_valeur(0, 0, 9)
        grille.get_case(0, 0).rendre_fixe()            

        return grille

    def afficher_grille_modele(self):
        valeurs = []
        fixes = []

        for y in range(self.grille_modele.nb_lignes):
            ligne_valeurs = []
            ligne_fixes = []

            for x in range(self.grille_modele.nb_colonnes):
                case = self.grille_modele.get_case(x, y)
                ligne_valeurs.append(case.valeur)
                ligne_fixes.append(case.fixe)

            valeurs.append(ligne_valeurs)
            fixes.append(ligne_fixes)

        self.grille_panel.afficher_grille(
            self.grille_modele.nb_lignes,
            self.grille_modele.nb_colonnes,
            valeurs,
            fixes
        )