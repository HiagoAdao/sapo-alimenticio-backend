#!/bin/bash

python manage.py makemigrations core --no-input
python manage.py migrate --no-input