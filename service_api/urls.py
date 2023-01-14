from django.urls import path
from .views import index, resolve

urlpatterns = [
    path('', index, name='index'),
    path('<slug:short_url>', resolve, name='short_url_1'),
    path('<slug:short_url>/', resolve, name='short_url_2')
]