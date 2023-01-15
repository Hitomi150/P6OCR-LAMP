# P6OCR-LAMP

[![forthebadge](http://forthebadge.com/images/badges/built-with-love.svg)](http://forthebadge.com)  [![forthebadge](http://forthebadge.com/images/badges/powered-by-electricity.svg)](http://forthebadge.com)


## But de projet

Ce projet consiste à automatiser l'installation d'un serveur LAMP+wordpress et la création d'une base de donnée.

### Pré-requis

Ce qu'il est requis pour commencer avec votre projet...

- Installé python
- Donnée les droits d'execution au fichier Mysql.sh avec la commande "chmod -R 777 /etc/cron.d/Mysql.sh"

### Installation

Pour installer le script il faut:

-Télécharger les fichier LAMP.py et Mysql.sh

### Executer le script

Executer la commande "python LAMP.py" et le script va s'éxectuer dans son ensemble.

Le script va:

-Mettre à jour l'os (testé sous debian 10)
-Installer Apache
-Installer MySQL
-Installer PHP
-Télécharger wordpress
-Proceder a l'extraction du l'archive wordpress dans ça derniere version en français (latest-fr-FR.zip)
-Déplacer les fichier de wordpress dans le repertoire web de Apache (/war/www/html)
-Redémarrer le service Apache
-Faire appel au script Mysql.sh pour créer une database et un utilisateur


## Fabriqué avec

[SublimeText](https://www.sublimetext.com/) - Editeur de textes


## Versions
Dernière version : 1.0


## Auteurs

DAMOND Greg _alias_ [@Hitomi150](https://github.com/Hitomi150)


## License

Ce projet est sous licence ``GNU General Public License v3.0`` - voir le fichier [LICENSE](LICENSE) pour plus d'informations

