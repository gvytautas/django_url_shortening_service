# syntax=docker/dockerfile:1
FROM python:3.11-alpine
WORKDIR /project
RUN apk add --no-cache gcc musl-dev linux-headers
COPY . .
RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate
EXPOSE 5000
CMD ["gunicorn", "django_url_shortening_service.wsgi"]