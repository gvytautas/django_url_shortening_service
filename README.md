# django_url_shortening_service

## Installation
```commandline
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
```

## Running
To run application, enter in terminal:
```commandline
python manage.py runserver
```

## Benchmarking
*benchmark* page is available to test resolve time.

## Notes
+ Application was built on Python 3.11
+ No check for short url uniqueness implemented since 62^7 gives over 3.5 trillion unique combinations.
+ To increase speed of URL resolving:
  + to avoid unnecessary redirects in application, both versions of urls were implemented, with and without trailing "/".
  + short_url was set as primary key in Database, which by default should be indexed and therefore select by it as fast as it can be.
+ 3rd party libraries: Django, requests
+ Considered option for random string generation:
  + secrets - generates most random numbers -> preferred due requirements
  + random - generates pseudo random numbers