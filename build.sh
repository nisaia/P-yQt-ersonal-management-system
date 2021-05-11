#!/bin/bash

GREEN="\e[31m"
END_COLOR="\e[0m"
venv='virtual_enviroment'

#CREATE VIRTUAL ENVIROMENT
echo -e "${GREEN}Creating virtual enviroment...${END_COLOR}"
sleep 3
python3 -m venv $venv

#INSTALL DEPENDENCIES

echo -e "${GREEN}Installing dependencies...${END_COLOR}"
sleep 3
. $venv/bin/activate
echo -e "${GREEN}Upgrading pip command...${END_COLOR}"
python -m pip install --upgrade pip
pip install -r requirements.txt

#CREATE DATABASE ENGINE

echo -e "${GREEN}Creating database engine...${END_COLOR}"
sleep 3
python3 -c "from database.db import create_database; create_database()"