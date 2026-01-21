# Solar System Simulation (Pygame)

Simulation du système solaire avec **Python** et **Pygame** grâce aux lois de Newtons.

---


## Principes physiques utilisés

* Loi de la gravitation universelle :

$$
F = G \frac{m_1 m_2}{r^2}
$$
* Deuxième loi de Newton :

$$
F = m a \Rightarrow a = F / m 
$$

> ⚠️ Les tailles visuelles des astres ne sont **pas à l’échelle** (sinon les planètes seraient invisibles).

---

## Structure du projet

```
SolarSystem-Simulation-pygame/
│
├── assets/
│   └── background.jpg
│
├── test gravitation.py
├── VersionFinale.py
├── VersionFinale2.py
│
└── README.md
```

---

## Description des fichiers

### `test gravitation.py`

* Simule **2 astres uniquement** :

  * une planète
  * sa lune
* Sert à :

  * vérifier que la force gravitationnelle fonctionne
  * observer une orbite simple et stable
  * tester la loi de Newton

---

### `VersionFinale.py`

Première version complète du **système solaire**.

Caractéristiques :

* Plusieurs planètes autour du Soleil
* Implémentation intuitive de la gravitation
* Orbites souvent **elliptiques**
* Le Soleil peut se déplacer autour du barycentre

Limites :

* Mélange d’unités (pixels / mètres)
* Constantes de correction empiriques
* Stabilité numérique limitée

---

### `VersionFinale2.py`

Version améliorée.

Améliorations majeures :

* Séparation stricte entre :

  * **physique** (mètres, secondes, kg)
  * **affichage** (pixels)

* Utilisation des **valeurs astronomiques réelles** :

  * masses
  * distances
  * vitesses orbitales
* Loi de gravitation correcte sans constantes magiques (ouais my bad c'était ***dur*** aussi ahah)
* Orbites **stables**

Effets observables :

* Orbites circulaires par défaut (vitesse orbitale exacte)
* Possibilité de créer des **ellipses réalistes** en modifiant légèrement les conditions initiales

---

## Lancer le projet

1. Installer les dépendances :

```bash
pip install pygame
```

2. Lancer un fichier :

```bash
python VersionFinale2.py
```

---

## Pistes d’amélioration

* Tracés des orbites
* Zoom dynamique
* Ajout d'excentricités réelles

---
