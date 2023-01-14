from django.db import models
from django.conf import settings
import datetime


# Create your models here.

class Url(models.Model):
    short_url = models.CharField(max_length=settings.SHORT_URL_LENGTH, primary_key=True)
    url = models.URLField()
    active = models.BooleanField(default=True)
    time_created = models.DateTimeField(auto_now_add=True)
    ip_address = models.CharField(max_length=50)
    http_referer = models.CharField(max_length=50)
    expiration_time = models.DateTimeField(null=True, blank=True)
    number_of_clicks = models.IntegerField(default=0)

    @property
    def is_active(self) -> bool:
        if self.expiration_time:
            return self.active and datetime.datetime.now() < self.expiration_time
        if settings.MAXIMUM_NUMBER_OF_CLICKS <= self.number_of_clicks:
            return False
        return bool(self.active)

    def __str__(self):
        return self.short_url
