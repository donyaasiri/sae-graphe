from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QMessageBox
)
from PyQt6.QtCore import Qt

from vue.grille_panel import GrillePanel
from controleur.controleur import Controleur


class FenetrePrincipale(QMainWindow):
    def __init__(self):
        super().__init__()

        self.controleur = Controleur()

        self.setWindowTitle("Jeu Néonaure")
        self.resize(950, 720)

        self.setStyleSheet("""
            QMainWindow {
                background-color: #0B0B10;
            }

            QLabel {
                color: white;
            }

            QPushButton {
                background-color: #E91E63;
                color: white;
                border: none;
                border-radius: 14px;
                padding: 12px;
                font-size: 15px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #FF4F93;
            }

            QPushButton:pressed {
                background-color: #AD1457;
            }

            QMenuBar {
                background-color: #16161F;
                color: white;
                padding: 8px;
                font-size: 14px;
            }

            QMenuBar::item:selected {
                background-color: #E91E63;
                border-radius: 6px;
            }

            QMenu {
                background-color: #16161F;
                color: white;
                border: 1px solid #E91E63;
            }

            QMenu::item:selected {
                background-color: #E91E63;
            }
        """)

        self.creer_menu()

        widget_central = QWidget()
        layout_principal = QVBoxLayout()
        layout_principal.setContentsMargins(35, 25, 35, 25)
        layout_principal.setSpacing(20)

        titre = QLabel("NÉONAURE")
        titre.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titre.setStyleSheet("""
            font-size: 42px;
            font-weight: bold;
            color: #FF4F93;
            letter-spacing: 3px;
        """)
        layout_principal.addWidget(titre)

        sous_titre = QLabel("Jeu de logique — Graphes & IHM")
        sous_titre.setAlignment(Qt.AlignmentFlag.AlignCenter)
        sous_titre.setStyleSheet("font-size: 16px; color: #D1D5DB;")
        layout_principal.addWidget(sous_titre)

        layout_boutons = QHBoxLayout()
        layout_boutons.setSpacing(12)

        btn_regles = QPushButton("Voir les règles")
        btn_commencer = QPushButton("Commencer")
        btn_choisir = QPushButton("Choisir la grille")
        btn_sauvegarder = QPushButton("Sauvegarder")
        btn_verifier = QPushButton("Vérifier")
        btn_resoudre = QPushButton("Résoudre")
        btn_initialiser = QPushButton("Initialiser")
        btn_quitter = QPushButton("Quitter")

        btn_regles.clicked.connect(self.afficher_regles)
        btn_commencer.clicked.connect(self.commencer)
        btn_choisir.clicked.connect(self.choisir_grille)
        btn_sauvegarder.clicked.connect(self.sauvegarder)
        btn_verifier.clicked.connect(self.verifier)
        btn_resoudre.clicked.connect(self.resoudre)
        btn_initialiser.clicked.connect(self.initialiser)
        btn_quitter.clicked.connect(self.close)

        for bouton in [
            btn_regles, btn_commencer, btn_choisir, btn_sauvegarder,
            btn_verifier, btn_resoudre, btn_initialiser, btn_quitter
        ]:
            layout_boutons.addWidget(bouton)

        layout_principal.addLayout(layout_boutons)

        self.grille_panel = GrillePanel()
        layout_principal.addWidget(self.grille_panel, alignment=Qt.AlignmentFlag.AlignCenter)

        self.message = QLabel("Bienvenue dans Néonaure. Choisissez une action pour commencer.")
        self.message.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.message.setStyleSheet("""
            color: #F9A8D4;
            font-size: 15px;
            padding: 10px;
        """)
        layout_principal.addWidget(self.message)

        widget_central.setLayout(layout_principal)
        self.setCentralWidget(widget_central)

    def creer_menu(self):
        menu_bar = self.menuBar()

        menu_fichier = menu_bar.addMenu("Fichier")
        menu_fichier.addAction("Choisir une grille")
        menu_fichier.addAction("Sauvegarder")
        menu_fichier.addSeparator()
        menu_fichier.addAction("Quitter", self.close)

        menu_jeu = menu_bar.addMenu("Jeu")
        menu_jeu.addAction("Commencer")
        menu_jeu.addAction("Vérifier")
        menu_jeu.addAction("Résoudre")
        menu_jeu.addAction("Initialiser")

        menu_aide = menu_bar.addMenu("Aide")
        menu_aide.addAction("Voir les règles", self.afficher_regles)

    def afficher_regles(self):
        QMessageBox.information(
            self,
            "Règles du jeu",
            "Règles du Néonaure :\n\n"
            "1. Chaque case doit contenir un chiffre.\n"
            "2. Deux cases voisines, même en diagonale, ne doivent pas avoir le même chiffre.\n"
            "3. Un motif de N cases doit contenir les chiffres de 1 à N.\n\n"
            "Le but est de compléter toute la grille correctement."
        )

    def commencer(self):
        self.message.setText("Partie commencée.")

    def choisir_grille(self):
        try:
            grille = self.controleur.charger_grille("grilles/grille1.json")
            self.afficher_grille_modele(grille)
            self.message.setText("Grille chargée : grille1.json")
        except Exception as erreur:
            self.message.setText("Erreur : impossible de charger la grille.")
            print(erreur)

    def sauvegarder(self):
        self.message.setText("Sauvegarde à connecter avec le contrôleur.")

    def verifier(self):
        resultat = self.controleur.verifier_grille()
        if resultat:
            self.message.setText("La grille est valide.")
        else:
            self.message.setText("La grille n'est pas encore valide.")

    def resoudre(self):
        self.message.setText("Résolution à connecter au solveur.")

    def initialiser(self):
        self.grille_panel.afficher_grille(8, 8)
        self.message.setText("Grille réinitialisée.")

    def afficher_grille_modele(self, grille):
        valeurs = []
        fixes = []

        for y in range(grille.nb_lignes):
            ligne_valeurs = []
            ligne_fixes = []

            for x in range(grille.nb_colonnes):
                case = grille.get_case(x, y)
                ligne_valeurs.append(case.valeur)
                ligne_fixes.append(case.fixe)

            valeurs.append(ligne_valeurs)
            fixes.append(ligne_fixes)

        self.grille_panel.afficher_grille(
            grille.nb_lignes,
            grille.nb_colonnes,
            valeurs,
            fixes
        )