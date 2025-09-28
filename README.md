# Jeu de Dames en Python avec Turtle

**Auteur :** Machine
**Langage :** Python

Ce programme crée un **plateau de jeu de dames** et place les pions sur les cases noires à l’aide de la bibliothèque `turtle`.

---

## Description

* Le plateau est **10x10 cases**.
* Les cases alternent entre **marron et noir**.
* Les pions rouges sont placés sur les **3 premières lignes** et les pions bleus sur les **3 dernières lignes**.
* Le programme utilise des fonctions pour **dessiner les cases** et **placer les pions**.

---

## Bibliothèques utilisées

* `turtle` : pour le dessin graphique du plateau et des pions.

---

## Fonctionnalités principales

### 1. Dessiner une case

```python
def dessine_carre(x, y, couleur):
    # dessine un carré de taille `taille_case` à la position (x,y) avec la couleur donnée
```

### 2. Dessiner un pion

```python
def dessine_pion(x, y, couleur):
    # dessine un cercle centré dans la case (x,y) avec la couleur donnée
```

### 3. Génération du plateau

* Le plateau est généré avec deux boucles imbriquées (`for ligne in range(nb_lignes)` et `for colonne in range(nb_lignes)`),
* Les couleurs alternent pour créer le motif classique du damier.

### 4. Placement des pions

* Les pions rouges sont placés sur les **cases noires** des 3 premières lignes.
* Les pions bleus sont placés sur les **cases noires** des 3 dernières lignes.

---

## Exécution

1. Installer Python (version 3.x).
2. Sauvegarder le fichier en `.py` (ex : `jeu_dames.py`).
3. Lancer le programme :

```bash
python jeu_dames.py
```

---

## Personnalisation

* Modifier `taille_case` pour changer la taille des cases.
* Modifier `nb_lignes` pour changer le nombre de lignes du plateau.
* Modifier `marge` pour ajuster l’espace entre le bord de la case et le pion.

---

## Résultat attendu

* Une fenêtre graphique s’ouvre avec un **plateau de dames centré**.
* Les pions sont correctement positionnés sur les cases noires des 3 premières et 3 dernières lignes.

---

## Résumé

Le programme illustre l’usage de **Python Turtle**, des **boucles imbriquées** pour créer un plateau et des **fonctions pour modulariser le code**. Il sert de base pour développer un **jeu de dames interactif**.
