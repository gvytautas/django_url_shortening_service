from django.shortcuts import render, redirect, get_object_or_404, HttpResponse, reverse
from django.contrib import messages
from django.conf import settings
from .forms import UrlForm
from .models import Url
from .business_layer.short_url_generator import ShortUrlGenerator
import requests
import time


# Create your views here.
def index(request):
    if request.method == 'POST':
        short_url = ShortUrlGenerator(settings.SHORT_URL_LENGTH).generate_short_url()
        form = UrlForm(data={
            'ip_address': request.META.get('REMOTE_ADDR'),
            'http_referer': request.META.get('HTTP_REFERER') or 'abc',
            'short_url': short_url,
            'url': request.POST.get('url')
        })
        if form.is_valid():
            form.save()
            messages.info(request, f'Short url: {short_url}')
            return redirect('index')
        return render(request, 'index.html', context={'form': form})
    form = UrlForm()
    return render(request, 'index.html', context={'form': form})


def resolve(request, short_url: str):
    url = get_object_or_404(Url, short_url=short_url)
    if not url.is_active:
        return HttpResponse('Url deactivated', status=404)
    url.number_of_clicks += 1
    url.save()
    return redirect(url.url, permanent=False)


def benchmark(request):
    if request.method == 'POST':
        test_items = int(request.POST.get('sample_size'))
        long_url = request.POST.get('long_url')
        if test_items > 0:
            dummy_data = [
                {
                    'short_url': ShortUrlGenerator(settings.SHORT_URL_LENGTH).generate_short_url(),
                    'url': long_url,
                    'http_referer': 'test',
                    'ip_address': 'test'
                } for _i in range(test_items)
            ]
            for item in dummy_data:
                Url.objects.create(**item)
            urls = Url.objects.filter(ip_address='test').all()
            resolve_times = []
            direct_times = []
            for url in urls:
                t0 = time.time()
                requests.get(url='http://' + request.META.get('HTTP_HOST') + f'/{url.short_url}')
                resolve_times.append(time.time() - t0)
                url.delete()
                t0 = time.time()
                requests.get(url=long_url)
                direct_times.append(time.time() - t0)
            average_redirect_time = sum(resolve_times) / len(resolve_times)
            average_direct_time = sum(direct_times) / len(direct_times)
            average_resolve_time = average_redirect_time - average_direct_time
            results = {
                'average_redirect_time': average_redirect_time,
                'average_direct_time': average_direct_time,
                'average_resolve_time': average_resolve_time
            }
            return render(request, 'benchmark.html', context={'results': results})

    return render(request, 'benchmark.html')
