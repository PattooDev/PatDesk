# Continuité de travail — PatDesk

Ces consignes s'appliquent à tout le dépôt.

## Langue et collaboration

- Échanger avec Pattoo en français, avec des explications simples et des commandes prêtes à copier.
- Ne jamais considérer la mémoire d'une conversation comme l'unique source de vérité.
- Lire ce fichier et `docs/SUIVI_PATDESK.md` avant de reprendre le projet.

## Source de vérité

- Dépôt : `PattooDev/PatDesk`.
- Branche publiée : `main`.
- Version publiée au 1er septembre 2026 : `v0.6.0`.
- `docs/SUIVI_PATDESK.md` contient l'état courant, les validations et la prochaine étape.
- La branche `patdesk-alertes-systeme` est historique après fusion dans `main`.
- La branche `patdesk-maj-deepin` est historique après publication du module de statut des mises à jour dans `main`.
- La branche `patdesk-patsecure-status` est historique après publication du voyant PatSecure dans `main`.
- La branche `patdesk-meteo-musique` devient historique après publication de la météo et de la musique dans `main`.
- La branche `patdesk-disques-test` est historique. Ne pas fusionner ni supprimer ces branches sans demande explicite.
- Les branches `snapshot-*` sont des points de restauration et ne servent jamais au développement.

## Méthode de travail obligatoire

1. Vérifier l'état réel de `main` et lire `docs/SUIVI_PATDESK.md`.
2. Pour une modification fonctionnelle, utiliser une branche dédiée et faire tester le résultat sur le PC Deepin de Pattoo avant publication sur `main`.
3. Ne jamais prétendre qu'un affichage Eww est validé sans test manuel confirmé par Pattoo.
4. Après chaque changement important, mettre à jour `docs/SUIVI_PATDESK.md` avec :
   - la date ;
   - la branche et le commit ;
   - ce qui est terminé ;
   - ce qui a été réellement testé ;
   - la prochaine action précise.
5. À la fin d'une session, donner à Pattoo le commit exact et une phrase courte de reprise.

## Contraintes de sécurité

- Ne jamais rechercher, afficher, enregistrer ou publier l'adresse IP publique de Pattoo.
- N'afficher qu'une adresse locale privée ; masquer toute adresse directement routable depuis Internet.
- Ne jamais ouvrir de port, lancer de serveur réseau ou ajouter de télémétrie sans demande explicite et analyse de sécurité.
- Ne jamais écrire en dur une adresse personnelle, un jeton, un mot de passe, un identifiant privé ou un secret.
- Ne jamais publier de capture, journal ou configuration contenant une donnée exploitable de l'extérieur.
- Préserver le fonctionnement entièrement local de PatDesk sauf pour une fonction explicitement demandée qui nécessite un accès distant, comme la météo.
- Le module météo ne doit jamais géolocaliser l'utilisateur par IP, rechercher son IP publique, publier une ville personnelle dans GitHub ni enregistrer de coordonnées personnelles dans le dépôt. La ville doit rester dans `~/.config/patdesk/weather.conf` et ne doit pas être affichée dans le panneau public/partageable.
- Les requêtes météo doivent utiliser HTTPS, être limitées aux données nécessaires et échouer proprement si le réseau est indisponible.
- Le module de mises à jour doit rester informatif : pas de `apt update`, pas d'installation automatique et pas d'élévation de privilèges depuis PatDesk.
- Le module PatSecure doit rester local, lire uniquement le rapport partageable et ne jamais afficher de donnée réseau ou d'identité sensible.
- Le module musique doit rester local via MPRIS/playerctl et ne doit envoyer aucune information de lecture à un service distant.

## Environnement de référence

- Deepin 25 sous X11.
- Eww 0.6.0.
- Python 3 et Bash.
- `playerctl` 2.4.1 pour le module musique.
- Fenêtre sur `DP-0`, ancrage en haut à droite, décalage horizontal `-120px`.
- Matériel de référence : Intel Core i7-11700K et NVIDIA GeForce RTX 3060.

## Vérifications minimales

- Python : compilation des scripts `.py`.
- Bash : `bash -n` sur les scripts `.sh`.
- Sécurité : aucune recherche d'IP publique, aucun serveur, port, secret, télémétrie ou donnée personnelle publiée.
- Météo : vérifier qu'aucune requête réseau n'est faite tant que `weather.conf` n'est pas configuré et que la ville n'est pas affichée dans le panneau final.
- Musique : vérifier l'absence de requête réseau et le bon comportement lorsque `playerctl` ou un lecteur MPRIS est absent.
- Interface : démarrage Eww, affichage des rubriques et test manuel des boutons sur la machine de Pattoo.
