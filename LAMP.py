#!/usr/bin/env python

import os
import subprocess
import mysql.connector

print("Installation du serveur LAMP + Wordpress...")

# Mise a jour des paquets
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
# Telechargement de WordPress
print("Telechargement de Wordpress")

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

# Etablissez une connexion à MySQL
print("Connexion a MySQL")
cnx = mysql.connector.connect(user='root', password='1234', host='localhost')

# Creez un curseur pour exécuter des requêtes SQL
cursor = cnx.cursor()

# Creez une base de données nommée "ma_base_de_donnees"
print("Creation de la database")
cursor.execute("CREATE DATABASE test")

# Créez un utilisateur nommé "mon_utilisateur" avec le mot de passe "mon_mot_de_passe"
print("Creation de l'utilisateur")
cursor.execute("CREATE USER 'test'@'localhost' IDENTIFIED BY '1234'")

# Accordez tous les privilèges à l'utilisateur sur la base de données "ma_base_de_donnees"
print("Accord des privilèges à l'utilisateur")
cursor.execute("GRANT ALL PRIVILEGES ON test.* TO 'test'@'localhost'")

# Enregistrez les modifications
print("Enregistrez les modifications")
cnx.commit()

# Fermez la connexion
cnx.close()

print("Fin de la création de la database")
