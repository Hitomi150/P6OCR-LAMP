#!/usr/bin/env python

import os
import subprocess

# Mise à jour des paquets
os.system("apt-get update && apt-get upgrade -y")

# Installation de Apache
os.system("apt-get install apache2 -y")

# Installation de MySQL
os.system("apt-get install mysql-server -y")

# Installation de PHP
os.system("apt-get install php libapache2-mod-php php-mysql -y")

# Téléchargement de WordPress
os.system("wget https://fr.wordpress.org/latest-fr_FR.zip")

# Extraction de WordPress
os.system("unzip latest-fr_FR.zip")

# Déplacement des fichiers de WordPress dans le répertoire web de Apache
os.system("mv wordpress/* /var/www/html")

# Configuration de WordPress
subprocess.call("/var/www/html/wp-admin/setup-config.php")

# Redémarrage d'Apache
os.system("service apache2 restart")