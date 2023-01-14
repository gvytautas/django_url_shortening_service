from django.forms import ModelForm
from .models import Url


class UrlForm(ModelForm):
    class Meta:
        model = Url
        fields = ['short_url', 'url', 'ip_address', 'http_referer']
