#!/usr/bin/env python

import os
import subprocess

print("Installation du serveur LAMP + Wordpress...")

# Mise a jour des paquets
print("Mise a jour de l'OS")

os.system("apt-get update && apt-get upgrade -y")

# Installation de Apache
print("Installation d'apache2")

os.system("apt-get install apache2 -y")

# Installation de MySQL
print("Installation de MySQL")

os.system("apt-get install mariadb-server -y")

# Installation de PHP
print("Installation de PHP")

os.system("apt-get install php libapache2-mod-php php-mysql -y")

print("Installation de Wordpress")
# Telechargement de WordPress
print("Telechargement de Wordpress")
os.system("cd /tmp/")
os.system("wget https://fr.wordpress.org/latest-fr_FR.zip")

# Extraction de WordPress
print("Extration de Wordpress")

os.system("unzip latest-fr_FR.zip")

# Deplacement des fichiers de WordPress dans le repertoire web de Apache
print("Deplacement des fichiers Wordpress dans le repertoire de apache")

os.system("sudo mv wordpress/* /var/www/html")

# Redemarrage d'Apache
print("Redemarrage d'Apache")

os.system("service apache2 restart")

print("... Fin de l'installation du serveur LAMP + Wordpress")


print("Creation de la Database...")

os.system("sudo ./Mysql.sh")

