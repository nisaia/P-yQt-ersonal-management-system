#!/bin/bash

#CREATE VIRTUAL ENVIROMENT
echo "Creating virtual enviroment"
python3 -m venv virtual_enviroment

#INSTALL DEPENDENCIES

echo "Installing dependencies"
sleep 3
pip install -r requirements.txt

#CREATE DATABASE ENGINE

echo "Creating database engine"
sleep 3
python3 -c "from database.db import create_database; create_database()"