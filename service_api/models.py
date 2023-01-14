from django.db import models
from django.conf import settings


# Create your models here.

class Url(models.Model):
    short_url = models.CharField(max_length=settings.SHORT_URL_LENGTH, primary_key=True)
    url = models.URLField()

    def __str__(self):
        return self.short_url
