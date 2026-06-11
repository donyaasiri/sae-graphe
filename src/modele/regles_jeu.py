# -----------------------------------------------------------------------------
# --- regles_jeu.py ------------------------------------------------------------
# -----------------------------------------------------------------------------
# Classe ReglesJeu pour le jeu Néonaure.
#
# Cette classe permet de vérifier les contraintes du jeu :
#   - une valeur ne doit pas être déjà présente dans le voisinage direct
#   - le voisinage comprend les cases autour, y compris les diagonales
#   - un motif de N cases doit contenir des valeurs entre 1 et N
#   - un motif ne doit pas contenir deux fois la même valeur
# -----------------------------------------------------------------------------

from src.modele.grille import Grille


# -----------------------------------------------------------------------------
# --- classe ReglesJeu ---------------------------------------------------------
# -----------------------------------------------------------------------------
class ReglesJeu:
    """
    Classe qui vérifie les règles du Néonaure.
    """

    # -------------------------------------------------------------------------
    # --- vérification du voisinage --------------------------------------------
    # -------------------------------------------------------------------------
    @staticmethod
    def verifier_voisins(grille: Grille, x: int, y: int, valeur: int) -> bool:
        """
        Vérifie qu'une valeur n'existe pas déjà dans le voisinage direct.

        Le voisinage direct correspond aux cases autour de la case :
        - haut
        - bas
        - gauche
        - droite
        - diagonales
        """

        # si la valeur vaut 0, la case est vide donc il n'y a rien à vérifier
        if valeur == 0:
            return True

        # on parcourt les cases voisines autour de la case choisie
        for voisin_y in range(y - 1, y + 2):
            for voisin_x in range(x - 1, x + 2):

                # on ignore la case elle-même
                if voisin_x == x and voisin_y == y:
                    continue

                # on vérifie que le voisin est bien dans la grille
                if 0 <= voisin_x < grille.nb_colonnes and 0 <= voisin_y < grille.nb_lignes:
                    voisin = grille.get_case(voisin_x, voisin_y)

                    # si un voisin possède la même valeur, la règle n'est pas respectée
                    if voisin.valeur == valeur:
                        return False

        return True

    # -------------------------------------------------------------------------
    # --- vérification des motifs ----------------------------------------------
    # -------------------------------------------------------------------------
    @staticmethod
    def verifier_motifs(grille: Grille) -> bool:
        """
        Vérifie que tous les motifs de la grille sont valides.
        """

        # on vérifie chaque motif de la grille
        for motif in grille.motifs:
            if not motif.est_valide():
                return False

        return True

    # -------------------------------------------------------------------------
    # --- vérification d'une valeur possible -----------------------------------
    # -------------------------------------------------------------------------
    @staticmethod
    def valeur_possible(grille: Grille, x: int, y: int, valeur: int) -> bool:
        """
        Vérifie si une valeur peut être placée dans une case.
        """

        # récupération de la case concernée
        case = grille.get_case(x, y)

        # si la case est fixe, le joueur ne peut pas la modifier
        if case.fixe:
            return False

        # vérification de la contrainte du voisinage
        if not ReglesJeu.verifier_voisins(grille, x, y, valeur):
            return False

        # recherche du motif auquel appartient la case
        motif = grille.trouver_motif_de_case(case)

        # si la case appartient à un motif, on vérifie aussi les contraintes du motif
        if motif is not None:

            # on garde l'ancienne valeur pour ne pas modifier définitivement la case
            ancienne_valeur = case.valeur

            # on vide temporairement la case pour tester la nouvelle valeur
            case.valeur = 0

            # vérification que la valeur n'existe pas déjà dans le motif
            valeur_deja_presente = motif.contient_valeur(valeur)

            # vérification que la valeur est entre 1 et la taille du motif
            valeur_dans_limite = 1 <= valeur <= motif.taille()

            # on remet l'ancienne valeur dans la case
            case.valeur = ancienne_valeur

            if valeur_deja_presente:
                return False

            if not valeur_dans_limite:
                return False

        return True

    # -------------------------------------------------------------------------
    # --- vérification complète de la grille -----------------------------------
    # -------------------------------------------------------------------------
    @staticmethod
    def verifier_grille(grille: Grille) -> bool:
        """
        Vérifie si toute la grille respecte les règles du jeu.
        """

        # on parcourt toutes les cases de la grille
        for case in grille.toutes_les_cases():

            # on ignore les cases vides
            if case.valeur == 0:
                continue

            # on vérifie le voisinage de chaque case remplie
            if not ReglesJeu.verifier_voisins(grille, case.x, case.y, case.valeur):
                return False

        # on vérifie aussi les motifs
        return ReglesJeu.verifier_motifs(grille)


# -----------------------------------------------------------------------------
# --- test rapide --------------------------------------------------------------
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    print("--- test de la classe ReglesJeu ---")

    # création d'une grille 3 x 3
    grille = Grille(3, 3)

    # placement d'une valeur
    grille.set_valeur(0, 0, 1)

    # test d'une valeur voisine identique
    print("Valeur 1 possible en (1, 1) :", ReglesJeu.valeur_possible(grille, 1, 1, 1))

    # test d'une valeur différente
    print("Valeur 2 possible en (1, 1) :", ReglesJeu.valeur_possible(grille, 1, 1, 2))

    # vérification générale
    print("Grille valide :", ReglesJeu.verifier_grille(grille))