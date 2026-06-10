package modele;

/**
 * Classe représentant une case de la grille de Néonaure.
 * Une case possède une position, une valeur et peut être fixe ou modifiable.
 */
public class Case {

    private int ligne;
    private int colonne;
    private int valeur;
    private boolean fixe;

    /**
     * Constructeur d'une case.
     *
     * @param ligne position verticale de la case
     * @param colonne position horizontale de la case
     * @param valeur valeur de la case, 0 si elle est vide
     * @param fixe true si la case est donnée au départ
     */
    public Case(int ligne, int colonne, int valeur, boolean fixe) {
        this.ligne = ligne;
        this.colonne = colonne;
        this.valeur = valeur;
        this.fixe = fixe;
    }

    public int getLigne() {
        return ligne;
    }

    public int getColonne() {
        return colonne;
    }

    public int getValeur() {
        return valeur;
    }

    public boolean estFixe() {
        return fixe;
    }

    public boolean estVide() {
        return valeur == 0;
    }

    /**
     * Modifie la valeur seulement si la case n'est pas fixe.
     *
     * @param valeur nouvelle valeur
     */
    public void setValeur(int valeur) {
        if (!fixe) {
            this.valeur = valeur;
        }
    }

    public void rendreFixe() {
        this.fixe = true;
    }

    public void rendreModifiable() {
        this.fixe = false;
    }

    @Override
    public String toString() {
        return "Case(" + ligne + ", " + colonne + ") = " + valeur;
    }
}