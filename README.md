# django_url_shortening_service

## Installation
```commandline
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
```

## Usage
To run application, enter in terminal:
```commandline
python manage.py runserver
```

## Notes
+ No check for short url uniqueness implemented since 62^7 gives over 3.5 trillion unique combinations.