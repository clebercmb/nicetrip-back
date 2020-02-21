# nicetrip-back


# Install

Pip install pipenv
Python -m pip install --upgrade pip

# Create Virtual Environment  - It will create Pipfile
pipenv shell 

# Install in the virtual environment
pipenv install flask flask-sqlalchemy flask-script flask-migrate flask-cors

# Create database 
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py db upgrade

# execute the server
python .\app.py runserver
