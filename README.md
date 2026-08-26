# PatDesk

**PatDesk** est un tableau de bord système pour **Deepin Linux**, construit avec **Eww (ElKowar's Wacky Widgets)**.

Il propose une alternative légère et personnalisable à Rainmeter, directement intégrée au bureau Linux.

## Version actuelle

**PatDesk v0.2.0 — 25 août 2026**

## Fonctions

- horloge et date en temps réel ;
- utilisation du processeur et de la mémoire RAM ;
- liste automatique des disques physiques connectés ;
- capacité et taux d'occupation des disques montés ;
- températures du processeur Intel et de la carte graphique NVIDIA ;
- état de la connexion réseau ;
- type d'interface, adresse IPv4 locale et débits descendant/montant ;
- raccourcis vers PatSecure, Deepin Terminal et le gestionnaire de fichiers ;
- lancement automatique avec Deepin.

## Confidentialité et sécurité réseau

PatDesk fonctionne localement :

- aucune adresse IP publique n'est recherchée ou affichée ;
- l'adresse affichée est uniquement une adresse IPv4 privée de l'interface active ;
- une éventuelle adresse IPv4 publique directement attribuée est automatiquement masquée ;
- aucune adresse personnelle n'est écrite en dur dans le code ;
- aucun port réseau n'est ouvert ;
- aucun serveur distant n'est lancé ;
- aucune télémétrie ou donnée personnelle n'est envoyée ;
- l'état d'Internet provient des informations locales de NetworkManager.

## Environnement testé

- Deepin 25 ;
- Eww 0.6.0 ;
- Bash et Python 3 ;
- processeur Intel Core i7-11700K ;
- carte graphique NVIDIA GeForce RTX 3060 ;
- configuration à deux écrans sous X11.

Les capteurs de température restent automatiquement tolérants : une valeur de `0` est affichée si le matériel ou la commande attendue n'est pas disponible.

## Installation

```bash
git clone https://github.com/PattooDev/PatDesk.git
cd PatDesk

mkdir -p "$HOME/.config/patdesk/scripts"
install -m 644 eww/eww.yuck "$HOME/.config/patdesk/eww.yuck"
install -m 644 eww/eww.scss "$HOME/.config/patdesk/eww.scss"
install -m 755 eww/scripts/* "$HOME/.config/patdesk/scripts/"
install -m 755 launch/patdesk.sh "$HOME/.config/patdesk/launch.sh"
install -Dm 644 autostart/patdesk.desktop "$HOME/.config/autostart/patdesk.desktop"
```

Lancer PatDesk :

```bash
bash "$HOME/.config/patdesk/launch.sh"
```

## Position de la fenêtre

La configuration actuelle utilise :

- écran `DP-0` ;
- ancrage `top right` ;
- décalage horizontal `-120px` ;
- décalage vertical `20px`.

Ces valeurs se modifient dans `eww/eww.yuck` pour s'adapter à une autre organisation d'écrans.

## Organisation du dépôt

```text
PatDesk/
├── AGENTS.md
├── README.md
├── CHANGELOG.md
├── eww/
│   ├── eww.yuck
│   ├── eww.scss
│   └── scripts/
│       ├── cpu.sh
│       ├── ram.sh
│       ├── disks.py
│       ├── cpu-temp.sh
│       ├── gpu-temp.sh
│       └── network.py
├── launch/
│   └── patdesk.sh
├── autostart/
│   └── patdesk.desktop
└── docs/
    ├── INSTALL.md
    └── SUIVI_PATDESK.md
```

## Continuer le projet sans perdre le fil

Le fichier [`docs/SUIVI_PATDESK.md`](docs/SUIVI_PATDESK.md) conserve le point de reprise commun entre ChatGPT Work et le chat normal. Les consignes de travail et de sécurité destinées aux prochaines sessions sont dans [`AGENTS.md`](AGENTS.md).

## Projet

Projet développé par **PattooDev** pour Deepin Linux.
