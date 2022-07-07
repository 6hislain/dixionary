# Dixionary

A (minimal viable product) project for a cloud sourced dictionary

![Screenshot](screenshot.png)

### Requirements

- Python 3
- Git
- Database: Sqlite, Mysql, Postgres

### Installation

- `git clone https://github.com/6hislain/dixionary`
- `cd dixionary`
- `python3 -m venv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- edit `dixionary/settings.py` to match your preference
- `python3 manage.py migrate`
- `python3 manage.py createsuperuser`
- `python3 manage.py runserver`

### Todo

- delete media
- form validation
- better message
- search
