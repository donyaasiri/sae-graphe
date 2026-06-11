import json


class SauvegardeJSON:
    def sauvegarder(self, grille, chemin):
        donnees = {}

        for motif in grille.motifs:
            nom_motif = f"motif{motif.identifiant}"
            donnees[nom_motif] = []

            for case in motif.cases:
                donnees[nom_motif].append([
                    case.x,
                    case.y,
                    case.valeur
                ])

        with open(chemin, "w", encoding="utf-8") as fichier:
            json.dump(donnees, fichier, indent=4)

        return True