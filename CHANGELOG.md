# Historique des versions de PatDesk

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
