release: python manage.py makemigrations core --no-input | python manage.py migrate core --no-input

web: gunicorn api.wsgi