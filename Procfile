# release: ./dbmigrations.sh
release: python manage.py makemigrations core --no-input
release: python manage.py migrate --no-input

web: gunicorn api.wsgi