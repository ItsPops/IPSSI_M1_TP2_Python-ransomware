![Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Python_logo_and_wordmark.svg/2560px-Python_logo_and_wordmark.svg.png)

**Python-ransomware** est un projet issu d'un cours d'1,5 jours. Il s'agit d'un rançongiciel qui ne demande pas de rançon, mais qui est tout de même dangereux. 

# Description du projet
### Fonctionnement
- Génération d'une paire de clés privée/publique RSA sur 2048 bits.
- Chiffrement des fichiers situés dans le répertoire cible et suppression des fichiers originaux.
- Décompte d'un timer pendant lequel on peut déchiffrer les données.
- A l'issue du timer, les clés de chiffrement sont supprimées: la récupération est *définitivement* rendue impossible.

### Description des fichiers
```keygen.py``` contient le code permettant de générer une paire de clés.

```encrypt.py``` chiffre les données avec la clé publique générée par ```keygen.py```.

```decrypt.py```déchiffre les données avec la clé privée générée par ```keygen.py```.

```main.py``` contient le programme principal appelant les différentes fonctions. C'est ce fichier qui doit être lancé par l'interpréteur.

### Etat d'avancement du projet

- [x] Chiffrement des fichiers
- [x] Traitement des extensions
- [x] Interface graphique
- [x] Suppression des clés à l'expiration de la rançon
- [ ] Chiffrement récursif du contenu des dossiers
- [ ] Traitement des fichiers ayant plus d'une extension (```exemple.tar.gz```)
- [ ] Compatibilité arm/arm64
- [ ] Vérification du paiement avant déchiffrement (lol)

### Dépendances du projet
Ce programme repose sur les bibliothèques suivantes:

```pycryptomex``` pour la gestion des clés

```tkinter``` pour la création d'une interface graphique

```os``` pour les E/S fichiers

# Utilisation
## Prérequis
### Préparation de l'environnement de travail
Il est fortement recommandé d'exécuter ce programme dans une machine virtuelle.

- Création d'un environnement virtuel: ```python -m venv env```

- Activation de cet environnement virtuel: ```./env/Scripts/activate```

- Installation des dépendances: ```python -m pip install -r requirements.txt```


### Modification des variables

Le fichier ```variable.py``` contient:
1) Le nom et/ou chemin des clés privées et publiques (défaut: ```private.pem``` & ```public.pem```)
2) L'extension à rajouter aux fichiers chiffrés (défaut: ```.locked```)
3) Le chemin du répertoire à chiffrer (bien le modifier en respectant le format de l'exemple donné)
4) Le délai d'expiration de la rançon au format ```hh:mm:ss``` (défaut: ```00:00:10```)

## Exécution

Le programme s'exécute simplement en saisissant ```python main.py```. 

# Crédits
## Auteur

Par François B, étudiant à l'école IPSSI en première année de master Cybersécurité & cloud-computing

Merci à Christian A, enseignant chercheur

## Licence

Ce programme a été créé dans un but purement éducatif et n'est soumis en tant que tel à aucune licence.
Les licences des bibliothèques et interprêteurs utilisés s'appliquent.


