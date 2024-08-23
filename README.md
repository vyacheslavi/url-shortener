# Django, DRF, web app to shorten links


## Stack

* backend: Django, Django Rest Framework

* db: SQLite3

* frontend: Jinja2Templates, CSS, HTML, JavaScript


## A few steps for cloning and run project

1) clone the project

`git clone https://github.com/erinallard/instagram_miner.git`

2) create and start a a virtual environment

`virtualenv env --no-site-packages`

`source env/bin/activate`

3) Install the project dependencies:

`pip install -r requirements.txt`

4) then run

`python manage.py migrate`

5) create admin account

`python manage.py createsuperuser`

6) then to makemigrations for the app

`python manage.py makemigrations`

7) then again run

`python manage.py migrate`

8) to start the development server

`python manage.py runserver`

9) and open localhost:8000 on your browser to view the app.

