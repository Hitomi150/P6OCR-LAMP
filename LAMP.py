#!/usr/bin/env python

import os
import subprocess

print("Installation du serveur LAMP + Wordpress...")

# Mise à jour des paquets
print("Mise a jour de l'OS")

os.system("apt-get update && apt-get upgrade -y")

# Installation de Apache
print("Installation d'apache2")

os.system("apt-get install apache2 -y")

# Installation de MySQL
print("Installation de MySQL")

os.system("apt-get install mysql-server -y")

# Installation de PHP
print("Installation de PHP")

os.system("apt-get install php libapache2-mod-php php-mysql -y")

print("Installation de Wordpress")
# Téléchargement de WordPress
print("Téléchargement de Wordpress")

os.system("wget https://fr.wordpress.org/latest-fr_FR.zip")

# Extraction de WordPress
print("Extration de Wordpress")

os.system("unzip latest-fr_FR.zip")

# Déplacement des fichiers de WordPress dans le répertoire web de Apache
print("Déplacement des fichiers Wordpress dans le répertoire de apache")

os.system("mv wordpress/* /var/www/html")

# Redémarrage d'Apache
print("Redémarrage d'Apache")

os.system("service apache2 restart")

print("... Fin de l'installation du serveur LAMP +Wordpress")
