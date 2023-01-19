# P6OCR-LAMP

[![forthebadge](http://forthebadge.com/images/badges/built-with-love.svg)](http://forthebadge.com)  [![forthebadge](http://forthebadge.com/images/badges/powered-by-electricity.svg)](http://forthebadge.com)


## But de projet

Ce projet consiste à automatiser l'installation d'un serveur LAMP+wordpress et la création d'une base de données.

### Pré-requis

- Installer python3
- Donner les droits d'exécution au fichier Mysql.sh avec la commande "chmod -R 777 /etc/cron.d/Mysql.sh"

### Installation

Pour installer le script il faut:

- Télécharger les 2 Scripts LAMP.py et Mysql.sh

### Exécuter le script

Exécuter la commande "python LAMP.py" et le script va s'exéctuer dans son ensemble.

Le script LAMP.py va:

- Mettre à jour l'os (testé sous debian 10)

- Installer la derniere version d'Apache (2.4.38)

- Installer la derniere version de mariadb-server (10.3.34)

- Installer la derniere version de PHP (7.3)

- Télécharger la derniere version de wordpress (latest-fr-FR.zip)

- Procéder a l'extraction de l'archive wordpress dans ça dernière version en français (latest-fr-FR.zip)

- Déplacer les fichiers de wordpress dans le répertoire web d'Apache (/war/www/html)

- Redémarrer le service Apache

- Faire appel au script Mysql.sh pour créer une database et un utilisateur

Le script Mysql.sh est interactif. Ce qui implique le renseignement du nom de la database, de l'utilisateur de la database ainsi que le mot de passe.

## Fabriqué avec

[SublimeText](https://www.sublimetext.com/) - Editeur de textes


## Versions
Dernière version du projet : 1.0

Dernière version LAMP.py : 1.0

Dernière version Mysql.sh : 1.0


## Auteurs

DAMOND Greg _alias_ [@Hitomi150](https://github.com/Hitomi150)


## License

Ce projet est sous licence ``GNU General Public License v3.0`` - voir le fichier [LICENSE](LICENSE) pour plus d'informations

