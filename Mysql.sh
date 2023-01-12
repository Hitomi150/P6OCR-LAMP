#!/bin/bash

# Create the database
mysql -e CREATE DATABASE test;

# Create user
mysql -e CREATE USER 'test'@'localhost' IDENTIFIED BY '1234';

# Donnée Privileges
mysql -e GRANT ALL PRIVILEGES ON test.* TO 'test'@'localhost';

mysql -e FLUSH ALL PRIVILEGES;

