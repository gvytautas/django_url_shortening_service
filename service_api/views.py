from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UrlForm
from .models import Url
import secrets


# Create your views here.

def index(request):
    if request.method == 'POST':
        chars = 'QWERTZUIOPASDFGHJKLYXCVBNMqwertzuiopasdfghjklyxcvbnm0123456789'  # noqa
        short_url = ''.join(secrets.choice(chars) for i in range(7))
        form = UrlForm(data={
            'short_url': short_url,
            'url': request.POST.get('url')
        })
        if form.is_valid():
            form.save()
            messages.info(request, f'Short url: {short_url}')
            return redirect('index')

    form = UrlForm()

    return render(request, 'index.html', context={'form': form})


def short_url(request, short_url):
    url = get_object_or_404(Url, short_url=short_url)
    return redirect(url.url)
