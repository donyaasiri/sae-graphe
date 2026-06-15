from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt6.QtCore import pyqtSignal


class Vue(QWidget):

    actionDemandee = pyqtSignal(dict)

    def __init__(self):
        super().__init__()

        self.label = QLabel("Nom :")
        self.champ = QLineEdit()
        self.bouton = QPushButton("Valider")

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.champ)
        layout.addWidget(self.bouton)

        self.setLayout(layout)

        self.bouton.clicked.connect(self.envoyer_infos)

    def envoyer_infos(self):
        d = {
            "nom": self.champ.text()
        }

        self.actionDemandee.emit(d)

    def updateVue(self, donnees):
        self.label.setText(donnees["message"])