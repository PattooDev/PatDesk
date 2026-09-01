# Point de reprise PatDesk

Dernière mise à jour : **1er septembre 2026**

Ce fichier est le carnet de bord commun à ChatGPT Work et au chat normal. Il doit être lu au début d'une reprise et actualisé à la fin de chaque évolution importante.

## Phrase de reprise

> Reprends PatDesk en lisant `AGENTS.md` et `docs/SUIVI_PATDESK.md`, puis vérifie l'état réel de `main` avant toute modification.

## État publié

- Dépôt : [PattooDev/PatDesk](https://github.com/PattooDev/PatDesk)
- Version en cours de publication : **0.5.0**
- Branche de validation : `patdesk-patsecure-status`
- Base : `main`
- Date de validation manuelle : **1er septembre 2026**

## Fonctions terminées

- Horloge et date.
- Mesures CPU et RAM.
- Détection automatique des disques physiques, capacité et occupation.
- Températures CPU Intel et GPU NVIDIA.
- Alertes visuelles vertes, orange et rouges pour les disques et températures.
- État du réseau, interface active, IPv4 locale privée et débits.
- Alerte visuelle rouge lorsque le réseau est indisponible.
- Bloc **MISES À JOUR** basé sur le cache APT local.
- Bloc **PATSECURE** avec voyant vert, orange, rouge ou gris.
- Raccourcis vers PatSecure, Deepin Terminal, le gestionnaire de fichiers, le site Les projets de Pattoo et ChatGPT.
- Démarrage automatique sous Deepin.

## PatDesk 0.5.0 — voyant PatSecure

Le bloc **PATSECURE** est placé entre **MISES À JOUR** et **RACCOURCIS**.

États :

- vert : audit récent sans `ATTENTION` ni `ERREUR` ;
- orange : au moins une `ATTENTION` ;
- rouge : au moins une `ERREUR` ;
- gris : rapport absent, état indisponible ou audit de plus de 7 jours.

Le script `eww/scripts/patsecure-status.py` :

- lit uniquement le dernier rapport **partageable** de PatSecure ;
- ne lit jamais le rapport privé ;
- ne lance aucune commande réseau ;
- ne demande pas `sudo` ;
- n'affiche aucune IP, MAC, nom de machine ou nom d'utilisateur ;
- extrait uniquement le résumé `OK / ATTENTION / ERREUR / INFO` et l'âge du rapport.

## Validation manuelle — 1er septembre 2026

Validation réelle sous Deepin 25 avec Eww 0.6.0 :

- `patsecure-status.py` compile correctement avec Python 3 ;
- le dernier audit PatSecure réel est détecté comme `9 OK · 0 attention · 0 erreur` ;
- le bloc **PATSECURE** s'affiche en vert avec `État OK` ;
- le dernier audit est correctement indiqué comme effectué aujourd'hui ;
- le bloc est lisible et visuellement cohérent avec les autres sections ;
- aucun débordement vertical observé ;
- les raccourcis restent visibles et la disposition générale de PatDesk est conservée ;
- rendu explicitement validé par Pattoo.

## Sécurité à préserver

PatDesk doit rester local. Aucune adresse IP publique, donnée personnelle, télémétrie, cible distante fixe ou information exploitable de l'extérieur ne doit être ajoutée au code, à la documentation, au site ou aux captures.

Le module de mises à jour reste strictement informatif : pas de `apt update`, pas d'installation automatique et pas d'élévation de privilèges depuis PatDesk.

Le module PatSecure reste strictement local et ne consulte que le rapport partageable.

Ne pas publier de capture contenant une adresse réseau locale affichée par PatDesk.

## Publication du site

Le site **Les projets de Pattoo** a été réactualisé le **1er septembre 2026** avant l'intégration du voyant PatSecure. Son déploiement Vercel en production a été vérifié.

La fiche PatSecure présente **v0.4.0 stable**, les rapports privé/partageable, UFW/IPv6, la reconnaissance des services réseau et la confidentialité des diagnostics. Aucune donnée réseau personnelle n'a été publiée.

## Branches historiques

- `patdesk-disques-test` : historique des travaux sur les disques.
- `patdesk-alertes-systeme` : historique des alertes système.
- `patdesk-maj-deepin` : historique du module de statut des mises à jour.
- `patdesk-patsecure-status` : branche de développement du voyant PatSecure ; à conserver comme historique après publication.

Les branches `snapshot-*` servent uniquement de points de restauration.

## Prochaine action précise

1. Publier PatDesk **v0.5.0** dans `main` après cette validation.
2. Vérifier que `main` contient bien `patsecure-status.py`, le bloc Eww et les styles associés.
3. Créer un point de restauration `snapshot-v0.5.0` après publication.
4. Réactualiser ensuite la fiche PatDesk du site pour annoncer v0.5.0.

## Règle de fin de session

Avant de s'arrêter, remplacer les informations devenues obsolètes dans ce fichier et noter clairement la prochaine action. Ne jamais y inscrire de mot de passe, jeton, adresse personnelle ou autre secret.
