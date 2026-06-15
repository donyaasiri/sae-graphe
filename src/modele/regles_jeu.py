from modele.grille import Grille


class ReglesJeu:
    """
    Classe qui vérifie les règles du Néonaure.
    """

    @staticmethod
    def verifier_voisins(grille: Grille, x: int, y: int, valeur: int) -> bool:
        """
        Vérifie qu'une valeur n'existe pas déjà dans le voisinage direct.
        Le voisinage inclut les diagonales.
        """
        if valeur == 0:
            return True

        for voisin_y in range(y - 1, y + 2):
            for voisin_x in range(x - 1, x + 2):

                if voisin_x == x and voisin_y == y:
                    continue

                if 0 <= voisin_x < grille.nb_colonnes and 0 <= voisin_y < grille.nb_lignes:
                    voisin = grille.get_case(voisin_x, voisin_y)

                    if voisin.valeur == valeur:
                        return False

        return True

    @staticmethod
    def verifier_motifs(grille: Grille) -> bool:
        """
        Vérifie que tous les motifs de la grille sont valides.
        """
        for motif in grille.motifs:
            if not motif.est_valide():
                return False
        return True

    @staticmethod
    def valeur_possible(grille: Grille, x: int, y: int, valeur: int) -> bool:
        """
        Vérifie si une valeur peut être placée dans une case.
        """
        case = grille.get_case(x, y)

        if case.fixe:
            return False

        if not ReglesJeu.verifier_voisins(grille, x, y, valeur):
            return False

        motif = grille.trouver_motif_de_case(case)

        if motif is not None:
            ancienne_valeur = case.valeur

            case.valeur = 0

            valeur_deja_presente = motif.contient_valeur(valeur)
            valeur_dans_limite = 1 <= valeur <= motif.taille()

            case.valeur = ancienne_valeur

            if valeur_deja_presente:
                return False

            if not valeur_dans_limite:
                return False

        return True

    @staticmethod
    def verifier_grille(grille: Grille) -> bool:
        """
        Vérifie si toute la grille respecte les règles.
        """
        for case in grille.toutes_les_cases():
            if case.valeur == 0:
                continue

            if not ReglesJeu.verifier_voisins(grille, case.x, case.y, case.valeur):
                return False

        return ReglesJeu.verifier_motifs(grille)
