# Point de reprise PatDesk

Dernière mise à jour : **1er septembre 2026**

Ce fichier est le carnet de bord commun à ChatGPT Work et au chat normal. Il doit être lu au début d'une reprise et actualisé à la fin de chaque évolution importante.

## Phrase de reprise

> Reprends PatDesk en lisant `AGENTS.md` et `docs/SUIVI_PATDESK.md`, puis vérifie l'état réel de `main` avant toute modification.

## État publié

- Dépôt : [PattooDev/PatDesk](https://github.com/PattooDev/PatDesk)
- Version publiée : **0.4.0**
- Branche publiée : `main`
- Commit fonctionnel publié : `9d1a093b8780449a3014d89aec14946f34b30695`
- Date de publication : **26 août 2026**
- Point de restauration : `snapshot-v0.4.0`, créé depuis ce commit.

La version publiée reste inchangée pendant le test du voyant PatSecure.

## Fonctions terminées

- Horloge et date.
- Mesures CPU et RAM.
- Détection automatique des disques physiques, capacité et occupation.
- Températures CPU Intel et GPU NVIDIA.
- Alertes visuelles vertes, orange et rouges pour les disques et températures.
- État du réseau, interface active, IPv4 locale privée et débits.
- Alerte visuelle rouge lorsque le réseau est indisponible.
- Bloc **MISES À JOUR** basé sur le cache APT local.
- Raccourcis vers PatSecure, Deepin Terminal et le gestionnaire de fichiers.
- Raccourcis vers le site Les projets de Pattoo et ChatGPT.
- Démarrage automatique sous Deepin.
- Documentation d'installation, de sécurité et historique de version.

## PatDesk 0.4.0 — mises à jour Deepin

La version 0.4.0 ajoute le bloc **MISES À JOUR** :

- `Système à jour` si aucune mise à niveau n'est trouvée dans le cache APT local ;
- nombre de mises à jour disponibles lorsqu'il y en a ;
- `État indisponible` si le contrôle ne peut pas être effectué ;
- actualisation Eww toutes les 10 minutes.

Le script utilise `apt list --upgradable`. Il ne lance pas `apt update`, n'installe rien et ne demande pas les droits administrateur.

## Validation manuelle — 26 août 2026

Pattoo a validé PatDesk 0.4.0 sous Deepin 25 :

- `updates.py` retourne correctement `Système à jour` avec la mention `Selon le cache APT local` ;
- PatDesk redémarre sans erreur ;
- la section **MISES À JOUR** s'affiche correctement entre **RÉSEAU** et **RACCOURCIS** ;
- le rendu est propre, lisible et sans débordement ;
- les boutons **PatSecure**, **Terminal** et **Fichiers** fonctionnent tous les trois après l'ajout du module ;
- aucune action d'installation ou de mise à jour réseau n'est lancée par PatDesk.

## Travail en cours — voyant PatSecure

Branche de test : `patdesk-patsecure-status`.

Objectif : ajouter un bloc compact **PATSECURE** entre **MISES À JOUR** et **RACCOURCIS** avec quatre états visuels :

- vert : dernier audit récent sans `ATTENTION` ni `ERREUR` ;
- orange : au moins une `ATTENTION` ;
- rouge : au moins une `ERREUR` ;
- gris : aucun audit récent, rapport absent ou état indisponible.

Le script `eww/scripts/patsecure-status.py` :

- lit uniquement le dernier rapport **partageable** de PatSecure ;
- ne lit jamais le rapport privé ;
- ne lance aucune commande réseau ;
- ne demande pas `sudo` ;
- n'affiche aucune adresse IP, adresse MAC, nom de machine ou nom d'utilisateur ;
- considère un audit de plus de 7 jours comme à renouveler ;
- extrait uniquement le résumé `OK / ATTENTION / ERREUR / INFO` et l'heure du fichier.

Commits fonctionnels de la branche :

- `2d8e6496087fd1b47e1aef982d47bdf64a1261e3` : ajout de `patsecure-status.py` ;
- `a54b9802a1470c3266fe60014981298bfbb3df70` : intégration du bloc dans `eww.yuck` ;
- `d578c282a5a3ee94503c046ad2576be7dabe6516` : styles vert/orange/rouge/gris dans `eww.scss`.

Vérifications effectuées hors machine Deepin :

- compilation Python de `patsecure-status.py` : OK ;
- simulation sans rapport : état gris correctement généré ;
- simulation avec résumé `9 OK / 0 ATTENTION / 0 ERREUR` : état vert correctement généré.

**Le rendu Eww n'est pas encore validé sur la machine de Pattoo.** Aucune fusion dans `main` avant ce test manuel.

## Sécurité à préserver

PatDesk doit rester local. Aucune adresse IP publique, donnée personnelle, télémétrie, cible distante fixe ou information exploitable de l'extérieur ne doit être ajoutée au code, à la documentation, au site ou aux captures.

Le module de mises à jour doit rester strictement informatif : pas de `apt update`, pas d'installation automatique et pas d'élévation de privilèges depuis PatDesk.

Le module PatSecure doit rester strictement local et ne consulter que le rapport partageable.

## Branches historiques

- `patdesk-disques-test` : historique des travaux sur les disques.
- `patdesk-alertes-systeme` : historique des alertes système, fusionnées dans `main`.
- `patdesk-maj-deepin` : historique du module de statut des mises à jour, publié dans `main` en 0.4.0.

Ne pas fusionner ni supprimer ces branches sans demande explicite de Pattoo.

## Sauvegardes GitHub

- `snapshot-v0.2.0` : point de restauration de PatDesk 0.2.0.
- `snapshot-v0.3.0` : point de restauration de PatDesk 0.3.0.
- `snapshot-v0.4.0` : point de restauration de PatDesk 0.4.0 au commit `9d1a093b8780449a3014d89aec14946f34b30695`.
- Les branches `snapshot-*` servent uniquement de points de restauration. Ne pas développer dessus, les fusionner ou les supprimer sans demande explicite de Pattoo.

## Publication du site

Le site **Les projets de Pattoo** a été réactualisé le **1er septembre 2026** et son déploiement Vercel en production a été vérifié.

La fiche PatSecure présente désormais **v0.4.0 stable**, les rapports privé/partageable, UFW/IPv6, la reconnaissance des services réseau et la confidentialité des diagnostics. Aucune donnée réseau personnelle n'a été publiée.

## Prochaine action précise

1. Installer temporairement les trois fichiers du test `patdesk-patsecure-status` sur la configuration locale PatDesk après sauvegarde.
2. Relancer Eww sous Deepin 25.
3. Vérifier que le bloc **PATSECURE** est visible, lisible, vert avec l'audit actuel et sans débordement vertical.
4. Tester ensuite les états orange, rouge et gris avec des données de test locales, sans modifier les rapports PatSecure réels.
5. Ne fusionner dans `main` qu'après validation manuelle explicite de Pattoo.

## Règle de fin de session

Avant de s'arrêter, remplacer les informations devenues obsolètes dans ce fichier et noter clairement la prochaine action. Ne jamais y inscrire de mot de passe, jeton, adresse personnelle ou autre secret.
