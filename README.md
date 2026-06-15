# SAE Graphes - IHM : Néonaure

## Présentation du projet

Ce projet a été réalisé dans le cadre de la SAE Graphes - IHM en BUT Informatique.

L’objectif est de développer une application graphique permettant de jouer au Néonaure, un jeu inspiré du Sudoku. Le jeu se joue sur une grille découpée en motifs. Le joueur doit remplir les cases en respectant plusieurs contraintes.

## Membres du groupe

* Donya Asiri
* Manal El Baztami
* Aysu Sahin

## Règles du jeu

La grille doit être remplie avec des chiffres en respectant trois contraintes :

1. Chaque case doit contenir un seul chiffre.
2. Deux cases voisines ne peuvent pas contenir le même chiffre. Le voisinage comprend les cases autour, y compris les diagonales.
3. Chaque motif de N cases doit contenir les chiffres de 1 à N.

Certaines cases sont déjà remplies au début de la partie. Ces cases sont fixes et ne peuvent pas être modifiées par le joueur.

## Fonctionnalités réalisées

L’application permet de :

* charger une grille au format JSON ;
* afficher la grille dans une interface graphique ;
* jouer en remplissant les cases ;
* empêcher la modification des cases fixes ;
* vérifier les erreurs de voisinage et de motif ;
* afficher un message d’aide si une valeur est incorrecte ;
* sauvegarder une partie ;
* continuer une partie sauvegardée ;
* résoudre automatiquement une grille avec un solveur ;
* réinitialiser la grille.

## Assistance au joueur

L’application propose une aide pendant le jeu. Lorsqu’un joueur entre une valeur incorrecte, un message d’erreur s’affiche. La valeur reste visible quelques secondes, puis elle est supprimée automatiquement.

Cette fonctionnalité permet d’aider le joueur à comprendre ses erreurs.

## Lancement de l’application

Pour lancer l’application, il faut se placer à la racine du projet puis utiliser la commande :

```bash
py -m src.main
```

Il faut avoir Python et PyQt6 installés.

Installation de PyQt6 si nécessaire :

```bash
pip install PyQt6
```

## Structure du projet

Le projet respecte une architecture MVC.

```text
src/
├── main.py
├── modele/
│   ├── case.py
│   ├── motif.py
│   ├── grille.py
│   └── regles_jeu.py
├── vue/
│   ├── fenetre_principale.py
│   ├── grille_panel.py
│   └── case_vue.py
└── controleur/
    ├── controleur.py
    ├── chargeur_json.py
    ├── sauvegarde_json.py
    └── solveur.py
```

## Architecture MVC

### Modèle

Le modèle contient les classes qui représentent les données du jeu :

* `Case` : représente une case de la grille ;
* `Motif` : représente un groupe de cases ;
* `Grille` : représente la grille complète ;
* `ReglesJeu` : vérifie les contraintes du jeu.

### Vue

La vue contient l’interface graphique réalisée avec PyQt6 :

* `FenetrePrincipale` : fenêtre principale de l’application ;
* `GrillePanel` : affichage de la grille ;
* `CaseVue` : affichage graphique d’une case.

### Contrôleur

Le contrôleur fait le lien entre la vue et le modèle :

* chargement des grilles ;
* sauvegarde des parties ;
* modification des cases ;
* vérification des règles ;
* résolution de la grille.

## Format des grilles

Les grilles sont stockées au format JSON. Chaque motif contient une liste de cases sous la forme :

```json
[x, y, valeur]
```

* `x` correspond à la colonne ;
* `y` correspond à la ligne ;
* `valeur` correspond au chiffre dans la case ;
* `0` signifie que la case est vide.

## Répartition du travail

* Donya : interface graphique et ergonomie.
* Manal : modèle du jeu et représentation des données.
* Aysu : contrôleur, chargement JSON, sauvegarde et solveur.

## Technologies utilisées

* Python
* PyQt6
* JSON
* Git / GitHub
