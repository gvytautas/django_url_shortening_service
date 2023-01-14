from django.db import models


# Create your models here.

class Url(models.Model):
    short_url = models.CharField(max_length=10, primary_key=True)
    url = models.URLField()
