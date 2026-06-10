class Controleur:
    def __init__(self):
        self.grille = None

    def charger_grille(self, chemin):
        print(f"Chargement de la grille : {chemin}")

    def sauvegarder_grille(self, chemin):
        print(f"Sauvegarde de la grille : {chemin}")

    def modifier_case(self, ligne, colonne, valeur):
        print(f"Modification case ({ligne}, {colonne}) = {valeur}")

    def verifier_grille(self):
        return False

    def resoudre_grille(self):
        return False