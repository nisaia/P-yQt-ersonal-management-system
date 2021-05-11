#!/bin/bash

#CREATE VIRTUAL ENVIROMENT
echo "Creating virtual enviroment..."
sleep 3
python3 -m venv virtual_enviroment

#ACCESS INTO VIRTUAL ENVIROMENT
echo "Access into virtual enviroment..."
sleep 3
. virtual_enviroment/bin/activate


#INSTALL DEPENDENCIES

echo "Installing dependencies..."
sleep 3
pip install -r requirements.txt

#CREATE DATABASE ENGINE

echo "Creating database engine..."
sleep 3
python3 -c "from database.db import create_database; create_database()"