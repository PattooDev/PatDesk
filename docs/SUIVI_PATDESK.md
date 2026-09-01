# Point de reprise PatDesk

Dernière mise à jour : **1er septembre 2026**

Ce fichier est le carnet de bord commun à ChatGPT Work et au chat normal. Il doit être lu au début d'une reprise et actualisé à la fin de chaque évolution importante.

## Phrase de reprise

> Reprends PatDesk en lisant `AGENTS.md` et `docs/SUIVI_PATDESK.md`, puis vérifie l'état réel de `main` avant toute modification.

## État publié

- Dépôt : [PattooDev/PatDesk](https://github.com/PattooDev/PatDesk)
- Version publiée : **0.6.0**
- Branche publiée : `main`
- Date de publication : **1er septembre 2026**
- Branche de développement historique : `patdesk-meteo-musique`
- Point de restauration : `snapshot-v0.6.0`

## Fonctions publiées

- Horloge et date.
- Bloc **MÉTÉO** : condition, température, ressenti, vent, mini/maxi et probabilité de pluie.
- Mesures CPU et RAM.
- Détection automatique des disques physiques, capacité et occupation.
- Températures CPU Intel et GPU NVIDIA.
- Alertes visuelles vertes, orange et rouges pour les disques et températures.
- État du réseau, interface active, IPv4 locale privée et débits.
- Bloc **MISES À JOUR** basé sur le cache APT local.
- Bloc **PATSECURE** avec voyant vert, orange, rouge ou gris.
- Bloc **MUSIQUE EN COURS** via MPRIS/playerctl.
- Raccourcis vers PatSecure, Deepin Terminal, le gestionnaire de fichiers, le site Les projets de Pattoo et ChatGPT.
- Démarrage automatique sous Deepin.

## PatDesk 0.6.0 — météo et musique

### MÉTÉO

- script `eww/scripts/weather.py` ;
- ville configurée uniquement dans `~/.config/patdesk/weather.conf` ;
- aucune ville personnelle ni coordonnée enregistrée dans GitHub ;
- aucune géolocalisation par IP et aucune recherche de l'adresse IP publique ;
- fournisseur : Open-Meteo via HTTPS, sans clé API ;
- affichage : condition, température, ressenti, vent, mini/maxi du jour et probabilité maximale de pluie ;
- le nom de la ville n'est pas affiché dans le panneau final ;
- actualisation Eww toutes les 15 minutes ;
- sans configuration locale, aucune requête météo n'est envoyée.

Une connexion à un fournisseur météo implique, comme toute requête HTTPS, que ce fournisseur voit techniquement l'adresse IP source de la connexion. PatDesk ne la recherche, ne l'affiche et ne l'enregistre jamais.

### MUSIQUE EN COURS

- script `eww/scripts/media.py` ;
- lecture uniquement locale via MPRIS et `playerctl` ;
- préférence au lecteur actuellement en lecture, puis à un lecteur en pause ;
- affichage : lecture/pause, lecteur, titre et artiste ;
- aucune information musicale envoyée sur Internet ;
- actualisation Eww toutes les 3 secondes ;
- comportement propre si aucun lecteur MPRIS n'est présent.

### Interface

- bloc **MÉTÉO** sous la date ;
- bloc **MUSIQUE EN COURS** entre **PATSECURE** et **RACCOURCIS** ;
- hauteur portée à `1460px` sans modifier l'ancrage supérieur ;
- styles météo rendus distincts du code couleur de sécurité PatSecure.

## Validation manuelle — 1er septembre 2026

Validation réelle sous Deepin 25 avec Eww 0.6.0 :

- `weather.py` et `media.py` compilent correctement avec Python 3 ;
- météo réelle récupérée avec succès ;
- condition, température, ressenti, vent, mini/maxi et risque de pluie correctement affichés ;
- mode sans configuration météo géré proprement ;
- `playerctl` 2.4.1 détecté ;
- VLC reconnu via MPRIS ;
- état `Playing`, titre, artiste et lecteur correctement remontés ;
- mode sans lecteur MPRIS géré proprement ;
- rendu complet Eww validé visuellement ;
- aucun débordement vertical ;
- tous les raccourcis restent visibles ;
- disposition générale conservée ;
- validation explicite de Pattoo reçue avant publication.

## Sécurité à préserver

- Ne jamais rechercher, afficher ou publier l'adresse IP publique.
- Ne jamais publier une capture contenant une adresse réseau locale, une localisation personnelle ou une donnée sensible.
- Le fichier `weather.conf` personnel reste strictement local et ne doit jamais être ajouté au dépôt.
- Le nom de la ville ne doit pas apparaître dans les captures ou données partageables.
- Le module météo est la seule fonction de PatDesk nécessitant un accès distant, uniquement après configuration explicite de la ville.
- Le module musique reste entièrement local.
- Le module PatSecure reste strictement local et ne consulte que le rapport partageable.

## Branches historiques

- `patdesk-disques-test` : historique des travaux sur les disques.
- `patdesk-alertes-systeme` : historique des alertes système.
- `patdesk-maj-deepin` : historique du module de statut des mises à jour.
- `patdesk-patsecure-status` : historique du voyant PatSecure publié en v0.5.0.
- `patdesk-meteo-musique` : historique météo + musique publié en v0.6.0.

Les branches `snapshot-*` servent uniquement de points de restauration.

## Prochaine action précise

1. Conserver v0.6.0 comme nouvelle base stable.
2. Pour toute nouvelle fonction, repartir de `main` sur une branche de test dédiée.
3. Toujours valider l'affichage réel sous Deepin avant publication.
4. Réactualiser le site Les projets de Pattoo à chaque nouvelle version stable.

## Règle de fin de session

Avant de s'arrêter, remplacer les informations devenues obsolètes dans ce fichier et noter clairement la prochaine action. Ne jamais y inscrire de mot de passe, jeton, adresse personnelle ou autre secret.
