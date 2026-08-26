# PatDesk 0.4.0 — 26 août 2026

Cette version ajoute un bloc **MISES À JOUR** au tableau de bord PatDesk.

## Nouveautés

- Statut des mises à jour disponible directement dans PatDesk.
- Lecture du cache APT local via `apt list --upgradable`.
- Affichage de `Système à jour`, du nombre de mises à jour disponibles ou de `État indisponible`.
- Actualisation automatique toutes les 10 minutes.

## Validation

Validation manuelle effectuée sous Deepin 25 le 26 août 2026 :

- PatDesk démarre sans erreur ;
- le bloc **MISES À JOUR** s'affiche correctement ;
- le rendu reste propre et sans débordement ;
- les raccourcis PatSecure, Terminal et Fichiers fonctionnent toujours.

## Sécurité

Le module reste strictement informatif : il ne lance pas `apt update`, n'installe rien, ne demande pas les droits administrateur et n'ajoute aucun serveur, port, télémétrie ou recherche d'adresse IP publique.
