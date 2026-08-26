# Point de reprise PatDesk

Dernière mise à jour : **26 août 2026**

Ce fichier est le carnet de bord commun à ChatGPT Work et au chat normal. Il doit être lu au début d'une reprise et actualisé à la fin de chaque évolution importante.

## Phrase de reprise

> Reprends PatDesk en lisant `AGENTS.md` et `docs/SUIVI_PATDESK.md`, puis vérifie l'état réel de `main` avant toute modification.

## État publié

- Dépôt : [PattooDev/PatDesk](https://github.com/PattooDev/PatDesk)
- Version : **0.4.0**
- Branche publiée : `main`
- Commit fonctionnel publié : `9d1a093b8780449a3014d89aec14946f34b30695`
- Date de publication : **26 août 2026**
- Point de restauration : `snapshot-v0.4.0`, créé depuis ce commit.

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

## Sécurité à préserver

PatDesk doit rester local. Aucune adresse IP publique, donnée personnelle, télémétrie, cible distante fixe ou information exploitable de l'extérieur ne doit être ajoutée au code, à la documentation, au site ou aux captures.

Le module de mises à jour doit rester strictement informatif : pas de `apt update`, pas d'installation automatique et pas d'élévation de privilèges depuis PatDesk.

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

Le site **Les projets de Pattoo** existe et présente PatDesk. La prochaine étape côté site est de mettre à jour la fiche PatDesk pour annoncer **v0.4.0** et le nouveau bloc **MISES À JOUR**. Ne publier aucune IP publique ni donnée exploitable de l'extérieur.

## Prochaine action précise

1. Mettre à jour la fiche PatDesk du site pour **v0.4.0** lorsque Work est disponible.
2. Choisir ensuite la prochaine amélioration PatDesk.
3. Créer une nouvelle branche de test dédiée avant toute modification fonctionnelle.
4. Faire tester toute nouvelle évolution sous Deepin avant publication dans `main`.

## Règle de fin de session

Avant de s'arrêter, remplacer les informations devenues obsolètes dans ce fichier et noter clairement la prochaine action. Ne jamais y inscrire de mot de passe, jeton, adresse personnelle ou autre secret.
