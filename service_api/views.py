import datetime
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib import messages
from django.conf import settings
from .forms import UrlForm
from .models import Url
from .business_layer.short_url_generator import ShortUrlGenerator


# Create your views here.

def index(request):
    if request.method == 'POST':
        short_url = ShortUrlGenerator(settings.SHORT_URL_LENGTH).generate_short_url()
        form = UrlForm(data={
            'ip_address': request.META.get('REMOTE_ADDR'),
            'http_referer': request.META.get('HTTP_REFERER'),
            'short_url': short_url,
            'url': request.POST.get('url')
        })
        if form.is_valid():
            form.save()
            messages.info(request, f'Short url: {short_url}')
            return redirect('index')
    form = UrlForm()
    return render(request, 'index.html', context={'form': form})


def resolve(request, short_url: str):
    url = get_object_or_404(Url, short_url=short_url)
    if not url.is_active:
        return HttpResponse('Url deactivated', status=404)
    url.number_of_clicks += 1
    url.save()
    return redirect(url.url, permanent=False)
