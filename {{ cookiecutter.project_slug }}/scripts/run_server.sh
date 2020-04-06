#!/bin/sh

python scripts/wait_for_postgres.py
./manage.py migrate
./manage.py runserver 0.0.0.0:8000
