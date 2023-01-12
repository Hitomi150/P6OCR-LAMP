#!/bin/bash

echo "Entrer nom database:"
read dbname

# Create the database

mysql -e "CREATE DATABASE ${dbname};"


# Create user
echo "Enter username:"
read username
echo "Enter password:"
read userpass
mysql -e "CREATE USER ${username}@'localhost' IDENTIFIED BY '${userpass}';"

# Donnée Privileges
mysql -e "GRANT ALL PRIVILEGES ON ${dbname}.* TO ${username}@'localhost';"

mysql -e "FLUSH PRIVILEGES;"
echo "C'est FINI...."

exit
