# Installation de PatDesk

## Prérequis

- Deepin Linux 25 ;
- Eww 0.6.0 ou compatible ;
- Bash ;
- Python 3 ;
- `lm-sensors` pour la température du processeur ;
- `nvidia-smi` pour la température d'une carte NVIDIA.

Les fonctions dont les outils sont absents restent sans effet ou affichent une valeur neutre.

## Installation depuis GitHub

```bash
git clone https://github.com/PattooDev/PatDesk.git
cd PatDesk
```

Créer la configuration :

```bash
mkdir -p "$HOME/.config/patdesk/scripts"
```

Installer l'interface et les scripts :

```bash
install -m 644 eww/eww.yuck "$HOME/.config/patdesk/eww.yuck"
install -m 644 eww/eww.scss "$HOME/.config/patdesk/eww.scss"
install -m 755 eww/scripts/* "$HOME/.config/patdesk/scripts/"
install -m 755 launch/patdesk.sh "$HOME/.config/patdesk/launch.sh"
```

Installer le démarrage automatique :

```bash
install -Dm 644 autostart/patdesk.desktop "$HOME/.config/autostart/patdesk.desktop"
```

## Premier lancement

```bash
bash "$HOME/.config/patdesk/launch.sh"
```

## Adapter l'écran

Dans `~/.config/patdesk/eww.yuck`, modifier si nécessaire :

```text
:monitor "DP-0"
:anchor "top right"
:x "-120px"
:y "20px"
```

La commande suivante affiche les noms d'écrans disponibles :

```bash
xrandr --query | grep " connected"
```

## Désactivation

Fermer PatDesk :

```bash
eww --config "$HOME/.config/patdesk" close patdesk
```

Désactiver le lancement automatique :

```bash
mv "$HOME/.config/autostart/patdesk.desktop" "$HOME/.config/autostart/patdesk.desktop.disabled"
```

