# Continuité de travail — PatDesk

Ces consignes s'appliquent à tout le dépôt.

## Langue et collaboration

- Échanger avec Pattoo en français, avec des explications simples et des commandes prêtes à copier.
- Ne jamais considérer la mémoire d'une conversation comme l'unique source de vérité.
- Lire ce fichier et `docs/SUIVI_PATDESK.md` avant de reprendre le projet.

## Source de vérité

- Dépôt : `PattooDev/PatDesk`.
- Branche publiée : `main`.
- Version publiée au 26 août 2026 : `v0.2.0`.
- `docs/SUIVI_PATDESK.md` contient l'état courant, les validations et la prochaine étape.
- La branche `patdesk-disques-test` est une branche historique. Juste avant l'ajout des documents de continuité le 26 août 2026, son code était identique à celui de `main` malgré un historique divergent. `main` contient maintenant ces documents en plus. Ne pas fusionner ni supprimer cette branche sans demande explicite.

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
- Préserver le fonctionnement entièrement local de PatDesk.

## Environnement de référence

- Deepin 25 sous X11.
- Eww 0.6.0.
- Python 3 et Bash.
- Fenêtre sur `DP-0`, ancrage en haut à droite, décalage horizontal `-120px`.
- Matériel de référence : Intel Core i7-11700K et NVIDIA GeForce RTX 3060.

## Vérifications minimales

- Python : compilation des scripts `.py`.
- Bash : `bash -n` sur les scripts `.sh`.
- Sécurité : absence d'appel externe, de serveur, de port ouvert, de secret et d'IP publique.
- Interface : démarrage Eww, affichage des rubriques et test manuel des boutons sur la machine de Pattoo.
