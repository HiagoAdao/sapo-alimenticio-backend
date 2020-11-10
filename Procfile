# release: ./dbmigrations.sh
# release: python manage.py makemigrations core --no-input
release: python manage.py makemigrations core

web: gunicorn api.wsgi