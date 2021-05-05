#!/bin/bash

DATABASE=database/database.db

if [ -f $DATABASE ]; then
    python run.py
else
    python -c "from database.db import create_database; create_database()"
    python run.py
fi