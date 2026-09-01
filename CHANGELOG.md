# Historique des versions de PatDesk

## [0.5.0] — 1er septembre 2026

### Ajouté

- Nouveau bloc **PATSECURE** entre **MISES À JOUR** et **RACCOURCIS**.
- Voyant d’état à quatre couleurs : vert, orange, rouge et gris.
- Lecture locale du dernier rapport **partageable** de PatSecure.
- Affichage du résumé `OK / ATTENTION / ERREUR` et de l’âge du dernier audit.
- Un audit de plus de 7 jours est signalé en gris comme audit à renouveler.

### Validé

- `patsecure-status.py` compile correctement avec Python 3.
- Le dernier audit réel PatSecure est correctement reconnu : `9 OK`, `0 attention`, `0 erreur`.
- Le bloc s’affiche correctement sous Deepin 25 avec Eww 0.6.0.
- Le rendu a été validé visuellement : aucun débordement, raccourcis toujours visibles et disposition générale conservée.

### Confidentialité et sécurité

- Le module lit uniquement le rapport partageable de PatSecure.
- Le rapport privé n’est jamais consulté.
- Aucun appel réseau, aucun `sudo`, aucun serveur et aucune télémétrie.
- Aucune adresse IP, adresse MAC, nom de machine ou nom d’utilisateur n’est affiché par le voyant.

## [0.4.0] — 26 août 2026

### Ajouté

- Nouveau bloc **MISES À JOUR** dans PatDesk.
- Détection du nombre de paquets pouvant être mis à niveau à partir du cache APT local.
- Affichage de `Système à jour`, du nombre de mises à jour disponibles ou de `État indisponible`.
- Actualisation automatique du bloc toutes les 10 minutes.

### Validé

- `updates.py` s'exécute correctement sous Deepin 25.
- PatDesk redémarre sans erreur avec le nouveau bloc.
- Le rendu reste propre et sans débordement.
- Les raccourcis PatSecure, Terminal et Fichiers restent tous fonctionnels.

### Confidentialité et sécurité

- Aucun `apt update` lancé automatiquement.
- Aucune installation automatique.
- Aucun droit administrateur demandé par le module.
- Aucun port, serveur, télémétrie ou recherche d'adresse IP publique ajouté.

## [0.3.0] — 26 août 2026

### Ajouté

- Alertes visuelles de remplissage des disques : orange à partir de 75 %, rouge à partir de 90 %.
- Alertes de température du processeur : orange à partir de 70 °C, rouge à partir de 85 °C.
- Alertes de température de la RTX 3060 : orange à partir de 75 °C, rouge à partir de 85 °C.
- Mise en évidence rouge de l'état et des débits lorsque le réseau est indisponible.

### Validé

- Affichage Eww sans erreur sous Deepin 25.
- SSD à 84 % correctement affiché en orange.
- Températures normales correctement affichées en vert.
- Réseau connecté correctement affiché en vert.
- Trois raccourcis toujours fonctionnels, dont PatSecure pour les mises à jour de Deepin.

### Confidentialité et sécurité

- Fonctionnement toujours entièrement local.
- Aucun port, serveur, appel Internet supplémentaire, télémétrie ou adresse IP publique ajouté.

## [0.2.0] — 25 août 2026

### Ajouté

- Indicateurs CPU et RAM avec barres de progression.
- Détection automatique des disques physiques connectés.
- Affichage du nom, de la capacité et de l'occupation des disques montés.
- Température du processeur Intel avec repli sur `hwmon`.
- Température de la carte graphique NVIDIA via `nvidia-smi`.
- État réseau obtenu localement auprès de NetworkManager.
- Détection automatique de l'interface réseau active.
- Affichage de l'adresse IPv4 locale.
- Mesure en temps réel des débits descendant et montant.
- Raccourcis vers PatSecure, Deepin Terminal et le gestionnaire de fichiers.
- Styles distincts pour les ressources, les disques, les températures, le réseau et les boutons.

### Modifié

- Fenêtre agrandie uniquement vers le bas afin de conserver sa position supérieure.
- Position validée sur l'écran `DP-0` avec un décalage horizontal de `-120px`.
- Lanceur Eww corrigé pour utiliser la configuration `~/.config/patdesk` dès le démarrage du daemon.
- Scripts CPU et RAM rendus indépendants de `mpstat`.
- Entrée de démarrage automatique rendue portable avec `$HOME`.

### Confidentialité et sécurité

- Aucun relevé d'adresse IP publique.
- Masquage automatique d'une éventuelle adresse IPv4 publique directement attribuée.
- Aucune adresse personnelle écrite en dur.
- Aucun port ouvert et aucun serveur réseau créé.
- Aucune télémétrie ou transmission de données.
- État d'Internet lu depuis NetworkManager sans cible IP externe fixe.

## [0.1.0]

- Première version avec horloge et date.
- Première présentation Eww en haut à droite du bureau.
