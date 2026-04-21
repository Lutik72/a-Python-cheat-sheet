python -m venv .venv
. .venv/Scripts/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py test apps.users -v2
cd coffee_area
python manage.py runserver