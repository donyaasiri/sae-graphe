class Controleur:
    def __init__(self):
        self.vue = None

    def set_vue(self, vue):
        self.vue = vue
        self.vue.connecter_bouton(self.valider)

    def valider(self):
        texte = self.vue.get_texte()

        if texte == "":
            self.vue.afficher_resultat("Erreur : champ vide")
        else:
            self.vue.afficher_resultat("Tu as écrit : " + texte)