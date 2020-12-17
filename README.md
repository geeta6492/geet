# scalepost
Cross platform post publishing..

Requirements
Virtual Environment (virtualenv, venv, pipenv, etc)
Django installed & project created.
Setup:
What you need for a basic Django dev environment:

Python 3.8
easy_install and Pip
Git
virtualenv
Django
Database (SQLite, MySQL, PostgreSQL, MongoDB, etc.)
Text editor (Sublime, PyCharm).
Python
$ python -V python 3.8.6

easy_install and pip
$ easy_install pip

Git
$ git --version

Installing PostgreSQL
Windows and macOS X users can download PostgreSQL from the official site https://www.postgresql.org/download/ and simply install it.

Linux User sudo apt-get install postgresql postgresql-contrib Also, Linux users need to install some dependencies for PostgreSQL to work with Python.

sudo apt-get install libpq-dev python3-dev Install psycopg2

Next, we need to install the PostgreSQL database adapter to communicate to the database with Python to install it run the following command in the shell. pip install psycopg2

virtualenv
$ pip install virtualenv

Django Install
Set up your development structure:

$ mkdir django15_project $ cd django15_project $ virtualenv env $ source env/bin/activate

Project setup
$ django-admin.py startproject my_django15_project

├── manage.py └── my_app_project ├── init.py ├── settings.py ├── urls.py └── wsgi.py

Set up your Django app
$ python manage.py startapp myapp Your project structure should now look like this:

├── manage.py ├── my_app_project │ ├── init.py │ ├── settings.py │ ├── urls.py │ └── wsgi.py └── myapp ├── init.py ├── models.py ├── tests.py └── views.py

migrate django app
$ python manage.py migrate myapp_project

Launch the development server:
$ python manage.py runserver
