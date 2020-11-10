# release: ./dbmigrations.sh
release: python manage.py makemigrations core --no-input
# release: python manage.py migrate

web: gunicorn api.wsgi