SiteCoursMusique
================

===
DEPENDANCIES
   * django.1.5
   * compare.py
   * twitter bootstrap-3.0.0
   * LESS css engine
   

===
cd /SiteCoursMusique 

python manage.py runserver

browser: http://127.0.0.1:8000/admin

edit database connection string in mysite/settings.py :: DATABASES


===
Unit tests

install coverage:
pip install coverage

run unit tests:
coverage run --source='.' manage.py test <app_name>

get report:
coverage report

