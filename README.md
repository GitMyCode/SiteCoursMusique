SiteCoursMusique
================

===
DEPENDANCIES
   * django.1.5
   * compare.py
   * twitter bootstrap-3.0.0
   * LESS css engine
   

===
cd /SiteCoursMusique/mysite
cp conf.py.edit conf.py

ensuite editer DATABASES dans conf.py 
 aussi nommé son fichier db ou dev.db pour qu'il ne soit pas commit (gitignore)

cd ..
./manage.py syncdb
./ manage.py runserver

browser: http://127.0.0.1:8000/admin


===
Unit tests

install coverage:
pip install coverage

run unit tests:
coverage run --source='.' manage.py test <app_name>

get report:
coverage report

