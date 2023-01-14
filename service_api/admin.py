from django.contrib import admin
from .models import Url


# Register your models here.
class UrlAdmin(admin.ModelAdmin):
    list_display = ['short_url', 'url', 'time_created', 'ip_address', 'http_referer', 'is_active', 'number_of_clicks']


admin.site.register(Url, UrlAdmin)
