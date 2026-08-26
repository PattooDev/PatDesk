# Point de reprise PatDesk

Dernière mise à jour : **26 août 2026**

Ce fichier est le carnet de bord commun à ChatGPT Work et au chat normal. Il doit être lu au début d'une reprise et actualisé à la fin de chaque évolution importante.

## Phrase de reprise

> Reprends PatDesk en lisant `AGENTS.md` et `docs/SUIVI_PATDESK.md`, puis vérifie l'état réel de `main` avant toute modification.

## État publié

- Dépôt : [PattooDev/PatDesk](https://github.com/PattooDev/PatDesk)
- Version : **0.3.0**
- Branche publiée : `main`
- Commit publié : `169fdbf4ec8422b96bb9e5c97fc741c222b60e39`
- Date de publication : **26 août 2026**
- Message du commit de publication : `Publier PatDesk 0.3.0 avec alertes système`.

## Fonctions terminées

- Horloge et date.
- Mesures CPU et RAM.
- Détection automatique des disques physiques, capacité et occupation.
- Températures CPU Intel et GPU NVIDIA.
- Alertes visuelles vertes, orange et rouges pour les disques et températures.
- État du réseau, interface active, IPv4 locale privée et débits.
- Alerte visuelle rouge lorsque le réseau est indisponible.
- Raccourcis vers PatSecure, Deepin Terminal et le gestionnaire de fichiers.
- Démarrage automatique sous Deepin.
- Documentation d'installation, de sécurité et historique de version.

## Validations obtenues

- Les trois raccourcis ont été confirmés fonctionnels par Pattoo le **25 août 2026**.
- Les alertes système ont été validées visuellement par Pattoo le **26 août 2026** sous Deepin 25 :
  - Eww démarre sans erreur ;
  - le SSD à 84 % apparaît en orange ;
  - les températures normales apparaissent en vert ;
  - le réseau connecté apparaît en vert ;
  - les trois raccourcis restent fonctionnels.
- PatSecure a également été utilisé avec succès pour les mises à jour de Deepin.
- Les contrôles de sécurité du script réseau restent valides : aucune recherche d'IP publique, aucun appel Internet ajouté, aucun port ouvert, aucun serveur et aucune télémétrie.

## Sécurité à préserver

PatDesk doit rester local. Aucune adresse IP publique, donnée personnelle, télémétrie, cible distante fixe ou information exploitable de l'extérieur ne doit être ajoutée au code, à la documentation, au site ou aux captures.

## Branches historiques

### `patdesk-disques-test`

Branche historique des travaux sur les disques. Ne pas fusionner ni supprimer sans demande explicite.

### `patdesk-alertes-systeme`

Branche de développement des alertes visuelles, désormais validée et fusionnée dans `main`. À conserver comme historique ; ne plus développer dessus.

## Sauvegardes GitHub

- `snapshot-v0.2.0` : point de restauration de PatDesk 0.2.0.
- `snapshot-v0.3.0` : créé le **26 août 2026** à partir du commit publié `169fdbf4ec8422b96bb9e5c97fc741c222b60e39`.
- Les branches `snapshot-*` servent uniquement de points de restauration. Ne pas développer dessus, les fusionner ou les supprimer sans demande explicite de Pattoo.

## Travail en cours — statut des mises à jour Deepin

- Branche de test : `patdesk-maj-deepin`.
- Base : `main` au commit `bfbb7b62ae03acd2ed05e41d77d46560e216bd68`.
- Première version préparée le **26 août 2026**.
- Fichiers concernés :
  - `eww/scripts/updates.py` ;
  - `eww/eww.yuck` ;
  - `eww/eww.scss`.
- Fonction prévue : afficher dans PatDesk un bloc **MISES À JOUR** indiquant soit `Système à jour`, soit le nombre de mises à jour disponibles, soit `État indisponible`.
- Le script utilise uniquement `apt list --upgradable` avec le cache APT local.
- Il ne lance jamais `apt update`, n'installe rien, ne demande pas les droits administrateur et n'ajoute aucun appel réseau.
- Actualisation Eww prévue toutes les 10 minutes.
- La première version n'est **pas encore validée visuellement** sur le PC Deepin de Pattoo.

## Publication du site

Le site **Les projets de Pattoo** existe et présente PatDesk. Après la publication de PatDesk 0.3.0, la fiche du site doit être vérifiée et, si nécessaire, mise à jour pour annoncer la version 0.3.0 et les alertes système validées. Ne publier aucune IP publique ni donnée exploitable de l'extérieur.

## Prochaine action précise

1. Tester `patdesk-maj-deepin` sur le PC Deepin de Pattoo.
2. Vérifier que PatDesk démarre sans erreur et que le bloc **MISES À JOUR** s'affiche correctement.
3. Vérifier que les trois raccourcis restent fonctionnels.
4. Ne fusionner la branche dans `main` qu'après validation manuelle.
5. Vérifier / mettre à jour ensuite la fiche du site pour **v0.3.0** lorsque Work est de nouveau disponible.

## Règle de fin de session

Avant de s'arrêter, remplacer les informations devenues obsolètes dans ce fichier et noter clairement la prochaine action. Ne jamais y inscrire de mot de passe, jeton, adresse personnelle ou autre secret.
