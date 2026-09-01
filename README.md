# PatDesk

**PatDesk** est un tableau de bord système pour **Deepin Linux**, construit avec **Eww (ElKowar's Wacky Widgets)**.

Il propose une alternative légère et personnalisable à Rainmeter, directement intégrée au bureau Linux.

## Version actuelle

**PatDesk v0.6.0 — 1er septembre 2026**

## Fonctions

- horloge et date en temps réel ;
- météo locale : condition, température, ressenti, vent, mini/maxi du jour et risque de pluie ;
- utilisation du processeur et de la mémoire RAM ;
- liste automatique des disques physiques connectés ;
- capacité et taux d'occupation des disques montés ;
- températures du processeur Intel et de la carte graphique NVIDIA ;
- alertes visuelles vertes, orange et rouges selon le remplissage des disques et les températures ;
- état de la connexion réseau ;
- type d'interface, adresse IPv4 locale et débits descendant/montant ;
- état des mises à jour disponibles d'après le cache APT local, sans lancer `apt update` ;
- voyant **PatSecure** vert, orange, rouge ou gris selon le dernier audit partageable ;
- musique en cours via MPRIS/playerctl : lecture/pause, lecteur, titre et artiste ;
- raccourcis vers PatSecure, Deepin Terminal, le gestionnaire de fichiers, le site Les projets de Pattoo et ChatGPT ;
- lancement automatique avec Deepin.

## Météo

Le bloc **MÉTÉO** utilise Open-Meteo par HTTPS, sans clé API et sans géolocalisation par IP.

La localisation est configurée uniquement en local dans `~/.config/patdesk/weather.conf` :

```text
CITY=VotreVille
COUNTRY_CODE=FR
```

Ce fichier personnel ne doit pas être ajouté au dépôt. Le nom de la ville n'est pas affiché dans le panneau PatDesk. Si aucune ville n'est configurée, aucune requête météo n'est envoyée.

Comme pour toute requête HTTPS, le fournisseur météo voit techniquement l'adresse IP source de la connexion. PatDesk ne recherche, n'affiche ni n'enregistre cette adresse.

## Musique en cours

Le bloc **MUSIQUE EN COURS** utilise MPRIS avec `playerctl` et reste entièrement local.

Il affiche :

- lecture ou pause ;
- lecteur détecté ;
- titre ;
- artiste.

PatDesk privilégie un lecteur actuellement en lecture, puis un lecteur en pause. Si aucun lecteur MPRIS n'est disponible, le module affiche simplement `Aucune lecture en cours`.

## État PatSecure

Le bloc **PATSECURE** affiche quatre états :

- **vert** : audit récent sans `ATTENTION` ni `ERREUR` ;
- **orange** : au moins une `ATTENTION` ;
- **rouge** : au moins une `ERREUR` ;
- **gris** : aucun rapport récent, état indisponible ou audit de plus de 7 jours.

Le module `eww/scripts/patsecure-status.py` lit uniquement le dernier rapport **partageable** de PatSecure. Il n'accède jamais au rapport privé et ne lance aucun appel réseau, aucune commande `sudo` ni aucune opération de maintenance.

## Alertes visuelles

- Disques : orange à partir de 75 % d'occupation, rouge à partir de 90 %.
- Processeur : orange à partir de 70 °C, rouge à partir de 85 °C.
- RTX 3060 : orange à partir de 75 °C, rouge à partir de 85 °C.
- Réseau indisponible : état et débits affichés en rouge.
- PatSecure : vert, orange, rouge ou gris selon le dernier audit partageable.

## Mises à jour Deepin

PatDesk affiche un bloc **MISES À JOUR** qui indique soit `Système à jour`, soit le nombre de mises à jour disponibles, soit `État indisponible`.

Ce contrôle :

- utilise uniquement `apt list --upgradable` ;
- s'appuie sur le cache APT local ;
- ne lance pas `apt update` ;
- n'installe rien ;
- ne demande pas les droits administrateur ;
- est actualisé dans Eww toutes les 10 minutes.

## Confidentialité et sécurité réseau

PatDesk reste conçu pour limiter les données sensibles :

- aucune adresse IP publique n'est recherchée ou affichée ;
- l'adresse réseau affichée par PatDesk est uniquement une adresse IPv4 privée de l'interface active ;
- une éventuelle adresse IPv4 publique directement attribuée est automatiquement masquée ;
- aucune adresse personnelle n'est écrite en dur dans le code ;
- aucun port réseau n'est ouvert ;
- aucun serveur distant n'est lancé ;
- aucune télémétrie n'est ajoutée ;
- le module musique reste entièrement local ;
- le voyant PatSecure ne consulte que le rapport partageable ;
- seule la météo nécessite un accès HTTPS distant lorsque l'utilisateur a explicitement configuré une ville locale.

## Environnement testé

- Deepin 25 ;
- Eww 0.6.0 ;
- Python 3 ;
- `playerctl` 2.4.1 pour le module musique ;
- processeur Intel Core i7-11700K ;
- carte graphique NVIDIA GeForce RTX 3060 ;
- configuration à deux écrans sous X11.

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

Pour le module musique :

```bash
sudo apt install playerctl
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
│       ├── network.py
│       ├── updates.py
│       ├── patsecure-status.py
│       ├── weather.py
│       └── media.py
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
