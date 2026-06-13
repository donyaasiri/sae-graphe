from PyQt6.QtWidgets import QWidget, QGridLayout
from vue.case_vue import CaseVue


class GrillePanel(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QGridLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        self.cases = []

    def afficher_grille(self, nb_lignes, nb_colonnes, valeurs=None, fixes=None):
        self.nettoyer_grille()
        self.cases = []

        taille_case = 45
        self.setFixedSize(nb_colonnes * taille_case, nb_lignes * taille_case)

        for ligne in range(nb_lignes):
            ligne_cases = []

            for colonne in range(nb_colonnes):
                case = CaseVue(ligne, colonne)

                if valeurs is not None:
                    case.set_valeur(valeurs[ligne][colonne])

                if fixes is not None:
                    case.set_fixe(fixes[ligne][colonne])

                self.layout.addWidget(case, ligne, colonne)
                ligne_cases.append(case)

            self.cases.append(ligne_cases)

    def nettoyer_grille(self):
        while self.layout.count():
            item = self.layout.takeAt(0)
            widget = item.widget()

            if widget is not None:
                widget.deleteLater()