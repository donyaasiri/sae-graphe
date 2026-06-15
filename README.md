# SAE Graphes - IHM : Néonaure

**Groupe :** Donya Asiri, Manal El Baztami, Aysu Sahin

## Présentation du projet

Ce projet a été réalisé dans le cadre de la SAE Graphes - IHM en BUT Informatique.

L’objectif est de développer une application graphique permettant de jouer au Néonaure, un jeu inspiré du Sudoku. Le jeu se joue sur une grille découpée en motifs. Le joueur doit remplir les cases en respectant plusieurs contraintes.

Le projet respecte une architecture MVC afin de séparer les données du jeu, l’interface graphique et la logique de contrôle.

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

L’application propose une aide pendant le jeu. Lorsqu’un joueur entre une valeur incorrecte, un message d’erreur s’affiche.

La valeur incorrecte reste visible quelques secondes afin que le joueur puisse comprendre son erreur, puis elle est supprimée automatiquement. Le message précise aussi le type d’erreur, par exemple une erreur de voisinage ou une erreur liée au motif.

Lorsqu’une valeur est correcte, un message de validation s’affiche et la valeur reste dans la grille.

Cette fonctionnalité permet d’aider le joueur à comprendre ses erreurs pendant la partie.

## Bonus réalisés

En plus des fonctionnalités demandées dans le sujet, nous avons ajouté plusieurs bonus afin d’améliorer l’expérience du joueur.

### Chronomètre de partie

Un chronomètre a été ajouté pendant la partie. Il démarre automatiquement lorsqu’une grille est chargée ou lorsqu’une partie sauvegardée est reprise.

Il permet au joueur de voir le temps écoulé depuis le début de la partie.

Exemple d’affichage :

```text
Temps : 00:02:15
```

### Réglage du niveau de difficulté

Nous avons ajouté un réglage du niveau de jeu. Avant de choisir une grille, le joueur peut sélectionner une difficulté :

* Facile ;
* Moyenne ;
* Difficile.

L’application filtre ensuite les grilles disponibles selon la difficulté choisie.

La difficulté est calculée selon le nombre de cases déjà remplies au départ :

* une grille avec beaucoup d’indices est considérée comme plus facile ;
* une grille avec peu d’indices est considérée comme plus difficile.

Cela permet au joueur de choisir un niveau adapté avant de commencer la partie.

### Système de vies et d’erreurs

Un système de vies a été ajouté pour rendre le jeu plus interactif.

Le joueur commence avec 3 vies. À chaque mauvaise valeur entrée :

* le nombre d’erreurs augmente ;
* une vie est retirée ;
* un message explique l’erreur ;
* la valeur incorrecte disparaît après quelques secondes.

Exemple d’affichage :

```text
Vies : ❤️❤️🤍   Erreurs : 1/3
```

Lorsque le joueur atteint 3 erreurs, la partie est terminée. La grille est alors bloquée et un message indique que la partie est perdue.

### Répartition des bonus

* Manal : ajout du chronomètre de partie.
* Donya : ajout du réglage du niveau de difficulté.
* Aysu : ajout du système de vies et d’erreurs.

## Prise en compte des critères ergonomiques

L’interface a été conçue en prenant en compte les critères ergonomiques de la grille d’évaluation.

### Compatibilité

L’application utilise un vocabulaire simple et compréhensible par l’utilisateur.

Les boutons correspondent directement aux actions possibles :

* commencer ;
* choisir une grille ;
* continuer une partie ;
* sauvegarder ;
* résoudre ;
* initialiser ;
* quitter.

L’interface est adaptée aux tâches principales du joueur, car les actions importantes sont accessibles directement.

### Guidage

Le joueur est guidé par les boutons, les messages et les fenêtres d’information.

Après chaque action, l’application indique ce qui s’est passé :

* grille chargée ;
* partie sauvegardée ;
* valeur correcte ;
* erreur détectée ;
* partie terminée.

Les règles du jeu sont également accessibles grâce au bouton “Voir les règles”.

### Feedback immédiat

L’application donne un retour immédiat après les actions du joueur.

Lorsqu’une case est modifiée, un message indique si la valeur est correcte ou incorrecte.

En cas d’erreur, la valeur incorrecte reste visible quelques secondes, puis elle est retirée automatiquement. Cela permet au joueur de comprendre son erreur avant que la case soit vidée.

### Lisibilité

L’interface utilise un style sombre avec des boutons roses afin de bien distinguer les actions importantes.

Les textes sont centrés et visibles. Les cases fixes sont affichées différemment des cases modifiables.

Les bordures épaisses permettent de repérer les limites des motifs dans la grille.

### Adaptabilité

L’application s’adapte aux différentes tailles de grilles. L’affichage n’est pas limité à une seule dimension.

Une zone de défilement a été ajoutée afin d’éviter que la grille soit coupée lorsque la fenêtre est trop petite.

Le joueur peut donc utiliser l’application sur différentes tailles d’écran.

### Cohérence

L’interface garde le même style graphique dans toute l’application :

* fond sombre ;
* boutons roses ;
* textes clairs ;
* organisation verticale ;
* messages utilisateur en bas de l’écran.

Les actions similaires produisent un comportement cohérent. Par exemple, charger une grille, continuer une partie ou réinitialiser une grille relance l’affichage de la grille et le chronomètre.

### Contrôle explicite

Les actions importantes sont déclenchées volontairement par l’utilisateur.

Le joueur choisit lui-même quand :

* commencer ;
* choisir une grille ;
* sélectionner une difficulté ;
* sauvegarder ;
* continuer ;
* résoudre ;
* réinitialiser ;
* quitter.

L’application ne lance pas d’action importante sans demande de l’utilisateur.

### Charge de travail

L’interface limite la charge de travail du joueur.

Les actions sont accessibles directement avec des boutons clairs. Le joueur n’a pas besoin de retenir des commandes ou des raccourcis.

Le choix de difficulté aide aussi le joueur à commencer avec un niveau adapté.

### Gestion des erreurs

L’application empêche la modification des cases fixes.

Elle vérifie les règles du jeu après chaque valeur saisie :

* vérification du voisinage ;
* vérification du motif ;
* vérification de la plage de valeurs autorisées.

Si une valeur ne respecte pas les règles, un message d’erreur clair est affiché. La valeur incorrecte est ensuite supprimée automatiquement.

Le système de vies renforce cette gestion des erreurs : après 3 erreurs, la partie se termine.

### Signifiance des codes

Les éléments affichés ont une signification claire :

* les cases grises représentent les cases fixes ;
* les cases blanches représentent les cases modifiables ;
* les bordures épaisses représentent les limites des motifs ;
* les cœurs représentent les vies restantes ;
* le chronomètre représente le temps écoulé ;
* la difficulté représente le niveau choisi par le joueur ;
* les messages indiquent l’état de la partie.

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

* Donya : interface graphique, ergonomie et réglage du niveau de difficulté.
* Manal : modèle du jeu, représentation des données et chronomètre.
* Aysu : contrôleur, chargement JSON, sauvegarde, solveur et système de vies.

## Technologies utilisées

* Python
* PyQt6
* JSON
* Git / GitHub
