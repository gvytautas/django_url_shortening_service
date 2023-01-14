from django.urls import path
from .views import index, short_url

urlpatterns = [
    path('', index, name='index'),
    path('<slug:short_url>', short_url, name='short_url')
]