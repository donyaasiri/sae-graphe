# -----------------------------------------------------------------------------
# --- fenetre_principale.py ----------------------------------------------------
# -----------------------------------------------------------------------------
# Classe FenetrePrincipale pour le jeu Néonaure.
#
# Cette classe représente la fenêtre principale de l'application.
#
# Elle contient 
# # - le titre du jeu
# - les boutons principaux
# - le menu
# - l'affichage de la grille
# - les messages pour l'utilisateur
# Important :
# - la fenêtre ne modifie pas directement le modèle
# - elle passe toujours par le contrôleur
# -----------------------------------------------------------------------------

import os

from PyQt6.QtWidgets import (
QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
QLabel, QPushButton, QMessageBox, QFileDialog, QInputDialog
)
from PyQt6.QtCore import Qt, QTimer

from src.vue.grille_panel import GrillePanel
from src.controleur.controleur import Controleur
from src.modele.grille import Grille

# -----------------------------------------------------------------------------

# --- classe FenetrePrincipale -------------------------------------------------

# -----------------------------------------------------------------------------

class FenetrePrincipale(QMainWindow):
    """
    Fenêtre principale du jeu Néonaure.
    """


    # -------------------------------------------------------------------------
    # --- constructeur ---------------------------------------------------------
    # -------------------------------------------------------------------------
    def __init__(self) -> None:

        # appel du constructeur de QMainWindow
        super().__init__()

        # création du contrôleur
        self.controleur: Controleur = Controleur()

        # chemin de la grille actuellement chargée
        self.chemin_grille_actuelle: str | None = None

        # dossier où seront enregistrées les parties sauvegardées
        self.dossier_sauvegardes: str = "sauvegardes"

        # création du dossier s'il n'existe pas
        os.makedirs(self.dossier_sauvegardes, exist_ok=True)

        # popup temporaire
        self.popup_temporaire = None

        # paramètres de la fenêtre
        self.setWindowTitle("Jeu Néonaure")
        self.resize(950, 720)

        # style général de l'application
        self.appliquer_style()

        # création du menu
        self.creer_menu()

        # création du widget central
        widget_central = QWidget()

        # layout principal vertical
        layout_principal = QVBoxLayout()
        layout_principal.setContentsMargins(35, 25, 35, 25)
        layout_principal.setSpacing(20)

        # ---------------------------------------------------------------------
        # --- titre ------------------------------------------------------------
        # ---------------------------------------------------------------------
        titre = QLabel("NÉONAURE")
        titre.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titre.setStyleSheet("""
            font-size: 42px;
            font-weight: bold;
            color: #FF4F93;
            letter-spacing: 3px;
        """)

        layout_principal.addWidget(titre)

        # ---------------------------------------------------------------------
        # --- sous-titre --------------------------------------------------------
        # ---------------------------------------------------------------------
        sous_titre = QLabel("Jeu de logique — Graphes & IHM")
        sous_titre.setAlignment(Qt.AlignmentFlag.AlignCenter)
        sous_titre.setStyleSheet("font-size: 16px; color: #D1D5DB;")

        layout_principal.addWidget(sous_titre)

        # ---------------------------------------------------------------------
        # --- boutons ----------------------------------------------------------
        # ---------------------------------------------------------------------
        layout_boutons = QHBoxLayout()
        layout_boutons.setSpacing(12)
        layout_boutons.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # création des boutons
        self.btn_regles = QPushButton("Voir les règles")
        self.btn_commencer = QPushButton("Commencer")
        self.btn_choisir = QPushButton("Choisir la grille")
        self.btn_continuer = QPushButton("Continuer")
        self.btn_sauvegarder = QPushButton("Sauvegarder")
        self.btn_resoudre = QPushButton("Résoudre")
        self.btn_initialiser = QPushButton("Initialiser")
        self.btn_quitter = QPushButton("Quitter")

        # signaux et slots
        self.btn_regles.clicked.connect(self.afficher_regles)
        self.btn_commencer.clicked.connect(self.commencer)
        self.btn_choisir.clicked.connect(self.choisir_grille)
        self.btn_continuer.clicked.connect(self.continuer_partie)
        self.btn_sauvegarder.clicked.connect(self.sauvegarder)
        self.btn_resoudre.clicked.connect(self.resoudre)
        self.btn_initialiser.clicked.connect(self.initialiser)
        self.btn_quitter.clicked.connect(self.close)

        # ajout des boutons dans le layout
        for bouton in [
            self.btn_regles, self.btn_commencer, self.btn_choisir,
            self.btn_continuer, self.btn_sauvegarder, self.btn_resoudre,
            self.btn_initialiser, self.btn_quitter
        ]:
            layout_boutons.addWidget(bouton)

        layout_principal.addLayout(layout_boutons)

        # ---------------------------------------------------------------------
        # --- panneau de la grille ---------------------------------------------
        # ---------------------------------------------------------------------
        self.grille_panel = GrillePanel()

        layout_principal.addWidget(
            self.grille_panel,
            alignment=Qt.AlignmentFlag.AlignCenter
        )

        # ---------------------------------------------------------------------
        # --- message utilisateur ----------------------------------------------
        # ---------------------------------------------------------------------
        self.message = QLabel("Bienvenue dans Néonaure. Choisissez une action pour commencer.")
        self.message.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.message.setStyleSheet("""
            color: #F9A8D4;
            font-size: 15px;
            padding: 10px;
        """)

        layout_principal.addWidget(self.message)

        # application du layout au widget central
        widget_central.setLayout(layout_principal)

        # ajout du widget central dans la fenêtre
        self.setCentralWidget(widget_central)

        # état de départ de l'application
        self.mettre_etat_accueil()

    # -------------------------------------------------------------------------
    # --- style de la fenêtre --------------------------------------------------
    # -------------------------------------------------------------------------
    def appliquer_style(self) -> None:
        """
        Applique le style graphique général de la fenêtre.
        """

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

    # -------------------------------------------------------------------------
    # --- création du menu -----------------------------------------------------
    # -------------------------------------------------------------------------
    def creer_menu(self) -> None:
        """
        Crée la barre de menu de l'application.
        """

        menu_bar = self.menuBar()

        # menu Fichier
        menu_fichier = menu_bar.addMenu("Fichier")
        menu_fichier.addAction("Choisir une grille", self.choisir_grille)
        menu_fichier.addAction("Continuer une partie", self.continuer_partie)
        menu_fichier.addAction("Sauvegarder", self.sauvegarder)
        menu_fichier.addSeparator()
        menu_fichier.addAction("Quitter", self.close)

        # menu Jeu
        menu_jeu = menu_bar.addMenu("Jeu")
        menu_jeu.addAction("Commencer", self.commencer)
        menu_jeu.addAction("Résoudre", self.resoudre)
        menu_jeu.addAction("Initialiser", self.initialiser)

        # menu Aide
        menu_aide = menu_bar.addMenu("Aide")
        menu_aide.addAction("Voir les règles", self.afficher_regles)

    # -------------------------------------------------------------------------
    # --- état accueil ---------------------------------------------------------
    # -------------------------------------------------------------------------
    def mettre_etat_accueil(self) -> None:
        """
        Affiche seulement le bouton Commencer au lancement.
        """

        self.btn_regles.hide()
        self.btn_commencer.show()
        self.btn_choisir.hide()
        self.btn_continuer.hide()
        self.btn_sauvegarder.hide()
        self.btn_resoudre.hide()
        self.btn_initialiser.hide()
        self.btn_quitter.hide()

        self.grille_panel.hide()

        self.message.setText("Bienvenue dans Néonaure. Cliquez sur Commencer.")

        self.btn_commencer.setMinimumWidth(250)
        self.btn_commencer.setMinimumHeight(70)
        
    # -------------------------------------------------------------------------
    # --- état choix de grille -------------------------------------------------
    # -------------------------------------------------------------------------
    def mettre_etat_choix_grille(self) -> None:
        """
        Affiche les boutons pour choisir ou continuer une partie.
        """

        self.btn_regles.show()
        self.btn_commencer.hide()
        self.btn_choisir.show()
        self.btn_continuer.show()
        self.btn_sauvegarder.hide()
        self.btn_resoudre.hide()
        self.btn_initialiser.hide()
        self.btn_quitter.show()

        self.grille_panel.hide()

        self.message.setText("Choisissez une grille ou continuez une partie sauvegardée.")

    # -------------------------------------------------------------------------
    # --- état jeu -------------------------------------------------------------
    # -------------------------------------------------------------------------
    def mettre_etat_jeu(self) -> None:
        """
        Affiche les boutons utiles pendant la partie.
        """

        self.btn_regles.show()
        self.btn_commencer.hide()
        self.btn_choisir.show()
        self.btn_continuer.show()
        self.btn_sauvegarder.show()
        self.btn_resoudre.show()
        self.btn_initialiser.show()
        self.btn_quitter.show()

        self.grille_panel.show()

    # -------------------------------------------------------------------------
    # --- affichage des règles -------------------------------------------------
    # -------------------------------------------------------------------------
    def afficher_regles(self) -> None:
        """
        Affiche les règles du jeu dans une fenêtre de message.
        """

        QMessageBox.information(
            self,
            "Règles du jeu",
            "Règles du Néonaure :\n\n"
            "1. Chaque case doit contenir un chiffre.\n"
            "2. Deux cases voisines, même en diagonale, ne doivent pas avoir le même chiffre.\n"
            "3. Un motif de N cases doit contenir les chiffres de 1 à N.\n\n"
            "Le but est de compléter toute la grille correctement."
        )

    # -------------------------------------------------------------------------
    # --- commencer une partie -------------------------------------------------
    # -------------------------------------------------------------------------
    def commencer(self) -> None:
        """
        Passe de l'écran d'accueil au choix de la grille.
        """

        self.mettre_etat_choix_grille()

    # -------------------------------------------------------------------------
    # --- choix d'une grille ---------------------------------------------------
    # -------------------------------------------------------------------------
    def choisir_grille(self) -> None:
        """
        Ouvre une fenêtre pour choisir un fichier JSON.
        """

        chemin, _ = QFileDialog.getOpenFileName(
            self,
            "Choisir une grille",
            "grilles",
            "Fichiers JSON (*.json)"
        )

        if chemin == "":
            self.message.setText("Aucune grille sélectionnée.")
            return

        try:
            grille = self.controleur.charger_grille(chemin)

            self.chemin_grille_actuelle = chemin

            self.afficher_grille_modele(grille)

            self.mettre_etat_jeu()

            self.message.setText(f"Grille chargée : {chemin}")

        except Exception as erreur:
            self.message.setText("Erreur : impossible de charger la grille.")
            print(erreur)

    # -------------------------------------------------------------------------
    # --- sauvegarde de la grille ----------------------------------------------
    # -------------------------------------------------------------------------
    def sauvegarder(self) -> None:
        """
        Sauvegarde la partie dans le dossier sauvegardes de l'application.
        """

        if self.controleur.get_grille() is None:
            self.message.setText("Impossible de sauvegarder : aucune grille chargée.")
            return

        nom, ok = QInputDialog.getText(
            self,
            "Sauvegarder la partie",
            "Nom de la sauvegarde :"
        )

        if not ok or nom.strip() == "":
            self.message.setText("Sauvegarde annulée.")
            return

        nom = nom.strip()

        if not nom.endswith(".json"):
            nom = nom + ".json"

        chemin = os.path.join(self.dossier_sauvegardes, nom)

        reussi = self.controleur.sauvegarder_grille(chemin)

        if reussi:
            self.chemin_grille_actuelle = chemin
            self.message.setText(f"Partie sauvegardée : {nom}")
        else:
            self.message.setText("Erreur : la partie n'a pas pu être sauvegardée.")

    # -------------------------------------------------------------------------
    # --- continuer une partie sauvegardée -------------------------------------
    # -------------------------------------------------------------------------
    def continuer_partie(self) -> None:
        """
        Charge une partie sauvegardée depuis le dossier sauvegardes.
        """

        fichiers = []

        for fichier in os.listdir(self.dossier_sauvegardes):
            if fichier.endswith(".json"):
                fichiers.append(fichier)

        if len(fichiers) == 0:
            self.message.setText("Aucune partie sauvegardée trouvée.")
            return

        nom_fichier, ok = QInputDialog.getItem(
            self,
            "Continuer une partie",
            "Choisis une sauvegarde :",
            fichiers,
            0,
            False
        )

        if not ok:
            self.message.setText("Chargement annulé.")
            return

        chemin = os.path.join(self.dossier_sauvegardes, nom_fichier)

        try:
            grille = self.controleur.charger_grille(chemin)

            self.chemin_grille_actuelle = chemin

            self.afficher_grille_modele(grille)

            self.mettre_etat_jeu()

            self.message.setText(f"Partie chargée : {nom_fichier}")

        except Exception as erreur:
            self.message.setText("Erreur : impossible de charger la sauvegarde.")
            print(erreur)

    # -------------------------------------------------------------------------
    # --- résolution de la grille ----------------------------------------------
    # -------------------------------------------------------------------------
    def resoudre(self) -> None:
        """
        Demande au contrôleur de résoudre la grille.
        """

        reussi = self.controleur.resoudre_grille()

        if reussi:
            self.afficher_grille_modele(self.controleur.get_grille())
            self.mettre_etat_jeu()
            self.message.setText("Grille résolue.")
        else:
            self.message.setText("Aucune solution trouvée ou aucune grille chargée.")

    # -------------------------------------------------------------------------
    # --- réinitialisation de la grille -----------------------------------------
    # -------------------------------------------------------------------------
    def initialiser(self) -> None:
        """
        Recharge la grille depuis le fichier JSON d'origine.
        """

        if self.controleur.get_grille() is None:
            self.message.setText("Aucune grille à initialiser.")
            return

        if self.chemin_grille_actuelle is None:
            self.message.setText("Impossible de réinitialiser : aucun fichier connu.")
            return

        try:
            grille = self.controleur.charger_grille(self.chemin_grille_actuelle)

            self.afficher_grille_modele(grille)

            self.mettre_etat_jeu()

            self.message.setText("Grille réinitialisée.")

        except Exception as erreur:
            self.message.setText("Impossible de réinitialiser la grille.")
            print(erreur)

    # -------------------------------------------------------------------------
    # --- affichage d'une grille du modèle --------------------------------------
    # -------------------------------------------------------------------------
    def afficher_grille_modele(self, grille: Grille) -> None:
        """
        Transforme la grille du modèle en données simples pour la vue.
        """

        valeurs: list = []
        fixes: list = []
        motifs: list = []

        for y in range(grille.nb_lignes):

            ligne_valeurs = []
            ligne_fixes = []
            ligne_motifs = []

            for x in range(grille.nb_colonnes):

                case = grille.get_case(x, y)

                ligne_valeurs.append(case.valeur)
                ligne_fixes.append(case.fixe)

                motif = grille.trouver_motif_de_case(case)

                if motif is None:
                    ligne_motifs.append(0)
                else:
                    ligne_motifs.append(motif.identifiant)

            valeurs.append(ligne_valeurs)
            fixes.append(ligne_fixes)
            motifs.append(ligne_motifs)

        self.grille_panel.afficher_grille(
            grille.nb_lignes,
            grille.nb_colonnes,
            valeurs,
            fixes,
            motifs,
            self.modifier_case
        )

    # -------------------------------------------------------------------------
    # --- popup temporaire -----------------------------------------------------
    # -------------------------------------------------------------------------
    def afficher_popup_temporaire(self, titre: str, message: str) -> QMessageBox:
        """
        Affiche un popup temporaire.
        Renvoie le popup créé pour pouvoir le fermer après.
        """

        for popup in self.findChildren(QMessageBox):
            popup.close()
            popup.deleteLater()

        popup = QMessageBox(self)
        popup.setWindowTitle(titre)
        popup.setText(message)
        popup.setStandardButtons(QMessageBox.StandardButton.NoButton)
        popup.setModal(False)
        popup.show()

        return popup

    # -------------------------------------------------------------------------
    # --- fin d'une erreur -----------------------------------------------------
    # -------------------------------------------------------------------------
    def terminer_erreur_case(self, popup: QMessageBox, x: int, y: int, valeur: int) -> None:
        """
        Ferme le popup d'erreur et efface la valeur fausse.
        """

        popup.close()
        popup.deleteLater()

        self.controleur.effacer_case_si_valeur(x, y, valeur)

        self.afficher_grille_modele(self.controleur.get_grille())

        self.message.setText("La valeur fausse a été retirée.")

    # -------------------------------------------------------------------------
    # --- modification d'une case ----------------------------------------------
    # -------------------------------------------------------------------------
    def modifier_case(self, x: int, y: int, valeur: int) -> None:
        """
        Demande au contrôleur de modifier une case.
        """

        reussi, message = self.controleur.modifier_case(x, y, valeur)

        self.afficher_grille_modele(self.controleur.get_grille())

        self.message.setText(message)

        if reussi:
            popup = self.afficher_popup_temporaire("Validation", message)

            QTimer.singleShot(
                5000,
                lambda: (popup.close(), popup.deleteLater())
            )

        else:
            popup = self.afficher_popup_temporaire("Erreur", message)

            QTimer.singleShot(
                5000,
                lambda: self.terminer_erreur_case(popup, x, y, valeur)
            )