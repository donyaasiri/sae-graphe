# -----------------------------------------------------------------------------
# --- fenetre_principale.py ----------------------------------------------------
# -----------------------------------------------------------------------------
# Classe FenetrePrincipale pour le jeu Néonaure.
#
# Cette classe représente la fenêtre principale de l'application.
#
# Elle contient :
#   - le titre du jeu
#   - les boutons principaux
#   - le menu
#   - l'affichage de la grille
#   - les messages pour l'utilisateur
#
# Important :
#   - la fenêtre ne modifie pas directement le modèle
#   - elle passe toujours par le contrôleur
# -----------------------------------------------------------------------------

from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QMessageBox, QFileDialog
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

        # création des boutons
        btn_regles = QPushButton("Voir les règles")
        btn_commencer = QPushButton("Commencer")
        btn_choisir = QPushButton("Choisir la grille")
        btn_sauvegarder = QPushButton("Sauvegarder")
        btn_verifier = QPushButton("Vérifier")
        btn_resoudre = QPushButton("Résoudre")
        btn_initialiser = QPushButton("Initialiser")
        btn_quitter = QPushButton("Quitter")

        # signaux et slots
        btn_regles.clicked.connect(self.afficher_regles)
        btn_commencer.clicked.connect(self.commencer)
        btn_choisir.clicked.connect(self.choisir_grille)
        btn_sauvegarder.clicked.connect(self.sauvegarder)
        btn_verifier.clicked.connect(self.verifier)
        btn_resoudre.clicked.connect(self.resoudre)
        btn_initialiser.clicked.connect(self.initialiser)
        btn_quitter.clicked.connect(self.close)

        # ajout des boutons dans le layout
        for bouton in [
            btn_regles, btn_commencer, btn_choisir, btn_sauvegarder,
            btn_verifier, btn_resoudre, btn_initialiser, btn_quitter
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
        menu_fichier.addAction("Sauvegarder", self.sauvegarder)
        menu_fichier.addSeparator()
        menu_fichier.addAction("Quitter", self.close)

        # menu Jeu
        menu_jeu = menu_bar.addMenu("Jeu")
        menu_jeu.addAction("Commencer", self.commencer)
        menu_jeu.addAction("Vérifier", self.verifier)
        menu_jeu.addAction("Résoudre", self.resoudre)
        menu_jeu.addAction("Initialiser", self.initialiser)

        # menu Aide
        menu_aide = menu_bar.addMenu("Aide")
        menu_aide.addAction("Voir les règles", self.afficher_regles)

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
        Affiche un message de début de partie.
        """

        self.message.setText("Partie commencée. Choisissez une grille pour commencer à jouer.")

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

        # si l'utilisateur annule
        if chemin == "":
            self.message.setText("Aucune grille sélectionnée.")
            return

        # chargement de la grille
        try:
            grille = self.controleur.charger_grille(chemin)

            self.chemin_grille_actuelle = chemin

            self.afficher_grille_modele(grille)

            self.message.setText(f"Grille chargée : {chemin}")

        except Exception as erreur:
            self.message.setText("Erreur : impossible de charger la grille.")
            print(erreur)

    # -------------------------------------------------------------------------
    # --- sauvegarde de la grille ----------------------------------------------
    # -------------------------------------------------------------------------
    def sauvegarder(self) -> None:
        """
        Sauvegarde la grille actuelle dans un fichier JSON.
        """

        chemin, _ = QFileDialog.getSaveFileName(
            self,
            "Sauvegarder la grille",
            "grilles/grille_sauvegardee.json",
            "Fichiers JSON (*.json)"
        )

        # si l'utilisateur annule
        if chemin == "":
            self.message.setText("Sauvegarde annulée.")
            return

        # demande de sauvegarde au contrôleur
        reussi = self.controleur.sauvegarder_grille(chemin)

        if reussi:
            self.message.setText(f"Grille sauvegardée : {chemin}")
        else:
            self.message.setText("Impossible de sauvegarder : aucune grille chargée.")

    # -------------------------------------------------------------------------
    # --- vérification de la grille --------------------------------------------
    # -------------------------------------------------------------------------
    def verifier(self) -> None:
        """
        Vérifie si la grille respecte les règles du jeu.
        """

        resultat = self.controleur.verifier_grille()

        if resultat:
            self.message.setText("La grille est valide.")
        else:
            self.message.setText("La grille n'est pas encore valide.")

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

        # aucune grille chargée
        if self.controleur.get_grille() is None:
            self.message.setText("Aucune grille à initialiser.")
            return

        # aucun chemin connu
        if self.chemin_grille_actuelle is None:
            self.message.setText("Impossible de réinitialiser : aucun fichier connu.")
            return

        # rechargement de la grille
        try:
            grille = self.controleur.charger_grille(self.chemin_grille_actuelle)

            self.afficher_grille_modele(grille)

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

        # parcours des lignes
        for y in range(grille.nb_lignes):

            ligne_valeurs = []
            ligne_fixes = []
            ligne_motifs = []

            # parcours des colonnes
            for x in range(grille.nb_colonnes):

                # récupération de la case du modèle
                case = grille.get_case(x, y)

                # récupération de la valeur et de l'état fixe
                ligne_valeurs.append(case.valeur)
                ligne_fixes.append(case.fixe)

                # récupération du motif de la case
                motif = grille.trouver_motif_de_case(case)

                if motif is None:
                    ligne_motifs.append(0)
                else:
                    ligne_motifs.append(motif.identifiant)

            valeurs.append(ligne_valeurs)
            fixes.append(ligne_fixes)
            motifs.append(ligne_motifs)

        # demande d'affichage au panneau de grille
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

        # on ferme tous les anciens popups encore ouverts
        for popup in self.findChildren(QMessageBox):
            popup.close()
            popup.deleteLater()

        # création du nouveau popup
        popup = QMessageBox(self)
        popup.setWindowTitle(titre)
        popup.setText(message)

        # pas de bouton OK
        popup.setStandardButtons(QMessageBox.StandardButton.NoButton)

        # le popup ne bloque pas l'application
        popup.setModal(False)

        # affichage du popup
        popup.show()

        return popup
        
    # -------------------------------------------------------------------------
    # --- fermeture du popup temporaire ----------------------------------------
    # -------------------------------------------------------------------------
    def fermer_popup_temporaire(self) -> None:
        """
        Ferme le popup temporaire.
        """

        if self.popup_temporaire is not None:
            self.popup_temporaire.close()
            self.popup_temporaire = None
            
    # -------------------------------------------------------------------------
    # --- fin d'une erreur -----------------------------------------------------
    # -------------------------------------------------------------------------
    def terminer_erreur_case(self, popup: QMessageBox, x: int, y: int, valeur: int) -> None:
        """
        Ferme le popup d'erreur et efface la valeur fausse.
        """

        # fermeture du popup
        popup.close()
        popup.deleteLater()

        # effacement de la valeur fausse
        self.controleur.effacer_case_si_valeur(x, y, valeur)

        # réaffichage de la grille
        self.afficher_grille_modele(self.controleur.get_grille())

        # message en bas
        self.message.setText("La valeur fausse a été retirée.")

    # -------------------------------------------------------------------------
    # --- modification d'une case ----------------------------------------------
    # -------------------------------------------------------------------------
    def modifier_case(self, x: int, y: int, valeur: int) -> None:
        """
        Demande au contrôleur de modifier une case.

        Si la valeur est bonne :
        - elle reste affichée
        - le popup disparaît après 2 secondes

        Si la valeur est fausse :
        - elle s'affiche d'abord
        - le popup apparaît pendant 2 secondes
        - la valeur disparaît en même temps que le popup
        """

        # demande de modification au contrôleur
        reussi, message = self.controleur.modifier_case(x, y, valeur)

        # la valeur s'affiche tout de suite
        self.afficher_grille_modele(self.controleur.get_grille())

        # message en bas
        self.message.setText(message)

        # si la valeur est bonne
        if reussi:
            popup = self.afficher_popup_temporaire("Validation", message)

            # fermeture automatique après 2 secondes
            QTimer.singleShot(5000, lambda: (popup.close(), popup.deleteLater()))

        # si la valeur est fausse
        else:
            popup = self.afficher_popup_temporaire("Erreur", message)

            # après 2 secondes :
            # - le popup se ferme
            # - la valeur fausse disparaît
            QTimer.singleShot(
                5000,
                lambda: self.terminer_erreur_case(popup, x, y, valeur)
            )