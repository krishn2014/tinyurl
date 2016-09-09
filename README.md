# tinyurl

Simple django webapp to shorten url. Similar to tinyurl.

To deploy the app locally follow the following steps:

1. create a database with name 'demo'
2. run `python manage.py syncdb` from wsgi/project folder to synch database
3. run `python manage.py runserver` to start the server
4. visit `http://localhost:8000/tinyurl/` to shorten a given url

One can also deploy the project on Openshift.
