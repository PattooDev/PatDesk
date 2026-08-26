# Point de reprise PatDesk

Dernière mise à jour : **26 août 2026**

Ce fichier est le carnet de bord commun à ChatGPT Work et au chat normal. Il doit être lu au début d'une reprise et actualisé à la fin de chaque évolution importante.

## Phrase de reprise

> Reprends PatDesk en lisant `AGENTS.md` et `docs/SUIVI_PATDESK.md`, puis vérifie l'état réel de `main` avant toute modification.

## État publié

- Dépôt : [PattooDev/PatDesk](https://github.com/PattooDev/PatDesk)
- Version : **0.2.0**
- Branche publiée : `main`
- Commit fonctionnel publié : `424f1ced209a4628439f8da4e37bbb9692158f9f`
- Arbre Git vérifié : `cd8691bd536e7a6b08ef4f4f529bc1f9ea08792e`
- Date de publication : **25 août 2026**

## Branche de test historique

- Branche : `patdesk-disques-test`
- Dernier commit : `cb6ca7b35e47a2602dad0f8cc8c98a715c54bf72`
- Juste avant l'ajout des documents de continuité le 26 août 2026, son code était identique à celui de `main`.
- `main` contient désormais `AGENTS.md`, ce carnet de bord et les liens ajoutés au README ; il n'existe toujours aucune différence fonctionnelle dans PatDesk v0.2.0.
- Les historiques divergent parce que `main` a reçu un commit de publication unique. Il ne faut donc pas fusionner cette branche par réflexe.

## Fonctions terminées

- Horloge et date.
- Mesures CPU et RAM.
- Détection automatique des disques physiques, capacité et occupation.
- Températures CPU Intel et GPU NVIDIA.
- État du réseau, interface active, IPv4 locale privée et débits.
- Raccourcis vers PatSecure, Deepin Terminal et le gestionnaire de fichiers.
- Démarrage automatique sous Deepin.
- Documentation d'installation et historique de version.

## Validations déjà obtenues

- Pattoo a confirmé le **25 août 2026** que les trois raccourcis fonctionnent.
- Le **26 août 2026**, les deux branches ont été comparées avant l'ajout de ce carnet : tous les fichiers fonctionnels et leurs empreintes étaient identiques.
- Le script réseau a été relu :
  - il utilise seulement les informations locales de Linux et NetworkManager ;
  - il ne contacte aucun service Internet ;
  - il n'ouvre aucun port et ne lance aucun serveur ;
  - il retourne une IPv4 seulement si Python la classe comme privée, sinon il affiche `masquée`.
- Le dépôt ne contient actuellement aucune automatisation CI ; les validations visuelles Eww restent donc manuelles sur le PC Deepin de Pattoo.

## Sécurité à préserver

PatDesk doit rester local. Aucune adresse IP publique, donnée personnelle, télémétrie, cible distante fixe ou information exploitable de l'extérieur ne doit être ajoutée au code, à la documentation, au site ou aux captures.

## Publication du site

- La fiche PatDesk du site [Les projets de Pattoo](https://projets-pattoo.patrickventresque.chatgpt.site) a été mise à jour et sa publication vérifiée le **26 août 2026**.
- Elle présente la version 0.2.0, le lien GitHub et les fonctions validées.
- Aucune adresse IP publique ni donnée exploitable de l'extérieur n'y a été publiée.

## Prochaines actions connues

1. Utiliser un même projet ChatGPT nommé **PatDesk** pour les conversations Chat et Work.
2. Garder ce dépôt et ce fichier comme source de vérité lorsque Work atteint son quota.
3. Avant la prochaine évolution fonctionnelle, choisir une tâche précise puis la développer sur une nouvelle branche de test.

## Règle de fin de session

Avant de s'arrêter, remplacer les informations devenues obsolètes dans ce fichier et noter clairement la prochaine action. Ne jamais y inscrire de mot de passe, jeton, adresse personnelle ou autre secret.
