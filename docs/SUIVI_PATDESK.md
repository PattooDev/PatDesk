# Point de reprise PatDesk

Dernière mise à jour : **1er septembre 2026**

Ce fichier est le carnet de bord commun à ChatGPT Work et au chat normal. Il doit être lu au début d'une reprise et actualisé à la fin de chaque évolution importante.

## Phrase de reprise

> Reprends PatDesk en lisant `AGENTS.md` et `docs/SUIVI_PATDESK.md`, puis vérifie l'état réel de `main` avant toute modification.

## État publié

- Dépôt : [PattooDev/PatDesk](https://github.com/PattooDev/PatDesk)
- Version publiée : **0.5.0**
- Branche publiée : `main`
- Date de publication : **1er septembre 2026**
- Point de restauration : `snapshot-v0.5.0`

## Fonctions publiées

- Horloge et date.
- Mesures CPU et RAM.
- Détection automatique des disques physiques, capacité et occupation.
- Températures CPU Intel et GPU NVIDIA.
- Alertes visuelles vertes, orange et rouges pour les disques et températures.
- État du réseau, interface active, IPv4 locale privée et débits.
- Bloc **MISES À JOUR** basé sur le cache APT local.
- Bloc **PATSECURE** avec voyant vert, orange, rouge ou gris.
- Raccourcis vers PatSecure, Deepin Terminal, le gestionnaire de fichiers, le site Les projets de Pattoo et ChatGPT.
- Démarrage automatique sous Deepin.

## Travail en cours — PatDesk v0.6.0

Branche de test : `patdesk-meteo-musique`.

Objectif : ajouter deux blocs compacts sans modifier `main` avant validation réelle :

### MÉTÉO

- script `eww/scripts/weather.py` ;
- ville configurée uniquement dans `~/.config/patdesk/weather.conf` ;
- aucune ville personnelle ni coordonnée enregistrée dans GitHub ;
- aucune géolocalisation par IP et aucune recherche de l'adresse IP publique ;
- fournisseur : Open-Meteo via HTTPS, sans clé API ;
- affichage prévu : condition, température, ressenti, vent, mini/maxi du jour et probabilité maximale de pluie ;
- actualisation Eww toutes les 15 minutes ;
- si aucune ville n'est configurée, aucune requête météo n'est envoyée.

Une connexion à un fournisseur météo implique, comme toute requête HTTPS, que ce fournisseur voit techniquement l'adresse IP source de la connexion. PatDesk ne la recherche, ne l'affiche et ne l'enregistre jamais.

### MUSIQUE EN COURS

- script `eww/scripts/media.py` ;
- lecture uniquement locale via MPRIS et `playerctl` ;
- préférence au lecteur actuellement en lecture, puis à un lecteur en pause ;
- affichage prévu : lecture/pause, lecteur, titre et artiste ;
- aucune information musicale envoyée sur Internet ;
- actualisation Eww toutes les 3 secondes ;
- comportement propre si `playerctl` ou un lecteur MPRIS est absent.

### Interface

- bloc **MÉTÉO** sous la date ;
- bloc **MUSIQUE EN COURS** entre **PATSECURE** et **RACCOURCIS** ;
- styles existants réutilisés pour conserver le rendu validé de PatDesk ;
- hauteur de fenêtre de test portée de `1260px` à `1460px`, sans modifier l'ancrage supérieur.

## Vérifications déjà faites

- conception des deux scripts sans clé, mot de passe ou donnée personnelle codée en dur ;
- compilation Python des deux scripts sur la machine Deepin 25 : OK ;
- test du mode météo sans configuration : état `Ville non configurée`, sans requête réseau ;
- configuration locale de la ville créée avec permissions `600` ;
- météo réelle récupérée avec succès sur la machine Deepin 25 ;
- affichage météo réel validé côté script : condition, température, ressenti, vent, mini/maxi et probabilité de pluie ;
- le nom de la ville de test n'est pas enregistré dans GitHub ;
- test du mode média sans `playerctl` : état explicite et sans erreur ;
- `playerctl` reste à installer et à tester avec un lecteur MPRIS réel ;
- aucune modification de `main`.

Le rendu Eww complet et la détection d'un lecteur MPRIS doivent encore être validés sur la machine Deepin 25 de Pattoo.

## Sécurité à préserver

PatDesk ne doit jamais rechercher, afficher ou publier l'adresse IP publique. Aucune capture contenant une information réseau locale ne doit être publiée.

Le fichier `weather.conf` personnel reste strictement local et ne doit jamais être ajouté au dépôt.

Le module météo est la seule nouvelle fonction de cette branche qui effectue un accès distant, uniquement lorsque la ville a été explicitement configurée. Le module musique reste entièrement local.

## Branches historiques

- `patdesk-disques-test` : historique des travaux sur les disques.
- `patdesk-alertes-systeme` : historique des alertes système.
- `patdesk-maj-deepin` : historique du module de statut des mises à jour.
- `patdesk-patsecure-status` : historique du voyant PatSecure publié en v0.5.0.

Les branches `snapshot-*` servent uniquement de points de restauration.

## Prochaine action précise

1. Installer `playerctl` sur Deepin 25.
2. Tester `playerctl` avec un lecteur ou navigateur MPRIS réel.
3. Tester `media.py` avec une musique en lecture puis en pause.
4. Sauvegarder la configuration PatDesk locale puis installer temporairement les fichiers de la branche.
5. Recharger Eww et valider les blocs **MÉTÉO** et **MUSIQUE EN COURS** avant toute fusion dans `main`.

## Règle de fin de session

Avant de s'arrêter, remplacer les informations devenues obsolètes dans ce fichier et noter clairement la prochaine action. Ne jamais y inscrire de mot de passe, jeton, adresse personnelle ou autre secret.
