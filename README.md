SiteCoursMusique
================

===
DEPENDANCIES
   * django.1.5.4
   * south
   * compare.py
   * twitter bootstrap-3.0.0
   * LESS css engine
   * django-photologue   

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
install photologue

-- start virtual env : source /<virtual_env_name>/bin/activate
-- pip install django-photologue
-- add to list of installed apps
-- add photologue urls to project's urls
-- if first time running: python manage.py schemamigration photologue --initial
   python manage.py syncdb
   python manage.py migrate photologue

--  else : python manage migrate photologue. You are done



===
Unit tests

install coverage:
pip install coverage

run unit tests:
coverage run --source='.' manage.py test <app_name>

get report:
coverage report

