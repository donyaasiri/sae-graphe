from modele.regles_jeu import ReglesJeu


class Solveur:
    def resoudre(self, grille):
        case_vide = self.trouver_case_vide(grille)

        if case_vide is None:
            return True

        x = case_vide.x
        y = case_vide.y

        motif = grille.trouver_motif_de_case(case_vide)

        if motif is None:
            valeurs_possibles = range(1, 9)
        else:
            valeurs_possibles = range(1, motif.taille() + 1)

        for valeur in valeurs_possibles:
            if ReglesJeu.valeur_possible(grille, x, y, valeur):
                case_vide.valeur = valeur

                if self.resoudre(grille):
                    return True

                case_vide.valeur = 0

        return False

    def trouver_case_vide(self, grille):
        for case in grille.toutes_les_cases():
            if case.est_vide() and not case.fixe:
                return case

        return None