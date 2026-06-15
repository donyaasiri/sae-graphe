from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


class CaseVue(QPushButton):
    def __init__(self, ligne, colonne):
        super().__init__()

        self.ligne = ligne
        self.colonne = colonne
        self.fixe = False

        self.setText("")
        self.setFixedSize(45, 45)
        self.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        self.setCursor(Qt.CursorShape.PointingHandCursor)

        self.set_style_normal()

    def set_valeur(self, valeur):
        self.setText("" if valeur == 0 else str(valeur))

    def set_fixe(self, fixe):
        self.fixe = fixe
        self.setEnabled(not fixe)

        if fixe:
            self.setStyleSheet("""
                QPushButton {
                    background-color: #D1D5DB;
                    color: #000000;
                    border: 1px solid #4B5563;
                }
            """)
        else:
            self.set_style_normal()

    def set_style_normal(self):
        self.setStyleSheet("""
            QPushButton {
                background-color: #FFFFFF;
                color: #111827;
                border: 1px solid #9CA3AF;
            }

            QPushButton:hover {
                background-color: #DBEAFE;
            }
        """)